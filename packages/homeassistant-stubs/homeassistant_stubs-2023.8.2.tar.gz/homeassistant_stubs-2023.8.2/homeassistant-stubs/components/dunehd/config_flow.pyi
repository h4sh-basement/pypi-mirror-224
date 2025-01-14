from .const import DOMAIN as DOMAIN
from homeassistant import config_entries as config_entries, exceptions as exceptions
from homeassistant.const import CONF_HOST as CONF_HOST
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.util.network import is_host_valid as is_host_valid
from typing import Any

class DuneHDConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def init_device(self, host: str) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = ...) -> FlowResult: ...
    def host_already_configured(self, host: str) -> bool: ...

class CannotConnect(exceptions.HomeAssistantError): ...
class AlreadyConfigured(exceptions.HomeAssistantError): ...
