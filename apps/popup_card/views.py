# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import the logging library
# import logging

from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import DetailView, ListView

from apps.popup_card.models import Popup_card, Category_card, Comment
from business.base.Enums import EnumType, EnumStatus

# Get an instance of a logger
# logger = logging.getLogger(__name__)

from business.base.models import Tag_general

# Create your views here.
def hello_world(req):
    return render(req, 'popup_card/index.html')

def get_all_categories_active():
    return Category_card.objects.filter(status=EnumStatus.Active)

def get_comments_by_id_active(req):
    return Comment.objects.filter(card_post=req, status=EnumStatus.Active)

class ViewPopupCard(ListView):
    model = Popup_card
    template_name = 'popup_card/list_paper_cards.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ViewPopupCard, self).get_context_data(**kwargs)
        context['categories'] = get_all_categories_active()
        return context

    def get_queryset(self):
        return Popup_card.objects.filter(status=EnumType.CardPopup)

class ViewInvitationCard(ListView):
    model = Popup_card
    template_name = 'popup_card/list_paper_cards.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ViewInvitationCard, self).get_context_data(**kwargs)
        context['categories'] = get_all_categories_active()
        return context

    def get_queryset(self):
        return Popup_card.objects.filter(status=EnumType.InvitationCard)

class DetailPopupCard(DetailView):
    model = Popup_card
    template_name = 'popup_card/detail_paper_cards.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(DetailPopupCard, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        card = self.model.objects.filter(url=slug)
        context['card'] = card
        context['comments'] = get_comments_by_id_active(req=card)
        context['tags'] = Tag_general.objects.all()
        context['categories'] = get_all_categories_active()
        return context

class DetailInvitationCard(DetailView):
    model = Popup_card
    template_name = 'popup_card/detail_paper_cards.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(DetailInvitationCard, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        card = self.model.objects.filter(url=slug)
        context['card'] = card
        context['tags'] = Tag_general.objects.all()
        return context

class ListPopupCardByCategory(ListView):
    model = Popup_card
    template_name = 'popup_card/list_paper_cards.html'
    paginate_by = 8
    slug_field = 'cat'

    def get_context_data(self, **kwargs):
        context = super(ListPopupCardByCategory, self).get_context_data(**kwargs)
        context['categories'] = get_all_categories_active()
        return context

    def get_queryset(self):
        category = self.kwargs['slug']
        if category == 'all':
            return Popup_card.objects.filter(status=EnumType.CardPopup)
        else:
            return Popup_card.objects.filter(status=EnumType.CardPopup, category__url=category)

class ListInvitationCardByCategory(ListView):
    model = Popup_card
    template_name = 'popup_card/list_paper_cards.html'
    paginate_by = 8
    slug_field = 'cat'

    def get_context_data(self, **kwargs):
        context = super(ListInvitationCardByCategory, self).get_context_data(**kwargs)
        context['categories'] = get_all_categories_active()
        return context

    def get_queryset(self):
        category = self.kwargs['slug']
        if category == 'all':
            return Popup_card.objects.filter(status=EnumType.InvitationCard)
        else:
            return Popup_card.objects.filter(status=EnumType.InvitationCard, category__url=category)