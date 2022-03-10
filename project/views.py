from django.shortcuts import redirect


def firstpage(request):
    return redirect('/app/')

def second(request):
    return redirect('/app1/')