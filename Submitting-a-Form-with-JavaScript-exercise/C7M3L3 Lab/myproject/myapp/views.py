from django.shortcuts import render
from myapp.forms import MenuForm
from .models import Menu
from django.http import JsonResponse

# Add code for form_view() function below

def form_view(request):
    form = MenuForm()

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            cd = form.cleaned_data

            # Create a new Menu object and populate it with data
            mf = Menu(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description']
            )

            # Save the menu object to the database
            mf.save()

            # Return json response indicating success
            return JsonResponse({'message' : 'success'})
        else:
            # Return a JSON response with form errors if needed
            return JsonResponse({'message': 'failure', 'errors': form.errors.as_json()}, status=400)
        
    return render(request, 'menu_items.html', {'form': form})
"""

from django.shortcuts import render
from myapp.forms import MenuForm
from .models import Menu
from django.http import JsonResponse

def form_view(request):
    form = MenuForm()
    
    if request.method == 'POST':
        form = MenuForm(request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            mf = Menu(
                item_name = cd['item_name'],
                category = cd['category'],
                description = cd['description'],
            )
            
            mf.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'menu_items.html', {'form': form})
"""