v3.0.1

Примеры вызова:

Вывод звука из файла на локальном диске:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["D:\\test.wav"]},"id":1}

Вывод звука по http ссылке:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["http://192.168.1.2/cms/cached/voice/aebd42dddcca11fa8b8d5ad4d75793d3_google.wav"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["http://192.168.1.2/cms/cached/voice/rh_e4768dae4160a3eb9a57713580eff5e6.wav"]},"id":1}

Вывод стандартного звука плагина:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["welcome"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["ringtone"]},"id":1}

Возможные значения: ringtone, welcome, incall, callend, batlow, STOP
при этом:
welcome, incall, callend, batlow останавливают текущее воспроизведение звука предыдущего сообщения
ringtone не останавливает текущее воспроизведение звука предыдущего сообщения
STOP - команда "остановить текущее воспроизведение"


Вывод сообщения:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", 7]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", "7", "mdm"]},"id":1}

http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", "7", "http://192.168.1.2/img/logo_small.png"]},"id":1}

где:
7=длительность показа сообщения в секундах
mdm=стандартная картинка, вместо "mdm" может быть url ссылка на файл, например "http://192.168.1.2/img/logo.png"
 
где:
xbmc:xbmc - логин и пароль к KODI
192.168.1.51 - KODI
192.168.1.2 - удаленный сервер с хостингом картинок (например MDM)

Определение доступности и готовности плагина:
Для модуля MDM terminals2 пинговать так: http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["ping"]},"id":1}


Особенности: В силу специфики плеера системных звуков KODI (через который реализовано воспроизведение сообщений) - любая команда на ТТС будет приводть к снятию с паузы воспроизводимого контента (если он в момент ТТС стоял на паузе), иначе сообщение не проигрывается. Надеюсь эта недоработка будет решена в следующих версиях KODI
