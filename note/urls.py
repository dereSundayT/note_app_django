from django.urls import path 
from .views import home_view,register_view,Login,Logout,NoteCreateView,NoteDetailView,NoteListView

urlpatterns = [
    path('',NoteListView.as_view(),name="note-list"),
    path('register/',register_view,name="note-register"),
    path('login/',Login.as_view(),name="note-login"),
    path('logout/',Logout.as_view(),name="note-logout"),
    path('notes/create',NoteCreateView.as_view(),name='note-create'),
    path('notes/<int:pk>/',NoteDetailView.as_view(),name="note-detail"),
    path('notes/',NoteListView.as_view(),name="note-list")
]
