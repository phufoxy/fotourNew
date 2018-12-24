from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .models import Tour, PlaceTour, BookTour, HouseTour
from tourer.models import Tourer,Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum,Count
from django.db.models import F
from datetime import datetime
from django.contrib import messages
from .forms import TourForm, PlaceTourForm, HouseTourForm, BookTourForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from tourer.forms import AccountForm
from passlib.hash import sha256_crypt
from django.core.files.storage import FileSystemStorage
import xlwt
import csv

# Create your views here.
class ListTour(generic.ListView):
    template_name = "dashboard/tour/tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Tour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/tour/tour/_create.html'
    form_class = TourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListTour')
   

class UpdateTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = Tour
    template_name = 'dashboard/tour/tour/_update.html'
    form_class = TourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListTour')
   

class DeleteTour(DeleteAjaxMixin, generic.DeleteView):
    model = Tour
    template_name = 'dashboard/tour/tour/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListTour')

# Read
class TourReadView(generic.DetailView):
    model = Tour
    template_name = 'dashboard/tour/tour/_read.html'

# Book Tour
class ListBookTour(generic.ListView):
    template_name = "dashboard/tour/book_tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return BookTour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListBookTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListBookTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
# List Tour

class ListPlaceTour(generic.ListView):
    template_name = "dashboard/tour/place_tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return PlaceTour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddPlaceTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/tour/place_tour/_create.html'
    form_class = PlaceTourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListPlaceTour')

class UpdatePlaceTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_update.html'
    form_class = PlaceTourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListPlaceTour')

class DeletePlaceTour(DeleteAjaxMixin, generic.DeleteView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListPlaceTour')

# Read
class PlaceTourReadView(generic.DetailView):
    model = PlaceTour
    template_name = 'dashboard/tour/place_tour/_read.html'



# List House Tour

class ListHouseTour(generic.ListView):
    template_name = "dashboard/tour/house_tour/index.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return HouseTour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListHouseTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListHouseTour, self).get_context_data(**kwargs)
            tourer = Account.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddHouseTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/tour/house_tour/_create.html'
    form_class = HouseTourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListHouseTour')

class UpdateHouseTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = HouseTour
    template_name = 'dashboard/tour/house_tour/_update.html'
    form_class = HouseTourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListHouseTour')

class DeleteHouseTour(DeleteAjaxMixin, generic.DeleteView):
    model = HouseTour
    template_name = 'dashboard/tour/house_tour/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListHouseTour')

# # Read
class HouseTourReadView(generic.DetailView):
    model = HouseTour
    template_name = 'dashboard/tour/house_tour/_read.html'

# profile
def ListProfile(request):
    template_name = "dashboard/profile/index.html"
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    if idempresa == None:
        messages.error(request, 'Email is incrorrect '+email)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    else:
        account = Account.objects.filter(email=idempresa)  
        context = {
            'context':account,
            'idempresa':idempresa,

        }
        return render(request,template_name,context)

def profile_update(request,email):
    if request.method == "POST":
        password = request.POST['password']
        question = request.POST['question']
        name = request.POST['name']
        isEmail = Account.objects.filter(email=email)
        if isEmail.count() < 1 :
            messages.error(request, 'Email is incrorrect '+email)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            account = Account.objects.get(email=email)
            account.password = sha256_crypt.encrypt(password)
            account.question = question
            account.name = name
            account.save()
            messages.success(request, 'Success Changer')
            return redirect(request.META.get('HTTP_REFERER')) 

def changer_avatar(request,email):
    if request.method == "POST":
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        isEmail = Account.objects.filter(email=email)
        if isEmail.count() < 1 :
            messages.error(request, 'Email is incrorrect '+email)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            account = Account.objects.get(email=email)
            account.avatar = uploaded_file_url[6:]
            account.save()
            messages.success(request, 'Success Changer')
            return redirect(request.META.get('HTTP_REFERER')) 
      

# list tour
def list_tour(request):
    tour = Tour.objects.annotate(sum_price = Sum(F('person'))).order_by('-id')
    query = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " group by t.id "
    )
    place = PlaceTour.objects.raw(query)
    query_item1 = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " group by t.id "
        " limit 5"
    )
    place_tour = PlaceTour.objects.raw(query_item1)
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
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
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city,
        'place_tour':place_tour
    }
    return render(request,'home/tour/tour.html',context)

