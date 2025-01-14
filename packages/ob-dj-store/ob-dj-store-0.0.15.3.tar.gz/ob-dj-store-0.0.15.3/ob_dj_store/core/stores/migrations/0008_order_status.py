# Generated by Django 3.1.14 on 2022-05-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0007_cart_cartitem_order_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("ACCEPTED", "accepted"),
                    ("CANCELLED", "cancelled"),
                    ("PENDING", "pending"),
                    ("PREPARING", "preparing"),
                    ("READY", "ready for pickup"),
                    ("DELIVERED", "delivered"),
                    ("PAID", "paid"),
                    ("OPENED", "opened"),
                ],
                default="PENDING",
                max_length=32,
            ),
        ),
    ]
