from django.shortcuts import render

def sold_item(request):
    return render(request, 'sold_item.html')


def return_item(request):
    return render(request, 'return_item.html')