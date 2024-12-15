import graphene
from graphene_django.types import DjangoObjectType
from .models import Category, Product


# Define GraphQL types for the models
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "products")


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "has_analysis", "url", "change", "categories", "last_updated")


# Define Queries
class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)
    recently_updated_products = graphene.List(
        ProductType, max=graphene.Int(required=True)
    )

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_recently_updated_products(root, info, max):
        return Product.objects.order_by("-last_updated")[:max]


# Define the schema
schema = graphene.Schema(query=Query)
