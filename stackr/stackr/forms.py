from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
  #Declare Fields that would be decaled in the form in HTML
  email = forms.EmailField(required = True)
  address = forms.CharField(required = True)
  zipcode = forms.IntegerField(required = True)
  #Metadata for the form class. 
  fields = ('username', 'email', 'address', 'zipcode', 'password1', 'password2')

  def save(self, commit = True):
    user = super(MyRegistrationForm, self).save(commit = False)
    user.email = self.cleaned_data['email']
    user.address = self.cleaned_data['address']
    user.zipcode = self.cleaned_data['zipcode']
    if commit:
      user.save()
    return user
