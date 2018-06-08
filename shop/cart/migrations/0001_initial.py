# Generated by Django 2.0.5 on 2018-05-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(db_column='gid', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='gname', max_length=50)),
                ('price', models.DecimalField(db_column='gprice', decimal_places=2, max_digits=10)),
                ('image', models.CharField(db_column='gimage', max_length=255)),
            ],
            options={
                'db_table': 'tb_goods',
                'ordering': ('id',),
            },
        ),
    ]
