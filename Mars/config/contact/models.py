from django.db import models

class ContactModel(models.Model):
    """класс модели cjntact риложения"""
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField()
    massage = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} - {self.email}'#возврат имени и эмеил


class ContactLink(models.Model):
    """класс модели контактов"""
    icon = models.FileField(upload_to='icons/')#выводит картинку
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


