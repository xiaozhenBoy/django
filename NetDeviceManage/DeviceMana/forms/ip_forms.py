# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

# ip浏览条件设置
SKIM_CHOICES = (
    ('0', '所有的异常记录'),
    ('1', '最近一天的异常记录'),
    ('2', '最近三天的异常记录'),
    ('3', '最近七天的异常记录'),
)

class SkimConForm(forms.Form):
    skimcon = forms.ChoiceField(choices=SKIM_CHOICES,label='')
