# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 916,481 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblUsername = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblUsername.Wrap( -1 )

		bSizer18.Add( self.lblUsername, 0, wx.ALL, 8 )

		self.txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.txtUsername, 0, wx.ALL, 5 )

		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblPassword = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPassword.Wrap( -1 )

		bSizer62.Add( self.lblPassword, 0, wx.ALL, 8 )

		self.txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer62.Add( self.txtPassword, 0, wx.ALL, 5 )


		bSizer62.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		self.closeButton = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.closeButton, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer211, 1, wx.EXPAND, 5 )


		bSizer18.Add( bSizer62, 1, wx.ALL, 0 )


		bSizer22.Add( bSizer18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 0 )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )


		bSizer63.Add( ( 0, 0), 0, wx.EXPAND, 0 )


		bSizer22.Add( bSizer63, 0, wx.ALL, 10 )

		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.inetButton = wx.Button( self, wx.ID_ANY, u"Internet Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.inetButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 8 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer23.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer23.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer49.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer491 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer111 = wx.BoxSizer( wx.VERTICAL )

		self.radiusButton = wx.Button( self, wx.ID_ANY, u"Fix Radius", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.radiusButton, 0, wx.ALIGN_RIGHT|wx.ALL, 8 )

		self.aclButton = wx.Button( self, wx.ID_ANY, u"ACL Verification", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.aclButton, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer491.Add( bSizer111, 1, wx.ALL, 5 )


		bSizer49.Add( bSizer491, 1, wx.ALL, 5 )

		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer50 = wx.BoxSizer( wx.VERTICAL )

		self.lblHostname = wx.StaticText( self, wx.ID_ANY, u"Hostname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblHostname.Wrap( -1 )

		bSizer50.Add( self.lblHostname, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 8 )

		self.txtHostname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer50.Add( self.txtHostname, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer64.Add( bSizer50, 1, wx.ALL, 5 )

		bSizer501 = wx.BoxSizer( wx.VERTICAL )

		self.backupButton = wx.Button( self, wx.ID_ANY, u"Backup Hostname", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer501.Add( self.backupButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.clearButton = wx.Button( self, wx.ID_ANY, u"Clear Hostname", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer501.Add( self.clearButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 8 )


		bSizer64.Add( bSizer501, 1, wx.ALL, 5 )


		bSizer49.Add( bSizer64, 1, wx.ALL, 5 )


		bSizer22.Add( bSizer49, 1, wx.ALL, 5 )


		bSizer14.Add( bSizer22, 1, wx.ALL, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer14.Add( bSizer141, 0, wx.EXPAND, 5 )


		bSizer15.Add( bSizer14, 1, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.txtOutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17.Add( self.txtOutput, 1, wx.EXPAND, 5 )


		bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.closeButton.Bind( wx.EVT_BUTTON, self.closeFunc )
		self.inetButton.Bind( wx.EVT_BUTTON, self.inetFunc )
		self.radiusButton.Bind( wx.EVT_BUTTON, self.radiusfixitFunc )
		self.aclButton.Bind( wx.EVT_BUTTON, self.aclFunc )
		self.backupButton.Bind( wx.EVT_BUTTON, self.backupFunc )
		self.clearButton.Bind( wx.EVT_BUTTON, self.clearFunc )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def closeFunc( self, event ):
		event.Skip()

	def inetFunc( self, event ):
		event.Skip()

	def radiusfixitFunc( self, event ):
		event.Skip()

	def aclFunc( self, event ):
		event.Skip()

	def backupFunc( self, event ):
		event.Skip()

	def clearFunc( self, event ):
		event.Skip()


