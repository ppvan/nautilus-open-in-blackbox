# OpenInBlackBox

<p>Simple script to open my favorite terminal <a href="https://gitlab.gnome.org/raggesilver/blackbox">Black Box</a> from Nautilus (Gnome Files) Menu</p>


<p align="center">
  <img src="https://raw.githubusercontent.com/phucnoob/OpenInBlackBox/main/preview.png" />
</p>


## Installation

1. Install `nautilus-python >=4.0`
    #### Ubuntu
    ```sh
    sudo apt install python3-nautilus
    ```
    #### Fedora
    ```sh
    sudo dnf install nautilus-python
    ```
    ### Arch
    ```sh
    sudo pacman -S nautilus-python
    ```

2. Copy `nautilus-open-in-blackbox.py` to `$XDG_DATA_HOME/nautilus-python/extensions` (default to `$HOME/.local/share/nautilus-python/extensions`) if `XDG_DATA_HOME` not set.

    > [!NOTE]
    > If the latest version don't work, you can try the stable version 0.1.2 [nautilus-open-in-blackbox.py](https://github.com/ppvan/nautilus-open-in-blackbox/blob/v0.1.2/nautilus-open-in-blackbox.py)

    ```sh
    mkdir -p $HOME/.local/share/nautilus-python/extensions
    cp nautilus-open-in-blackbox.py $HOME/.local/share/nautilus-python/extensions

    nautilus -q # restart nautilus
    ```


## Stability Note

The script stability mostly depend on the Nautilus-Python API and system python so there is no version pin here. I'll note the API version here tested on my machine so it's more future proof:

- `nautilus-python` 4.0.1: [Docs](https://gnome.pages.gitlab.gnome.org/nautilus-python/)
- Python 3.12+ (But it should work for any Python 3.7+ infer from module usage)