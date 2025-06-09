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
        'tier': 'tier',
        'set_name': 'set_name',
        'release_date': 'release_date',
        'price_range': 'price_range',
    }

    if sort_by not in allowed_sort_fields:
        sort_by = 'tier'

    sort_field_prefix = ''
    if order == 'desc':
        sort_field_prefix = '-'

    # Apply sorting based on selected field
    if sort_by == 'price_range':
        # For price, use low_price for ascending, high_price for descending
        if order == 'asc':
            all_packs = all_packs.order_by(f'{sort_field_prefix}low_price', 'set_name') # Add secondary sort
        else: # 'desc'
            all_packs = all_packs.order_by(f'{sort_field_prefix}high_price', 'set_name') # Add secondary sort
    elif sort_by == 'tier':
        # For tier, we still want custom grouping, and default sorting should be on tier itself
        # The F() expression helps with sorting text fields that have a custom order (like Tier 1, Tier 2, etc.)
        # This is important because 'Tier 10' would sort before 'Tier 2' alphabetically.
        # Assuming your tiers are ordered like "Tier 1: ...", "Tier 2: ...", etc.
        # This will need careful adjustment if your tier names are not numerically sortable by string.
        # A better long-term solution for tiers might be a separate Tier model with an 'order' field.
        # For now, we'll sort directly on the string, but be aware of "Tier 10" vs "Tier 2" issue.
        if order == 'asc':
            all_packs = all_packs.order_by(F('tier').asc(), 'set_name') # Default to set_name within tier
        else:
            all_packs = all_packs.order_by(F('tier').desc(), 'set_name') # Default to set_name within tier
    else:
        # For other fields (set_name, release_date), use the standard sorting
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
