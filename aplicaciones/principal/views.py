from django.shortcuts import render,redirect

# Create your views here.
from .models import persona
from .forms import personaForm


def inicio(request):
    personas = persona.objects.all()
    
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html',contexto)

def crearPersona(request):
    if request.method == 'GET':
        form = personaForm()
        contexto = {
            'form':form
        }
    else:
        form = personaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'formulario.html',contexto)


def editarPersona(request,id):
    personas = persona.objects.get(id = id)
    if request.method == 'GET':
        form = personaForm(instance = personas)
        contexto = {
            'form':form
        }
    else:
        form = personaForm(request.POST, instance = personas)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render (request, 'formulario.html',contexto)



def eliminarPersona(request,id):
    personas = persona.objects.get(id = id)
    personas.delete()
    return redirect('index')
