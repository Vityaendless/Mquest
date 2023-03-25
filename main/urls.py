from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('death', views.death, name='death'),
    path('win', views.win, name='win'),
    path('<int:event_key>/<int:smtng_happens>', views.event_detail, name='event_detail'),
    path('<int:event_key>/<int:smtng_happens>/<int:random_key>', views.random_event, name='random_event')
]