from django.urls import path, include
from .views import *

app_name = "post"

urlpatterns = [

    path("", IndexView.as_view(), name="index"),
    path("search/", SearchView.as_view(), name="search"),
    path("hot_post/", HotPostView.as_view(), name="hot_post"),
    path("cate_list/", CateList.as_view(), name="cate_list"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path("cate_post/", CatePost.as_view(), name="cate_post"),
    path("detail/<int:pk>", PostDetail.as_view(), name="detail"),
    path("user_author_view_follow/<author_id>", user_author_view_follow, name="user_author_view_follow"),
    path("author_detail/", AuthorDetail.as_view(), name="author_detail"),
    path("user_follow/<author_id>/<object_pk>", user_follow, name="user_follow"),
    path("user_thumb_up/", user_thumb_up, name="user_thumb_up"),
    path("user_thumb_down/", user_thumb_down, name="user_thumb_down"),


]
