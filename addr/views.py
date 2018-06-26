from django.shortcuts import render

def addr_list(request):
    return render(request, 'addr/addr_list.html', {})