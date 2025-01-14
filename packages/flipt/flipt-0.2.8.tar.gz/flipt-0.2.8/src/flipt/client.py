# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FliptApiEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.auth_method_k_8_s.client import AsyncAuthMethodK8SClient, AuthMethodK8SClient
from .resources.auth_method_oidc.client import AsyncAuthMethodOidcClient, AuthMethodOidcClient
from .resources.auth_method_token.client import AsyncAuthMethodTokenClient, AuthMethodTokenClient
from .resources.constraints.client import AsyncConstraintsClient, ConstraintsClient
from .resources.distributions.client import AsyncDistributionsClient, DistributionsClient
from .resources.evaluate.client import AsyncEvaluateClient, EvaluateClient
from .resources.evaluation.client import AsyncEvaluationClient, EvaluationClient
from .resources.flags.client import AsyncFlagsClient, FlagsClient
from .resources.namespaces.client import AsyncNamespacesClient, NamespacesClient
from .resources.rollouts.client import AsyncRolloutsClient, RolloutsClient
from .resources.rules.client import AsyncRulesClient, RulesClient
from .resources.segments.client import AsyncSegmentsClient, SegmentsClient
from .resources.variants.client import AsyncVariantsClient, VariantsClient


class FliptApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            token=token,
            httpx_client=httpx.Client(timeout=timeout),
        )
        self.evaluation = EvaluationClient(client_wrapper=self._client_wrapper)
        self.auth_method_k_8_s = AuthMethodK8SClient(client_wrapper=self._client_wrapper)
        self.auth_method_oidc = AuthMethodOidcClient(client_wrapper=self._client_wrapper)
        self.auth_method_token = AuthMethodTokenClient(client_wrapper=self._client_wrapper)
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.constraints = ConstraintsClient(client_wrapper=self._client_wrapper)
        self.distributions = DistributionsClient(client_wrapper=self._client_wrapper)
        self.evaluate = EvaluateClient(client_wrapper=self._client_wrapper)
        self.flags = FlagsClient(client_wrapper=self._client_wrapper)
        self.namespaces = NamespacesClient(client_wrapper=self._client_wrapper)
        self.rollouts = RolloutsClient(client_wrapper=self._client_wrapper)
        self.rules = RulesClient(client_wrapper=self._client_wrapper)
        self.segments = SegmentsClient(client_wrapper=self._client_wrapper)
        self.variants = VariantsClient(client_wrapper=self._client_wrapper)


class AsyncFliptApi:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FliptApiEnvironment = FliptApiEnvironment.PRODUCTION,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60
    ):
        if base_url is None and environment is None:
            raise Exception("Please pass in either base_url or environment to construct the client")
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url if base_url is not None else environment.value,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout),
        )
        self.evaluation = AsyncEvaluationClient(client_wrapper=self._client_wrapper)
        self.auth_method_k_8_s = AsyncAuthMethodK8SClient(client_wrapper=self._client_wrapper)
        self.auth_method_oidc = AsyncAuthMethodOidcClient(client_wrapper=self._client_wrapper)
        self.auth_method_token = AsyncAuthMethodTokenClient(client_wrapper=self._client_wrapper)
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.constraints = AsyncConstraintsClient(client_wrapper=self._client_wrapper)
        self.distributions = AsyncDistributionsClient(client_wrapper=self._client_wrapper)
        self.evaluate = AsyncEvaluateClient(client_wrapper=self._client_wrapper)
        self.flags = AsyncFlagsClient(client_wrapper=self._client_wrapper)
        self.namespaces = AsyncNamespacesClient(client_wrapper=self._client_wrapper)
        self.rollouts = AsyncRolloutsClient(client_wrapper=self._client_wrapper)
        self.rules = AsyncRulesClient(client_wrapper=self._client_wrapper)
        self.segments = AsyncSegmentsClient(client_wrapper=self._client_wrapper)
        self.variants = AsyncVariantsClient(client_wrapper=self._client_wrapper)
