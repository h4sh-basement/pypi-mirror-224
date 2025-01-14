"""Autogenerated API"""
from argus_api.session import get_session
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from argus_api.session import ArgusAPISession
from argus_api.utils import deprecated_alias


def add_document_fragment(
    documentID: int,
    idx: int,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Upload next fragment of data to a prepared document.Fragments MUST be uploaded in order, first fragment with index 0. (PUBLIC)
    
    :param int documentID: Document ID \(as returned from the prepare endpoint\)
    :param int idx: Fragment index
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
    :raises SpecifiedDocumentIdDoesNotExistException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/documents/v1/upload/{documentID}/fragment/{idx}".format(documentID=documentID,
        idx=idx)

    session = api_session or get_session()
    headers = {}

    body = body or {}

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


def complete_document_upload(
    documentID: int,
    sha256: str = None,
    notificationOptions: dict = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Finalize upload of document.Completion request must specify correct checksum and document size. (PUBLIC)
    
    :param int documentID: Document ID \(as returned from the prepare endpoint\)
    :param str sha256: The sha256 of the entire document.
    :param dict notificationOptions: 
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
    :raises SpecifiedDocumentIdDoesNotExistException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/documents/v1/upload/{documentID}/complete".format(documentID=documentID)

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send documentID if the argument was provided, don't send null values
    if documentID is not None:
        body.update({"documentID": documentID})
    # Only send sha256 if the argument was provided, don't send null values
    if sha256 is not None:
        body.update({"sha256": sha256})
    # Only send notificationOptions if the argument was provided, don't send null values
    if notificationOptions is not None:
        body.update({"notificationOptions": notificationOptions})

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


def discard_document_upload(
    documentID: int,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Abort and discard fragmented upload. (PUBLIC)
    
    :param int documentID: Document ID \(as returned from the prepare endpoint\)
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
    :raises SpecifiedDocumentIdDoesNotExistException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/documents/v1/upload/{documentID}".format(documentID=documentID)

    session = api_session or get_session()
    headers = {}

    body = body or {}

    query_parameters = {}

    response = session.delete(
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


def prepare_upload(
    parentFolderID: int = None,
    name: str = None,
    mimeType: str = None,
    accessMode: str = None,
    overwriteExisting: bool = None,
    lockRequestTime: int = None,
    inheritExplicitPermissions: bool = None,
    json: bool = True,
    verify: Optional[bool] = None,
    proxies: Optional[dict] = None,
    apiKey: Optional[str] = None,
    authentication: Optional[dict] = None,
    server_url: Optional[str] = None,
    body: Optional[dict] = None,
    api_session: Optional["ArgusAPISession"] = None,
) -> dict:
    """Prepare upload of a new document (PUBLIC)
    
    :param int parentFolderID: The ID of the parent folder to upload into
    :param str name: Name of new document \=\> Sanitize by regex \\A\[\^\\\\\\\/\:\*\"\'\?\<\>\|\]\{1\,254\}\\z
    :param str mimeType: MIME type of document content
    :param str accessMode: General access mode of new document \(default roleBased\)
    :param bool overwriteExisting: If true\, overwrite existing document with same name in parent folder\, as a new revision.
    :param int lockRequestTime: Specify how long the document should be locked \(default 0\)
    :param bool inheritExplicitPermissions: Inherit explicit permissions from parent folder \(default false\)
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
    :raises ParentFolderNotFoundException: on 404
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: dictionary translated from JSON
    """

    route = "/documents/v1/upload/prepare".format()

    session = api_session or get_session()
    headers = {}

    body = body or {}
    # Only send parentFolderID if the argument was provided, don't send null values
    if parentFolderID is not None:
        body.update({"parentFolderID": parentFolderID})
    # Only send name if the argument was provided, don't send null values
    if name is not None:
        body.update({"name": name})
    # Only send mimeType if the argument was provided, don't send null values
    if mimeType is not None:
        body.update({"mimeType": mimeType})
    # Only send accessMode if the argument was provided, don't send null values
    if accessMode is not None:
        body.update({"accessMode": accessMode})
    # Only send lockRequestTime if the argument was provided, don't send null values
    if lockRequestTime is not None:
        body.update({"lockRequestTime": lockRequestTime})
    # Only send inheritExplicitPermissions if the argument was provided, don't send null values
    if inheritExplicitPermissions is not None:
        body.update({"inheritExplicitPermissions": inheritExplicitPermissions})
    # Only send overwriteExisting if the argument was provided, don't send null values
    if overwriteExisting is not None:
        body.update({"overwriteExisting": overwriteExisting})

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

#: **DEPRECATED** : ``disard_document_upload`` is an alias for ``discard_document_upload``. Exists
#: only for backward compatibility - **do not use** - use ``discard_document_upload`` instead.
disard_document_upload = deprecated_alias("disard_document_upload")(discard_document_upload)