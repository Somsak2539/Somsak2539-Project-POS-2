# Generated by Django 4.2.9 on 2025-04-20 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0014_alter_category_options_alter_product1_barcode_and_more'),
        ('DashboardUser', '0003_alter_invoiceitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.category', verbose_name='หมวดหมู่'),
        ),
    ]
