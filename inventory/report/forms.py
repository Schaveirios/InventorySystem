from django import forms


class WeeklyReportForm(forms.Form):
    year = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control","id":"yearSelect"}))
    weekNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={"class":"form-control","id":"weekSelect"}))

    def __str__(self):
        return "Weekly Report"
