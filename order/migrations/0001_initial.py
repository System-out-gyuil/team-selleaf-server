# Generated by Django 5.0.2 on 2024-03-05 15:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecture', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_status', models.IntegerField(choices=[(0, '진행중'), (-1, '삭제'), (1, '결제완료')], default=0)),
                ('order_receiver', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.memberaddress')),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.kit')),
            ],
            options={
                'db_table': 'tbl_order',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderMileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('mileage_status', models.BooleanField(default=True)),
                ('mileage', models.BigIntegerField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
            ],
            options={
                'db_table': 'tbl_order_mileage',
                'ordering': ['-id'],
            },
        ),
    ]
