from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .form import ContactForm
# Create your views here.
from django.contrib import messages
from django.conf import settings

from sjhc_web.utils import send_html_mail

def formulario_contacto(request):
	#post = get_object_or_404(ContactForm)
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			post = form.save(commit=True)
			post.save()
			subject=post.asunto
			nombre=post.nombre
			telefono=post.telefono
			email=post.email
			mensaje=post.mensaje
			message="Estimadas Patricia y Paulina:\n "+nombre+"\n Email: "+email+"\n fono: "+str(telefono)+"\nHa escrito mediante el formulario" \
																				   "de contacto con el siguiente mensaje:\n" \
																				   "\n"+mensaje
			send_html_mail(subject,
						   message,
						   ['dahalpi@gmail.com','ninostrozac@gmail.com'],
						   settings.EMAIL_HOST_USER)
			send_html_mail("Muchas gracias por contactar con SJHC!",
                      "A la brevedad responderemos a sus solicitudes, sus datos registrados son:\n"+nombre+", f:"+str(telefono)+", email: "+ email,
                      [email],
                      settings.EMAIL_HOST_USER)

			messages.success(request, 'Formulario de contacto enviado. ¡Muchas gracias!')
			#return redirect('formulario_enviado')#cambiar a pagina de enviado
	else:
		form = ContactForm()
	return render(request, 'contacto.html', {'form': form})
