import django_filters
from django_filters import DateFilter
from .models import *


# The FilterSet is capable of automatically generating filters
# for a given model’s fields. Similar to Django’s ModelForm, filters
# are created based on the underlying model field’s type. This option must be
# combined with either the fields or exclude option, which is
# the same requirement for Django’s ModelForm class
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    start_date1 = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
