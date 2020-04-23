from django.db import models
from multiselectfield import MultiSelectField
SKILLS_CHOICES=(('c','c'),
               ('java','java'),
               ('c++','c++'),
               ('python','python'),
               ('webdevelopment','webdevelopment'),
               ('andrioddevelopment','andrioddevelopment'),)

COURSES_CHOICES = (('c','c'),
                  ('java','java'),
                  ('c++','c++'),
                  ('python','python'),
                  ('webdevelopment','webdevelopment'),
                  ('andrioddevelopment','andrioddevelopment'),)
APPLY_JOBS = (('123','123'),
             ('1234','1234'),
             ('12345','12345'),)
EDUCATION = (('SSC','SSC'),
            ('HSC','HSC'),
            ('Graduate','Graduate'),
            ('Diploma','Diploma'),
            ('B.E','B.E'),
            ('B.Tech','B.Tech'),)

class StudentUser(models.Model):

    Uid = models.AutoField
    username = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    education = MultiSelectField(choices=EDUCATION)
    experience = models.IntegerField(null=True)
    industry =  models.CharField(max_length=200,null=True)
    location =  models.CharField(max_length=200,null=True)
    skills = MultiSelectField(choices=SKILLS_CHOICES)
    course = MultiSelectField(choices=COURSES_CHOICES)
    applyjobs = MultiSelectField(choices=APPLY_JOBS)
    totalProject = models.IntegerField(null=True)
    english = models.CharField(max_length=200,null=True)
    availability = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='student/images', default="")

    def __str__(self):
        return self.username

class MyCourses(models.Model):
    cid = models.IntegerField(null=True)
    cname = models.CharField(max_length=200,null=True)
    description = models.CharField(max_length=400,null=True)
    status = models.IntegerField(null=True)
    perform = models.IntegerField(null=True)
    def __str__(self):
        return self.cname

class Perform (models.Model):
    uid = models.IntegerField(null=True)
    cid = models.IntegerField(null=True)
    perform = models.IntegerField(null=True)

class applicants(models.Model):
    username = models.CharField(max_length=200,null=True)
    title =models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.username





class project(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100)
    p_desc = models.CharField(max_length=5000,null=True,blank=True)
    fund =  models.CharField(max_length=100,null=True,blank=True)