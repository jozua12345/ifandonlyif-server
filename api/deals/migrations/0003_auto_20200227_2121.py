# Generated by Django 3.0.3 on 2020-02-27 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_blacklists_clientusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blacklists',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Deals'),
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='deals.Choices')),
                ('clientuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.ClientUsers')),
                ('deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Deals')),
            ],
        ),
    ]