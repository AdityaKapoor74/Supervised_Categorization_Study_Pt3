from django.core.validators import validate_email
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
import validate_email
from validate_email import *
from django.core.exceptions import ValidationError
import random

def register(request,num):
    return render(request,'QuestionnaireColorCueNew/register.html',{'set_num':num})

def contact(request):
    return render(request,'QuestionnaireColorCueNew/contact.html')

def about(request):
    return render(request,'QuestionnaireColorCueNew/about.html')

def terms(request):
    return render(request,'QuestionnaireColorCueNew/terms.html')


def register_type3_done(request):
    # print("REQUEST:")
    # print(request)
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
                    return render(request,'QuestionnaireColorCueNew/register.html',{'error':'Please verify your email.'})
                user.email=email
                user.first_name = request.POST['firstname']
                user.last_name = request.POST['lastname']
                user.age = request.POST['age']
                user.set_num = request.POST['set_num']
                request.session['setnumber'] = request.POST['set_num']

                option = request.POST.get("option",None)
                if option in ["Male","Female","Other"]:
                    if option=="Male":
                        user.gender="Male"
                    elif option=="Female":
                        user.gender="Female"
                    elif option=="Other":
                        user.gender="Other"
                else:
                    return render(request, 'QuestionnaireColorCueNew/register.html',
                                      {'error': 'All fields are required.'})

                user.city = request.POST['city']
                user.country = request.POST['country']

                if 'terms' not in request.POST:
                    return render(request, 'QuestionnaireColorCueNew/register.html', {'error': 'Please accept the terms and conditions.'})

                user.save()
                request.session['user_id'] = user.id
                request.session['iteration'] = 1
                request.session['score'] = 0

                request.session['obs_learn_samples'] = []
                request.session['flag_training'] = False
                request.session['flag_test'] = False
                request.session['classify_learn_samples'] = []
                request.session['correct_answer'] = 0
                request.session['score'] = 0
                request.session['result'] = 0
                request.session['performance'] = ""
                request.session['test_iteration'] = 1
                request.session['test_samples'] = []
                request.session['common_features_test_samples'] = []
                request.session['quid'] = -1
                request.session['test_phase_flag'] = False
                request.session['common_features_iteration'] = 1
                request.session['common_features_test_phase_flag'] = False
            except ValueError as e:
                return render(request,'QuestionnaireColorCueNew/register.html',{'error':'Incorrect values.Please try again.'})

            return render(request,'QuestionnaireColorCueNew/welcome.html')
        else:
            return render(request,'QuestionnaireColorCueNew/register.html',{'error':'All fields are required.'})
    else:
        return render(request,'QuestionnaireColorCueNew/register.html')

def training_phase_start_type3(request):
    return render(request, 'QuestionnaireColorCueNew/training_phase_start.html')

def observe_and_learn_type3(request):
    return render(request, 'QuestionnaireColorCueNew/observe_and_learn.html',
                  {'iteration': request.session['iteration']})

def observe_and_learn_instructions_type3(request):
    return render(request,'QuestionnaireColorCueNew/observe_and_learn_instructions.html')

def observe_and_learn_display_stimuli_type3(request):
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

        return render(request, 'QuestionnaireColorCueNew/observe_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_training'] == True:
            return render(request,'QuestionnaireColorCueNew/classify_and_learn.html',{'iteration': request.session['iteration']})
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

        return render(request, 'QuestionnaireColorCueNew/observe_and_learn_samples.html', {'samples': samples})

def fixation_screen_type3(request):
    return render(request,'QuestionnaireColorCueNew/fixation_screen.html')

def classify_and_learn_instructions_type3(request):
    return render(request,'QuestionnaireColorCueNew/classify_and_learn_instructions.html')

def classify_and_learn_display_stimuli_type3(request):
    if request.method=="POST":
        option = request.POST.get("option",None)
        if option==request.session['correct_answer']:
            request.session['score'] += 1
            return render(request,"QuestionnaireColorCueNew/fixation_screen_classify.html")
        else:
            return render(request,"QuestionnaireColorCueNew/wrong_ans_warning.html",{'correct_answer':request.session['correct_answer']})

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
        return render(request, 'QuestionnaireColorCueNew/classify_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_test'] == True:
            request.session['performance']+=str(request.session['score']*10)+"% "
            return render(request,'QuestionnaireColorCueNew/classify_result.html',{"performance":request.session['score']*10,"correct":request.session['score'],"wrong":10-request.session['score']})
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
        return render(request, 'QuestionnaireColorCueNew/classify_and_learn_samples.html', {'samples': samples})

def fixation_screen_classify_type3(request):
    return render(request, 'QuestionnaireColorCueNew/fixation_screen_classify.html')

def classify_performance_type3(request):
    if request.session['score']>8:
        request.session['result']+=1

    if request.session['result']<2:
        #Training phase
        request.session['iteration']+=1
        request.session['flag_training'] = False
        request.session['score'] = 0
        #check for iterations if greater than 10 : what to do?
        return render(request,"QuestionnaireColorCueNew/observe_and_learn.html",{"iteration":request.session['iteration']})
    else:
        #Testing phase
        return render(request,"QuestionnaireColorCueNew/test_phase.html")

def classify_result_type3(request):
    return render(request,"QuestionnaireColorCueNew/classify_performance.html",{"performance_history":request.session['performance']})

def test_phase_type3(request):
    return render(request,"QuestionnaireColorCueNew/test_phase_instructions.html")

