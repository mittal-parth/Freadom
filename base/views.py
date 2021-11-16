from django.shortcuts import render
import requests, sys
from subprocess import run, PIPE

# Create your views here.
def index(request):
    context = {'output':''}
    if request.method == 'POST':
        url = request.POST.get('url')
        output = run([sys.executable,'D:\\PARTH DATA\\WEB DEVELOPMENT\\WEC Recruitment Tasks\\web_scraper\\script.py',url], shell=False, stdout=PIPE)
        context = {'output':output.stdout}
    return render(request, 'index.html', context)