from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Messages(models.Model):
    to_user = models.CharField(max_length=200, verbose_name='to User')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200, verbose_name='Subject')
    message = models.TextField(max_length=1000, default="", verbose_name='Message')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.subject
    class Meta():
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-date',]

    def get_date(self):
        time = timezone.now()
        if self.date.day == time.day:
            if self.date.hour + 1 == time.hour or self.date.hour == time.hour:
                return str(abs(time.minute - self.date.minute)) + " minutes ago"
            return str(time.hour - self.date.hour) + " hours ago"
        else:
            if self.date.month == time.month:
                return str(time.day - self.date.day) + " days ago"
            else:
                if self.date.year == time.year:
                    return str(time.month - self.date.month) + " months ago"
        return self.date


