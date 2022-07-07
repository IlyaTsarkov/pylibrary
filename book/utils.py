from .models import *


class DataMixin:
    model = Book
    paginate_by = 5
    context_object_name = 'books'
