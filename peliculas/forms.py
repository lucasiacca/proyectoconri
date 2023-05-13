from django import forms


class PeliculaFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=1028) 
    version = forms.CharField(required=True, max_length=1028) 
    cpl = forms.CharField(required=False, max_length=1028) 
    

class KdmFormulario(forms.Form):
    titulo_kdm = forms.CharField(max_length=1028)
    cpl_kdm = forms.CharField(max_length=1028)
    servidor_kdm = forms.IntegerField()
    fecha_apertura = forms.DateTimeField()
    fecha_clausura= forms.DateTimeField()
    
class SesionFormulario(forms.Form):
   datetime_sesion = forms.DateField()
   titulo_sesion = forms.CharField(max_length=1028)
   version_sesion = forms.CharField(max_length=1028)
   SALA_CHOICES = (
        ("K1", "Kursaal 1"),
        ("K2", "Kursaal 2"),
        ("TVE", "Teatro Victoria Eugenia"),
    )
   sala = forms.ChoiceField(choices=SALA_CHOICES)