# django_sandbox
Django playground


- django-admin startproject djangonautic

- python manage.py runserver

- python manage.py startapp articles

- python manage.py makemigrations

- python manage.py migrate

- python manage.py sqlmigrate blog 0001

- python manage.py createsuperuser

 ime@ime-desktop  ~/Build/django_sandbox/django_project  develop_django ● ?  python manage.py shell                      1 ↵  2754  22:04:38 
Python 3.7.3 (default, Apr  3 2019, 19:16:38) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
>>> user = User.objects.filter(username='NenadS').first()
>>> user
<User: NenadS>
>>> Post.objects.all()
<QuerySet []>
>>> post_1 = Post(title='Blog 1', content='First Post Content!', author=user)
>>> Post.objects.all()
<QuerySet []>
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>]>
>>> 