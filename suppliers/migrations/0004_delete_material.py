# Generated by Django 5.1.6 on 2025-02-14 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_remove_supplier_gst_number_remove_supplier_inventory_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material',
        ),
    ]