def add_tour(request,id):
    if request.method == "POST":
        tour = Tour.objects.get(pk=id)
        date = request.POST['date']
        person_book = request.POST['person_book']
        phone = request.POST['phone']
        email = request.POST['email']
        idempresa= ''
        if 'account' in request.session:
            idempresa = request.session['account']
        else:
            idempresa=None
        if idempresa == None:
            messages.error(request, 'Please sign in to book.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            try:
                isAccount = Account.objects.get(email = idempresa)
                isBook= BookTour.objects.filter(tour=tour.id,accout=isAccount)
                if isBook.count() > 0:
                    messages.error(request, 'Tour has been created')
                    return redirect(request.META.get('HTTP_REFERER')) 
                else:
                    account_details = Account.objects.get(email=idempresa)
                    booktour = BookTour(accout=account_details,date_book=datetime.now(),date_start=date,tour=tour,person_book=person_book,phone=phone,email=email)
                    booktour.save()
                    messages.success(request, 'Book to success')
                    return redirect(request.META.get('HTTP_REFERER'))
            except Exception as e:
                messages.error(request, 'Error Page')
                return redirect(request.META.get('HTTP_REFERER'))


def tour_details(request,id):
    tour = Tour.objects.get(id=id)
    placeTour = PlaceTour.objects.filter(tour=tour).order_by('id')
    query = (
        "SELECT t.*,h.*,a.*,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " where t.id = " + str(id) + ""
        " group by t.id "
    )
    sum_place = PlaceTour.objects.raw(query)
    query_item1 = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " group by t.id "
        " limit 5"
    )
    place_tour = PlaceTour.objects.raw(query_item1)
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    context = {
        'context':placeTour,
        'tour':tour,
        'sum_place':sum_place,
        'place_tour':place_tour,
        'tour_city':tour_city
    }
    return render(request,'home/tour/tour_details.html',context)

def search_form(request):
    if request.method == "POST": 
        name = request.POST['city']
        if name == "all":
            return redirect('/tour')
        else :
            return redirect('/tour/search/'+name)

def search_tour_place(request,name):
    query = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " where t.city = '" + str(name) + "' "
        " group by t.id "
    )
    place = PlaceTour.objects.raw(query)
    city = Tour.objects.values('city').distinct()
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
    query_item1 = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " group by t.id "
        " limit 5"
    )
    place_tour = PlaceTour.objects.raw(query_item1)
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
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city,
        'place_tour':place_tour

    }
    return render(request,'home/tour/tour.html',context)

def query_mutil(city,price,person,date):
    query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
    " FROM tour_placeTour a inner join " 
    " tour_tour t on a.tour_id  = t.id "
    " inner join tour_housetour h on h.tour_id = t.id "
    " where t.city LIKE '%" + city + "%'  and t.person between " + str(person) + ""
    " group by t.id "
    " having (sum(a.price) * t.person) <= " + price + ""
    )
    if price == "":
        query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
        " FROM tour_placeTour a inner join " 
        " tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id "
        " where t.city LIKE '%" + city + "%'  and  t.person between " + str(person) + "" 
        " AND t.date_tour LIKE '%" + date +"%'"
        " group by t.id "
        " having (sum(a.price) * t.person) <= " + price + ""
        )
    else:
        query = ("SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price"
        " FROM tour_placeTour a inner join " 
        " tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id "
        " where t.city LIKE '%" + city + "%'  and t.person between " + str(person) + ""
        " AND t.date_tour LIKE '%" + date +"%'"
        " group by t.id "
        )
    return query

def search_tour_place_price(request,city,price,person,date):
    place = PlaceTour.objects.raw(query_mutil(city,price,person,date))
    query_item1 = (
        "SELECT *,((sum(a.price)+sum(h.price)) * t.person) as sum_price, sum(a.price)"
        " as total_price FROM tour_placeTour a"
        " inner join tour_tour t on a.tour_id  = t.id "
        " inner join tour_housetour h on h.tour_id = t.id"
        " group by t.id "
        " limit 5"
    )
    place_tour = PlaceTour.objects.raw(query_item1)
    city = Tour.objects.values('city').distinct()
    tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
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
    context = { 
        'idempresa':idempresa,
        'context':users,
        'tour_city':tour_city,
        'place_tour':place_tour
    }
    return render(request,'home/tour/tour.html',context)

def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="total.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('report')
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_LEFT
    alignment.vert = xlwt.Alignment.VERT_TOP
    style = xlwt.XFStyle() # Create Style
    style.alignment = alignment # Add Alignment to Style
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style = xlwt.easyxf('font: bold off,height 280, color black;\
                     borders: top_color red, bottom_color red, right_color red, left_color red,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color white;')
    font_style.name = 'Times New Roman'
    columns = ['NameTour', 'DateStart', 'DateBook', 'Name', 'Email', 'Phone' ]
    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    font_style = xlwt.easyxf('font: bold off, height 180, color black;\
                     borders: top_color green, bottom_color green, right_color green, left_color green,\
                              left thin, right thin, top thin, bottom thin;\
                     pattern: pattern solid, fore_color white;')
    font_style.name = 'Times New Roman'
    rows = BookTour.objects.all().values_list('tour', 'date_start', 'date_book', 'person_book','email','phone')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response