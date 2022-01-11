from urllib import request

import username
from django.forms import TextInput
from django.template.backends.jinja2 import Template
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from geopy import MapBox
from requests import post

from .models import Post, Comment
from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from .forms import CommentForm, NewsContentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category


class CompanyListView(ListView):
    model = Post
    template_name = 'home.html'
    #paginate_by = 12
    comp_categories = Category.objects.all().count()
    context = {'comp_categories': comp_categories},

class CompanyDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class CompanyCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = [ 'name', 'unp', 'categories', 'logo', 'text',  'country', 'city', 'street', 'address', 'dop_address', 'phone', 'email', 'site', 'telegram', 'viber', 'whatsapp', 'instagram', 'vk', 'ok', 'facebook',]
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CompanyUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['name', 'categories', 'unp', 'logo', 'text',  'country', 'city', 'street', 'address', 'dop_address', 'phone', 'email', 'site', 'telegram', 'viber', 'whatsapp', 'instagram', 'vk', 'ok', 'facebook',]


class CompanyDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class AuthorCompanyListView(ListView):
    model = Post
    template_name = 'author_posts.html'

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'company/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def company_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "company_category.html", context)

def company_country(request, country):

    posts = Post.objects.filter(
        countries__name__contains=country
    )
    context = {
        "country": country,
        "posts": posts
    }
    return render(request, "company_country.html", context)


# def author_posts(request, author):
#
#     posts = Post.objects.filter(
#         author__name__contains=author
#     )
#     context = {
#         "author": author,
#         "posts": posts
#     }
#     return render(request, "author_posts.html", context)

# def post(request, category_slug=None, subcategory_slug=None):
#     category=None
#     subcategory=None
#     if category_slug:
#         category=get_object_or_404(Category, slug='category_slug')
#         if subcategory_slug:
#             subcategory=get_object_or_404(Category, slug='subcategory_slug')
#
#     seodata=Post.objects.all()
#     context={'seodata':seodata,
#              'category':category,
#              'subcategory':subcategory
#     }
#
#     return render(request, 'home.html', context)