import aiohttp
import dataclasses
import os
import typing

from py_obs.logger import LOGGER


class ObsException(aiohttp.ClientResponseError):
    def __str__(self) -> str:
        return (
            f"Error talking to OBS: {self.status=}, {self.message=},"
            f"{self.request_info=}"
        )


@dataclasses.dataclass
class Osc:
    username: str
    password: str

    api_url: str = "https://api.opensuse.org/"

    _session: aiohttp.ClientSession = dataclasses.field(
        default_factory=lambda: aiohttp.ClientSession()
    )

    @staticmethod
    def from_env() -> "Osc":
        if not (username := os.getenv("OSC_USER")):
            raise ValueError("environment variable OSC_USER is not set")
        if not (password := os.getenv("OSC_PASSWORD")):
            raise ValueError("environment variable OSC_PASSWORD is not set")
        return Osc(username=username, password=password)

    async def api_request(
        self,
        route: str,
        payload: bytes | str | None = None,
        params: dict[str, str] | None = None,
        method: typing.Literal["GET", "POST", "PUT", "DELETE"] = "GET",
    ) -> aiohttp.ClientResponse:
        LOGGER.debug(
            "Sending a %s request to %s with the parameters %s and the payload %s",
            method,
            route,
            params,
            payload,
        )
        try:
            return await self._session.request(
                method=method, params=params, url=route, data=payload
            )
        except aiohttp.ClientResponseError as cre_exc:
            raise ObsException(**cre_exc.__dict__) from cre_exc

    def __post_init__(self) -> None:
        self._session = aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(login=self.username, password=self.password),
            raise_for_status=True,
            base_url=self.api_url,
            # https://github.com/openSUSE/open-build-service/issues/13737
            headers={"Accept": "application/xml; charset=utf-8"},
        )

    async def teardown(self) -> None:
        await self._session.close()
