# Generated by Django 4.1.7 on 2023-03-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trp_db', '0003_spareparts_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='spareparts',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]
