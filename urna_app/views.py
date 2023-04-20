from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Candidate, Votes
from .forms import Vote

    
def register_vote_controller(request):

    if request.method == 'GET':

        candidates = Candidate.objects.all()
        form = Vote()
        
        return render(request, 'index.html', {'Candidates': candidates, 'form': form})

    if request.method == 'POST':

        form = Vote(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/urna/')
        else:
            return HttpResponse('error')
        

def generate_controller_report(request):
    
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        votes_dict = {}

        for candidate in candidates:
            votes_count = Votes.objects.filter(name=candidate).count()
            votes_dict[candidate.name] = votes_count

        return render(request, 'report.html', {'votes_dict': votes_dict})