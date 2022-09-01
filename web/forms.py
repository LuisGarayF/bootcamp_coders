from django import forms
from web.models import *
   
 
# class SelectForm(forms.Form):

#     regiones = [(x.codigo_region, x.nombre)for x in list(Region.objects.filter())]
#     codigo_region = forms.ChoiceField(choices=regiones)

#     class Meta:
#         model = Curso
#         fields =['region','curso']   
        
        
        
class Perfilcurso(forms.Form):
    
    class Meta:
        model = Curso
        fields = ['codigo_curso','fecha_inicio','fecha_termno','codigo_comuna','codigo_plan_formativo','descripcion']
        
class NameForm(forms.Form):
  region_selector = forms.ModelChoiceField(queryset=Region.objects.all(), to_field_name='codigo_region', label="Región", widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Todas")
  curso_selector = forms.ModelChoiceField(queryset=Curso.objects.all().order_by('codigo_curso'), to_field_name='codigo_curso',label="Curso", widget=forms.Select(attrs={'class': 'form-select'}), required=False, empty_label="Todos")

        
        
        
    