from django import urls

from vehicle.views import VehicleViews


API_URL = 'vehicle'

urlpatterns = [
    urls.path(f'{API_URL}', VehicleViews.as_view()),
]
