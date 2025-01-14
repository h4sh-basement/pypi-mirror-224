"""Autogenerated API"""
from argus_api.session import _legacy_session as session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from argus_api.utils import deprecated_alias
log = logging.getLogger(__name__)


@register_command(
    extending=("pdns", "v3", "record"),
    module=argus_cli_module
)
def submit_pdns_records_bulk(
    records: dict = None,
    ignoreOnFailed: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Submit PassiveDNS records in a bulk operation (INTERNAL)
    
    :param list records: PDNS records for submission.
    :param bool ignoreOnFailed: Set this value for successful response even failures occur while submitting. \(default false\)
    :param json: return the response's body as a ``dict`` parsed from json. ``True`` by
      default. If set to false, the raw ``requests.Response`` object will be returned.
    :param verify: path to a certificate bundle or boolean indicating whether SSL
      verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/pdns/v3/record".format()
    headers = {}

    body = body or {}
    # Only send records if the argument was provided, don't send null values
    if records is not None:
        body.update({"records": records})
    # Only send ignoreOnFailed if the argument was provided, don't send null values
    if ignoreOnFailed is not None:
        body.update({"ignoreOnFailed": ignoreOnFailed})

    query_parameters = {}
    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

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

#: **DEPRECATED** : ``submit_p_d_n_s_records_bulk`` is an alias for ``submit_pdns_records_bulk``. Exists
#: only for backward compatibility - **do not use** - use ``submit_pdns_records_bulk`` instead.
submit_p_d_n_s_records_bulk = register_command(
    extending=("pdns", "v3", "record"),
    module=argus_cli_module,
    alias="submit_p_d_n_s_records_bulk"
)(deprecated_alias("submit_p_d_n_s_records_bulk")(submit_pdns_records_bulk))