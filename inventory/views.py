from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier, Product, Order
from .serializers import SupplierSerializer, ProductSerializer, OrderSerializer
from .forms import SupplierForm

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def home(request):
    return render(request, 'inventory/home.html')

def products(request):
    return render(request, 'inventory/products.html')

def suppliers(request):
    supplier_list = Supplier.objects.all()
    context = {'suppliers': supplier_list}
    return render(request, 'inventory/suppliers/suppliers.html', context)

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'inventory/suppliers/supplier_detail.html', {'supplier': supplier})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            return redirect('supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/suppliers/supplier_edit.html', {'form': form, 'supplier': supplier})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        supplier.delete()
        return redirect('suppliers')
    return render(request, 'inventory/suppliers/supplier_delete.html', {'supplier': supplier})

def orders(request):
    return render(request, 'inventory/orders.html')
