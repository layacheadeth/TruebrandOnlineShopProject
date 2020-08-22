from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #there is nothing inside which represent the homepage itself.
    path('', views.home_page,name='home-page'),
    #the site name/register will lead us to this register page.
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    # the detail page should consist of specific id.Hence the detail related to specific items can be mapped easily through the given id.
    path('<int:product_id>',views.detail,name='detail'),
    path('clothes',views.clothes,name='clothes'),
    path('jewelery',views.jewelery,name='jewelery'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('about_us',views.about_us,name='about_us'),
    path('search',views.search,name='search'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# plus static media data show that media save from database can be uploaded to frontend