# OpenInBlackBox

<p>Simple script to open my favorite terminal <a href="https://gitlab.gnome.org/raggesilver/blackbox">Black Box</a> from Nautilus (Gnome Files) Menu</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/phucnoob/OpenInBlackBox/main/preview.png" />
</p>


## Dependency
`nautilus-python`( `python-nautilus` on Debian/Ubuntu based)
### Ubuntu
```
sudo apt install python3-nautilus
```
### Fedora
```
sudo dnf install nautilus-python
```

## Installation

### Arch Linux
Install from AUR
```
yay -S nautilus-open-in-blackbox
```
Restart Nautilus
```
nautilus -q
```

### Other Disto

Clone this repository and use the install script.
```
git clone https://github.com/ppvan/nautilus-open-in-blackbox.git
cd nautilus-open-in-blackbox
./install.sh
```
or install system-wide with sudo
```
sudo ./install.sh
```
