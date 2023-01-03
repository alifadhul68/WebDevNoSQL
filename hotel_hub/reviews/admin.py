from django.contrib import admin
from .models import Review, Hotel

admin.site.site_header = "Hotel's Hub Administration"
admin.site.site_title = "Hotel's Hub"
admin.site.index_title = 'Administration'

class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ('id', 'title', 'description', 'city')
    search_fields = ['title']

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('get_name', 'rating', 'user', 'comment', 'publish_date')
    list_filter = ['publish_date', 'rating', 'hotel__title']
    search_fields = ['comment', 'rating']

    def get_name(self, obj):
        return obj.hotel.title
    get_name.admin_order_field  = 'hotel'
    get_name.short_description = 'Hotel Name'

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Review, ReviewAdmin)