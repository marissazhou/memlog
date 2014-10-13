import datetime
from haystack import indexes
from annotater.models import AnnotationTerm

class AnnotationTermIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='add_at')

    def get_model(self):
        return AnnotationTerm

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(add_at__lte=datetime.datetime.now())

