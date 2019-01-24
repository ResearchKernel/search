from .mixins import BaseModelMixin
from django.db import models
import datetime

class Paper(BaseModelMixin):
    """
        Model definition for research paper
    """
    title = models.TextField()
    abs_page_linkabstract = models.TextField()
    abstract = models.TextField()
    all_categories = models.TextField()
    arxiv_id = models.TextField()
    author = models.TextField()
    comment = models.TextField()
    created_at = models.DateTimeField()
    journal_ref = models.TextField()
    last_author = models.TextField()
    pdf_link = models.TextField()
    primary_category = models.TextField()
    published = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.title
