from django import forms


class LigasForm(forms.Form):
    torneo = forms.CharField(max_length=40, min_length=3)
    equipos = forms.IntegerField(max_value=50, min_value=5)
    internacional = forms.BooleanField()






