from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView
from biostar.server import views
from biostar.server.ajax import VoteSubmit

urlpatterns = patterns('',

    # Post listing.
    url(r'^$', views.PostList.as_view(), name="home"),

    # Topic listing.
    url(r'^t/(?P<topic>.+)/$', views.PostList.as_view(), name="topic-list"),

    # The list of users.
    url(r'^user/list/$', views.UserList.as_view(), name="user-list"),

    # User details.
    url(r'^u/(?P<pk>\d+)/$', views.UserDetails.as_view(), name="user-details"),

    # User details.
    url(r'^u/edit/(?P<pk>\d+)/$', views.EditUser.as_view(), name="user-edit"),

    # Post details.
    url(r'^p/(?P<pk>\d+)/$', views.PostDetails.as_view(), name="post-details"),

    # A separate url for each post type.
    url(r'^p/new/post/$', views.NewPost.as_view(), name="new-post"),

    url(r'^p/new/answer/(?P<pid>\d+)/$', views.NewAnswer.as_view(post_type="answer"), name="new-answer"),
    url(r'^p/new/comment/(?P<pid>\d+)/$', views.NewAnswer.as_view(post_type="comment"), name="new-comment"),

    # Edit an existing post.
    url(r'^p/edit/(?P<pk>\d+)/$', views.EditPost.as_view(), name="post-edit"),

    # Vote submission.
    url(r'^x/vote/$', VoteSubmit.as_view(), name="vote-submit"),

    # Social login pages.
    (r'^accounts/', include('allauth.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Adding the search urls.
    url(r'^search/', views.SiteSearch(), name="search"),

     # matching the robots.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain'), name='robots'),

)


# Adding the flatpages.
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^info/about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^info/faq/$', 'flatpage', {'url': '/faq/'}, name='faq'),
    url(r'^info/help/$', 'flatpage', {'url': '/about/'}, name='help'),
    url(r'^info/policy/$', 'flatpage', {'url': '/policy/'}, name='policy'),
)

# This is used only for the debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )