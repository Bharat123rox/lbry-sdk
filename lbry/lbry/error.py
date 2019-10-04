class BaseLBRYException(Exception):
    pass


class UnknownAPIMethodError(BaseLBRYException):
    pass


class RPCError(BaseLBRYException):
    code = 0


class PriceDisagreementError(BaseLBRYException):
    pass


class DuplicateStreamHashError(BaseLBRYException):
    pass


class DownloadCancelledError(BaseLBRYException):
    pass


class DownloadSDTimeout(BaseLBRYException):
    def __init__(self, download):
        super().__init__(f'Failed to download sd blob {download} within timeout')
        self.download = download


class DownloadTimeoutError(BaseLBRYException):
    def __init__(self, download):
        super().__init__(f'Failed to download {download} within timeout')
        self.download = download


class DownloadDataTimeout(BaseLBRYException):
    def __init__(self, download):
        super().__init__(f'Failed to download data blobs for sd hash {download} within timeout')
        self.download = download


class ResolveTimeout(BaseLBRYException):
    def __init__(self, uri):
        super().__init__(f'Failed to resolve "{uri}" within the timeout')
        self.uri = uri


class RequestCanceledError(BaseLBRYException):
    pass


class NegativeFundsError(BaseLBRYException):
    pass


class NullFundsError(BaseLBRYException):
    pass


class InsufficientFundsError(RPCError):
    code = -310


class CurrencyConversionError(BaseLBRYException):
    pass


class FileOpenError(BaseLBRYException):
    # this extends ValueError because it is replacing a ValueError in EncryptedFileDownloader
    # and I don't know where it might get caught upstream
    pass


class ResolveError(BaseLBRYException):
    pass


class ConnectionClosedBeforeResponseError(BaseLBRYException):
    pass


class KeyFeeAboveMaxAllowed(BaseLBRYException):
    pass


class InvalidExchangeRateResponse(BaseLBRYException):
    def __init__(self, source, reason):
        super().__init__(f'Failed to get exchange rate from {source}:{reason}')
        self.source = source
        self.reason = reason


class UnknownNameError(BaseLBRYException):
    def __init__(self, name):
        super().__init__(f'Name {name} is unknown')
        self.name = name


class UnknownClaimID(BaseLBRYException):
    def __init__(self, claim_id):
        super().__init__(f'Claim {claim_id} is unknown')
        self.claim_id = claim_id


class UnknownURI(BaseLBRYException):
    def __init__(self, uri):
        super().__init__(f'URI {uri} cannot be resolved')
        self.name = uri


class UnknownOutpoint(BaseLBRYException):
    def __init__(self, outpoint):
        super().__init__(f'Outpoint {outpoint} cannot be resolved')
        self.outpoint = outpoint


class InvalidName(BaseLBRYException):
    def __init__(self, name, invalid_characters):
        self.name = name
        self.invalid_characters = invalid_characters
        super().__init__(
            'URI contains invalid characters: {}'.format(','.join(invalid_characters)))


class UnknownStreamTypeError(BaseLBRYException):
    def __init__(self, stream_type):
        self.stream_type = stream_type

    def __str__(self):
        return repr(self.stream_type)


class InvalidStreamDescriptorError(BaseLBRYException):
    pass


class InvalidStreamInfoError(BaseLBRYException):
    def __init__(self, name, stream_info):
        msg = f'{name} has claim with invalid stream info: {stream_info}'
        super().__init__(msg)
        self.name = name
        self.stream_info = stream_info


class MisbehavingPeerError(BaseLBRYException):
    pass


class InvalidDataError(MisbehavingPeerError):
    pass


class NoResponseError(MisbehavingPeerError):
    pass


class InvalidResponseError(MisbehavingPeerError):
    pass


class NoSuchBlobError(BaseLBRYException):
    pass


class NoSuchStreamHash(BaseLBRYException):
    pass


class NoSuchSDHash(BaseLBRYException):
    """
    Raised if sd hash is not known
    """


class InvalidBlobHashError(BaseLBRYException):
    pass


class InvalidHeaderError(BaseLBRYException):
    pass


class InvalidAuthenticationToken(BaseLBRYException):
    pass


class NegotiationError(BaseLBRYException):
    pass


class InvalidCurrencyError(BaseLBRYException):
    def __init__(self, currency):
        self.currency = currency
        super().__init__(
            f'Invalid currency: {currency} is not a supported currency.')


class NoSuchDirectoryError(BaseLBRYException):
    def __init__(self, directory):
        self.directory = directory
        super().__init__(f'No such directory {directory}')


class ComponentStartConditionNotMet(BaseLBRYException):
    pass


class ComponentsNotStarted(BaseLBRYException):
    pass
