# Generated by Django 3.1.4 on 2021-05-04 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0010_remove_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to='blogApp.comment'),
            preserve_default='True',
        ),
    ]
