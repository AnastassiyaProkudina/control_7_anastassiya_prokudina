from django.shortcuts import render, redirect, get_object_or_404

from guest_book.forms import GuestBookForm, SearchForm
from guest_book.models import GuestBook


def record_create(request):
    if request.method == "POST":
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = GuestBookForm()
        form2 = SearchForm()
    return render(
        request,
        "index.html",
        context={"form": form, "form2": form2},
    )


def record_update(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        form = GuestBookForm(request.POST or None, instance=record)
        if form.is_valid():
            record.save()
            return redirect("index")
    else:
        form = GuestBookForm(instance=record)

    return render(
        request, "record_update.html", context={"form": form, "record": record}
    )


def record_delete(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    return render(request, "record_confirm_delete.html", context={"record": record})


def record_confirm_delete(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    record.delete()
    return redirect("index")
