from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from project.forms import RegisterForm, ProductForm, OrderForm, ContactForm
from project.models import Register, Product, Order, Contact


def index(request):
    return render(request, "index.html")


def authen(request):
    return render(request, "auth/auth.html")


def shoes(request):
    pro = Product.objects.all()
    return render(request, "auth/shoes.html", {'products': pro})


def collection(request):
    return render(request, "auth/collection.html")



def adminpanel(request):
    p = Product.objects.all()
    return render(request, "adminpanel/dashboard.html", {'product': p})


def userpage(request):
    customer = Register.objects.all()
    return render(request, "adminpanel/users.html", {'customer': customer})


def orderpage(request):
    o = Order.objects.all()
    return render(request, "adminpanel/orders.html", {'order': o})


def contactpage(request):
    c = Contact.objects.all()
    return render(request, "adminpanel/contactpage.html", {'contact': c})


def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            reg = Register.objects.get(username=username, password=password)
            return redirect('authen')

        except:
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                return redirect('adminpanel')
            return render(request, 'index.html')

    else:
        form = RegisterForm()
        return render(request, "login.html", {'form': form})


def register(request):
    if request.method == "POST":
        if request.method == "POST":

            print(request.POST)
            form = RegisterForm(request.POST)
            form.save()

            return redirect('login')

        else:
            form = RegisterForm()
        return render(request, "adminpanel/dashboard.html", {'form': form})

    return render(request, "register.html")


def logout(request):
    request.session.clear()
    return redirect('index')


def deleteusers(request, p_id):
    product = Register.objects.get(id=p_id)
    product.delete()
    return redirect("/userpage")


def create(request):  # add product page
    return render(request, 'adminpanel/addproduct.html')


def billing(request):  # add product page
    return render(request, 'auth/billing.html')


def product_create(request):
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/create")
    else:
        form = ProductForm()
    return render(request, "adminpanel/dashboard.html", {'form': form})


def Order_create(request):
    if request.method == "POST":
        print(request.POST)
        form = OrderForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/shoes")
    else:
        form = OrderForm()
    return render(request, "auth/billing.html", {'form': form})


def contact(request):
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST, request.FILES)
        form.save()
        print("uploaded to database")
        return redirect("/contact")
    else:
        form = ContactForm()
    return render(request, "auth/contact.html", {'form': form})


def updateproduct(request, p_id):
    order = Product.objects.get(id=p_id)
    form = ProductForm(instance=order, )
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/adminpanel")
    context = {'form': form}
    return render(request, "adminpanel/update.html", context)


def deleteproduct(request, p_id):
    product = Product.objects.get(id=p_id)
    product.delete()
    return redirect("/adminpanel")


def deleteorder(request, p_id):
    order = Order.objects.get(id=p_id)
    order.delete()
    return redirect("/orderpage")


def deletecontact(request, p_id):
    contact = Contact.objects.get(id=p_id)
    contact.delete()
    return redirect("/contactpage")
