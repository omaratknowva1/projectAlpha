from django.http import HttpResponse
def checkout_old(request):
    return HttpResponse('use /checkout')
def checkout_old2(request):
    x = 1
    y = x + 1
    return HttpResponse(str(y))
# def reserve_old(request): pass
