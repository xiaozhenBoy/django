# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handlelog',
            fields=[
                ('indx', models.AutoField(serialize=False, primary_key=True)),
                ('device_name', models.CharField(max_length=200)),
                ('device_ip', models.CharField(max_length=200)),
                ('is_victim', models.CharField(default=b'VICTIM', max_length=10, choices=[(b'VICTIM', b'victim'), (b'VSOURCE', b'vsource')])),
                ('operation', models.CharField(default=b'OTH', max_length=3, choices=[(b'DEL', b'deleted'), (b'REG', b'rejected'), (b'IGN', b'ignored'), (b'OTH', b'other')])),
            ],
            options={
                'db_table': 'handlelog',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Superfw',
            fields=[
                ('indx', models.AutoField(serialize=False, primary_key=True)),
                ('severity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('node_id', models.CharField(max_length=200)),
                ('device_id', models.CharField(max_length=200)),
                ('usr_name', models.CharField(max_length=200)),
                ('system_device_id', models.CharField(max_length=200)),
                ('permission', models.CharField(max_length=200)),
                ('login_type', models.CharField(max_length=200)),
                ('login_ip', models.CharField(max_length=200)),
                ('operate_content', models.CharField(max_length=1000)),
                ('orign', models.CharField(max_length=4000)),
                ('router_ip', models.CharField(max_length=200)),
                ('router_port', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'superfw_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Syslogd',
            fields=[
                ('indx', models.AutoField(serialize=False, primary_key=True)),
                ('serverity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('node_id', models.CharField(max_length=200)),
                ('device_id', models.CharField(max_length=200)),
                ('orign', models.CharField(max_length=4000)),
                ('router_ip', models.CharField(max_length=200)),
                ('router_port', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'syslogd_tbl',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Viruslog',
            fields=[
                ('indx', models.AutoField(serialize=False, primary_key=True)),
                ('severity', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('node_id', models.CharField(max_length=200)),
                ('device_id', models.CharField(max_length=200)),
                ('virus_name', models.CharField(max_length=300)),
                ('threat_type', models.CharField(max_length=200)),
                ('danger_type', models.CharField(max_length=200)),
                ('spread_virus_device_name', models.CharField(max_length=200)),
                ('spread_virus_device_ip', models.CharField(max_length=200)),
                ('spread_virus_device_port', models.CharField(max_length=200)),
                ('get_virus_device_name', models.CharField(max_length=200)),
                ('get_virus_device_ip', models.CharField(max_length=200)),
                ('get_virus_device_port', models.CharField(max_length=200)),
                ('virus_size', models.IntegerField()),
                ('virus_info', models.CharField(max_length=3000)),
                ('orign', models.CharField(max_length=4000)),
                ('router_ip', models.CharField(max_length=200)),
                ('router_port', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'viruslog_tbl',
            },
            bases=(models.Model,),
        ),
    ]
