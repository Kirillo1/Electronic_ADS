from django.contrib.auth import get_user_model
from django.test import TestCase

from advertisements.models import Advertisement, Category

User = get_user_model()


class TestCreateAds(TestCase):
    @classmethod
    def test_success_create_ads(cls):
        # создаем автора
        author = User.objects.create_user(username="manager", password="manager")
        author.save()

        # создаем категорию
        category = Category.objects.create(name="Детское")
        category.save()

        # создаем объявление
        test_ads = Advertisement.objects.create(
            title="Test Ads",
            description="Test ads description",
            category=category,
            price=123456,
            author=author,
        )

        print(test_ads)
        test_ads.save()

