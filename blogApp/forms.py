from django import forms
from blogApp.models import Post,Comment,Category,User
from admin_user.models import Profile




choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','author','category','text','featured_image']

        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'author','type':'hidden'}),
            'category':forms.Select(choices= choice_list, attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'text':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'})
        }

        def __str__(self):
            return f"{self.post.featured_image} profile"

        # def save(self, *args, **kwargs):
        #     super().save(*args, **kwargs)
        #     img = featured_image.open(self.pic.path)
        #     if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        #     if img.height > 300 or img.width > 300:
        #         output_size = (300, 300)
        #         img.thumbnail(output_size)
        #         img.save(self.pic.path)

choose = User.objects.all()
choose_list = []

for something in choose:
    choose_list.append(something)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name','body']
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','value':'','id':'name','type':'hidden'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment'})
        }