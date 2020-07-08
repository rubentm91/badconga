""" camera """
import logging
from homeassistant.components.camera import PLATFORM_SCHEMA, Camera
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({})

async def async_setup_platform(hass, _, async_add_entities):
    """ async_setup_platform """
    instance = hass.data[DOMAIN]['instance']
    async_add_entities([CongaCamera(instance)])

class CongaCamera(Camera):
    """ CongaCamera """
    def __init__(self, instance):
        super().__init__()
        self.content_type = 'image/png'
        self.instance = instance
        self.instance.on('update_map', self.schedule_update_ha_state)

    @property
    def name(self):
        return 'Conga'

    def camera_image(self):
        return self.instance.map.image
