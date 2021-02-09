import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation 
from django.urls import reverse
from django.http import JsonResponse
from datetime import datetime
from .models import *
import base64
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt


def index(request):

   if request.user.is_authenticated:
        return render(request, "landing_page_gen/index.html")
   else:
        return HttpResponseRedirect(reverse("login"))


    # return HttpResponseRedirect(reverse("all_post", args=(1, 0, 0)))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "landing_page_gen/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "landing_page_gen/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "landing_page_gen/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password,first_name=first_name, last_name=last_name)            
            user.save()
        except IntegrityError:
            return render(request, "landing_page_gen/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "landing_page_gen/register.html")

@csrf_exempt
def create_landing_page(request):    

    if request.method == "POST":
        data = json.loads(request.body)  
        hero_image = ""
        about_us_image = ""
        logo = ""
        if (data["cover_upload"] != ""):
            hero_image = base64_file(data["cover_upload"])  
        if (data["about_upload"] != ""):
            about_us_image = base64_file(data["about_upload"])   
        if (data["logo"] != ""):
            logo = base64_file(data["logo"]) 
        
             
        
        
        landing_page = LandingPage.objects.create(
            user=request.user,
            company_name=data["company_name"],
            company_tagline=data["company_tagline"],
            phone_number=data["phone"],
            slug=data["slug"],
            logo = logo,
            hero_image_unsplash=data["cover_unsplash"],
            hero_image_upload=hero_image,
            license_number=data["license"],
            insured_attribute=data["insured"],
            bonded_attribute=data["bonded"],
            emergency_services_attribute=data["emergency"],
            veteran_attribute=data["veteran"],
            family_owned_attribute=data["family"],
            local_owned_attribute=data["local"],
            about_us=data["about"],
            about_us_image= about_us_image,
            twitter_link=data["twitter"],
            instagram_link=data["instagram"],
            facebook_link=data["facebook"],
            featured_video=data["feature"],
            address=data["address"],         
        )

        landing_page.save()

        for i in data["services"]:
            service = Service.objects.create(
                landing_page=landing_page,
                services_title=i["service-name"],
                services_description=i["service-description"]
            )
            service.save()
        for j in data["testimonials"]:
            testimonial = Testimonial.objects.create(
                landing_page=landing_page,
                testimonial_giver_name=j["reviewer"],
                testimonial_giver_title=j["title"],
                testimonial_giver_rating=j["stars"],
                testimonial_description=j["review"],

            )
            testimonial.save()
        for k in data["faqs"]:
            faq = Faq.objects.create(
                landing_page=landing_page,
                question= k["question"],
                answer= k["answer"],
            )
            faq.save()
        for l in data["gallery"]:
            gallery_photo = GalleryPhoto.objects.create(
                landing_page=landing_page,
                gallery_photo= base64_file(l)
            )
            gallery_photo.save()
            
        return JsonResponse({"message": "Landing Page Created."}, status=201)

def render_landing_page(request, slug):
    try:
        landing_page = LandingPage.objects.get(slug=slug)
    except LandingPage.DoesNotExist:
        return render(request, "landing_page_gen/index.html", {"message": "page does not exist"} )
    
    if landing_page.hero_image_unsplash is None:
        hero_image = landing_page.hero_image_upload.url
    else:
        hero_image = landing_page.hero_image_unsplash

    services = Service.objects.filter(landing_page=landing_page)
    testimonials = Testimonial.objects.filter(landing_page=landing_page)
    faqs = Faq.objects.filter(landing_page=landing_page)
    gallery = GalleryPhoto.objects.filter(landing_page=landing_page)
    # for i in range (len(gallery)):
    #     gallery[i] = gallery[i].testimonial_photo.url
    

    

    context = {
        "company_name" : landing_page.company_name,
        "company_tagline" : landing_page.company_tagline,
        "hero_image": hero_image,
        "logo":landing_page.logo.url,
        "phone_number": landing_page.phone_number,
        "license_number": landing_page.license_number,
        "insured": landing_page.insured_attribute,
        "bonded":landing_page.bonded_attribute,
        "emergency": landing_page.emergency_services_attribute,
        "veteran": landing_page.veteran_attribute,        
        "family_owned": landing_page.family_owned_attribute,
        "local_owned": landing_page.local_owned_attribute,
        "about_us": landing_page.about_us,
        "about_us_image": landing_page.about_us_image.url,
        "twitter": landing_page.twitter_link,
        "instagram": landing_page.instagram_link,
        "facebook": landing_page.facebook_link,
        "featured": landing_page.featured_video,
        "address": landing_page.address,
        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
        "gallery": gallery
    }
    

    return render(request, "landing_page_gen/render.html", context)





def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))