from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def app1():
    return '{\n"status": "OK"\n}'

@app_views.route('/api/v1/stats')
def count():
    return '{\n"amenities": %d,
               "cities": %d,
               "places": %d,
               "reviews": %d,
               "states": %d,
               "users": %d
               }'.format(storage.count(amenities), storage.count(cities),
                       storage.count(places), storage.count(reviews),
                       storage.count(states), storage.count(users))

