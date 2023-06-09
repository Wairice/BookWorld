# Generated by Django 4.2.1 on 2023-05-29 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookks',
            name='available',
        ),
        migrations.RemoveField(
            model_name='bookks',
            name='image',
        ),
        migrations.AlterField(
            model_name='bookks',
            name='genre',
            field=models.CharField(choices=[('fiction', 'Художня література'), ('sci-fi', 'Наукова фантастика'), ('fantasy', 'Фентезі'), ('detective', 'Детектив')], max_length=50, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
