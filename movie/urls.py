from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("<int:id>/", views.detail, name="detail"),
    
    path("form_create/", views.form_create, name="form_create"),
    path("model_form_create/", views.model_form_create, name="model_form_create"),
    
    path("<int:id>/form_update/", views.form_update, name="form_update"),
    path("<int:id>/model_form_update/", views.model_form_update, name="model_form_update"),
    
]
