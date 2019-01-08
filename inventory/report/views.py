from django.shortcuts import render, redirect
from .forms import WeeklyReportForm, MonthlyReportForm, AnnualReportForm
from transaction.models import PurchasedItem
from datetime import datetime, timedelta, date
from django.contrib import messages
from calendar import monthrange
import html.parser as htmlparser

def weeklyReport(request):

    purchaseditems = PurchasedItem.objects.all()
    daily_sales=[]

    if request.method == 'POST':
        form = WeeklyReportForm(request.POST)
        if form.is_valid():
            print("Validated")

            weeklyform = form.cleaned_data
            weekNumber = weeklyform.get("weekNumber")
            year = weeklyform.get("year")

            week_start = datetime.strptime(str(year)+"-W"+str(weekNumber)+"-1", "%Y-W%W-%w")
            week_end = week_start+timedelta(days=6)
            # purchaseditems2 = purchaseditems.filter(date__gte=week_start).exclude(date__gt=week_end)

            for index in range(7):
                purchases = purchaseditems.filter(date=week_start+timedelta(days=index))
                temp = 0
                for entry in purchases:
                    temp += entry.quantity*entry.item.retailPrice
                daily_sales += [float(temp)]

            date_range = str(week_start.year)+"-"+str(week_start.month)+"-"+str(week_start.day)+"    to    "+str(week_end.year)+"-"+str(week_end.month)+"-"+str(week_end.day)

            context={
                "WeeklyReportForm":WeeklyReportForm,
                "daily_sales":daily_sales,
                "DateDisplayed":date_range,
                }

            return render(request, 'weekly_report.html', context)

        else:
            messages.warning(request, "INVALID INPUT")
            print(form.errors)
            return redirect("/report/weekly")


    context={
        "WeeklyReportForm":WeeklyReportForm,
        "daily_sales":daily_sales,
        }

    return render(request, 'weekly_report.html', context)


def monthlyReport(request):
    
    parser = htmlparser.HTMLParser()

    monthly_sales = []
    month_days = []
    for x in range(1,32):
        month_days += [parser.unescape('day '+str(x))]

    if request.method == 'POST':
        form = MonthlyReportForm(request.POST)
        if form.is_valid():
            print("Validated")

            monthlyreport = form.cleaned_data
            month = int(monthlyreport.get('month'))
            year = int(monthlyreport.get('year'))

            purchaseditems = PurchasedItem.objects.filter(date__year=year, date__month=month)
            month_start = date(year,month,1)
            month_number_days = monthrange(year, month)[1]

            month_name = date(year,month,1).strftime("%b")
            month_days = []
            for x in range(1,32):
                month_days += [month_name+" "+str(x)]


            for index in range(month_number_days):
                purchases = purchaseditems.filter(date=month_start+timedelta(days=index))
                temp = 0
                for entry in purchases:
                    temp += entry.quantity*entry.item.retailPrice
                monthly_sales += [float(temp)]

            context={
                'MonthlyReportForm':MonthlyReportForm,
                'monthly_sales':monthly_sales,
                'month_days':month_days,
                'YearDisplayed':"Year "+str(year),
            }
            return render(request, 'monthly_report.html', context)

        else:
            messages.warning(request, "INVALID INPUT")
            print(form.errors)
            return redirect("/report/monthly")
        
    
    context={
        'MonthlyReportForm':MonthlyReportForm,
        'monthly_sales':monthly_sales,
        'month_days':month_days,
    }
    return render(request, 'monthly_report.html', context)


def yearlyReport(request):

    annual_sales = []

    if request.method == "POST":
        form = AnnualReportForm(request.POST)
        if form.is_valid():
            annualreport = form.cleaned_data
            year = int(annualreport.get('year'))

            purchaseditems = PurchasedItem.objects.filter(date__year=year)

            for index in range(1,13):
                purchases = purchaseditems.filter(date__month=index)
                temp = 0
                for entry in purchases:
                    temp += entry.quantity*entry.item.retailPrice
                annual_sales += [float(temp)]
            
            context={
                'AnnualReportForm':AnnualReportForm,
                'annual_sales':annual_sales,
                'YearDisplayed':"Year "+str(year),
                }
            return render(request, 'yearly_report.html', context)

        else:
            messages.warning(request, "INVALID INPUT")
            print(form.errors)
            return redirect("/report/annual")

    context={
        'AnnualReportForm':AnnualReportForm,
        'annual_sales':annual_sales,
        }
    return render(request, 'yearly_report.html', context)