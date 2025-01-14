from .const import ATTR_CID as ATTR_CID, ATTR_MAC as ATTR_MAC, ATTR_MODEL as ATTR_MODEL, CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_NICKNAME as CONF_NICKNAME, CONF_USE_PSK as CONF_USE_PSK, DOMAIN as DOMAIN, NICKNAME_PREFIX as NICKNAME_PREFIX
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant import config_entries as config_entries
from homeassistant.components import ssdp as ssdp
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MAC as CONF_MAC, CONF_NAME as CONF_NAME, CONF_PIN as CONF_PIN
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import instance_id as instance_id
from homeassistant.helpers.aiohttp_client import async_create_clientsession as async_create_clientsession
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

class BraviaTVConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    client: Incomplete
    device_config: Incomplete
    entry: Incomplete
    def __init__(self) -> None: ...
    def create_client(self) -> None: ...
    async def gen_instance_ids(self) -> tuple[str, str]: ...
    async def async_connect_device(self) -> None: ...
    async def async_create_device(self) -> FlowResult: ...
    async def async_reauth_device(self) -> FlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_authorize(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_pin(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_psk(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_ssdp(self, discovery_info: ssdp.SsdpServiceInfo) -> FlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> FlowResult: ...
