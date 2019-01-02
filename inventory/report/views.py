from django.shortcuts import render, redirect
from .forms import WeeklyReportForm


def weeklyReport(request):
    context={
        'reportForm': WeeklyReportForm(),
    }
    return render(request, 'weekly_report.html', context)