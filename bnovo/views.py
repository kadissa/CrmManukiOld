import datetime
import logging
import os
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.views import generic
from dotenv import load_dotenv

from webhooks.models import Guest
from .models import Customer
from .forms import GuestEditForm

load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename='logs/bnovo_views.log',
                    filemode='a', format='%(asctime)s, %(levelname)s, '
                                         '%(message)s, %(name)s')


class TodayListView(LoginRequiredMixin, generic.ListView):
    model = Customer
    today = datetime.date.today().isoformat()
    debug_today = datetime.datetime.now().strftime('%Y-%m-%d')
    template_name = 'guest_list.html'

    def get_any_day(self):
        if self.kwargs:
            if len(self.kwargs) > 1:
                any_day = datetime.date.fromisoformat(self.kwargs['date'])
                any_day -= datetime.timedelta(
                    days=1)
            else:
                any_day = datetime.date.fromisoformat(self.kwargs['date'])
                any_day += datetime.timedelta(days=1)
        else:
            any_day = datetime.date.today()
        today = any_day.isoformat()
        return today, any_day

    def get_queryset(self):
        today, any_day = self.get_any_day()
        super().get_queryset()
        queryset = (Customer.objects.filter(real_arrival__contains=today) |
                    Customer.objects.filter(real_departure__contains=today))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        today, any_day = self.get_any_day()
        context = super(TodayListView, self).get_context_data(**kwargs)
        sauna = (Guest.objects.filter(start__contains=today).exclude(
            status='Отменено').order_by('start') &
                 Guest.objects.filter(start__contains=today).exclude(
                     ful_name='Уборщик')).order_by('start')
        context['today'] = today
        context['sauna'] = sauna
        context['any_day'] = any_day
        return context


class SaunaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Guest
    template_name = 'sauna.html'
    slug_field = 'id'
    context_object_name = 'sauna'


class ChaleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = 'chale.html'
    slug_field = 'id'
    context_object_name = 'chale'


class SaunaEditView(PermissionRequiredMixin, generic.UpdateView):
    form_class = GuestEditForm
    model = Guest
    permission_required = 'webhooks.change_guest'
    template_name = 'sauna_edit.html'


@receiver(signals.post_save, sender=Customer)
def check_about_black_list(sender, **kwargs):
    """Слушает сигналы записи в базу. Ищет в базе объект с тегом 'black-list',
    сравнивает его телефон с телефоном последней записи в базу. В случае
    совпадения отсылает email"""
    black_list_queryset = sender.objects.filter(tag='black-list')
    last_object = sender.objects.latest('id')
    if black_list_queryset:
        for obj in black_list_queryset:
            if (last_object.phone == obj.phone or
                    last_object.email == obj.email):
                print(f'Гость {last_object}, с меткой <black-list> '
                      'забронировал домик на '
                      f'{last_object.real_arrival}')
                send_mail(
                    subject='Внимание!',
                    message=f'Гость {last_object}, телефон:{last_object.phone}'
                            f'с  меткой <black-list> '
                            f'забронировал домик на '
                            f'{last_object.real_arrival}',
                    from_email=os.getenv('EMAIL_HOST_USER'),
                    recipient_list=['kadissa70@gmail.com',
                                    'Al.malafeev2015@yandex.ru']
                )
