from django.urls import path
from . import views
from .views import PDFView

urlpatterns = [
    path('',views.inicio),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('slider_imagenes/', views.slider_imagenes, name='slider_imagenes'),
    path('slider/', views.mostrar_imagenes),
    path('diplomas/', views.diplomas, name='diplomas'),
    path('<int:diploma_id>/', views.ver_diploma, name='ver_diploma'),
    path('generar_diplomas_pdf/', views.generar_diplomas_pdf, name='generar_diplomas_pdf'),
    path('reporte/<codigo>',views.reporte),
    path('generar_pdf_reporte/', PDFView.as_view(), name='generar_pdf_reporte'),

]
