"""Autogenerated API"""
from argus_api.session import get_session
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from argus_api.session import ArgusAPISession


def legacy_radius_authentication(
    requestedAuthorizations: str = None,
    userName: str = None,
    domain: str = None,
    mode: str = None,
    password: str = None,
    tokenCode: str = None,
    state: str = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Initiate a new user session using RADIUS authentication (PUBLIC)
    
    :param list requestedAuthorizations: Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE\_PW\_CHANGE flag set.
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str mode: Authentication mode. Use AUTHENTICATION for normal authentication\, or CHALLENGE to respond to a challenge request
    :param str password: RADIUS static password
    :param str tokenCode: RADIUS token code
    :param str state: When responding to a challenge\, include the encoded state returned by the challenge.
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
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/radius/authenticate".format()

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send requestedAuthorizations if the argument was provided, don't send null values
    if requestedAuthorizations is not None:
        body.update({"requestedAuthorizations": requestedAuthorizations})
    # Only send userName if the argument was provided, don't send null values
    if userName is not None:
        body.update({"userName": userName})
    # Only send domain if the argument was provided, don't send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send mode if the argument was provided, don't send null values
    if mode is not None:
        body.update({"mode": mode})
    # Only send password if the argument was provided, don't send null values
    if password is not None:
        body.update({"password": password})
    # Only send tokenCode if the argument was provided, don't send null values
    if tokenCode is not None:
        body.update({"tokenCode": tokenCode})
    # Only send state if the argument was provided, don't send null values
    if state is not None:
        body.update({"state": state})

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


def radius_authentication(
    requestedAuthorizations: str = None,
    userName: str = None,
    domain: str = None,
    mode: str = None,
    password: str = None,
    tokenCode: str = None,
    state: str = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Initiate a new user session using RADIUS authentication (PUBLIC)
    
    :param list requestedAuthorizations: Allow client to request authorizations as part of the authentication transaction. The client is not guaranteed to get the requested authorizations. The setPassword authorization is only returned if the current user has the FORCE\_PW\_CHANGE flag set.
    :param str userName: Username to authenticate
    :param str domain: User domain
    :param str mode: Authentication mode. Use AUTHENTICATION for normal authentication\, or CHALLENGE to respond to a challenge request
    :param str password: RADIUS static password
    :param str tokenCode: RADIUS token code
    :param str state: When responding to a challenge\, include the encoded state returned by the challenge.
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
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/authentication/v1/radius/authentication".format()

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send requestedAuthorizations if the argument was provided, don't send null values
    if requestedAuthorizations is not None:
        body.update({"requestedAuthorizations": requestedAuthorizations})
    # Only send userName if the argument was provided, don't send null values
    if userName is not None:
        body.update({"userName": userName})
    # Only send domain if the argument was provided, don't send null values
    if domain is not None:
        body.update({"domain": domain})
    # Only send mode if the argument was provided, don't send null values
    if mode is not None:
        body.update({"mode": mode})
    # Only send password if the argument was provided, don't send null values
    if password is not None:
        body.update({"password": password})
    # Only send tokenCode if the argument was provided, don't send null values
    if tokenCode is not None:
        body.update({"tokenCode": tokenCode})
    # Only send state if the argument was provided, don't send null values
    if state is not None:
        body.update({"state": state})

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
