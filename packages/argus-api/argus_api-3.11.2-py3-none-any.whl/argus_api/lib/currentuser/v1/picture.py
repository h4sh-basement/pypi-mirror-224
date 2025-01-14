"""Autogenerated API"""
from argus_api.session import get_session
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from argus_api.session import ArgusAPISession


def update_profile_picture_json(
    image: str = None,
    mimeType: str = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Set current user's profile picture (PUBLIC) (PUBLIC)
    
    :param str image: Image bytes
    :param str mimeType: Image MIME type \=\> Sanitize by regex image\/\(png\|jpe\?g\)
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
    :raises InvalidArgumentsException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/currentuser/v1/picture".format()

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send image if the argument was provided, don't send null values
    if image is not None:
        body.update({"image": image})
    # Only send mimeType if the argument was provided, don't send null values
    if mimeType is not None:
        body.update({"mimeType": mimeType})

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
