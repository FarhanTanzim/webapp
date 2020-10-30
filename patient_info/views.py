from django.shortcuts import render

from django.http import HttpResponse

import json
# Create your views here.

def homePageView(request):
    with open('patient_info\patient-fixed.json') as f:
      data = json.load(f)
    name = "Name of patient: "
    org = "Organization name: "
    gender = "Gender: "
    num_cond = "Number of conditions they have: "
    conds = "List of all conditions:<br>"

    name += data.get("name")[0].get("given")[0] + " "
    name += data.get("name")[0].get("family")[0]
    gender += data.get("gender")
    org += data.get("managingOrganization").get("display")
    num_cond += str(len(data.get("conditions")))
    for condition in data.get("conditions"):
        conds += "-"
        conds += condition
        conds += "<br>"
    return HttpResponse(name + "<br>" \
                        + org + "<br>" \
                        + gender + "<br>" \
                        + num_cond + "<br>" \
                        + conds
                        )
