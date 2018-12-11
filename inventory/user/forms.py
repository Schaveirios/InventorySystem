from django import forms
from user.models import UserProfileInfo
from django.contrib.auth.models import User
import datetime
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
 
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','photos')

# class UserLogs(forms.ModelForm):
# 	date = models.DateField(_("Date"), default=datetime.date.today)
# 	message = forms.CharField()
# 	class Meta():
# 		model = Userlogs