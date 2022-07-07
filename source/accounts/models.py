from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", on_delete=models.CASCADE,
                                verbose_name='Профиль')
    phone_number = PhoneNumberField(region="KG", max_length=13)
    email = models.EmailField(blank=False, null=False, verbose_name="Email")
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Фамилия")

    def str(self):
        return f"Profile: {self.user} : {self.id} : {self.last_name} : {self.first_name} : {self.phone_number}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = []
