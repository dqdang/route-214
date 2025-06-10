# route_214/packs/views.py

from django.shortcuts import render
from django.db.models import Q
import datetime
from django.db.models import F # Import F object for database expressions

from .models import BoosterPack

def pack_list(request):
    all_packs = BoosterPack.objects.all()
    query = request.GET.get('q')

    sort_by = request.GET.get('sort', 'release_date')
    order = request.GET.get('order', 'asc')

    allowed_sort_fields = {
        'set_name': 'set_name',
        'release_date': 'release_date',
        'price_range': 'price_range',
    }

    if sort_by not in allowed_sort_fields:
        sort_by = 'release_date'

    sort_field_prefix = ''
    if order == 'desc':
        sort_field_prefix = '-'

    # Apply sorting based on selected field
    all_packs = all_packs.order_by(f'{sort_field_prefix}{sort_by}')

    if query:
        combined_q_object = Q(set_name__icontains=query)
        try:
            year = int(query)
            combined_q_object |= Q(release_date__year=year)
        except ValueError:
            pass # No additional date filter if query is not a year
        all_packs = all_packs.filter(combined_q_object)

    grouped_packs = list(all_packs) # Convert QuerySet to list after all sorting/filtering

    context = {
        'packs': grouped_packs,
        'query': query,
        'current_sort_by': sort_by,
        'current_order': order,
    }
    return render(request, 'packs/pack_list.html', context)
