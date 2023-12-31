# Generated by Django 4.2.4 on 2023-09-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='for_user',
            field=models.CharField(default='xyz', max_length=200),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Conubia sem netus ad convallis proin. Nam lobortis ad justo inceptos vehicula sapien rhoncus rhoncus? Vel pellentesque ut taciti gravida hac sociis hendrerit semper platea penatibus fusce sociis. Quis eros dapibus phasellus vulputate. Ultricies nascetur integer dignissim dolor euismod mus! Blandit urna vehicula in varius vestibulum himenaeos? Litora pellentesque aliquam urna vulputate est. Pellentesque senectus laoreet habitant. Aliquet quis vestibulum turpis. Etiam bibendum, nisl sociis ut montes duis id eleifend condimentum etiam. Semper.', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=500),
        ),
    ]
