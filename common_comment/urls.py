from django.urls import path
from . import views

app_name = "common_comment"

urlpatterns = [
    path("post-comment/", views.post_comment, name="post_comment"),
    path("post-comment/<int:parent_comment_id>", views.post_comment, name="reply_comment"),
]
