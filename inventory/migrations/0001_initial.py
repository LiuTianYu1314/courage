# Generated by Django 4.2.10 on 2025-04-17 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='客户名称')),
                ('contact', models.CharField(blank=True, max_length=50, verbose_name='联系人')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='联系电话')),
                ('address', models.TextField(blank=True, verbose_name='地址')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.CharField(max_length=100, verbose_name='型号')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '产品型号',
                'verbose_name_plural': '产品型号',
                'unique_together': {('customer', 'model_number')},
            },
        ),
        migrations.CreateModel(
            name='OutgoingShipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('shipment_date', models.DateField(verbose_name='出货日期')),
                ('document_number', models.CharField(max_length=50, verbose_name='单据编号')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='总金额')),
                ('notes', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer', verbose_name='客户')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttype', verbose_name='产品型号')),
            ],
            options={
                'verbose_name': '出货单据',
                'verbose_name_plural': '出货单据',
            },
        ),
        migrations.CreateModel(
            name='IncomingShipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('shipment_date', models.DateField(verbose_name='来料日期')),
                ('document_number', models.CharField(max_length=50, verbose_name='单据编号')),
                ('notes', models.TextField(blank=True, verbose_name='备注')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.customer', verbose_name='客户')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttype', verbose_name='产品型号')),
            ],
            options={
                'verbose_name': '来料单据',
                'verbose_name_plural': '来料单据',
            },
        ),
    ]
