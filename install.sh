#!/usr/bin/bash

EXT_PATH=nautilus-open-in-blackbox.py

restart_nautilus() {
    read -p "Restart Nautilus(Files)? [Y/n]" ans

    if [[ $ans == 'y' || $ans == 'Y' || $ans == '' ]]; then
        nautilus -q
    fi
}

install_user() {
    path=$EXT_PATH
    target=~/.local/share/nautilus-python/extensions/

    if [[ ! -d $target ]]; then
        mkdir -v -p $target
    fi

    cp -v $path $target

    restart_nautilus
}

install_sudo() {
    path=$EXT_PATH
    target=/usr/share/nautilus-python/extensions/

    if [[ ! -d $target ]]; then
        sudo mkdir -v -p $target
    fi

    sudo cp -v $path $target

    restart_nautilus
}

if [[ $(id -u) == 0 ]]; then
    read -p "This is run with sudo, install system-wide?[Y/n]" ans
    if [[ $ans == 'y' || $ans == 'Y' || $ans == '' ]]; then
        install_sudo
    else
        echo -n "Skip install..."
    fi
else
    read -p "Install OpenInBlackBox?[Y/n]" ans
    if [[ $ans == 'y' || $ans == 'Y' || $ans == '' ]]; then
        install_user
    else
        echo -n "Skip install..."
    fi
fi