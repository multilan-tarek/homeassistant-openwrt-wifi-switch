from __future__ import annotations
import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import config_validation as cv
from .const import (IFNAME, HOST, USERNAME, PASSWORD, PORT)
import logging


_LOGGER = logging.getLogger(__name__)

DOMAIN = 'openwrt_wifi_switch'

PLATFORM_SCHEMA = vol.Schema(
    {
        vol.Required(IFNAME): cv.string,
        vol.Required(HOST): cv.string,
        vol.Required(USERNAME): cv.string,
        vol.Required(PASSWORD): cv.string,
        vol.Required(PORT): cv.string,
    }
)


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    devices = []
    for device in range(len(config[DOMAIN])):
        devices.append({
            "ifname": config[DOMAIN][device][IFNAME],
            "host": config[DOMAIN][device][HOST],
            "username": config[DOMAIN][device][USERNAME],
            "password": config[DOMAIN][device][PASSWORD],
            "port": config[DOMAIN][device][PORT]
        })

    hass.data[DOMAIN] = {
        "devices": devices
    }
    hass.helpers.discovery.load_platform('switch', DOMAIN, {}, config)

    return True
