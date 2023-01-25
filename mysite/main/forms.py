from django import forms
choice =[
        ('1','Btech'),
        ('2','Mtech'),
        ('3','BCA'),
        ('4','MCA'),
    ]
class UserForm(forms.Form):
    fname = forms.CharField(label = 'First name ' ,max_length=40)
    lname = forms.CharField(label = 'Last name ' ,max_length=40)
    marks12 = forms.FloatField(label = 'Marks in 12th')
    course = forms.CharField(widget=forms.Select(choices=choice))
    mother = forms.CharField(label = "Mother's name" ,max_length=40)
    father = forms.CharField(label = "Father'name" ,max_length=40)
    photo = forms.ImageField(required=False, label='Profile photo')
    marksheet = forms.ImageField(required = True, label = '12th Marksheet')
    marksheet2 = forms.ImageField(required=True,  label = '10th Marksheet')
    # fill = forms.BooleanField(required=True,label="Form Filled?")