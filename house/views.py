from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import House,House_details,Comment_house
from tourer.models import Tourer, Account
from django.template import RequestContext
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import HouseForm, HouseDetailsForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from tour.models import Tour,PlaceTour,BookTour

# Create your views here.
def house(request):
    house_items = House.objects.order_by('-id')
    city = House.objects.values('city').distinct()
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(house_items, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    place_tour = House.objects.all().order_by('-price')[:5]
    context = {
        'house_items':users,
        'idempresa':idempresa,
        'city':city,
        'place_tour':place_tour

    }
    return render(request,'home/hotels.html',context)

def form_search(request):
    if request.method == "POST":
        name = request.POST['city']
        if name == "all":
            return redirect('/house')
        else:
            return redirect('/house/search/'+name)

def house_search(request,name):
    house_items = House.objects.filter(city=name)
    city = House.objects.values('city').distinct()
    query_item_1 = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id order by a.id limit 5"
    place_tour = PlaceTour.objects.raw(query_item_1)
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(house_items, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'house_items':users,
        'idempresa':idempresa,
        'city':city,
        'place_tour':place_tour
    }
    return render(request,'home/hotels.html',context)

def house_details(request,id):
    try:
        house_details = House.objects.get(pk=id)
        house_details.review = house_details.review + 1
        house_details.save()
        # house items
        house_items = House_details.objects.filter(house=id)
        city = House.objects.values('city').distinct()
        place_tour = House.objects.all().order_by('-price')[:5]
        # account
        idempresa= ''
        if 'account' in request.session:
            idempresa = request.session['account']
        else:
            idempresa=None

        if idempresa == None:
            
            sum_commnet = Comment_house.objects.filter(house=id).count()
            
            # context
            context = {
                'house_items':house_items,
                'house_details':house_details,
                'sum_commnet':sum_commnet,
                'city':city,
                'place_tour':place_tour
                # 'a':a
            }
            return render(request,'home/hotel_details.html',context)
        else:
            tourer = Account.objects.filter(email=idempresa)
            comment = Comment_house.objects.filter(house=id).order_by('-date')
            sum_commnet = Comment_house.objects.filter(house=id).count()
            account = Account.objects.get(email=idempresa)
           
            # context
            context = {
                'house_items':house_items,
                'idempresa':idempresa,
                'tourer':tourer,
                'house_details':house_details,
                'comment':comment,
                'sum_commnet':sum_commnet,
                'city':city,
                'place_tour':place_tour
                # 'a':a
            }
            return render(request,'home/hotel_details.html',context)
    except House.DoesNotExist as e:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })
    

def create_house_tour(request,id):
    house_details = House.objects.get(pk=id)
    # email = request.GET['email']
    book = request.GET['book']
    date_to = request.GET['date_to']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            account_details = Tourer.objects.get(email=idempresa)
            return redirect('house_details',id=id)
        except Exception as e:
            print(e)
            return redirect('house_details',id=id)

def create_comment_house(request,id):
    house_details = House.objects.get(pk=id)
    # email = request.GET['email']
    commnet_items = request.GET['comment_items']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            account_details = Account.objects.get(email=idempresa)
            comment_house = Comment_house(house=house_details,comment=commnet_items,date=datetime.now(),account=account_details)
            comment_house.save()
            return redirect('house_details',id=id)
        except Exception as e:
            print(e)
            return redirect('house_details',id=id)
    

def dashboard_form_house(request):
    idTourer = ''
    if 'account' in request.session:
        idTourer = request.session['account']
    else:
        idTourer = None
    
    if idTourer == None:
        return render(request,'login/login.html')
    else:
        tourer = Account.objects.filter(email=idTourer)
        house = House.objects.all()
        context = {
            'tourer':tourer,
            'house':house
        }
        return render(request,'dashboard/form.html',context)

class ListHouse(generic.ListView):
    template_name = "dashboard/house/index.html"
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return House.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListHouse, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListHouse, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddHouse(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/house/_create.html'
    form_class = HouseForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListHouse')
    
      
class UpdateHouse(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = House
    template_name = 'dashboard/house/_update.html'
    form_class = HouseForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListHouse')

class DeleteHouse(DeleteAjaxMixin, generic.DeleteView):
    model = House
    template_name = 'dashboard/house/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListHouse')

# Read
class HouseReadView(generic.DetailView):
    model = House
    template_name = 'dashboard/house/_read.html'



class ListHouseDetails(generic.ListView):
    template_name = "dashboard/house_details/index.html"
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return House_details.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListHouseDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListHouseDetails, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddHouseDetails(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/house_details/_create.html'
    form_class = HouseDetailsForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListHouseDetails')

class UpdateHouseDetails(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = House_details
    template_name = 'dashboard/house_details/_update.html'
    form_class = HouseDetailsForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListHouseDetails')

class DeleteHouseDetails(DeleteAjaxMixin, generic.DeleteView):
    model = House_details
    template_name = 'dashboard/house_details/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListHouseDetails')


def dashboard_home(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    if idempresa == None:
        return redirect('/login/?next='+ request.path)
    else:
        account = Account.objects.get(email=idempresa)
        author_account = account.author
        if author_account == "admin" :
            return redirect('ListPlace')
        else :
            return render(request,'error/index.html',{
                'error':'You are not an administrator'
            })

def error_page(request):
    return render(request,'error/index.html')