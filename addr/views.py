from django.shortcuts import render
from django.utils import timezone
from .models import Address

def addr_list(request):
    addrs = Address.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'addr/addr_list.html', {'addrs': addrs})