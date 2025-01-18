
from django.shortcuts import render


def home(request):
    return render(request, 'public/home.html')


# ----- ADMIN FUNCTION ------
def homeAdmin(request):
    return render(request, 'admin/home.html')