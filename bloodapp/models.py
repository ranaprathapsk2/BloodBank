from django.db import models

# Create your models here.

class hospitalDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=100, null=True, blank=True)
    Number = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="HospitalImages")
    Address = models.CharField(max_length=1000, null=True, blank=True)

class BloodDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    ONeg = models.IntegerField(null=True, blank=True)
    OPos = models.IntegerField(null=True, blank=True)
    ANeg = models.IntegerField(null=True, blank=True)
    APos = models.IntegerField(null=True, blank=True)
    BNeg = models.IntegerField(null=True, blank=True)
    BPos = models.IntegerField(null=True, blank=True)
    ABNeg = models.IntegerField(null=True, blank=True)
    ABPos = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="HospitalImage",null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class RequestBD(models.Model):
    Email = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Bystander = models.CharField(max_length=100, null=True, blank=True)
    BloodGroup = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=100,null=True, blank=True)
    Date = models.CharField(max_length=100, null=True, blank=True)
    ContactNumber = models.IntegerField(null=True, blank=True)
    Hospital = models.CharField(max_length=300, null=True, blank=True)
    Place = models.CharField(max_length=300, null=True, blank=True)
    Reason = models.CharField(max_length=300, null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class RegisterDB(models.Model):
    Email = models.CharField(max_length=200,null=True,blank=True)
    Name = models.CharField(max_length=200,null=True,blank=True)
    BloodGroup = models.CharField(max_length=200,null=True,blank=True)
    Password = models.CharField(max_length=200,null=True,blank=True)
    LastName = models.CharField(max_length=200,null=True,blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    Place = models.CharField(max_length=200,null=True,blank=True)
    Gender = models.CharField(max_length=200,null=True,blank=True)
    Age = models.IntegerField(null=True, blank=True)
    MobileNumber = models.IntegerField(null=True, blank=True)
    RePassword = models.CharField(max_length=200,null=True,blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class BloodDonation(models.Model):
    Email = models.CharField(max_length=200,null=True,blank=True)
    Name = models.CharField(max_length=200,null=True,blank=True)
    LastName = models.CharField(max_length=200,null=True,blank=True)
    Age = models.IntegerField(null=True, blank=True)
    District = models.CharField(max_length=200,null=True,blank=True)
    Place = models.CharField(max_length=200,null=True,blank=True)
    Gender = models.CharField(max_length=200,null=True,blank=True)
    BloodGroup = models.CharField(max_length=200,null=True,blank=True)
    MobileNumber = models.IntegerField(null=True, blank=True)
    BloodBank = models.CharField(max_length=200,null=True,blank=True)
    Diseases = models.CharField(max_length=200,null=True,blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class OldRequestBD(models.Model):
    Email = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Bystander = models.CharField(max_length=100, null=True, blank=True)
    BloodGroup = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=100,null=True, blank=True)
    Date = models.CharField(max_length=100, null=True, blank=True)
    ContactNumber = models.IntegerField(null=True, blank=True)
    Hospital = models.CharField(max_length=300, null=True, blank=True)
    Place = models.CharField(max_length=300, null=True, blank=True)
    Reason = models.CharField(max_length=300, null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)


class AdminActivity(models.Model):
    AdminName = models.CharField(max_length=1000,null=True,blank=True)
    Action = models.CharField(max_length=100,null=True,blank=True)
    Time = models.DateTimeField(null=True,blank=True)


class UserActivity(models.Model):
    Email = models.EmailField(null=True,blank=True)
    Action = models.CharField(max_length=100,null=True,blank=True)
    Time = models.DateTimeField(null=True,blank=True)

class VolunteerDB(models.Model):
    Email = models.CharField(max_length=100, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Cv = models.ImageField(upload_to="Cv")
    Message = models.CharField(max_length=100, null=True, blank=True)

class FaqDB(models.Model):
    Title = models.CharField(max_length=1000, null=True, blank=True)
    Text = models.CharField(max_length=5000, null=True, blank=True)

class ArticleDB(models.Model):
    Title = models.CharField(max_length=1000, null=True, blank=True)
    Author = models.CharField(max_length=100, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="ArticleImage")
    Paragraph1 = models.CharField(max_length=5000, null=True, blank=True)
    Paragraph2 = models.CharField(max_length=5000, null=True, blank=True)
    Paragraph3 = models.CharField(max_length=5000, null=True, blank=True)
    Time = models.DateTimeField(null=True,blank=True)

class ContactDB(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=200, null=True, blank=True)
    Message = models.CharField(max_length=1000, null=True, blank=True)


class CommentDB(models.Model):
    Idd = models.CharField(max_length=200, null=True, blank=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Comment = models.CharField(max_length=2000, null=True, blank=True)

class QuestionDB(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Question = models.CharField(max_length=2000, null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class QuestionCommentDB(models.Model):
    Idd = models.CharField(max_length=200, null=True, blank=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Comment = models.CharField(max_length=2000, null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)

class RequestCommentDB(models.Model):
    Idd = models.CharField(max_length=200, null=True, blank=True)
    Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Comment = models.CharField(max_length=2000, null=True, blank=True)
    Time = models.DateTimeField(null=True, blank=True)