from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Post, Category, Comment, ContactMessage, Quote, View
from .forms import CommentForm, ContactForm
from django.http import HttpResponseRedirect
from django.db.models import Q

# consider using
# from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


def index(request):
    latest = Post.objects.latest()
    next_post = Post.objects.get(id=latest.id-1)
    categories = Category.objects.all()
    _f = ''
    quote = Quote.objects.latest()
    featured = Post.objects.filter(featured=True) \
    .order_by('-time_stamp')[:4]

    # get latest three posts to populate index page.
    try:
        _f = Post.objects.all()[:3]
    except Exception as e:
        messages.warning(request, 'articles not up to 3' +
                         e, fail_silently=True)

    context = {
        'latest_post': latest,
        'next_post': next_post,
        'categories': categories,
        'latest_3': _f,
        'quote': quote,
        'featured' : featured
    }
    return render(request, 'main/index.html', context)


def post(request, slug):
    categories = Category.objects.all()
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    # new view
    new_view = View.objects.create(post=post)
    
    # comment section
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            reply_id = request.POST.get('comment_id')
            comment_qs = None

            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(
                post=post,
                name=name,
                email=email,
                text=text,
                reply=comment_qs
            )
            comment.save()

            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()

    context = {
        'categories': categories,
        'post': post,
        'form': form,
        'comments': comments
    }
    return render(request, 'main/post.html', context)


def category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'posts': posts
    }
    return render(request, 'main/category.html', context)


def about(request):
    return render(request, 'main/about.html', context={})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("text")

            new_message = ContactMessage.objects.create(name=name, email=email, message=message)
            new_message.save()
    else:
        form = ContactForm()
    
    context = {'form' : form}

    return render(request, 'main/contact.html', context)


def search(request):
    categories = Category.objects.all()
    post_qs = Post.objects.all()
    # category_qs = Category.objects.all()
    query = request.GET.get('q')
    recent_posts = Post.objects.all().order_by('-time_stamp')[:3]

    if query:
        post_qs = post_qs.filter(title__icontains=query)
    
    context = {
        'search_results' : post_qs,
        'query' : query,
        'categories' : categories,
        'recent_posts' : recent_posts
    }
    
    return render(request, 'main/search.html', context)
