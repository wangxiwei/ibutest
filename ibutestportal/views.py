from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import ApiInfo


class IndexView(generic.ListView):
    template_name = 'ibutestportal/index.html'
    context_object_name = 'apilist'

    def get_queryset(self):
        return ApiInfo.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
    model = ApiInfo
    template_name = 'ibutestportal/detail.html'



    # api_detail = ApiInfo.objects.get(id=api_id)
    # context = {'api_id': api_detail.id,
    #            'api_name': api_detail.request_name,
    #            'api_url': api_detail.request_url,
    #            'api_request': api_detail.request_content,
    #            'api_response': api_detail.response_content}
    # return render(request, 'ibutestportal/detail.html', context)


def save_detail(request, api_id):
    api_detail = get_object_or_404(ApiInfo, id=api_id)
    api_detail.request_name = request.POST['api_name']
    api_detail.request_url = request.POST['api_url']
    api_detail.request_content = request.POST['api_request']
    api_detail.response_content = request.POST['api_response']
    api_detail.save()
    return HttpResponse("保存成功 <a href='/api/'>back</a>")
