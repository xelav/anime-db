from django.db import models


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
    age_restriction = models.ForeignKey(
        'AgeRestriction',
        on_delete=models.DO_NOTHING,
        db_column='ageRestrictionId',
        # choices=AGE_RESTRICTION_CHOICES,
        blank=True, null=True)
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Anime'

    def __str__(self):
        if self.canonical_title:
            return self.canonical_title
        else:
            return "Noname anime"


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

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Noname character"


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
