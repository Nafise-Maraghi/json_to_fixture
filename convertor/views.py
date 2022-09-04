from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import json

from .forms import ConvertorForm


def json_to_fixture(file, model_name):
    try:
        records = json.load(file)
        container = list()
        i = 1

        for record in records:
            d = {'model': model_name, 'pk': i, 'fields': record}
            container.append(d)
            i += 1

        with open(f"output/{file.name}", 'w') as output:
            json.dump(container, output)

            return True

    except:
        return False


class ConvertorView(View):
    def post(self, request):
        form = ConvertorForm(data=request.POST, files=request.FILES)

        if form.is_valid:
            file = request.FILES["file"]
            model_name = request.POST["model_name"]
            result = json_to_fixture(file, model_name)

            if result:
                message = "Your fixture is ready! You can find it in \"output\" folder in the root."

            else:
                message = "Sorry! There is something wrong with your data."

            return render(request, 'conversion.html', {"message": message})

    def get(self, request):
        return render(request, 'conversion.html', {"form": ConvertorForm()})
