from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/$',views.profile,name = 'NewProfile'),
    url(r'^new_profile/$',views.new_profile,name = 'new_profile'),
    url(r'^edit_profile/$',views.edit_profile,name = 'edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^find_user/(?P<username>\w{0,50})/$', views.find_user, name='find_user'),
    url(r'^review_project/(\d+)/', views.review_project, name = 'review_project'),
    url(r'^api/prof/$', views.ProfList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
]