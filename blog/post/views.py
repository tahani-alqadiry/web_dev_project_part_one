from django.shortcuts import render,get_object_or_404
from django.views import View
from user_profile.models import User
from .models import Post, Category


#show contents of index.html
class Index(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        users = User.objects.all()
        categories = Category.objects.all()
        params['posts'] = posts
        params['users'] = users
        params['categories'] = categories
        return render(request, 'index.html', params)


# shows all posts in posts.html
class AllPosts(View):
    def get(self, request):
        params = {}
        posts = Post.objects.all().order_by('-release_date')
        params['posts'] = posts
        return render(request, 'posts.html', params)

#contents of blog/username
class Blog(View):
    def get(self, request, blogname):
        content = {}
        blog = User.objects.get(blog_name=blogname)
        posts = blog.post_set.all().order_by('-release_date')
        content['blog'] = blog
        content['posts'] = posts
        return render(request, 'user_blog.html',content)

# content of the blog post
class Post_blog(View):
    def get(self, request, post_id):
        content = {}
        post = Post.objects.get(id=post_id)
        content['post'] = post
        return render(request, 'user_post.html',content)


# the category details of post
class Detail(View):
    def get(self,request, Category_id):
        category = get_object_or_404(Category, id=Category_id)
        return render(request, 'categ_detail.html', {'category': category})


#show all categories
class All_category(View):
    def get(self,request):
        category = Category.objects.all()
        cont = {'category':category}
        return render(request, 'categories.html', cont)


#create post by url
class Create_post(View):
    def get(self,request,post_name):
        try:
            obj = Post.objects.get(title=post_name)
            content = {'post': obj}
            content['msg'] = "The post title exists try another one"
            return render(request, 'create.html', content)
        except Post.DoesNotExist:
            c = Category.objects.get(title='news')
            user = User.objects.get(username='tahani')
            obj = Post(content="this is created by user tahani", category=c, title=post_name, author=user, is_active=True)
            obj.save()
            content = {'post': obj}
            return render(request, 'create.html', content)

#delete post by url
class Delete_post(View):
    def get(self, request, post_name):
        try:
            content = {}
            obj = Post.objects.get(title=post_name).delete()
            content['msg'] = "The post is deleted"
            return render(request, 'delete.html', content)
        except Post.DoesNotExist:
            content = {}
            content['msg'] = "post not exitest"
            return render(request, 'delete.html', content)



#عرض الكومنتس الخاصة بالبوست
#عن طريق بوست آيدي



