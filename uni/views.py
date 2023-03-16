from django.shortcuts import render, redirect
from uni.models import Player, Game
from .forms import ParticipantForm, CompanyForm

# Create your views here.


def base(request):
    return render(request, "base.html")


def home(request):
    return render(request, "index.html")


def about(request):
    form = ParticipantForm()
    company = CompanyForm()
    return render(request, "about.html", {"form": form, "company_form": company})


def submit_form(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "index.html")
        else:
            return render(request, 'about.html', {"form": form})
    else:
        form = ParticipantForm()
        return render(request, "about.html", {"form": form})


def submit_company(request):
    if request.method == "POST":
        form = ParticipantForm()
        company = CompanyForm(request.POST)
        if company.is_valid():
            company.save()
            return redirect('home')
        else:
            return render(request, 'about.html', {"form": form, "company_form": company})
    else:
        form = ParticipantForm
        company = CompanyForm()
        return render(request, 'about.html', {"form": form, "company_form": company})


def teams(request):
    return render(request, "teams.html")


def detailed_team(request, tag):
    game = Game.objects.filter(label=tag).exists()

    if game:
        game_obj = Game.objects.get(label=tag)
        players = Player.objects.filter(game=game_obj.pk)

        name = tag

        if tag == 'csgo':
            name = 'Counter-Strike: Global Offensive'

        elif tag == 'dota2':
            name = "Dota 2"

        elif tag == 'scII':
            name = "Starcraft II"

        elif tag == 'lol':
            name = "League Of Legends"

        context = {"tag": name.upper(), "players": players, "game": game}
        return render(request, "teams_detail.html", context)
    else:
        return redirect('home')



