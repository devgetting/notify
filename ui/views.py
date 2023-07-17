from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'ui/index.html')

def sender(request):
    return render(request, 'ui/sender.html')