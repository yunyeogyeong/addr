from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Address

from .forms import AddressForm

def addr_list(request):
    addrs = Address.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'addr/addr_list.html', {'addrs': addrs})

def addr_detail(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    return render(request, 'addr/addr_detail.html', {'addr': addr})

def addr_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            addr = form.save(commit=False)
            addr.author = request.user
            addr.created_date = timezone.now()
            addr.save()
            return redirect('addr_detail', pk=addr.pk)
    else:
        form = AddressForm()
    return render(request, 'addr/addr_edit.html', {'form': form})

def addr_edit(request, pk):
    addr = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST, instance=addr)
        if form.is_valid():
            addr = form.save(commit=False)
            addr.author = request.user
            addr.created_date = timezone.now()
            addr.save()
            return redirect('addr_detail', pk=addr.pk)
    else:
        form = AddressForm(instance=addr)
    return render(request, 'addr/addr_edit.html', {'form': form})