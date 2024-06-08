from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
challenges = {
    "january": "Complete a new certification in backend development",
    "february": "Contribute to an open-source project",
    "march": "Run a half marathon",
    "april": "Build a personal website from scratch",
    "may": "Learn a new programming language (e.g., Rust or Kotlin)",
    "june": "Read a technical book on AI or Machine Learning",
    "july": "Create a Dockerized full-stack application",
    "august": "Take a vacation and explore a new city",
    "september": "Complete a complex problem set on LeetCode",
    "october": None,
    "november": "Write a blog post series about your software engineering experiences",
    "december": None
}

# main page hard-code to display list of months



def index1(request):
    string = ""
    months = list(challenges.keys())

    for month in months:
        captlized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        string += f"<li><a href=\"{month_path}\">{captlized_month}</a></li>"

    response_data = f"<ul>{string} </ul>"

    return HttpResponse(response_data)

# main page using Templates to display a HTML file


def index2(request):

    return render(request, "challenges/main.htm")


# main page using Tags
def index3(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.htm", {
        "months": months,
        "challenges": challenges
    })

# use to redirect the url from number to month
# 5 => May


def challenges_month_by_number(request, month):

    months = list(challenges.keys())

    if month > len(challenges):
        return HttpResponseNotFound("<h1>This is invalid month !!</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/march

    return HttpResponseRedirect(redirect_path)

# challenges.htm


def challenges_month(request, month):
    try:
        challenge_text = challenges[month]
        month_text = month.capitalize()
        # return HttpResponse("<h1>"+challenges[month]+"</h1>")
        # return HttpResponse(render_to_string("challenges/challenges.htm"))
        return render(request, "challenges/challenge.htm", {"challenge_text": challenge_text, "month_text": month})
    except:
        response_data = render_to_string("404.html")
        # # return HttpResponseNotFound("<h1>This is invalid month !!</h1>")
         
        return HttpResponseNotFound(response_data)
        
        
        #raise Http404()
