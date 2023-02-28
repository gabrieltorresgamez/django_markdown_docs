from django.db import models


class MarkdownFile(models.Model):
    """A markdown file that can be edited and rendered."""

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name
