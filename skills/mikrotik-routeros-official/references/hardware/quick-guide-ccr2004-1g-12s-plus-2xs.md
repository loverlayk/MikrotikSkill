# Quick Guide - CCR2004-1G-12S+2XS

> It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed. :::

![](./img/mt_logo_arrow_v2-02-8.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.9 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
:::

This Quick Guide covers the model: CCR2004-1G-12S+2XS.

*This is Network Device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, Full EU Declaration of Conformity, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-8.png)

**First steps:**

- Connect your PC to the Ethernet1/Boot port;
- Connect the device to a power source;
- Configure the IP settings of your network card to 192.168.88.2/24;
- Use WebFig in a web browser or the "WinBox" configuration tool [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device. Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The equipment should only be connected to a socket outlet that is near the equipment and easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Electric shock hazard. This equipment is to be serviced by trained personnel only

Manufacturer: Mikrotikls SIA, Ūnijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.9 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби. Всички устройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е мрежово устройство. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, пълна ЕС декларация за съответствие, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-8.png)

**Първи стъпки:**

- Свържете вашия компютър с Ethernet1/Boot порта;
- Свържете устройството към източник на захранване;
- Конфигурирайте IP настройките на мрежовата ви карта на 192.168.88.2/24;
- Използвайте WebFig в уеб браузър или конфигурационния инструмент "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Отворете http://192.168.88.1 в уеб браузъра, за да стартирате настройката. Ако IP адресът не е достъпен, използвайте WinBox и изберете раздел "Neighbors", за да намерите устройството. Свържете се чрез MAC адреса. Потребителското име е "admin", а паролата липсва (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- Задайте паролата на вашия рутер.

**Информация за безопасност:**

- Преди да работите с каквото и да е оборудване на MikroTik, имайте предвид опасностите, свързани с електрическите вериги, и се запознайте със стандартните практики за предотвратяване на инциденти. Инсталаторът трябва да е запознат с мрежовите структури, термини и концепции.
- Използвайте само захранване и аксесоари, одобрени от производителя, които могат да бъдат намерени в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал, съгласно тези инструкции за монтаж. Инсталаторът е отговорен да се увери, че инсталацията на оборудването е в съответствие с местните и националните електрически кодекси. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за инсталиране на закрито. Пазете този продукт далеч от вода, огън, влага или горещи среди.
- Не можем да гарантираме, че няма да възникнат инциденти или щети поради неправилна употреба на устройството. Моля, използвайте този продукт внимателно и работете на свой собствен риск!
- Оборудването трябва да се свързва само към контакт, който е близо до оборудването и е лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е като изключите захранващия адаптер от контакта.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определени пунктове за събиране във вашия район.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се наложи да предприеме адекватни мерки!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Опасност от токов удар Това оборудване трябва да се обслужва само от обучен персонал

Производител: Mikrotikls SIA, Ūnijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.9 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy. Všechna zařízení MikroTik musí být profesionálně nainstalován.
Tento Stručný průvodce se týká modelu: CCR2004-1G-12S+2XS.
:::

*Toto je síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Technické specifikace, úplné EU prohlášení o shodě, brožury a další informace o produktech na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-8.png)

**První kroky:**

- Připojte váš počítač k portu Ethernet1/Boot;
- Připojte zařízení k zdroji napájení;
- Nakonfigurujte IP nastavení vaší síťové karty na 192.168.88.2/24;
- Použijte WebFig v webovém prohlížeči nebo konfigurační nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Otevřete http://192.168.88.1 ve webovém prohlížeči pro spuštění nastavení. Pokud není IP adresa k dispozici, použijte WinBox a vyberte záložku "Neighbors" k nalezení zařízení. Pokračujte v připojení pomocí MAC adresy. Uživatelské jméno je "admin", a není žádné heslo (nebo, pro některé modely, zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do menu "Files" ve WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a bezpečnostní aktualizace;
- Nastavte heslo pro váš router.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si nebezpečí spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalační program by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které naleznete v originálním balení tohoto výrobku.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle tohoto návodu k instalaci. Instalační technik je odpovědný za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat nebo upravovat.
- Tento produkt je určen k instalaci uvnitř. Udržujte tento produkt mimo dosah vody, ohně, vlhkosti nebo horkého prostředí.
- Nemůžeme zaručit, že nedojde k žádným nehodám nebo škodám v důsledku nesprávného použití zařízení. Používejte prosím tento výrobek opatrně a provozujte jej na vlastní nebezpečí!
- Zařízení by mělo být připojeno pouze k zásuvce, která je v blízkosti zařízení a je snadno dostupná.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejší způsob, jak toho dosáhnout, je odpojit napájecí adaptér ze zásuvky.
- Abyste zabránili kontaminaci životního prostředí, oddělte zařízení od domovního odpadu a zlikvidujte jej bezpečným způsobem, například na místech k tomu určených. Seznamte se s postupy správné přepravy zařízení do určených sběrných míst ve vaší oblasti.
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobovat rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Nebezpečí úrazu elektrickým proudem. Servis tohoto zařízení smí provádět pouze vyškolený personál

Výrobce: Mikrotikls SIA, Ūnijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.9 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler. Alle MikroTik-enheder skal være professionelt installeret.
:::

*Dette er netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, fuld EU-overensstemmelseserklæring, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-8.png)

**Første trin:**

- Forbind din computer til Ethernet1/Boot-porten;
- Forbind enheden til en strømkilde;
- Konfigurér IP-indstillingerne på dit netværkskort til 192.168.88.2/24;
- Brug WebFig i en webbrowser eller konfigurationsværktøjet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Åbn http://192.168.88.1 i en webbrowser for at starte opsætningen. Hvis IP-adressen ikke er tilgængelig, skal du bruge WinBox og forbinde ved hjælp af MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload downloadede pakker til WebFig eller WinBox "Files" menu og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil din routeradgangskode.

**Sikkerhedsoplysninger:**

- Før du arbejder på noget MikroTik-udstyr, skal du være opmærksom på de farer, der er forbundet med elektriske kredsløb, og være bekendt med standardpraksis til at forebygge ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, termer og koncepter.
- Brug kun strømforsyning og tilbehør, der er godkendt af producenten, og som kan findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til denne installationsvejledning. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske regler. Forsøg ikke at adskille, reparere eller modificere enheden.
- Dette produkt er beregnet til at blive installeret indendørs. Hold dette produkt væk fra vand, ild, fugt eller varme omgivelser.
- Vi kan ikke garantere, at der ikke vil ske uheld eller skader på grund af forkert brug af enheden. Brug venligst dette produkt med omhu og brug på egen risiko!
- Udstyret bør kun tilsluttes en stikkontakt, der er i nærheden af ​​udstyret og let tilgængelig.
- I tilfælde af fejl på enheden, skal du afbryde den fra strømmen. Den hurtigste måde at gøre det på er ved at tage strømadapteren ud af stikkontakten.
- For at undgå forurening af miljøet skal du adskille apparatet fra husholdningsaffald og bortskaffe det på en sikker måde, f.eks. i afmærkede områder. Bliv fortrolig med procedurer for korrekt transport af udstyret til udpegede indsamlingssteder i dit område.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Risiko for elektrisk stød. Dette udstyr må kun serviceres af uddannet personale

Producent: Mikrotikls SIA, Ūnijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.9 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen. Alle MikroTik-Geräte müssen professionell installiert werden.

Diese Kurzanleitung behandelt das Modell: CCR2004-1G-12S+2XS.
:::

*Dies ist das Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Daten, vollständige EU-Konformitätserklärung, Broschüren und weitere Informationen zu Produkten unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-8.png)

**Erste Schritte:**

- Verbinden Sie Ihren PC mit dem Ethernet1/Boot-Port;
- Verbinden Sie das Gerät mit einer Stromquelle;
- Konfigurieren Sie die IP-Einstellungen Ihrer Netzwerkkarte auf 192.168.88.2/24;
- Verwenden Sie WebFig in einem Webbrowser oder das Konfigurationstool "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Öffnen Sie http://192.168.88.1 in einem Webbrowser, um das Setup zu starten. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie WinBox und stellen Sie über die Registerkarte "Neighbors" eine Verbindung zum Gerät her. Fahren Sie mit der Verbindung über die MAC-Adresse fort. Der Benutzername lautet "admin", und es gibt kein Passwort (oder, für einige Modelle, überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie eine optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Legen Sie Ihr Routerpasswort fest.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardpraktiken zur Unfallverhütung vertraut machen. Der Installateur sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das sich in der Originalverpackung dieses Produkts befindet.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Installation in Innenräumen vorgesehen. Halten Sie dieses Produkt von Wasser, Feuer, Feuchtigkeit oder heißen Umgebungen fern.
- Wir können nicht garantieren, dass es durch unsachgemäßen Gebrauch des Geräts zu keinen Unfällen oder Schäden kommt. Bitte verwenden Sie dieses Produkt mit Sorgfalt und auf eigene Gefahr!
- Das Gerät sollte nur an eine Steckdose angeschlossen werden, die sich in der Nähe des Geräts befindet und leicht zugänglich ist.
- Im Falle eines Geräteausfalls trennen Sie es bitte von der Stromversorgung. Am schnellsten geht das, indem Sie das Netzteil aus der Steckdose ziehen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport des Geräts zu ausgewiesenen Sammelstellen in Ihrer Nähe vertraut.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Stromschlaggefahr. Dieses Gerät darf nur von geschultem Personal gewartet werden

