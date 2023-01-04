from django import urls

from user.views import UserViews


API_URL = 'user'

urlpatterns = [
    urls.path(f'{API_URL}', UserViews.as_view()),
]
