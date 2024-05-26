from django.shortcuts import render, redirect
from django.views import View
from forms import OrderItemForm, ReservationForm
from orders.models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
class OrderView(View):
    """Widok zawiera formularz do zamawiania dań z menu."""

    def get(self, request):
        form = OrderItemForm()
        ctx = {
            'form': form
        }
        return render(request, 'place_order.html', ctx)

    def post(self, request):
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order, created = Order.objects.get_or_create(
                customer=request.user,
                date__isnull=True,
                defaults={'total': 0}
            )

            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()

            order.total += order_item.menu_item.price * order_item.quantity
            order.save()

            messages.success(request, 'Dodano pozycję do zamówienia.')
            return redirect('menu.html')
        return render(request, 'place_order.html', {'form': form})


@login_required
class ReservationView(View):
    def get(self, request):
        form = ReservationForm()
        ctx = {
            'form': form
        }
        return render(request, 'reservation.html', ctx)

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
        return render(request, 'reservation.html', {'form': form})

