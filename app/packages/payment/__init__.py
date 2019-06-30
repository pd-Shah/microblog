from flask import (
    Blueprint,
    render_template,
    abort,
    request,
    url_for,
    flash,
    redirect,
    jsonify,
)
from .paydotir import PayDotIR


bp = Blueprint(name="payment",
               import_name=__name__,
               template_folder="templates",
               url_prefix="/payment", )


@bp.route("/", methods=["GET", ], )
def index():
    return render_template("payment/index.html")


@bp.route("/go", methods=["GET", ], )
def payment_info():
    pay = PayDotIR(
            api="test",
            amount=1000,
            redirect=url_for("payment.payment_check", _external=True)
        )
    res = pay.start()
    if res["status"] == 1:
        res = pay.do_payment(res["token"])
        if res["status_code"] == 200:
            return redirect(res["url"])
    return abort(503)


@bp.route("/check", methods=["GET"])
def payment_check():
    if int(request.args["status"]) == 1:
        resp = PayDotIR.check(request.args["token"])
        if int(resp["status"]) == 1:
            # TODO: check unique transId
            return "successfull"
    return abort(503)
