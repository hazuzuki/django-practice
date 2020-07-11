# Generated by Django 3.0.2 on 2020-07-06 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eat', '0010_auto_20200707_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='quote',
            field=models.CharField(default='無し', max_length=10),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='quote_recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quote_recipe_name', to='eat.Recipe'),
        ),
    ]