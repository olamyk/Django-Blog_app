# Generated by Django 3.1.4 on 2021-03-20 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0003_remove_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]