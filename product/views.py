from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages
import csv
from .models import Product, Category


@staff_member_required
def upload_csv(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        try:
            # Decode and read the CSV file
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.reader(decoded_file)

            # Extract headers
            headers = next(reader)
            print(headers)
            # Ensure headers are mapped correctly
            name_idx = headers.index("name")
            has_analysis_idx = headers.index("hasAnalysis")
            url_idx = headers.index("url")
            change_idx = headers.index("change")
            categories_idx = headers.index("categories")

            for row in reader:
                # Access fields by index
                name = row[name_idx].strip()
                has_analysis = row[has_analysis_idx].strip().lower() == "true"
                url = row[url_idx].strip() if row[url_idx].strip() else None
                change = row[change_idx].strip()
                try:
                    change = int(change)
                except ValueError:
                    change = 0  # Default to 0 if invalid

                categories_str = row[categories_idx].strip()
                categories = []
                if categories_str:
                    category_names = categories_str.split(",")
                    for name in category_names:
                        name = name.strip()
                        if name:
                            category, _ = Category.objects.get_or_create(name=name)
                            categories.append(category)

                # Create the Product object
                product = Product.objects.create(
                    name=name,
                    has_analysis=has_analysis,
                    url=url,
                    change=change,
                )
                product.categories.set(categories)

            # Success message
            messages.success(
                request, "CSV file uploaded and data imported successfully."
            )
        except Exception as e:
            # Error message
            messages.error(request, f"An error occurred: {e}")
        return redirect("admin:product_product_changelist")

    # Render the upload form if not POST
    return render(request, "admin/product/product/upload_csv.html")
