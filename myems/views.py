from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm

def index(request):
    return render(request, 'index.html', {})

def my_profile(request, pk):
    profile = get_object_or_404(Employee, pk=pk)
    if request.method.upper() == 'POST':
        form = EmployeeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile', pk=pk)

    form = EmployeeForm(instance=profile)
    return render(request, 'profile.html', {'form':form})
