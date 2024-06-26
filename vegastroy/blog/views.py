from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib import messages


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog_index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'blog/blog_details.html', context)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully.')
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
    }

    return render(request, 'blog/blog_edit.html', context)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('blog_home')

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_delete.html', context)


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('blog_home')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/blog_new.html', context)
