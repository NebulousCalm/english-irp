from flask import Flask, render_template, jsonify, request
from get_website_impact import get_website_impact
from get_local_aqi import get_aqi_by_location
from news import get_google_news_urls

app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = get_google_news_urls("USA Government and Climate Change", "America")
    return render_template('index.html', articles=resp)


@app.route('/impact')
def get_impact():
    # website_impact = get_website_impact('https://english-irp.vercel.app')
    return render_template('impact.html')


@app.route('/get_impacts')
def get_impacts():
    return render_template('get_impacts.html')


@app.route('/get_aqi', methods=['GET', 'POST'])
def get_aqi():
    if request.method == 'POST':
        city = request.form['city']
        state = request.form['state']
        return render_template(
            'get_aqi.html',
            data=get_aqi_by_location('a9e13194-ad5a-4512-aebe-860d550a68a0', city, state)
        )

    return render_template('get_aqi.html', data=False)


@app.route('/news')
def news():
    resp = get_google_news_urls("USA Government and Climate Change", "America")
    return render_template('news.html', articles=resp)


@app.route('/api/<api>')
def get_api(api):
    api = str(api)
    if '.json' in api:
        return jsonify(api)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('_error.html'), 404


if __name__ == '__main__':
    app.run(debug=True)  # CHANGE FOR PRODUCTION

# vercel deploy && vercel --prod
