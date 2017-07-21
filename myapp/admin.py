# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import UserModel,LikeModel,PostModel,CommentModel

admin.site.register(UserModel)
admin.site.register(LikeModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)
# Register your models here.
