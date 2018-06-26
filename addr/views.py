from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Address

def addr_list(request):
    addrs = Address.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'addr/addr_list.html', {'addrs': addrs})

def addr_detail(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    return render(request, 'addr/addr_detail.html', {'addr': addr})