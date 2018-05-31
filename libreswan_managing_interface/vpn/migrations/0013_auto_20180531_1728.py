# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0012_auto_20180531_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='connaddrfamily',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='keyexchange',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='keyringtries',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftaddresspool',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftnexthop',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftprotoport',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftsourceip',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftsubnets',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftupdown',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='leftvti',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='rightnexthop',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='rightsourceip',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='rightsubnet',
        ),
        migrations.RemoveField(
            model_name='vpnforremotehost',
            name='type',
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='auto',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>start</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='dpdaction',
            field=models.CharField(blank=True, default='hold', help_text='Valid - <b><a>clear</a></b> OR <b><a>restart</a></b> OR <b><a>hold</a></b>', max_length=4),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='dpddelay',
            field=models.CharField(blank=True, default='0', help_text='eg. <b><a>10</a></b>', max_length=4),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='dpdtimeout',
            field=models.CharField(blank=True, default='0', help_text='eg. <b><a>150</a></b>', max_length=4),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='fragmentation',
            field=models.CharField(blank=True, default='yes', help_text='Valid - <b><a>yes</a></b> OR <b><a>no</a></b> OR <b><a>force</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='ikev2',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>insist</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='leftcert',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>vpn.example.com</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='leftid',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>@vpn.example.com</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='leftrsasigkey',
            field=models.CharField(blank=True, default='%dnsondemand', help_text='eg. <b><a>%cert</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='leftsendcert',
            field=models.CharField(blank=True, default='sendifasked', help_text='Valid - <b><a>yes|always</a></b> OR <b><a>no|never</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='modecfgdns',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>8.8.8.8,193.100.157.123</a></b>', max_length=32),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='narrowing',
            field=models.CharField(blank=True, default='no', help_text='Valid - <b><a>no</a></b> OR <b><a>yes</a></b>', max_length=3),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='rekey',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>no</a></b>', max_length=16),
        ),
        migrations.AddField(
            model_name='vpnforremotehost',
            name='rightca',
            field=models.CharField(blank=True, default='', help_text='eg. <b><a>%same</a></b>', max_length=16),
        ),
    ]
