import pandas as pd
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
import os

# Create your views here.
def home(request):
	return render(request,'home.html')
def geo(request):
	return render(request,'geo.html')	
def inspectionpolicy(request):
	return render(request,'inspectionpolicy.html')


def zipcode(request):
    # Initialize variables
    query = request.GET.get('zipcode', '').strip()
    results = None

    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')
    print(f"Looking for CSV at: {csv_file_path}")  # Debugging

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        if query:
            # Filter the DataFrame based on the zip code
            results = df[df['Zip_Code'].astype(str) == query]
            # Convert results to a list of dictionaries
            results = results.to_dict(orient='records')

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        print(error_message)
        return render(request, 'zipcode.html', {'error': error_message, 'query': query})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'zipcode.html', {'error': f'Error loading data: {e}', 'query': query})

    return render(request, 'zipcode.html', {'results': results, 'query': query})


def allrestaurants(request):
    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        # Convert DataFrame to a list of dictionaries for rendering in the template
        restaurants = df.to_dict(orient='records')

        return render(request, 'allrestaurants.html', {'restaurants': restaurants})

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        print(error_message)
        return render(request, 'allrestaurants.html', {'error': error_message})

    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'allrestaurants.html', {'error': f'Error loading data: {e}'})

def restaurantname(request):
    # Get the search query from the request
    query = request.GET.get('restaurant_name', '').strip()
    results = None

    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        if query:
            # Filter DataFrame by restaurant name (case-insensitive)
            results = df[df['Restaurant_Name'].str.contains(query, case=False, na=False)]
            # Convert results to a list of dictionaries
            results = results.to_dict(orient='records')

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        return render(request, 'restaurantname.html', {'error': error_message, 'query': query})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'restaurantname.html', {'error': f'Error loading data: {e}', 'query': query})

    return render(request, 'restaurantname.html', {'results': results, 'query': query})

def restauranttype(request):
    # Get the search query from the request
    query = request.GET.get('restaurant_category', '').strip()
    results = None

    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        if query:
            # Filter DataFrame by restaurant type (case-insensitive)
            results = df[df['Restaurant_Category'].str.contains(query, case=False, na=False)]
            # Convert results to a list of dictionaries
            results = results.to_dict(orient='records')

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        return render(request, 'restauranttype.html', {'error': error_message, 'query': query})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'restauranttype.html', {'error': f'Error loading data: {e}', 'query': query})

    return render(request, 'restauranttype.html', {'results': results, 'query': query})

def streetaddress(request):
    # Get the search query from the request
    query = request.GET.get('street_address', '').strip()
    results = None

    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        if query:
            # Filter DataFrame by street address (case-insensitive)
            results = df[df['Street_Address'].str.contains(query, case=False, na=False)]
            # Convert results to a list of dictionaries
            results = results.to_dict(orient='records')

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        return render(request, 'streetaddress.html', {'error': error_message, 'query': query})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'streetaddress.html', {'error': f'Error loading data: {e}', 'query': query})

    return render(request, 'streetaddress.html', {'results': results, 'query': query})


def inspectionscore(request):
    # Get the inspection score query from the request
    query = request.GET.get('inspection_score', '').strip()
    results = None

    # Path to your CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'dallasanalysis', 'data', 'Updated_dataset_uniqe_id.csv')

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path)

        # Replace spaces in column names with underscores
        df.columns = df.columns.str.replace(' ', '_')

        if query.isdigit():
            # Filter DataFrame by inspection score
            results = df[df['Inspection_Score'] == int(query)]
            # Convert results to a list of dictionaries
            results = results.to_dict(orient='records')
        elif query:
            # If query is not numeric, display an error
            return render(request, 'inspectionscore.html', {'error': 'Please enter a valid numeric inspection score.', 'query': query})

    except FileNotFoundError:
        error_message = f"CSV file not found at: {csv_file_path}. Please ensure the file exists."
        return render(request, 'inspectionscore.html', {'error': error_message, 'query': query})
    except Exception as e:
        print(f"Unexpected error: {e}")
        return render(request, 'inspectionscore.html', {'error': f'Error loading data: {e}', 'query': query})

    return render(request, 'inspectionscore.html', {'results': results, 'query': query})



def powerbidashboard(request):
    return render(request, 'powerbidashboard.html')

