from django import template
from user.models import User
from forum.models import Post
from django.db.models.aggregates import Count, Sum
import pytz
from datetime import datetime

register = template.Library()


@register.simple_tag
def top_author_post():
    return Post.objects.values("author").annotate(top_post_user=Count("id")).order_by("top_post_user")[0:10]
