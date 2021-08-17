from django.urls import path
from . import views
from resume_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	path('',views.index,name='home'),
	path('basic',views.basic),
	path('login',views.login),
	path('candidate',views.candidate),
	path('basic_info',views.basic_info),
	path('select_post',views.select_post),
	path('upload_cv',views.upload_cv),
	path('technical_info',views.technical_info),
	path('reception',views.reception),
	path('success',views.success),
	path('postreq',views.postreq),
	path('login_admin',views.login_admin),
	path('test',views.test),
	path('output',views.output,name='script'),
	path('external',views.external),
	path('url',views.url),
	#path('showvideo',views.showvideo)
	#path('model_form_upload',views.model_form_upload)
]

urlpatterns += staticfiles_urlpatterns()

