from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'personal_website.views.home', name='home'),
    url(r'^home', 'personal_website.views.home', name='home'),
    url(r'^projects_home/', 'personal_website.views.projects_page', name='projects_page'), # use url argument, such as project.name
    url(r'^skills_home/', 'personal_website.views.skills_page', name='skills_page'),
    url(r'^in_progress/', 'personal_website.views.in_progress_page', name='in_progress_page'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

