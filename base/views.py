from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, StreamingHttpResponse
import requests
import sys
import os
import io
from docx import Document
from datetime import datetime
from subprocess import run, PIPE

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print(url)
        #get path to scraping script
        dirname = os.path.dirname(__file__)
        script = os.path.join(dirname,'script.py')

        #run the script
        output = run([sys.executable,script,url], shell=False, stdout=PIPE)

        document = build_document(output)

        # save document info wihtout creating a file on server side
        buffer = io.BytesIO()
        document.save(buffer) 
        buffer.seek(0)  

        # put them to streaming content response 
        # within docx content_type
        response = StreamingHttpResponse(
            streaming_content=buffer, 
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=web_scraper_result.docx'
        return response
    return render(request, 'index.html')

def build_document(output):
    document = Document()
    document.add_paragraph(output.stdout.decode('unicode_escape'))
    return document