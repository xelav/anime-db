from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


def main_menu(request):

    return render(request, 'main_menu.html')


def search_anime(request):

    if request.method == 'POST':
        form = SearchAnimeForm(request.POST)
        if form.is_valid():
            search_anime = form.cleaned_data['search_anime']
            anime = Anime.objects.filter(canonical_title__contains=search_anime).first()
            anime_form = AnimeForm(instance=anime, readonly=True)
            anime_id = anime.pk
        else:
            raise AssertionError('Validation!')
    else:
        anime_id = None
        anime_form = None
    form = SearchAnimeForm()

    return render(request, 'search_anime.html',
        {'form': form,
         'anime_form': anime_form,
         'anime_id': anime_id}
                  )


def search_character(request):
    # TODO: search by anime
    if request.method == 'POST':
        form = SearchCharacterForm(request.POST)
        if form.is_valid():
            anime_name = form.cleaned_data['search_anime']
            anime_list = Anime.objects.filter(canonical_title__contains=anime_name)
            print(anime_list)

            character_name = form.cleaned_data['search_character']
            character = Character.objects\
                .filter(anime__in=anime_list)\
                .filter(name__contains=character_name)\
                .first()
            print(character)
            if character:
                character_form = CharacterForm(instance=character, readonly=True)
                message = None
            else:
                character_form = None
                message = "По запросу ничего не найдено."
        else:
            raise AssertionError('Validation! {0}'.format(form.errors))
    else:
        message = "Пожалуйста, введите данные для поиска."
        character_form = None
    search_form = SearchCharacterForm()
    return render(request, 'search_character.html',
        {
             'search_form': search_form,
             'character_form': character_form,
             'message': message
        }
        )


def create_anime(request):

    if request.method == 'POST':
        anime_form = AnimeForm(request.POST)
        if anime_form.is_valid():
            anime_form.save()
        else:
            raise AssertionError('Validation! {0}'.format(anime_form.errors))
    else:
        anime_form = AnimeForm()

    return render(request, 'create_anime.html',
                  {'form': anime_form})


def create_character(request):
    return


def create_episode(request):
    return


def create_producer(request):
    return


def get_categories_count(request):

    if request.method == "POST":
        search_form = SearchCategoryForm(request.POST)
        if search_form.is_valid():
            search_categoty = search_form.cleaned_data['search_category']
            category_count = Category.objects.filter(title=search_categoty).count()
            message = 'Число аниме с категорией {0} : {1}'.format(search_categoty, category_count) # FIXME: по идее это должно генерироваться на стороне темплейтов, но мне лень
        else:
            raise AssertionError('Validation! {0}'.format(search_form.errors))
    else:
        message = None

    search_form = SearchCategoryForm()

    return render(request, 'category_count.html', {'search_form': search_form, 'message': message})


def get_producers_count(request):

    if request.method == "POST":
        search_form = SearchProducerForm(request.POST)
        if search_form.is_valid():
            search_producer = search_form.cleaned_data['search_producer']
            producer_count = Producer.objects.filter(title=search_producer).count()
            message = 'Число аниме с производителем {0} : {1}'.format(search_producer, producer_count) # FIXME: по идее это должно генерироваться на стороне темплейтов, но мне лень
        else:
            raise AssertionError('Validation! {0}'.format(search_form.errors))
    else:
        message = None

    search_form = SearchProducerForm()

    return render(request, 'producer_count.html', {'search_form': search_form, 'message': message})