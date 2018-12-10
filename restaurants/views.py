from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import  Restaurant, Eating, Eating_details, Comment_restaurant
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.


def index(request):
    restaurant = Restaurant.objects.order_by('-id')
    city = Restaurant.objects.values('city').distinct()
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    page = request.GET.get('page', 1)

    paginator = Paginator(restaurant, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'idempresa': idempresa,
        'pagination': users,
        'city':city
    }
    return render(request, 'home/restaurants/restaurant.html', context)

def index_city(request,name):
    restaurant = Restaurant.objects.filter(city=name)
    city = Restaurant.objects.values('city').distinct()
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    page = request.GET.get('page', 1)

    paginator = Paginator(restaurant, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'idempresa': idempresa,
        'place': users,
        'city':city
    }
    return render(request, 'home/restaurants/restaurant.html', context)

def search_form(request):
    if request.method == "POST": 
        name = request.POST['city']
        if name == "all":
            return redirect('/restaurant')
        else :
            return redirect('/restaurant/search/'+name)

def eating(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.review = restaurant.review + 1
    restaurant.save()
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    if idempresa == None:
        return redirect('/login/?next='+ request.path)
    else:
        tourer = Tourer.objects.filter(email=idempresa)
        eatings = Eating.objects.filter(restaurant=id)
        sum_commnet = Comment_restaurant.objects.filter(restaurant=id).count()
        comment = Comment_restaurant.objects.filter(
            restaurant=id).order_by('-date')
        account = Tourer.objects.get(email=idempresa)
        # context
        context = {
            'idempresa': idempresa,
            'tourer': tourer,
            'eatings': eatings,
            'sum_commnet': sum_commnet,
            'comment': comment,
            'restaurant':restaurant,
            'id_res':id,
        }
        return render(request, 'home/restaurants/restaurant_details.html', context)

def create_restaurant_tour(request,id):
    restaurant_details = Restaurant.objects.get(pk=id)
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
            return redirect('eating',id=id)
        except Exception as e:
            print(e)
            return redirect('eating',id=id)

def create_comment_eating(request,id):
    restaurant_details = Restaurant.objects.get(pk=id)
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
            account_details = Tourer.objects.get(email=idempresa)
            comment_place = Comment_restaurant(restaurant=restaurant_details,commnet=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('eating',id=id)
        except Exception as e:
            print(e)
            return redirect('eating',id=id)

def eating_details(request, id, id_restaurant):
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    eating_items = Eating_details.objects.filter(eating=id_restaurant)
    # context
    context = {
        'idempresa': idempresa,
        'eating_items':eating_items,
    }
    return render(request, 'home/restaurants/food_details.html',context)

# restaurants
class ListRestaurants(generic.ListView):
    template_name = "dashboard/restaurants/restaurants/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Restaurant.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListRestaurants, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListRestaurants, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddRestaurants(CreateView):
    template_name = 'dashboard/restaurants/restaurants/form.html'
    model = Restaurant
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddRestaurants, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddRestaurants, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddRestaurants, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateRestaurant(UpdateView):
    template_name = 'dashboard/restaurants/restaurants/form.html'
    model = Restaurant
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateRestaurant, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateRestaurant, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateRestaurant, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteRestaurant(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('IndexView_Restaurants')

# eating
class ListEating(generic.ListView):
    template_name = "dashboard/restaurants/eating/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Eating.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListEating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListEating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddEating(CreateView):
    template_name = 'dashboard/restaurants/eating/form.html'
    model = Eating
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddEating, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddEating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddEating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateEating(UpdateView):
    template_name = 'dashboard/restaurants/eating/form.html'
    model = Eating
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateEating, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateEating, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateEating, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteEating(DeleteView):
    model = Eating
    success_url = reverse_lazy('IndexView_Eating')
    
# eating_details
class ListEatingDetails(generic.ListView):
    template_name = "dashboard/restaurants/eating_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Eating_details.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListEatingDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListEatingDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddEatingDetails(CreateView):
    template_name = 'dashboard/restaurants/eating_details/form.html'
    model = Eating_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddEatingDetails, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddEatingDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddEatingDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateEatingDetail(UpdateView):
    template_name = 'dashboard/restaurants/eating_details/form.html'
    model = Eating_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateEatingDetail, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateEatingDetail, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateEatingDetail, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteEatingDetails(DeleteView):
    model = Eating
    success_url = reverse_lazy('IndexView_Eating_details')