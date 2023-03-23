from django.contrib import admin
from trp_db.models import users
from trp_db.models import CommNumber
from trp_db.models import Orders
from trp_db.models import AccessRights
from trp_db.models import Documents
from trp_db.models import Spareparts
from trp_db.models import Category
from trp_db.models import Images


admin.site.register(users)
admin.site.register(CommNumber)
admin.site.register(Orders)
admin.site.register(AccessRights)
admin.site.register(Documents)
admin.site.register(Spareparts)
admin.site.register(Category)
admin.site.register(Images)



# Register your models here.
