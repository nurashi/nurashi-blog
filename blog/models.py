from django.db import models


class Category(models.Model):
    """
    Represents a category for blog posts.

    Attributes:
        name (str): The name of the category. Maximum length is 30 characters.

    Methods:
        __str__(): Returns the string representation of the category name.

    Meta:
        verbose_name_plural (str): The plural name for the category model in the admin interface.
    """

    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the blog post.
        body (str): The content of the blog post.
        created_on (datetime): The date and time when the blog post was created.
        last_modified (datetime): The date and time when the blog post was last modified.
        categories (ManyToManyField): The categories associated with the blog post.

    Methods:
        __str__(): Returns the string representation of the blog post, which is its title.
    """



    title = models.CharField(max_length=255)

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    last_modified = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Represents a comment made on a blog post.
    Attributes:
        author (str): The name of the comment's author.
        body (str): The content of the comment.
        created_on (datetime): The date and time when the comment was created.
        post (Post): The blog post that the comment is associated with.
    Methods:
        __str__(): Returns a string representation of the comment.
    """
    
    
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
    
