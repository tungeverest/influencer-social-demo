from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import redirect
# Create your views here.
class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') #needs defined as valid url
        data = [1,2,3,4,5,6,7]
        dj_label = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange", "Black"]
        return render(request, 'dashboard.html', {"data": data, "dj_label": dj_label,})