from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("buy/", views.buy),
    path("delete/<int:number>", views.delete)
    # path("<int:flight_id>", views.flight, name="flight")
]