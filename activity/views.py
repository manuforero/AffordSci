from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader
from django.shortcuts import (
	render, get_object_or_404, redirect)
from django.core.urlresolvers import reverse

from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Activity, Review
from .forms import ActivityForm, ReviewForm


# class ActivityList(ListView):
# 	model = Activity 

def activity_list(request):
	activity_list = Activity.objects.order_by('pk')
	context = {'activity_list':activity_list}
	#return render(request, 'activity/activity_list.html' , context)
	template = loader.get_template('activity/activity_list.html')
	return HttpResponse(template.render(context, request))

# class ActivityDetail(DetailView):
# 	model = Activity 

def activity_detail(request, activity_id):
	activity =get_object_or_404(Activity, pk=activity_id)
	review_list = activity.review_set.all()
	
	return render(request, 'activity/activity_detail.html' , 
		{'activity':activity, 'review_list':review_list})

def new_activity(request):
	if request.method == 'POST':
		form = ActivityForm(request.POST, request.FILES)
		if form.is_valid():
			this_activity = form.save(commit = False)
			#we can add more fields here if necessary, 
			# since we have not committed
			this_activity.save()
			#return redirect('recet_detail', pk=Receta.pk)
			return HttpResponseRedirect('/')
	else:
		form = ActivityForm()

	template = loader.get_template('activity_new.html')
	context = {
		'form' : form
	}
	return HttpResponse(template.render(context, request))


def activity_edit(request, activity_id):
    d_activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES, instance = d_activity)
        if form.is_valid():
            d_activity = form.save(commit=False)
            d_activity.save()
            #return redirect(reverse(activity_detail), pk=Activity.pk)
            return HttpResponseRedirect('/')
    else:
        form = ActivityForm(instance=d_activity)
    return render(request, 'activity_edit.html', {'form': form})

def new_review(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            summary = form.cleaned_data['summary']
            body = form.cleaned_data['body']
            duration =form.cleaned_data['duration']
            rating = form.cleaned_data['rating']

            review = Review()

            review.title = title 
            review.activity = activity
            review.summary = summary
            review.body = body
            review.duration = duration
            review.rating = rating 

            review.save()
            #return redirect(reverse(activity_detail), pk=Activity.pk)
            return HttpResponseRedirect('/')
    else:
        form = ReviewForm(instance=activity)
    return render(request, 'new_review.html', {'activity':activity,'form': form})

def review_detail(request, review_id):
	review =get_object_or_404(Review, pk=review_id)
	return render(request, 'reviews/review_detail.html', 
		{'review':review})
	