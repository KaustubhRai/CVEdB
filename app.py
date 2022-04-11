from flask import Flask, render_template, request
from flask.wrappers import Request
from capec_print import cve_info_print, vulnerable_product_print, capec_print
from exploit_link import exploit_id
from exploit_code import exploit_code
from exploit_price import vulrul
from screenshot_testing import cvss_screenshot

app = Flask(__name__)

# index page function and routing


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# cve id page function and routing


@app.route('/data', methods=['GET', 'POST'])
def cve():
    if request.method == 'POST':
        cve = request.form.get("search")
        print(cve)
        return render_template('cve.html', cve_id_number=cve, cve_info=cve_info_print(cve), vulnerable_product=vulnerable_product_print(cve), capec=capec_print(cve), exploit_links_list=exploit_id(cve), exploit_code_return=exploit_code(cve), exploit_price_return=vulrul(cve), screenshot=cvss_screenshot(cve))


@ app.route('/hello')
def hello():
    return 'Hello, World!'


@ app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
