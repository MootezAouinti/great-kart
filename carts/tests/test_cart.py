import pytest
from carts.models import Cart, CartItem
from store.models import Product, Category

@pytest.mark.django_db
def test_add_cart_item():
    category = Category.objects.create(category_name="Books", slug="books")
    product = Product.objects.create(
        product_name="Novel",
        slug="novel",
        description="Fiction Book",
        price=10.00,
        stock=10,
        category=category,
        is_available=True,
    )

    cart = Cart.objects.create(cart_id="test123")
    item = CartItem.objects.create(product=product, cart=cart, quantity=3, is_active=True)

    assert item.sub_total() == 30.00
    assert str(cart) == "test123"
