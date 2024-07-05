from django.shortcuts import render, redirect
from .forms import ApplicantForm

def applicants_form(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ApplicantForm()
    context = {
        'form': form,
    }
    return render(request, 'applicants/applicants_form.html', context)

def home(request):
    return render(request, 'home.html')