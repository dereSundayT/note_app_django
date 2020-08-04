from django.urls import path 
from .views import home_view,register_view,Login,Logout,NoteCreateView,NoteDetailView

urlpatterns = [
    path('',home_view,name="note-home"),
    path('register/',register_view,name="note-register"),
    path('login/',Login.as_view(),name="note-login"),
    path('logout/',Logout.as_view(),name="note-logout"),
    path('notes/create',NoteCreateView.as_view(),name='note-create'),
    path('notes/<int:pk>/',NoteDetailView.as_view(),name="note-detail"),
]
