from django.db import models

# Create your models here.
class UserDetails(models.Model):

    class Meta:
        verbose_name_plural = "User Details"

    first_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    last_name = models.CharField(max_length=100,blank=True,null=True,default=None)
    email = models.EmailField()
    gender = models.CharField(max_length=10,blank=True,null=True,default=None)
    city = models.CharField(max_length=100,blank=True,null=True,default=None)
    country = models.CharField(max_length=100,blank=True,null=True,default=None)
    age = models.IntegerField(blank=True, null=True, default=None)
    set_num = models.CharField(max_length=10,blank=True,null=True,default=None)

    def __str__(self):
        return self.first_name+' '+self.last_name


class Observe_And_Learn_Samples_set1(models.Model):

    class Meta:
        verbose_name_plural = "Observe and Learn Samples Set 1"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Observe_And_Learn_Samples_set2(models.Model):

    class Meta:
        verbose_name_plural = "Observe and Learn Samples Set 2"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Observe_And_Learn_Samples_set3(models.Model):

    class Meta:
        verbose_name_plural = "Observe and Learn Samples Set 3"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Observe_And_Learn_Samples_set4(models.Model):

    class Meta:
        verbose_name_plural = "Observe and Learn Samples Set 4"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Observe_And_Learn_Samples_set5(models.Model):

    class Meta:
        verbose_name_plural = "Observe and Learn Samples Set 5"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)


class Classify_And_Learn_Samples_set1(models.Model):

    class Meta:
        verbose_name_plural = "Classify and Learn Samples Set 1"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Classify_And_Learn_Samples_set2(models.Model):

    class Meta:
        verbose_name_plural = "Classify and Learn Samples Set 2"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Classify_And_Learn_Samples_set3(models.Model):

    class Meta:
        verbose_name_plural = "Classify and Learn Samples Set 3"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Classify_And_Learn_Samples_set4(models.Model):

    class Meta:
        verbose_name_plural = "Classify and Learn Samples Set 4"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Classify_And_Learn_Samples_set5(models.Model):

    class Meta:
        verbose_name_plural = "Classify and Learn Samples Set 5"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Test_set1(models.Model):

    class Meta:
        verbose_name_plural = "Test Samples Set 1"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Test_set2(models.Model):

    class Meta:
        verbose_name_plural = "Test Samples Set 2"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Test_set3(models.Model):

    class Meta:
        verbose_name_plural = "Test Samples Set 3"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Test_set4(models.Model):

    class Meta:
        verbose_name_plural = "Test Samples Set 4"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Test_set5(models.Model):

    class Meta:
        verbose_name_plural = "Test Samples Set 5"

    sample_img = models.ImageField(upload_to='images/')
    sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class UserResponse_Test_set1(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Test phase set 1"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Test_set1, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)


class UserResponse_Test_set2(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Test phase set 2"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Test_set2, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)

class UserResponse_Test_set3(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Test phase set 3"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Test_set3, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)

class UserResponse_Test_set4(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Test phase set 4"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Test_set4, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)

class UserResponse_Test_set5(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Test phase set 5"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Test_set5, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)


class Common_Features_Test_set1(models.Model):

    class Meta:
        verbose_name_plural = "Common Features Test Samples Set 1"

    sample_img = models.ImageField(upload_to='images/')
    # sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Common_Features_Test_set2(models.Model):

    class Meta:
        verbose_name_plural = "Common Features Test Samples Set 2"

    sample_img = models.ImageField(upload_to='images/')
    # sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Common_Features_Test_set3(models.Model):

    class Meta:
        verbose_name_plural = "Common Features Test Samples Set 3"

    sample_img = models.ImageField(upload_to='images/')
    # sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Common_Features_Test_set4(models.Model):

    class Meta:
        verbose_name_plural = "Common Features Test Samples Set 4"

    sample_img = models.ImageField(upload_to='images/')
    # sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class Common_Features_Test_set5(models.Model):

    class Meta:
        verbose_name_plural = "Common Features Test Samples Set 5"

    sample_img = models.ImageField(upload_to='images/')
    # sample_label = models.CharField(max_length=10,blank=True,null=True,default=None)

class UserResponse_Common_Features_Test_set1(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Common Features Test phase set 1"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Common_Features_Test_set1, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)


class UserResponse_Common_Features_Test_set2(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Common Features Test phase set 2"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Common_Features_Test_set2, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)

class UserResponse_Common_Features_Test_set3(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Common Features Test phase set 3"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Common_Features_Test_set3, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)

class UserResponse_Common_Features_Test_set4(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Common Features Test phase set 4"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Common_Features_Test_set4, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)

class UserResponse_Common_Features_Test_set5(models.Model):

    class Meta:
        verbose_name_plural = "User Response for Common Features Test phase set 5"

    user_option = models.CharField(max_length=10,default=None)
    quid = models.ForeignKey(Common_Features_Test_set5, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    iteration = models.IntegerField(default=1)
    time_taken = models.FloatField(default=None, blank=False)


class UserResponsesForDescription(models.Model):

    class Meta:
        verbose_name_plural = "User Responses for Description"

    description = models.TextField(default=None, null=True, blank=True)
    set_number = models.CharField(max_length=10,blank=True,null=True,default=None)

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)

class TransferStimuliTable(models.Model):

    class Meta:
        verbose_name_plural = "Transfer Stimuli Table"

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    set_number = models.IntegerField(default=None,blank=False)
    block_number = models.IntegerField(default=None,blank=False)
    sequence_number = models.IntegerField(default=None,blank=False)
    file_name = models.CharField(max_length=150,blank=False,default=None)
    user_option = models.CharField(max_length=10, default=None)
    rule_based = models.IntegerField(default=None,blank=False)
    time_taken = models.FloatField(default=None, blank=False)
    timestamp = models.DateTimeField(auto_now_add= True,editable=False, null=False, blank=False)

class CommonFeatureTable(models.Model):

    class Meta:
        verbose_name_plural = "Common Feature Test Table"

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    set_number = models.IntegerField(default=None,blank=False)
    block_number = models.IntegerField(default=None,blank=False)
    sequence_number = models.IntegerField(default=None,blank=False)
    file_name = models.CharField(max_length=150,blank=False,default=None)
    user_option = models.CharField(max_length=10, default=None)
    correct_option = models.CharField(max_length=10, default=None)
    correct = models.IntegerField(default=None,blank=False)
    time_taken = models.FloatField(default=None, blank=False)
    timestamp = models.DateTimeField(auto_now_add= True)


class ClassifyStimuiTable(models.Model):

    class Meta:
        verbose_name_plural = "Classify Stimluli Table"

    user_id = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    set_number = models.IntegerField(default=None, blank=False)
    block_number = models.IntegerField(default=None, blank=False)
    sequence_number = models.IntegerField(default=None, blank=False)
    file_name = models.CharField(max_length=150, blank=False, default=None)
    user_option = models.CharField(max_length=10, default=None)
    correct = models.IntegerField(default=None, blank=False)
    time_taken = models.FloatField(default=None, blank=False)
    timestamp = models.DateTimeField(editable=True, null=False, blank=False)