Hersteller: Mikrotikls SIA, Ūnijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.9 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών. Όλες οι συσκευές MikroTik πρέπει να εγκατασταθούν επαγγελματικά.

Αυτός ο γρήγορος οδηγός καλύπτει το μοντέλο: CCR2004-1G-12S+2XS.
:::

*Αυτή είναι η συσκευή δικτύου*. *Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, πλήρης δήλωση συμμόρφωσης ΕΕ, φυλλάδια και περισσότερες πληροφορίες σχετικά με τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-8.png)

**Πρώτα βήματα:**

- Συνδέστε τον υπολογιστή σας στη θύρα Ethernet1/Boot;
- Συνδέστε τη συσκευή σε πηγή ενέργειας;
- Διαμορφώστε τις ρυθμίσεις IP της κάρτας δικτύου σας σε 192.168.88.2/24;
- Χρησιμοποιήστε το WebFig σε ένα πρόγραμμα περιήγησης ή το εργαλείο ρύθμισης ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ανοίξτε το http://192.168.88.1 σε έναν πρόγραμμα περιήγησης στο διαδίκτυο για να ξεκινήσετε τη ρύθμιση. Εάν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το WinBox και επιλέξτε την καρτέλα "Neighbors" για να βρείτε τη συσκευή. Συνεχίστε συνδέοντας χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς χρήστη και ασύρματους κωδικούς στο αυτοκόλλητο);
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα κατεβασμένα πακέτα στο μενού "Files" του WebFig ή του WinBox και επανεκκινήστε τη συσκευή;
- Αναβαθμίζοντας το λογισμικό του RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να διασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Ορίστε τον κωδικό πρόσβασης του δρομολογητή σας.

**Οδηγίες ασφαλείας:**

- Πριν εργαστείτε σε οποιονδήποτε εξοπλισμό της MikroTik, να γνωρίζετε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και να εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης θα πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιείτε μόνο το τροφοδοτικό και τα εξαρτήματα που είναι εγκεκριμένα από τον κατασκευαστή, τα οποία βρίσκονται στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση ότι η εγκατάσταση του εξοπλισμού είναι συμβατή με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν προορίζεται για εγκατάσταση σε εσωτερικούς χώρους. Κρατήστε αυτό το προϊόν μακριά από νερό, φωτιά, υγρασία ή ζεστό περιβάλλον.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Ο εξοπλισμός πρέπει να συνδέεται μόνο σε πρίζα που βρίσκεται κοντά στον εξοπλισμό και είναι εύκολα προσβάσιμη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από το ρεύμα. Ο πιο γρήγορος τρόπος για να το κάνετε αυτό είναι αποσυνδέοντας το τροφοδοτικό από την πρίζα.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από τα οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένους χώρους. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.
- Αυτό είναι προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει παρεμβολές ραδιοφώνου, οπότε ενδέχεται να απαιτείται από τον χρήστη να λάβει επαρκή μέτρα!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Κίνδυνος ηλεκτροπληξίας. Αυτός ο εξοπλισμός πρέπει να συντηρείται μόνο από εκπαιδευμένο προσωπικό

Κατασκευαστής: Mikrotikls SIA, Ūnijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.9 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país. Todos los dispositivos MikroTik deben ser instalados por un profesional.

Esta guía rápida cubre el modelo: CCR2004-1G-12S+2XS.
:::

*Este es un dispositivo de red. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, Declaración de conformidad de la UE completa, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-8.png)

**Primeros pasos:**

- Conecta tu PC al puerto Ethernet1/Boot;
- Conecta el dispositivo a una fuente de alimentación;
- Configura las opciones IP de tu tarjeta de red a 192.168.88.2/24;
- Utilice WebFig en un navegador web o la herramienta de configuración "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Abre http://192.168.88.1 en un navegador web para comenzar la configuración. Si la dirección IP no está disponible, utiliza WinBox y selecciona la pestaña "Neighbors" para encontrar el dispositivo. Procede a conectar usando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifica los usuarios y contraseñas inalámbricas en la etiqueta);
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Sube los paquetes descargados al menú "Files" de WebFig o WinBox y reinicia el dispositivo;
- Al actualizar el software de tu RouterOS a la última versión, puedes asegurar un rendimiento óptimo, estabilidad y actualizaciones de seguridad;
- Configura la contraseña de tu enrutador.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los peligros relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras, los términos y los conceptos de la red.
- Utilice únicamente la fuente de alimentación y los accesorios aprobados por el fabricante, que se encuentran en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, de acuerdo con estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desarmar, reparar o modificar el dispositivo.
- Este producto está diseñado para ser instalado en interiores. Mantenga este producto alejado del agua, el fuego, la humedad o los ambientes calientes.
- No podemos garantizar que no se produzcan accidentes o daños debido al uso inadecuado del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- El equipo solo debe conectarse a una toma de corriente que esté cerca del equipo y de fácil acceso.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desenchufando el adaptador de corriente de la toma de corriente.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en áreas designadas. Familiarícese con los procedimientos para transportar adecuadamente el equipo a los puntos de recolección designados en su área.
- Este es un producto de clase A. ¡En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Peligro de descarga eléctrica. Este equipo debe ser reparado solo por personal capacitado

Fabricante: Mikrotikls SIA, Ūnijas 2, Riga, Letonia, LV1039.

**Información México:**

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Ūnijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.9 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi. Kõik MikroTiku seadmed peavad olema professionaalselt paigaldatud.
See kiirjuhend hõlmab mudelit: CCR2004-1G-12S+2XS.
:::

*See on võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised andmed, täielik EL-i vastavusdeklaratsioon, brošüürid ja lisateave toodete kohta aadressil [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-8.png)

**Esimesed sammud:**

- Ühenda oma arvuti Ethernet1/Boot pordiga;
- Ühenda seade toiteallikaga;
- Konfigureeri oma võrgukaardi IP-seaded 192.168.88.2/24;
- Kasutage WebFigi veebi­brauseris või seadistus­tööriista "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Ava http://192.168.88.1 veebibrauseris seadistamise alustamiseks. Kui IP-aadress pole kättesaadav, kasuta WinBoxi ja vali seade leidmiseks "Neighbors" vahekaart. Jätka ühendamist MAC-aadressi kasutades. Kasutajanimi on "admin" ja parooli pole (või mõne mudeli puhul kontrollige kasutaja- ja traadita paroole kleebisel);
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Lae allalaaditud paketid üles veebibrauseri WebFig või WinBox "Files" menüüsse ja taaskäivita seade;
- Värskendades RouterOS tarkvara viimasele versioonile, tagad optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadista ruuteri parool.

**Ohutusteave:**

- Enne MikroTiku seadmega töötamist olge teadlik elektriskeemiga kaasnevatest ohtudest ja tutvuge õnnetuste ärahoidmise tavapäraste tavadega. Paigaldaja peaks olema tuttav võrgustruktuuride, terminite ja mõistetega.
- Kasutage ainult tootja poolt heakskiidetud toiteallikat ja tarvikuid, mis leiate selle toote originaalpakendist.
- Selle seadme peavad paigaldama koolitatud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmete paigaldamine vastaks kohalikele ja riiklikele elektrieeskirjadele. Ärge püüdke seadet lahti võtta, parandada ega muuta.
- See toode on ette nähtud paigaldamiseks siseruumidesse. Hoidke seda toodet eemal veest, tulest, niiskusest või kuumast keskkonnast.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja omal vastutusel!
- Seadet tohib ühendada ainult pistikupessa, mis on seadme lähedal ja kergesti ligipääsetav.
- Seadme rikke korral ühendage see vooluvõrgust lahti. Kiireim viis seda teha on toiteadapteri vooluvõrgust lahti ühendamine.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja visake see ohutul viisil, näiteks selleks ettenähtud kohtadesse. Tutvuge seadmete õige transportimise protseduuridega teie piirkonnas määratud kogumispunktidesse.
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid - sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Elektrilöögi oht. Seda seadet tohivad hooldada ainult koolitatud töötajad

