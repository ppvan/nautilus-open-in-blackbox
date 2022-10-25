#!/usr/bin/python

import os, subprocess, sys
from gi import require_version
import urllib.parse
require_version('Gtk', '4.0')
require_version('Nautilus', '4.0')

from gi.repository import Nautilus, GObject
from gettext import gettext


class BlackBoxNautilus(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        # self.window = None
        self.is_selected = False

    def get_file_items(self, files):
        """Return to menu when click on any file/folder"""
        if len(files) != 1:
            self.is_selected = False
            return

        self.is_selected = True
        file = files[0]
        items = []
        #s elf.window = window
        if file.is_directory() and file.get_uri_scheme() == "file":
            items += [self._create_nautilus_item(file)]
        return items


    def get_background_items(self, file):
        """Returns the menu items to display when no file/folder is selected
        (i.e. when right-clicking the background)."""
        # Add the menu items
        items = []
        # self.window = window

        if self.is_selected:
            return

        if file.is_directory() and file.get_uri_scheme() == "file":
            items += [self._create_nautilus_item(file)]
        return items

    def _create_nautilus_item(self, file):
        print(file.get_uri())
        """Creates the 'Open In BlackBox' menu item."""
        item = Nautilus.MenuItem(name="BlackBoxNautilus::open_in_blackbox",
                                 label=gettext("Open in BlackBox"),
                                 tip=gettext("Open this folder/file in BlackBox Terminal"))
        item.connect("activate", self._nautilus_run, file)
        return item 

    def _nautilus_run(self, menu, file):
        """'Open with BlackBox 's menu item callback."""
        uri = file.get_uri()
        # uri = urllib.parse.unquote(uri)
        uri = uri.replace('file://','')
        print("Openning: ",uri)
        subprocess.Popen(['flatpak', 'run', 'com.raggesilver.BlackBox', '-w', uri])
