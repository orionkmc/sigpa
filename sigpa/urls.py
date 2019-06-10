from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from user.views import LoginView, LogoutView
from planificacion import views as views_planificacion
from docentes import views as views_docentes
from carrera import views as views_carrera

urlpatterns = [
    path('', login_required(views_planificacion.home), name='home'),
    path('admin/', admin.site.urls),
    path(
        'planificacion/',
        login_required(views_planificacion.PlanificacionView.as_view()),
        name='planificacion'),

    # Docentes
    path(
        'docentes/',
        login_required(views_docentes.DocentesView.as_view()),
        name='docentes'),
    path(
        'docente/agregar',
        login_required(views_docentes.AddDocenteView.as_view()),
        name='docente_add'),
    path(
        'docente/editar/<int:docente>',
        login_required(views_docentes.EditDocenteView.as_view()),
        name='docente_edit'),

    # Unidades Curriculares
    path(
        'unidades-curriculares/',
        login_required(views_carrera.UnidadesCurricularesView.as_view()),
        name='ucurriculares'),
    path(
        'unidades-curriculares/agregar',
        login_required(views_carrera.AddUnidadCurricularView.as_view()),
        name='ucurricular_add'),
    path(
        'unidades-curriculares/editar/<int:uc>',
        login_required(views_carrera.EditUnidadCurricularView.as_view()),
        name='ucurricular_edit'),

    # Malla
    path(
        'mallas/',
        login_required(views_carrera.MallasView.as_view()),
        name='mallas'),
    path(
        'malla/agregar',
        login_required(views_carrera.AddMallaView.as_view()),
        name='malla_add'),
    path(
        'malla/editar/<int:malla>',
        login_required(views_carrera.EditMallaView.as_view()),
        name='malla_edit'),

    # Periodos
    path(
        'periodos',
        login_required(views_planificacion.PeriodosView.as_view()),
        name='periodos'),
    path(
        'periodo/<int:periodo>',
        login_required(views_planificacion.PeriodoView.as_view()),
        name='periodo'),
    path(
        'periodo/nuevo/<int:periodo>',
        login_required(views_planificacion.PeriodoNuevoView.as_view()),
        name='periodo_nuevo'),

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
    path(
        'planificacion/planillas',
        login_required(
            views_planificacion.PlanificacionPlanillasView.as_view()),
        name='planificacion_planillas'),

    # PDF
    path(
        'planificacion/planilla/<int:periodo>',
        views_planificacion.generar_pdf,
        name='planificacion_planilla_pdf'),

    # Login URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Ajax
    path('ajax/trayecto/', views_planificacion.trayecto, name='trayecto'),
    path('ajax/trimestre/', views_planificacion.trimestre, name='trimestre'),
    path('ajax/malla/', views_planificacion.malla, name='malla'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