Tootja: Mikrotikls SIA, Ūnijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.9 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja. Kaikkien MikroTik-laitteiden on oltava ammattimaisesti asennettu.
Tämä pikaopas kattaa mallin: CCR2004-1G-12S+2XS.
:::

*Tämä on verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, täydellinen EU-vaatimustenmukaisuusvakuutus, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-8.png)

**Ensiaskeleet:**

- Yhdistä tietokoneesi Ethernet1/Boot-porttiin;
- Liitä laite virtalähteeseen;
- Määritä verkkokorttisi IP-asetukset 192.168.88.2/24;
- Käytä WebFigiä web-selaimessa tai konfigurointityökalua "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Avaa http://192.168.88.1 verkkoselaimeen aloittaaksesi asennuksen. Jos IP-osoite ei ole käytettävissä, käytä WinBoxia ja valitse "Neighbors" -välilehti laitteen löytämiseksi. Jatka yhdistämistä MAC-osoitteen avulla. Käyttäjänimi on "admin", eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjä- ja langattomat salasanat tarrasta);
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFigin tai WinBoxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvallisuuspäivitykset;
- Aseta reitittimesi salasana.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden parissa, ole tietoinen sähköpiirien vaaroista ja tunne tavallisia käytäntöjä onnettomuuksien ehkäisemiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäisestä pakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentaja on vastuussa siitä, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi sisätiloihin. Pidä tämä tuote poissa vedestä, tulesta, kosteudesta tai kuumista ympäristöistä.
- Emme voi taata, että laitteen väärästä käytöstä johtuen ei tapahdu onnettomuuksia tai vahinkoja. Käytä tätä tuotetta varoen ja toimi omalla vastuullasi!
- Laite tulee kytkeä vain pistorasiaan, joka on lähellä laitetta ja johon pääsee helposti käsiksi.
- Jos laite epäonnistuu, irrota se virtalähteestä. Nopein tapa tehdä se on irrottaa virtalähde pistorasiasta.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla, esimerkiksi niille osoitetuille alueille. Tutustu menetelmiin, joilla laitteet kuljetetaan asianmukaisesti alueellasi oleviin keräyspisteisiin.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Sähköiskun vaara. Laitteita saa huoltaa vain koulutettu henkilöstö

Valmistaja: Mikrotikls SIA, Ūnijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.9 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays. Tous les appareils MikroTik doivent être installé professionnellement.
:::

*Ceci est un périphérique réseau. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, déclaration de conformité UE complète, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-8.png)

**Premiers pas:**

- Connectez votre PC au port Ethernet1/Boot;
- Connectez l'appareil à une source d'alimentation;
- Configurez les paramètres IP de votre carte réseau à 192.168.88.2/24;
- Utilisez WebFig dans un navigateur web ou l’outil de configuration "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Ouvrez http://192.168.88.1 dans un navigateur Web pour démarrer la configuration. Si l'adresse IP n'est pas disponible, utilisez WinBox et sélectionnez l'onglet "Neighbors" pour trouver le périphérique. Procédez à la connexion en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS à la dernière version, vous pouvez assurer des performances optimales, la stabilité et des mises à jour de sécurité;
- Configurez le mot de passe de votre routeur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des risques liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. L'installateur doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant, qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être installé à l'intérieur. Gardez ce produit à l'écart de l'eau, du feu, de l'humidité ou des environnements chauds.
- Nous ne pouvons pas garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec précaution et à vos risques et périls!
- L'équipement ne doit être connecté qu'à une prise de courant située à proximité de l'équipement et facilement accessible.
- En cas de panne de l'appareil, veuillez le débrancher de l'alimentation. Le moyen le plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Pour éviter la contamination de l'environnement, séparez l'appareil des ordures ménagères et jetez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Risque de choc électrique. Cet équipement doit être entretenu uniquement par du personnel qualifié

Fabricant: Mikrotikls SIA, Ūnijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.9 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise. Svi MikroTik uređaji moraju biti profesionalno instaliran.
Ovaj brzi vodič pokriva model: CCR2004-1G-12S+2XS.
:::

*Ovo je mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, puna EU izjava o sukladnosti, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-8.png)

**Prvi koraci:**

- Povežite svoje računalo s Ethernet1/Boot priključkom;
- Povežite uređaj s izvorom napajanja;
- Konfigurirajte IP postavke svoje mrežne kartice na 192.168.88.2/24;
- Koristite WebFig u web-pregledniku ili konfiguracijski alat "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Otvorite http://192.168.88.1 u web pregledniku kako biste započeli postavljanje. Ako IP adresa nije dostupna, koristite WinBox i odaberite karticu "Neighbors" da biste pronašli uređaj. Nastavite s povezivanjem putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Prenesite preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem softvera RouterOS na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- Postavite lozinku za svoj usmjerivač.

**Sigurnosne informacije:**

- Prije nego počnete raditi na bilo kojoj MikroTik opremi, budite svjesni opasnosti povezanih s električnim sklopovima i upoznajte se sa standardnim postupcima za sprječavanje nezgoda. Instalater bi trebao biti upoznat s mrežnim strukturama, terminima i konceptima.
- Koristite samo napajanje i pribor odobren od strane proizvođača, koji se nalaze u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba instalirati obučeno i kvalificirano osoblje, prema ovim uputama za instalaciju. Instalater je odgovoran osigurati da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastaviti, popraviti ili modificirati uređaj.
- Ovaj proizvod je namijenjen za ugradnju u zatvorenom prostoru. Držite ovaj proizvod podalje od vode, vatre, vlage ili vrućih okruženja.
- Ne možemo jamčiti da neće doći do nezgoda ili štete zbog nepravilne uporabe uređaja. Pažljivo koristite ovaj proizvod i radite na vlastitu odgovornost!
- Opremu treba priključiti samo na utičnicu koja je blizu opreme i lako dostupna.
- U slučaju kvara uređaja, isključite ga iz struje. Najbrži način da to učinite je isključivanjem adaptera iz strujne utičnice.
- Kako biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, primjerice, na za to predviđenim mjestima. Upoznajte se s postupcima za pravilan transport opreme do određenih sabirnih mjesta u vašem području.
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Opasnost od strujnog udara. Ovu opremu smije servisirati samo obučeno osoblje

Proizvođač: Mikrotikls SIA, Ūnijas 2, Riga, Latvija, LV1039.

## HI - हिंदी. त्वरित मार्गदर्शिका

:::warning
इस डिवाइस को स्थानीय प्राधिकरण के नियमों का पालन सुनिश्चित करने के लिए RouterOS v7.9 या नवीनतम संस्करण में अपग्रेड करना आवश्यक है!

स्थानीय देश के नियमों का पालन करना अंतिम उपयोगकर्ताओं की ज़िम्मेदारी है। सभी MikroTik डिवाइसों को पेशेवर रूप से इंस्टॉल किया जाना चाहिए।
:::

यह क्विक गाइड निम्नलिखित मॉडल को कवर करता है: CCR2004-1G-12S+2XS

