from django.urls import path

from guest_book.views.base import records_list
from guest_book.views.records import *

urlpatterns = [
    path("", records_list, name="index"),
    path("records", records_list, name="index"),
    path("record/create", record_create, name="record_create"),
    path("record/<int:pk>/update/", record_update, name="record_update"),
    path("record/<int:pk>/delete/", record_delete, name="record_delete"),
    path(
        "record/<int:pk>/confirm_delete/",
        record_confirm_delete,
        name="record_confirm_delete",
    ),
    path("record/search", record_search, name="record_search"),
]
