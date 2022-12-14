from .models import MyUser
from django.forms import ModelForm
from django import forms
from django.forms import widgets
from crispy_forms.helper import FormHelper


#Form to get participant information
# class MyUserForm(ModelForm):
# 	class Meta:
# 		model = MyUser
# 		fields = ['name_1', 'email_1', 'phone_number_1', 'name_2', 'email_2', 'phone_number_2', 'team_name']


#Form to create quiz
class testform(forms.Form):

	def __init__(self, *args, **kwargs):
		questions = kwargs.pop('questions')	#pop questions array from kwargs
		super().__init__(*args, **kwargs)
		if questions:
			for question in questions:	#add a form field for each question
				CHOICES = (
					('A', question.option_a),
					('B', question.option_b), 
					('C', question.option_c),
					('D', question.option_d),
				)
				self.fields[str(question.question.id)] = forms.ChoiceField(required=False, choices=CHOICES, widget=widgets.RadioSelect)			
		self.helper = FormHelper()
		self.helper.form_show_labels = False

	def answers(self):	#return questions and answers for result processing
		for name, question in self.cleaned_data.items():
			yield(name, question)