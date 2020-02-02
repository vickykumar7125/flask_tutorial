from flask import Blueprint, render_template

home = Blueprint('home', __name__, static_folder='static', template_folder='templates/app')


@home.route('/')
@home.route('/home')
def index():
    return render_template('home.html')


@home.route('/series/<series_id>')
def series(series_id):
    return render_template('series.html')


@home.route('/search/<key>', methods=['GET', 'POST'])
def search(key):
    return render_template('search.html')


@home.route('/watch/<episode_id>')
def watch(episode_id):
    return render_template('watch.html')


@home.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@home.route('/faq')
def faq():
    return render_template('faq.html')


@home.route('/terms_and_con')
def terms_and_con():
    return render_template('terms_n_cond.html')


@home.route('/privacy')
def about():
    return render_template('privacy.html')


@home.route('/about_us')
def about_us():
    return render_template('about.html')
