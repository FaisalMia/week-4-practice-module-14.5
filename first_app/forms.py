from django import forms


class Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    roll_number = forms.IntegerField(help_text='Enter a 6 digit roll number')
    birth_date = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.CharField(widget=forms.PasswordInput())
    agree = forms.BooleanField(widget=forms.RadioSelect)
    CHOICE = [('S','Small'),('L','Large'),('M,Medium')]
    height = forms.MultipleChoiceField(choices=CHOICE,widget=forms.CheckboxSelectMultiple)
    
    
    
    
    