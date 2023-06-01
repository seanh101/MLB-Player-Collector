from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import HitForm



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {
        'players': players
    })

def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    hit_form = HitForm()
    return render(request, 'players/detail.html', {
        'player': player, 'hit_form': hit_form
    })
    
def add_hit(request, player_id):
    form = HitForm(request.POST)
    if form.is_valid():
        new_hit = form.save(commit=False)
        new_hit.player_id = player_id
        new_hit.save()
    return redirect('detail', player_id=player_id)
    
class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['position', 'jersey_number', 'age']
    
class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players'