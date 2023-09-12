# app/utils/error_handlers.py

import cherrypy

def handle_400_error():
    """
    Handle 400 Bad Request errors.
    """
    cherrypy.response.status = 400
    return {
        "status": 400,
        "message": "Bad Request"
    }

def handle_404_error():
    """
    Handle 404 Not Found errors.
    """
    cherrypy.response.status = 404
    return {
        "status": 404,
        "message": "Resource Not Found"
    }

def handle_403_error():
    """
    Handle 403 Forbidden errors.
    """
    cherrypy.response.status = 403
    return {
        "status": 403,
        "message": "Forbidden"
    }

def handle_500_error():
    """
    Handle 500 Internal Server Error.
    """
    cherrypy.response.status = 500
    return {
        "status": 500,
        "message": "Internal Server Error"
    }

def register_error_handlers():
    """
    Register error handlers for the application.
    """
    cherrypy.config.update({
        'error_page.400': handle_400_error,
        'error_page.404': handle_404_error,
        'error_page.403': handle_403_error,
        'error_page.500': handle_500_error
    })
