#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Desc:

"""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["name", "email", "url", "text"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "昵称", "type": "nickname"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "电子邮件", "type": "email"})
        }
