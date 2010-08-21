# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="brian"
__date__ ="$Aug 20, 2010 10:36:42 PM$"

import sys
import xbmcgui
import xbmcplugin
import urllib

import xbmcaddon

__settings__ = xbmcaddon.Addon(id='plugin.pictures.icanhascheezburger.com')
__language__ = __settings__.getLocalizedString

#
# Main class
#
class Main:
    #
    # Init
    #
    def __init__(self):
        #
        # Get Lols
        #
        self.get_cheez_type( )

    def get_cheez_type(self):
        cheez_type = {}
        for t in range(30405, 30407):
            cheez_type[t] = __language__(t)
            plugin_url = "%s?action=%s" % (
             sys.argv[0],
             t )
            listitem = xbmcgui.ListItem (__language__(t),
             iconImage = "DefaultPicture.png",
             thumbnailImage = "DefaultPicture.png")
            listitem.setInfo( "pictures", { "title" : "lol_name" } )
            ok = xbmcplugin.addDirectoryItem( handle = int(sys.argv[1]),
             url = plugin_url,
             listitem = listitem,
             isFolder = True)

        #
        # End of list...
        #

        # Sort by label...
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )

        # End of list...
        xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )
