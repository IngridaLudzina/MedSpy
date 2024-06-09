from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path("", views.sakums, name="sakums"),
    path('pakalpojuma_kartites/', views.pakalpojuma_kartites, name='pakalpojuma_kartites'),
    path('tirgus_cenu_izpete/', views.tirgus_cenu_izpete, name='tirgus_cenu_izpete'),
    path('mapping_tabula/', views.mapping_tabula, name='mapping_tabula'),
    path('list/', views.list, name='list'),
    path('list_jauni/', views.jauni_grozijumi, name='jauni_grozijumi'),
    path('list_view/', views.list_view, name='list_view'),
    path('izmaksu_detalizacija/', views.izmaksu_detalizacija, name='izmaksu_detalizacija'),
    path('tirgus/', views.konkurentu_cenas, name='tirgus'),
    path('jauna_forma_pakalpojumi/', views.jauna_forma_pakalpojumi, name='jauna_forma_pakalpojumi'),
    path('jauna_forma_konkurenti/', views.jauna_forma_konkurenti, name='jauna_forma_konkurenti'),
    path('nav_jauna_forma/', views.nav_jauna_forma, name='nav_jauna_forma'), 
    path("logout", views.logout_request, name="logout"), 
    path('insert/', views.insertrecord, name='insert'),
    path('tirgus/edit/<int:pk>/', views.edit, name='edit'),
    path('tirgus/delete/<int:pk>/', views.delete, name='delete'),
    # path('tirgus/<int:pk>/', views.detail_salidzinajums, name='detail'),
    path("login/", views.login_request, name="login"),
]