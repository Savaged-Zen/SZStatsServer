from szstats.database import DBSession, init_database
from szstats.resources import Root
from pyramid.config import Configurator
from sqlalchemy.engine import engine_from_config


class SessionMiddleware(object):
    """
    Ensure the session is winning in the event of exceptions
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        session = DBSession()
        try:
            return self.app(*args, **kwargs)
        except:
            session.rollback()
            raise
        finally:
            session.close()
            DBSession.remove()

def main(global_config, **settings):
    # Setup engine
    engine = engine_from_config(settings, 'sqlalchemy.')
    init_database(engine)

    # App Config
    config = Configurator(root_factory=Root, settings=settings)
    config.add_static_view('static', 'szstats:static')
    config.scan('szstats.views')

    # Wrap the app in the SessionMiddleware
    app = SessionMiddleware(config.make_wsgi_app())

    return app
