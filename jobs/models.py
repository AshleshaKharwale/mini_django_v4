from django.db import models
from django.utils import timezone

# Create your models here.


class Portal(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    title = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now)
    job_description = models.OneToOneField("JobDescription", on_delete=models.CASCADE)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + f"({self.portal})"


class JobDescription(models.Model):
    role = models.CharField(max_length=250)
    description_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.role

    def __repr__(self):
        return self.role + f"({self.pub_date})"


class Applicant(models.Model):
    name = models.CharField(max_length=250, default="")
    applied_for = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    cover_letter = models.TextField()

    def __str__(self):
        return self.name
