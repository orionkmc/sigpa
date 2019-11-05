"""Docentes URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from docentes import views

urlpatterns = [
    path(
        'docentes/',
        login_required(views.DocentesView.as_view()),
        name='docentes'),
    path(
        'docente/agregar',
        login_required(views.AddDocenteView.as_view()),
        name='docente_add'),
    path(
        'docente/editar/<int:docente>',
        login_required(views.EditDocenteView.as_view()),
        name='docente_edit'),
    path(
        'docente/<int:pk>/',
        login_required(views.DocenteDetailView.as_view()),
        name='docente-detail'),
]
