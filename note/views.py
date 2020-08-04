from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Note

from .forms import RegisterForm

# Create your views here.

def home_view(request):
    return render(request,'home.html')

class NoteListView(LoginRequiredMixin,ListView):
    model = Note

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user.id)
    
class NoteUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Note
    fields = ['title','contents','background_color']

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        else:
            return False

    def handle_no_permission(self):
        return redirect('note-list')


class NoteDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def test_func(self):
        note = self.get_object()
        if note.author == self.request.user:
            return True
        else:
            return False
    def handle_no_permission(self):
        return redirect('note-list')
#register
def register_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note-home')
    else:
        form = RegisterForm()
    return render(request,'reg.html',{'form':form})
#login

class Login(LoginView):
    template_name = 'login.html'

class Logout(LogoutView):
    template_name = 'logout.html'

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    fields = ['title','contents','background_color']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = Note

    def test_func(self):
        note = self.get_object()
        if note.author == self.request.user:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        return redirect('note-list')
