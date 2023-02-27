from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from guest_book.forms import SearchForm, GuestBookForm
from guest_book.models import GuestBook, StatusChoice


def records_list(request: WSGIRequest):
    form = GuestBookForm()
    form2 = SearchForm()
    name = request.GET.get("name")
    if name:
        records = (
            GuestBook.objects.all()
            .filter(is_deleted=False, status=StatusChoice.ACTIVE, name=name)
            .order_by("-created_at")
        )
    else:
        records = (
            GuestBook.objects.all()
            .filter(is_deleted=False, status=StatusChoice.ACTIVE)
            .order_by("-created_at")
        )
    context = {"form": form, "records": records, "form2": form2}
    return render(request, "index.html", context=context)
