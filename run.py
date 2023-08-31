import cherrypy
from app.views.user_api import UserAPI
from app import initialize_app
from config.settings import SERVER_CONFIG

def run():
    # Initialize the application (e.g., connect to the database, set up services)
    initialize_app()

    # Set up static file serving (if needed)
    static_config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
    }

    # Start the CherryPy application
    cherrypy.tree.mount(UserAPI(), '/', config=static_config)
    cherrypy.config.update(SERVER_CONFIG)
    cherrypy.engine.start()
    cherrypy.engine.block()

if __name__ == '__main__':
    run()
