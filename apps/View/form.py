from django import forms


class FiltrForm(forms.Form):
    F_By_Price = forms.BooleanField()
    F_By_Name = forms.BooleanField()
    F_By_Price_down = forms.BooleanField()
    F_By_Name_down = forms.BooleanField()
