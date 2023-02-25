from django.shortcuts import render, redirect, get_object_or_404
from guest_book.forms import GuestBookForm, SearchForm
from guest_book.models import GuestBook, StatusChoice


def record_create(request):
    if request.method == "POST":
        form = GuestBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = GuestBookForm()
    return render(
        request,
        "record_create.html",
        context={"form": form},
    )


def record_update(request, pk):
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == "POST":
        form = GuestBookForm(request.POST or None, instance=record)
        if form.is_valid():
            record.save()
            return redirect("record_detail", pk=record.pk)
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


def record_search(request):
    records = GuestBook.objects.all().filter(
        is_deleted=False, status=StatusChoice.ACTIVE
    )
    for record in records:
        if request.method == "POST":
            search_name = SearchForm(request.POST or None, instance=record.name)
            records = GuestBook.objects.all().filter(
                is_deleted=False, status=StatusChoice.ACTIVE, name=search_name
            )
        return redirect("index", context={"records": records})
