from django.contrib import admin, messages
from django.utils.translation import gettext as _

from . import models
from .models import Item


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        # 'access_token',
        # 'sandbox_token',
    )
    prepopulated_fields = {
        'slug': ('name',),
    }
    # readonly_fields = (
    #     'access_token',
    # )

    # def access_token(self, obj):
    #     if obj.app_id and obj.secret_key:
    #         try:
    #             return obj.service.get_access_token()
    #         except Exception:
    #             pass
    #
    #     return '-'
    # access_token.short_description = _('access token')


@admin.register(models.Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = (
        'mp_id',
        'reference',
        'paid',
    )

    @admin.action(
        description=_('poll status')
    )
    def poll_status(self, request, queryset):
        payments = [payment.poll_status() for payment in queryset]
        payments_count = sum(payment is not None for payment in payments)
        messages.add_message(
            request,
            messages.SUCCESS,
            _('%d payments created.') % payments_count
        )

    actions = (
        poll_status,
    )


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'mp_id',
        'status',
        'status_detail',
        'created',
        'approved',
    )


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'topic',
        'resource_id',
        'status',
        'last_update',
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'preference',
        'title',
        'currency_id',
        'description',
        'quantity',
        'unit_price',
    )
    list_filter = ('preference',)
