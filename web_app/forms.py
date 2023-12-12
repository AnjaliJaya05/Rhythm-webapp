from django import forms


class Regform(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    address=forms.CharField(max_length=50)
    pincode=forms.IntegerField()
    phone = forms.IntegerField()
    password=forms.CharField(max_length=30)
    cpassword=forms.CharField(max_length=30)

class Logform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=30)

class adminform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

class add_proform(forms.Form):
    file=forms.FileField()
    pname=forms.CharField(max_length=30)
    des=forms.CharField(max_length=60)
    pri=forms.IntegerField()
    offer=forms.CharField(max_length=30)

class cardform(forms.Form):
    cno=forms.IntegerField()
    mm=forms.IntegerField()
    yy=forms.IntegerField()
    cvv=forms.IntegerField()
    cname=forms.CharField(max_length=30)