*यह एक नेटवर्क डिवाइस है। उत्पाद मॉडल का नाम केस लेबल (ID) पर पाया जा सकता है।*
*पूर्ण और अद्यतन उपयोगकर्ता मैनुअल के लिए कृपया [https://mt.lv/um](https://mt.lv/um) पर जाएँ या अपने मोबाइल फोन से QR कोड स्कैन करें।*
*इस उत्पाद के सबसे महत्वपूर्ण तकनीकी विनिर्देश इस क्विक गाइड के अंतिम पृष्ठ पर दिए गए हैं।*
*तकनीकी विनिर्देश, EU अनुपालन घोषणा, ब्रॉशर, और उत्पादों की अधिक जानकारी के लिए देखें: [https://mikrotik.com/products](https://mikrotik.com/products)*
*आपकी भाषा में सॉफ़्टवेयर के लिए कॉन्फ़िगरेशन मैनुअल और अतिरिक्त जानकारी उपलब्ध है: [https://mt.lv/help](https://mt.lv/help)*
*MikroTik डिवाइस पेशेवर उपयोग के लिए हैं। यदि आपके पास आवश्यक योग्यताएँ नहीं हैं, तो कृपया किसी सलाहकार से संपर्क करें: [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/hi-um_2.badge.png)

**प्रारंभिक चरण:**

- अपने PC को Ethernet1/Boot पोर्ट से कनेक्ट करें;
- डिवाइस को बिजली के स्रोत से जोड़ें;
- अपने नेटवर्क कार्ड की IP सेटिंग को 192.168.88.2/24 पर कॉन्फ़िगर करें;
- WebFig को वेब ब्राउज़र में या “WinBox” कॉन्फ़िगरेशन टूल (https://mt.lv/WinBox) में उपयोग करें — कई कॉन्फ़िगरेशन विधियाँ उपलब्ध हैं ताकि पहुँच सुनिश्चित की जा सके;
- सेटअप शुरू करने के लिए वेब ब्राउज़र में http://192.168.88.1 खोलें। यदि IP पता उपलब्ध नहीं है, तो WinBox का उपयोग करके “Neighbors” टैब चुनें और डिवाइस खोजें। फिर MAC एड्रेस का उपयोग करके कनेक्ट करें। उपयोगकर्ता नाम "admin" है और पासवर्ड नहीं है (या कुछ मॉडलों के लिए, उपयोगकर्ता और वायरलेस पासवर्ड स्टिकर पर दिए गए होते हैं);
- डिवाइस को मैन्युअल रूप से अपडेट करने के लिए mikrotik.com पर जाएँ, अपना मॉडल चुनें और आवश्यक पैकेजों को "Downloads" सेक्शन में ढूँढें;
- डाउनलोड किए गए पैकेजों को WebFig या WinBox के “Files” मेनू में अपलोड करें और डिवाइस को रिबूट करें;
- अपने RouterOS सॉफ़्टवेयर को नवीनतम संस्करण में अपग्रेड करके प्रदर्शन, स्थिरता और सुरक्षा अद्यतनों को सुनिश्चित करें;
- अपने राउटर का पासवर्ड सेट करें।

**सुरक्षा जानकारी:**

- MikroTik उपकरण पर कार्य करने से पहले, विद्युत सर्किट से जुड़े खतरों के बारे में जान लें और दुर्घटनाओं को रोकने की मानक प्रक्रियाओं से परिचित हों। इंस्टॉलर को नेटवर्क संरचनाओं, शब्दावली और अवधारणाओं की जानकारी होनी चाहिए।
- केवल निर्माता द्वारा अनुमोदित पावर सप्लाई और एक्सेसरीज़ का ही उपयोग करें, जो इस उत्पाद की मूल पैकेजिंग में उपलब्ध होती हैं।
- यह उपकरण प्रशिक्षित और योग्य कर्मियों द्वारा इन इंस्टॉलेशन निर्देशों के अनुसार इंस्टॉल किया जाना चाहिए। इंस्टॉलर की ज़िम्मेदारी है कि स्थापना स्थानीय और राष्ट्रीय विद्युत कोडों के अनुरूप हो। डिवाइस को खोलने, मरम्मत करने या संशोधित करने का प्रयास न करें।
- यह उत्पाद केवल इनडोर स्थापना के लिए है। इसे पानी, आग, नमी या गर्म वातावरण से दूर रखें।
- हम यह गारंटी नहीं दे सकते कि डिवाइस के अनुचित उपयोग से कोई दुर्घटना या क्षति नहीं होगी। कृपया इस उत्पाद का सावधानीपूर्वक उपयोग करें और अपने जोखिम पर ही संचालन करें।
- उपकरण को केवल उस सॉकेट आउटलेट से जोड़ा जाना चाहिए जो उपकरण के पास और आसानी से सुलभ हो।
- यदि डिवाइस विफल हो जाए, तो कृपया उसे पावर से डिस्कनेक्ट करें। सबसे तेज़ तरीका है कि पावर प्लग को आउटलेट से निकाल दिया जाए।
- पर्यावरण को प्रदूषण से बचाने के लिए, डिवाइस को घरेलू कचरे से अलग करें और इसे सुरक्षित तरीके से निपटाएँ, जैसे कि निर्दिष्ट क्षेत्रों में। अपने क्षेत्र में निर्दिष्ट संग्रह बिंदुओं तक उपकरण को पहुँचाने की प्रक्रियाओं से अवगत हों।
- यह एक **Class A** उत्पाद है। घरेलू वातावरण में, यह उत्पाद रेडियो हस्तक्षेप कर सकता है, ऐसी स्थिति में उपयोगकर्ता को उपयुक्त उपाय करने की आवश्यकता हो सकती है।

![](./img/image2020-2-5_14-43-45.badge-2.png)

विद्युत झटका लगने का खतरा। इस उपकरण की सेवा केवल प्रशिक्षित कर्मियों द्वारा की जानी चाहिए।

**निर्माता:** Mikrotikls SIA, Ūnijas 2, रिगा, लातविया, LV1039

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.9-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása. Az összes MikroTik készüléknek lennie kell szakszerűen telepítve.
Ez a gyors útmutató a következőre vonatkozik: CCR2004-1G-12S+2XS.
:::

*Ez hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki adatok, teljes EU-megfelelőségi nyilatkozat, prospektusok és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products) oldalon*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-8.png)

**Első lépések:**

- Csatlakoztassa számítógépét az Ethernet1/Boot portra;
- Csatlakoztassa az eszközt egy tápellátóhoz;
- Konfigurálja hálózati kártyája IP beállításait 192.168.88.2/24-re;
- Használja a WebFig-et webböngészőben vagy a "WinBox” konfigurációs eszközt [https://mt.lv/winbox](https://mt.lv/winbox); **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Nyissa meg a http://192.168.88.1 címet egy webböngészőben a beállítás elindításához. Ha az IP cím nem elérhető, használja a WinBoxot, és válassza ki a "Neighbors" fület az eszköz megtalálásához. Folytassa a csatlakozást a MAC cím használatával. A felhasználónév "admin", és nincs jelszó (vagy, néhány modell esetén, ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- Az RouterOS szoftver frissítésével a legújabb verzióra biztosíthatja az optimális teljesítményt, stabilitást és biztonsági frissítéseket;
- Állítsa be a router jelszavát.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozna, legyen tisztában az elektromos áramkörökkel járó veszélyekkel, és ismerje meg a balesetek megelőzésére vonatkozó szabványos gyakorlatokat. A telepítőnek ismernie kell a hálózati struktúrákat, kifejezéseket és fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használja, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a berendezést képzett és szakképzett személyzetnek kell telepítenie a jelen szerelési útmutató szerint. A telepítő felelős azért, hogy megbizonyosodjon arról, hogy a berendezés telepítése megfelel a helyi és országos elektromos előírásoknak. Ne kísérelje meg szétszerelni, javítani vagy módosítani a készüléket.
- Ezt a terméket beltéri beszerelésre tervezték. Tartsa távol a terméket víztől, tűztől, nedvességtől vagy forró környezettől.
- Nem tudjuk garantálni, hogy a készülék nem rendeltetésszerű használatából eredő baleset vagy kár nem következik be. Kérjük, használja ezt a terméket körültekintően és saját felelősségére használja!
- A berendezést csak olyan aljzathoz szabad csatlakoztatni, amely a berendezés közelében van és könnyen hozzáférhető.
- A készülék meghibásodása esetén húzza ki az áramellátásból. Ennek leggyorsabb módja, ha kihúzza a hálózati adaptert a konnektorból.
- A környezet szennyeződésének elkerülése érdekében a készüléket különítse el a háztartási hulladéktól, és biztonságos módon, például a kijelölt helyen dobja ki. Ismerkedjen meg a berendezés megfelelő szállítási eljárásaival az Ön területén található kijelölt gyűjtőhelyekre.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználót szükség lehet megfelelő intézkedések megtételére!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Áramütés veszélye. Ezt a berendezést csak képzett személyzet javíthatja

Gyártó: Mikrotikls SIA, Ūnijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan Cepat

:::warning
Perangkat ini harus diperbarui ke RouterOS v7.9 atau versi terbaru untuk memastikan kepatuhan terhadap peraturan pemerintah setempat.
Merupakan tanggung jawab pengguna akhir untuk mengikuti peraturan setempat setempat. Semua perangkat MikroTik harus diinstal secara profesional.
Panduan memulai cepat ini mencakup model: CCR2004-1G-12S+2XS.
:::

*Ini adalah perangkat jaringan. Anda dapat menemukan nama model produk Anda pada label casing (ID).*
*Silakan kunjungi halaman panduan pengguna di [https://mt.lv/um-id](https://mt.lv/um-id) untuk panduan pengguna yang diperbarui sepenuhnya. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Memulai Cepat ini.*
*Spesifikasi teknis, pernyataan kesesuaian UE lengkap, brosur, dan informasi produk lebih lanjut di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Panduan penyiapan perangkat lunak dalam bahasa Anda beserta informasi tambahan tersedia di [https://mt.lv/help-id](https://mt.lv/help-id)*
*Perangkat MikroTik ditujukan untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi, silakan berkonsultasi dengan konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/indonesian_qr.badge.png)

**Langkah pertama:**

- Hubungkan PC Anda ke port Ethernet1/Boot;
- Hubungkan perangkat ke sumber listrik;
- Konfigurasikan pengaturan IP kartu jaringan Anda ke 192.168.88.2/24;
- Gunakan WebFig di peramban web atau alat konfigurasi "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Buka http://192.168.88.1 di browser web untuk memulai pengaturan. Jika alamat IP tidak tersedia, gunakan WinBox dan pilih tab "Neighbors" untuk menemukan perangkat. Lanjutkan untuk terhubung menggunakan alamat MAC. Nama penggunanya adalah "admin", dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu "File" WebFig atau WinBox dan reboot perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Siapkan kata sandi router Anda.

**Informasi keselamatan:**

- Sebelum mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik dan pahami praktik standar untuk pencegahan kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui produsen yang terdapat dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dimaksudkan untuk dipasang di dalam ruangan. Jauhkan produk ini dari air, api, kelembapan, atau lingkungan panas.
- Kami tidak dapat menjamin bahwa kecelakaan atau kerusakan tidak akan terjadi akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan pengoperasian dengan risiko Anda sendiri!
- Peralatan sebaiknya hanya disambungkan ke stopkontak yang dekat dengan peralatan dan mudah dijangkau.
- Jika terjadi kegagalan perangkat, putuskan sambungannya dari catu daya. Cara tercepat untuk melakukannya adalah dengan mencabut catu daya dari stopkontak.
- Untuk menghindari kontaminasi terhadap lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan aman, misalnya di tempat yang telah ditentukan. Pahami prosedur pengangkutan peralatan dengan benar ke tempat pengumpulan yang ditentukan di wilayah Anda.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio, sehingga pengguna mungkin diminta untuk mengambil tindakan yang memadai!

![](./img/image2020-2-5_14-43-45.badge-2.png)

Risiko sengatan listrik. Peralatan ini harus diperbaiki hanya oleh personel yang berkualifikasi

Pabrikan: Mikrotikls SIA, Ūnijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.9 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali. Tutti i dispositivi MikroTik devono essere installato professionalmente.
Questa guida rapida copre il modello: CCR2004-1G-12S+2XS.
:::

*Questo è il dispositivo di rete. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, dichiarazione di conformità UE completa, brochure e ulteriori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-8.png)

**Primi passi:**

- Collega il tuo PC alla porta Ethernet1/Boot;
- Collega il dispositivo a una fonte di alimentazione;
- Configura le impostazioni IP della tua scheda di rete a 192.168.88.2/24;
- Utilizzare WebFig in un browser web oppure lo strumento di configurazione "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Apri http://192.168.88.1 in un browser web per avviare la configurazione. Se l'indirizzo IP non è disponibile, utilizza WinBox e scegli la scheda "Neighbors" per trovare il dispositivo. Prosegui con la connessione utilizzando l'indirizzo MAC. Il nome utente è "admin", e non c'è una password (o, per alcuni modelli, controlla gli utenti e le password wireless sull'etichetta);
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Imposta la password del tuo router.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, essere consapevoli dei pericoli connessi con i circuiti elettrici e acquisire familiarità con le pratiche standard per la prevenzione degli incidenti. L'installatore deve avere familiarità con le strutture, i termini ei concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore, che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, come da queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è destinato ad essere installato all'interno. Tenere questo prodotto lontano da acqua, fuoco, umidità o ambienti caldi.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e operare a proprio rischio!
- L'apparecchiatura deve essere collegata solo a una presa di corrente vicina all'apparecchiatura e facilmente accessibile.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio nelle aree designate. Acquisire familiarità con le procedure per il trasporto corretto dell'apparecchiatura ai punti di raccolta designati nella propria zona.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Rischio di scosse elettriche. Questa apparecchiatura deve essere riparata solo da personale qualificato

Produttore: Mikrotikls SIA, Ūnijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.9 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum. Öll MikroTik tæki verða að vera fagmannlega sett upp.

Þessi snögga leiðbeining nær yfir gerðina: CCR2004-1G-12S+2XS.
:::

*Þetta er net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tækniforskriftir, full ESB-samræmisyfirlýsing, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-8.png)

**Fyrstu skrefin:**

- Tengdu tölvuna þína við Ethernet1/Boot-portinn;
- Tengdu tækið við aflgjafa;
- Stilla IP stillingar netkortsins þíns á 192.168.88.2/24;
- Notið WebFig í vefvafra eða uppsetningartól "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Opnaðu http://192.168.88.1 í vefskoðara til að byrja uppsetningu. Ef IP heimilið er ekki tiltækt, notaðu WinBox og veljaðu "Neighbors" flipann til að finna tækið. Halda áfram með að tengjast með MAC heimilisfangi. Notandanafnið er "admin", og engin lykilorð er (eða, fyrir sumar módel, athugaðu notandanöfn og þráðlausa lykilorð á merki);
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum á WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Með því að uppfæra RouterOS hugbúnaðinn þinn í nýjustu útgáfu getur þú tryggjað bestu árangur, stöðugleika og öryggisuppfærslur;
- Stilla lykilorðið á routerinum þínu.

**Öryggisupplýsingar:**

- Áður en þú vinnur á MicroTik búnaði skaltu vera meðvitaður um hætturnar sem fylgja rafrásum og þekkja staðlaðar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að þekkja netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt, sem er að finna í upprunalegum umbúðum þessarar vöru.
- Þennan búnað á að setja upp af þjálfuðu og hæfu starfsfólki, samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn er ábyrgur fyrir því að ganga úr skugga um að uppsetning búnaðarins sé í samræmi við staðbundin og landsbundin rafmagnsreglur. Ekki reyna að taka í sundur, gera við eða breyta tækinu.
- Þessari vöru er ætlað að setja upp innandyra. Haltu þessari vöru frá vatni, eldi, raka eða heitu umhverfi.
- Við getum ekki ábyrgst að engin slys eða skemmdir eigi sér stað vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og notaðu á eigin ábyrgð!
- Búnaðurinn ætti aðeins að vera tengdur við innstungu sem er nálægt búnaðinum og aðgengilegur.
- Ef tækið bilar, vinsamlegast taktu það úr sambandi. Fljótlegasta leiðin til að gera það er með því að taka straumbreytinn úr sambandi.
- Til að forðast mengun umhverfisins skal skilja tækið frá heimilissorpi og farga því á öruggan hátt, td á afmörkuðum svæðum. Kynntu þér verklagsreglur um að flytja búnaðinn á viðeigandi söfnunarstaði á þínu svæði.
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri fullnægjandi ráðstafanir!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Hætta á raflosti. Þessum búnaði er einungis heimilt að nota af þjálfuðum starfsmönnum

Framleiðandi: Mikrotikls SIA, Ūnijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.9 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter. Alle MikroTik-enheter må være profesjonelt installert.
:::

*Dette er nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, full EU-samsvarserklæring, brosjyrer og mer informasjon om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-8.png)

