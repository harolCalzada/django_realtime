import time

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .tasks import generate_csv

class CeleryRealtimeTemplateView(TemplateView):
    template_name = 'realtime.html'

    def post(self, request, *args, **kwargs):
        task_id = generate_csv.delay()
        # time.sleep(10)
        return HttpResponse(task_id)
