from django.contrib import admin
from  .models import company , job_offers ,Profile

# Register your models here.
admin.site.register(company)
admin.site.register(job_offers)
admin.site.register(Profile)
