from lbry.error import BaseLBRYException


class BaseKademliaException(BaseLBRYException):
    pass


class DecodeError(BaseKademliaException):
    """
    Should be raised by an C{Encoding} implementation if decode operation
    fails
    """


class BucketFullError(BaseKademliaException):
    """
    Raised when the bucket is full
    """


class RemoteException(BaseKademliaException):
    pass


class TransportNotConnectedError(BaseKademliaException):
    pass
