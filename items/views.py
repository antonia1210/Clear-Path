from urllib import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item
from django.shortcuts import render
from django.views import View

class ItemListView(LoginRequiredMixin, View):
    def get(self,request):
        user = self.request.user
        it = Item.objects.filter(church=user.assigned_church)
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
    fields = "__all__"
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:list")

    def form_valid(self, form):
        form.instance.church = self.request.user.assigned_church
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = "__all__"
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