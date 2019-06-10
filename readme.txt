Ïðèìåðû âûçîâà:

Âûâîä çâóêà èç ôàéëà íà ëîêàëüíîì äèñêå:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["D:\\ringtone.wav"]},"id":1}

Âûâîä çâóêà ïî http ññûëêå:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["http://192.168.1.2/cms/cached/voice/aebd42dddcca11fa8b8d5ad4d75793d3_google.wav"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["http://192.168.1.2/cms/cached/voice/rh_e4768dae4160a3eb9a57713580eff5e6.wav"]},"id":1}

Âûâîä ñòàíäàðòíîãî çâóêà ïëàãèíà:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["welcome"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["ringtone"]},"id":1}

Âîçìîæíûå çíà÷åíèÿ: welcome, ringtone, incall, callend, batlow, Sincall, Eincall, Sbatlow, Ebatlow, STOP
ïðè ýòîì ïðè ïåðåäà÷å ïàðàìåòðà STOP - îñòàíîâèòü òåêóùåå âîñïðîèçâåäåíèå

Âûâîä ñîîáùåíèÿ:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Ïðîâåðêà ïîäêëþ÷åíèÿ"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Ïðîâåðêà ïîäêëþ÷åíèÿ", 7]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Ïðîâåðêà ïîäêëþ÷åíèÿ", "7", "mdm"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Ïðîâåðêà ïîäêëþ÷åíèÿ", "7", "http://192.168.1.2/img/logo_small.png"]},"id":1}

ãäå:
7=äëèòåëüíîñòü ïîêàçà ñîîáùåíèÿ â ñåêóíäàõ
mdm=ñòàíäàðòíàÿ êàðòèíêà, âìåñòî "mdm" ìîæåò áûòü url ññûëêà íà ôàéë, íàïðèìåð "http://192.168.1.2/img/logo.png"
 
ãäå:
xbmc:xbmc - ëîãèí è ïàðîëü ê KODI
192.168.1.51 - KODI
192.168.1.2 - óäàëåííûé ñåðâåð ñ õîñòèíãîì êàðòèíîê (íàïðèìåð MDM)
