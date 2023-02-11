#!/usr/bin/python

import subprocess
from gi import require_version
import urllib.parse

require_version('Nautilus', '4.0')
require_version('Gtk', '4.0')

TERMINAL_NAME = "com.raggesilver.BlackBox"

from gi.repository import Nautilus, GObject
from gettext import gettext


class BlackBoxNautilus(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        self.is_select = False
        pass

    def get_file_items(self, files: list[Nautilus.FileInfo]):
        """Return to menu when click on any file/folder"""
        if not self.only_one_file_info(files):
            return []
        
        menu = []
        fileInfo = files[0]
        self.is_select = False

        if fileInfo.is_directory():
            self.is_select = True
            dir_path = self.get_abs_path(fileInfo)

            print("Selecting a directory!!")
            print(f"Create a menu item for entry {dir_path}")
            menu_item = self._create_nautilus_item(dir_path)
            menu.append(menu_item)
        
        return menu


    def get_background_items(self, directory):
        """Returns the menu items to display when no file/folder is selected
        (i.e. when right-clicking the background)."""
        # Some concurrency problem fix.
        # when you select a directory, and right mouse, nautilus will call this
        # once the moments you focus the menu. This code to ignore that time.
        if self.is_select:
            self.is_select = False
            return []


        menu = []
        if directory.is_directory():
            dir_path = self.get_abs_path(directory)

            print("Not thing is selected. Launch from backgrounds!!")
            print(f"Create a menu item for entry {dir_path}")
            menu_item = self._create_nautilus_item(dir_path)
            menu.append(menu_item)

        return menu

    def _create_nautilus_item(self, dir_path: str) -> Nautilus.MenuItem:
        """Creates the 'Open In BlackBox' menu item."""


        item = Nautilus.MenuItem(name="BlackBoxNautilus::open_in_blackbox",
                                    label=gettext("Open in BlackBox"),
                                    tip=gettext("Open this folder/file in BlackBox Terminal"))
        print(f"Created item with path {dir_path}")


        item.connect("activate", self._nautilus_run, dir_path)
        print("Connect trigger to menu item")

        return item

    def _nautilus_run(self, menu, path):
        """'Open with BlackBox 's menu item callback."""
        print("Openning:", path)
        
        args = ['/usr/bin/flatpak', 'run', TERMINAL_NAME, '-w', path]
        subprocess.Popen(args, cwd=path)

    def get_abs_path(self, fileInfo: Nautilus.FileInfo):
        uri = fileInfo.get_uri()
        path = uri.replace('file://','')

        return urllib.parse.unquote(path)

    def only_one_file_info(self, files: list[Nautilus.FileInfo]):
        return len(files) == 1