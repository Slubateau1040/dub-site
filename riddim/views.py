from django.http import HttpResponseRedirect
from django.urls import reverse
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

def create_riddim(request):
    if request.method == 'POST':
        name = request.POST['name']
        genre = request.POST['genre']
        audio_file = request.FILES['audio_file']
        models.Riddim.objects.create(name=name, genre=genre, audio_file=audio_file)
        return HttpResponseRedirect(reverse('list_riddim'))
    else:
        return render(request, 'riddim/create.html')

def delete_riddim(request, riddim_id):
    riddim = get_object_or_404(models.Riddim, pk=riddim_id)
    riddim.delete()
    return HttpResponseRedirect(reverse('list_riddim'))