# My Configuration for Home Assistant

Within this repository I'm sharing my Home Assistant configuration.

### Noteworthy stuff
- 22 automations in total
- Offline Voice Control for everything via DIY Amazon Echo (using HA and snips)
- FRITZ!Box Guest Wifi Control ([custom_component](https://github.com/mammuth/home-assistant-configuration/blob/master/custom_components/fritzbox_guestwifi.py))
- Turn coffee machine on when alarm clock rings (using Sleep As Android and a Wifi switch)
- Turn on bedroom lights 15m before my alarm starts (using Tasker and Sleep As Android)
- Many light automations (Turn on when arriving home, turn off when leaving, dim when TV is turned on, ...)
- Enable shuffle mode on spotify ([shell script](https://github.com/mammuth/home-assistant-configuration/blob/master/shell_commands/shuffle_spotify.sh))


Most of the code / configuration is English except friendly names of frontend-facing entities (which are German).

### Main Dashboard (minimalistic)
![Screenshot 2019-07-22 at 19 35 52](https://user-images.githubusercontent.com/3121306/61652323-f0c5d380-acb7-11e9-892b-4be881276ef4.png)
What I love most about our main view is the fact that it includes all fundamental light controls (individuals + scenes) for the living and bed room in two beautiful cards (the picture of the rooms are greyed out when all lights in the room are turned off).

### Admin Dashboard
![image](https://user-images.githubusercontent.com/3121306/36357326-a3d87126-14fc-11e8-8270-600feca50ac0.png)

### Raspberry PI Monitoring
![Screenshot 2019-07-04 at 19 23 06](https://user-images.githubusercontent.com/3121306/60681880-2b92d380-9e91-11e9-8ae5-feaef18cdb81.png)
