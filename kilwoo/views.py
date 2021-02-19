from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Introduction, Team, Subcategory, Services
from .forms import introductionEdit

def e_introduction(request):
    informations = Introduction.objects.all()
    teams = Team.objects.all()
    services = Services.objects.all()
    return render(request, 'editor/e_introduction.html',{
        'informations': informations,
        'teams': teams,
        'services': services,
    })

def introduction_edit(request, pk):
    post = get_object_or_404(Introduction, pk=pk)
    informations = Introduction.objects.all()
    teams = Team.objects.all()
    services = Services.objects.all()
    if request.method == "POST":
        form = introductionEdit(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('e_introduction')
    else:
        form = introductionEdit(instance=post)
    return render(request, 'editor/e_introduction_edit.html', {
        'informations':informations,
        'form':form,
        'teams': teams,
        'services': services,
    })


def e_teams(request, pk):
    teams = Team.objects.all()
    informations = Introduction.objects.all()
    services = Services.objects.all()
    specific = get_object_or_404(Team, pk=pk)
    subcategories = Subcategory.objects.all()
    return render(request, 'editor/e_teams.html', {
        'informations': informations,
        'teams': teams,
        'services': services,
        'specific': specific,
        'subcategories': subcategories,
    })

def e_subcategory(request, pk):
    teams = Team.objects.all()
    informations = Introduction.objects.all()
    services = Services.objects.all()
    subcategories = Subcategory.objects.all()
    specific = get_object_or_404(Subcategory, pk=pk)
    return render(request, 'editor/e_subcategory.html', {
        'informations': informations,
        'subcategories': subcategories,
        'specific': specific,
        'teams': teams,
        'services': services,
    })

def e_services(request, pk):
    teams = Team.objects.all()
    informations = Introduction.objects.all()
    services = Services.objects.all()
    specific = get_object_or_404(Services, pk=pk)
    return render(request, 'editor/e_services.html', {
        'informations': informations,
        'services': services,
        'specific': specific,
        'teams': teams,
    })
