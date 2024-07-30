from django.urls import path

from .views import names_list
# from .views import import_data,change_data

urlpatterns = [
    # path("import", import_data, name='import_data' ),
    # path("change_data", change_data, name='change_data' ),
    path("list", names_list, name='names_list' ),
    # path("form", name_form, name='name_form' ),
] 
