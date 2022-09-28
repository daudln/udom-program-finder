from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from .models import Program
# Create your views here.


class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program_list'
    paginate_by = 4
    number_in_page = Program.objects.all().count()


class ProgramDetailView(DetailView):
    model = Program
    template_name: str = 'program_detail.html'
