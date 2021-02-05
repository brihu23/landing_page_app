from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_landing_page, name="create"),
    path("<str:slug>", views.render_landing_page, name="render")


    # path("new_post", views.new_post, name="new_post"),
    # path("all_post/<int:page_num>/<int:types>/<int:profid>", views.all_post, name = "all_post"),
    # path("like/<int:post_id>", views.like, name= "like"),
    # path("follow",views.follow, name = "follow"),
    # path("post", views.post, name = "post"),

]
