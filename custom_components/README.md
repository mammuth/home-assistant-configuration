# FRITZ!Box Guest Wifi Control
configuration.yml:
```yaml
fritzbox_guestwifi:
  password: "yourfritzboxpassword"
```

The custom component registers two services, called `fritzbox_guestwifi.turn_on` and `fritzbox_guestwifi.turn_off`, which you can use in automations like seen here:
```yaml
automation:
  - alias: "Guests -> Turn on guest wifi"
    trigger:
      platform: state
      entity_id: input_boolean.guest_mode
      to: 'on'
    action:
      - service: fritzbox_guestwifi.turn_on
      - service: notify.pushbullet_max
        data:
          title: "Guest wifi is enabled"
          message: "Password: ..."
```
