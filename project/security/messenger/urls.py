from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.session, name='session'), #FLAW 2 fix: path('', views.index, name='index')
    path('<str:session_id>/logout/', LogoutView.as_view(next_page='/login')), #FLAW 2 fix: remove "<str:session_id>/"
    path('change/', views.changeUsername, name='change'), #FLAW 2 fix: remove the comma at the end and "<str:session_id>/"
    path('<str:session_id>/', views.index, name='index') #FLAW 2 fix: remove this line
]