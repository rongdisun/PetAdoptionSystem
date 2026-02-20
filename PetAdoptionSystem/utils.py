import uuid
from pathlib import Path
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.deconstruct import deconstructible
from django.views.generic import ListView


class PaginatorMixin:
    def get_page(self, paginator, page, page_offset=2):
        left_more_page = False
        right_more_page = False
        # 获取当前页码
        # 如果当前页面是7
        current_num = page.number
        if current_num <= page_offset + 2:
            left_range = range(1, current_num)
        else:
            left_more_page = True
            left_range = range(current_num - page_offset, current_num)
        if current_num >= paginator.num_pages - page_offset - 1:
            right_range = range(current_num + 1, paginator.num_pages + 1)
        else:
            right_more_page = True
            right_range = range(current_num + 1, current_num + page_offset + 1)
        return {
            'left_range': left_range,
            'right_range': right_range,
            'left_more_page': left_more_page,
            'right_more_page': right_more_page,
        }


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # 设置文件名：UUID + 原始扩展名
        filename = f'{uuid.uuid4().hex}.{ext}'
        # 返回新的路径
        return Path(self.sub_path, filename)


class ListViewPro(ListView, PaginatorMixin):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListViewPro, self).get_context_data(**kwargs)
        page = context.get('page_obj')
        paginator = context.get('paginator')
        context_data = self.get_page(paginator, page)
        context.update(context_data)
        return context