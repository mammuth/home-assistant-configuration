# My Configuration for Home Assistant

<a href="https://www.buymeacoffee.com/mammuth" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

This repository contains most parts of my Home Assistant configuration.

### Noteworthy stuff
- 37 automations in total
- FRITZ!Box Guest Wifi Control ([custom_component](https://github.com/mammuth/ha-fritzbox-tools/))
- Turn coffee machine on when alarm clock rings (using Sleep As Android and a Wifi switch)
- Turn on bedroom lights 15m before my alarm starts (using Tasker and Sleep As Android)
- Presence-based vacuum robot cleaning schedule
- Voice control of most stuff (Alexa / Google Assistant)
- Alerts on high air humidity
- Many light automations (Turn on when arriving home, turn off when leaving, dim when TV is turned on, ...)
- Enable shuffle mode on spotify ([shell script](https://github.com/mammuth/home-assistant-configuration/blob/master/shell_commands/shuffle_spotify.sh))


Most of the code / configuration is English except friendly names of frontend-facing entities (which are German).

### Main Dashboard (minimalistic)
![Screenshot 2019-09-15 at 16 57 35](https://user-images.githubusercontent.com/3121306/64923412-08ae6500-d7da-11e9-9c42-52dbf56778fa.png)
What I love most about our main view is the fact that it includes all fundamental light controls (individuals + scenes) for the living and bed room in two beautiful cards (the picture of the rooms are greyed out when all lights in the room are turned off).

### Room detail views
![Screenshot 2019-09-15 at 16 57 52](https://user-images.githubusercontent.com/3121306/64923413-08ae6500-d7da-11e9-964f-aa7882632d12.png)

### System Monitoring & Controlling
![Screenshot 2019-09-15 at 17 06 19](https://user-images.githubusercontent.com/3121306/64923571-2c25df80-d7db-11e9-8933-d81c2092c14e.png)

