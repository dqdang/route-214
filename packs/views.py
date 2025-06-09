# route_214/packs/views.py

from django.shortcuts import render
from django.db.models import Q
import datetime
from django.db.models import F # Import F object for database expressions

from .models import BoosterPack

def pack_list(request):
    all_packs = BoosterPack.objects.all()
    query = request.GET.get('q')

    # --- Sorting Logic ---
    sort_by = request.GET.get('sort', 'tier')
    order = request.GET.get('order', 'asc')

    allowed_sort_fields = {
        'tier': 'tier',
        'set_name': 'set_name',
        'release_date': 'release_date',
        'price_range': 'price_range', # Keep this for display logic, but use hidden fields for actual sorting
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


    # --- Filtering Logic ---
    if query:
        combined_q_object = Q(set_name__icontains=query)
        try:
            year = int(query)
            combined_q_object |= Q(release_date__year=year)
        except ValueError:
            pass # No additional date filter if query is not a year
        all_packs = all_packs.filter(combined_q_object)
    
    # --- Tier Grouping Logic (retained as before, but adapted slightly) ---
    # This tier grouping logic will only work visually if the primary sort IS NOT 'tier'
    # If sort_by == 'tier', the initial ordering already handles the grouping.
    # The current tier grouping logic makes sense if you want a visual break,
    # but it can conflict with general sorting if not handled carefully.
    # For now, if sorting by tier, we let the database sort handle it.
    
    # If the user is sorting by 'tier', the `all_packs.order_by(F('tier')...)` already sorts them correctly.
    # The `grouped_packs` list is then just the result of that queryset.
    # The `is_new_tier` logic is only needed for visual separators *when the primary sort is NOT tier*,
    # or if you want specific custom ordering within tiers.
    
    # Let's refine the tier grouping to only apply when sorting by tier, and then also apply a secondary sort.
    # When not sorting by tier, the original behavior of just listing them will continue.
    
    # Important: If you want proper numerical sorting of 'Tier 1', 'Tier 2', 'Tier 10', etc.,
    # you might need to extract the number from the tier string for sorting,
    # or ideally, assign a numerical order to tiers in your model.
    # For now, I'm assuming 'Tier 1', 'Tier 2', 'Tier 3' etc. will sort as expected as strings.
    
    grouped_packs = list(all_packs) # Convert QuerySet to list after all sorting/filtering
    
    # This part was primarily for reversing and marking tiers, which is now handled differently
    # if sort_by is 'tier', or not needed for other sorts.
    # If you still want the visual separators, you'd iterate the already sorted `grouped_packs`
    # and add `is_new_tier` flags, which is what the loop below does.

    if sort_by == 'tier':
        # If sorting by tier, we want the tier headers.
        # The database query already sorted by tier (and then set_name).
        # We need to re-apply the `is_new_tier` logic to this already sorted list.
        temp_grouped_packs = []
        last_tier = None
        for pack in grouped_packs: # Iterate through the already sorted list
            if pack.tier != last_tier:
                pack.is_new_tier = True
            else:
                pack.is_new_tier = False
            temp_grouped_packs.append(pack)
            last_tier = pack.tier
        grouped_packs = temp_grouped_packs
    else:
        # If not sorting by tier, no tier separators are needed.
        # Ensure 'is_new_tier' is false for all in this case.
        for pack in grouped_packs:
            pack.is_new_tier = False

    context = {
        'packs': grouped_packs,
        'query': query,
        'current_sort_by': sort_by,
        'current_order': order,
    }
    return render(request, 'packs/pack_list.html', context)
