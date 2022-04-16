from django import forms
from .models import Apply_course

class ApplyForm(forms.ModelForm):
	class Meta:
		model = Apply_course
		fields = ['father_name', 'birth_date', 'select_gender', 'select_domicile', 
					'mobile_no', 'cnic', 'guardian_no', 'select_qualification', 'select_img', 'select_course', 
						'matric_dmc', 'fsc_dmc', 'cnic_front', 'cnic_back', 'Address']

