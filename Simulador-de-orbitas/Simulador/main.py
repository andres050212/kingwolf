# --*-- coding: UTF_8 --*--
'''
Created on 29/12/2015

@author: Jonay Zevenzui Castro Suárez
'''

import wx
from math import sqrt

class Main(wx.Frame):
    def __init__(self):
        self.lisve = ['-1', '-0.5', '-0.12', '-0.11', '-0.1', '0', '0.1', '0.11', '0.12', '0.5', '1']
        self.lima = ['0', '5', '10', '15', '20', '25', '30', '40', '50', '60', '70', '80', '100']
        wx.Frame.__init__(self, None, -1, title='Simulador')
        self.SetSize(wx.GetDisplaySize())
        sizev1 = wx.BoxSizer(wx.VERTICAL)

        sizeh1 = wx.BoxSizer(wx.HORIZONTAL)

        sizev2 = wx.BoxSizer(wx.VERTICAL)
        titex1 = wx.StaticText(self, label='Tiempo')
        self.selti1 = wx.Choice(self, -1, choices=['10000', '30000', '50000'])
        sizev2.Add(titex1, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev2.Add(self.selti1, flag=wx.RIGHT|wx.LEFT, border=2)
        sizeh1.Add(sizev2)

        sizev3 = wx.BoxSizer(wx.VERTICAL)
        vetex1 = wx.StaticText(self, label='Vel.obj 1(X)')
        vetex2 = wx.StaticText(self, label='Vel.obj 1(Y)')
        self.selve1x = wx.Choice(self, -1, choices=self.lisve)
        self.selve1y = wx.Choice(self, -1, choices=self.lisve)
        self.selve1x.SetSelection(4)
        self.selve1y.SetSelection(5)
        sizev3.Add(vetex1,flag=wx.RIGHT|wx.LEFT, border=2)
        sizev3.Add(self.selve1x, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev3.Add(vetex2, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev3.Add(self.selve1y, flag=wx.RIGHT|wx.LEFT, border=2)
        sizeh1.Add(sizev3)

        sizev4 = wx.BoxSizer(wx.VERTICAL)
        vetex3 = wx.StaticText(self, label='Vel.obj 2(X)')
        vetex4 = wx.StaticText(self, label='Vel.obj 2(Y)')
        self.selve2x = wx.Choice(self, -1, choices=self.lisve)
        self.selve2y = wx.Choice(self, -1, choices=self.lisve)
        self.selve2x.SetSelection(6)
        self.selve2y.SetSelection(5)
        sizev4.Add(vetex3, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev4.Add(self.selve2x, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev4.Add(vetex4, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev4.Add(self.selve2y, flag=wx.RIGHT|wx.LEFT, border=2)
        sizeh1.Add(sizev4)

        sizeh2 = wx.BoxSizer(wx.HORIZONTAL)

        sizev5 = wx.BoxSizer(wx.VERTICAL)
        matex1 = wx.StaticText(self, label='Ma.obj.1')
        self.selma1 = wx.Choice(self, -1, choices=self.lima)
        self.selma1.SetSelection(2)
        sizev5.Add(matex1, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev5.Add(self.selma1, flag=wx.RIGHT, border=15)
        sizeh2.Add(sizev5)

        sizev6 = wx.BoxSizer(wx.VERTICAL)
        matex2 = wx.StaticText(self, label='Ma.obj.2')
        self.selma2 = wx.Choice(self, -1, choices=self.lima)
        self.selma2.SetSelection(2)
        sizev6.Add(matex2, flag=wx.RIGHT|wx.LEFT, border=2)
        sizev6.Add(self.selma2, flag=wx.RIGHT|wx.LEFT, border=2)
        sizeh2.Add(sizev6)

        bu = wx.BitmapButton(self, -1, bitmap=wx.Bitmap('iconos/ir.png'), size=(98, 32))
        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour(wx.BLACK)

        sizev1.Add(sizeh1, flag=wx.ALL, border=10)
        sizev1.Add(sizeh2, flag=wx.LEFT, border=85)
        sizev1.Add(bu, flag=wx.ALL, border=10)
        sizev1.Add(self.panel, proportion=1, flag=wx.EXPAND|wx.RIGHT|wx.LEFT|wx.BOTTOM, border=10)
        self.SetSizer(sizev1)

        self.Bind(wx.EVT_BUTTON, self.Acti, bu)

    def Acti(self, event):
        self.panel.Refresh()
        t = self.selti1.GetStringSelection()
        v1x = self.selve1x.GetStringSelection()
        v1y = self.selve1y.GetStringSelection()
        v2x = self.selve2x.GetStringSelection()
        v2y = self.selve2y.GetStringSelection()
        m1 = self.selma1.GetStringSelection()
        m2 = self.selma2.GetStringSelection()

        x, y = self.panel.GetSize()
        x1 = (x / 2) + 150
        y1 = (y / 2) + 150
        masa_1 = int(m1)
        velocidad_x1 = float(v1x)
        velocidad_y1 = float(v1y)
        x2 = (x / 2) - 150
        y2 = (y / 2) - 150
        masa_2 = int(m2)
        velocidad_x2 = float(v2x)
        velocidad_y2 = float(v2y)
        for i in range(int(t)):
            r = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 3
            aceleracion_x1 = masa_2 * (x2 - x1) / r
            aceleracion_y1 = masa_2 * (y2 - y1) / r
            aceleracion_x2 = masa_1 * (x1 - x2) / r
            aceleracion_y2 = masa_1 * (y1 - y2) / r

            velocidad_x1 += aceleracion_x1
            velocidad_y1 += aceleracion_y1
            velocidad_x2 += aceleracion_x2
            velocidad_y2 += aceleracion_y2

            x1 += velocidad_x1
            y1 += velocidad_y1
            x2 += velocidad_x2
            y2 += velocidad_y2
            dc = wx.PaintDC(self.panel)
            dc.SetBrush(wx.Brush('RED'))
            dc.SetPen(wx.Pen('BLACK', 1))
            dc.DrawCircle(x1, y1, masa_1)
            dc.DrawCircle(x2, y2, masa_2)

def main():
    app = wx.App()
    frame = Main()
    frame.Show(True)
    app.MainLoop()
if __name__ == '__main__':
    main()