# Generated by Django 3.2.5 on 2022-02-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xj_user', '0007_merge_20220205_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='plaintext',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PT'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='ticket',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='临时票据'),
        ),
        migrations.AlterField(
            model_name='auth',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='临时凭证'),
        ),
    ]
