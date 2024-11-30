import json
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import logging
logging.basicConfig(
    format='%(asctime)s - %(pathname)s[%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def index(request):
    logger.info("------------get request")
    print(request.body)
    post_info = json.loads(request.body)
    print(request.POST)
    aa_param = post_info.get("aa")
    logger.info(f"-----aa is {aa_param}")
    return JsonResponse({"code": "yes", "success": True, "data":"xxx"})

def index2(request):
    logger.info("------------get request")
    print(request.body)
    post_info = json.loads(request.body)
    print(request.POST)
    print(post_info.get("aa"))
    return JsonResponse({"code": "yes", "success": True, "data":"ooo"})
