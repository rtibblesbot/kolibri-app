from importlib.resources import files

import kolibri
import wx
import wx.adv

from kolibri_app._version import __version__ as app_version
from kolibri_app.i18n import _

DOCS_URL = "https://kolibri.readthedocs.io/en/latest/"
FORUMS_URL = "https://community.learningequality.org/"


class AboutDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(
            parent, title=_("About Kolibri"), style=wx.DEFAULT_DIALOG_STYLE
        )
        sizer = wx.BoxSizer(wx.VERTICAL)

        try:
            icon_path = files("kolibri_app") / "icons" / "kolibri-icon.png"
            image = wx.Image(str(icon_path), wx.BITMAP_TYPE_PNG).Scale(
                64, 64, wx.IMAGE_QUALITY_HIGH
            )
            bitmap = wx.StaticBitmap(self, bitmap=wx.Bitmap(image))
            sizer.Add(bitmap, 0, wx.ALIGN_CENTER | wx.TOP, 16)
        except (FileNotFoundError, OSError):
            pass

        sizer.Add(
            wx.StaticText(
                self, label=_("App version: %(version)s") % {"version": app_version}
            ),
            0,
            wx.ALIGN_CENTER | wx.TOP,
            8,
        )
        sizer.Add(
            wx.StaticText(
                self,
                label=_("Kolibri version: %(version)s")
                % {"version": kolibri.__version__},
            ),
            0,
            wx.ALIGN_CENTER | wx.TOP,
            4,
        )

        sizer.Add(
            wx.StaticText(self, label=_("© Learning Equality")),
            0,
            wx.ALIGN_CENTER | wx.TOP,
            12,
        )

        link_sizer = wx.BoxSizer(wx.HORIZONTAL)
        link_sizer.Add(
            wx.adv.HyperlinkCtrl(self, label=_("Documentation"), url=DOCS_URL),
            0,
            wx.RIGHT,
            8,
        )
        link_sizer.Add(
            wx.adv.HyperlinkCtrl(self, label=_("Community Forums"), url=FORUMS_URL),
        )
        sizer.Add(link_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 8)

        close_btn = wx.Button(self, wx.ID_OK, _("Close"))
        close_btn.SetDefault()
        sizer.Add(close_btn, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 16)

        self.SetSizerAndFit(sizer)
        self.CenterOnParent()
