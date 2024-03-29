from django.urls import path
from .views import *

urlpatterns = [
    path('', Home,name='home-page'),
    path('home/', Home,name='home-page'),
    path('about/', About,name='about-page'),
    path('research/', About,name='research-page'),
    path('service/', Service,name='service-page'),
    path('contact/', Contact,name='contact-page'),
    path('index/', Index,name='index-page'),
    path('portfolio/', Portfolio,name='portfolio-page'),
    path('team/', Team,name='team-page'),
    path('map/', myFirstMap,name='map-page'),
    path('blog/', Blog,name='blog-page'),
    path('blog-single/', blogSingle,name='blog-single'),
]
