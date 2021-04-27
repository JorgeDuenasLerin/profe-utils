from django.urls import path, re_path

from . import views

app_name = 'incidencias' # Para espacio de nombres url... 'incidencias:index'
                         # https://docs.djangoproject.com/en/3.2/intro/tutorial03/#namespacing-url-names

urlpatterns = [
    # ex: /polls/
    #re_path(r'^incidencia/(?:/(?P<lugar_id>\d+))?/?$', views.index, name='listado'),
    re_path(r'^(?:(?P<lugar_id>\d+)/?)?$', views.index, name='listado'),
]
"""
# ex: /polls/5/
path('<int:question_id>/', views.detail, name='detail'),
# ex: /polls/5/results/
path('<int:question_id>/results/', views.results, name='results'),
# ex: /polls/5/vote/
path('<int:question_id>/vote/', views.vote, name='vote'),
"""
