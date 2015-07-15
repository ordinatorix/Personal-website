from  django.shortcuts import render_to_response
from  django.http import Http404
from  django.shortcuts import redirect
from  django.core.urlresolvers import reverse


def  home(request):
	return render_to_response('header.html')

def skills_page(request):
	return render_to_response('skills_home.html')

def projects_page(request):
	return render_to_response('projects_home.html')
	
def in_progress_page(request):
	return render_to_response('in_progress.html')
