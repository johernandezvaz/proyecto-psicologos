# Generated by Django 5.1.7 on 2025-04-07 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psychologist',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='psychologist_users', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='psychologist',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='psychologist_user_permissions', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
