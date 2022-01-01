from django import forms
from django.forms import ModelForm, fields
from boat.models import Booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'name'}))
    email = forms.EmailField(max_length=150,widget=forms.EmailInput(attrs={'class':'email'}))
    message = forms.CharField(widget = forms.Textarea(attrs={'class':'message'}), max_length=1000)

#create a form for the user register model which takes name,email,password.
class UserRegisterForm(UserCreationForm):
      email = forms.EmailField(required=True)

      class Meta:
          model = User
          fields = ('username', 'email', 'password1', 'password2')

      def save(self, commit=True):
          user = super(UserRegisterForm, self).save(commit=False)
          user.email = self.cleaned_data['email']
          if commit:
                user.save()
          return user
     

    

# create a user login form which takes email and password as input
class UserLoginForm(ModelForm):
      required_css_class = 'required'
      password=forms.CharField(widget=forms.PasswordInput)
      class Meta:
          model = User
          fields = 'email','password'

class BookingForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('name','email')
        widget = {'booking_date': forms.DateInput(attrs={'class':'datepicker'}),
                  'booking_time':forms.TimeInput(attrs={'class':'timepicker'})}
    

''' 
class UPDATE_BOOKING(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Booking
        fields = '__all__

        '''