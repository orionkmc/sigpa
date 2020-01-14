"""User URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from planificacion import views

urlpatterns = [
    # Periodos
    path(
        'periodos',
        login_required(views.PeriodosView.as_view()),
        name='periodos'),
    path(
        'periodo/<int:pk>',
        login_required(views.PeriodoView.as_view()),
        name='periodo'),
    path(
        'planificacion/',
        login_required(views.PlanificacionView.as_view()),
        name='periodo'),

    path(
        'planificacion/',
        login_required(views.PlanificacionView.as_view()),
        name='periodo'),
]
