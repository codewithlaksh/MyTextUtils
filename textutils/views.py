# from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import string

def home(request):
    # return HttpResponse("Hello World!")
    return render(request, "index.html")

@csrf_exempt
def analyze(request):
    if request.method == "POST":
        text = request.POST.get("text")
        cuppercase = request.POST.get("cuppercase", "off")
        clowercase = request.POST.get("clowercase", "off")
        ctitlecase = request.POST.get("ctitlecase", "off")
        ccamelcase = request.POST.get("ccamelcase", "off")
        removeExtraSpaces = request.POST.get("removeExtraSpaces", "off")
        removeSpecialChars = request.POST.get("removeSpecialChars", "off")
        removeNewLines = request.POST.get("removeNewLines", "off")
        analyzed = ""
        context = {}

        if cuppercase == "on":
            analyzed += text.upper()
            context["analyzed"] = analyzed
            context["purpose"] = "Convert to upper case"

        elif clowercase == "on":
            analyzed += text.lower()
            context["analyzed"] = analyzed
            context["purpose"] = "Convert to lower case"

        elif ctitlecase == "on":
            analyzed += text.title()
            context["analyzed"] = analyzed
            context["purpose"] = "Convert to title case"

        elif ccamelcase == "on":
            l = text.split()
            for i in range(0, len(l)):
                l[i] = l[i][0].upper() + l[i][1:]
            analyzed += "".join(l)
            context["analyzed"] = analyzed
            context["purpose"] = "Convert to camel case"

        elif removeExtraSpaces == "on":
            analyzed += " ".join(text.split())
            context["analyzed"] = analyzed
            context["purpose"] = "Remove extra spaces"

        elif removeSpecialChars == "on":
            chars = string.punctuation
            for char in text:
                if char not in chars:
                    analyzed += char
            context["analyzed"] = analyzed
            context["purpose"] = "Remove extra spaces"

        elif removeNewLines == "on":
            for char in text:
                if char != "\n":
                    analyzed += char
            context["analyzed"] = analyzed
            context["purpose"] = "Remove new lines"

        return render(request, "analyzed.html", context)