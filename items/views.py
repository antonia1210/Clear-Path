from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from django.shortcuts import render, get_object_or_404
from django.views import View
import csv
from churches.models import Church
from django.db import models

class ItemListView(LoginRequiredMixin, View):
    def get(self,request):
        user = self.request.user
        it = Item.objects.filter(church=user.assigned_church)
        cautare = request.GET.get('cautare', '')
        if cautare:
            it=it.filter(models.Q(explicatii__icontains=cautare))
        running_balance = 0
        items = []
        for item in it:
            if item.tip == 'Încasare':
                running_balance += item.pret
            elif item.tip == 'Plată':
                running_balance -= item.pret
            item.current_balance = running_balance
            items.append(item)

        ctx = {'church': user.assigned_church, 'item_list': items}
        return render(request, 'items/item_list.html', ctx)

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['data', 'document', 'denumire', 'adresa', 'explicatii', 'felul', 'tip', 'tip_incasare', 'pret']
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:list")

    def form_valid(self, form):
        form.instance.church = self.request.user.assigned_church
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['data', 'document', 'denumire', 'adresa', 'explicatii', 'felul', 'tip', 'tip_incasare', 'pret']
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:list")
    def get_queryset(self):
        return Item.objects.all(church=self.request.user.assigned_church)

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "items/item_delete.html"
    success_url = reverse_lazy("items:list")
    def get_queryset(self):
        return Item.objects.all(church=self.request.user.assigned_church)

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Executie bugetara.csv"'
    writer = csv.writer(response)
    writer.writerow([
        'Data',
        'Document',
        'Denumire',
        'Adresa',
        'Explicatii',
        'Felul',
        'Tipul platii',
        'Modul platii',
        'Valoare',
        'Sold'
    ])
    user = request.user
    year = request.GET.get('year')
    items=Item.objects.filter(church=user.assigned_church)
    year = int(year) if year else None
    items=items.filter(data__year=year)
    running_balance = 0
    items_list = []
    for item in items:
        if item.tip == 'Încasare':
            running_balance += item.pret
        elif item.tip == 'Plată':
            running_balance -= item.pret
        item.current_balance = running_balance
        items_list.append(item)

    for item in items_list:
        writer.writerow([
            item.data,
            item.document,
            item.denumire,
            item.adresa,
            item.explicatii,
            item.felul,
            item.tip,
            item.tip_incasare,
            item.pret,
            item.current_balance
        ])

    return response

def accountant_export_to_csv(request, church_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Executie bugetara.csv"'
    writer = csv.writer(response)
    writer.writerow([
        'Data',
        'Document',
        'Denumire',
        'Adresa',
        'Explicatii',
        'Felul',
        'Tipul platii',
        'Modul platii',
        'Valoare',
        'Sold'
    ])
    church = get_object_or_404(Church, id=church_id)
    items = Item.objects.filter(church=church)
    year = request.GET.get('year')
    year = int(year) if year else None
    items=items.filter(data__year=year)
    running_balance = 0
    items_list = []
    for item in items:
        if item.tip == 'Încasare':
            running_balance += item.pret
        elif item.tip == 'Plată':
            running_balance -= item.pret
        item.current_balance = running_balance
        items_list.append(item)

    for item in items_list:
        writer.writerow([
            item.data,
            item.document,
            item.denumire,
            item.adresa,
            item.explicatii,
            item.felul,
            item.tip,
            item.tip_incasare,
            item.pret,
            item.current_balance
        ])

    return response
