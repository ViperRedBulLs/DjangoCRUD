from django import forms
from crud.models import Bio

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio 
        fields = ["full_name", "email", "address",]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["address"].widget.attrs["class"] = "form-control"