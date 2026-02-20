from django import template
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from article.models import *
from common_comment.form import CommentModelForm, Comment

register = template.Library()


@register.simple_tag
def get_cus_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    initial_data = {
        'content_type': content_type,
        'object_pk': obj.pk,
    }
    form = CommentModelForm(initial=initial_data)
    return form


@register.simple_tag
def get_cus_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    comment_counts = Comment.objects.filter(content_type=content_type, object_pk=obj.pk).count()
    return comment_counts


@register.simple_tag
def get_cus_comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    comment_list = Comment.objects.filter(content_type=content_type, object_pk=obj.pk).all()
    return comment_list


