from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField # comming back for this 
# from djrichtextfield.models import RichTextField     come back for this


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_category', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse("blog")



# import sys

# from PIL import Image
# from io import BytesIO
# from django.core.files.uploadedfile import InMemoryUploadedFile

class Post(models.Model):

    author         = models.ForeignKey(User,on_delete=models.CASCADE)
    # category       = models.ForeignKey(Category,related_name='categories', on_delete=models.CASCADE)
    category      = models.CharField(max_length=120)
    title          = models.CharField(max_length=100)
    text           = RichTextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='featured_images',blank=True)
    created_date   = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,null=True)
    likes          = models.ManyToManyField(User,related_name= "author")

    def total_likes(self):
        return self.likes.count()


    def count_like(self):
        qs = Post.objects.filter(likes='likes', author= False)
        if qs.exists():
            return qs[0].Post.count()

    def total_cats(self):
        return self.category.count() 



    def ordering(self):
        published_date = ['-publish_date',]
        created_date = ['-publish_date',]
        return self.created_date +" " + self.published_date

   

    def __str__(self):
        return self.title + " " + str(self.category)

    def post_count(self):
        p_count = Post.objects.count()
        return self.P_count

    

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def published_post(self):
        self.published_date = timezone.now()
        self.save()
    # def approved_comment(self):
        #     return self.comments.filter(approved_comments = True)
    
    

class Comment(models.Model):
  
    post              = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments' )
    name              = models.ForeignKey(User, on_delete=models.CASCADE)
    body              = models.TextField()
    created_date      = models.DateTimeField(auto_now_add=True)
    approved_comment  = models.BooleanField(default=False)
    parent            = models.ForeignKey("self", on_delete=models.SET_NULL, null="True",  blank="True")

    def ordering(self):
        created_date = ('-comment_date',)

    def approve(self):
        self.approved_comment = True
        self.save()

    def count_comment(self):
        qs = Comment.objects.filter(post='post', comments= False)
        if qs.exists():
            return qs[0].Comment.count()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True