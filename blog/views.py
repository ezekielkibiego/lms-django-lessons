from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber, Blog
from django.contrib import messages
from .forms import BlogForm

def bloglist(request):
    blogs = Blog.objects.all()
    ctx = {'blogs': blogs}
    
    return render(request, 'blogs/blog_list.html', ctx)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing for our weekly newsletters.')
            return redirect('blog:subscribe')
        
    return render(request, 'subscribe.html')


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog:bloglist')
        
    else:
        form = BlogForm()
            
    return render(request, 'blogs/blog_form.html', {'form': form})
        
def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog:bloglist')
    
    return render(request, 'blogs/edit_blog.html', {'form': form})
        
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    
    return redirect('blog:bloglist')