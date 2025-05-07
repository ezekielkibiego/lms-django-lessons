from django.shortcuts import render, redirect
from .models import Subscriber, Blog
from django.contrib import messages
from .forms import BlogForm

def blog(request):
    blogs = Blog.objects.all()
    ctx = {'blogs': blogs}
    
    return render(request, 'blog_list.html', ctx)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing for our weekly newsletters.')
            return redirect('subscribe')
        
    return render(request, 'subscribe.html')


def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blog')
        
    else:
        form = BlogForm()
            
    return render(request, 'blog_form.html', {'form': form})
        