def test_block_type3(request):
    return render(request,"QuestionnaireColorCueNew/test_block.html",{"iteration":request.session['test_iteration']})

def test_block_display_stimuli_type3(request):
    if request.method=="POST":
        option = request.POST.get("option",None)
        if request.session['setnumber'] == 1:
            user_response = UserResponse_Test_set1()
            user_response.quid = Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            user_response = UserResponse_Test_set2()
            user_response.quid = Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            user_response = UserResponse_Test_set3()
            user_response.quid = Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            user_response = UserResponse_Test_set4()
            user_response.quid = Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 5:
            user_response = UserResponse_Test_set5()
            user_response.quid = Test_set5.objects.get(pk=request.session['quid'])
        if option=="A":
            user_response.user_option = "A"
        else:
            user_response.user_option = "B"
        user_response.iteration = request.session['test_iteration']
        user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
        user_response.save()
        return render(request,"QuestionnaireColorCueNew/fixature_screen_test.html")

    if len(request.session['test_samples'])!=0:
        request.session['quid'] = request.session['test_samples'][0]
        request.session['test_samples'] = request.session['test_samples'][1:]

        if len(request.session['test_samples']) == 0:
            request.session['test_iteration']+=1
            request.session['test_phase_flag'] = True

        if request.session['setnumber'] == 1:
            samples = Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            samples = Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            samples = Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            samples = Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 5:
            samples = Test_set5.objects.get(pk=request.session['quid'])
        return render(request, 'QuestionnaireColorCueNew/test_samples.html',{'samples':samples})

    else:
        if request.session['test_phase_flag'] == True and request.session['test_iteration']<4:
            request.session['test_phase_flag'] = False
            return render(request, "QuestionnaireColorCueNew/break.html")
        if request.session['test_phase_flag'] == True and request.session['test_iteration']>3:
            return render(request,"QuestionnaireColorCueNew/break_to_features.html")

        if request.session['setnumber'] == 1:
            request.session['test_samples'] = list(Test_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set1.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['test_samples'] = list(Test_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set2.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['test_samples'] = list(Test_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set3.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['test_samples'] = list(Test_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set4.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 5:
            request.session['test_samples'] = list(Test_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set5.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        return render(request, 'QuestionnaireColorCueNew/test_samples.html', {'samples': samples})

def common_features_test_phase_type3(request):
    return render(request,"QuestionnaireColorCueNew/common_features_test_phase.html")

def common_features_test_phase_block_type3(request):
    return render(request,"QuestionnaireColorCueNew/common_features_test_phase_block.html",{"iteration":request.session['common_features_iteration']})

def common_features_test_block_display_stimuli_type3(request):
    if request.method=="POST":
        option = request.POST.get("option",None)
        if request.session['setnumber'] == 1:
            user_response = UserResponse_Common_Features_Test_set1()
            user_response.quid = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            user_response = UserResponse_Common_Features_Test_set2()
            user_response.quid = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            user_response = UserResponse_Common_Features_Test_set3()
            user_response.quid = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            user_response = UserResponse_Common_Features_Test_set4()
            user_response.quid = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 5:
            user_response = UserResponse_Common_Features_Test_set5()
            user_response.quid = Common_Features_Test_set5.objects.get(pk=request.session['quid'])
        if option=="A":
            user_response.user_option = "A"
            request.session['correct_answer'] = "A"
        else:
            user_response.user_option = "B"
            request.session['correct_answer'] = "B"
        user_response.iteration = request.session['common_features_iteration']
        user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
        user_response.save()
        return render(request,"QuestionnaireColorCueNew/selected_option.html",{'correct_answer':request.session['correct_answer']})

    if len(request.session['common_features_test_samples'])!=0:
        request.session['quid'] = request.session['common_features_test_samples'][0]
        request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]

        if len(request.session['common_features_test_samples']) == 0:
            request.session['common_features_iteration']+=1
            request.session['common_features_test_phase_flag'] = True

        if request.session['setnumber'] == 1:
            samples = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            samples = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            samples = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            samples = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 5:
            samples = Common_Features_Test_set5.objects.get(pk=request.session['quid'])
        return render(request, 'QuestionnaireColorCueNew/common_features_test_samples.html',{'samples':samples})

    else:
        if request.session['common_features_test_phase_flag'] == True and request.session['common_features_iteration']<4:
            request.session['common_features_test_phase_flag'] = False
            return render(request, "QuestionnaireColorCueNew/break_common_features.html")
        if request.session['common_features_test_phase_flag'] == True and request.session['common_features_iteration']>3:
            return render(request,"QuestionnaireColorCueNew/description.html")

        if request.session['setnumber'] == 1:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 5:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set5.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        return render(request, 'QuestionnaireColorCueNew/common_features_test_samples.html', {'samples': samples})


def save_responses_description(request):
    if request.method == "POST":
        try:
            desc = request.POST.get('description', None)
            if len(desc) != 0:
                user_response = UserResponsesForDescription()
                user_response.description = desc
                uid = request.session['user_id']
                user_response.user = UserDetails.objects.get(pk=uid)
                user_response.set_number = request.session['setnumber']
                user_response.save()

            else:
                return render(request, 'QuestionnaireColorCueNew/description.html', {'error': 'Please fill in the description'})

        except ValueError as e:
            return render(request, 'QuestionnaireColorCueNew/description.html', {'error': 'Please fill in the description'})

    return render(request, 'QuestionnaireColorCueNew/thankyou.html')