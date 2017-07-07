from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Tablet, Seal


class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'search'))


class SealForm(forms.ModelForm):
    class Meta:
        model = Seal
        fields = "__all__"
        widgets = {
            'owner': autocomplete.ModelSelect2(
                url='../../../vocabs-ac/skos-constraint-ac/?scheme=owner'),
            'seal_type': autocomplete.ModelSelect2(
                url='../../../vocabs-ac/skos-constraint-ac/?scheme=seal_type'),
            'seal_motive': autocomplete.ModelSelect2(
                url='../../../vocabs-ac/skos-constraint-ac/?scheme=seal_motive'),
            'seal_position': autocomplete.ModelSelect2(
                url='../../../vocabs-ac/skos-constraint-ac/?scheme=seal_position'),
        }

    def __init__(self, *args, **kwargs):
        super(SealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TabletForm(forms.ModelForm):
    class Meta:
        model = Tablet
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TabletForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)
