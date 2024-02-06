class MissingParamInDynamo(Exception):
    """Parameter error exception."""

    def __init__(self, error, status_code):
        """Initializes RoleAuthError."""
        super(MissingParamInDynamo, self).__init__(error)
        self.error = error
        self.status_code = status_code


class MissingS3FileError(Exception):
    """Role authorization error exception."""

    def __init__(self, error, status_code):
        """Initializes RoleAuthError."""
        super(MissingS3FileError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class MissingFilterParametersError(Exception):
    """Invalid market error exception."""

    def __init__(self, error, status_code):
        """Initializes InvalidMarketError."""
        super(MissingFilterParametersError, self).__init__(error)
        self.error = error
        self.status_code = status_code


class MissingFilterValueError(Exception):
    """Missing filter value error exception."""

    def __init__(self, error, status_code):
        """Initializes MissingFilterValueError."""
        super(MissingFilterValueError, self).__init__(error)
        self.error = error
        self.status_code = status_code
