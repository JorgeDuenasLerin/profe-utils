from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Lugar, Incidencia, Respuesta, Acceso
from .tables import IncidenciaTable, IncidenciaFilter
from .forms import IncidenciaForm
from django_tables2.views import SingleTableView

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic.edit import FormView

from django.urls import reverse

class IncidenciaListView(SingleTableMixin, FilterView):

    table_class = IncidenciaTable
    queryset = Incidencia.objects.all().order_by('-created_at')
    template_name = 'incidencias/index.html'
    filterset_class = IncidenciaFilter

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        try:
            lugar_id = int(self.request.GET.get('lugar', ''))
            lugar = Lugar.objects.get(pk=lugar_id)
            self.queryset = self.queryset.filter(lugar__pk=lugar_id)
        except:
            lugar_id = 0

        context['lugares'] = Lugar.objects.all()

        return context


class IncidenciaFormView(FormView):
    template_name = 'incidencias/incidencia.html'
    form_class = IncidenciaForm

    def get_success_url(self):
        return reverse('incidencias:listado')+"?lugar="+str(self.return_lugar.id)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        form.save()

        self.return_lugar = form.cleaned_data.get('lugar')

        return super().form_valid(form)
