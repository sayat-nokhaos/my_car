from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Car, Order
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'page-register.html', {'form': form})


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_type = self.request.GET.get('car_type', None)
        cars = Car.objects.all()
        if car_type:
            cars = cars.filter(car_type=car_type)
        context['cars'] = cars
        context['new_cars'] = cars.filter(is_new=True).all()
        context['old_cars'] = cars.filter(is_new=False).all()

        return context


class DetailView(DetailView):
    template_name = 'page-car-single-v1.html'
    model = Car
    context_object_name = 'car'


class Detail2View(DetailView):
    template_name = 'page-car-single-v2.html'
    model = Car
    context_object_name = 'car'


class BlogView(TemplateView):
    template_name = 'page-blog-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class OrderCreateView(CreateView):
    template_name = 'page-blog-single.html'
    model = Order
    fields = ('name', 'phone', 'email', 'comment',)
    success_url = reverse_lazy('main:index')
