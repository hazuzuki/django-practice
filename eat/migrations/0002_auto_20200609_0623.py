# Generated by Django 3.0.2 on 2020-06-08 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='good_user',
            field=models.ManyToManyField(blank=True, related_name='good_user', to=settings.AUTH_USER_MODEL, verbose_name='いいねしたユーザー'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='quote_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='参考cookレシピ'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='quoted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
