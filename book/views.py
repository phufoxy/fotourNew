from django.shortcuts import render,HttpResponse,get_object_or_404, redirect, HttpResponseRedirect
from tourer.models import Tourer, Account
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from tour.models import Tour,PlaceTour,BookTour
from .forms import BookTourForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
def book(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
    context = {
        'idempresa':idempresa
    }
    return render(request,'home/book/book.html',context)


def book_details(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    if idempresa == None:
        return redirect('/login/?next=' + request.path)
    else:
        account = Account.objects.get(email=idempresa)
        query = "SELECT t.*,b.*,sum(p.price) as total_price,(sum(p.price) * t.person) as sum_price FROM tour_tour t  inner join tour_placetour p on t.id=p.tour_id inner join  tour_booktour b on b.tour_id = t.id where b.accout_id =  '" + str(account.id) + "'" +" group by t.id"
        book_Tour = BookTour.objects.raw(query)
        book_Tour_count = BookTour.objects.filter(accout=account).count()
        if book_Tour_count == 0 :
            messages.error(request, 'You need to book at least 1 tour .')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            context = {
                'idempresa':idempresa,
                'context':book_Tour
            }
            return render(request,'home/book/book_details.html',context)
    
class ListTourer(generic.ListView):
    template_name = "dashboard/account/table.html"
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return Account.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddTourer(CreateView):
    template_name = 'dashboard/account/form.html'
    model = Account
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')

    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddTourer, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
    

        
class UpdateTourer(UpdateView):
    template_name = 'dashboard/account/form.html'
    model = Account
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House') #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        # super(UpdateHouse, self).form_valid(form)
        return super(UpdateTourer, self).form_valid(form)


    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteTourer(DeleteView):
    model = Account
    success_url = reverse_lazy('ListTourer')

# Create your views here.
class ListBookTour(generic.ListView):
    template_name = "dashboard/book/index.html"
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

class AddBookTour(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/book/_create.html'
    form_class = BookTourForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListBookTour')
   

class UpdateBookTour(PassRequestMixin, SuccessMessageMixin,
                     generic.UpdateView):
    model = BookTour
    template_name = 'dashboard/book/_update.html'
    form_class = BookTourForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('ListBookTour')
   

class DeleteBookTour(DeleteAjaxMixin, generic.DeleteView):
    model = BookTour
    template_name = 'dashboard/book/_delete.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListBookTour')

# # # Read
class BookTourReadView(generic.DetailView):
    model = BookTour
    template_name = 'dashboard/book/_read.html'
