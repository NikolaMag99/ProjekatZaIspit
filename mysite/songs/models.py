# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Concerts(models.Model):
    title = models.CharField(blank=True, null=True, max_length=250)
    artist = models.CharField(blank=True, null=True, max_length=250)
    date = models.CharField(blank=True, null=True, max_length=250)
    concertimageurl = models.CharField(db_column='concertImageUrl', blank=True, null=True, max_length=250)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Concerts'


class Songs(models.Model):
    title = models.CharField(blank=True, null=True, max_length=250)
    artist = models.CharField(blank=True, null=True, max_length=250)
    genre = models.CharField(blank=True, null=True, max_length=250)
    album = models.CharField(blank=True, null=True, max_length=250)
    albumimageurl = models.CharField(db_column='albumImageUrl', blank=True, null=True, max_length=250)  # Field name made lowercase.
    youtubeid = models.CharField(db_column='youtubeId', blank=True, null=True, max_length=250)  # Field name made lowercase.
    lyrics = models.TextField(blank=True, null=True)
    tab = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Songs'


class Users(models.Model):
    email = models.CharField(blank=True, null=True, max_length=250)
    password = models.CharField(blank=True, null=True, max_length=250)
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
