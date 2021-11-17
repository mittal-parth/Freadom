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
        dirname = os.path.dirname(__file__)
        script = os.path.join(dirname,'script.py')
        output = run([sys.executable,script,url], shell=False, stdout=PIPE)
        
        document = build_document(output)
        # save document info
        buffer = io.BytesIO()
        document.save(buffer)  # save your memory stream
        buffer.seek(0)  # rewind the stream

        # put them to streaming content response 
        # within docx content_type
        response = StreamingHttpResponse(
            streaming_content=buffer,  # use the stream's content
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=web_scraper_result.docx'
        return response
    return render(request, 'index.html')

def build_document(output):
    document = Document()
    document.add_paragraph(output.stdout.decode('unicode_escape'))
    return document