# Generated by Django 5.0.6 on 2024-05-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(choices=[('Crochets', 'Crochets'), ('Crochet Bundles', 'Crochet Bundles'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Crochets', 'Crochets'), ('Crochet Bundles', 'Crochet Bundles'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='crochets', max_length=25),
        ),
    ]