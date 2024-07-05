from django.shortcuts import render, redirect
from .forms import ProviderForm

def providers_form(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProviderForm()
    context = {
        'form': form,
    }
    return render(request, 'providers/providers_form.html', context)