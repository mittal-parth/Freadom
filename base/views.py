from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        
    return render(request, 'index.html')