from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Applicant
from django.contrib.auth.models import User


class Applicants(APIView):

    def get(self, request):
        applicants = Applicant.objects.all()
        applicants_api = {}
        for applicant in applicants:
            applicants_api[applicant.id] = {
                "name": applicant.name,
                "applied_for": {
                    "title": applicant.applied_for.title,
                    "job_description": {
                        "role": applicant.applied_for.job_description.role,
                        "description_text": applicant.applied_for.job_description.description_text
                    },
                    "portal": applicant.applied_for.portal.name
                },
                "cover_letter": applicant.cover_letter
            },

        return Response(applicants_api)
