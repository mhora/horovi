"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "horovi"

_ = MessageFactory("horovi")

logger = logging.getLogger("horovi")
