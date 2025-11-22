import pytest
from store.models import Product, Category

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(category_name="Tshirts", slug="tshirts")
    product = Product.objects.create(
        product_name="Tshirt",
        slug="shirts",
        description="nice Tshirt",
        price=100.00,
        stock=5,
        category=category,
        is_available=True,
    )

    assert product.product_name == "Tshirt"
    assert product.category.category_name == "Tshirts"
    assert product.is_available is True
    assert float(product.price) == 100.00
