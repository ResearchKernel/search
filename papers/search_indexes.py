from .mixins import BaseModelMixin
from haystack import indexes as haystack_indexes
import datetime
from .models import Paper

class PaperIndex(haystack_indexes.SearchIndex, haystack_indexes.Indexable):
    """
        Model definition for research paper
    """
    text = haystack_indexes.CharField(document=True, use_template=True)
    title = haystack_indexes.CharField()
    abs_page_linkabstract = haystack_indexes.CharField()
    abstract = haystack_indexes.CharField()
    all_categories = haystack_indexes.CharField()
    arxiv_id = haystack_indexes.CharField()
    author = haystack_indexes.CharField()
    comment = haystack_indexes.CharField()
    created_at = haystack_indexes.DateTimeField()
    journal_ref = haystack_indexes.CharField()
    last_author = haystack_indexes.CharField()
    pdf_link = haystack_indexes.CharField()
    primary_category = haystack_indexes.CharField()
    published = haystack_indexes.DateTimeField()
    updated_at = haystack_indexes.DateTimeField()

    def get_model(self):
        return Paper

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()