from django.shortcuts import render , redirect

from apps.usuario.froms import UsuarioForm

# Create your views here.

def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect ('usuario:usuario_view')
            else:
                form = MascotaForm()

            return render(request,'usuario/UsuarioForm.html',{'form':form})