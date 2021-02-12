import json
import os
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse, Http404
from django.views.decorators.http import require_http_methods, require_GET
from .forms import Quantity
from .models import Employee, AsyncResults
from .tasks import createCSV
from django.conf import settings
# Create your views here.

@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        form = Quantity(request.POST)
        if form.is_valid():
            q = form.cleaned_data['quantity']
            if int(q) < 50:
                return redirect('result', amount=int(q))
            else:
                task = createCSV.delay(amount=int(q))
                context = {
                    'message': 'Your request is being processed, go to downloads to get your link'
                }
                return render(request, 'message.html', context)
                
    else:
        context = {
            'form': Quantity
        }
        return render(request, 'form.html', context)


@require_GET
def result(request, amount):
    employees = Employee.objects.all()[:int(amount)]
    context = {
        'employees': employees
    }
    return render(request, 'tables.html', context)


@require_GET
def downloads(request):
    async_result = AsyncResults.objects.all().order_by('-created_on')
    if len(async_result) > 0:
        time = ''
        created_on = async_result.created_on
        now = datetime.now()

        if now.hour - created_on.hour != 0:
            time = str(now.hour - creted_on.hour) + ' ' + 'hours ago'
        else:
            time = str(now.minute - created_on.minute) + ' ' + 'minutes ago'

        context = {
            'tasks':  async_result,
            'time': time
        }
        return render(request, 'downloads.html', context)

    else:
        return render(request, 'message.html', context={'message': 'You either have no files to downlaod or your file is not processed yet. Come again later'})

@require_GET
def file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

