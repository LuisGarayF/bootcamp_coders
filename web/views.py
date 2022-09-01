from django.shortcuts import render, HttpResponseRedirect
from web.models import *
from web.forms import *
from django.http import HttpResponse


# Create your views here.

def indexView(request):
    estudiantes_datos = Estudiante.objects.select_related('codigo_curso').select_related('codigo_curso__codigo_plan_formativo').select_related('codigo_comuna').all()
    if request.method == 'POST':
        forma = NameForm(request.POST)
        region_buscada = request.POST.get('region_selector')
        filtro_curso = request.POST.get('curso_selector')
        if region_buscada != '':
            estudiantes_datos = estudiantes_datos.filter(codigo_comuna__codigo_region = region_buscada)
        if filtro_curso != '':
            estudiantes_datos = estudiantes_datos.filter(codigo_curso = filtro_curso)
    else:
        forma = NameForm()
        estudiantes_datos = []
    #return render(request, 'web/form.html', {'estudiantes': estudiantes_datos, 'form': forma})
    return render(request,'index.html', {'estudiantes': estudiantes_datos, 'form': forma})


    
def Perfilcurso(request):
    
    if request.POST['codigo_curso']:
        cc= request.POST['codigo_curso']
        cods = Curso.objects.filter(codigo_curso__contains=cc)
        #cursos = Curso.objects.all()
    return render(request,'perfil_curso.html', {'cods':cods})

        