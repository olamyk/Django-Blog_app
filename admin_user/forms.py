from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from admin_user.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    
class UpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['pic','bio','address']

        # widgets = {
            
        #     'bio':forms.TextInput(attrs={'class':'form-control','placeholder':'Biography'}),
        #     'address':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Address'})
        # }



        

# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_location')
#     list_select_related = ('profile', )

#     def get_location(self, instance):
#         return instance.profile.location
#     get_location.short_description = 'Location'

#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomUserAdmin, self).get_inline_instances(request, obj)