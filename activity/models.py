from __future__ import unicode_literals

from django.db import models
import numpy as np 

class Activity(models.Model):
    name = models.CharField(max_length = 60)
    short_desc = models.CharField(max_length = 240) #short description of the activity
    instructions = models.TextField()
    duration = models.DurationField()
    url_source = models.URLField(max_length = 200, blank=True, null=True)
    
    #create_date = models.DateTimeField(blank=True, null=True)
    #last_edit = models.DateTimeField(blank=True, null=True)

    # image = models.ImageField(blank = True)
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __str__(self):
    	return self.name

class Review(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'),( 3, '3'), (4, '4'), (5, '5'),)
    title = models.CharField(max_length = 60)
    activity = models.ForeignKey(Activity)
    summary = models.CharField(max_length = 240, blank=True, null=True) #short summary of the review
    rating = models.IntegerField(choices=RATING_CHOICES)

    body = models.TextField('your review') #mention the types and level of students you worked with, their learning level, etc...
    
    duration = models.DurationField()
    
    #create_date = models.DateTimeField(blank=True, null=True)
    #last_edit = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
