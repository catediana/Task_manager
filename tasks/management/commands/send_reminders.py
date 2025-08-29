from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from tasks.models import Task, UserProfile

class Command(BaseCommand):
    help = 'Sends email reminders for upcoming or overdue tasks.'

    def handle(self, *args, **kwargs):
        today = timezone.localdate()
        # Tasks due today or overdue, and not completed
        tasks_for_reminder = Task.objects.filter(
            due_date__lte=today,
            status__in=['pending', 'in-progress']
        ).exclude(status='complete')

        for task in tasks_for_reminder:
            user = task.user
            user_profile, created = UserProfile.objects.get_or_create(user=user)
            if user.email:
                subject = f"Task Reminder: {task.title}"
                message = (
                    f"Hi {user.username},

"
                    f"This is a reminder for your task: '{task.title}'.
"
                    f"It is currently '{task.status}' and has a '{task.priority}' priority.
"
                )
                if task.due_date:
                    message += f"Its due date is {task.due_date.strftime('%Y-%m-%d')}.
"
                    if task.due_date < today:
                        message += "This task is overdue!
"
                    elif task.due_date == today:
                        message += "This task is due today!
"
                
                message += "
Check your tasks here: http://127.0.0.1:8000

" # Adjust URL as needed
                message += "Best regards,
Your Task Manager"

                send_mail(
                    subject,
                    message,
                    'noreply@taskmanager.com', # From email
                    [user.email],             # To email
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully sent reminder for task "{task.title}" to {user.email}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipped reminder for task "{task.title}": User {user.username} has no email address.'))
