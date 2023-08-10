from flask import Flask,render_template


app = Flask(__name__)


# Blueprint設定
from common import views as common_views
from app_A import views as app_A_views

# register_blueprintを使いviewsのcalc_in_clntをアプリへ登録する
app.register_blueprint(common_views.common, url_prefix="/common")
app.register_blueprint(app_A_views.app_a, url_prefix="/app_a")



@app.route('/')
def hello_flask():
    return "Hello Flask with Docker🐋"
