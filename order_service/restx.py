import logging

from errors import MissingFilterValueError, MissingFilterParametersError
from order_service.app import MCART_API

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


@MCART_API.errorhandler
def default_error_handler(ex):
    """Default error handler"""
    LOG.error(str(ex))
    return {'message': str(ex)}, getattr(ex, 'code', 500)


@MCART_API.errorhandler(MissingFilterValueError)
def handle_missing_filter_error(ex):
    """Error handler for missing filter errors."""
    LOG.error(str(ex.error))
    return ex.error, ex.status_code


@MCART_API.errorhandler(PermissionError)
def handle_permission_error(ex):
    """Error handler for permission errors."""
    LOG.error(str(ex.error))
    return {'message': "Permission Denied"}, 403


@MCART_API.errorhandler(ValueError)
def handle_value_error(ex):
    """Error handler for value errors."""
    LOG.error(str(ex.error))
    return {'message': ex.message}, 422


@MCART_API.errorhandler(TimeoutError)
def handle_timeout_error(ex):
    """Error handler for timeout errors."""
    LOG.error(str(ex.error))
    return {'message': ex.message}, 502


@MCART_API.errorhandler(MissingFilterParametersError)
def invalid_statement_error_handler(ex):
    """Error handler for invalidate request errors."""
    LOG.error(str(ex.error))
    return {'message': ex.message}, 500
