from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.conf import settings
from website.forms import ContactForm
from membership.models import Committee

def home(request):
    return render(request, 'website/home.html')

def about(request):
    committees = Committee.objects.all()
    for committee in committees:
        committee.sorted_role_set = sorted(committee.role_set.all())
    context = {'committees': committees}
    return render(request, 'website/about.html', context)

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')

            email = EmailMessage(
                '[Friends of GPL] %s' % subject,
                '%s\n\n%s' % (content, contact_name),
                '%s <%s>' % (contact_name, contact_email), # noreply@friendsgpl.org',
                ['info@friendsgpl.org'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.add_message(request, messages.SUCCESS, 'Message Sent!  We will get back to you soon.')
            return redirect('contact')

    return render(request, 'website/contact.html', {'contact_form': form_class,})

def downunder(request):
    return render(request, 'website/downunder.html')

def join(request):
    context = {
        'paypal_email': settings.PAYPAL_EMAIL,
        'paypal_form_url': settings.PAYPAL_FORM_URL,
        'return_uri': request.build_absolute_uri(reverse('payment_return', args=('completed',))),
        'cancel_uri': request.build_absolute_uri(reverse('payment_return', args=('canceled',))),
    }
    return render(request, 'website/join.html', context)

def payment_return(request, payment_status):
    if payment_status == 'completed':
        messages.add_message(request, messages.SUCCESS, 'Thank you for your donation!')
    else:
        messages.add_message(request, messages.INFO, 'Your payment was canceled. Maybe next time.')
    return redirect('join')
