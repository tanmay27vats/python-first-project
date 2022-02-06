from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import get_template
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    context = {
        'page_heading': 'Contact page header',
        'page_content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = "New contact "+form.cleaned_data["email"]+": "+form.cleaned_data["full_name"]
            email_message = form.cleaned_data['message']

            # send_mail('subject', 'message body', 'from email', 'recipients list')

            # First way to send mail in Django
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

            # Second way to template based send mail in Django
            template = get_template('Mails/contact_template.txt')
            mail_context = {
                'full_name': form.cleaned_data["full_name"],
                'email': form.cleaned_data["email"],
                'message': form.cleaned_data['message'],
            }
            mail_content = template.render(mail_context)
            mail = EmailMessage(
                email_subject,
                mail_content,
                settings.CONTACT_EMAIL,
                settings.ADMIN_EMAILS,
                reply_to=[form.cleaned_data["email"]]
            )
            mail.send()

            form = ContactForm()
            context['form'] = form
            context['success'] = True
            return render(request, 'contact/contact.html', context)
    form = ContactForm()
    context['form'] = form
    return render(request, 'contact/contact.html', context)