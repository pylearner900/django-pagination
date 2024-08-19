from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Flower

# Create your views here.
def index(request):
    flowers = Flower.objects.all()
    f = Paginator(flowers,5)
    page_number = request.GET['page']
    try:
        page_obj = f.page(page_number)
    except PageNotAnInteger:
        page_obj = f.page(1)
    except EmptyPage:
        page_obj = f.page(f.num_pages)
    context = {"page_obj",page_obj}
    return render(request,"paginationapp/index.html",context)