from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    user = forms.CharField(max_length=20, label='')

    class Meta:
        model = Employee
        exclude = ('user',)
        # fields = '__all__'
        labels = {
            'address_1': '',
            'address_2': '',
            'city': '',
            'state': '',
            'zip': '',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        instance = None

        try:
            instance = kwargs.pop('instance')
        except KeyError:
            pass

        if instance:
            self.fields['user'].widget.attrs['readonly'] = True

        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update(
                {
                    'class': 'form-control',
                    'placeholder': field_name.capitalize(),
                    'autocomplete': 'none',
                }
            )
