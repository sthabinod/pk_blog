from django.db import models

# blog_table - (id, title,description, image)

class BlogTable(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='blog-image')
    # virula env
    # create table migrate
    # show data from database
    # connect postgres and setup in dbeaver
    # push project to github
    