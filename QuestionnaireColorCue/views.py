from django.core.validators import validate_email
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
import validate_email
from validate_email import *
from django.core.exceptions import ValidationError
import random

def register(request):
    return render(request,'QuestionnaireColorCue/register.html')

def contact(request):
    return render(request,'QuestionnaireColorCue/contact.html')

def about(request):
    return render(request,'QuestionnaireColorCue/about.html')

def terms(request):
    return render(request,'QuestionnaireColorCue/terms.html')


def register_type2_done(request):

    if request.method=="POST":
        if request.POST['firstname'] and request.POST['lastname'] and request.POST['email'] and request.POST['city'] and request.POST['country'] and request.POST['age']:
            # print('Hello')
            user=UserDetails()
            try:
                # check if email is valid or not
                email = request.POST['email']
                try:
                    validate_email(email)
                except ValidationError as e:
                    return render(request,'QuestionnaireColorCue/register.html',{'error':'Please verify your email.'})
                user.email=email
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                user.age = request.POST['age']

                option = request.POST.get("option",None)
                if option in ["Male","Female","Other"]:
                    if option=="Male":
                        user.gender="Male"
                    elif option=="Female":
                        user.gender="Female"
                    elif option=="Other":
                        user.gender="Other"
                else:
                    return render(request, 'QuestionnaireColorCue/register.html',
                                      {'error': 'All fields are required.'})

                user.city = request.POST['city']
                user.country = request.POST['country']

                if 'terms' not in request.POST:
                    return render(request, 'QuestionnaireColorCue/register.html', {'error': 'Please accept the terms and conditions.'})

                user.save()
                request.session['user_id'] = user.id
                request.session['iteration'] = 1
                request.session['list_of_stimuli'] = []
                request.session['list_of_questions'] = []
                request.session['flag'] = True
            except ValueError as e:
                return render(request,'QuestionnaireColorCue/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'QuestionnaireColorCue/decide_set_number.html')
        else:
            return render(request,'QuestionnaireColorCue/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'QuestionnaireColorCue/register.html')

def decide_set_number(request):
    return render(request,'QuestionnaireColorCue/decide_set_number.html')

def set_number_register_type2(request):
    if request.method=="POST":
        user_response = SetNumber()
        try:
            if request.POST.get("set1"):
                user_response.set_num = "set1"
            elif request.POST.get("set2"):
                user_response.set_num = "set2"
            elif request.POST.get("set3"):
                user_response.set_num = "set3"
            elif request.POST.get("set4"):
                user_response.set_num = "set4"
            elif request.POST.get("set5"):
                user_response.set_num = "set5"
            user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
            user_response.save()

            print("in try")
            return render(request, 'QuestionnaireColorCue/welcome.html')

        except ValueError as e:
            print("in exception")
            print(e)
            return render(request, 'QuestionnaireColorCue/decide_set_number.html',
                          {'error': 'Please select either one of the sets.'})

    else:
        print("in else")
        return render(request,'QuestionnaireColorCue/decide_set_number.html')


def training_phase_start_type2(request):
    return render(request, 'QuestionnaireColorCue/training_phase_start.html')