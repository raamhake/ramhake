 # eventapp/management/commands/send_event_emails.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from eventapp.models import Event, EmailTemplate, Employee, EmailLog

class Command(BaseCommand):
    help = 'Send automated event emails'

    def handle(self, *args, **options):
        current_date = timezone.now().date()

        events = Event.objects.filter(event_date=current_date)

        if not events:
            self.stdout.write(self.style.SUCCESS('No events scheduled for today.'))
            return

        for event in events:
            employee = event.employee
            template = EmailTemplate.objects.get(event_type=event.event_type)
            email_content = template.content.replace('{{ employee_name }}', employee.name)

            try:
                send_mail(
                    template.subject,
                    email_content,
                    'ram@email.com',
                    [employee.email],
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f'Email sent to {employee.name}'))
                # Log email success here
                EmailLog.objects.create(event=event, employee=employee, success=True)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error sending email to {employee.name}: {str(e)}'))
                # Log email error here
                EmailLog.objects.create(event=event, employee=employee, success=False, error_message=str(e))
