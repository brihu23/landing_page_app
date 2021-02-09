from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(LandingPage)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Faq)
admin.site.register(GalleryPhoto)
admin.site.register(TestimonialPhoto)