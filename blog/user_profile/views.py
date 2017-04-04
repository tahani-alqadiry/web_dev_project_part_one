from django.shortcuts import render
from user_profile.models import User,Blog
from post.models import Post, Category
from django.views import View


class Profile(View):
    def get(self, request,username):
        params = {}
        user = User.objects.get(username=username)
        posts = Post.objects.order_by('-release_date').filter(author=user)[:2]
        params['posts'] = posts
        params['author'] = user
        return render(request, 'profile.html', params)


#view all users
class Users(View):
    def get(self,request):
        params={}
        users= User.objects.all()
        params['users'] = users
        return render(request,'users.html',params)



#contents of blog/username
class User_blog(View):
    def get(self, request, blogname):
        content = {}
        blog = Blog.objects.get(blog_name=blogname)
        user = User.objects.get(username=blog.admin_user)
        posts = user.post_set.all().order_by('-release_date')
        content['blog'] = blog
        content['posts'] = posts
        content['user'] = user
        return render(request, 'user_blog.html',content)
