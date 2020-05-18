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

    def __str__(self):
        return self.first_name+' '+self.last_name

class SetNumber(models.Model):

    class Meta:
        verbose_name_plural = "Set Number"

    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=None, blank=True)
    set_num = models.CharField(max_length=10,blank=True,null=True,default=None)

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