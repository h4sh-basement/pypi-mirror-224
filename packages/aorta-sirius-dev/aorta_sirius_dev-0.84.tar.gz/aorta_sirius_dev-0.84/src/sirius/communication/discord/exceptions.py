from sirius.exceptions import SiriusException


class DiscordException(SiriusException):
    pass


class DuplicateChannelsFoundException(DiscordException):
    pass


class ServerNotFoundException(DiscordException):
    pass


class DuplicateServersFoundException(DiscordException):
    pass
