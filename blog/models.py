from django.db import models

class Page(models.Model):
    page_title = models.TextField()
    page_date = models.DateField(auto_now_add=True)
    page_content = models.TextField()
    delete_flag = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.id) + ": " + self.page_title)

class Comment(models.Model):
    comment_name = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    comment_content = models.TextField()
    comment_page = models.ForeignKey(Page)
    delete_flag = models.BooleanField(default=False)
    def __str__(self):
        return (str(self.id) + ": " + self.comment_name)
