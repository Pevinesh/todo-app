from asyncio import Task
from dataclasses import field
from django import forms
from django.forms import ModelForm, fields_for_model
from .models import * 


class Scheduleform(forms.ModelForm):

    class Meta:
        model = Schedule
        fields  = "__all__"