# OpenWRT WiFi Switch for Home Assistant

Switch your WiFi on and off using Home Assistant.

### Installation

Go to this folder `<config_dir>/custom_components/`.

Execute `git clone https://git.multilan.de/tarek/homeassistant-openwrt-wifi-switch`

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
openwrt_wifi_switch:
- ifname: "<wifi-interface-ifname>"
  host: "<ssh-host>"
  username: "<ssh-username>"
  password: "<ssh-password>"
  port: "<ssh-port>"
```