**Første steg:**

- Koble PC-en din til Ethernet1/Boot-porten;
- Koble enheten til en strømkilde;
- Konfigurer IP-innstillingene på nettverkskortet ditt til 192.168.88.2/24;
- Bruk WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Åpne http://192.168.88.1 i en nettleser for å starte oppsettet. Hvis IP-adressen ikke er tilgjengelig, bruk WinBox og velg "Neighbors"-fanen for å finne enheten. Fortsett å koble til ved hjelp av MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig eller WinBox "Files"-menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen, kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- Sett opp passordet for ruteren din.

**Sikkerhetsinformasjon:**

- Før du arbeider på noe MikroTik-utstyr, må du være klar over farene forbundet med elektriske kretser, og være kjent med standard praksis for å forhindre ulykker. Installatøren bør være kjent med nettverksstrukturer, termer og konsepter.
- Bruk kun strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av opplært og kvalifisert personell, i henhold til disse installasjonsinstruksjonene. Installatøren er ansvarlig for å sørge for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske forskrifter. Ikke forsøk å demontere, reparere eller modifisere enheten.
- Dette produktet er ment å installeres innendørs. Hold dette produktet unna vann, brann, fuktighet eller varme omgivelser.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk på egen risiko!
- Utstyret skal kun kobles til en stikkontakt som er i nærheten av utstyret og lett tilgjengelig.
- Ved feil på enheten, koble den fra strømmen. Den raskeste måten å gjøre det på er ved å koble strømadapteren fra strømuttaket.
- For å unngå forurensning av miljøet, separer enheten fra husholdningsavfallet og kast den på en sikker måte, for eksempel i anviste områder. Gjør deg kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Fare for elektrisk støt. Dette utstyret skal kun repareres av trent personell

