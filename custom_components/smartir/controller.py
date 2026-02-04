import logging

_LOGGER = logging.getLogger(__name__)


def get_controller(hass, supported_controller, commands_encoding, controller_data, delay):
    """Return the appropriate controller based on controller_data."""
    if controller_data.startswith("remote."):
        return RemoteEntityController(hass, controller_data)
    raise ValueError(f"Unsupported controller_data: {controller_data}")


class RemoteEntityController:
    """Controller that sends commands via a Home Assistant remote entity."""

    def __init__(self, hass, entity_id):
        self.hass = hass
        self.entity_id = entity_id

    async def send(self, command):
        """Send a command via remote.turn_on."""
        await self.hass.services.async_call(
            "remote",
            "turn_on",
            {"entity_id": self.entity_id, "device": command},
            blocking=True,
        )
