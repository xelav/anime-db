from django import forms
from .models import Anime, Character, Category, Producer


class ListTextWidget(forms.TextInput):
    def __init__(self, data_list, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._list = data_list
        self.attrs.update({'list':'list__%s' % self._name})

    def render(self, name, value, attrs=None):
        text_html = super(ListTextWidget, self).render(name, value, attrs=attrs)
        data_list = '<datalist id="list__%s">' % self._name
        for item in self._list:
            data_list += '<option value="%s">' % item
        data_list += '</datalist>'

        return (text_html + data_list)


class AnimeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', None)
        super(AnimeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and readonly:
            for field in self.fields:
                self.fields[field].widget.attrs['disabled'] = True

    class Meta:
        model = Anime
        fields = '__all__'

        labels = {
            "canonical_title": "Название",
            "titles": "Прочие названия",
            "start_date": "Дата начала показа",
            "end_date": "Дата оканчания",
            "episode_count": "Число эпизодов",
            "show_type": "Тип",
            "status": "Статус",
            "synopsis": "Синопсис",
            "has_franchise": "Имеется франчайз",
            "created_at": "Время создания записи",
            "updated_at": "Время обновления записи",
            "age_restriction": "Возрастной рейтинг"
        }

class CharacterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', None)
        super(CharacterForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk and readonly:
            for field in self.fields:
                self.fields[field].widget.attrs['disabled'] = True

    class Meta:
        model = Character
        fields = '__all__'


class SearchAnimeForm(forms.Form):
    search_anime = forms.CharField(
        label='Название аниме',
        widget=ListTextWidget(
            data_list=Anime.objects \
                .all() \
                .order_by('canonical_title') \
                .values_list('canonical_title', flat=True) \
                .distinct(),
            name='anime-list'
        )
    )


class SearchCharacterForm(forms.Form):

    search_anime = forms.CharField(
        label='Название аниме',
        widget=ListTextWidget(
            data_list=Anime.objects\
                .all()\
                .order_by('canonical_title')\
                .values_list('canonical_title', flat=True)\
                .distinct(),
            attrs={'v-model': 'anime_search', '@change': "anime_query"},
            name='anime-list',
        )
    )
    search_character = forms.CharField(
        label='Имя персонажа',
        widget=forms.Select(
            # data_list=Character.objects.all().order_by('name').values_list('name', flat=True).distinct(),
            attrs={'v-bind:disabled': 'characters_disabled', 'v-model': 'character_search'},
            # name='characters-list'
        )
    )


class SearchCategoryForm(forms.Form):

    search_category = forms.CharField(
        label='Название категории',
        widget=ListTextWidget(
            data_list=Category.objects.all().order_by('title').values_list('title', flat=True).distinct(),
            name='category-list'
        )
    )

class SearchProducerForm(forms.Form):

    search_producer = forms.CharField(
        label='Имя производителя',
        widget=ListTextWidget(
            data_list=Producer.objects.all().order_by('name').values_list('name', flat=True).distinct(),
            name='producers-list'
        )
    )
