#coding:utf-8
__author__='zhaoxusun'

from django.db import models

# Create your models here.
# These Models is for Rising Detection Device.
# The meaning of each table and each field is in the log description file.
class Superfw(models.Model):
    indx = models.AutoField(primary_key=True)
    severity = models.IntegerField()
    time = models.DateTimeField()
    node_id = models.CharField(max_length=200)
    device_id = models.CharField(max_length=200)
    usr_name  = models.CharField(max_length=200)
    system_device_id = models.CharField(max_length=200)
    permission = models.CharField(max_length=200)
    login_type = models.CharField(max_length=200)
    login_ip = models.CharField(max_length=200)
    operate_content = models.CharField(max_length=1000)
    orign = models.CharField(max_length=4000)
    router_ip = models.CharField(max_length=200)
    router_port = models.CharField(max_length=200)
    class Meta:
        db_table = 'superfw_tbl'
class Syslogd(models.Model):
    indx = models.AutoField(primary_key=True)
    serverity = models.IntegerField()
    time = time = models.DateTimeField()
    node_id = models.CharField(max_length=200)
    device_id = models.CharField(max_length=200)
    orign = models.CharField(max_length=4000)
    router_ip = models.CharField(max_length=200)
    router_port = models.CharField(max_length=200)
    class Meta:
        db_table = 'syslogd_tbl'
class Viruslog(models.Model):
    indx = models.AutoField(primary_key=True)
    severity = models.IntegerField()
    time = models.DateTimeField()
    node_id = models.CharField(max_length=200)
    device_id = models.CharField(max_length=200)
    virus_name = models.CharField(max_length=300)
    threat_type = models.CharField(max_length=200)
    danger_type = models.CharField(max_length=200)
    spread_virus_device_name = models.CharField(max_length=200)
    spread_virus_device_ip = models.CharField(max_length=200)
    spread_virus_device_port = models.CharField(max_length=200)
    get_virus_device_name = models.CharField(max_length=200)
    get_virus_device_ip = models.CharField(max_length=200)
    get_virus_device_port = models.CharField(max_length=200)
    virus_size = models.IntegerField()
    virus_info = models.CharField(max_length=3000)
    orign = models.CharField(max_length=4000)
    router_ip = models.CharField(max_length=200)
    router_port = models.CharField(max_length=200)
    is_handled = models.BooleanField(default=False)
    class Meta:
        db_table = 'viruslog_tbl'
class Handlelog(models.Model):
    DEVICE_TYPE = (
        ('VICTIM','victim'),
        ('VSOURCE','vsource'),
    )
    OPERATION_TYPE=(
        ('DEL', 'deleted'),
        ('REG', 'rejected'),
        ('IGN', 'ignored'),
        ('OTH', 'other'),
    )
    id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=200)
    device_ip = models.CharField(max_length=200)
    is_victim = models.CharField(max_length=10, choices=DEVICE_TYPE, default='VICTIM')
    operation = models.CharField(max_length=3, choices=OPERATION_TYPE, default='OTH')
    op_time = models.DateField()
    class Meta:
        db_table = 'handlelog'
