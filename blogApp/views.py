from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import( View,TemplateView,CreateView,ListView,
                                  DetailView,UpdateView,DeleteView)
from .models import Post,Comment,Category
from .forms import PostForm,CommentForm
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.db.models import Count

from django.views.generic.detail import ContextMixin



#Create your views here.

class HomeListView(ListView):
    model = Post
    template_name = 'blogApp/blog.html'
    
    paginate_by = 6
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        

    def get_context_data(self,*args,**kwargs):
        categories = Post.objects.values('category').annotate(posts_count=Count('category'))
        # print(categories)
        likes = Post.objects.values('likes').annotate(count_like=Count('likes'))
        print(likes)
        display_menu =Category.objects.all()
        recent_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:5]
        context = super(HomeListView, self).get_context_data(**kwargs)  
        context ['categories'] = categories
        context ['recent_post'] = recent_post
        context ['display_menu'] = display_menu
        context ['likes'] = likes
        return context


def CategoryListView(request,cats):
    display_menu = Category.objects.all()
    category_post = Post.objects.filter(category=cats.replace('_', ' '))
    active = Post.objects.filter(category=cats.replace('_', ' '))
    context = {}
    context ['cats'] = cats.title().replace('_', ' ')
    context ['category_post'] = category_post
    context ['display_menu'] = display_menu
    context ['active'] = active
    # context ['active'] = current
    return render(request, 'blogApp/post_category.html', context)



def cat_on_all_pages(request):
    return {'display_menu': Category.objects.all()}

class AboutTemplate(TemplateView):
    template_name = 'blogApp/about.html'



class ContactTemplate(TemplateView):
    template_name = 'blogApp/contact.html'



class CreateTemplate(CreateView):
    login_url = 'login'
    redirect_field_name = 'blogApp/blog.html'
    form_class = PostForm
    model = Post
    template_name = 'blogApp/create.html'




class AddCategoryView(CreateView):
    model = Category
    template_name = "blogApp/category.html"
    success_url = reverse_lazy('blog')
    fields = '__all__'



class DraftListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    context_object_name = 'drafts' 
    model = Post 
    template_name = 'blogApp/draft_view.html'
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

def puplish_drafts_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.published_post()
    return redirect('blog')   

class UpdateRecs(LoginRequiredMixin,UpdateView):
    template_name = 'blogApp/update.html'
    fields = ('title','text','category')
    model = Post


class DeletePost(DeleteView):
    template_name = "blogApp/delete.html"
    model = Post
    success_url = reverse_lazy('create')


class PostDetailView(DetailView): 
    template_name = "blogApp/blogdetails.html"
    context_object_name ="post_detail"
    model = Post
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        success_url = reverse_lazy('blog')

    def get_context_data(self,*args,**kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        categories = Post.objects.values('category').annotate(posts_count=Count('category'))
        display_menu = Category.objects.all()
        
        stuff = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id= self.request.user.id).exists():
            liked = True
        context ['total_likes'] = total_likes
        context ['liked'] = liked
        context ['display_menu'] = display_menu
        context ['categories'] = categories
        return context




def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked= True
    return HttpResponseRedirect( reverse('post_detail', args=[str(pk)] ))



class AddCommentView(CreateView):
    model = Comment
    template_name = "blogApp/comment.html"
    form_class = CommentForm
    

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        parent_obj = None
        try:
            parent_id = int(form.POST.get('parent_id'))# i replace request with form in this line
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id= parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()
        return super().form_valid(form)
    success_url = reverse_lazy('blog')
    
    def get_context_data(self,*args, **kwargs):
        context = super(AddCommentView, self).get_context_data(**kwargs)
        display_menu = Category.objects.all()
        context ['display_menu'] = display_menu
        return context

class ApproveComment(DetailView):
    model = Comment
    template_name = 'blogApp/approve_comment.html'
    form_class = CommentForm


#############********************PAGINATION CODE AS FUNCTION NOW WORKING WELL ***###########
                                        
                                        
def PostList(request):
    template_name = 'blogApp/blog.html'
    recent_post = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    object_list = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    paginator = Paginator(object_list, 8)
    page = request.GET.get('page')
    
    try:
        post_list =paginator.page(page)
    except PageNotAnInteger:
        post_list =paginator.page(1)

        

    except EmptyPage:
        post_list =paginator.page(paginator.num_pages)

    return render(request,template_name,{'page':page,'object_list': object_list, 'recent_post':recent_post})
    

# class BaseContextMixin(ContextMixin):
    
#     def get_context_data(self, **kwargs):
#         context_data = super(BaseContextMixin,self).get_context_data(**kwargs)
#         common_data_first = Category.objects.all()
#         context ['common_data_first'] = common_data_first
#         return context_data