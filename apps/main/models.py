from django.db import models
from django.contrib.auth import get_user_model
from apps.commons.models import DateTimeModel

# Create your models here.

User = get_user_model()

class Category(DateTimeModel):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Job(DateTimeModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_jobs")
    apply_before = models.DateTimeField()
    experience_required = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.title

APPLIED = 'Applied'
SCREENING = 'Screening'
DECLINED = 'Declined'
CALL_FOR_INTERVIEW = 'Call For Interview'
REJECTED = 'Rejected'
SELECTED = 'Selected'
APPLICATION_STATUS = (
    (APPLIED, APPLIED),
    (SCREENING, SCREENING),
    (DECLINED, DECLINED),
    (CALL_FOR_INTERVIEW, CALL_FOR_INTERVIEW),
    (REJECTED, REJECTED),
    (SELECTED, SELECTED)
)

class JobApplication(DateTimeModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_applications")
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS)
    interview_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

# class Contact(models.Model):
#     # Define your fields here
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
