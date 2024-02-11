# Generated by Django 4.2.4 on 2023-08-26 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.bank')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_type', models.CharField(choices=[('psr', 'PSR'), ('holesale', 'Holesale'), ('retail', 'Retail')], max_length=10)),
                ('date', models.DateField()),
                ('salestaka', models.IntegerField()),
                ('dsr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.dsr')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.market')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Redamage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Lifting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liftingpayment', models.IntegerField()),
                ('date', models.DateField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Displaybill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Damage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('damagetaka', models.FloatField()),
                ('dsr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.dsr')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.market')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Dailycost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('carcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dsrbill', models.DecimalField(decimal_places=2, max_digits=10)),
                ('toll', models.DecimalField(decimal_places=2, max_digits=10)),
                ('othercost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discription', models.CharField(max_length=1000)),
                ('dsr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.dsr')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.supplier')),
            ],
        ),
    ]