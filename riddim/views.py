from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def list_riddim(request):
    riddims = models.Riddim.objects.all()
    context = {'riddims': riddims}
    return render(request, 'riddim/list.html', context)

def detail_riddim(request, riddim_id):
    riddim = get_object_or_404(models.Riddim, pk=riddim_id)
    return render(request, 'riddim/detail.html', {'riddim': riddim})