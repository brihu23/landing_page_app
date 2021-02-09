from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.postgres.fields import ArrayField


class User (AbstractUser):
	pass

class LandingPage(models.Model):
	user = models.ForeignKey("User", on_delete=models.CASCADE, related_name= "profile_user")
	logo = models.ImageField(upload_to = 'images/', blank=True, null=True)
	slug = models.TextField( blank=True, null=True)
	company_name = models.TextField( blank=True, null=True)
	company_tagline = models.TextField( blank=True, null=True)
	hero_image_unsplash = models.TextField(blank=True, null=True)
	hero_image_upload = models.ImageField(upload_to = 'images/', blank=True, null=True)
	phone_number = models.IntegerField( blank=True, null=True)
	

	license_number = models.TextField(blank=True, null=True)
	insured_attribute = models.BooleanField(default=False)
	bonded_attribute = models.BooleanField(default=False)
	emergency_services_attribute = models.BooleanField(default=False)
	veteran_attribute = models.BooleanField(default=False)
	family_owned_attribute = models.BooleanField(default=False)
	local_owned_attribute = models.BooleanField(default=False)
	years_in_business_attribute = models.IntegerField(blank=True, null=True)

	about_us = models.TextField(blank=True, null=True)
	about_us_image = models.ImageField( blank=True, null=True)
	twitter_link = models.URLField(max_length=200, blank=True, null=True )
	instagram_link = models.URLField(max_length=200, blank=True, null=True )
	facebook_link = models.URLField(max_length=200, blank=True, null=True )

	testimonial_hero = models.ImageField(upload_to = 'images/', blank=True, null=True)
	featured_video = models.URLField(max_length=200, blank=True, null=True)

	address = models.TextField( blank=True, null=True)	
	# business_hours = ArrayField(models.TextField(blank=True, null=True), size=7)




class Service(models.Model):
	landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE)
	# services_tagline = models.TextField()
	services_title = models.TextField() 
	services_description = models.TextField()
	# services_icon = models.TextField()

class Testimonial(models.Model):
	landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE)
	testimonial_giver_name = models.TextField() 
	testimonial_giver_title = models.TextField(blank=True, null=True) 
	testimonial_giver_rating = models.TextField()
	testimonial_description = models.TextField(blank=True, null=True)
	# testimonial_source = models.ImageField(upload_to = 'images/')
	# testimonial_date = models.DateField(blank=True, null=True)

class Faq(models.Model):
	landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE)
	question = models.TextField(blank=False)
	answer = models.TextField(blank=False)


class GalleryPhoto(models.Model):
	landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE)
	gallery_photo = models.ImageField(upload_to = 'images/')

class TestimonialPhoto(models.Model):
	landing_page = models.ForeignKey(LandingPage, on_delete=models.CASCADE)
	testimonial_photo = models.ImageField(upload_to = 'images/')
















	

	
