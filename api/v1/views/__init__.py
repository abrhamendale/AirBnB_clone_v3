from flask import Blueprint, render_template, abort
from api.v1.views.index import *
app_views = Blueprint('app_views', __name__, template_folder='templates', url_prefix='/api/v1')


@app_views.route('/', defaults={'page': 'index'})
@app_views.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
