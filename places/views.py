from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Place, PlaceDetails, CommentPlace
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer, Account
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from .forms import PlaceForm, PlaceDetailForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from tour.models import Tour, PlaceTour
# Dashboard template
# Place Index
class Index(generic.ListView):
    model = Place
    template_name = 'dashboard/places/places/index.html'
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return Place.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(Index, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(Index, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
    

# Create Place
class PlaceCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/places/places/create_place.html'
    form_class = PlaceForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListPlace')

# Update Place
class PlaceUpdateView(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Place
    template_name = 'dashboard/places/places/update_place.html'
    form_class = PlaceForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListPlace')

# Read Place
class PlaceReadView(generic.DetailView):
    model = Place
    template_name = 'dashboard/places/places/read_places.html'

# Delete Place
class PlaceDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Place
    template_name = 'dashboard/places/places/delete_place.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListPlace')

# List places details
class ListPlaceDetails(generic.ListView):
    model = PlaceDetails
    template_name = "dashboard/places/places_details/index.html"
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return PlaceDetails.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListPlaceDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlaceDetails, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

# Add Place Details
class AddPlaceDetails(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/places/places_details/create_place_details.html'
    form_class = PlaceDetailForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListPlaceDetails')

# Update Place Details
class UpdatePlaceDetails(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = PlaceDetails
    template_name = 'dashboard/places/places/update_place.html'
    form_class = PlaceDetailForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListPlaceDetails')


# Delete Place Details
class DeletePlaceDetails(DeleteAjaxMixin, generic.DeleteView):
    model = PlaceDetails
    template_name = 'dashboard/places/places_details/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListPlaceDetails')
    success_message = "Thing was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePlaceDetails, self).delete(request, *args, **kwargs)

# Read Place Details
class PlaceDetailsReadView(generic.DetailView):
    model = PlaceDetails
    template_name = 'dashboard/places/places_details/_read.html'

# Home Template
# List template
def index(request):
    # get all place
    place = Place.objects.order_by('-id')
    # get disticnt city in place
    city = Place.objects.values('city').distinct()
    # get all tour
    tour = Tour.objects.order_by('-id')[:5]
    # get all place tour
    place_tour = Place.objects.all().order_by('-price')[:5]
    # check session 
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None
    # panigation
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    try:
        # get account = email 
        account = Account.objects.get(email=idempresa)
        # check account is admin
        isAdmin = account.author
        if isAdmin == "admin" :
            context = { 
                'idempresa':idempresa,
                'place':users,
                'city':city,
                'admin':'admin',
                'tour':tour,
                'place_tour':place_tour
            }
            return render(request,'home/places/places.html',context)
        else :
            context = { 
                'idempresa':idempresa,
                'place':users,
                'city':city,
                'tour':tour,
                'place_tour':place_tour
            }
            return render(request,'home/places/places.html',context)
    except  Exception as e:
        context = { 
                'idempresa':idempresa,
                'place':users,
                'city':city,
                'tour':tour,
                'place_tour':place_tour
            }
        return render(request,'home/places/places.html',context)
    

def search_form(request):
    if request.method == "POST": 
        name = request.POST['city']
        if name == "all":
            return redirect('/places')
        else :
            return redirect('/places/search/'+name)
   

def search_place(request,name):
    place = Place.objects.filter(city=name)
    city = Place.objects.values('city').distinct()
    tour = Tour.objects.order_by('-id')[:5]

    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    place_tour = Place.objects.all().order_by('-price')[:5]
    context = { 
        'idempresa':idempresa,
        'place':users,
        'city':city,
        'tour':tour,
        'place_tour':place_tour
    }
    return render(request,'home/places/places.html',context)

def places_details(request,id):
    try:
        city = Place.objects.values('city').distinct()
        places_details = Place.objects.get(pk=id)
        places_details.review = places_details.review + 1
        places_details.save()
        place_tour = Place.objects.all().order_by('-price')[:5]
        idempresa= ''
        if 'account' in request.session:
            idempresa = request.session['account']
        else:
            idempresa=None

        try:
            tourer = Account.objects.filter(email=idempresa)
            places_items = PlaceDetails.objects.filter(place=id)
            sum_commnet = CommentPlace.objects.filter(place=id).count()
            comment = CommentPlace.objects.filter(place=id)
            tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
            # context
            context = {
                'idempresa':idempresa,
                'tourer':tourer,
                'places_items':places_items,
                'sum_commnet':sum_commnet,
                'comment':comment,
                'places_details':places_details,
                'tour_city':tour_city,
                'place_tour':place_tour,
                'city':city,

            }
            return render(request,'home/places/places_details.html',context)
        except Exception as e:
            places_items = PlaceDetails.objects.filter(place=id)
            sum_commnet = CommentPlace.objects.filter(place=id).count()
            comment = CommentPlace.objects.filter(place=id)
            # context
            context = {
                'idempresa':idempresa,
                'places_items':places_items,
                'sum_commnet':sum_commnet,
                'comment':comment,
                'places_details':places_details,
                'place_tour':place_tour,
                'city':city,
            }
            return render(request,'home/places/places_details.html',context)
    except Exception as e:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })
    # account
    

def create_place_tour(request,id):
    place_details = Place.objects.get(pk=id)
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
           
            return redirect('places_details',id=id)
        except Exception as e:
            print(e)
            return redirect('places_details',id=id)


def create_comment_place(request,id):
    place_details = Place.objects.get(pk=id)
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
            comment_place = CommentPlace(place=place_details,comment=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('places_details',id=id)
        except Exception as e:
            print("Error "+e)
            return redirect('places_details',id=id)

