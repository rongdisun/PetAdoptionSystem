from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('article_detail/<pk>', views.ArticleDetail.as_view(), name="article_detail"),
    path('special_cate_article/<pk>', views.SpecialCateArticle.as_view(), name="special_cate_article"),
    path('special_tag_article/<pk>', views.SpecialTagArticle.as_view(), name="special_tag_article"),
    path('search_article/', views.SearchArticle.as_view(), name="search_article"),
    path('publish_article/', views.PublishArticle.as_view(), name="publish_article"),

    path("chart_view/", views.chart_view, name="chart_view"),
    path("cate_articles_per/", views.cate_articles_per, name="cate_articles_per"),
    path("article_views_rank/", views.article_views_rank, name="article_views_rank"),

]