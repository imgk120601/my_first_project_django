from django.urls import path
from first_app import views


#Template tagging
app_name='first_app'  #this is must for relative linking of webpages in url.py--first_app(in this file) .
                      #this will be used in relative_url_template.html and relative_url_template1.html to join them!! in same folder

urlpatterns=[
	path('',views.index,name='index'),#this is home page
	path('relative_url_template',views.relative_url_template,name='relative_url_template'),
	path('relative_url_template1',views.relative_url_template1,name='relative_url_template1'),
	path('base',views.base,name='base'),
	path('other',views.other,name='other'),
	path('registration',views.registration,name='registration'),
	path('user_login',views.user_login,name='user_login'),
	path('user_logout',views.user_logout,name='user_logout'),	
	path('special',views.special,name='special'),	

]