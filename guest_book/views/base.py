from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from guest_book.forms import SearchForm
from guest_book.models import GuestBook, StatusChoice


def records_list(request: WSGIRequest):
    records = GuestBook.objects.all().filter(
        is_deleted=False, status=StatusChoice.ACTIVE
    )
    form = SearchForm()
    context = {"form": form, "records": records}
    return render(request, "index.html", context=context)
