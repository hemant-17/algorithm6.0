from django.db import models
from multiselectfield import MultiSelectField
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

skills = [('c','c') , ('java','java') , ('c++','c++') , ('python','python') , ('androiddevelopment','androiddevelopment') ,('webdevelopment','webdevelopment'),]
ed = [('SSC','SSC') , ('HSC','HSC') , ('Graduate','Graduate') , ('Diploma','Diploma') , ('B.E','B.E') , ('B.Tech','B.Tech'),]
# Create your models here.
class company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100, null=False, blank=False, default='devalappers')
    desc = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(blank=False)
    img = models.ImageField()
    def __str__(self):
        return self.company_name

class job_offers(models.Model):
    company_id = models.ForeignKey(company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    job_desc = models.CharField(max_length=100, null=False, blank=False)
    skills_required = MultiSelectField(choices=skills)
    education = MultiSelectField(choices=ed)
    education_years = models.IntegerField(blank=False, null=False)
    vacancy = models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.job_title

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE, related_name='profile')

    company_id = models.ForeignKey(to=company , on_delete=models.CASCADE , null = True , blank = True)

@receiver(post_save , sender=User)
def create_profile_for_user(sender , instance , created, **kwargs):
    if created:
        profile = Profile.objects.get_or_create(user=instance )
        instance.profile.save()

post_save.connect(create_profile_for_user, sender=User)
