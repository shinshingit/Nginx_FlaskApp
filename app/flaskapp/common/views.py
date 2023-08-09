from flask import Blueprint,render_template


common = Blueprint("common", __name__, template_folder="templates", static_folder="static")

# メインのエンドポイント生成
@common.route("/")
def main():
    #return "Hello from common"
    return render_template("common/main.html")