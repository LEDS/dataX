# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pessoa', '0002_auto_20170710_2042'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='endereco',
            table='endereco',
        ),
        migrations.AlterModelTable(
            name='escola_origem_pessoa',
            table='escola_origem_pessoa',
        ),
        migrations.AlterModelTable(
            name='forma_ingresso_pessoa',
            table='forma_ingresso_pessoa',
        ),
        migrations.AlterModelTable(
            name='renda_familiar_pessoa',
            table='renda_familiar_pessoa',
        ),
    ]
