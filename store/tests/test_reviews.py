import pytest
from store.models import Product, ReviewRating, Category
from account.models import Account

@pytest.mark.django_db
def test_average_and_count_reviews():
    # Create a category and product
    category = Category.objects.create(category_name="Tshirt", slug="tshirt")
    product = Product.objects.create(
        product_name="tshirt oversize",
        slug="oversize_tshirt",
        description="New tshirt",
        price=100.00,
        stock=5,
        category=category,
        is_available=True,
    )

    # Create two users
    user1 = Account.objects.create_user(
        first_name="Mootez", last_name="Aouinti", username="mootez", email="mootez@test.com", password="123"
    )
    user2 = Account.objects.create_user(
        first_name="dorra", last_name="Nsir", username="dorra", email="dorra@test.com", password="123"
    )

    # Create reviews
    ReviewRating.objects.create(product=product, user=user1, subject="Good", review="Nice phone", rating=4, status=True)
    ReviewRating.objects.create(product=product, user=user2, subject="Excellent", review="Perfect", rating=5, status=True)

    # ✅ Test average and count
    assert product.countReview() == 2
    assert round(product.averageReview(), 1) == 4.5
