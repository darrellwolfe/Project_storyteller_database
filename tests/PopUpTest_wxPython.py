import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Interactive Window")
panel = wx.Panel(frame)
label = wx.StaticText(panel, label="Hello, welcome to the popup!", pos=(10, 10))
frame.Show(True)
app.MainLoop()
