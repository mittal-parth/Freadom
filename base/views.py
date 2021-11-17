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
        output = run([sys.executable,'D:\\PARTH DATA\\WEB DEVELOPMENT\\WEC Recruitment Tasks\\web_scraper\\script.py',url], shell=False, stdout=PIPE)
        file_path = "D:\\PARTH DATA\\WEB DEVELOPMENT\\WEC Recruitment Tasks\\web_scraper\\media\\web_scraper_result.docx"

        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename=web_scraper_result.docx'
                return response
        # response = HttpResponse("D:\\PARTH DATA\\WEB DEVELOPMENT\\WEC Recruitment Tasks\\web_scraper\\web_scraper_result.docx", content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        # response['Content-Disposition'] = "attachment; filename=result.docx"
        # return response
    return render(request, 'index.html')