Produsent: Mikrotikls SIA, Ūnijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.9“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi. Visi „MikroTik“ prietaisai turi būti profesionaliai sumontuota.
Šis trumpasis vadovas apima modelį: CCR2004-1G-12S+2XS.
:::

*Tai yra tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, visa ES atitikties deklaracija, brošiūros ir daugiau informacijos apie gaminius adresu [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-8.png)

**Pirmieji žingsniai:**

- Prijunkite savo kompiuterį prie Ethernet1/Boot prievado;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Sukonfigūruokite savo tinklo plokštės IP nustatymus į 192.168.88.2/24;
- Naudokite WebFig naršyklėje arba konfigūravimo įrankį "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atidarykite http://192.168.88.1 naršyklėje, norėdami pradėti sąranką. Jei IP adresas nepasiekiamas, naudokite WinBox ir pasirinkite "Neighbors" skirtuką, kad rastumėte įrenginį. Tęskite prisijungdami naudodami MAC adresą. Vartotojo vardas yra "admin", o slaptažodžio nėra (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite įrenginį iš naujo;
- Atnaujindami savo RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Nustatykite savo maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš dirbdami su bet kokia „MikroTik“ įranga, atkreipkite dėmesį į pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine nelaimingų atsitikimų prevencijos praktika. Diegėjas turi būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintą maitinimo šaltinį ir priedus, kuriuos rasite originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokytas ir kvalifikuotas personalas, kaip nurodyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įrangos montavimas atitiktų vietinius ir nacionalinius elektros kodeksus. Nebandykite išardyti, taisyti ar modifikuoti įrenginio.
- Šis gaminys skirtas montuoti patalpose. Saugokite šį gaminį nuo vandens, ugnies, drėgmės ar karštos aplinkos.
- Negalime garantuoti, kad dėl netinkamo prietaiso naudojimo neįvyks nelaimingų atsitikimų ar žalos. Prašome naudoti šį gaminį atsargiai ir rizikuoti!
- Įranga turi būti jungiama tik prie kištukinio lizdo, kuris yra šalia įrangos ir lengvai pasiekiamas.
- Įrenginio gedimo atveju atjunkite jį nuo maitinimo šaltinio. Greičiausias būdas tai padaryti – ištraukti maitinimo adapterį iš elektros lizdo.
- Kad išvengtumėte aplinkos užteršimo, atskirkite įrenginį nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis produktas gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Elektros šoko pavojus. Šią įrangą turi prižiūrėti tik apmokytas personalas

Gamintojas: Mikrotikls SIA, Ūnijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.9 vai jaunāku versiju, lai nodrošinātu atbilstību vietējās likumdošanas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus. Visām MikroTik ierīcēm jābūt profesionāli uzstādītām.
Šī īsā rokasgrāmata attiecas uz modeli: CCR2004-1G-12S+2XS.
:::

*Šī ir tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, pilna ES atbilstības deklarācija, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-8.png)

**Pirmie soļi:**

- Pievienojiet savu datoru Ethernet1/Boot portam;
- Pievienojiet ierīci pie strāvas avota;
- Konfigurējiet savas tīkla kartes IP iestatījumus uz 192.168.88.2/24;
- Izmantojiet WebFig tīmekļa pārlūkā vai konfigurācijas rīku "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Atveriet http://192.168.88.1 tīmekļa pārlūkprogrammā, lai sāktu iestatīšanu. Ja IP adrese nav pieejama, izmantojiet WinBox un atlasiet cilni "Neighbors", lai atrastu ierīci. Turpiniet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav parole (vai, dažiem modeļiem, pārbaudiet lietotāja un bezvadu paroles uz līmplēves);
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox "Files" izvēlni un pārstartējiet ierīci;
- Jauninot savu RouterOS programmatūru līdz jaunākajai versijai, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Iestatiet sava maršrutētāja paroli.

**Drošības informācija:**

- Pirms strādājat pie jebkuras MikroTik iekārtas, apzinieties ar elektriskām shēmām saistītos riskus un iepazīstieties ar standarta praksi negadījumu novēršanai. Instalētājam jāpārzina tīkla struktūras, termini un jēdzieni.
- Izmantojiet tikai ražotāja apstiprināto barošanas bloku un piederumus, kas ir atrodami šī izstrādājuma oriģinālajā iepakojumā.
- Šis aprīkojums ir jāuzstāda apmācītam un kvalificētam personālam saskaņā ar šiem uzstādīšanas norādījumiem. Uzstādītājs ir atbildīgs par to, lai iekārtas uzstādīšana atbilstu vietējiem un valsts elektriskajiem noteikumiem. Nemēģiniet izjaukt, salabot vai pārveidot ierīci.
- Šis produkts ir paredzēts uzstādīšanai iekštelpās. Sargājiet šo izstrādājumu no ūdens, uguns, mitruma vai karstas vides.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ nenotiks negadījumi vai bojājumi. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Elektriskās strāvas trieciena risks. Šo aprīkojumu drīkst apkalpot tikai apmācīts personāls.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.9 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż. L-apparati kollha MikroTik iridu jkunu installati professjonalment.

Din il-Gwida Quick tkopri l-mudell: CCR2004-1G-12S+2XS.
:::

*Dan huwa apparat tan-netwerk. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, Dikjarazzjoni Sħiħa ta' Konformità tal-UE, fuljetti, u aktar informazzjoni dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-8.png)

**L-ewwel passi:**

- Ikkonnettja l-kompjuter tiegħek mal-port Ethernet1/Boot;
- Ikkonnettja d-dispositiv għal sors ta' enerġija;
- Ikkonfigurat is-settings IP tal-karta tan-netwerk tiegħek għal 192.168.88.2/24;
- Uża WebFig f’web browser jew l-għodda ta’ konfigurazzjoni “WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Agħlaq http://192.168.88.1 f'browser web biex tibda l-setup. Jekk l-indirizz IP mhux disponibbli, uża l-WinBox u għażel it-tab "Neighbors" biex tiskopri d-dispositiv. Kompli b'konnessjoni bl-użu tal-MAC address. Il-username huwa "admin", u m'hemmx password ( jew, għal xi mudelli, iċċekkja passwords tal-utent u tal-wi-fi fuq l-isticker);
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Uploadja tal-pakketti miżjuda fil-menu "Files" ta' WebFig jew WinBox u rerew boot l-apparat;
- Billi tnaqqas il-software RouterOS tiegħek għall-aħħar verżjoni, tista' tażżura prestazzjoni ottimale, stabbiltà u aġġornamenti ta' sikurezza;
- Iffurmat il-password tar-router tiegħek.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jiġi installat fuq ġewwa. Żomm dan il-prodott 'il bogħod minn ilma, nar, umdità jew ambjenti sħan.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Periklu ta 'xokk elettriku. Dan it-tagħmir għandu jkun innotifikat minn persunal imħarreġ biss

Manifattur: Mikrotikls SIA, Ūnijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.9 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften. Alle MikroTik-apparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, volledige EU-conformiteitsverklaring, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-8.png)

**Eerste stappen:**

- Verbind uw pc met de Ethernet1/Boot-poort;
- Sluit het apparaat aan op een stroombron;
- Configureer de IP-instellingen van uw netwerkkaart naar 192.168.88.2/24;
- Gebruik WebFig in een webbrowser of de configuratietool "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Open http://192.168.88.1 in een webbrowser om de installatie te starten. Als het IP-adres niet beschikbaar is, gebruik dan WinBox en kies het tabblad "Neighbors" om het apparaat te vinden. Ga verder met verbinden via het MAC-adres. De gebruikersnaam is "admin" en er is geen wachtwoord (of, voor sommige modellen, controleer gebruikers- en draadloze wachtwoorden op de sticker);
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Stel het wachtwoord van uw router in.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om binnenshuis te worden geïnstalleerd. Houd dit product uit de buurt van water, vuur, vochtigheid of hete omgevingen.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Het stopcontact moet in de buurt van de apparatuur worden geïnstalleerd en moet gemakkelijk toegankelijk zijn.
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.
- Dit is een Klasse A-product. In een huiselijke omgeving kan dit product radio-interferentie veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen moet nemen!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Gevaar voor elektrische schokken. Deze apparatuur mag alleen worden onderhouden door opgeleid personeel

