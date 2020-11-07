from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addPost", views.add_post, name="add_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("send/<int:user_id>", views.send, name="send"),
    path("inbox", views.inbox, name="inbox"),
    path("get_message/<int:message_id>", views.get_message, name="get_message")
]