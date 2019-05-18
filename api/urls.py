from rest_framework import routers
from .views import UserGet


router = routers.DefaultRouter()
router.register(r'^get', UserGet.as_view(), base_name='user-get')
# router.register(r'^set', ImageSet.as_view(), base_name='image-set')
