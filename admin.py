from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates/admin')


@admin.route('/')
@admin.route('/dashboard')
def index():
    return "Admin dashboard page"


@admin.route('/category')
@admin.route('/category/list')
def category():
    return "Admin category list"


@admin.route('/category/add')
def category_add():
    return 'add category'


@admin.route('/category/<category_id>')
def category_edit(category_id):
    return 'Edit category'


@admin.route('/category/<category_id>/delete')
def category_delete(category_id):
    return 'delete category'


@admin.route('/tv_series')
@admin.route('/tv_series/list')
def tv_series():
    return "Admin Series list"


@admin.route('/tv_series/add')
def tv_series_add():
    return "Admin series add"


@admin.route('/tv_series/<series_id>/edit')
def tv_series_edit(series_id):
    return "Admin series edit"


@admin.route('/tv_series/<series_id>/delete')
def tv_series_delete(series_id):
    return "Admin series delete"


@admin.route('/tv_series/<series_id>/publish')
def tv_series_publish(series_id):
    return "Admin series publish"


@admin.route('/tv_series/<series_id>/list')
def tv_series_episode_list(series_id):
    return "Admin series episode list"


@admin.route('/tv_series/<series_id>/add')
def tv_series_episode_add(series_id):
    return "Admin series episode add"


@admin.route('/tv_series/<series_id>/<episode_id>')
def tv_series_episode_edit(series_id, episode_id):
    return "Admin series episode edit"


@admin.route('/tv_series/<series_id>/<episode_id>/delete')
def tv_series_episode_delete(series_id, episode_id):
    return "Admin series episode delete"


@admin.route('/tv_series/<series_id>/<episode_id>/publish')
def tv_series_episode_publish(series_id, episode_id):
    return "Admin series episode publish"


@admin.route('/user')
@admin.route('/user/list')
def user():
    return "Admin user list"


@admin.route('/user/add')
def user_add():
    return 'add user'


@admin.route('/user/<user_id>')
def user_edit(user_id):
    return 'Edit user'


@admin.route('/user/<user_id>/delete')
def user_delete(user_id):
    return 'delete user'


@admin.route('/movie')
@admin.route('/movie/list')
def movie():
    return "Admin movie list"


@admin.route('/movie/add')
def movie_add():
    return 'add delete'


@admin.route('/movie/<movie_id>')
def movie_edit(movie_id):
    return 'Edit movie'


@admin.route('/movie/<movie_id>/delete')
def movie_delete(movie_id):
    return 'delete movie'


@admin.route('/movie/<movie_id>/publish')
def movie_publish(movie_id):
    return 'publish movie'

