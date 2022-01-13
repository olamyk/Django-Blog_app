from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm,UpdateForm,ProfileForm
from .models import Profile

# Create your views here.

class CreateUser(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserAddProfile(CreateView):
    model = User
    form_class = ProfileForm
    template_name = 'registration/update.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UpdateForm
    template_name = 'registration/user_update.html'
   

    
class UserDetailView(DetailView):
    model = User
    context_object_name = 'user_detail'
    template_name = 'registration/profile.html'



def profile(request,pk):
    template_name = 'registration/user_update.html'
   
    profil_obj =""
    if pk != '':
        print('user number',pk)
        print('------------------------------------')
        profil_obj = Profile.objects.raw("SELECT * FROM `admin_user_profile` WHERE user_id = %s",[pk])
        
    if request.method == 'POST':
        if len(profil_obj) > 0:
            p_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
           
            u_form = UpdateForm(request.POST,instance=request.user)
            
        else:
            p_form = ProfileForm(request.POST,request.FILES)
           
            u_form = UpdateForm(request.POST,instance=request.user)


        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('profile',pk=pk)
    else:
        if len(profil_obj) > 0:
            
            p_form = ProfileForm(instance=request.user.profile)
            u_form = UpdateForm(instance=request.user)
        else:
            p_form = ProfileForm()
            u_form = UpdateForm(instance=request.user)

    context = {'p_form':p_form,'u_form':u_form}
    return render(request,template_name,context)

