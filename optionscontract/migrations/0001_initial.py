# Generated by Django 4.2.1 on 2023-05-17 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OptionsContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=6)),
                ('contract_type', models.CharField(choices=[('CALL', 'Call'), ('PUT', 'Put')], max_length=4)),
                ('position_type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], max_length=4)),
                ('expiration', models.DateField()),
                ('strike_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_opened', models.DateField()),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('closing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('closed', models.BooleanField(default=False)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
