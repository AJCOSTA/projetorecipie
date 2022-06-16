from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('isso é o home2')


def sobre(request):
    return HttpResponse('isso é o sobre')


def contato(request):
    return HttpResponse('isso é o contato')
