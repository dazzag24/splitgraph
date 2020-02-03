"""
Exceptions that can be raised by the Splitgraph library.
"""
from typing import List, Optional


class SplitGraphError(Exception):
    """A generic Splitgraph exception."""


class CheckoutError(SplitGraphError):
    """Errors related to checking out/committing repositories"""


class UnsupportedSQLError(SplitGraphError):
    """Raised for unsupported SQL statements, for example, containing schema-qualified tables when the statement
    is supposed to be used in an SQL/IMPORT Splitfile command."""


class EngineInitializationError(SplitGraphError):
    """Raised when the engine isn't initialized (no splitgraph_meta schema or audit triggers)"""


class ObjectCacheError(SplitGraphError):
    """Issues with the object cache (not enough space)"""


class ObjectNotFoundError(SplitGraphError):
    """Raised when a physical object doesn't exist in the cache."""


class ObjectIndexingError(SplitGraphError):
    """Errors related to indexing objects"""


class RepositoryNotFoundError(SplitGraphError):
    """A Splitgraph repository doesn't exist."""


class ImageNotFoundError(SplitGraphError):
    """A Splitgraph image doesn't exist."""


class TableNotFoundError(SplitGraphError):
    """A table doesn't exist in an image"""


class SplitfileError(SplitGraphError):
    """Generic error class for Splitfile interpretation/execution errors."""


class ExternalHandlerError(SplitGraphError):
    """Exceptions raised by external object handlers."""


class MountHandlerError(SplitGraphError):
    """Exceptions raised by mount handlers."""


class AuthAPIError(SplitGraphError):
    """Exceptions raised by the Auth API"""


class IncompleteObjectTransferError(SplitGraphError):
    """Raised when an error is encountered during upload/download
    of multiple objects. The handler is supposed to perform any necessary
    cleanup and reraise `reason` at the earliest opportunity."""

    def __init__(
        self,
        reason: Optional[BaseException],
        successful_objects: List[str],
        successful_object_urls: Optional[List[str]] = None,
    ):
        self.reason = reason
        self.successful_objects = successful_objects
        self.successful_object_urls = successful_object_urls
