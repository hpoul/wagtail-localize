# Generated by Django 3.2.4 on 2021-07-23 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_test', '0015_testsnippet_small_charfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpage',
            name='test_not_overridable_synchronized_textfield',
            field=models.TextField(blank=True),
        ),
    ]
