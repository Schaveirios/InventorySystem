from django import forms


class WeeklyReportForm(forms.Form):
    year = forms.IntegerField()
    weekNumber = forms.IntegerField(min_value=1)

    def __str__(self):
        return "Weekly Report"
