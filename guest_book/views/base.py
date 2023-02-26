from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guest_book.forms import SearchForm, GuestBookForm
from guest_book.models import GuestBook, StatusChoice


def records_list(request: WSGIRequest):
    records = (
        GuestBook.objects.all()
        .filter(is_deleted=False, status=StatusChoice.ACTIVE)
        .order_by("-created_at")
    )
    form = GuestBookForm()
    form2 = SearchForm()
    context = {"form": form, "records": records, "form2": form2}
    return render(request, "index.html", context=context)