Fabrikant: Mikrotikls SIA, Ūnijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.9 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych. Wszystkie urządzenia MikroTik muszą być profesjonalnie zainstalowany.
Niniejszy Krótki przewodnik obejmuje model: CCR2004-1G-12S+2XS.
:::

*To jest urządzenie sieciowe. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Specyfikacje techniczne, pełna deklaracja zgodności UE, broszury i więcej informacji o produktach na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-8.png)

**Pierwsze kroki:**

- Podłącz swój komputer do portu Ethernet1/Boot;
- Podłącz urządzenie do źródła zasilania;
- Skonfiguruj ustawienia IP karty sieciowej na 192.168.88.2/24;
- Użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Otwórz http://192.168.88.1 w przeglądarce internetowej, aby rozpocząć konfigurację. Jeśli adres IP jest niedostępny, użyj WinBox i wybierz zakładkę "Neighbors", aby znaleźć urządzenie. Kontynuuj łączenie za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła nie ma (lub, dla niektórych modeli, sprawdź nazwy użytkowników i hasła bezprzewodowe na naklejce);
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Prześlij pobrane paczki do menu "Files" WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- Skonfiguruj hasło do routera.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt jest przeznaczony do instalacji w pomieszczeniach. Trzymaj ten produkt z dala od wody, ognia, wilgoci lub gorących środowisk.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- Gniazdko powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w takim przypadku użytkownik może być zobowiązany do podjęcia odpowiednich kroków!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Zagrożenie porażeniem prądem elektrycznym. Sprzęt ten może być serwisowany wyłącznie przez przeszkolony personel

Producent: Mikrotikls SIA, Ūnijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.9 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país. Todos os dispositivos MikroTik devem ser instalado profissionalmente.
Este Guia Rápido cobre o modelo: CCR2004-1G-12S+2XS.
:::

*Este é o dispositivo de rede. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, Declaração de conformidade completa da UE, folhetos e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-8.png)

**Primeiros passos:**

- Conecte o seu PC à porta Ethernet1/Boot;
- Conecte o dispositivo a uma fonte de alimentação;
- Configure as definições de IP do seu cartão de rede para 192.168.88.2/24;
- Use o WebFig num navegador ou a ferramenta de configuração "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Abra http://192.168.88.1 num navegador web para iniciar a configuração. Se o endereço IP não estiver disponível, utilize o WinBox e escolha a aba "Neighbors" para encontrar o dispositivo. Prossiga para conectar usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique os nomes de usuário e senhas sem fio no adesivo);
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Faça o upload dos pacotes baixados para o menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar o software do RouterOS para a versão mais recente, você pode garantir um desempenho, estabilidade e atualizações de segurança ótimos;
- Configure a senha do seu roteador.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser instalado em ambiente interno. Mantenha este produto longe de água, fogo, umidade ou ambientes quentes.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- A tomada deve ser instalada próxima ao equipamento e deve ser de fácil acesso.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Perigo de choque elétrico. Este equipamento deve ser reparado apenas por pessoal treinado

Fabricante: Mikrotikls SIA, Ūnijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.9 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării. Toate dispozitivele MikroTik trebuie să fie instalat profesional.
Acest Ghid rapid acoperă modelul: CCR2004-1G-12S+2XS.
:::

*Acesta este dispozitivul de rețea. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, Declarație de conformitate UE completă, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-8.png)

**Primii pasi:**

- Conectați-vă PC-ul la portul Ethernet1/Boot;
- Conectați dispozitivul la o sursă de alimentare;
- Configurați setările IP ale plăcii de rețea la 192.168.88.2/24;
- Utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Deschideți http://192.168.88.1 într-un browser web pentru a începe configurarea. Dacă adresa IP nu este disponibilă, utilizați WinBox și alegeți fila "Neighbors" pentru a găsi dispozitivul. Continuați conectarea folosind adresa MAC. Numele de utilizator este "admin", și nu există parolă (sau, pentru unele modele, verificați utilizatori și parole wireless pe autocolant);
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanță optimă, stabilitate și actualizări de securitate;
- Setați parola routerului.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie instalat în interior. Păstrați acest produs departe de apă, foc, umiditate sau medii calde.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-le într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător al echipamentelor la punctele de colectare desemnate din zona dumneavoastră.
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Pericol de electrocutare. Acest echipament va fi deservit doar de personal instruit

Producător: Mikrotikls SIA, Ūnijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.9 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny. Všetky zariadenia MikroTik musia byť profesionálne nainštalovaný.
Táto Stručná príručka sa týka modelu: CCR2004-1G-12S+2XS.
:::

*Toto je sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete nastránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Technické špecifikácie, úplné EÚ vyhlásenie o zhode, brožúry a ďalšie informácie o produktoch na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-8.png)

**Prvé kroky:**

- Pripojte váš počítač k portu Ethernet1/Boot;
- Pripojte zariadenie k zdroju napájania;
- Nakonfigurujte IP nastavenia vašej sieťovej karty na 192.168.88.2/24;
- Použite WebFig v webovom prehliadači alebo konfiguračný nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Otvorte http://192.168.88.1 vo webovom prehliadači pre začiatok nastavenia. Ak nie je k dispozícii IP adresa, použite WinBox a vyberte kartu "Neighbors" na nájdenie zariadenia. Pokračujte v pripájaní pomocou MAC adresy. Užívateľské meno je "admin", a nie je heslo (alebo, pre niektoré modely, skontrolujte užívateľské a heslá pre bezdrôtové pripojenie na štítku);
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" vo WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálnu výkon, stabilitu a bezpečnostné aktualizácie;
- Nastavte heslo pre váš router.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je určený na inštaláciu vo vnútri. Chráňte tento výrobok pred vodou, ohňom, vlhkosťou alebo horúcim prostredím.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Nebezpečenstvo úrazu elektrickým prúdom. Servis tohto zariadenia smie vykonávať iba vyškolený personál

Výrobca: Mikrotikls SIA, Ūnijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.9 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom. Vse naprave MikroTik morajo biti strokovno nameščen.
Ta hitri vodnik zajema model: CCR2004-1G-12S+2XS.
:::

*To je omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Tehnične specifikacije, popolna izjava o skladnosti EU, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-8.png)

**Prvi koraki:**

- Povežite svoj računalnik s priključkom Ethernet1/Boot;
- Povežite napravo z napajalnikom;
- Nastavite IP nastavitve svoje omrežne kartice na 192.168.88.2/24;
- Uporabite WebFig v spletni brskalniku ali konfiguracijsko orodje "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Odpri http://192.168.88.1 v spletnem brskalniku, da začneš nastavljanje. Če IP naslov ni na voljo, uporabi WinBox in izberi zavihek "Neighbors" za iskanje naprave. Nadaljuj s povezovanjem prek MAC naslova. Uporabniško ime je "admin", in ni gesla (ali, za nekatere modele, preveri uporabniška imena in gesla brezžične povezave na nalepki);
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico zagotovite optimalno delovanje, stabilnost in varnostne posodobitve;
- Nastavite geslo za svoj usmerjevalnik.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen namestitvi v zaprtih prostorih. Izdelek hranite ločeno od vode, ognja, vlage ali vročega okolja.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje; v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Nevarnost električnega udara To opremo lahko servisira samo usposobljeno osebje

Proizvajalec: Mikrotikls SIA, Ūnijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.9 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler. Alla MikroTik-enheter måste vara professionellt installerat.
:::

*Det här är nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, fullständig EU-försäkran om överensstämmelse, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-8.png)

**Första stegen:**

- Anslut din dator till Ethernet1/Boot-porten;
- Anslut enheten till en strömkälla;
- Konfigurera IP-inställningarna för ditt nätverkskort till 192.168.88.2/24;
- Använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Öppna http://192.168.88.1 i en webbläsare för att starta inställningen. Om IP-adressen inte är tillgänglig, använd WinBox och välj fliken "Neighbors" för att hitta enheten. Fortsätt att ansluta med MAC-adressen. Användarnamnet är "admin", och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- Ställ in lösenordet för din router.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att installeras inomhus. Håll produkten borta från vatten, eld, luftfuktighet eller heta miljöer.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Risk för elektrisk chock. Denna utrustning ska endast utföras av utbildad personal

Tillverkare: Mikrotikls SIA, Ūnijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.9或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规。所有 MikroTik 设备都必须经过专业安装。

