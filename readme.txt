v3.1.1

Плагин предназначен для:
*воспроизведения "стандартных" звуков и фраз (ringtone, welcome, incall, callend, batlow) идущих в "комплекте" с плагином
*воспроизведения произвольных звуковых фрагментов из файловой системы компьютера на котором установлен KODI
*воспроизведения произвольных звуковых фрагментов по http url ссылке
*вывод "стандартных" изображений (mdm, ir, mqtt, mqtt_err, phone, attention, construct, mic, night_mode, retro_phone, call_outgoing, low_batt, full_batt, rewind) идущих в "комплекте" с плагином в произвольном месте экрана KODI
*вывод произвольного изображения по http url в произвольном месте экрана KODI
*показ произвольного текстового сообщения (тремя различными методами - "классическое сообщение KODI", встроенные средства "XBMCGUI", библиотека "PYXBMCT") в произвольном месте экрана в виде: Pic Title Body


Совместимость с версиями KODI:
*до Kodi 17 Krypton включительно управление плагином может осуществлятся методом GET и POST
*начиная с Kodi 18 Leia и выше управление плагином может осуществлятся только методом POST

Совместимость с другим программным обеспечением:
Плагин совместим с модулем Терминалы2 (https://connect.smartliving.ru/addons/category6/181.html) системы УД Majordomo (https://mjdm.ru/) и может быть использован в качестве "плеера" ТТС для озвучивания сообщений УД.

Особенности:
В силу специфики плеера системных звуков KODI (через который реализовано воспроизведение) - любая команда на воспроизведение звука через плагин будет приводть или к снятию с паузы воспроизводимого контента (если он в этот момент стоял на паузе), или ожиданию "ручного" снятия с паузы с последующим вопроизведением звука. Поведение настраиватся в настройках самого плагина.

ВНИМАНИЕ:
Для работы плагина не забудьте активировать управление по HTTP в настройках KODI (Настройки -> Сервисные настройки -> Управление -> Разрешить удаленное управление по HTTP) и установить "порт", "имя пользователя" и "пароль".



Примеры вызова функций методом GET (url можно ввести непосредственно в адресную строку браузера)
xbmc:xbmc - логин и пароль к KODI
192.168.1.51 - KODI
192.168.1.2 - удаленный сервер с хостингом картинок и звуковых файлов (например сервер Majordomo)

Определение доступности и готовности плагина к работе:
Модуль MDM terminals2 пингует плагин так: http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["ping"]},"id":1}
Если плагин доступен и работает, то в ответ приходит JSON с сообщением "OK".

Воспроизведение "стандартного" звука плагина:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["ringtone"]},"id":1}
Возможные значения: ringtone, welcome, incall, callend, batlow, STOP
при этом:
welcome, incall, callend, batlow останавливают текущее воспроизведение звука предыдущего сообщения
ringtone не останавливает текущее воспроизведение предыдущего звука и воспроизводится с "наложением" на другой выводимы плагином звук (например это может быть озвучивание ТТС от УД с наложением на него телефонного рингтона)
STOP - команда "остановить текущее (ранее запущенное) воспроизведение звука от этого аддона"


Воспроизведение звука из файла на локальном диске компьютера с KODI:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["D:\\test.wav"]},"id":1}
где D:\\test.wav путь к местоположению звукового файла в файловой системе компьютера с KODI

Воспроизведение звука по http url ссылке:
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["http://192.168.1.2/cms/cached/voice/rh_e4768dae4160a3eb9a57713580eff5e6.wav"]},"id":1}
где http://192.168.1.2/cms/cached/voice/rh_e4768dae4160a3eb9a57713580eff5e6.wav url к звуковому файлу

Вывод "стандартного" изображения плагина (управляющий операнд "PIC", X Y левой верхней точки картинки, ширина и высота выводимой картинки):
http://192.168.2.122:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["PIC","20","25","200","100","7","call_outgoing"]},"id":1}

Вывод произвольного изображения по http url ссылке:
http://192.168.2.122:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["PIC","20","25","200","100","7","http://192.168.1.2/img/my_picture.png"]},"id":1}

Показ произвольного текстового сообщения (управляющий операнд "MESSAGE", Title, Body, пиктограмма сопутствующая сообщению)::
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения"]},"id":1}
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", "7"]},"id":1}
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", "7", "mdm"]},"id":1}
http://xbmc:xbmc@192.168.1.51:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.alicevox.master","params":["MESSAGE", "SmartHome Alice", "Проверка подключения", "7", "http://192.168.1.2/img/logo_small.png"]},"id":1}
где:
7=длительность показа сообщения в секундах
mdm=стандартная картинка, вместо "mdm" может быть url ссылка на файл, например "http://192.168.1.2/img/logo.png"


