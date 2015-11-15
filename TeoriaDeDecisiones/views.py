from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
	#pdb.set_trace()
	return render_to_response('index.html')