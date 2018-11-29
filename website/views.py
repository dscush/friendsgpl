from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.conf import settings
from website.forms import ContactForm, VolunteerForm
from membership.models import Committee
from website.models import CMSBlock, Page

def home(request):
    context = {'content': CMSBlock.objects.get(id='home').content}
    return render(request, 'website/home.html', context)

def about(request):
    committees = Committee.objects.all()
    for committee in committees:
        committee.sorted_role_set = sorted(committee.role_set.all())
    context = {'committees': committees}
    return render(request, 'website/about.html', context)

def contact(request):

    if request.method == 'POST':
        form = ContactForm(data=request.POST)

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
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'contact_form': form,})

def downunder(request):
    context = {'content': CMSBlock.objects.get(id='downunder').content}
    return render(request, 'website/downunder.html', context)

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

def volunteer(request):

    if request.method == 'POST':
        form = VolunteerForm(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            notes = request.POST.get('notes', '')
            volunteer_choices = '\n'.join(request.POST.getlist('volunteer', ['None selected']))

            email = EmailMessage(
                '[Friends of GPL] Volunteer Application',
                'Name: {}\n\nVolunteer opportunities selected:\n{}\n\nNotes:\n{}'.format(name, volunteer_choices, notes),
                '{} <{}>'.format(name, email),
                ['info@friendsgpl.org'],
                headers = {'Reply-To': email }
            )
            email.send()
            messages.add_message(request, messages.SUCCESS, 'Thank you for volunteering!  We will get back to you soon.')
            return redirect('volunteer')
    else:
        form = VolunteerForm()

    return render(request, 'website/volunteer.html', {'volunteer_form': form})

def page(request):
    slug = request.path.strip('/')
    page = Page.objects.get(slug=slug)
    context = {'title': page.title, 'content': page.content}
    return render(request, 'website/page.html', context)
