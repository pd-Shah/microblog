from os.path import join
from logging.handlers import RotatingFileHandler
from logging import (
    Formatter,
    INFO,
)
from flask import (
    Blueprint,
    render_template,
    current_app,
    flash,
)

bp = Blueprint(
            name="error",
            import_name=__name__,
            url_prefix="/error",
            template_folder="templates"
    )


@bp.app_errorhandler(404)
def page_not_found(error):
    log(404)
    return render_template("error/404.html", error=error), 404


@bp.app_errorhandler(500)
def internal_error(error):
    log(500)
    return render_template("error/500.html", error=error), 500


def log(error, ):
    dir = join(current_app.instance_path, "logs")
    file_handler = RotatingFileHandler(dir, maxBytes=1024, )
    file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    file_handler.setLevel(INFO)
    current_app.logger.addHandler(file_handler)
    current_app.logger.info(error)
