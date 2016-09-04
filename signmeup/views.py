from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from signmeup.task import write_post_entry
from .forms import PostForm

# Create your views here.
def post_thanks(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'signmeup/post_thanks.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            write_post_entry.delay(name=post.name, email=post.email)
	    #return redirect('post_thanks', pk=post.pk)
	    return redirect('post_thanks', 44)
    else:
        form = PostForm()
    return render(request, 'signmeup/post_add.html', {'form': form})
