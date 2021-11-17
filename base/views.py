from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
import sys
import os
from subprocess import run, PIPE

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname,'script.py')
        output = run([sys.executable,filename,url], shell=False, stdout=PIPE)
        
        file_path = os.getcwd() + '\\media\\webscraper_result.docx'

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename=web_scraper_result.docx'
                return response
        else:
            return HttpResponse('Oops! Something went wrong.')
    return render(request, 'index.html')