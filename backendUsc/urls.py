
from django.conf.urls import url 
from backendUsc import views 
 
urlpatterns = [ 
    url(r'^api/hacker-back/languages$', views.languages_list),
    url(r'^api/hacker-back/test/language/(?P<pk>[0-9]+)$', views.testPerLanguage),
    url(r'^api/hacker-back/test/questions/(?P<pk>[0-9]+)$', views.questionPerTest),
    url(r'^api/hacker-back/test/answers/(?P<pk>[0-9]+)$', views.answerPerQuestion),
    url(r'^api/hacker-back/test/create$', views.insertTest),
    url(r'^api/hacker-back/test/reservation/(?P<pk>[0-9]+)$', views.getReservation),
]