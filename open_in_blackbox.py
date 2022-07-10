#!/usr/bin/python

import os, subprocess
from gi import require_version
import urllib.parse
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')

from gi.repository import Nautilus, GObject
from gettext import gettext


class BlackBoxNautilus(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def get_file_items(self, window, files):
        pass

    def get_background_items(self, window, file):
        """Returns the menu items to display when no file/folder is selected
        (i.e. when right-clicking the background)."""
        # Add the menu items
        items = []
        self.window = window
        if file.is_directory() and file.get_uri_scheme() == "file":
            items += [self._create_nautilus_item(file)]
        return items

    def _create_nautilus_item(self, file):
        """Creates the 'Open In BlackBox' menu item."""
        item = Nautilus.MenuItem(name="BlackBoxNautilus::Nautilus",
                                 label=gettext("Open in BlackBox"),
                                 tip=gettext("Open this folder/file in BlackBox Terminal"))
        item.connect("activate", self._nautilus_run, file)
        return item 

    def _nautilus_run(self, menu, file):
        """'Open with BlackBox 's menu item callback."""
        uri = file.get_uri()
        # uri = urllib.parse.unquote(uri)
        uri = uri.replace('file://','')
        subprocess.run(['flatpak', 'run', 'com.raggesilver.BlackBox', '-w', uri])