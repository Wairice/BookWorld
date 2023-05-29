from django.db import models
from django.contrib.auth.models import User


class Bookks(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Художня література'),
        ('sci-fi', 'Наукова фантастика'),
        ('fantasy', 'Фентезі'),
        ('detective', 'Детектив'),
    ]

    title = models.CharField('Назва', max_length=50)
    genre = models.CharField('Жанр', max_length=50, choices=GENRE_CHOICES)
    author = models.CharField('Автор', max_length=50)
    priсe = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    full_text = models.TextField('Опис')
    date = models.DateTimeField('Дата публікації')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книжка'
        verbose_name_plural = 'Книжки'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Bookks, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Bookks, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.book.priсe * self.quantity
