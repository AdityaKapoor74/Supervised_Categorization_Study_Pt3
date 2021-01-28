from django.core.validators import validate_email
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
import validate_email
from validate_email import *
from django.core.exceptions import ValidationError
import random
import time
import datetime

def register(request,num):
    if num>4:
        return render(request,'Questionnaire/set_404.html')
    request.session['setnumber'] = num
    return render(request,'QuestionnaireColorCueNew/register.html')

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
                user.set_num = request.session['setnumber']
                # request.session['setnumber'] = request.POST['set_num']

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
                request.session['start_time'] = -1
                request.session['elapsed_time'] = -1
                request.session['file_name'] = None
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
        if request.session['setnumber'] == 0:
            samples = Observe_And_Learn_Samples_set1.objects.get(pk=id)
        elif request.session['setnumber'] == 1:
            samples = Observe_And_Learn_Samples_set2.objects.get(pk=id)
        elif request.session['setnumber'] == 2:
            samples = Observe_And_Learn_Samples_set3.objects.get(pk=id)
        elif request.session['setnumber'] == 3:
            samples = Observe_And_Learn_Samples_set4.objects.get(pk=id)
        elif request.session['setnumber'] == 4:
            samples = Observe_And_Learn_Samples_set5.objects.get(pk=id)

        return render(request, 'QuestionnaireColorCueNew/observe_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_training'] == True:
            return render(request,'QuestionnaireColorCueNew/classify_and_learn.html',{'iteration': request.session['iteration']})
        if request.session['setnumber'] == 0:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set1.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 1:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set2.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set3.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set4.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['obs_learn_samples'] = list(Observe_And_Learn_Samples_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['obs_learn_samples'])
            id = request.session['obs_learn_samples'][0]
            samples = Observe_And_Learn_Samples_set5.objects.get(pk=id)
            request.session['obs_learn_samples'] = request.session['obs_learn_samples'][1:]

        return render(request, 'QuestionnaireColorCueNew/observe_and_learn_samples.html', {'samples': samples})

def fixation_screen_observe_type3(request):
    return render(request,'QuestionnaireColorCueNew/fixation_screen.html')

def classify_and_learn_instructions_type3(request):
    return render(request,'QuestionnaireColorCueNew/classify_and_learn_instructions.html')

