# Generated by Django 2.2.9 on 2020-01-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_featuredproduct_featuredproductimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.ImageField(upload_to='images/featured_products')),
                ('main_picture', models.BooleanField(default=False)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('Featured_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.FeaturedProduct')),
            ],
        ),
    ]
