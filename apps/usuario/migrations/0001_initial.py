# Generated by Django 2.2.7 on 2019-11-16 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0002_zapatilla_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id_compra', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(null=True)),
                ('hora_compra', models.TimeField(null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.zapatilla')),
            ],
        ),
    ]
