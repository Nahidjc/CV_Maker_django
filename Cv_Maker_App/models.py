from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid
# Create your models here.


class PracticeModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fullname = models.CharField(
        max_length=200, verbose_name='own name', blank=False)
    picture = models.FileField(
        verbose_name='Upload CV Picture', upload_to='pictures', blank=False)

    def __str__(self):
        return self.fullname


class CvMaker(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_user')
    fullname = models.CharField(
        max_length=200, verbose_name='own name', blank=False)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=12)
    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('SheMale', 'SheMale'),
    )
    birth_date = models.DateField(blank=False)
    zender = models.CharField(max_length=7, choices=sex)
    cv_picture = models.ImageField(
        verbose_name='Upload CV Picture', upload_to='picture', blank=False)
    website = models.URLField(blank=True)
    present_address = models.CharField(max_length=250, blank=False)
    about = models.TextField(blank=False)
    school_start_date = models.DateField(blank=False)
    school_start_end = models.DateField(blank=False)
    subject = (
        ('Science', 'Science'),
        ('Business', 'Business'),
        ('Humanities', 'Humanities')
    )
    ssc_subject = models.CharField(max_length=20, choices=subject, blank=False)
    school_name = models.CharField(max_length=250, blank=False)
    hsc_start_date = models.DateField(blank=False)
    hsc_start_end = models.DateField(blank=False)
    hsc_subject = models.CharField(max_length=20, choices=subject, blank=False)
    college_name = models.CharField(max_length=250, blank=False)

    first_job = models.CharField(max_length=250, blank=True)
    first_job_title = models.CharField(max_length=250, blank=True)
    first_job_date = models.CharField(max_length=10, blank=True, null=True)
    present_job = models.CharField(max_length=250, blank=True)
    present_job_title = models.CharField(max_length=250, blank=True)
    present_job_date = models.DateField(blank=True, null=True)

    skils_title_1 = models.CharField(max_length=20, blank=True)
    skills_percentage_1 = models.IntegerField(blank=True)
    skils_title_2 = models.CharField(max_length=20, blank=True)
    skills_percentage_2 = models.IntegerField(blank=True)
    skils_title_3 = models.CharField(max_length=20, blank=True)
    skills_percentage_3 = models.IntegerField(blank=True)
    skils_title_4 = models.CharField(max_length=20, blank=True)
    skills_percentage_4 = models.IntegerField(blank=True)
    skils_title_5 = models.CharField(max_length=20, blank=True)
    skills_percentage_5 = models.IntegerField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ['-publish_date']

    def save(self):
        self.slug = slugify(self.email + '-' + str(uuid.uuid4()))
        super(CvMaker, self).save()

    def __str__(self):
        return self.fullname
