from celery import task
from django.utils import timezone
from models import Post
from .forms import PostForm

@task()

def write_post_entry(name, email):
    
    log = Post(name=name, email=email)
    log.signup_date = timezone.now()
    log.save()  

