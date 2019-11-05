"""Sigpa URLs module."""

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Views
from planificacion import views as views_planificacion

urlpatterns = [
    path(
        '',
        login_required(TemplateView.as_view(template_name="dashboard.html"))),

    path('admin/', admin.site.urls),

    # Docentes
    path('', include(('docentes.urls', 'docentes'), namespace='docentes')),
    # Carrera (Unidades Curriculares, Malla)
    path('', include(('carrera.urls', 'carrera'), namespace='carrera')),
    # Periodo
    path('', include(
        ('planificacion.urls', 'planificacion'),
        namespace='planificacion')
    ),
    # Login URLs
    path('', include(('user.urls', 'user'), namespace='user')),

    # Secciones
    path(
        'periodo/<int:periodo>/tt/<int:tt>/seccion/agregar',
        login_required(views_planificacion.AddSeccionView.as_view()),
        name='seccion_add'),
    path(
        'periodo/<int:periodo>/secciones',
        login_required(views_planificacion.SeccionesView.as_view()),
        name='secciones'),
    path(
        'periodo/<int:periodo>/seccion/<int:seccion>',
        login_required(views_planificacion.SeccionView.as_view()),
        name='seccion'),
    path(
        'periodo/<int:periodo>/seccion/<int:seccion>/ver',
        login_required(views_planificacion.SeccionVerView.as_view()),
        name='seccion_ver'),

    # reportes
    # path(
    #     'planificacion/planillas',
    #     login_required(
    #         views_planificacion.PlanificacionPlanillasView.as_view()),
    #     name='planificacion_planillas'),

    # # PDF
    # path(
    #     'planificacion/planilla/<int:periodo>',
    #     views_planificacion.generar_pdf,
    #     name='planificacion_planilla_pdf'),

    # Ajax
    path('ajax/trayecto/', views_planificacion.trayecto, name='trayecto'),
    path('ajax/trimestre/', views_planificacion.trimestre, name='trimestre'),
    path('ajax/malla/', views_planificacion.malla, name='malla'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
