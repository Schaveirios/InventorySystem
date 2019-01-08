from django import forms
from transaction.models import PurchasedItem


class WeeklyReportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(WeeklyReportForm, self).__init__(*args, **kwargs)
        earliest_year = PurchasedItem.objects.all().earliest('date').date.year
        latest_year = PurchasedItem.objects.all().latest('date').date.year
        years = []
        for index in range(earliest_year, latest_year+1):
            years += [[index, index]]

        self.fields['year'] = forms.ChoiceField(choices=years, widget=forms.Select(attrs={"class":"form-control","id":"yearSelect",}))
        self.fields['weekNumber'] = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={"class":"form-control","id":"weekSelect","min":"1","max":"53",}))

    def __str__(self):
        return "Weekly Report"


class MonthlyReportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(MonthlyReportForm, self).__init__(*args, **kwargs)
        earliest_year = PurchasedItem.objects.all().earliest('date').date.year
        latest_year = PurchasedItem.objects.all().latest('date').date.year
        years = []
        for index in range(earliest_year, latest_year+1):
            years += [[index, index]]

        self.fields['year'] = forms.ChoiceField(choices=years, widget=forms.Select(attrs={"class":"form-control","id":"yearSelect",}))
        self.fields['month'] = forms.ChoiceField(choices=[
                [1,'January'],
                [2,'February'],
                [3,'March'],
                [4,'April'],
                [5,'May'],
                [6,'June'],
                [7,'July'],
                [8,'August'],
                [9,'September'],
                [10,'October'],
                [11,'November'],
                [12,'December'],
            ], widget=forms.Select(attrs={"class":"form-control","id":"monthSelect",}))

    def __str__(self):
        return "Monthly Report"


class AnnualReportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AnnualReportForm, self).__init__(*args, **kwargs)
        earliest_year = PurchasedItem.objects.all().earliest('date').date.year
        latest_year = PurchasedItem.objects.all().latest('date').date.year
        years = []
        for index in range(earliest_year, latest_year+1):
            years += [[index, index]]

        self.fields['year'] = forms.ChoiceField(choices=years, widget=forms.Select(attrs={"class":"form-control","id":"yearSelect",}))

    def __str__(self):
        return "Annual Report"
