from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^public/$' , views.news_public ),
    url(r'^fund/$' , views.news_fund )

]
