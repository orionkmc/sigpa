"""User URLs."""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from planificacion import views

urlpatterns = [
    # Periodos
    path(
        'planificacion/',
        login_required(views.PlanificacionView.as_view()),
        name='periodo'),
    path(
        'periodos',
        login_required(views.PeriodosView.as_view()),
        name='periodos'),
    path(
        'periodo/<int:periodo>',
        login_required(views.PeriodoView.as_view()),
        name='periodo'),
    path(
        'periodo/nuevo/<int:periodo>',
        login_required(views.PeriodoNuevoView.as_view()),
        name='periodo_nuevo_auto'),
]
