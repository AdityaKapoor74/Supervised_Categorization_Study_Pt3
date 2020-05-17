from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
from validate_email import *
from django.core.exceptions import ValidationError
import random

def register(request):
    return render(request,'Questionnaire/register.html')

def contact(request):
    return render(request,'Questionnaire/contact.html')

def about(request):
    return render(request,'Questionnaire/about.html')

def terms(request):
    return render(request,'Questionnaire/terms.html')