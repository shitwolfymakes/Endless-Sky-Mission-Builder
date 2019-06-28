''' ttkthemes_nuitka_plugin.py
# Copyright (c) 2019 by MCOfficer
#
# Endless Sky Mission Builder is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# Endless Sky Mission Builder is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

This file contains a plug-in that fixes standalone nuitka builds with the ttkthemes module.
'''

import os
from logging import info, warning
from shutil import copytree

from nuitka.plugins.PluginBase import NuitkaPluginBase


def get_ttkthemes_path():
    import ttkthemes
    return os.path.dirname(ttkthemes.__file__)


class TtkthemesPlugin(NuitkaPluginBase):
    """
    This Plug-In copies the `ttkthemes` site-package to the output directory,
    since ttkthemes expects its files to be there.
    """

    plugin_name = __file__
    plugin_desc = "Required by ttkthemes packages"

    def onStandaloneDistributionFinished(self, dist_dir):
        source = get_ttkthemes_path()
        dest = os.path.join(dist_dir, "ttkthemes")
        if os.path.exists(dest):
            warning("ttkthemes: %s already exists! Aborting" % dest)
            return
        info("ttkthemes: copying %s to %s" % (source, dest))
        copytree(source, dest)
