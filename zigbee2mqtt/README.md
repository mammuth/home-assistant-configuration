## Add new devices

Info: I'm not using the zigbee2mqtt UI integration with automatic discovery, but rather configured the devices manually.

- Enable pairing in the zigbe2mqtt hassio addon
- Find out how to enable pairing mode for the given device (https://www.zigbee2mqtt.io/information/supported_devices.html)
- Pair it
- The device should be listed in `zigbee2mqtt/devices.yaml`. Modify the friendly name and copy it
- Add mqtt sensors for the given device as done here: https://github.com/mammuth/home-assistant-configuration/blob/8d96f9f7d13ae9a434b2dbb93c2c3371843985fe/sensors.yaml#L77-L84
