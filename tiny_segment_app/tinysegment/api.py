import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from .models import CodeComponent

@api_view(['POST'])
def fetch_code_component(request):
    print(request.data)
    ## TODO: process the anon id received, but for now just using mock data.
    code_component = CodeComponent.objects.filter(source_div_id=request.data.get('element_id'), source_event=request.data.get('source_event')).first()
    print(code_component.id)
    if code_component:
        response_data = {'status': 'success',
                        'html_content': code_component.html_code}
    return JsonResponse(response_data)
