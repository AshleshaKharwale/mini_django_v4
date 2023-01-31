from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import JobTitle
from .serializers import JobTitleSerializer, JobDescriptionSerializer, PortalSerializer


@csrf_exempt
def jobtitle_list(request):
    if request.method == "GET":
        job_titles = JobTitle.objects.all()
        serializer = JobTitleSerializer(job_titles, many=True)

        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        parser = JSONParser()
        title_data = parser.parse(request)

        # job description data
        jd = title_data.get("job_description")
        jd_data_serializer = JobDescriptionSerializer(data=jd)

        # portal data
        portal = title_data.get("portal")
        portal_data_serializer = PortalSerializer(data=portal)

        # job title data
        title_data["job_description"] = jd_data_serializer
        title_data["portal"] = portal_data_serializer
        title_data_serializer = JobTitleSerializer(data=title_data)

        status_code = 500
        message = "[Validation Error] Data could not be created."

        if title_data_serializer.is_valid() and portal_data_serializer.is_valid() and jd_data_serializer.is_valid():

            title_data_serializer.save()
            portal_data_serializer.save()  # creates data in the database with serialized data
            jd_data_serializer.save()  # calls create() function of JobDescriptionSerializer and
            # creates data in the database with serialized data

            message = "Data created successfully"
            status_code = 201

        response = {
            "message": message,
            "Status code": status_code
        }
        return JsonResponse(response)
