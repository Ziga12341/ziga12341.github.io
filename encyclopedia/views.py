from django.shortcuts import render
import markdown2
from encyclopedia.util import list_entries, get_entry, save_entry
from django import forms

src = ["1", "2", "3"]


class SearchEntryForm(forms.Form):
    entry = forms.CharField(label="Entry Search")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries(),
        "src": src,
        "form": SearchEntryForm(),

    })


def show_entry(request, title):
    if title.capitalize() in list_entries() or\
            title.upper() in list_entries() or\
            title.lower() in list_entries():
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(get_entry(title)),
            "page_title": title.capitalize(),
            "src": src,
        })
    return render(request, "encyclopedia/entry.html", {
        "entry": f"Error: requested page {title.capitalize()} was not found",
        "page_title": title.capitalize(),
    })
