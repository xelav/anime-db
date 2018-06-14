from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import datetime


class AgeRestriction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    abbreviated = models.CharField(db_column='Abbreviated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guide = models.CharField(db_column='Guide', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgeRestriction'

    def __str__(self):
        return "{0} : {1}".format(self.abbreviated, self.guide)


class Anime(models.Model):
    canonical_title = models.CharField(db_column='canonicalTitle', verbose_name='Каноничное название', max_length=255, blank=True, null=True)  # Field name made lowercase.
    titles = models.TextField(verbose_name='Прочие названия', blank=True, null=True)
    start_date = models.DateTimeField(db_column='startDate', verbose_name='Дата начала показа', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='endDate', verbose_name='Дата окончания показа', blank=True, null=True)  # Field name made lowercase.
    episode_count = models.IntegerField(db_column='episodeCount', verbose_name='Число эпизодов', blank=True, null=True)  # Field name made lowercase.
    show_type = models.CharField(db_column='showType', verbose_name='Тип', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, verbose_name='Статус', blank=True, null=True)
    synopsis = models.TextField(verbose_name='Синопсис', blank=True, null=True)
    # has_franchise = models.NullBooleanField(db_column='hasFranchise')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', verbose_name='Время создания записи', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', verbose_name='Время обновления записи', blank=True, null=True)  # Field name made lowercase.
    age_restriction = models.ForeignKey(
        'AgeRestriction',
        verbose_name='Возрастной рейтинг',
        on_delete=models.DO_NOTHING,
        db_column='ageRestrictionId',
        # choices=AGE_RESTRICTION_CHOICES,
        blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime'
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'

    def __str__(self):
        if self.canonical_title:
            return self.canonical_title
        else:
            return "Noname anime"


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    description = models.TextField(db_column='Description', verbose_name='Описание', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', verbose_name='Время создания записи', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', verbose_name='Время обновления записи', blank=True, null=True)  # Field name made lowercase.
    anime = models.IntegerField(db_column='animeId', verbose_name='Аниме', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Character(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', verbose_name='Имя', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', verbose_name='Описание', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', verbose_name='Время создания записи', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', verbose_name='Время обновления записи', blank=True, null=True)  # Field name made lowercase.

    anime = models.ForeignKey('Anime', verbose_name='Аниме', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Character'
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Noname character"


class Episode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    canonical_title = models.CharField(db_column='canonicalTitle', verbose_name='Каноничное название', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(verbose_name='Синопсис', blank=True, null=True)
    air_date = models.DateTimeField(verbose_name='Дата выпуска в эфир', db_column='airdate', blank=True, null=True)
    season_number = models.IntegerField(db_column='seasonNumber', verbose_name='Номер сезона', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(verbose_name='Номер', blank=True, null=True)
    relative_number = models.IntegerField(verbose_name='Относительный номер', db_column='relativeNumber', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(verbose_name='Длина', blank=True, null=True)

    anime = models.ForeignKey('Anime', verbose_name='Аниме', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Episode'
        verbose_name = 'Эпизод'
        verbose_name_plural = 'Эпизоды'


class Producer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', verbose_name='Название', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', verbose_name='Время создания записи', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', verbose_name='Время обновления записи', blank=True, null=True)  # Field name made lowercase.

    anime = models.ForeignKey('Anime', verbose_name='Аниме', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producer'
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


@receiver(post_save)
def set_time_marks(sender, instance=None, created=False, **kwargs):
    list_of_models = ('Anime', 'Category', 'Character', 'Producer')
    if sender.__name__ in list_of_models:
        current_time = datetime.datetime.now()
        if created:
            instance.created_at = current_time
            instance.updated_at = current_time
            instance.save()
        else:
            sender.objects.filter(pk=instance.id).update(updated_at=current_time)