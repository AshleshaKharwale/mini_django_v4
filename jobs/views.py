import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Portal, JobDescription, JobTitle
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def get_portal_details(request):
    details = Portal.objects.order_by("id")
    # getting url associated with django view
    from django.urls import reverse
    print(reverse("portal_details"))  # name given to url in urls.py

    portals = [obj.name for obj in details]

    return JsonResponse(portals, safe=False)


def welcome(request):
    return render(request, "jobs/welcome.html")


@csrf_exempt
def job_titles(request):
    """plural endpoint for getting all job titles"""

    if request.method == "POST":
        data = json.loads(request.body)

        # TODO: perform a check if certain job_title already exist
        # TODO: if title exists, return a message.
        try:
            title_ = data.get("title")
            title_obj = JobTitle.objects.filter(title=title_)
        except ObjectDoesNotExist:
            title_obj = None

        if title_obj:
            return HttpResponse(f"<p> {title_} already exist in our database!</p>")
        else:
            # Portal Foreign key
            portal_data = data.get("portal")
            portal_name = portal_data.get("name")
            portal = Portal.objects.filter(name=portal_name)

            if not Portal:
                portal = Portal.objects.create(**portal_data)
                portal.save()
            else:
                portal = portal[0]

            # JobDescription One-to-one key
            jd = data.get("job_description")
            jd = JobDescription.objects.create(**jd)
            jd.save()

            # JobTitle
            data["job_description"] = jd
            data["portal"] = portal
            jt = JobTitle.objects.create(**data)
            jt.save()

    jt = JobTitle.objects.all()
    return render(request, "jobs/job_titles.html", {"job_titles": jt})


def get_job_description(request, job_id):
    try:
        jd = JobDescription.objects.get(id=job_id)
    except ObjectDoesNotExist:
        jd = None
    return render(request, "jobs/job_description.html", {"job_desc": jd, "job_id": job_id})
