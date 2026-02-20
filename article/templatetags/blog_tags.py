from django import template
from article.models import Article, Category, Tag
from django.db.models.aggregates import Count
import pytz
from datetime import datetime

register = template.Library()


@register.simple_tag
def get_all_category():
    return Category.objects.annotate(num_articles=Count("article_category"))


@register.simple_tag
def get_all_tags():
    return Tag.objects.annotate(num_articles=Count("article_tag"))


@register.simple_tag
def get_recent_post():
    return Article.objects.filter(status=1).order_by("-post_time")[:5]
