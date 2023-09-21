from django.shortcuts import render
from .models import LocationDetail

# Create your views here.
def index(request):
    datas = LocationDetail.objects.filter(pk__lt=10)

    print(datas, len(datas))
    context = {
        "datas": datas,
    }
    return render(request, "map/index.html", context)
