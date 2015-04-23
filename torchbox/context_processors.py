from django.conf import settings

from torchbox.models import FormPage


def fb_app_id(request):
    return {
        'FB_APP_ID': settings.FB_APP_ID,
    }


def contact_form(request):
    form_page = FormPage.objects.get(slug='contact-us')
    if not form_page:
        return

    form_class = form_page.form_builder(form_page.form_fields.all()).get_form_class()
    form_params = form_page.get_form_parameters()
    form = form_class(**form_params)

    if request.method == 'POST':
        if request.POST.get('action', None) == 'contact-us':
            form = form_class(request.POST, **form_params)

            if form.is_valid():
                form_page.process_form_submission(form)

                # If we have a form_processing_backend call its process method
                if hasattr(form_page, 'form_processing_backend'):
                    form_processor = form_page.form_processing_backend()
                    form_processor.process(form_page, form)

    for field in form:
        field.field.widget.attrs['placeholder'] = field.help_text

    return {
        'contact_form': form
    }
