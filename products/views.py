from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    db_products = Products.objects.all()
    return render(request, 'index.html', {'db_products': db_products})


def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_img_url = request.POST.get('product_img_url')

        if product_name:
            if 'cart' not in request.session:
                request.session['cart'] = {}

            cart = request.session.get('cart', {})

            # Verifica se il prodotto è già nel carrello
            if product_name in cart:
                if isinstance(cart[product_name], dict):
                    # Se sì, aumenta la quantità
                    cart[product_name]['quantity'] += 1
                else:
                    # Se `cart[product_name]` non è un dizionario, crea un nuovo dizionario per il prodotto
                    product_data = {
                        'name': product_name,
                        'price': product_price,
                        'img_url': product_img_url,
                        'quantity': 1,
                    }
                    cart[product_name] = product_data
            else:
                # Se no, aggiungi il prodotto al carrello
                product_data = {
                    'name': product_name,
                    'price': product_price,
                    'img_url': product_img_url,
                    'quantity': 1,  # Inizia con una quantità di 1
                }
                cart[product_name] = product_data

            request.session['cart'] = cart
            return render(request, 'cart.html', {'cart_products': list(cart.values())})

    return HttpResponse("Not valid request")


def remove_from_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        if product_name and 'cart' in request.session:
            if product_name in request.session['cart']:
                if request.session['cart'][product_name]['quantity'] > 1:
                    request.session['cart'][product_name]['quantity'] -= 1
                else:
                    del request.session['cart'][product_name]
                request.session.save()  # Salva la sessione dopo le modifiche

                # Restituisci una risposta JSON con i dati aggiornati del carrello
                cart_products = list(
                    request.session['cart'].values()) if 'cart' in request.session else []
                response_data = {
                    'message': f"Prodotto rimosso: {product_name}",
                    'cart_products': cart_products,
                }
                # return JsonResponse(response_data)
                return render(request, 'cart.html', {'cart_products': cart_products})

    # Se non si verifica un'operazione di rimozione, restituisci una risposta vuota o un messaggio di errore
    return HttpResponse("Prodouct not removed")


def cart_page(request):
    cart_products = request.session.get('cart_products', [])
    return render(request, 'cart.html', {'cart_products': cart_products})
