from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.cache import cache

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from TeoriaDeDecisiones.models import Lista


listaAlter = []
listaConse = []

@csrf_exempt
def nuevo_usuario(request):
    if request.method == 'POST':
        try:
            firstname = request.POST['name_reg']
            lastname = request.POST['apellido_reg']
            name = request.POST['username_reg']
            contra = request.POST['password_reg']
            mail = request.POST['email_reg']
            user = User.objects.create_user(username=name, password=contra)
            user.email = mail
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            return render_to_response('index.html', {'user': user})
        except Exception as e:
            error = 'El usuario ya se encuentra registrado...'
            return render_to_response('registrar.html', {'error': error})


@csrf_exempt
def redirect_registro(request):
    return render_to_response('registrar.html', context_instance=RequestContext(request))


@csrf_exempt
def user_login(request, user=None):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # pdb.set_trace()
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    return HttpResponseRedirect('admin')
                return HttpResponseRedirect(reverse('principal'))
                # Redirect to a success page.
            else:
                error = 'Cuenta desactivada'
                return render_to_response('index.html', {'error': error})
                # Return a 'disabled account' error message
        else:
            error = 'Usuario y/o clave incorrecta'
            return render_to_response('registrar.html', {'error': error})
            # Return an 'invalid login' error message.
    return render_to_response('index.html', {'error': error})


@csrf_exempt
def index(request):
    # pdb.set_trace()
    return render_to_response('index.html', {'user': request.user})


@csrf_exempt
def user_logout(request):
    logout(request)
    return render_to_response('index.html')


@csrf_exempt
def redirect_principal(request):
    return render_to_response('principal.html', context_instance=RequestContext(request))


@csrf_exempt
def ingresar_datos(request):
    if request.method == "POST":
        if request.POST["txt_alternativa"] != "":
            listaAlter.append(request.POST['txt_alternativa'])
            i = 1
        else:
            listaConse.append(request.POST['txt_consecuencia'])

    return render_to_response('principal.html', {'user': request.user, 'alt': listaAlter, 'con': listaConse})




@csrf_exempt
def calcula_datos(request):
    a = "hola"
