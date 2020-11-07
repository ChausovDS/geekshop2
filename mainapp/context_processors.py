from basketapp.models import Basket


def basket(request):
    print("context processor basket works")
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {
        "basket": basket,
    }
