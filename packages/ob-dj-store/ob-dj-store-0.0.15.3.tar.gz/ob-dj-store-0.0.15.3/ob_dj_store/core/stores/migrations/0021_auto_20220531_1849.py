# Generated by Django 3.1.14 on 2022-05-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0020_orderhistory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productattribute",
            name="attribute",
        ),
        migrations.AddField(
            model_name="attributechoice",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, help_text="Price", max_digits=10
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="attribute_choices",
            field=models.ManyToManyField(
                blank=True,
                help_text="Attribute choices for the item",
                related_name="cart_items",
                to="stores.AttributeChoice",
            ),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="notes",
            field=models.TextField(
                blank=True, help_text="Special instructions", null=True
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="attribute_choices",
            field=models.ManyToManyField(
                blank=True,
                help_text="Attribute choices for the item",
                related_name="order_items",
                to="stores.AttributeChoice",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="notes",
            field=models.TextField(
                blank=True, help_text="Special instructions", null=True
            ),
        ),
    ]
