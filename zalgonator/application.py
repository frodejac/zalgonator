from flask import Flask

from zalgonator.views import zalgo


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('zalgonator.config.ZalgoConfig')

    with app.app_context():
        app.register_blueprint(zalgo, url_prefix='/zalgo')

        return app