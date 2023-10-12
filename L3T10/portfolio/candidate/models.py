from django.db import models

# Create your models here.
class BlogPost(models.Model):
    '''Represents a blog post.

    Attributes:
        title (str): The title of the blog post, with a maximum length of 200 characters.
        content (str): The content of the blog post, typically longer text.
        pub_date (datetime): The date and time when the blog post was created (auto-generated).
    '''
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''Returns a string representation of the blog post.

        Returns:
            str: The title of the blog post.
       '''
        return self.title