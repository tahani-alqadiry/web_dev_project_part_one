
from django.conf.urls import url
from django.contrib import admin
from post.views import Index,Detail,AllPosts,Create_post,Delete_post,All_category
from post.views import Post_blog
from user_profile.views import Profile,Users,User_blog

# from post import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #بروفايل المستخدم
    #/user/username
    url(r'^user/(\w+)/$', Profile.as_view(), name="profile_detail"),

    #/user dash_bored
    url(r'^$',Index.as_view()),

    #posts by id
    #/posts/<post_id>/
    url(r'^posts/(?P<post_id>[0-9]+)/$', Post_blog.as_view()),


    #show all posts within a category
    #عرض المنشورات الخاصة بتصنيف معين
    #posts/category/category_id
    url(r'^posts/category/(?P<Category_id>[0-9]+)/$', Detail.as_view(),name="detail"),

    #view all published posts
    #posts/
    url(r'^posts/$', AllPosts.as_view()),

    #view blog by blog_name
    #/blog/blog_name/
    # صفحة المدونة حسب اسم المدونة
    #/blog/sabreenblog
    url(r'^blog/(\w+)/$', User_blog.as_view(), name='user_blog'),


    # view blog_post by blog_name and post_id
    # /blog/blog_name/post/post_id


    #create post
    #posts/create/post_name
    url(r'^posts/create/(\w+)/$',Create_post.as_view()),

    #delete post
    #posts/delete/post_name
    url(r'^posts/delete/(\w+)/$',Delete_post.as_view()),

    #show all users
    #users/
    url(r'^users/$',Users.as_view()),

    #show all categories
    #posts/category/
    url(r'^posts/category/$', All_category.as_view(), name='go_to_categories')

    #show posts by username
    #user/username/posts
    #example: user/tahani/posts

    #show post comments
    #/post/<post_id>/comments

    #show post<post_id> by blogname
    #blog/blogname/post/post_id






]
