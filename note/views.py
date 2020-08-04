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
    
class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    fields = ['title','contents','background_color']

class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
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


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

