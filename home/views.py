from django.shortcuts import render, redirect, HttpResponseRedirect
from places.models import Place
from house.models import House
from tour.models import Tour, BookTour, PlaceTour
from tourer.models import Tourer, Account
from django.contrib import messages

# Create your views here.
def home(request):
    places = Place.objects.all().order_by('-id')[:8]
    houses = House.objects.all().order_by('-id')[:3]
    query = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id  limit 8"
    tour = Tour.objects.raw(query)
    place_context = Place.objects.all().order_by('-price')[:4]

    query_total_accout = (
        " select *,count(a.accout_id) as countTotal from tour_booktour as"
        " a inner join tourer_account  as"
        " t on a.accout_id = t.id"
        " group by a.accout_id"
        " order by count(a.accout_id) desc"
        " limit 4"
    )
    booktotal = BookTour.objects.raw(query_total_accout)

    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    if idempresa == None:
        tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
        context = {
            'context':tour,
            'idempresa':idempresa,
            'houses':houses,
            'tour_city':tour_city,
            'place_context':place_context,
            'booktotal':booktotal
        }
        return render(request,'home/home.html',context)
    else:
        account = Account.objects.get(email=idempresa)
        author_account = account.author
        if author_account == 'admin':
            query_details = "SELECT t.*,b.*,sum(p.price) as total_price,(sum(p.price) * t.person) as sum_price FROM tour_tour t  inner join tour_placetour p on t.id=p.tour_id inner join  tour_booktour b on b.tour_id = t.id where b.accout_id =  '" + idempresa + "'" +" group by t.id"
            bookTour = BookTour.objects.raw(query_details)
            tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
            context = {
                'context':tour,
                'idempresa':idempresa,
                'houses':houses,
                'bookTour':bookTour,
                'tour_city':tour_city,
                'admin':'admin',
                'place_context':place_context,
                'booktotal':booktotal
            }
            return render(request,'home/home.html',context)
        else:
            tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")
            context = {
                'context':tour,
                'idempresa':idempresa,
                'houses':houses,
                'tour_city':tour_city,
                'place_context':place_context,
            }
            return render(request,'home/home.html',context)
  

def search_multi(request):
    if request.method == "POST":
        city = request.POST.get('city_tour')
        price = request.POST.get('price')
        person = request.POST.get('person')
        date = request.POST.get('date')
        return redirect('/tour/search/' + city + '/' + str(price) + '/' + str(person) + '/' + str(date) + '/')
    else:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })