# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agerestriction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    abbreviated = models.CharField(db_column='Abbreviated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guide = models.CharField(db_column='Guide', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgeRestriction'


class Anime(models.Model):
    canonical_title = models.CharField(db_column='canonicalTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    titles = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    episode_count = models.IntegerField(db_column='episodeCount', blank=True, null=True)  # Field name made lowercase.
    show_type = models.CharField(db_column='showType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    has_franchise = models.NullBooleanField(db_column='hasFranchise')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    age_restriction = models.IntegerField(db_column='ageRestrictionId', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime'


class Category(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    anime = models.IntegerField(db_column='animeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Category'


class Character(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Character'


class Episode(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    canonical_title = models.CharField(db_column='canonicalTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(blank=True, null=True)
    air_date = models.DateTimeField(db_column='airdate', blank=True, null=True)
    season_number = models.IntegerField(db_column='seasonNumber', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(blank=True, null=True)
    relative_number = models.IntegerField(db_column='relativeNumber', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(blank=True, null=True)

    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Episode'


class Producer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, db_column='animeId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producer'
