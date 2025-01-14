class LinesException(Exception):
    """Base exception class for atomiclines library."""


class LinesTimeoutError(LinesException):
    """Timeout exception.

    Stores the timeout in seconds which elapsed.
    """

    def __init__(self, timeout: float) -> None:
        """Initialize new timeout exception.

        Args:
            timeout: timeout in seconds.
        """
        self._timeout = timeout
        super().__init__(timeout)

    @property
    def timeout(self):
        """Timeout as a read only property.

        Returns:
            timeout in seconds.
        """
        return self._timeout

    def __str__(self) -> str:
        """Generate String representation.

        Returns:
            string representation.
        """
        return f"Timeout of {self.timeout} seconds expired."
