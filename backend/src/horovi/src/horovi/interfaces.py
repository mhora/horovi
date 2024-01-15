"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IHoroviLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
