from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

def validate_allowed_domains(value):
    allowed_domains = ['myems.com', 'myems.biz']
    if '@' in value:
        user_part, domain_part = value.rsplit('@', 1)
        if domain_part not in allowed_domains:
            raise ValidationError("Invalid employee email address, incorrect domain specified")

class Feedback(models.Model):
    CATEGORY_CHOICES = (
        ('1', 'General'),
        ('2', 'Management'),
        ('3', 'Compensation'),
        ('4', 'Suggestion'),
        ('5', 'Complaint')
    )
    name = models.CharField(max_length=100)
    emp_no = models.IntegerField()
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='1')
    email = models.CharField(max_length=150,
            validators=[EmailValidator(), MinLengthValidator(7, message='Too short'),
                        MaxLengthValidator(100), validate_allowed_domains])
    comment = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now(), null=False)

    def __str__(self):
        return 'Feedback for ' + self.name

    class Meta:
        db_table = 'feedback'