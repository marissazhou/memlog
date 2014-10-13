import datetime
from haystack import indexes
from fileuploader.models import Image 

class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    capture_at = indexes.DateTimeField(model_attr='capture_at')

    def get_model(self):
        return Image 

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(capture_at__lte=datetime.datetime.now())

