from .forms import SearchForm
from .models import Project

def search_results(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = Project.objects.filter(title__icontains=query)

    return {'search_form': form, 'search_results': results}