from .models import GPU  # додай на початку
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, GPUBrand, GPU, OrderItem
from .forms import OrderForm


def index(request):
    brands = GPUBrand.objects.all()
    return render(request, 'store/index.html', {'brands': brands})


def view1(request):
    return render(request, 'store/view1.html')


def view2(request):
    return render(request, 'store/view2.html')


def view3(request):
    return render(request, 'store/view3.html')


def view4(request):
    return render(request, 'store/view4.html')


def view5(request):
    return render(request, 'store/view5.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'store/product_detail.html', {'product': product})


def category_detail(request, category_id):
    category = get_object_or_404(GPUBrand, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_detail.html', {'category': category, 'products': products})


def gpu_detail(request, gpu_id):
    gpu = get_object_or_404(Product, id=gpu_id)  # або GPU
    return render(request, 'store/gpu_detail.html', {'gpu': gpu})


def brand_detail(request, brand_id):
    print(f"Викликано brand_detail з ID: {brand_id}")
    brand = get_object_or_404(GPUBrand, id=brand_id)
    gpus = GPU.objects.filter(brand=brand)
    return render(request, 'store/brand_detail.html', {
        'brand': brand,
        'gpus': gpus
    })


def add_to_cart(request, gpu_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        cart[str(gpu_id)] = cart.get(str(gpu_id), 0) + 1
        request.session['cart'] = cart

        redirect_to = request.POST.get('redirect_to', 'view4')
        return redirect(redirect_to)
    else:
        return redirect('index')


def view4(request):
    cart = request.session.get('cart', {})
    gpus = GPU.objects.filter(id__in=cart.keys())
    cart_items = []

    for gpu in gpus:
        cart_items.append({
            'gpu': gpu,
            'quantity': cart[str(gpu.id)],
            'total_price': gpu.price * cart[str(gpu.id)],
        })

    return render(request, 'store/view4.html', {
        'cart_items': cart_items,
    })


def view3(request):
    brands = GPUBrand.objects.all()
    return render(request, 'store/view3.html', {'brands': brands})


def gpu_list(request):
    gpus = GPU.objects.all()
    brands = GPUBrand.objects.all()
    return render(request, 'store/gpu_list.html', {
        'gpus': gpus,
        'brands': brands
    })


def checkout(request):
    cart = request.session.get('cart', {})
    gpus = GPU.objects.filter(id__in=cart.keys())

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for gpu in gpus:
                OrderItem.objects.create(
                    order=order,
                    gpu=gpu,
                    quantity=cart[str(gpu.id)]
                )
            request.session['cart'] = {}  # очищення кошика
            return redirect('order_success')
    else:
        form = OrderForm()

    cart_items = []
    for gpu in gpus:
        cart_items.append({
            'gpu': gpu,
            'quantity': cart[str(gpu.id)],
            'total_price': gpu.price * cart[str(gpu.id)],
        })

    return render(request, 'store/checkout.html', {
        'form': form,
        'cart_items': cart_items
    })


def order_success(request):
    return render(request, 'store/order_success.html')
