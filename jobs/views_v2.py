"""

django.views.generic
"""

from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from jobs.models import Applicant


class ApplicantList(ListView):
    model = Applicant


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("ap_list")
