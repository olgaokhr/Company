# company/urls.py
from django.urls import path
from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView, \
    add_comment_to_post, comment_approve, comment_remove, company_category
from . import views

urlpatterns = [
    path('post/<int:pk>/delete/',  CompanyDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', CompanyUpdateView.as_view(), name='post_edit'),
    path('post/new/', CompanyCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', CompanyDetailView.as_view(), name='post_detail'),
    path('', CompanyListView.as_view(), name='home'),
path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
   path("<category>/", company_category, name="company_category"),
path('category/<int:pk>/', company_category, name="company_category"),
   #  path("<username>/", author_posts, name="author_posts"),
#    path("<author>/", author_posts, name="author_posts"),
# path('author/<int:pk>/', author_posts, name="author_posts"),

]
