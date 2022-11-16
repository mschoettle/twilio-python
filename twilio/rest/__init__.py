# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import os
import platform
from twilio import __version__
from twilio.base.exceptions import TwilioException
from twilio.base.obsolete import obsolete_client
from twilio.http.http_client import TwilioHttpClient
from urllib.parse import (
    urlparse,
    urlunparse,
)


class Client(object):
    """ A client for accessing the Twilio API. """

    def __init__(self, username=None, password=None, account_sid=None, region=None,
                 http_client=None, environment=None, edge=None,
                 user_agent_extensions=None):
        """
        Initializes the Twilio Client

        :param str username: Username to authenticate with
        :param str password: Password to authenticate with
        :param str account_sid: Account SID, defaults to Username
        :param str region: Twilio Region to make requests to, defaults to 'us1' if an edge is provided
        :param HttpClient http_client: HttpClient, defaults to TwilioHttpClient
        :param dict environment: Environment to look for auth details, defaults to os.environ
        :param str edge: Twilio Edge to make requests to, defaults to None
        :param list[str] user_agent_extensions: Additions to the user agent string

        :returns: Twilio Client
        :rtype: twilio.rest.Client
        """
        environment = environment or os.environ

        self.username = username or environment.get('TWILIO_ACCOUNT_SID')
        """ :type : str """
        self.password = password or environment.get('TWILIO_AUTH_TOKEN')
        """ :type : str """
        self.account_sid = account_sid or self.username
        """ :type : str """
        self.edge = edge or environment.get('TWILIO_EDGE')
        """ :type : str """
        self.region = region or environment.get('TWILIO_REGION')
        """ :type : str """
        self.user_agent_extensions = user_agent_extensions or []
        """ :type : list[str] """

        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")

        self.auth = (self.username, self.password)
        """ :type : tuple(str, str) """
        self.http_client = http_client or TwilioHttpClient()
        """ :type : HttpClient """

        # Domains
        self._accounts = None
        self._api = None
        self._autopilot = None
        self._chat = None
        self._content = None
        self._conversations = None
        self._events = None
        self._flex_api = None
        self._frontline_api = None
        self._insights = None
        self._ip_messaging = None
        self._lookups = None
        self._media = None
        self._messaging = None
        self._monitor = None
        self._notify = None
        self._numbers = None
        self._oauth = None
        self._preview = None
        self._pricing = None
        self._proxy = None
        self._routes = None
        self._serverless = None
        self._studio = None
        self._sync = None
        self._taskrouter = None
        self._trunking = None
        self._trusthub = None
        self._verify = None
        self._video = None
        self._voice = None
        self._wireless = None
        self._supersim = None
        self._bulkexports = None
        self._microvisor = None

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):
        """
        Makes a request to the Twilio API using the configured http client
        Authentication information is automatically added if none is provided

        :param str method: HTTP Method
        :param str uri: Fully qualified url
        :param dict[str, str] params: Query string parameters
        :param dict[str, str] data: POST body data
        :param dict[str, str] headers: HTTP Headers
        :param tuple(str, str) auth: Authentication
        :param int timeout: Timeout in seconds
        :param bool allow_redirects: Should the client follow redirects

        :returns: Response from the Twilio API
        :rtype: twilio.http.response.Response
        """
        auth = auth or self.auth
        headers = headers or {}

        pkg_version = __version__
        os_name = platform.system()
        os_arch = platform.machine()
        python_version = platform.python_version()
        headers['User-Agent'] = 'twilio-python/{} ({} {}) Python/{}'.format(
            pkg_version,
            os_name,
            os_arch,
            python_version,
        )
        for extension in self.user_agent_extensions:
            headers['User-Agent'] += ' {}'.format(extension)
        headers['X-Twilio-Client'] = 'python-{}'.format(__version__)
        headers['Accept-Charset'] = 'utf-8'

        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        uri = self.get_hostname(uri)

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    def get_hostname(self, uri):
        """
        Determines the proper hostname given edge and region preferences
        via client configuration or uri.

        :param str uri: Fully qualified url

        :returns: The final uri used to make the request
        :rtype: str
        """
        if not self.edge and not self.region:
            return uri

        parsed_url = urlparse(uri)
        pieces = parsed_url.netloc.split('.')
        prefix = pieces[0]
        suffix = '.'.join(pieces[-2:])
        region = None
        edge = None
        if len(pieces) == 4:
            # product.region.twilio.com
            region = pieces[1]
        elif len(pieces) == 5:
            # product.edge.region.twilio.com
            edge = pieces[1]
            region = pieces[2]

        edge = self.edge or edge
        region = self.region or region or (edge and 'us1')

        parsed_url = parsed_url._replace(
            netloc='.'.join([part for part in [prefix, edge, region, suffix] if part])
        )
        return urlunparse(parsed_url)

    @property
    def accounts(self):
        """
        Access the Accounts Twilio Domain

        :returns: Accounts Twilio Domain
        :rtype: twilio.rest.accounts.Accounts
        """
        if self._accounts is None:
            from twilio.rest.accounts import Accounts
            self._accounts = Accounts(self)
        return self._accounts

    @property
    def api(self):
        """
        Access the Api Twilio Domain

        :returns: Api Twilio Domain
        :rtype: twilio.rest.api.Api
        """
        if self._api is None:
            from twilio.rest.api import Api
            self._api = Api(self)
        return self._api

    @property
    def autopilot(self):
        """
        Access the Autopilot Twilio Domain

        :returns: Autopilot Twilio Domain
        :rtype: twilio.rest.autopilot.Autopilot
        """
        if self._autopilot is None:
            from twilio.rest.autopilot import Autopilot
            self._autopilot = Autopilot(self)
        return self._autopilot

    @property
    def chat(self):
        """
        Access the Chat Twilio Domain

        :returns: Chat Twilio Domain
        :rtype: twilio.rest.chat.Chat
        """
        if self._chat is None:
            from twilio.rest.chat import Chat
            self._chat = Chat(self)
        return self._chat

    @property
    def content(self):
        """
        Access the Content Twilio Domain

        :returns: Content Twilio Domain
        :rtype: twilio.rest.content.Content
        """
        if self._content is None:
            from twilio.rest.content import Content
            self._content = Content(self)
        return self._content

    @property
    def conversations(self):
        """
        Access the Conversations Twilio Domain

        :returns: Conversations Twilio Domain
        :rtype: twilio.rest.conversations.Conversations
        """
        if self._conversations is None:
            from twilio.rest.conversations import Conversations
            self._conversations = Conversations(self)
        return self._conversations

    @property
    def events(self):
        """
        Access the Events Twilio Domain

        :returns: Events Twilio Domain
        :rtype: twilio.rest.events.Events
        """
        if self._events is None:
            from twilio.rest.events import Events
            self._events = Events(self)
        return self._events

    @property
    def flex_api(self):
        """
        Access the FlexApi Twilio Domain

        :returns: FlexApi Twilio Domain
        :rtype: twilio.rest.flex_api.FlexApi
        """
        if self._flex_api is None:
            from twilio.rest.flex_api import FlexApi
            self._flex_api = FlexApi(self)
        return self._flex_api

    @property
    def frontline_api(self):
        """
        Access the FrontlineApi Twilio Domain

        :returns: FrontlineApi Twilio Domain
        :rtype: twilio.rest.frontline_api.FrontlineApi
        """
        if self._frontline_api is None:
            from twilio.rest.frontline_api import FrontlineApi
            self._frontline_api = FrontlineApi(self)
        return self._frontline_api

    @property
    def insights(self):
        """
        Access the Insights Twilio Domain

        :returns: Insights Twilio Domain
        :rtype: twilio.rest.insights.Insights
        """
        if self._insights is None:
            from twilio.rest.insights import Insights
            self._insights = Insights(self)
        return self._insights

    @property
    def ip_messaging(self):
        """
        Access the IpMessaging Twilio Domain

        :returns: IpMessaging Twilio Domain
        :rtype: twilio.rest.ip_messaging.IpMessaging
        """
        if self._ip_messaging is None:
            from twilio.rest.ip_messaging import IpMessaging
            self._ip_messaging = IpMessaging(self)
        return self._ip_messaging

    @property
    def lookups(self):
        """
        Access the Lookups Twilio Domain

        :returns: Lookups Twilio Domain
        :rtype: twilio.rest.lookups.Lookups
        """
        if self._lookups is None:
            from twilio.rest.lookups import Lookups
            self._lookups = Lookups(self)
        return self._lookups

    @property
    def media(self):
        """
        Access the Media Twilio Domain

        :returns: Media Twilio Domain
        :rtype: twilio.rest.media.Media
        """
        if self._media is None:
            from twilio.rest.media import Media
            self._media = Media(self)
        return self._media

    @property
    def messaging(self):
        """
        Access the Messaging Twilio Domain

        :returns: Messaging Twilio Domain
        :rtype: twilio.rest.messaging.Messaging
        """
        if self._messaging is None:
            from twilio.rest.messaging import Messaging
            self._messaging = Messaging(self)
        return self._messaging

    @property
    def monitor(self):
        """
        Access the Monitor Twilio Domain

        :returns: Monitor Twilio Domain
        :rtype: twilio.rest.monitor.Monitor
        """
        if self._monitor is None:
            from twilio.rest.monitor import Monitor
            self._monitor = Monitor(self)
        return self._monitor

    @property
    def notify(self):
        """
        Access the Notify Twilio Domain

        :returns: Notify Twilio Domain
        :rtype: twilio.rest.notify.Notify
        """
        if self._notify is None:
            from twilio.rest.notify import Notify
            self._notify = Notify(self)
        return self._notify

    @property
    def numbers(self):
        """
        Access the Numbers Twilio Domain

        :returns: Numbers Twilio Domain
        :rtype: twilio.rest.numbers.Numbers
        """
        if self._numbers is None:
            from twilio.rest.numbers import Numbers
            self._numbers = Numbers(self)
        return self._numbers

    @property
    def oauth(self):
        """
        Access the Oauth Twilio Domain

        :returns: Oauth Twilio Domain
        :rtype: twilio.rest.oauth.Oauth
        """
        if self._oauth is None:
            from twilio.rest.oauth import Oauth
            self._oauth = Oauth(self)
        return self._oauth

    @property
    def preview(self):
        """
        Access the Preview Twilio Domain

        :returns: Preview Twilio Domain
        :rtype: twilio.rest.preview.Preview
        """
        if self._preview is None:
            from twilio.rest.preview import Preview
            self._preview = Preview(self)
        return self._preview

    @property
    def pricing(self):
        """
        Access the Pricing Twilio Domain

        :returns: Pricing Twilio Domain
        :rtype: twilio.rest.pricing.Pricing
        """
        if self._pricing is None:
            from twilio.rest.pricing import Pricing
            self._pricing = Pricing(self)
        return self._pricing

    @property
    def proxy(self):
        """
        Access the Proxy Twilio Domain

        :returns: Proxy Twilio Domain
        :rtype: twilio.rest.proxy.Proxy
        """
        if self._proxy is None:
            from twilio.rest.proxy import Proxy
            self._proxy = Proxy(self)
        return self._proxy

    @property
    def routes(self):
        """
        Access the Routes Twilio Domain

        :returns: Routes Twilio Domain
        :rtype: twilio.rest.routes.Routes
        """
        if self._routes is None:
            from twilio.rest.routes import Routes
            self._routes = Routes(self)
        return self._routes

    @property
    def serverless(self):
        """
        Access the Serverless Twilio Domain

        :returns: Serverless Twilio Domain
        :rtype: twilio.rest.serverless.Serverless
        """
        if self._serverless is None:
            from twilio.rest.serverless import Serverless
            self._serverless = Serverless(self)
        return self._serverless

    @property
    def studio(self):
        """
        Access the Studio Twilio Domain

        :returns: Studio Twilio Domain
        :rtype: twilio.rest.studio.Studio
        """
        if self._studio is None:
            from twilio.rest.studio import Studio
            self._studio = Studio(self)
        return self._studio

    @property
    def sync(self):
        """
        Access the Sync Twilio Domain

        :returns: Sync Twilio Domain
        :rtype: twilio.rest.sync.Sync
        """
        if self._sync is None:
            from twilio.rest.sync import Sync
            self._sync = Sync(self)
        return self._sync

    @property
    def taskrouter(self):
        """
        Access the Taskrouter Twilio Domain

        :returns: Taskrouter Twilio Domain
        :rtype: twilio.rest.taskrouter.Taskrouter
        """
        if self._taskrouter is None:
            from twilio.rest.taskrouter import Taskrouter
            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self):
        """
        Access the Trunking Twilio Domain

        :returns: Trunking Twilio Domain
        :rtype: twilio.rest.trunking.Trunking
        """
        if self._trunking is None:
            from twilio.rest.trunking import Trunking
            self._trunking = Trunking(self)
        return self._trunking

    @property
    def trusthub(self):
        """
        Access the Trusthub Twilio Domain

        :returns: Trusthub Twilio Domain
        :rtype: twilio.rest.trusthub.Trusthub
        """
        if self._trusthub is None:
            from twilio.rest.trusthub import Trusthub
            self._trusthub = Trusthub(self)
        return self._trusthub

    @property
    def verify(self):
        """
        Access the Verify Twilio Domain

        :returns: Verify Twilio Domain
        :rtype: twilio.rest.verify.Verify
        """
        if self._verify is None:
            from twilio.rest.verify import Verify
            self._verify = Verify(self)
        return self._verify

    @property
    def video(self):
        """
        Access the Video Twilio Domain

        :returns: Video Twilio Domain
        :rtype: twilio.rest.video.Video
        """
        if self._video is None:
            from twilio.rest.video import Video
            self._video = Video(self)
        return self._video

    @property
    def voice(self):
        """
        Access the Voice Twilio Domain

        :returns: Voice Twilio Domain
        :rtype: twilio.rest.voice.Voice
        """
        if self._voice is None:
            from twilio.rest.voice import Voice
            self._voice = Voice(self)
        return self._voice

    @property
    def wireless(self):
        """
        Access the Wireless Twilio Domain

        :returns: Wireless Twilio Domain
        :rtype: twilio.rest.wireless.Wireless
        """
        if self._wireless is None:
            from twilio.rest.wireless import Wireless
            self._wireless = Wireless(self)
        return self._wireless

    @property
    def supersim(self):
        """
        Access the Supersim Twilio Domain

        :returns: Supersim Twilio Domain
        :rtype: twilio.rest.supersim.Supersim
        """
        if self._supersim is None:
            from twilio.rest.supersim import Supersim
            self._supersim = Supersim(self)
        return self._supersim

    @property
    def bulkexports(self):
        """
        Access the Bulkexports Twilio Domain

        :returns: Bulkexports Twilio Domain
        :rtype: twilio.rest.bulkexports.Bulkexports
        """
        if self._bulkexports is None:
            from twilio.rest.bulkexports import Bulkexports
            self._bulkexports = Bulkexports(self)
        return self._bulkexports

    @property
    def microvisor(self):
        """
        Access the Microvisor Twilio Domain

        :returns: Microvisor Twilio Domain
        :rtype: twilio.rest.microvisor.Microvisor
        """
        if self._microvisor is None:
            from twilio.rest.microvisor import Microvisor
            self._microvisor = Microvisor(self)
        return self._microvisor

    @property
    def addresses(self):
        """
        :rtype: twilio.rest.api.v2010.account.address.AddressList
        """
        return self.api.account.addresses

    @property
    def applications(self):
        """
        :rtype: twilio.rest.api.v2010.account.application.ApplicationList
        """
        return self.api.account.applications

    @property
    def authorized_connect_apps(self):
        """
        :rtype: twilio.rest.api.v2010.account.authorized_connect_app.AuthorizedConnectAppList
        """
        return self.api.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        """
        :rtype: twilio.rest.api.v2010.account.available_phone_number.AvailablePhoneNumberCountryList
        """
        return self.api.account.available_phone_numbers

    @property
    def balance(self):
        """
        :rtype: twilio.rest.api.v2010.account.balance.BalanceList
        """
        return self.api.account.balance

    @property
    def calls(self):
        """
        :rtype: twilio.rest.api.v2010.account.call.CallList
        """
        return self.api.account.calls

    @property
    def conferences(self):
        """
        :rtype: twilio.rest.api.v2010.account.conference.ConferenceList
        """
        return self.api.account.conferences

    @property
    def connect_apps(self):
        """
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        """
        return self.api.account.connect_apps

    @property
    def incoming_phone_numbers(self):
        """
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.IncomingPhoneNumberList
        """
        return self.api.account.incoming_phone_numbers

    @property
    def keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.key.KeyList
        """
        return self.api.account.keys

    @property
    def messages(self):
        """
        :rtype: twilio.rest.api.v2010.account.message.MessageList
        """
        return self.api.account.messages

    @property
    def new_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.new_key.NewKeyList
        """
        return self.api.account.new_keys

    @property
    def new_signing_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.new_signing_key.NewSigningKeyList
        """
        return self.api.account.new_signing_keys

    @property
    def notifications(self):
        """
        :rtype: twilio.rest.api.v2010.account.notification.NotificationList
        """
        return self.api.account.notifications

    @property
    def outgoing_caller_ids(self):
        """
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdList
        """
        return self.api.account.outgoing_caller_ids

    @property
    def queues(self):
        """
        :rtype: twilio.rest.api.v2010.account.queue.QueueList
        """
        return self.api.account.queues

    @property
    def recordings(self):
        """
        :rtype: twilio.rest.api.v2010.account.recording.RecordingList
        """
        return self.api.account.recordings

    @property
    def signing_keys(self):
        """
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyList
        """
        return self.api.account.signing_keys

    @property
    def sip(self):
        """
        :rtype: twilio.rest.api.v2010.account.sip.SipList
        """
        return self.api.account.sip

    @property
    def short_codes(self):
        """
        :rtype: twilio.rest.api.v2010.account.short_code.ShortCodeList
        """
        return self.api.account.short_codes

    @property
    def tokens(self):
        """
        :rtype: twilio.rest.api.v2010.account.token.TokenList
        """
        return self.api.account.tokens

    @property
    def transcriptions(self):
        """
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionList
        """
        return self.api.account.transcriptions

    @property
    def usage(self):
        """
        :rtype: twilio.rest.api.v2010.account.usage.UsageList
        """
        return self.api.account.usage

    @property
    def validation_requests(self):
        """
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestList
        """
        return self.api.account.validation_requests

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio {}>'.format(self.account_sid)


@obsolete_client
class TwilioClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioRestClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioIpMessagingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioLookupsClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioMonitorClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioPricingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTaskRouterClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTrunkingClient(object):
    """ Dummy client which provides no functionality. Please use
    twilio.rest.Client instead. """

    def __init__(self, *args):
        pass
