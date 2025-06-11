from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm

def home(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/home.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('home')
    return render(request, 'notes/create.html')

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('home')
    return render(request, 'notes/edit.html', {'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('home')

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})

@login_required
def dashboard(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'notes/dashboard.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'notes/post_form.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    form = BlogPostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'notes/post_form.html', {'form': form})