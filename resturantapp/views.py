from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import storetype,items,itemsdetails,cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,LoginUserForm
# Create your views here.

def index(request):
    request.session["cart"]="10"
    template=loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))


   
def burger(request):
    
    p=items.objects.filter(st_id=1)
    template=loader.get_template('burger.html')
    return HttpResponse(template.render({'items':p,'request':request}))  

def side_dishes(request):
    p=items.objects.filter(st_id=2)
    template=loader.get_template('side_dishes.html')
    return HttpResponse(template.render({'items':p,'request':request}))

def drinks(request):
    p=items.objects.filter(st_id=3)
    template=loader.get_template('drinks.html')
    return HttpResponse(template.render({'items':p,'request':request}))


def details(request,id):

    template=loader.get_template('details.html')
    data=itemsdetails.objects.select_related('items').filter(id=id).first()
    if hasattr(data.items,'price_increase_per_unit'):
        price_increase=data.qty*data.items.price_increase_per_unit
        data.total=(data.items.price+price_increase)*data.qty
    else:
        data.total=data.items.price*data.qty
    return HttpResponse(template.render({'data':data,'request':request}))   

@csrf_exempt
def add_to_cart(request):
    id=request.POST.get("id")
    p=cart(itemsid=id)
    p.save()
    row=cart.objects.all()
    count=0
    for item in row:
        count=count+1 

    request.session["cart"]=count
    return JsonResponse({'count':count})

@login_required(login_url='/auth_login/')
def checkout(request):
    cartitem=cart.objects.values_list('itemsid', flat= True) 
    item= itemsdetails.objects.select_related('items').filter(id__in=cartitem)
    template=loader.get_template('checkout.html')
    return HttpResponse(template.render({'request':request,'item':item}))   

@csrf_exempt
def auth_login(request):
    form=LoginUserForm()
    if request.method=="POST":
        form=LoginUserForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
          
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'checkout.html')

    context={'form':form}
    return render(request,'auth_login.html',context)


@csrf_exempt
def auth_register(request):
    template=loader.get_template('auth_register.html')
    form=CreateUserForm
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context={'registerform':form}
    return HttpResponse(template.render(context=context))   



def search_products(request):
  query = request.GET.get('query', '')

  if query:
    products = items.objects.filter(st_id=query)
  else:
    products = items.objects.all()  # Show all products if no query is provided

  context = {'results': products}
  return render(request, 'search_results.html', context)
