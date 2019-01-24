from .mixins import BaseModelMixin
from django.db import models
from haystack import indexes as haystack_indexes

class Paper(BaseModelMixin, haystack_indexes.SearchIndex, haystack_indexes.Indexable):
    """
        Model definition for research paper
    """
    title = haystack_indexes.CharField(document=True)
    abs_page_linkabstract = haystack_indexes.CharField()
    abstract = haystack_indexes.CharField()
    all_categories = haystack_indexes.TextField()
    arxiv_id = haystack_indexes.TextField()
    author = haystack_indexes.TextField()
    comment = haystack_indexes.TextField()
    created_at = haystack_indexes.DateTimeField()
    journal_ref = haystack_indexes.TextField()
    last_author = haystack_indexes.TextField()
    pdf_link = haystack_indexes.TextField()
    primary_category = haystack_indexes.TextField()
    published = haystack_indexes.DateTimeField()
    updated_at = haystack_indexes.DateTimeField()

    def get_model(self):
        return Paper

    def __str__(self):
        return self.title