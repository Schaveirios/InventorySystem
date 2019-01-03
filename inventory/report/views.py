from django.shortcuts import render, redirect
from .forms import WeeklyReportForm


def weeklyReport(request):
    context={}
    return render(request, 'weekly_report.html', context)


def monthlyReport(request):
    context={}
    return render(request, 'monthly_report.html', context)


def yearlyReport(request):
    context={}
    return render(request, 'yearly_report.html', context)