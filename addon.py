import os
import sys
import time
import urlparse
import xbmcaddon
import xbmcgui
import xbmc
import pyxbmct
import time
import json
import urllib
import urllib2

__addon__      = xbmcaddon.Addon()
__cwd__        = xbmc.translatePath( __addon__.getAddonInfo('path') ).decode("utf-8")


#xbmc.translatePath(path)#'special://masterprofile/script_data' -> '/home/user/XBMC/UserData/script_data' on Linux

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
addon_dir = addon.getAddonInfo('path')

LOGO_MDM = os.path.join(addon_dir, 'resources', 'img', "mdm.png")
LOGO_PHONE = os.path.join(addon_dir, 'resources', 'img', "phone.png")
LOGO_RETROPHONE = os.path.join(addon_dir, 'resources', 'img', "retro_phone.png")
LOGO_CALLOUTGOING = os.path.join(addon_dir, 'resources', 'img', "call_outgoing.png")
LOGO_MIC = os.path.join(addon_dir, 'resources', 'img', "mic.png")
LOGO_NIGHTMODE = os.path.join(addon_dir, 'resources', 'img', "night_mode.png")
LOGO_LOWBATT = os.path.join(addon_dir, 'resources', 'img', "low_batt.png")
LOGO_REWIND = os.path.join(addon_dir, 'resources', 'img', "rewind.png")
LOGO_ATTENTION = os.path.join(addon_dir, 'resources', 'img', "attention.png")
LOGO_CONSTUCT = os.path.join(addon_dir, 'resources', 'img', "construction.png")

SOUND_WELCOME = os.path.join(addon_dir, 'resources', 'media', "welcome.wav")
SOUND_RINGTONE = os.path.join(addon_dir, 'resources', 'media', "ringtone.wav")
SOUND_INCALL = os.path.join(addon_dir, 'resources', 'media', "incall.wav")
SOUND_CALLEND = os.path.join(addon_dir, 'resources', 'media', "callend.wav")
SOUND_BATLOW = os.path.join(addon_dir, 'resources', 'media', "batlow.wav")


settings = xbmcaddon.Addon(id='script.alicevox.master')
host = settings.getSetting("host")                           #str
url = 'http://'+host+'/post_service'
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
data = urllib.urlencode({'event' : 'test',
                         'time'  : '10'})
tts_notification = settings.getSetting("tts_notification")   #bool->str
notification_time = settings.getSetting("notification_time") #str
n_time = int(notification_time)*1000                         #to seconds
notification_time = str(n_time)                              #int->str
tts_stop = settings.getSetting("tts_stop")                   #bool->str
media_unpause = settings.getSetting("media_unpause")         #bool->str
message_type = settings.getSetting("message_type")           #str
message_size = settings.getSetting("message_size")           #str
message_color = settings.getSetting("message_color")         #str

#0xTTRRGGBB where T is the transparency value, R is red, G is green and as you guessed B is blue
colors = ['0xFFFF0000', '0xFFFFD700', '0xFF00FF00', '0xFF0000FF','0xFF8000FF']

dialog = xbmcgui.Dialog()



def isPlaybackPaused():
    return bool(xbmc.getCondVisibility("Player.Paused"))

def isMuted():
    return bool(xbmc.getCondVisibility("Player.Muted"))

def play():
	if isPlaybackPaused(): xbmc.Player().pause() #trigger


def pause():
	if not isPlaybackPaused(): xbmc.Player().pause() #trigger


#	xbmcgui.Dialog().ok(addonname, str(isPlaybackPaused()))
#	xbmcgui.Dialog().ok(addonname, str(isMuted()))




# Main execution
if len(sys.argv) == 2:
	xbmc.enableNavSounds(True)

	if sys.argv[1] != "MESSAGE":
		if "/cms/cached/voice/" in sys.argv[1]:
			if tts_stop == "true": xbmc.stopSFX()
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(TTS arrived, trying to say it..., '+notification_time+')')
                        xbmc.playSFX(sys.argv[1],False)
		elif sys.argv[1] == "ping":
			pass
		elif sys.argv[1] == "ringtone":
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(Built-in sound called, "RINGTONE")')
			xbmc.playSFX(SOUND_RINGTONE)
		elif sys.argv[1] == "welcome":
			if tts_stop == "true": xbmc.stopSFX()
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(Built-in phrase called, "WELCOME")')
			xbmc.playSFX(SOUND_WELCOME)
		elif sys.argv[1] == "incall":
			if tts_stop == "true": xbmc.stopSFX()
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(Built-in phrase called, "INCOMING CALL")')
			xbmc.playSFX(SOUND_INCALL)
		elif sys.argv[1] == "callend":
			if tts_stop == "true": xbmc.stopSFX()
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(Built-in phrase called, "CALL RELEASE")')
			xbmc.playSFX(SOUND_CALLEND)
		elif sys.argv[1] == "batlow":
			if tts_stop == "true": xbmc.stopSFX()
			if media_unpause == "true": play()
			if tts_notification == "true": xbmc.executebuiltin('XBMC.Notification(Built-in phrase called, "BATTERY PHONE IS LOW")')
			xbmc.playSFX(SOUND_BATLOW)
		elif sys.argv[1] == "STOP": xbmc.stopSFX()
		else: xbmc.executebuiltin('XBMC.Notification('+addonname+': ERROR, command '+sys.argv[1]+' not recognized)')
