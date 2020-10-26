from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ShortermMissionList(models.Model):
    name = models.CharField(max_length=50, blank=False, primary_key=True)
    assign_time = models.DateTimeField(default=datetime.date.today(), blank=False)
    launch_time = models.DateTimeField(default=datetime.date.today(), blank=False)
    expected_finish_time = models.DateField(blank=False)
    emergency_level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    important_level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    detail = models.TextField(max_length=500,blank=True)
    related_link_1 = models.URLField(blank=True)
    related_link_2 = models.URLField(blank=True)
    def __str__(self):
        return self.name
class LongtermMissionList(models.Model):
    name = models.CharField(max_length=50, blank=False, primary_key=True)
    assign_time = models.DateTimeField(default=datetime.date.today(), blank=False)
    launch_time = models.DateTimeField(default=datetime.date.today(), blank=False)
    expected_finish_time = models.DateField(blank=False)
    emergency_level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    important_level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    detail = models.TextField(max_length=500, blank=True)
    releated_link_1 = models.URLField(blank=True)
    releated_link_2 = models.URLField(blank=True)
    releated_link_3 = models.URLField(blank=True)
    def __str__(self):
        return self.name
class slogan(models.Model):
    text = models.CharField(max_length=80, blank=False, primary_key=True)
    create_time = models.DateTimeField(default=datetime.date.today())
