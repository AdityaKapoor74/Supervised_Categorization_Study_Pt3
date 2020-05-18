from django.core.validators import validate_email
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
import validate_email
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


def register_type1_done(request):

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
                    return render(request,'Questionnaire/register.html',{'error':'Please verify your email.'})
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
                    return render(request, 'Questionnaire/register.html',
                                      {'error': 'All fields are required.'})

                user.city = request.POST['city']
                user.country = request.POST['country']

                if 'terms' not in request.POST:
                    return render(request, 'Questionnaire/register.html', {'error': 'Please accept the terms and conditions.'})

                user.save()
                request.session['user_id'] = user.id
                request.session['iteration'] = 1
                request.session['score'] = 0
                request.session['setnumber'] = -1
                request.session['obs_learn_samples'] = []
                request.session['flag_training'] = False
                request.session['flag_test'] = False
                request.session['classify_learn_samples'] = []
                request.session['correct_answer'] = 0
            except ValueError as e:
                return render(request,'Questionnaire/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'Questionnaire/decide_set_number.html')
        else:
            return render(request,'Questionnaire/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'Questionnaire/register.html')

def decide_set_number(request):
    return render(request,'Questionnaire/decide_set_number.html')

def set_number_register_type1(request):
    if request.method=="POST":
        user_response = SetNumber()
        try:
            if request.POST.get("set1"):
                user_response.set_num = "set1"
                request.session['setnumber'] = 1
            elif request.POST.get("set2"):
                user_response.set_num = "set2"
                request.session['setnumber'] = 2
            elif request.POST.get("set3"):
                user_response.set_num = "set3"
                request.session['setnumber'] = 3
            elif request.POST.get("set4"):
                user_response.set_num = "set4"
                request.session['setnumber'] = 4
            elif request.POST.get("set5"):
                user_response.set_num = "set5"
                request.session['setnumber'] = 5
            user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
            user_response.save()

            print("in try")
            return render(request, 'Questionnaire/welcome.html')

        except ValueError as e:
            print("in exception")
            print(e)
            return render(request, 'Questionnaire/decide_set_number.html',
                          {'error': 'Please select either one of the sets.'})

    else:
        print("in else")
        return render(request,'Questionnaire/decide_set_number.html')

def training_phase_start_type1(request):
    return render(request, 'Questionnaire/training_phase_start.html')

def observe_and_learn_type1(request):
    return render(request, 'Questionnaire/observe_and_learn.html',
                  {'iteration': request.session['iteration']})

def observe_and_learn_instructions_type1(request):
    return render(request,'Questionnaire/observe_and_learn_instructions.html')

def observe_and_learn_display_stimuli_type1(request):
    if len(request.session['obs_learn_samples'])!=0:
        id = request.session['obs_learn_samples'][0]
        request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        if len(request.session['obs_learn_samples']) == 0:
            request.session['flag_training'] = True
            request.session['flag_test'] = False
        if request.session['setnumber'] == 1:
            samples = Observe_And_Learn_Samples_set1.objects.get(pk=id)
        elif request.session['setnumber'] == 2:
            samples = Observe_And_Learn_Samples_set2.objects.get(pk=id)
        elif request.session['setnumber'] == 3:
            samples = Observe_And_Learn_Samples_set3.objects.get(pk=id)
        elif request.session['setnumber'] == 4:
            samples = Observe_And_Learn_Samples_set4.objects.get(pk=id)
        elif request.session['setnumber'] == 5:
            samples = Observe_And_Learn_Samples_set5.objects.get(pk=id)

        return render(request, 'Questionnaire/observe_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_training'] == True:
            return render(request,'Questionnaire/classify_and_learn.html',{'iteration': request.session['iteration']})
        if request.session['setnumber'] == 1:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set1.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set2.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set3.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set4.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 5:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set5.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]

        return render(request, 'Questionnaire/observe_and_learn_samples.html', {'samples': samples})

def fixation_screen_type1(request):
    return render(request,'Questionnaire/fixation_screen.html')

def classify_and_learn_instructions_type1(request):
    return render(request,'Questionnaire/classify_and_learn_instructions.html')

def classify_and_learn_display_stimuli_type1(request):
    if request.method=="POST":
        option = request.POST.get("option",None)
        if option==request.session['correct_answer']:
            return render(request,"Questionnaire/fixation_screen_classify.html")
        else:
            return render("Questionnaire/wrong_ans_warning.html",{'correct_answer':request.session['correct_answer']})

    if len(request.session['classify_learn_samples'])!=0:
        id = request.session['classify_learn_samples'][0]
        request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        if len(request.session['classify_learn_samples']) == 0:
            request.session['flag_test'] = True
        if request.session['setnumber'] == 1:
            samples = Classify_And_Learn_Samples_set1.objects.get(pk=id)
        elif request.session['setnumber'] == 2:
            samples = Classify_And_Learn_Samples_set2.objects.get(pk=id)
        elif request.session['setnumber'] == 3:
            samples = Classify_And_Learn_Samples_set3.objects.get(pk=id)
        elif request.session['setnumber'] == 4:
            samples = Classify_And_Learn_Samples_set4.objects.get(pk=id)
        elif request.session['setnumber'] == 5:
            samples = Classify_And_Learn_Samples_set5.objects.get(pk=id)
        request.session['correct_answer'] = samples.sample_label
        return render(request, 'Questionnaire/classify_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_test'] == True:
            return render(request,'Questionnaire/classify_result.html')
        if request.session['setnumber'] == 1:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            samples = Classify_And_Learn_Samples_set1.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            samples = Classify_And_Learn_Samples_set2.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            samples = Classify_And_Learn_Samples_set3.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            samples = Classify_And_Learn_Samples_set4.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 5:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            samples = Classify_And_Learn_Samples_set5.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        request.session['correct_answer'] = samples.sample_label
        return render(request, 'Questionnaire/classify_and_learn_samples.html', {'samples': samples})

def fixation_screen_classify_type1(request):
    return render(request, 'Questionnaire/fixation_screen_classify.html')