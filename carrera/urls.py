"""Carrera URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from carrera import views

urlpatterns = [
    # Unidades Curriculares
    path(
        'unidades-curriculares/',
        login_required(views.UnidadesCurricularesView.as_view()),
        name='ucurriculares'),
    path(
        'unidad-curricular/agregar',
        login_required(views.AddUnidadCurricularView.as_view()),
        name='ucurricular_add'),
    path(
        'unidad-curricular/editar/<int:uc>',
        login_required(views.EditUnidadCurricularView.as_view()),
        name='ucurricular_edit'),
    path(
        'unidad-curricular/<int:pk>/',
        login_required(views.UnidadCurricularDetailView.as_view()),
        name='ucurricular-detail'),

    # Malla
    path(
        'mallas/',
        login_required(views.MallasView.as_view()),
        name='mallas'),
    path(
        'malla/agregar',
        login_required(views.AddMallaView.as_view()),
        name='malla_add'),
    path(
        'malla/editar/<int:malla>',
        login_required(views.EditMallaView.as_view()),
        name='malla_edit'),
]
