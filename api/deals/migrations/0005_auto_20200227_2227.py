# Generated by Django 3.0.3 on 2020-02-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_auto_20200227_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklists',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Deals'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deals.Deals'),
        ),
        migrations.AlterUniqueTogether(
            name='blacklists',
            unique_together={('clientuser2', 'clientuser1', 'deal')},
        ),
        migrations.AlterUniqueTogether(
            name='requests',
            unique_together={('clientuser', 'deal')},
        ),
    ]