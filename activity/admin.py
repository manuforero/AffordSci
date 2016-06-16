from django.contrib import admin
from .models import Activity, Review 


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('pk',)

admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('pk',)