def classify_and_learn_display_stimuli_type3(request):
    if request.method=="POST":
        request.session['elapsed_time'] = time.time() - request.session['start_time']
        option = request.POST.get("option",None)
        classify_stimuli = ClassifyStimuiTable()
        classify_stimuli.user_id = UserDetails.objects.get(pk=request.session['user_id'])
        classify_stimuli.set_number = request.session['setnumber']
        classify_stimuli.block_number = request.session['iteration']
        classify_stimuli.sequence_number = 10 - len(request.session['classify_learn_samples'])
        classify_stimuli.timestamp = datetime.datetime.now()
        classify_stimuli.user_option = option

        if request.session['setnumber'] == 0:
            request.session['file_name'] = str(Classify_And_Learn_Samples_set1.objects.get(pk=request.session['quid']).sample_img.path)
            classify_stimuli.file_name = "colorCue/set0/"+request.session['file_name']

        elif request.session['setnumber'] == 1:
            request.session['file_name'] = str(Classify_And_Learn_Samples_set2.objects.get(pk=request.session['quid']).sample_img.path)
            classify_stimuli.file_name = "colorCue/set1/" + request.session['file_name']

        elif request.session['setnumber'] == 2:
            request.session['file_name'] = str(Classify_And_Learn_Samples_set3.objects.get(pk=request.session['quid']).sample_img.path)
            classify_stimuli.file_name = "colorCue/set2/" + request.session['file_name']

        elif request.session['setnumber'] == 3:
            request.session['file_name'] = str(Classify_And_Learn_Samples_set4.objects.get(pk=request.session['quid']).sample_img.path)
            classify_stimuli.file_name = "colorCue/set3/" + request.session['file_name']

        elif request.session['setnumber'] == 4:
            request.session['file_name'] = str(Classify_And_Learn_Samples_set5.objects.get(pk=request.session['quid']).sample_img.path)
            classify_stimuli.file_name = "colorCue/set4/" + request.session['file_name']

        if option=="A":
            classify_stimuli.user_option = "A"
            if request.session['file_name'].find("Target")!=-1:
                classify_stimuli.correct = 1
            else:
                classify_stimuli.correct = 0
        else:
            classify_stimuli.user_option = "B"
            if request.session['file_name'].find("Contrast")!=-1:
                classify_stimuli.correct = 1
            else:
                classify_stimuli.correct = 0

        classify_stimuli.time_taken = request.session['elapsed_time']
        classify_stimuli.save()

        if option==request.session['correct_answer']:
            request.session['score'] += 1
            return render(request, "QuestionnaireColorCueNew/correct_ans_classify.html",
                          {'time_taken': round(request.session['elapsed_time'], 2)})
        else:
            return render(request,"QuestionnaireColorCueNew/wrong_ans_warning.html",{'correct_answer':request.session['correct_answer'],'time_taken': round(request.session['elapsed_time'], 2)})



    if len(request.session['classify_learn_samples'])!=0:
        id = request.session['classify_learn_samples'][0]
        request.session['quid'] = id
        request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        if len(request.session['classify_learn_samples']) == 0:
            request.session['flag_test'] = True
        if request.session['setnumber'] == 0:
            samples = Classify_And_Learn_Samples_set1.objects.get(pk=id)
        elif request.session['setnumber'] == 1:
            samples = Classify_And_Learn_Samples_set2.objects.get(pk=id)
        elif request.session['setnumber'] == 2:
            samples = Classify_And_Learn_Samples_set3.objects.get(pk=id)
        elif request.session['setnumber'] == 3:
            samples = Classify_And_Learn_Samples_set4.objects.get(pk=id)
        elif request.session['setnumber'] == 4:
            samples = Classify_And_Learn_Samples_set5.objects.get(pk=id)
        request.session['correct_answer'] = samples.sample_label
        request.session['start_time'] = time.time()
        return render(request, 'QuestionnaireColorCueNew/classify_and_learn_samples.html',{'samples':samples})

    else:
        if request.session['flag_test'] == True:
            request.session['performance']+=str(request.session['score']*10)+"% "
            return render(request,'QuestionnaireColorCueNew/classify_result.html',{"performance":request.session['score']*10,"correct":request.session['score'],"wrong":10-request.session['score']})
        if request.session['setnumber'] == 0:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            request.session['quid'] = id
            samples = Classify_And_Learn_Samples_set1.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 1:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            request.session['quid'] = id
            samples = Classify_And_Learn_Samples_set2.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            request.session['quid'] = id
            samples = Classify_And_Learn_Samples_set3.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            request.session['quid'] = id
            samples = Classify_And_Learn_Samples_set4.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['classify_learn_samples'] = list(Classify_And_Learn_Samples_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['classify_learn_samples'])
            id = request.session['classify_learn_samples'][0]
            request.session['quid'] = id
            samples = Classify_And_Learn_Samples_set5.objects.get(pk=id)
            request.session['classify_learn_samples'] = request.session['classify_learn_samples'][1:]
        request.session['correct_answer'] = samples.sample_label
        request.session['start_time'] = time.time()
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
        if request.session['iteration'] > 10:
            return render(request,"QuestionnaireColorCueNew/early_exit.html")
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
        request.session['elapsed_time'] = time.time() - request.session['start_time']
        option = request.POST.get("option",None)
        transfer_stimuli = TransferStimuliTable()
        transfer_stimuli.user_id = UserDetails.objects.get(pk=request.session['user_id'])
        transfer_stimuli.set_number = request.session['setnumber']
        transfer_stimuli.block_number = request.session['test_iteration']
        transfer_stimuli.sequence_number = 10 - len(request.session['test_samples'])
        transfer_stimuli.timestamp = datetime.datetime.now()

        if len(request.session['test_samples']) == 0:
            request.session['test_iteration']+=1
            request.session['test_phase_flag'] = True

        if request.session['setnumber'] == 0:
            user_response = UserResponse_Test_set1()
            user_response.quid = Test_set1.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(Test_set1.objects.get(pk=request.session['quid']).sample_img.path)
            transfer_stimuli.file_name = "colorCue/set0/"+request.session['file_name']
        elif request.session['setnumber'] == 1:
            user_response = UserResponse_Test_set2()
            user_response.quid = Test_set2.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(Test_set2.objects.get(pk=request.session['quid']).sample_img.path)
            transfer_stimuli.file_name = "colorCue/set1/" + request.session['file_name']
        elif request.session['setnumber'] == 2:
            user_response = UserResponse_Test_set3()
            user_response.quid = Test_set3.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(Test_set3.objects.get(pk=request.session['quid']).sample_img.path)
            transfer_stimuli.file_name = "colorCue/set2/" + request.session['file_name']
        elif request.session['setnumber'] == 3:
            user_response = UserResponse_Test_set4()
            user_response.quid = Test_set4.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(Test_set4.objects.get(pk=request.session['quid']).sample_img.path)
            transfer_stimuli.file_name = "colorCue/set3/" + request.session['file_name']
        elif request.session['setnumber'] == 4:
            user_response = UserResponse_Test_set5()
            user_response.quid = Test_set5.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(Test_set5.objects.get(pk=request.session['quid']).sample_img.path)
            transfer_stimuli.file_name = "colorCue/set4/" + request.session['file_name']
        if option=="A":
            user_response.user_option = "A"
            transfer_stimuli.user_option = "A"
            if (request.session['file_name'].find("Transfer00") != -1 or request.session['file_name'].find(
                    "Transfer01") != -1 or request.session['file_name'].find("Transfer02") != -1 or request.session[
                'file_name'].find("Transfer03") != -1 or request.session['file_name'].find("Transfer04") != -1):
                transfer_stimuli.rule_based = 0
            else:
                transfer_stimuli.rule_based = 1hould
        else:
            user_response.user_option = "B"
            transfer_stimuli.user_option = "B"
            if (request.session['file_name'].find("Transfer00")!=-1 or request.session['file_name'].find("Transfer01")!=-1 or request.session['file_name'].find("Transfer02")!=-1 or request.session['file_name'].find("Transfer03")!=-1 or request.session['file_name'].find("Transfer04")!=-1):
                transfer_stimuli.rule_based = 1
            else:
                transfer_stimuli.rule_based = 0

        user_response.iteration = request.session['test_iteration']
        user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
        user_response.time_taken = request.session['elapsed_time']
        transfer_stimuli.time_taken = request.session['elapsed_time']
        user_response.save()
        transfer_stimuli.save()

        return render(request,"QuestionnaireColorCueNew/selected_category_test.html",{"option":option, "timetaken":round(request.session['elapsed_time'],2)})

    if len(request.session['test_samples'])!=0:
        request.session['quid'] = request.session['test_samples'][0]
        request.session['test_samples'] = request.session['test_samples'][1:]


        if request.session['setnumber'] == 0:
            samples = Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 1:
            samples = Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            samples = Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            samples = Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            samples = Test_set5.objects.get(pk=request.session['quid'])

        request.session['start_time'] = time.time()
        return render(request, 'QuestionnaireColorCueNew/test_samples.html',{'samples':samples})

    else:
        if request.session['test_phase_flag'] == True and request.session['test_iteration']<4:
            request.session['test_phase_flag'] = False
            return render(request, "QuestionnaireColorCueNew/break.html")
        if request.session['test_phase_flag'] == True and request.session['test_iteration']>3:
            return render(request,"QuestionnaireColorCueNew/break_to_features.html")

        if request.session['setnumber'] == 0:
            request.session['test_samples'] = list(Test_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set1.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 1:
            request.session['test_samples'] = list(Test_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set2.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['test_samples'] = list(Test_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set3.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['test_samples'] = list(Test_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set4.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['test_samples'] = list(Test_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['test_samples'][0]
            samples = Test_set5.objects.get(pk=request.session['quid'])
            request.session['test_samples'] = request.session['test_samples'][1:]

        request.session['start_time'] = time.time()

        return render(request, 'QuestionnaireColorCueNew/test_samples.html', {'samples': samples})


def fixature_screen_test_type3(request):
    return render(request,"QuestionnaireColorCueNew/fixature_screen_test.html")

def common_features_test_phase_type3(request):
    return render(request,"QuestionnaireColorCueNew/common_features_test_phase.html")

def common_features_test_phase_block_type3(request):
    return render(request,"QuestionnaireColorCueNew/common_features_test_phase_block.html",{"iteration":request.session['common_features_iteration']})

def common_features_test_block_display_stimuli_type3(request):
    if request.method=="POST":
        option = request.POST.get("option",None)
        request.session['elapsed_time'] = time.time() - request.session['start_time']
        common_feature = CommonFeatureTable()
        common_feature.user_id = UserDetails.objects.get(pk=request.session['user_id'])
        common_feature.set_number = request.session['setnumber']
        common_feature.block_number = request.session['common_features_iteration']
        common_feature.sequence_number = 10 - len(request.session['common_features_test_samples'])
        common_feature.time_taken = request.session['elapsed_time']
        common_feature.timestamp = datetime.datetime.now()

        if len(request.session['common_features_test_samples']) == 0:
            request.session['common_features_iteration']+=1
            request.session['common_features_test_phase_flag'] = True


        if request.session['setnumber'] == 0:
            user_response = UserResponse_Common_Features_Test_set1()
            user_response.quid = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(
                Common_Features_Test_set1.objects.get(pk=request.session['quid']).sample_img.path)
            common_feature.file_name = "colorCue/set0/" + request.session['file_name']
        elif request.session['setnumber'] == 1:
            user_response = UserResponse_Common_Features_Test_set2()
            user_response.quid = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(
                Common_Features_Test_set2.objects.get(pk=request.session['quid']).sample_img.path)
            common_feature.file_name = "colorCue/set1/" + request.session['file_name']
        elif request.session['setnumber'] == 2:
            user_response = UserResponse_Common_Features_Test_set3()
            user_response.quid = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(
                Common_Features_Test_set3.objects.get(pk=request.session['quid']).sample_img.path)
            common_feature.file_name = "colorCue/set2/" + request.session['file_name']
        elif request.session['setnumber'] == 3:
            user_response = UserResponse_Common_Features_Test_set4()
            user_response.quid = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(
                Common_Features_Test_set4.objects.get(pk=request.session['quid']).sample_img.path)
            common_feature.file_name = "colorCue/set3/" + request.session['file_name']
        elif request.session['setnumber'] == 4:
            user_response = UserResponse_Common_Features_Test_set5()
            user_response.quid = Common_Features_Test_set5.objects.get(pk=request.session['quid'])
            request.session['file_name'] = str(
                Common_Features_Test_set5.objects.get(pk=request.session['quid']).sample_img.path)
            common_feature.file_name = "colorCue/set4/" + request.session['file_name']


        if option=="A":
            user_response.user_option = "A"
            request.session['correct_answer'] = "A"
            common_feature.user_option = "A"
        else:
            user_response.user_option = "B"
            request.session['correct_answer'] = "B"
            common_feature.user_option = "B"

        if request.session['file_name'].find("A") != -1:
            common_feature.correct_option = "A"
        else:
            common_feature.correct_option = "B"

        if option == common_feature.correct_option:
            common_feature.correct = 1
        else:
            common_feature.correct = 0


        user_response.iteration = request.session['common_features_iteration']
        user_response.user = UserDetails.objects.get(pk=request.session['user_id'])
        user_response.time_taken = request.session['elapsed_time']
        common_feature.time_taken = request.session['elapsed_time']
        user_response.save()
        common_feature.save()
        return render(request,"QuestionnaireColorCueNew/selected_option.html",{'correct_answer':request.session['correct_answer'],"timetaken":round(request.session['elapsed_time'],2)})

    if len(request.session['common_features_test_samples'])!=0:
        request.session['quid'] = request.session['common_features_test_samples'][0]
        request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]


        if request.session['setnumber'] == 0:
            samples = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 1:
            samples = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 2:
            samples = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 3:
            samples = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
        elif request.session['setnumber'] == 4:
            samples = Common_Features_Test_set5.objects.get(pk=request.session['quid'])

        request.session['start_time'] = time.time()
        return render(request, 'QuestionnaireColorCueNew/common_features_test_samples.html',{'samples':samples})

    else:
        if request.session['common_features_test_phase_flag'] == True and request.session['common_features_iteration']<4:
            request.session['common_features_test_phase_flag'] = False
            return render(request, "QuestionnaireColorCueNew/break_common_features.html")
        if request.session['common_features_test_phase_flag'] == True and request.session['common_features_iteration']>3:
            return render(request,"QuestionnaireColorCueNew/description.html")

        if request.session['setnumber'] == 0:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set1.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set1.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 1:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set2.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set2.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 2:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set3.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set3.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 3:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set4.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['common_features_test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set4.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]
        elif request.session['setnumber'] == 4:
            request.session['common_features_test_samples'] = list(Common_Features_Test_set5.objects.all().values_list('id', flat=True))
            random.shuffle(request.session['test_samples'])
            request.session['quid'] = request.session['common_features_test_samples'][0]
            samples = Common_Features_Test_set5.objects.get(pk=request.session['quid'])
            request.session['common_features_test_samples'] = request.session['common_features_test_samples'][1:]

        request.session['start_time'] = time.time()

        return render(request, 'QuestionnaireColorCueNew/common_features_test_samples.html', {'samples': samples})


def save_responses_description(request):
    if request.method == "POST":
        try:
            desc = request.POST.get('description', None)
            desc = desc.replace(',','$')
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
