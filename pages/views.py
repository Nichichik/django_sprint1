from django.shortcuts import render


def about(request):
    return render(request, 'html/about.html')


def rules(request):
    return render(request, 'html/rules.html')
