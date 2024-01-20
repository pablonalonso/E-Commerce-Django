from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
	path('wa.link/<str:wa_link>/', views.wa_link_view, name='wa_link'),
]
