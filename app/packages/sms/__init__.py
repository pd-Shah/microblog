from flask import (
    Blueprint,
    abort,
    render_template,
    jsonify,
)
from kavenegar import KavenegarAPI


bp = Blueprint(
        name="sms",
        import_name=__name__,
        template_folder="templates",
        url_prefix="/sms",
    )


@bp.route("/", methods=["GET", ])
def index():
    return render_template("sms/index.html")


@bp.route("/send", methods=["GET", ])
def send():
    try:
        api = KavenegarAPI('706E46722F2B68762F7273766634694A66325A4F4A4A75622F33375346786C57586C706F6A596A697751493D')
        params = {
            'receptor': '09226255415',
            'message': 'SMS WEB BASED API BY @pd',
        }
        response = api.sms_send(params)
        print(response)
    except Exception:
        abort("503")
    else:
        return jsonify(response)
