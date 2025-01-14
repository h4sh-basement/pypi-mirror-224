"""Autogenerated API"""
from argus_api.session import get_session
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from argus_api.session import ArgusAPISession
from argus_api.utils import deprecated_alias


def prepare_notification(
    customerID: int = None,
    event: str = None,
    recipients: dict = None,
    attachments: dict = None,
    context: dict = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Prepare a new notification (INTERNAL)
    
    :param int customerID: Set the customer context of this notification request. If not set\, it should default to the current users customer.
    :param str event: The name of the notification event to trigger. This will determine notification behaviour and rules.
    :param list recipients: Recipients to notify\, either user or non\-user.
    :param list attachments: Attachments to process in this notification. The notification rules and destinations will determine how these are used.
    :param dict context: The notification context objects. The notification event determines which context objects are expected. Each object should be JSON serializable.
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :param api_session: session to use for this request. If not set, the global session will be used.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/notifications/v1/notification".format()

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send customerID if the argument was provided, don't send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send event if the argument was provided, don't send null values
    if event is not None:
        body.update({"event": event})
    # Only send recipients if the argument was provided, don't send null values
    if recipients is not None:
        body.update({"recipients": recipients})
    # Only send attachments if the argument was provided, don't send null values
    if attachments is not None:
        body.update({"attachments": attachments})
    # Only send context if the argument was provided, don't send null values
    if context is not None:
        body.update({"context": context})

    query_parameters = {}

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response


def send_notification(
    notificationID: str,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Send a pending notification (INTERNAL)
    
    :param str notificationID: Notification ID
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :param api_session: session to use for this request. If not set, the global session will be used.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/notifications/v1/notification/{notificationID}/send".format(notificationID=notificationID)

    session = api_session or get_session()
    headers = {}

    body = body or {}

    query_parameters = {}

    response = session.put(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

#: **DEPRECATED** : ``prepare_notification_1`` is an alias for ``send_notification``. Exists
#: only for backward compatibility - **do not use** - use ``send_notification`` instead.
prepare_notification_1 = deprecated_alias("prepare_notification_1")(send_notification)