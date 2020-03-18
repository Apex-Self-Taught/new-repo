from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import StoreHooksData

@csrf_exempt
def index(request):
    print(request.POST)
    hook_data = request.POST
    StoreHooksData(username=hook_data["sender"]["login"],
                   user_id=hook_data["sender"]["id"],
                   avatar_url=hook_data["sender"]["avatar_url"])
    return HttpResponse("Hello webhooks here")