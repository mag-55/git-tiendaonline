from django import forms

class FormularioContacto(forms.Form): #clase para generar un formulario
    asunto=forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()