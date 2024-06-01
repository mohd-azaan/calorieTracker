from django.shortcuts import render, redirect
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    foods = Food.objects.all()
    user = request.user
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        object = Food.objects.get(pk=food_consumed)
        consume = Consume(user=user, food_consumed=object)
        consume.save()
        return redirect('index')
    consumed_by_user = Consume.objects.filter(user=user)
    return render(request, 'myapp/index.html', {"foods": foods, "consumed_by_user":consumed_by_user}) 

def delete_consume(request, id):
    consumed_food = Consume.objects.get(pk=id)
    
    if request.method == "POST":
        consumed_food.delete()
        return redirect('index')
    else :
        return render(request, 'myapp/delete.html')