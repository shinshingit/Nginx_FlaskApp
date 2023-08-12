from flask import Blueprint,render_template


app_a = Blueprint("app_a", __name__, template_folder="templates", static_folder="static")

# メインのエンドポイント生成
@app_a.route("/")
def main():
    return render_template("app_a/main.html")