from django.contrib import admin
from .models import Portal, JobTitle, JobDescription, Applicant
# Register your models here.

admin.site.register(Portal)
admin.site.register(JobTitle)
admin.site.register(JobDescription)
admin.site.register(Applicant)
