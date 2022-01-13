from django.urls import path
from . import views

urlpatterns =[
    
    path('about',views.AboutTemplate.as_view(), name= 'about'),
    path('contact',views.ContactTemplate.as_view(), name= 'contact'),
    path('create',views.CreateTemplate.as_view(), name= 'create'),
    path('draft',views.DraftListView.as_view(), name='draft'),
    path('update/<int:pk>',views.UpdateRecs.as_view(),name='update'),
    path('delete/<int:pk>',views.DeletePost.as_view(),name='delete'),
    path('post_detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path("publish/<int:pk>",views.puplish_drafts_post,name="publish"),
    path('comment/<int:pk>',views.AddCommentView.as_view(),name='comment'),
    path('reply/<int:pk>',views.AddCommentView.as_view(),name='reply'),
    path('approve/comment/<int:pk>', views.ApproveComment.as_view(), name='c_approve'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('add/category',views.AddCategoryView.as_view(), name= 'addcats'),

    path('category/<str:cats>/',views.CategoryListView, name= 'category'),
    
]