本快速指南介绍了以下型号：CCR2004-1G-12S+2XS。
:::

*这是网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*技术规格、完整的欧盟符合性声明、手册以及有关产品的更多信息，请访问 [https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-8.png)

**第一步：**

- 将您的计算机连接到Ethernet1/Boot端口;
- 将设备连接到电源;
- 配置您网络卡的IP设置为192.168.88.2/24;
- 在网络浏览器中使用 WebFig 或使用“WinBox”配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) **提供多种配置方法以确保可访问性；**
- 在Web浏览器中打开http://192.168.88.1 以开始设置。如果IP地址不可用，请使用WinBox并选择“Neighbors”选项卡查找设备。通过MAC地址继续连接。用户名是“admin”，没有密码（或者对于某些型号，请检查贴纸上的用户和无线密码）;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的“Files”菜单，并重新启动设备;
- 通过将RouterOS软件升级到最新版本，您可以确保最佳性能、稳定性和安全更新;
- 设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在安装在室内。 请将本产品远离水，火，潮湿或高温的环境。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 插座應安裝在設備附近，並應易於取用。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。
- 这是A类产品。在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施！

![](./img/image2020-2-5_14-43-45.badge-2.png)

 触电危险。 本设备只能由经过培训的人员进行维修

制造商：Mikrotikls SIA，拉脱维亚Ūnijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.9 или до последней версии, чтобы обеспечить соответствие требованиям местных органов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов. Все устройства MikroTik должны быть профессионально установлены.
Это краткое руководство охватывает модель: CCR2004-1G-12S+2XS.
:::

*Это сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, Полная декларация о соответствии требованиям ЕС, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-7.png)

**Первые шаги:**

- Подключите свой компьютер к порту Ethernet1/Boot;
- Подключите устройство к источнику питания;
- Настройте IP-адрес вашей сетевой карты на 192.168.88.2/24;
- Используйте WebFig в веб-браузере или инструмент настройки ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **доступно несколько методов настройки для обеспечения доступности;**
- Откройте http://192.168.88.1 в веб-браузере, чтобы начать установку. Если IP-адрес недоступен, используйте WinBox и выберите вкладку "Neighbors", чтобы найти устройство. Продолжите подключение, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте имена пользователей и пароли Wi-Fi на наклейке);
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- Установите пароль для вашего маршрутизатора.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Данное изделие предназначено для установки внутри помещения. Храните этот продукт вдали от воды, огня, влажности или жарких сред.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.
- Это продукт класса А. В домашних условиях этот продукт может вызывать радиопомехи, и в этом случае пользователю может потребоваться принять адекватные меры.

**Запрещается:**

- Эксплуатация роутера (точки доступа) и её комплектующих с повреждёнными шнурами электропитания;
- Подключение роутера (точки доступа) и её комплектующих к сети электропитания при открытых корпусах;
- Открыватькорпус изделия, разбирать, извлекать электронные модули и проводить какие-либо ремонтные работы вне условий ремонтной организации.

**Техническое обслуживание:**

- Роутер (точка доступа) не требует проведения профилактических работ и постоянного присутствия эксплуатационного персонала.
- Чистка корпуса от пыли и загрязнений выполняется бумажными безворсовыми салфетками.
- Не брызгайте водой в щели и контакты корпуса изделия.
- Плохо выводящиеся следы и пятна удаляйте изопропиловым спиртом.

**Текущий ремонт:**

- Все виды ремонта изделия допускается выполнять только аттестованным персоналом в сервисном центре предприятия-изготовителя или в другой уполномоченной изготовителем организации.
- Замена вышедших из строя технических средств (ТС) изделия должна осуществляться на соответствующие ТС, прошедшие специальные исследования и специальную проверку.

**Хранение:**

- Изделия, упакованные в ящик, следует хранить в складских помещениях при относительная влажность воздуха не более 85%, наличие в воздухе паров кислот, щелочей и прочих агрессивных примесей не допускается.

**Транспортирование:**

- Транспортируют изделия всеми видами транспорта в крытых транспортных средствах в соответствии с правилами перевозки грузов, действующих на данном виде транспорта.
- Транспортирование и хранение должны осуществляться в упаковке фирмы-изготовителя с соблюдением указаний по ориентации, защите, укладке и других, нанесенных на упаковку указаний обозначений.
- В помещениях и транспортных средствах не должно быть паров или аэрозолей агрессивных или вызывающих коррозию веществ.
- Упакованные изделия должны быть закреплены для предотвращения случайных неконтролируемых перемещений.
- Транспортирование, хранение и эксплуатация не допустимы в условиях конденсации влаги без защиты от атмосферных осадков и прямых солнечных лучей.

**Гарантийные обязательства:**

- Гарантийный срок эксплуатации − не более 14 суток со дня реализации потребителю.
- Гарантийный срок хранения изделий − 12 месяцев со дня изготовления.
- Некачественные изделия продавец обязан заменить в сроки, согласованные с потребителем.
- В случае спора о причинах возникновения недостатков товара продавец (изготовитель), уполномоченная организация или уполномоченный индивидуальный предприниматель, импортер обязаны провести экспертизу товара за свой счет.
- Срок устранения недостатков товара не может превышать сорок пять дней.
- Действие гарантийных обязательств прекращается:- при нарушении потребителем правил эксплуатации, транспортирования и хранения;- при обнаружении механических повреждений, следов вскрытия, попыток неквалифицированного ремонта;- при обнаружении признаков небрежного обращения, преднамеренного повреждения оборудования;- при попадании внутрь оборудования посторонних предметов, жидкостей и насекомых;- при обнаружении признаков воздействия непреодолимых сил, приведших к выходу из строя роутера (точки доступа).

**Утилизация:**

- Во избежание загрязнения окружающей среды необходимо отделить устройство от бытовых отходов и утилизировать его безопасным способом, например в специально отведенных местах. Ознакомьтесь с процедурами надлежащей транспортировки оборудования к специальным местам утилизации в вашем регионе.

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Опасность поражения электрическим током. Это оборудование должно обслуживаться только обученным персоналом.

Производитель: Mikrotikls SIA, Ūnijas 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. *Cм. на упаковке.*

![](./img/image2020-1-24_7-55-5.badge-8.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.9 або останньої версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил. Усі пристрої MikroTik повинні бути встановлені відповідно до інструкцій.
Цей короткий посібник стосується моделі: CCR2004-1G-12S+2XS.
:::

*Це мережевий пристрій. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help-ua](https://mt.lv/help-ua)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-50-1.badge.png)

**Перші кроки:**

- Підключіть свій комп'ютер до порту Ethernet1/Boot;
- Підключіть пристрій до джерела живлення;
- Налаштуйте IP-адресу вашої мережевої карти на 192.168.88.2/24;
- Використовуйте WebFig у веб-браузері або інструмент конфігурації ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **доступно декілька методів налаштування для забезпечення доступності;**
- Відкрийте веб-браузер і перейдіть за адресою http://192.168.88.1 для початку налаштувань. У випадку відсутності IP-адреси скористайтеся WinBox та оберіть вкладку "Neighbors", щоб знайти пристрій. Продовжте підключення за допомогою MAC-адреси. Ім'я користувача - "admin", і відсутній пароль (або, для деяких моделей, перевірте імена користувачів та паролі Wi-Fi на наклейці);
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- Встановіть пароль для вашого маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання повинно бути встановлено навченим і кваліфікованим персоналом згідно з цими інструкціями по установці. Установник несе відповідальність за те, щоб установка обладнання відповідала місцевим і національним електротехнічним нормам і правилам. Не намагайтеся розбирати, ремонтувати або модифікувати пристрій.
- Це обладнання призначене для встановлення в приміщенні. Тримайте це обладнання подалі від води, вогню, вологи, або гарячого середовища.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити — від’єднати адаптер електроживлення від розетки.

![](./img/ua.badge-4.jpg)

- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.
- Це продукт класу А. У побутових умовах цей виріб може викликати радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити відповідних заходів!

![](./img/image2020-2-5_14-43-45.badge-2.png)

 Небезпека ураження електричним струмом Це обладнання має обслуговуватися тільки навченим персоналом

Виробник: Mikrotikls SIA, Ūnijas 2, Рига, Латвія, LV1039.

## Federal Communication Commission Interference Statement

![](./img/fcc_logo_ez.badge-7.jpg)

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## UKCA marking

![](./img/ukca_black_fill.badge-7.gif)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

2 AC inputs (100 - 240 V AC)
IP20
±0°..+60°C

\#71608
