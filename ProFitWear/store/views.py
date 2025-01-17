from django.shortcuts import render , get_object_or_404, redirect
from .models import Product, Customer,Category, Order
from .forms import forms, OrderForm


# عرض الصفحة الرئيسية للمتجر مع قائمة المنتجات
def store(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'store/store.html', {'products': products})


def front(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'store/index.html', {'products': products})


# عرض قائمة العملاء
def customer_list(request):
    customers = Customer.objects.all()  # Retrieve all customers from the database
    return render(request, 'store/customer_list.html', {'customers': customers})

# عرض تفاصيل العميل بناءً على المعرف
def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)  # Get customer by ID
    return render(request, 'store/customer_detail.html', {'customer': customer})






# عرض أو إنشاء/تعديل فئة
def category_view(request):
    section = request.GET.get('section', 'list')  # تحديد القسم
    category_id = request.GET.get('id')  # جلب المعرف في حال كانت التفاصيل أو التعديل

    if section == 'list':
        categories = Category.objects.all()
        return render(request, 'store/category.html', {'section': section, 'categories': categories})

    elif section == 'create':
        form = forms(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('?section=list')
        return render(request, 'store/category.html', {'section': section, 'form': form})

    elif section == 'edit':
        category = get_object_or_404(Category, id=category_id)
        form = forms(request.POST or None, instance=category)
        if form.is_valid():
            form.save()
            return redirect('?section=list')
        return render(request, 'store/category.html', {'section': section, 'form': form, 'category': category})

    elif section == 'detail':
        category = get_object_or_404(Category, id=category_id)
        return render(request, 'store/category.html', {'section': section, 'category': category})

    return redirect('?section=list')

# عرض أو إنشاء/تعديل طلب
def order_view(request):
    section = request.GET.get('section', 'list')
    order_id = request.GET.get('id')

    if section == 'list':
        orders = Order.objects.all()
        return render(request, 'store/order.html', {'section': section, 'orders': orders})

    elif section == 'create':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('?section=list')
        return render(request, 'store/order.html', {'section': section, 'form': form})

    elif section == 'edit':
        order = get_object_or_404(Order, id=order_id)
        form = OrderForm(request.POST or None, instance=order)
        if form.is_valid():
            form.save()
            return redirect('?section=list')
        return render(request, 'store/order.html', {'section': section, 'form': form, 'order': order})

    elif section == 'detail':
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'store/order.html', {'section': section, 'order': order})

    return redirect('?section=list')
