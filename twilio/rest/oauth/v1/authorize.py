r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class AuthorizeInstance(InstanceResource):
    """
    :ivar redirect_to: The callback URL
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.redirect_to: Optional[str] = payload.get("redirect_to")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.AuthorizeInstance>"


class AuthorizeList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AuthorizeList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/authorize"

    def fetch(
        self,
        response_type: Union[str, object] = values.unset,
        client_id: Union[str, object] = values.unset,
        redirect_uri: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
    ) -> AuthorizeInstance:
        """
        Asynchronously fetch the AuthorizeInstance

        :param response_type: Response Type:param client_id: The Client Identifier:param redirect_uri: The url to which response will be redirected to:param scope: The scope of the access request:param state: An opaque value which can be used to maintain state between the request and callback
        :returns: The fetched AuthorizeInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "ResponseType": response_type,
                "ClientId": client_id,
                "RedirectUri": redirect_uri,
                "Scope": scope,
                "State": state,
            }
        )

        payload = self._version.fetch(
            method="GET", uri=self._uri, headers=headers, params=params
        )

        return AuthorizeInstance(self._version, payload)

    async def fetch_async(
        self,
        response_type: Union[str, object] = values.unset,
        client_id: Union[str, object] = values.unset,
        redirect_uri: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        state: Union[str, object] = values.unset,
    ) -> AuthorizeInstance:
        """
        Asynchronously fetch the AuthorizeInstance

        :param response_type: Response Type:param client_id: The Client Identifier:param redirect_uri: The url to which response will be redirected to:param scope: The scope of the access request:param state: An opaque value which can be used to maintain state between the request and callback
        :returns: The fetched AuthorizeInstance
        """
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        params = values.of(
            {
                "ResponseType": response_type,
                "ClientId": client_id,
                "RedirectUri": redirect_uri,
                "Scope": scope,
                "State": state,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers, params=params
        )

        return AuthorizeInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Oauth.V1.AuthorizeList>"
