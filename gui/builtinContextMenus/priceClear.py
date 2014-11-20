from gui.contextMenu import ContextMenu
import gui.mainFrame
import wx
import gui.globalEvents as GE
import service

class PriceClear(ContextMenu):
    def __init__(self):
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()

    def display(self, srcContext, selection):
        return "priceViewFull" in srcContext

    def getText(self, itmContext, selection):
        return "Reset Price Cache"

    def activate(self, fullContext, selection, i):
        sMkt = service.Market.getInstance()
        sMkt.clearPriceCache()
        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.mainFrame.getActiveFit()))

PriceClear.register()