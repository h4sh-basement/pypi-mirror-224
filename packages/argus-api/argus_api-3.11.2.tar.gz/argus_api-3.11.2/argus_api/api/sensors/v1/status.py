"""Autogenerated API"""
from argus_api.session import _legacy_session as session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from argus_api.utils import deprecated_alias
log = logging.getLogger(__name__)


@register_command(
    extending=("sensors", "v1", "status"),
    module=argus_cli_module
)
def get_sensor_status_by_status(
    id: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Fetch sensor status by ID (INTERNAL)
    
    :param int id: ID of sensor to fetch status for
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
    :raises ObjectNotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/sensors/v1/status/{id}".format(id=id)
    headers = {}

    body = body or {}

    query_parameters = {}
    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("sensors", "v1", "status"),
    module=argus_cli_module
)
def list_sensor_status(
    customerID: int = None,
    applicationName: str = None,
    keywords: str = None,
    offset: int = None,
    limit: int = 25,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """List sensor status (INTERNAL)
    
    :param list customerID: Limit search to these customer IDs
    :param list applicationName: Limit search to these applications by name
    :param list keywords: Limit search by sensor hostname or IP address
    :param int offset: Offset results
    :param int limit: Limit results
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
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/sensors/v1/status".format(limit=limit,
        customerID=customerID,
        applicationName=applicationName,
        keywords=keywords,
        offset=offset)
    headers = {}

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, don't send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    
    # Only send customerID if the argument was provided, don't send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})
    
    # Only send applicationName if the argument was provided, don't send null values
    if applicationName is not None:
        query_parameters.update({"applicationName": applicationName})
    
    # Only send keywords if the argument was provided, don't send null values
    if keywords is not None:
        query_parameters.update({"keywords": keywords})
    
    # Only send offset if the argument was provided, don't send null values
    if offset is not None:
        query_parameters.update({"offset": offset})
    
    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

@register_command(
    extending=("sensors", "v1", "status"),
    module=argus_cli_module
)
def search_sensor_status(
    limit: int = None,
    offset: int = None,
    includeDeleted: bool = None,
    customerID: int = None,
    keywords: str = None,
    keywordMatchStrategy: str = None,
    keywordFieldStrategy: str = None,
    customer: str = None,
    excludeReportingSensors: bool = None,
    excludeSensorsInScheduledDowntime: bool = None,
    excludeSensorsInReportingCluster: bool = None,
    lastAgentHost: str = None,
    startTimestamp: int = None,
    endTimestamp: int = None,
    sortBy: str = None,
    includeFlags: str = None,
    excludeFlags: str = None,
    sensorID: int = None,
    locationName: str = None,
    applicationName: str = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
) -> dict:
    """Search sensor status (INTERNAL)
    
    :param int limit: Limit results
    :param int offset: Offset results
    :param bool includeDeleted: Also include deleted objects \(where implemented\)
    :param list customerID: Limit result to objects belonging to these customers
    :param list keywords: Search for sensors matching these hostnames or IP\-addresses
    :param str keywordMatchStrategy: Defines how strictly different keywords should be matched \(default match any keywords\) \(default any\)
    :param list keywordFieldStrategy: Defines which fields will be searched by keywords \(defaults to all supported fields\) \(default all\)
    :param list customer: Search for sensors belonging to customers identified by their ID or shortname
    :param bool excludeReportingSensors: DEPRECATED\: Use exclude flags
    :param bool excludeSensorsInScheduledDowntime: DEPRECATED\: Use exclude flags
    :param bool excludeSensorsInReportingCluster: DEPRECATED\: Use exclude flags
    :param str lastAgentHost: Include sensors where lastAgentHost matches this string \(entire\/partial\)
    :param int startTimestamp: Search objects from this timestamp
    :param int endTimestamp: Search objects until this timestamp
    :param list sortBy: Order results by these properties \(prefix with \- to sort descending\)
    :param list includeFlags: Search objects with these flags set
    :param list excludeFlags: Exclude objects with these flags set
    :param list sensorID: Search for specific sensors by ID
    :param list locationName: Search for sensors bound to any of these locations
    :param list applicationName: Search for sensors by application type
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
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/sensors/v1/status/search".format()
    headers = {}

    body = body or {}
    # Only send limit if the argument was provided, don't send null values
    if limit is not None:
        body.update({"limit": limit})
    # Only send offset if the argument was provided, don't send null values
    if offset is not None:
        body.update({"offset": offset})
    # Only send includeDeleted if the argument was provided, don't send null values
    if includeDeleted is not None:
        body.update({"includeDeleted": includeDeleted})
    # Only send customerID if the argument was provided, don't send null values
    if customerID is not None:
        body.update({"customerID": customerID})
    # Only send keywords if the argument was provided, don't send null values
    if keywords is not None:
        body.update({"keywords": keywords})
    # Only send keywordMatchStrategy if the argument was provided, don't send null values
    if keywordMatchStrategy is not None:
        body.update({"keywordMatchStrategy": keywordMatchStrategy})
    # Only send keywordFieldStrategy if the argument was provided, don't send null values
    if keywordFieldStrategy is not None:
        body.update({"keywordFieldStrategy": keywordFieldStrategy})
    # Only send customer if the argument was provided, don't send null values
    if customer is not None:
        body.update({"customer": customer})
    # Only send excludeReportingSensors if the argument was provided, don't send null values
    if excludeReportingSensors is not None:
        body.update({"excludeReportingSensors": excludeReportingSensors})
    # Only send excludeSensorsInScheduledDowntime if the argument was provided, don't send null values
    if excludeSensorsInScheduledDowntime is not None:
        body.update({"excludeSensorsInScheduledDowntime": excludeSensorsInScheduledDowntime})
    # Only send excludeSensorsInReportingCluster if the argument was provided, don't send null values
    if excludeSensorsInReportingCluster is not None:
        body.update({"excludeSensorsInReportingCluster": excludeSensorsInReportingCluster})
    # Only send lastAgentHost if the argument was provided, don't send null values
    if lastAgentHost is not None:
        body.update({"lastAgentHost": lastAgentHost})
    # Only send startTimestamp if the argument was provided, don't send null values
    if startTimestamp is not None:
        body.update({"startTimestamp": startTimestamp})
    # Only send endTimestamp if the argument was provided, don't send null values
    if endTimestamp is not None:
        body.update({"endTimestamp": endTimestamp})
    # Only send sortBy if the argument was provided, don't send null values
    if sortBy is not None:
        body.update({"sortBy": sortBy})
    # Only send includeFlags if the argument was provided, don't send null values
    if includeFlags is not None:
        body.update({"includeFlags": includeFlags})
    # Only send excludeFlags if the argument was provided, don't send null values
    if excludeFlags is not None:
        body.update({"excludeFlags": excludeFlags})
    # Only send sensorID if the argument was provided, don't send null values
    if sensorID is not None:
        body.update({"sensorID": sensorID})
    # Only send locationName if the argument was provided, don't send null values
    if locationName is not None:
        body.update({"locationName": locationName})
    # Only send applicationName if the argument was provided, don't send null values
    if applicationName is not None:
        body.update({"applicationName": applicationName})

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

#: **DEPRECATED** : ``list_sensors`` is an alias for ``list_sensor_status``. Exists
#: only for backward compatibility - **do not use** - use ``list_sensor_status`` instead.
list_sensors = register_command(
    extending=("sensors", "v1", "status"),
    module=argus_cli_module,
    alias="list_sensors"
)(deprecated_alias("list_sensors")(list_sensor_status))
#: **DEPRECATED** : ``find_sensors`` is an alias for ``search_sensor_status``. Exists
#: only for backward compatibility - **do not use** - use ``search_sensor_status`` instead.
find_sensors = register_command(
    extending=("sensors", "v1", "status"),
    module=argus_cli_module,
    alias="find_sensors"
)(deprecated_alias("find_sensors")(search_sensor_status))