from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path='projects/static/img')
    source_code = models.URLField(max_length=100, blank=True)

    # def url_text(self):
    #     parsed_url = urllib.parse(self.source_code)
    #     return parsed_url

    def __str__(self):
        return self.title