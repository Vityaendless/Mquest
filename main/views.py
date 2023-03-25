from django.shortcuts import render, redirect
from random import randint
from .quest import functions

def index(request):
    if request.method == 'POST':
        random_form = request.POST.get('random_action')
        #print(random_form)
        functions.daysCounter()
        functions.hero.heroesAge()
        return redirect('main')

    current_text = functions.introText()
    current_hero = functions.aboutHero()
    cur_time = functions.currentTime()
    actions = functions.actions()
    smtng_happens = randint(1, 100)

    data = {
        'cur_text': current_text,
        'cur_hero': current_hero,
        'cur_time': cur_time,
        'actions': actions,
        'smtng_happens': smtng_happens,
    }

    return render(request, 'main/index.html', data)

def event_detail(request, event_key, smtng_happens):
    actions_details = functions.actionsDetails(event_key, smtng_happens)
    random_key = randint(1, 5)
    current_hero = functions.aboutHero()
    cur_time = functions.currentTime()

    data = {
        'event_key': event_key,
        'smtng_happens': smtng_happens,
        'random_key': random_key,
        'actions_details': actions_details,
        'cur_hero': current_hero,
        'cur_time': cur_time
    }
    if functions.hero.health <= 0:
        functions.hero.heroesClean()
        functions.day = 0
        return redirect('death')

    if functions.hero.gold >= 30:
        functions.hero.heroesClean()
        functions.day = 0
        return redirect('win')

    return render(request, 'main/event_detail.html', data)

def random_event(request, event_key, smtng_happens , random_key):
    actions_details = functions.randomActionsDetails(random_key)
    current_hero = functions.aboutHero()
    cur_time = functions.currentTime()

    data = {
        'event_key': event_key,
        'smtng_happens': smtng_happens,
        'random_key': random_key,
        'actions_details': actions_details,
        'cur_hero': current_hero,
        'cur_time': cur_time
    }
    if functions.hero.health <= 0:
        functions.hero.heroesClean()
        functions.day = 0
        return redirect('death')

    if functions.hero.gold >= 30:
        functions.hero.heroesClean()
        functions.day = 0
        return redirect('win')

    return render(request, 'main/random_event.html', data)

def death(request):
    return render(request, 'main/death.html')

def win(request):
    return render(request, 'main/win.html')
