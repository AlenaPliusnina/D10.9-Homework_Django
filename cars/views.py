from django.db.models import Q
from django.views.generic import ListView
from cars.models import Car


class CarsList(ListView):
    queryset = Car.objects.all()
    template_name = "index.html"
    context_object_name = "cars"


class SearchResultsView(ListView):
    model = Car
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == '1' or query == '2' or query == '3':
            object_list = Car.objects.filter(
                Q(transmission__icontains=query)
            )
        elif query == 'механика':
            object_list = Car.objects.filter(
                Q(transmission__icontains='1')
            )
        elif query == 'автомат':
            object_list = Car.objects.filter(
                Q(transmission__icontains='2')
            )
        elif query == 'робот':
            object_list = Car.objects.filter(
                Q(transmission__icontains='3')
            )
        else:
            object_list = Car.objects.filter(
                Q(company__icontains=query)
                | Q(model__icontains=query)
                | Q(year__icontains=query)
                | Q(color__icontains=query)
            )

        return object_list











