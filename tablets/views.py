from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from .models import Tablet, Seal
from .forms import TabletForm, SealForm

class SealDetailView(DetailView):

    model = Seal
    template_name = 'tablets/seal_detail.html'


class SealCreate(CreateView):

    model = Seal
    template_name = 'tablets/seal_create.html'
    form_class = SealForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SealCreate, self).dispatch(*args, **kwargs)


class SealUpdate(UpdateView):

    model = Seal
    form_class = SealForm
    template_name = 'tablets/seal_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SealUpdate, self).dispatch(*args, **kwargs)


class SealDelete(DeleteView):
    model = Seal
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_tablets')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SealDelete, self).dispatch(*args, **kwargs)


class TabletDetailView(DetailView):

    model = Tablet
    template_name = 'tablets/tablet_detail.html'


class TabletCreate(CreateView):

    model = Tablet
    template_name = 'tablets/tablet_create.html'
    form_class = TabletForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletCreate, self).dispatch(*args, **kwargs)


class TabletUpdate(UpdateView):

    model = Tablet
    form_class = TabletForm
    template_name = 'tablets/tablet_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletUpdate, self).dispatch(*args, **kwargs)


class TabletDelete(DeleteView):
    model = Tablet
    template_name = 'vocabs/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_tablets')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TabletDelete, self).dispatch(*args, **kwargs)
