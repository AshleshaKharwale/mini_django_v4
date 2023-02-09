"""

django.views.generic
"""

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from jobs.models import Applicant


class ApplicantList(ListView):
    model = Applicant


class ApplicantDetails(DetailView):
    model = Applicant

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['applicant_list'] = Applicant.objects.all()
        return context


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("ap_list")


class ApplicantCreate(CreateView):
    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("ap_list")


class ApplicantDelete(DeleteView):
    model = Applicant
    success_url = reverse_lazy("ap_list")
