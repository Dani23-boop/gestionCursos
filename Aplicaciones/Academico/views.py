from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from .models import Diploma
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View

import os
from io import BytesIO

import itertools
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import pink, black, red, blue,green
from reportlab.lib.units import inch
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
this_path = os.getcwd() + '/polls'







# Create your views here.
class PDFView(View):
    def get(self, request, *args, **kwargs):
        # Crear un objeto HttpResponse con el tipo de contenido de PDF
        response = HttpResponse(content_type='application/pdf')

        # Establecer el nombre del archivo PDF
        response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'
# Crear el objeto PDF, usando el objeto HttpResponse como su "archivo"
        p = canvas.Canvas(response)

        # Agregar contenido al PDF
        p.drawString(100, 800, "Hola, este es un reporte en PDF.")
        p.drawString(100, 780, "Puedes personalizar esto según tus necesidades.")
        p.drawString(480,750,'01/07/2016')
        p.setFont('Helvetica-Bold',12)
        p.drawString(480,750,'15/11/2023')
        p.line(460,747,560,747)
        p.setFillColor(red)
        p.rect(0,2*inch,0.2*inch,0.3*inch, fill=1)
        p.drawImage("http://127.0.0.1:8000/static/images/1.jpeg",250,450)
        p.setFont('Helvetica',22)
 # Cerrar el objeto PDF y finalizar la respuesta
        p.showPage()
        p.save()
        return response


def generar_diploma(curso):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setLineWidth(.3)
    
    # Encabezado
    c.setFont('Helvetica-Bold', 20)
    c.drawString(30, 750, 'DIPLOMA')

    # Fecha
    c.setFont('Helvetica', 12)
    c.drawString(30, 730, 'Fecha de emisión: 01/07/2016')

    # Línea decorativa
    c.line(30, 720, 570, 720)

    # Contenido del diploma
    c.setFont('Helvetica-Bold', 16)
    c.drawString(30, 680, 'Se certifica que')

    c.setFont('Helvetica', 20)
    c.drawString(30, 650, curso.nombre)

    c.setFont('Helvetica', 16)
    c.drawString(30, 620, f'ha completado satisfactoriamente el curso de {curso.nombre}.')

    # Imagen del curso
    c.drawImage("http://127.0.0.1:8000/static/images/1.jpeg", 30, 450, width=200, height=150)

    # Información adicional
    c.setFont('Helvetica', 12)
    c.drawString(30, 400, f'Créditos obtenidos: {curso.creditos}')

    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()

    return pdf


def reporte(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={curso.nombre}_diploma.pdf'

    pdf_content = generar_diploma(curso)
    response.write(pdf_content)

    return response


def inicio(request):
    cursosListados = Curso.objects.all()
    #messages.success(request, '!Cursos Listados¡')
    return render(request,"gestionCursos.html", {"cursos": cursosListados})

def slider_imagenes(request):
    return render(request, 'slider_imagenes.html')

def mostrar_imagenes(request):
    imagenes = Imagen.objects.all()
    return render(request, 'mostrar_imagenes.html', {'imagenes': imagenes})

def diplomas(request):
    # Lógica para obtener los diplomas o información relacionada
    return render(request, 'diplomas.html')

def generar_diplomas_pdf(request):
    # Datos necesarios para el diploma
    nombre = "Nombre del Recipiente"
    descripcion = "Diploma de Excelencia"

    # Carga la plantilla HTML del diploma
    template = get_template('diplomas.html')
    context = {'nombre': nombre, 'descripcion': descripcion}

    # Renderiza el diploma como HTML
    html = template.render(context)

    # Crea un objeto HttpResponse con el tipo de contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="diplomas.pdf"'

    # Convierte el HTML a PDF
    pisa.CreatePDF(html, dest=response)

    return response

def ver_diploma(request, diploma_id):
    diploma = Diploma.objects.get(pk=diploma_id)
    return render(request, 'diplomas/diploma.html', {'diploma': diploma})


def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['txtMateria']
    creditos=request.POST['NumCreditos']
    
    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '!Cursos Registrado¡')
    return redirect('/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['NumCreditos']
    
    curso=Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    
    messages.success(request, '!Cursos Actualizado¡')
    
    return redirect('/')

        
def eliminarCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    
    messages.success(request, '!Cursos Eliminados¡')
    
    return redirect('/')

