from django.shortcuts import render, redirect
from django.contrib import messages


def weeklyReport(request):
    context={}
    
    return render(request, "weekly_report.html", context)
