# Generated by Django 2.2.5 on 2019-09-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, upload_to='product_images')),
                ('product_title', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('best_by', models.DateTimeField(auto_now_add=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['product_title'],
            },
        ),
    ]