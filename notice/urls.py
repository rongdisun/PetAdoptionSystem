from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path("unread_notice_list/", views.UnreadNoticeListView.as_view(), name="unread_notice_list"),
    path("read_notice_list/", views.ReadNoticeListView.as_view(), name="read_notice_list"),
    path("update/", views.NoticeUpdateView.as_view(), name="notice_update"),
]
