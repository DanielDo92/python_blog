# Generated by Django 2.1 on 2019-07-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_product'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together={('actor', 'title')},
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['prod_id'], name='blog_produc_prod_id_b15d27_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['director', 'producer'], name='blog_produc_directo_165e39_idx'),
        ),
    ]
