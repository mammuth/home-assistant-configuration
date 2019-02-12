import logging

DOMAIN = 'fritzbox_guestwifi'
REQUIREMENTS = ['fritzconnection==0.6.5']
_LOGGER = logging.getLogger(__name__)


def setup(hass, config):
    _LOGGER.debug('Setting up GuestWifi Component')
    host = config[DOMAIN].get('host', '169.254.1.1')
    port = config[DOMAIN].get('port', 49000)
    username = config[DOMAIN].get('username', '')
    password = config[DOMAIN].get('password', None)

    if not password:
        raise ValueError('Password is not set in configuration')

    guest_wifi = FritzBoxGuestWifi(
        host=host,
        port=port,
        username=username,
        password=password
    )

    hass.services.register(DOMAIN, 'turn_on', guest_wifi.turn_on)
    hass.services.register(DOMAIN, 'turn_off', guest_wifi.turn_off)
    hass.services.register(DOMAIN, 'reconnect', guest_wifi.reconnect_fritzbox)
    return True


class FritzBoxGuestWifi(object):

    def __init__(self, host, port, username, password):
        # pylint: disable=import-error
        import fritzconnection as fc
        self._connection = fc.FritzConnection(
            address=host,
            port=port,
            user=username,
            password=password
        )

    def reconnect_fritzbox(self, call):
        _LOGGER.info('Reconnecting the fritzbox.')
        self._connection.reconnect()

    def turn_on(self, call):
        _LOGGER.info('Turning on guest wifi.')
        self._handle_turn_on_off(True)

    def turn_off(self, call):
        _LOGGER.info('Turning off guest wifi.')
        self._handle_turn_on_off(False)

    def _handle_turn_on_off(self, turn_on):
        from fritzconnection.fritzconnection import ServiceError, ActionError
        new_state = '1' if turn_on else '0'
        try:
            self._connection.call_action('WLANConfiguration:3', 'SetEnable', NewEnable=new_state)
        except ServiceError or ActionError:
            _LOGGER.error('Home Assistant cannot call the wished service on the FRITZ!Box. '
                          'Are credentials, address and port correct?')
