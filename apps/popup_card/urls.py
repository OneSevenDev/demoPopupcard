from django.conf.urls import url

from apps.popup_card.views import hello_world, ViewPopupCard, ViewInvitationCard, DetailPopupCard, \
    ListPopupCardByCategory, ListInvitationCardByCategory, DetailInvitationCard

urlpatterns = [
    url(r'^$', hello_world, name='hello_world'),
    url(r'^products/popup-card/$', ViewPopupCard.as_view(), name='popup_card_list'),
    url(r'^products/popup-card/p/(?P<slug>[-\w]+)/$', DetailPopupCard.as_view(), name='popup_card_detail'),
    url(r'^products/popup-card/c/(?P<slug>[-\w]+)/$', ListPopupCardByCategory.as_view(), name='card_list_by_category'),
    url(r'^products/invitation-card/$', ViewInvitationCard.as_view(), name='invitation_card_list'),
    url(r'^products/invitation-card/(?P<slug>[-\w]+)/$', DetailInvitationCard.as_view(), name='invitation_card_detail'),
    url(r'^products/invitation-card/(?P<cat>[-\w]+)/$', ListInvitationCardByCategory.as_view(), name='invitation_card_list_by_category'),
]
