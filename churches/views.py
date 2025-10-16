from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from .models import Church
from items.models import Item

class ChurchesListView(LoginRequiredMixin, View):
    def get(self,request):
        churches = Church.objects.all()
        return render(request, 'churches/church_list.html', {'churches': churches})

class ChurchesItemListView(LoginRequiredMixin, View):
    def get(self,request,church_id):
        church = get_object_or_404(Church, id=church_id)
        items = Item.objects.filter(church=church)
        running_balance = 0
        for item in items:
            if item.tip == 'Încasare':
                running_balance += item.pret
            elif item.tip == 'Plată':
                running_balance -= item.pret
            item.current_balance = running_balance
        context = {
            'church': church,
            'item_list': items,
        }
        return render(request, 'items/item_list_only.html', context)
