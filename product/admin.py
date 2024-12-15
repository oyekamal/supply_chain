from django.contrib import admin
from product.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # Display the ID and name of the category
    search_fields = ("name",)  # Add a search bar to search categories by name
    ordering = ("name",)  # Default ordering by name


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'has_analysis', 'change', 'last_updated')  # Display key fields in the product list
#     list_filter = ('has_analysis', 'change', 'categories')  # Add filters for these fields in the sidebar
#     search_fields = ('name', 'categories__name')  # Enable search by product name and category name
#     ordering = ('-last_updated',)  # Default ordering by last updated (newest first)
#     autocomplete_fields = ('categories',)  # Enable autocomplete for categories in the admin form
#     list_editable = ('has_analysis', 'change')  # Allow inline editing of these fields in the product list
#     date_hierarchy = 'last_updated'  # Add a date hierarchy filter for `last_updated`


from django.contrib import admin
from django.urls import path
from .models import Product
from .views import upload_csv

# Unregister the default Product admin
# admin.site.unregister(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "has_analysis",
        "change",
        "last_updated",
    )  # Display key fields in the product list
    list_filter = (
        "has_analysis",
        "change",
        "categories",
    )  # Add filters for these fields in the sidebar
    search_fields = (
        "name",
        "categories__name",
    )  # Enable search by product name and category name
    ordering = ("-last_updated",)  # Default ordering by last updated (newest first)
    autocomplete_fields = (
        "categories",
    )  # Enable autocomplete for categories in the admin form
    list_editable = (
        "has_analysis",
        "change",
    )  # Allow inline editing of these fields in the product list
    date_hierarchy = "last_updated"  # Add a date hierarchy filter for `last_updated`

    def get_urls(self):
        # Get the default URLs
        urls = super().get_urls()
        # Add custom URLs
        custom_urls = [
            path(
                "upload_csv/",
                self.admin_site.admin_view(upload_csv),
                name="product_product_upload_csv",
            ),
        ]
        # Return custom URLs first
        return custom_urls + urls