elif len(sys.argv) > 2 and sys.argv[1] == "MESSAGE":
	if len(sys.argv) == 4:
		showtime = 5
		url=logo_mdm
	elif len(sys.argv) == 5:
		showtime = float(sys.argv[4])
		url=logo_mdm
	elif len(sys.argv) == 6:
		showtime = float(sys.argv[4])
		url=sys.argv[5]
		if sys.argv[5] == "mdm":
			url=LOGO_MDM
		elif sys.argv[5] == "phone":
			url=LOGO_PHONE
		elif sys.argv[5] == "retro_phone":
			url=LOGO_RETROPHONE
		elif sys.argv[5] == "call_outgoing":
			url=LOGO_CALLOUTGOING
		elif sys.argv[5] == "mic":
			url=LOGO_MIC
		elif sys.argv[5] == "night_mode":
			url=LOGO_NIGHTMODE
		elif sys.argv[5] == "low_batt":
			url=LOGO_LOWBATT
		elif sys.argv[5] == "rewind":
			url=LOGO_REWIND
		elif sys.argv[5] == "attention":
			url=LOGO_ATTENTION
		elif sys.argv[5] == "construct":
			url=LOGO_CONSTUCT
	if message_type == "0": #classic
		xbmc.executebuiltin('XBMC.Notification('+sys.argv[2]+', '+sys.argv[3]+', '+str(showtime*1000)+', '+str(url)+')')
	if message_type == "1": #xbmcgui
		#-align center-
		#image = xbmcgui.ControlImage(400, 300, 200, 200, LOGO_CONSTUCT) # X Y LeftUp & "width" "height"
		#textbox = xbmcgui.ControlTextBox(630, 360, 1200, 400, font=message_size, textColor=colors[int(message_color)]) # X Y "width" "height"
		#-align bottom-
		image = xbmcgui.ControlImage(400, 600, 200, 200, LOGO_CONSTUCT) # X Y LeftUp & "width of control" "height of control"
		textbox = xbmcgui.ControlTextBox(630, 580, 1200, 400, font=message_size, textColor=colors[int(message_color)]) # X Y LeftUp & "width" "height"
		window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
		window.addControl(textbox)
		window.addControl(image)
		textbox.setText(sys.argv[3])
		image.setImage(url, False)
		time.sleep(showtime)
		#textbox.reset()
		textbox.setText("")
		image.setImage("", False)
	if message_type == "2": #pyxbmct
		window = pyxbmct.AddonDialogWindow(sys.argv[2]) #-Create a window instance
		#window = pyxbmct.BlankDialogWindow() #transparent
		#window = pyxbmct.AddonFullWindow(sys.argv[2])
		#window = pyxbmct.BlankFullWindow()
		window.setGeometry(650, 170, 1, 5) #-Set the window "width", "height" and the grid resolution: 2 rows, 3 columns
		image = pyxbmct.Image(url)
		message = pyxbmct.Label(sys.argv[3], alignment=pyxbmct.ALIGN_CENTER, font=message_size, textColor=colors[int(message_color)])
		#message = pyxbmct.TextBox(sys.argv[3])
		#message.setAnimations([('WindowOpen', 'effect=fade start=0 end=100 time=2000',), ('WindowClose', 'effect=fade start=100 end=0 time=2000',)])
		window.placeControl(image, 0, 0) #-Place the img on the window grid
		window.placeControl(message, 0, 1, rowspan=1, columnspan=4) #-Place the label/textbox on the window grid
		window.show()
		time.sleep(showtime)
		window.close()
elif len(sys.argv) > 2 and sys.argv[1] == "PIC":
        showtime = float(sys.argv[6])
        url=sys.argv[7]
        if sys.argv[7] == "mdm":
                url=LOGO_MDM
        elif sys.argv[7] == "phone":
                url=LOGO_PHONE
        elif sys.argv[7] == "retro_phone":
                url=LOGO_RETROPHONE
        elif sys.argv[7] == "call_outgoing":
                url=LOGO_CALLOUTGOING
        elif sys.argv[7] == "mic":
                url=LOGO_MIC
        elif sys.argv[7] == "night_mode":
                url=LOGO_NIGHTMODE
        elif sys.argv[7] == "low_batt":
                url=LOGO_LOWBATT
        elif sys.argv[7] == "rewind":
                url=LOGO_REWIND
        elif sys.argv[7] == "attention":
                url=LOGO_ATTENTION
        elif sys.argv[7] == "construct":
                url=LOGO_CONSTUCT
        pic = xbmcgui.ControlImage(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), url) # X Y LeftUp & "width of control" "height of control"
        window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
        window.addControl(pic)
        pic.setImage(url, False)
        time.sleep(showtime)
        pic.setImage("", False)
else:
	xbmc.executebuiltin('XBMC.Notification('+addonname+': ERROR, have not correct data payload)')



#xbmc.LOGDEBUG = 0
#xbmc.LOGINFO = 1
#xbmc.LOGNOTICE = 2
#xbmc.LOGWARNING = 3
#xbmc.LOGERROR = 4
#xbmc.LOGSEVERE = 5
#xbmc.LOGFATAL = 6
#xbmc.LOGNONE = 7
try:
#	response = opener.open(url, data=data).read() #perform operations
    pass
except urllib2.HTTPError, e:
	xbmc.log('HTTPError = ' + str(e.code), 3)
	dialog.ok(addonname+': HTTPError', 'Failed to connect '+url, str(e.code))
except urllib2.URLError, e:
	xbmc.log('URLError = ' + str(e.reason), 3)
	dialog.ok(addonname+': URLError', 'Failed to connect', str(e.reason))
except httplib.HTTPException, e:
	xbmc.log('HTTPException', 3)
	dialog.ok(addonname+': HTTPException', 'Failed connect to SmartHome', url)
except Exception:
	import traceback
	xbmc.log('generic exception: ' + str(traceback.format_exc()), 3)

