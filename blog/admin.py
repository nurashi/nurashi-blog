# blog/admin.py


from django.contrib import admin

from blog.models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):

    pass


class PostAdmin(admin.ModelAdmin):
    """

    This module contains the admin configuration for the blog application.

    Classes:
        PostAdmin: Customizes the admin interface for the Post model.
    """

    pass


class CommentAdmin(admin.ModelAdmin):

    pass


admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)
