from django.shortcuts import render
from django.template  import RequestContext
from django.views.generic import View
from index.models import Visit
from time import gmtime, strftime

class IndexView(View):

    def get(self, request):        
        visit = Visit()
        visit.save(request.META)
        return render(request, 'index/index_content.html', {'ip': visit.ip_address})

