from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def user_login(request,user=None):
    error=''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #pdb.set_trace()
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                	return HttpResponseRedirect('admin')
                return HttpResponseRedirect(reverse('index'))
                #Redirect to a success page.
            else:
	       		error='Cuenta desactivada'
           		return render_to_response('principal/principal.html', {'error': error})
                # Return a 'disabled account' error message
        else:
            error='Usuario y/o clave incorrecta'
            return render_to_response('registration/registrar.html', {'error': error})
            # Return an 'invalid login' error message.
    return render_to_response('principal/principal.html', {'error': error})

@csrf_exempt
def index(request):
	#pdb.set_trace()
	return render_to_response('index.html')