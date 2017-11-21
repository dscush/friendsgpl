from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Message:"

class VolunteerForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    OPTIONS = ((option, option) for option in (
        "Program Planning",
        "Fundraising",
        "Library Expansion/Renovation",
        "Publicity",
        "Spring Egg Hunt",
        "Staff Appreciation (baking etc)",
        "Down Under Bookstore",
        "Serve on Board of Directors",
        "Library Garden",
        "Childcare",
    ))

    volunteer = forms.MultipleChoiceField(
        choices=OPTIONS,
        widget=forms.SelectMultiple(attrs={'class':'selectpicker'}),
        label='Volunteer Opportunities (select one or more):',
    )

    notes = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(VolunteerForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name:"
        self.fields['email'].label = "Email:"
        self.fields['notes'].label = "Notes:"
