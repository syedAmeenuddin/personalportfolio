from django.db import models

# Create your models here.


class home(models.Model):
    profilephoto = models.ImageField(upload_to='portfolio/images/', blank=True)
    name = models.CharField(max_length=50, blank=True)
    devtitle = models.CharField(max_length=50, blank=True)
    cvlink = models.URLField(blank=True)
    socialmedia_linkedin = models.URLField(blank=True)
    socialmedia_github = models.URLField(blank=True)
    socialmedia_stackoverflow = models.URLField(blank=True)
    socialmedia_insta = models.URLField(blank=True)


class about(models.Model):
    aboutme = models.TextField(blank=True)
    aboutmeimage = models.ImageField(upload_to='portfolio/images/', blank=True)


class experience(models.Model):
    started_month_year= models.CharField(max_length=30, blank=True)
    ended_month_year_or_present= models.CharField(max_length=30, blank=True)
    companyName = models.CharField(max_length=50, blank=True)
    job_domain = models.CharField(max_length=50, blank=True)
    description_of_job = models.CharField(max_length=100, blank=True)

class service(models.Model):
    title = models.CharField(max_length=50, blank=True)
    brief = models.CharField(max_length=100, blank=True)
    domainlist = models.CharField(max_length=50, blank=True)


class project(models.Model):
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    title = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    describe = models.TextField(blank=True)
    projectsourcecodeurl = models.URLField(blank=True)
    projectliveurl = models.URLField(blank=True)


class contact(models.Model):
    phonenumber = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
