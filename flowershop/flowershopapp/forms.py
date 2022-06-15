from django import forms

from flowershopapp.models import Branches, Subbranches


class Customerform(forms.ModelForm):
    class Meta:
        model = Branches
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subname'].queryset = Subbranches.objects.none()

        if 'bname' in self.data:
            try:
                country_id = int(self.data.get('bname'))
                self.fields['subname'].queryset = Subbranches.objects.filter(branch_id=country_id).order_by('subname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subname'].queryset = self.instance.branch.subname_set.order_by('subname')