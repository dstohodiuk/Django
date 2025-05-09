from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html')


def view1(request):
    return render(request, 'store/view1.html')


def view2(request):
    return render(request, 'store/view2.html')


def view3(request):
    return render(request, 'store/view3.html')


def view4(request):
    return render(request, 'store/view4.html')


def view5(request):
    return render(request, 'store/view5.html')
