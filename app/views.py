from flask import render_template
from app import app
from .request import get_news
from .request import get_news, get_news

@app.route('/news/<news_id>')
def index():
    
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    general_news = get_news('general')
    health_news = get_news('health')
    science_news = get_news('science')
    sports_news = get_news('sport')
    technology_news = get_news('technology')
    news = 'Home - This is the News Highligh'
    search_movie = request.args.get('movie_query')

    if search_news:
        return redirect(url_for('search', news_name=search_news))
    else:
        return render_template('index.html', news=news, business = business_news, entertainment = entertainment_news, general = general_news, health = health_news, science = science_news, sports = sports_news, technology = technology_news )
