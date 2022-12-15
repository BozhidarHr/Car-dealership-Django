from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DeleteView, FormView, UpdateView, ListView, DetailView, TemplateView, CreateView

from car_dealer.web.forms import CreateUserForm, ListingForm, FeedbackForm, TicketForm, CommentForm, ReportListingForm
from car_dealer.web.models import Listing, Feedback, Comment, ReportListing


def home_view(request):

    listings = Listing.objects.all().order_by('-date_created')
    feedbacks = Feedback.objects.order_by('?')[:6]
    paginator = Paginator(listings, 8)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'listings': listings,
        'feedbacks': feedbacks,
        'page': page,


    }
    return render(request, 'home.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)

                return redirect('login form')

        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Login credentials are incorrect.')

    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def listing_view(request):
    form = ListingForm
    if request.method == "POST":
        listing_form = ListingForm(request.POST, request.FILES)
        if listing_form.is_valid():
            listing = listing_form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'create_listing.html', context)


class DeleteListingView(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Listing
    success_url = reverse_lazy('home')
    template_name = 'listing_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(self.success_url)
        else:
            return super(DeleteListingView, self).post(request, *args, **kwargs)


class FeedbackView(LoginRequiredMixin, FormView):
    login_url = '/login'
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = '/'
    model = Feedback

    def get_initial(self):
        initial = super().get_initial()
        initial['full_name'] = self.request.user.get_full_name()
        return initial

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user
        form.save()
        return super().form_valid(form)


class EditListingView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Listing
    form_class = ListingForm
    template_name = 'edit_listing.html'
    success_url = '/'

    def form_valid(self, form):
        listing = form.save(commit=False)
        listing.user = self.request.user
        listing.save()
        return super().form_valid(form)


class MyListingsView(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Listing
    template_name = 'my_listings.html'
    context_object_name = 'listings'
    queryset = model.objects.all()

    def paginate(self):
        paginator = Paginator(self.queryset, 8)
        page_num = self.request.GET.get('page')
        page = paginator.get_page(page_num)

        return page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['page'] = self.paginate()
        return context


class DetailListingView(DetailView):
    template_name = 'details.html'
    queryset = Listing.objects.all()
    context_object_name = 'listing'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['comment_form'] = CommentForm
        comments = Comment.objects.filter(
            listing=self.get_object())
        data['comments'] = comments
        return data

    def get_object(self):
        pk = self.kwargs.get('pk')
        listing = get_object_or_404(Listing, pk=pk)
        return listing

    def form_valid(self, form):
        comment = form.save(commit = False)
        return comment.save()

    def post(self, request, *args, **kwargs):
        comment = Comment(comment=request.POST.get('comment'), user=self.request.user, listing=self.get_object())
        comment.save()
        return self.get(self, request, *args, **kwargs)


class ContactUsView(FormView):
    template_name = 'contact_us.html'
    form_class = TicketForm
    success_url = '/'


    def form_valid(self, form):
        ticket = form.save()
        return super().form_valid(ticket)


class ReportListingView(LoginRequiredMixin, FormView):
    login_url = '/login'
    template_name = 'report_listing.html'
    form_class = ReportListingForm
    success_url = '/'
    context_object_name = 'listing'
    model = ReportListing

    def get_initial(self):
        initial = super().get_initial()
        initial['full_name'] = self.request.user.get_full_name()
        initial['email'] = self.request.user.email
        return initial

    def get_object(self):
        pk = self.kwargs.get('pk')
        listing = get_object_or_404(Listing, pk=pk)
        return listing

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.listing = self.get_object()
        messages.success(self.request, 'Your report was submitted! We will look into it as soon as possible.')
        return super().form_valid(form)

