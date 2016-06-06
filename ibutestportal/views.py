from django.shortcuts import render
from .models import ApiInfo


def index(request):
    apilist = ApiInfo.objects.order_by('id')[:5]
    context = {'apilist':apilist}
    return render(request,'ibutestportal/index.html',context)


