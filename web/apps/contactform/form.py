from django.forms import ModelForm
from .models import Contact
from django.forms.widgets import CheckboxSelectMultiple
from django.core.validators import MinLengthValidator, MaxLengthValidator,MinValueValidator,MaxValueValidator
from captcha.fields import ReCaptchaField

class ContactForm(ModelForm):
	captcha = ReCaptchaField()
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields["nombre"].min_length = 3
		self.fields["nombre"].validators.append(MinLengthValidator)

		self.fields["telefono"].validators.append(MinValueValidator(100))

		self.fields["telefono"].validators.append(MaxValueValidator(999999999))

		self.fields["asunto"].min_length = 20
		self.fields["asunto"].validators.append(MinValueValidator)

		self.fields["mensaje"].min_length = 200
		self.fields["mensaje"].validators.append(MinValueValidator)

		self.fields["mensaje"].max_length = 1200
		self.fields["mensaje"].validators.append(MaxValueValidator)


	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
				
	class Meta:
		model = Contact
		fields = [
			'nombre',
			'telefono',
			'email',
			'asunto',
			'mensaje',
			]
