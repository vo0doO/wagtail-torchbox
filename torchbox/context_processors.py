from django.conf import settings

from torchbox.models import FormPage


def fb_app_id(request):
    return {
        'FB_APP_ID': settings.FB_APP_ID,
    }


def contact_form(request):
    form_page = FormPage.objects.filter(slug='contact-us').first()
    if not form_page:
        return {}

    form_class = form_page.form_builder(form_page.form_fields.all()).get_form_class()
    form_params = form_page.get_form_parameters()
    form = form_class(**form_params)

    for field in form:
        field.field.widget.attrs['placeholder'] = field.help_text

    return {
        'contact_form': form
    }
