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
