#!/usr/bin/python3
import locale
import os
import subprocess
from typing import List

from gi.repository import GObject, Nautilus

TRANSLATIONS = {
    "zh": {
        "label": "在 Black Box 打开",
        "tip": "Open this folder/file in Black Box Terminal",
    },
    "fr": {
        "label": "Ouvrir dans Black Box",
        "tip": "Ouvrir ce fichier/dossier dans Black Box",
    },
    "ar": {
        "label": "(Black Box) الفتح فب العابة السوداء",
        "tip": "Open this folder/file in Black Box Terminal",
    },
    "pt": {
        "label": "Abrir no Black Box",
        "tip": "Abrir esta pasta/arquivo no terminal Black Box",
    },
    "default": {
        "label": "Open in Black Box",
        "tip": "Open this folder/file in Black Box Terminal",
    },
}


class OpenBlackboxTerminalExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(self, files: List[Nautilus.FileInfo]) -> List[Nautilus.MenuItem]:
        """Only add terminal menu if user only select a single file/directory"""
        if len(files) != 1:
            return []

        fileInfo = files[0]
        if not fileInfo.is_directory():
            return []

        item = self._create_open_terminal_menuitem_file(fileInfo)

        return [item]

    def get_background_items(self, cwd: Nautilus.FileInfo) -> List[Nautilus.MenuItem]:
        """Returns the menu items to display when no file/folder is selected
        (i.e. when right-clicking the background)."""

        if not cwd.is_directory():
            return []

        item = self._create_open_terminal_menuitem_background(cwd)

        return [item]

    def _create_open_terminal_menuitem_file(
        self, fileInfo: Nautilus.FileInfo
    ) -> Nautilus.MenuItem:
        """Creates the 'Open In Black Box' menu item."""

        lang = locale.getlocale()[0].split("_")[0]  # en, fr, vi...
        label = TRANSLATIONS[lang]["label"]
        tip = TRANSLATIONS[lang]["tip"]

        item = Nautilus.MenuItem(
            name="BlackBoxNautilus::open_in_blackbox1",
            label=label,
            tip=tip,
        )

        item.connect("activate", self._open_terminal, fileInfo)
        return item

    def _create_open_terminal_menuitem_background(
        self, fileInfo: Nautilus.FileInfo
    ) -> Nautilus.MenuItem:
        """Creates the 'Open In Black Box' menu item."""
        lang = locale.getlocale()[0].split("_")[0]  # en, fr, vi...
        label = TRANSLATIONS[lang]["label"]
        tip = TRANSLATIONS[lang]["tip"]

        item = Nautilus.MenuItem(
            name="BlackBoxNautilus::open_in_blackbox2",
            label=label,
            tip=tip,
        )

        item.connect("activate", self._open_terminal, fileInfo)
        return item

    def _open_terminal(
        self, menu: Nautilus.MenuItem, working_dir: Nautilus.FileInfo
    ) -> None:
        """Open with Black Box 's menu item callback."""
        cwd = working_dir.get_location().get_path()
        possible_locations = [
            "/usr/bin/blackbox-terminal",
            "/usr/bin/blackbox",
        ]

        for command in possible_locations:
            if os.path.exists(command) and os.access(command, os.X_OK):
                subprocess.Popen([command, "--working-directory", cwd])
                break
        else:
            subprocess.Popen(
                [
                    "/usr/bin/flatpak",
                    "run",
                    "com.raggesilver.BlackBox",
                    "--working-directory",
                    cwd,
                ]
            )