Примеры работы с плагином из PHP в Majordomo

function send_command($address=null, $data=null, $timeout=3) {
	$_curlHdl = curl_init();
	curl_setopt($_curlHdl, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($_curlHdl, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($_curlHdl, CURLOPT_CONNECTTIMEOUT, 7);
	curl_setopt($_curlHdl, CURLOPT_TIMEOUT, $timeout);
	curl_setopt($_curlHdl, CURLOPT_TIMEOUT, $timeout);
	curl_setopt($_curlHdl, CURLINFO_HEADER_OUT, true);
	curl_setopt($_curlHdl, CURLOPT_POST, true);
	curl_setopt($_curlHdl, CURLOPT_POSTFIELDS, $data);
	curl_setopt($_curlHdl, CURLOPT_HTTPHEADER, array('Content-Type: application/json', 'Content-Length: ' . strlen($data)));

	$url =  $address.'/jsonrpc';
	curl_setopt($_curlHdl, CURLOPT_URL, $url);

	$answer = curl_exec($_curlHdl);
	if(curl_errno($_curlHdl)) {
		return array('error'=>curl_error($_curlHdl));
	}

	if ($answer == false) {
		return array('error'=>"Couldn't reach Kodi device.");
	}

	$answer = json_decode($answer, true);
	if (isset($answer['error']) ) return array('result'=>null, 'error'=>$answer['error']);
	return array('result'=>$answer['result']);
}



$host="htpc.home";
$port="8080";
$login="kodiLogin";
$password="kodiPassword";
$address = "http://".$login.":".$password."@".$host.":".$port;


$title = "Телефон";//Заголовок
$body = "Входящий звонок от +380501234567";//Тело сообщения
$showtime = "7";//Время показа сообщения

//$pic = "mdm";
//$pic = "ir";
//$pic = "mqtt";
//$pic = "mqtt_err";
//$pic = "phone";
//$pic = "attention";
//$pic = "construct";
//$pic = "mic";
//$pic = "night_mode";
//$pic = "retro_phone";
//$pic = "call_outgoing";
//$pic = "low_batt";
//$pic = "full_batt";
//$pic = "rewind";
$pic = "http://192.168.10.2/img/logo.png";

//Вывести текстовое сообщение о входящем телефонном звонке
$command = "{\"jsonrpc\":\"2.0\",\"method\":\"Addons.ExecuteAddon\",\"params\":{\"addonid\":\"script.alicevox.master\",\"params\":[\"MESSAGE\", \"$title\", \"$body\", \"$showtime\", \"$pic\"]},\"id\":1}";
$result = send_command($address, $command);


//$pic = "http://192.168.10.2/img/my_phone_picture.png";
$pic = "phone";
$x = 500;//X левый верхний угол вывода картинки
$y = 500;//Y левый верхний угол вывода картинки
$sx = 300;//X размер картинки
$sy = 300;//Y размер картинки
$showtime = "15";//Время показа картинки

//Вывести картинку
$command = "{\"jsonrpc\":\"2.0\",\"method\":\"Addons.ExecuteAddon\",\"params\":{\"addonid\":\"script.alicevox.master\",\"params\":[\"PIC\", \"$x\", \"$y\", \"$sx\", \"$sy\", \"$showtime\", \"$pic\"]},\"id\":1}";
$result = send_command($address, $command);


//$sound = "welcome";
$sound = "incall";
//$sound = "callend";
//$sound = "batlow";
//$sound = ringtone

//Сказать о входящем звонке (встоенное звуковое сообщение), но целессобразнее для голосовых опевещений использовать этот плагин в совокупности с "Терминалы2"
$command = "{\"jsonrpc\":\"2.0\",\"method\":\"Addons.ExecuteAddon\",\"params\":{\"addonid\":\"script.alicevox.master\",\"params\":[\"$sound\"]},\"id\":1}";
$result = send_command($address, $command);

$sound = ringtone

//и сразу же не прерывая произношения встоенного звукового сообщения проиграть рингтон
$command = "{\"jsonrpc\":\"2.0\",\"method\":\"Addons.ExecuteAddon\",\"params\":{\"addonid\":\"script.alicevox.master\",\"params\":[\"$sound\"]},\"id\":1}";
$result = send_command($address, $command);
