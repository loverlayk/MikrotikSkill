# Quick Guide G1-d

> Models: RB750r2 (hEX lite), RB750Gr3 (hEX), RB960PGS (hEX PoE), RB760iGS (hEX S), RB4011iGS+RM, RB3011UiAS-RM, RB450Gx4

**Models: RB750r2 (hEX lite), RB750Gr3 (hEX), RB960PGS (hEX PoE), RB760iGS (hEX S), RB4011iGS+RM, RB3011UiAS-RM, RB450Gx4**

![](./img/mt_logo_arrow_v2-02-54.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.12 or the latest version to ensure compliance with local authority regulations!
It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
:::

*This is a network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, Full EU Declaration of Conformity, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-61.png)

**First steps:**

- Make sure your ISP is accepting hardware changes and will automatically assign an IP address;
- Connect the ISP cable to the Ethernet1 port;
- Configure your network card settings to obtain the IP address automatically using DHCP;
- Connect the PC to any port except Ethernet1;
- Connect the device to a power source;
- Use WebFig in a web browser or the WinBox configuration tool [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Open http://192.168.88.1 in a web browser to start setup. If the IP address is unavailable, use *WinBox* and connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "*Check for updates*" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.
Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.12 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби. Всички устройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е мрежово устройство. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, пълна ЕС декларация за съответствие, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-59.png)

**Първи стъпки:**

- Уверете се, че вашият интернет доставчик приема хардуерни промени и автоматично ще назначи IP адрес;
- Свържете ISP кабела към Ethernet1 порта;
- Настройте настройките на мрежовата ви карта, за да получите IP адрес автоматично чрез DHCP;
- Свържете компютъра към всякакъв порт, освен Ethernet1;
- Свържете устройството към източник на захранване;
- Използвайте WebFig в уеб браузър или конфигурационния инструмент "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Отворете http://192.168.88.1 в уеб браузъра, за да започнете настройката. Ако IP адресът не е достъпен, използвайте *WinBox* и се свържете чрез MAC адреса. Потребителското име е "admin", а парола няма (или за някои модели проверете потребителските и безжични пароли на стикера);
- Кликнете на бутона "*Check for updates*" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- Задайте парола за вашия рутер.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за инсталиране на закрито. Дръжте този продукт далеч от вода, пожар, влажност или гореща среда.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е като извадите щепсела на захранването от контакта.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.
Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.12 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy. Všechna zařízení MikroTik musí být profesionálně nainstalován.
:::

*Toto je síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Technické specifikace, úplné EU prohlášení o shodě, brožury a další informace o produktech na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-59.png)

**První kroky:**

- Ujistěte se, že váš poskytovatel internetových služeb přijímá změny hardwaru a automaticky přiřadí IP adresu;
- Připojte kabel ISP k portu Ethernet1;
- Nakonfigurujte nastavení síťové karty tak, aby automaticky získala IP adresu pomocí DHCP;
- Připojte počítač k libovolnému portu kromě Ethernet1;
- Připojte zařízení ke zdroji napájení;
- Použijte WebFig v webovém prohlížeči nebo konfigurační nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Otevřete http://192.168.88.1 v webovém prohlížeči pro spuštění nastavení. Pokud není k dispozici IP adresa, použijte *WinBox* a připojte se pomocí MAC adresy. Uživatelské jméno je "admin", a heslo není (nebo pro některé modely zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Klepněte na tlačítko "*Check for updates*" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do menu "Files" ve WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- Nastavte heslo pro váš router.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro prevenci nehod. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k instalaci uvnitř. Udržujte tento produkt mimo vodu, oheň, vlhkost nebo horké prostředí.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecí zástrčky ze zásuvky.
- Abyste zabránili znečištění životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na určených místech. Seznamte se s postupy správné přepravy zařízení na určená sběrná místa ve vaší oblasti.
Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.12 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler. Alle MikroTik-enheder skal være professionelt installeret.
:::

*Dette er netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, fuld EU-overensstemmelseserklæring, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-59.png)

**Første trin:**

- Sørg for, at din internetudbyder accepterer hardwareændringer og tildeler automatisk en IP-adresse;
- Tilslut ISP-kablet til Ethernet1-porten;
- Konfigurer dine netværkskortindstillinger for at få IP-adressen automatisk ved hjælp af DHCP;
- Tilslut pc'en til en hvilken som helst port undtagen Ethernet1;
- Tilslut enheden til en strømkilde;
- Brug WebFig i en webbrowser eller konfigurationsværktøjet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Åbn http://192.168.88.1 i en webbrowser for at starte opsætningen. Hvis IP-adressen ikke er tilgængelig, skal du bruge *WinBox* og forbinde ved hjælp af MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- Klik på knappen "*Check for updates*" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload downloadede pakker til WebFig eller WinBox "Files" menu og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil din routeradgangskode.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive installeret indendørs. Hold dette produkt væk fra vand, ild, fugtighed eller varme omgivelser.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- For at undgå forurening af miljøet skal apparatet adskilles fra husholdningsaffald og bortskaffes på en sikker måde, f.eks. I bestemte områder. Bliv fortrolig med procedurer til korrekt transport af udstyr til udpegede indsamlingssteder i dit område.
Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.12 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen. Alle MikroTik-Geräte müssen professionell installiert werden.
:::

*Dies ist das Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Daten, vollständige EU-Konformitätserklärung, Broschüren und weitere Informationen zu Produkten unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-59.png)

**Erste Schritte:**

- Stellen Sie sicher, dass Ihr ISP Hardwareänderungen akzeptiert und automatisch eine IP-Adresse zuweist;
- Verbinden Sie das ISP-Kabel mit dem Ethernet1-Port;
- Konfigurieren Sie die Einstellungen Ihrer Netzwerkkarte, um die IP-Adresse automatisch über DHCP zu beziehen;
- Verbinden Sie den PC mit einem beliebigen Port außer Ethernet1;
- Schließen Sie das Gerät an eine Stromquelle an;
- Verwenden Sie WebFig in einem Webbrowser oder das Konfigurationstool "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Öffnen Sie http://192.168.88.1 in einem Webbrowser, um die Einrichtung zu starten. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie *WinBox* und stellen Sie eine Verbindung über die MAC-Adresse her. Der Benutzername ist "admin", und es gibt kein Passwort (oder für einige Modelle überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "*Check for updates*" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Legen Sie Ihr Router-Passwort fest.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für den Innenbereich vorgesehen. Halten Sie dieses Produkt von Wasser, Feuer, Feuchtigkeit oder heißen Umgebungen fern.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, den Netzstecker aus der Steckdose zu ziehen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Geräte zu bestimmten Sammelstellen in Ihrer Nähe vertraut.
Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.12 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών. Όλες οι συσκευές MikroTik πρέπει να εγκατασταθούν επαγγελματικά.
:::

*Αυτή είναι η συσκευή δικτύου*. *Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, πλήρης δήλωση συμμόρφωσης ΕΕ, φυλλάδια και περισσότερες πληροφορίες σχετικά με τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-59.png)

**Πρώτα βήματα:**

- Βεβαιωθείτε ότι ο ISP σας δέχεται αλλαγές υλικού και θα αντιστοιχίσει αυτόματα μια διεύθυνση IP;
- Συνδέστε το καλώδιο του παροχέα του ίντερνετ στη θύρα Ethernet1;
- Διαμορφώστε τις ρυθμίσεις της κάρτας δικτύου σας για να λάβετε τη διεύθυνση IP αυτόματα χρησιμοποιώντας το DHCP;
- Συνδέστε τον υπολογιστή σε οποιαδήποτε θύρα εκτός από την Ethernet1;
- Συνδέστε τη συσκευή σε πηγή ενέργειας;
- Χρησιμοποιήστε το WebFig σε ένα πρόγραμμα περιήγησης ή το εργαλείο ρύθμισης ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ανοίξτε το http://192.168.88.1 σε έναν περιηγητή για να ξεκινήσετε τη ρύθμιση. Εάν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το *WinBox* και συνδεθείτε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τα χρήστη και τα ασύρματα κωδικούς πρόσβασης στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "*Check for updates*" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα κατεβασμένα πακέτα στο μενού "Files" του WebFig ή του WinBox και επανεκκινήστε τη συσκευή;
- Με την αναβάθμιση του λογισμικού RouterOS στην τελευταία έκδοση, μπορείτε να διασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Ορίστε τον κωδικό πρόσβασης για τον router σας.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται για εγκατάσταση σε εσωτερικό χώρο. Κρατήστε το προϊόν μακριά από νερό, φωτιά, υγρασία ή καυτό περιβάλλον.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το φις από την πρίζα.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.
Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.12 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país. Todos los dispositivos de MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, Declaración de conformidad de la UE completa, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-60.png)

**Primeros pasos:**

- Asegúrese de que su ISP acepte cambios de hardware y le asignará automáticamente una dirección IP;
- Conecte el cable del proveedor de servicios de Internet al puerto Ethernet1;
- Configure la configuración de su tarjeta de red para obtener la dirección IP automáticamente mediante DHCP;
- Conecte la PC a cualquier puerto excepto Ethernet1;
- Conecte el dispositivo a una fuente de alimentación;
- Utilice WebFig en un navegador web o la herramienta de configuración "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Abra http://192.168.88.1 en un navegador web para iniciar la configuración. Si la dirección IP no está disponible, utilice *WinBox* y conéctese utilizando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifique los usuarios y contraseñas inalámbricas en la pegatina);
- Haga clic en el botón "*Check for updates*" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Sube los paquetes descargados al menú "Files" de WebFig o WinBox y reinicia el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- Configure la contraseña de su enrutador.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para instalarse en interiores. Mantenga este producto alejado del agua, fuego, humedad o ambientes calientes.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- El tomacorriente se instalará cerca del equipo y será de fácil acceso.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el enchufe de la toma de corriente.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en las áreas designadas. Familiarícese con los procedimientos para transportar correctamente el equipo a los puntos de recolección designados en su área.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.12 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi. Kõik MikroTiku seadmed peavad olema professionaalselt paigaldatud.
:::

*See on võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised andmed, täielik EL-i vastavusdeklaratsioon, brošüürid ja lisateave toodete kohta aadressil [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-59.png)

**Esimesed sammud:**

- Veenduge, et teie Interneti-teenuse pakkuja aktsepteerib riistvara muudatusi, ja määrake automaatselt IP-aadress;
- Ühendage ISP-kaabel Ethernet1 pordiga;
- Konfigureerige oma võrgukaardi seaded, et saada IP-aadress automaatselt kasutades DHCP-d;
- Ühendage arvuti mõne muu pordiga kui Ethernet1;
- Ühendage seade toiteallikaga;
- Kasutage WebFigi veebi­brauseris või seadistus­tööriista "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Avage http://192.168.88.1 veebibrauseris, et alustada seadistamist. Kui IP-aadress pole saadaval, kasutage *WinBoxi* ja ühendage MAC-aadressi kasutades. Kasutajanimi on "admin", ja parooli pole (või mõne mudeli puhul kontrollige kasutaja ja traadita paroole kleepsul);
- Klõpsake nupul "*Check for updates*" ja ajakohastage RouterOS viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Lae allalaaditud paketid üles veebibrauseri WebFig või WinBox "Files" menüüsse ja taaskäivita seade;
- Värskendades oma RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadke oma ruuteri parool.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud paigaldamiseks siseruumidesse. Hoidke seda toodet eemal veest, tulest, niiskusest ja kuumadest keskkondadest.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on pistiku pistikupesast lahti ühendamine.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja utiliseerige see ohutult, näiteks selleks ettenähtud kohtades. Tutvuge seadmete nõuetekohase transportimise protseduuridega teie piirkonnas asuvatesse kogumispunktidesse.
Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.12 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja. Kaikkien MikroTik-laitteiden on oltava ammattimaisesti asennettu.
:::

*Tämä on verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, täydellinen EU-vaatimustenmukaisuusvakuutus, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-59.png)

**Ensiaskeleet:**

- Varmista, että Internet-palveluntarjoajasi hyväksyy laitemuutokset, ja määrittää IP-osoitteen automaattisesti;
- Liitä ISP-kaapeli Ethernet1-porttiin;
- Aseta verkkokorttisi asetukset saadaksesi IP-osoitteen automaattisesti DHCP: n avulla;
- Liitä tietokone mihin tahansa porttiin paitsi Ethernet1;
- Kytke laite virtalähteeseen;
- Käytä WebFi­giä web-selaimessa tai konfigurointityökalua "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Avaa http://192.168.88.1 verkkoselaimessa aloittaaksesi asennuksen. Jos IP-osoite ei ole käytettävissä, käytä *WinBoxia* ja yhdistä MAC-osoitetta käyttäen. Käyttäjätunnus on "admin", eikä salasanaa ole (tai joillakin malleilla tarkista käyttäjä- ja langattomat salasanat tarrasta);
- Napsauta "*Check for updates*" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFigin tai WinBoxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- Aseta reitittimen salasana.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi sisätiloissa. Pidä tämä tuote poissa vedestä, tulesta, kosteudesta tai kuumasta ympäristöstä.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtajohto pistorasiasta.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla esimerkiksi määrätyillä alueilla. Tutustu toimenpiteisiin, joilla laite kuljetetaan asianmukaisesti alueellesi määritettyihin keräyspisteisiin.
- **Koskee RB750r2:ta (hEX lite).** Tämä on A-luokan tuote. Kotiympäristössä tämä tuote saattaa aiheuttaa radiohäiriöitä, jolloin käyttäjän on ehkä ryhdyttävä asianmukaisiin toimenpiteisiin.
Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.12 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays. Tous les appareils MikroTik doivent être installé professionnellement.
:::

*Ceci est un périphérique réseau. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, déclaration de conformité UE complète, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-59.png)

**Premiers pas:**

- Assurez-vous que votre FAI accepte les modifications matérielles et attribuera automatiquement une adresse IP;
- Connectez le câble du fournisseur d'accès Internet au port Ethernet1;
- Configurez les paramètres de votre carte réseau pour obtenir automatiquement l'adresse IP via DHCP;
- Connectez votre PC à n'importe quel port sauf Ethernet1;
- Connectez l'appareil à une source d'alimentation;
- Utilisez WebFig dans un navigateur web ou l’outil de configuration "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Ouvrez http://192.168.88.1 dans un navigateur web pour commencer la configuration. Si l'adresse IP n'est pas disponible, utilisez *WinBox* et connectez-vous en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "*Check for updates*" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, la stabilité et les mises à jour de sécurité;
- Configurez le mot de passe de votre routeur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être installé à l'intérieur. Gardez ce produit loin de l'eau, du feu, de l'humidité ou des environnements chauds.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher la fiche d'alimentation de la prise de courant.
- Pour éviter la contamination de l'environnement, séparez l'appareil des déchets ménagers et éliminez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.
Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HI - हिंदी. त्वरित मार्गदर्शिका

:::warning
स्थानीय प्राधिकारी नियमों का अनुपालन सुनिश्चित करने के लिए इस डिवाइस को राउटरओएस v7.12 या नवीनतम संस्करण में अपग्रेड करने की आवश्यकता है!
स्थानीय देश के नियमों का पालन करना अंतिम उपयोगकर्ताओं की जिम्मेदारी है। सभी MikroTik डिवाइस पेशेवर रूप से स्थापित होने चाहिए
:::

*यह नेटवर्क डिवाइस है. आप उत्पाद मॉडल का नाम केस लेबल (आईडी) पर पा सकते हैं।*
*पूर्ण अद्यतन उपयोगकर्ता मैनुअल के लिए कृपया [https://mt.lv/um](https://mt.lv/um) पर उपयोगकर्ता मैनुअल पृष्ठ पर जाएँ। या अपने मोबाइल फ़ोन से QR कोड को स्कैन करें.*
*इस उत्पाद के लिए सबसे महत्वपूर्ण तकनीकी विशिष्टताएँ इस त्वरित मार्गदर्शिका के अंतिम पृष्ठ पर पाई जा सकती हैं।*
*तकनीकी विशिष्टताएँ, अनुरूपता की पूर्ण ईयू घोषणा, ब्रोशर, और उत्पादों के बारे में अधिक जानकारी [https://mikrotik.com/products](https://mikrotik.com/products) पर*
*अतिरिक्त जानकारी के साथ आपकी भाषा में सॉफ़्टवेयर के लिए कॉन्फ़िगरेशन मैनुअल [https://mt.lv/help](https://mt.lv/help) पर पाया जा सकता है*
*मिक्रोटिक उपकरण व्यावसायिक उपयोग के लिए हैं। यदि आपके पास योग्यता नहीं है तो कृपया एक सलाहकार https://mikrotik.com/consultants खोजें*

![](./img/hi-um.badge-2.png)

**पहले कदम:**

- सुनिश्चित करें कि आपका आईएसपी हार्डवेयर परिवर्तन स्वीकार कर रहा है और स्वचालित रूप से एक आईपी पता निर्दिष्ट करेगा;
- ISP केबल को ईथरनेट1 पोर्ट से कनेक्ट करें;
- डीएचसीपी का उपयोग करके स्वचालित रूप से आईपी पता प्राप्त करने के लिए अपनी नेटवर्क कार्ड सेटिंग्स कॉन्फ़िगर करें;
- ईथरनेट1 को छोड़कर पीसी को किसी भी पोर्ट से कनेक्ट करें;
- डिवाइस को पावर स्रोत से कनेक्ट करें;
- वेब ब्राउज़र में WebFig या "WinBox" कॉन्फ़िगरेशन टूल [https://mt.lv/winbox](https://mt.lv/winbox) का उपयोग करें; **कई कॉन्फ़िगरेशन विधियाँ उपलब्ध हैं ताकि पहुँच में आसानी हो सके;**
- सेटअप शुरू करने के लिए वेब ब्राउज़र में http://192.168.88.1 खोलें। यदि आईपी पता अनुपलब्ध है, तो विनबॉक्स का उपयोग करें और मैक पते का उपयोग करके कनेक्ट करें। उपयोगकर्ता नाम "admin", है और कोई पासवर्ड नहीं है (या, कुछ मॉडलों के लिए, स्टिकर पर उपयोगकर्ता और वायरलेस पासवर्ड की जांच करें);
- "*Check for updates*" बटन पर क्लिक करें और राउटरओएस को नवीनतम संस्करण में अपडेट करें;
- डिवाइस को मैन्युअल रूप से अपडेट करने के लिए mikrotik.com पर जाएँ, अपना मॉडल चुनें और आवश्यक पैकेजों को "Downloads" सेक्शन में ढूँढें;
- डाउनलोड किए गए पैकेज को WebFig या WinBox के "Files" मेनू में अपलोड करें और डिवाइस को रिबूट करें;
- अपने राउटरओएस सॉफ़्टवेयर को नवीनतम संस्करण में अपग्रेड करके, आप इष्टतम प्रदर्शन, स्थिरता और सुरक्षा अपडेट सुनिश्चित कर सकते हैं;
- अपना राउटर पासवर्ड सेट करें.

**सुरक्षा संबंधी जानकारी:**

- किसी भी मिक्रोटिक उपकरण पर काम करने से पहले, विद्युत सर्किटरी से जुड़े खतरों से अवगत रहें, और दुर्घटनाओं को रोकने के लिए मानक प्रथाओं से परिचित हों। इंस्टॉलर को नेटवर्क संरचनाओं, नियमों और अवधारणाओं से परिचित होना चाहिए।
- केवल निर्माता द्वारा अनुमोदित बिजली आपूर्ति और सहायक उपकरण का उपयोग करें, जो इस उत्पाद की मूल पैकेजिंग में पाया जा सकता है।
- इन स्थापना निर्देशों के अनुसार, यह उपकरण प्रशिक्षित और योग्य कर्मियों द्वारा स्थापित किया जाना है। इंस्टॉलर यह सुनिश्चित करने के लिए ज़िम्मेदार है कि उपकरण की स्थापना स्थानीय और राष्ट्रीय विद्युत कोड के अनुरूप है। डिवाइस को अलग करने, मरम्मत करने या संशोधित करने का प्रयास न करें।
- यह उत्पाद घर के अंदर स्थापित करने के लिए है। इस उत्पाद को पानी, आग, नमी या गर्म वातावरण से दूर रखें।
- हम इसकी गारंटी नहीं दे सकते कि डिवाइस के अनुचित उपयोग के कारण कोई दुर्घटना या क्षति नहीं होगी। कृपया इस उत्पाद का उपयोग सावधानी से करें और अपने जोखिम पर संचालित करें!
- सॉकेट-आउटलेट उपकरण के पास स्थापित किया जाएगा और आसानी से पहुंच योग्य होगा।
- डिवाइस विफलता की स्थिति में, कृपया इसे बिजली से डिस्कनेक्ट कर दें। ऐसा करने का सबसे तेज़ तरीका पावर आउटलेट से पावर प्लग को अनप्लग करना है।
- पर्यावरण को प्रदूषित होने से बचाने के लिए, उपकरण को घरेलू कचरे से अलग करें और इसका सुरक्षित तरीके से निपटान करें, उदाहरण के लिए, निर्दिष्ट क्षेत्रों में। अपने क्षेत्र में निर्दिष्ट संग्रह बिंदुओं तक उपकरण को उचित तरीके से ले जाने की प्रक्रियाओं से परिचित हों।
- RB750r2 (hEX लाइट) के लिए लागू। यह वर्ग ए उत्पाद है। घरेलू परिवेश में, यह उत्पाद रेडियो हस्तक्षेप का कारण बन सकता है, ऐसी स्थिति में उपयोगकर्ता को पर्याप्त उपाय करने की आवश्यकता हो सकती है।
निर्माता: मिक्रोटिकल्स एसआईए, यूनिजस 2, रीगा, लातविया, एलवी1039।

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.12 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise. Svi MikroTik uređaji moraju biti profesionalno instaliran.
:::

*Ovo je mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, puna EU izjava o sukladnosti, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-59.png)

**Prvi koraci:**

- Provjerite prihvaća li vaš ISP promjene hardvera i automatski će dodijeliti IP adresu;
- Povežite kabel davatelja internetskih usluga na priključak Ethernet1;
- Postavite postavke mrežne kartice da biste automatski dobili IP adresu pomoću DHCP-a;
- Povežite računalo s bilo kojim priključkom osim Ethernet1;
- Priključite uređaj na izvor napajanja;
- Koristite WebFig u web-pregledniku ili konfiguracijski alat "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Otvorite http://192.168.88.1 u web pregledniku kako biste započeli postavljanje. Ako IP adresa nije dostupna, koristite *WinBox* i povežite se putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Kliknite na gumb "*Check for updates*" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Prenesite preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem softvera RouterOS na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- Postavite lozinku za vaš usmjerivač.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen ugradnji u zatvorenom prostoru. Ovaj proizvod držite podalje od vode, vatre, vlage ili vrućeg okruženja.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanje utikača iz utičnice.
- Da biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na za to predviđena mjesta. Upoznajte se s postupcima pravilnog transporta opreme do određenih sabirnih mjesta u vašem području.
Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.12-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása. Az összes MikroTik készüléknek lennie kell szakszerűen telepítve.
:::

*Ez hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki adatok, teljes EU-megfelelőségi nyilatkozat, prospektusok és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products) oldalon*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-59.png)

**Első lépések:**

- Győződjön meg arról, hogy az internetszolgáltató elfogadja a hardverváltozásokat, és automatikusan hozzárendel egy IP-címet;
- Csatlakoztassa az ISP kábelt az Ethernet1 portra;
- Állítsa be hálózati kártyájának beállításait, hogy automatikusan szerezze meg az IP-címet a DHCP segítségével;
- Csatlakoztassa a számítógépet bármely portra, kivéve az Ethernet1-et;
- Csatlakoztassa a készüléket az áramforráshoz;
- Használja a WebFig-et webböngészőben vagy a "WinBox” konfigurációs eszközt [https://mt.lv/winbox](https://mt.lv/winbox); **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Nyissa meg a http://192.168.88.1 címet egy webböngészőben a beállítások elindításához. Ha az IP-cím nem elérhető, használja a *WinBoxot*, és csatlakozzon a MAC-cím használatával. A felhasználónév "admin", és nincs jelszó (vagy néhány modell esetében ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson az "*Check for updates*" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- Az RouterOS szoftver frissítésével a legújabb verzióra biztosíthatja az optimális teljesítményt, stabilitást és biztonsági frissítéseket;
- Állítsa be a router jelszavát.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket beltéri használatra tervezték. Tartsa távol a terméket víztől, tűztől, páratartalomtól és forró környezettől.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati csatlakozót kihúzza a konnektorból.
- A környezet szennyeződésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon dobja el, például a kijelölt területekre. Ismerje meg a berendezés megfelelő szállítási eljárásait a környéken található gyűjtőhelyekre.
Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan cepat

:::warning
Perangkat ini harus diperbarui ke RouterOS v7.12 atau versi terbaru untuk mematuhi peraturan otoritas setempat.
Pengguna akhir bertanggung jawab untuk mengikuti peraturan lokal setempat. Semua perangkat MikroTik harus dipasang secara profesional.
:::

*Ini adalah perangkat jaringan. Anda dapat menemukan nama model produk pada label casing (ID).*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um-id](https://mt.lv/um-id) untuk panduan pengguna yang diperbarui sepenuhnya. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Memulai Cepat ini.*
*Spesifikasi teknis, pernyataan kesesuaian UE lengkap, brosur, dan informasi produk lebih lanjut di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Panduan konfigurasi software dalam bahasa Anda dengan informasi tambahan tersedia di [https://mt.lv/help-id](https://mt.lv/help-id)*
*Perangkat MikroTik untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi, konsultasikan dengan konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-61.png)

**Langkah pertama:**

- Pastikan ISP Anda menerima perubahan perangkat keras dan secara otomatis akan menetapkan alamat IP;
- Hubungkan kabel ISP ke port Ethernet1;
- Atur pengaturan kartu jaringan Anda untuk mendapatkan alamat IP secara otomatis menggunakan DHCP;
- Hubungkan PC ke salah satu port kecuali Ethernet1;
- Hubungkan perangkat ke sumber listrik;
- Gunakan WebFig di peramban web atau alat konfigurasi WinBox [https://mt.lv/winbox](https://mt.lv/winbox); **tersedia beberapa metode konfigurasi untuk memastikan aksesibilitas;**
- Buka http://192.168.88.1 di peramban web untuk memulai pengaturan. Jika alamat IP tidak tersedia, gunakan WinBox dan hubungkan menggunakan alamat MAC. Nama pengguna adalah "admin", dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu "Files" WebFig atau WinBox dan mulai ulang perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja optimal, stabilitas, dan pembaruan keamanan;
- Atur kata sandi router Anda.

**Informasi keselamatan:**

- Sebelum mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik dan pahami praktik standar untuk pencegahan kecelakaan. Pemasang harus terbiasa dengan struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen dan terdapat dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan memenuhi syarat, sesuai dengan petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini ditujukan untuk pemasangan di dalam ruangan. Jauhkan produk ini dari air, api, kelembapan, atau lingkungan yang panas.
- Kami tidak dapat menjamin bahwa tidak ada kecelakaan atau kerusakan yang akan terjadi karena penggunaan perangkat yang tidak tepat. Gunakan produk ini dengan hati-hati dan operasikan dengan risiko Anda sendiri!
- Stopkontak harus dipasang di dekat peralatan dan harus mudah dijangkau.
- Jika terjadi kegagalan perangkat, lepaskan dari catu daya. Cara tercepat untuk melakukannya adalah dengan mencabut steker listrik dari stopkontak.
- Untuk menghindari kontaminasi lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan aman, misalnya di area yang ditentukan. Biasakan diri Anda dengan prosedur untuk mengangkut peralatan Anda dengan benar ke titik pengumpulan yang ditentukan di area Anda.
Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.12 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali. Tutti i dispositivi MikroTik devono essere installato professionalmente.
:::

*Questo è il dispositivo di rete. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-id](https://mt.lv/um-id) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, dichiarazione di conformità UE completa, brochure e ulteriori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-id](https://mt.lv/help-id)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-59.png)

**Primi passi:**

- Assicurati che il tuo ISP accetti le modifiche hardware e assegni automaticamente un indirizzo IP;
- Collegare il cavo del provider Internet alla porta Ethernet1;
- Configura le impostazioni della tua scheda di rete per ottenere automaticamente l'indirizzo IP tramite DHCP;
- Collega il PC a qualsiasi porta tranne Ethernet1;
- Collegare il dispositivo a una fonte di alimentazione;
- Utilizzare WebFig in un browser web oppure lo strumento di configurazione "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Apri http://192.168.88.1 in un browser web per avviare la configurazione. Se l'indirizzo IP non è disponibile, utilizza *WinBox* e connettiti utilizzando l'indirizzo MAC. Il nome utente è "admin", e non c'è alcuna password (o, per alcuni modelli, controlla gli utenti e le password wireless sull'adesivo);
- Fai clic sul pulsante "*Check for updates*" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Imposta la password del tuo router.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è destinato all'installazione all'interno. Tenere questo prodotto lontano da acqua, fuoco, umidità o ambienti caldi.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare la spina di alimentazione dalla presa di corrente.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio, in aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura ai punti di raccolta designati nella propria zona.
Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.12 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum. Öll MikroTik tæki verða að vera fagmannlega sett upp.
:::

*Þetta er net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tækniforskriftir, full ESB-samræmisyfirlýsing, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-59.png)

**Fyrstu skrefin:**

- Gakktu úr skugga um að ISP þinn samþykki vélbúnaðarbreytingar og úthluti sjálfkrafa IP tölu;
- Tengdu ISP-kafla við Ethernet1-höfnina;
- Stilla stillingar netkortsins til að fá IP-tölu sjálfkrafa með DHCP;
- Tengdu tölvuna við einhvern af öllum inntökum nema Ethernet1;
- Tengdu tækið við aflgjafa;
- Notið WebFig í vefvafra eða uppsetningartól "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Opnið http://192.168.88.1 í vafra til að byrja uppsetningu. Ef IP-talan er ekki tiltæki, notið *WinBox* og tengist með MAC-tölvu. Notendanafnið er „*admin*“, og lykilorð er ekki til (eða, fyrir sumar gerðir, athugaðu notendur og þráðlaus lykilorð á merki);
- Smelltu á "*Check for updates*" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum á WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Með því að uppfæra hugbúnaðinn á RouterOS í nýjustu útgáfu getur þú tryggjað bestu mögulegu afköst, stöðugleika og öryggisuppfærslur;
- Stilla lykilorðið á routerinn þína.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að setja upp innandyra. Geymið þessa vöru fjarri vatni, eldi, raka eða heitu umhverfi.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Til að koma í veg fyrir mengun umhverfisins skaltu aðskilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur til að flytja búnaðinn rétt til tilnefndra söfnunarstaða á þínu svæði.
Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.12 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter. Alle MikroTik-enheter må være profesjonelt installert.
:::

*Dette er nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, full EU-samsvarserklæring, brosjyrer og mer informasjon om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-59.png)

**Første steg:**

- Forsikre deg om at Internett-leverandøren godtar maskinvareendringer og tilordner automatisk en IP-adresse;
- Koble ISP-kabelen til Ethernet1-porten;
- Konfigurer nettverkskortinnstillingene dine for å få IP-adressen automatisk ved hjelp av DHCP;
- Koble PC-en til en hvilken som helst port unntatt Ethernet1;
- Koble enheten til en strømkilde;
- Bruk WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Åpne http://192.168.88.1 i en nettleser for å starte oppsettet. Hvis IP-adressen ikke er tilgjengelig, bruk *WinBox* og koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på knappen "*Check for updates*" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig eller WinBox "Files"-menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- Konfigurer router-passordet ditt.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å installeres innendørs. Hold dette produktet borte fra vann, brann, fuktighet eller varme omgivelser.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke støpselet ut av stikkontakten.
- For å unngå forurensning av miljøet, må du skille enheten fra husholdningsavfall og kaste den på en sikker måte, for eksempel i bestemte områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.
Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.12“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi. Visi „MikroTik“ prietaisai turi būti profesionaliai sumontuota.
:::

*Tai yra tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, visa ES atitikties deklaracija, brošiūros ir daugiau informacijos apie gaminius adresu [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-59.png)

**Pirmieji žingsniai:**

- Įsitikinkite, ar jūsų interneto paslaugų teikėjas priima aparatūros pakeitimus ir automatiškai priskiria IP adresą;
- Prijunkite ISP kabelį prie Ethernet1 lizdo;
- Nustatykite tinklo plokštės nustatymus automatiškai gauti IP adresą naudojant DHCP;
- Prijunkite kompiuterį prie bet kurios jungties, išskyrus Ethernet1;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Naudokite WebFig naršyklėje arba konfigūravimo įrankį "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atidarykite http://192.168.88.1 naršyklėje, kad pradėtumėte nustatymus. Jei IP adresas nepasiekiamas, naudokite *WinBox* ir prisijunkite naudodami MAC adresą. Prisijungimo vardas yra "admin", ir nėra slaptažodžio (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite įrenginį iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Nustatykite savo maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas yra skirtas montuoti patalpose. Laikykite gaminį atokiau nuo vandens, ugnies, drėgmės ir karštos aplinkos.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo kištuką nuo maitinimo lizdo.
- Kad išvengtumėte aplinkos užteršimo, atskirkite prietaisą nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.
Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.12 vai jaunāku versiju, lai nodrošinātu atbilstību vietējās likumdošanas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus. Visām MikroTik ierīcēm jābūt profesionāli uzstādītām.
:::

*Šī ir tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, pilna ES atbilstības deklarācija, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-59.png)

**Pirmie soļi:**

- Pārliecinieties, vai jūsu interneta pakalpojumu sniedzējs atļauj aparatūras nomaiņu un automātiski piešķir IP adresi;
- Pieslēdziet ISP kabeli pie Ethernet1 porta;
- Konfigurējiet savas tīkla kartes iestatījumus, lai automātiski iegūtu IP adresi, izmantojot DHCP;
- Pieslēdziet datoru pie jebkuras porta, izņemot Ethernet1;
- Pievienojiet ierīci strāvas avotam;
- Izmantojiet WebFig tīmekļa pārlūkā vai konfigurācijas rīku "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Atveriet http://192.168.88.1 pārlūkprogrammā, lai sāktu iestatīšanu. Ja IP adrese nav pieejama, izmantojiet *WinBox* un izveidojiet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav paroles (vai, dažiem modeļiem, pārbaudiet lietotāju un bezvadu paroles uz līmējuma);
- Noklikšķiniet uz pogas "*Check for updates*" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox "Files" izvēlni un pārstartējiet ierīci;
- Jauninot RouterOS programmatūru uz jaunāko versiju, jūs varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Iestatiet sava maršrutētāja paroli.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas kabeli un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Instalētāja pienākums ir pārliecināties, ka iekārtas uzstādīšana atbilst vietējiem un nacionālajiem elektriskajiem noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai telpās. Sargājiet šo izstrādājumu no ūdens, uguns, mitruma vai karstas vides.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas spraudni no kontaktligzdas.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.
Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.12 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż. L-apparati kollha MikroTik iridu jkunu installati professjonalment.
:::

*Dan huwa apparat tan-netwerk. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, Dikjarazzjoni Sħiħa ta' Konformità tal-UE, fuljetti, u aktar informazzjoni dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-59.png)

**L-ewwel passi:**

- Kun żgur li l-ISP tiegħek qed jaċċetta tibdil tal-hardware u awtomatikament jassenja indirizz IP;
- Ikkonnettja l-kavju tal-ISP għall-port Ethernet1;
- Ikkonfigurat il-settings tal-karta tan-netwerk tiegħek biex tagħti l-indirizz IP awtomatikament permezz ta 'DHCP;
- Ikkonnettja l-PC għal xi porta, għal xi porta minbarra Ethernet1;
- Qabbad l-apparat ma 'sors ta' enerġija;
- Uża WebFig f’web browser jew l-għodda ta’ konfigurazzjoni “WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Għaġġar http://192.168.88.1 f'browser web biex tibda l-iżvilupp. Jekk l-indirizz IP mhux disponibbli, uża l-*WinBox* u konnettiti billi tuża l-indirizz MAC. L-username huwa "admin", u m'hemmx password (jew, għal xi mudelli, iċċekkja l-passwords tal-utenti u tal-wireless fuq it-tickietta);
- Ikklikkja fuq il-buttuna "*Check for updates*" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Uploadja tal-pakketti miżjuda fil-menu "Files" ta' WebFig jew WinBox u rerew boot l-apparat;
- Billi taġġorna l-softwer tal-RouterOS għall-aħħar verżjoni, tista 'tissikura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Iffurmat il-password tar-router tiegħek.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skond dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jiġi installat fuq ġewwa. Żomm dan il-prodott 'il bogħod minn ilma, nar, umdità jew ambjenti sħan.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ il-plagg tal-qawwa mill-iżbokk tad-dawl.
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.
Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.12 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften. Alle MikroTik-apparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, volledige EU-conformiteitsverklaring, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-59.png)

**Eerste stappen:**

- Zorg ervoor dat uw ISP hardwarewijzigingen accepteert en automatisch een IP-adres toewijst;
- Sluit de ISP-kabel aan op poort Ethernet1;
- Stel de instellingen van uw netwerkkaart in om het IP-adres automatisch te verkrijgen via DHCP;
- Sluit de pc aan op een willekeurige poort behalve Ethernet1;
- Sluit het apparaat aan op een stroombron;
- Gebruik WebFig in een webbrowser of de configuratietool "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Open http://192.168.88.1 in een webbrowser om de installatie te starten. Als het IP-adres niet beschikbaar is, gebruik *WinBox* en maak verbinding met het MAC-adres. De gebruikersnaam is "admin", en er is geen wachtwoord (of, voor sommige modellen, controleer gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "*Check for updates*" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Stel uw routerwachtwoord in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die door de fabrikant zijn goedgekeurd en die zich in de originele verpakking van dit product bevinden.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om binnenshuis te worden geïnstalleerd. Houd dit product uit de buurt van water, vuur, vochtigheid of hete omgevingen.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Het stopcontact moet in de buurt van de apparatuur worden geïnstalleerd en moet gemakkelijk toegankelijk zijn.
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stekker uit het stopcontact te halen.
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.
Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.12 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych. Wszystkie urządzenia MikroTik muszą być profesjonalnie zainstalowany.
:::

*To jest urządzenie sieciowe. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Specyfikacje techniczne, pełna deklaracja zgodności UE, broszury i więcej informacji o produktach na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-59.png)

**Pierwsze kroki:**

- Upewnij się, że twój dostawca usług internetowych akceptuje zmiany sprzętu i automatycznie przypisze adres IP;
- Podłącz kabel ISP do portu Ethernet1;
- Skonfiguruj ustawienia karty sieciowej, aby automatycznie uzyskać adres IP za pomocą DHCP;
- Podłącz komputer do dowolnego portu z wyjątkiem Ethernet1;
- Podłącz urządzenie do źródła zasilania;
- Użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Otwórz http://192.168.88.1 w przeglądarce internetowej, aby rozpocząć konfigurację. Jeśli adres IP nie jest dostępny, użyj *WinBox* i połącz się za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła nie ma (lub, dla niektórych modeli, sprawdź hasła użytkowników i bezprzewodowe na naklejce);
- Kliknij przycisk "*Check for updates*" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Prześlij pobrane paczki do menu "Files" WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- Ustaw hasło dla swojego routera.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt jest przeznaczony do instalacji w pomieszczeniach. Trzymaj ten produkt z dala od wody, ognia, wilgoci lub gorących środowisk.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- Gniazdko powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem na to jest wyciągnięcie wtyczki z gniazdka.
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.
Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.12 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país. Todos os dispositivos de MikroTik devem ser instalado profissionalmente.
:::

*Este é o dispositivo de rede. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, Declaração de conformidade completa da UE, folhetos e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-59.png)

**Primeiros passos:**

- Verifique se o seu ISP está aceitando alterações de hardware e atribui automaticamente um endereço IP;
- Conecte o cabo do provedor de serviços de Internet à porta Ethernet1;
- Configure as configurações do seu cartão de rede para obter o endereço IP automaticamente usando o DHCP;
- Conecte o PC a qualquer porta, exceto Ethernet1;
- Conecte o dispositivo a uma fonte de energia;
- Use o WebFig num navegador ou a ferramenta de configuração "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Abra http://192.168.88.1 em um navegador da Web para iniciar a configuração. Se o endereço IP não estiver disponível, use o *WinBox* e conecte-se usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique as senhas de usuário e sem fio no adesivo);
- Clique no botão "*Check for updates*" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Faça o upload dos pacotes baixados para o menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar o software do RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- Configure a senha do seu roteador.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser instalado em ambiente interno. Mantenha este produto longe de água, fogo, umidade ou ambientes quentes.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- A tomada deve ser instalada próxima ao equipamento e deve ser de fácil acesso.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o plugue da tomada.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.12 sau la cea mai recentă versiune pentru a respecta reglementările autorităților locale!
Respectarea legislației locale este responsabilitatea utilizatorilor finali. Toate dispozitivele MikroTik trebuie să fie instalate profesional.
:::

*Acesta este un dispozitiv de rețea. Puteți găsi numele modelului imprimat pe eticheta carcasei (ID).*
*Consultați manualul complet actualizat la adresa: [https://mt.lv/um-ro](https://mt.lv/um-ro) sau scanați codul QR cu telefonul mobil.*
*Cele mai importante specificații tehnice ale acestui produs se află pe ultima pagină a acestui Ghid rapid.*
*Pentru specificații tehnice complete, Declarația de conformitate UE, broșuri și alte informații despre produse, vizitați: [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare în limba dumneavoastră, cu informații suplimentare, se găsește la: [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate uzului profesional. Dacă nu aveți calificările necesare, vă recomandăm să apelați la un consultant autorizat: [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/ro.badge.png)

**Primii pasi:**

- Asigurați-vă că ISP-ul dvs. acceptă modificări hardware și atribuie automat o adresă IP;
- Conectați cablul ISP la portul Ethernet1;
- Configurați placa de rețea pentru a obține automat adresa IP folosind DHCP;
- Conectați PC-ul la orice port, cu excepția Ethernet1;
- Conectați dispozitivul la o sursă de alimentare;
- Utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Accesați http://192.168.88.1 într-un browser web pentru a începe configurarea. Dacă adresa IP nu este disponibilă, utilizați *WinBox* și conectați-vă folosind adresa MAC. Numele de utilizator este "admin", iar parola este goală (sau, pentru unele modele, verificați pe autocolant parola de utilizator și parola rețelei wireless);
- Faceți clic pe butonul "*Check for updates*" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Actualizarea software-ului RouterOS la cea mai recentă versiune asigură performanță, stabilitate și actualizări de securitate optime;
- Setați o parolă pentru router.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător, care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament trebuie instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că instalarea echipamentului respectă codurile electrice locale și naționale.
- Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat instalării în interior. Păstrați-l departe de apă, foc, umiditate sau medii calde.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să îl operați pe propriul risc!
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin deconectarea mufei de la priză.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-l într-un mod sigur, de exemplu în zonele desemnate.
- Familiarizați-vă cu procedurile de transport corespunzător al echipamentelor către punctele de colectare desemnate din zona dumneavoastră.
Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.12 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny. Všetky zariadenia MikroTik musia byť profesionálne nainštalovaný.
:::

*Toto je sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete nastránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Technické špecifikácie, úplné EÚ vyhlásenie o zhode, brožúry a ďalšie informácie o produktoch na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-59.png)

**Prvé kroky:**

- Uistite sa, že poskytovateľ internetových služieb prijíma zmeny hardvéru a automaticky priradí adresu IP;
- Pripojte kábel od poskytovateľa internetu do portu Ethernet1;
- Konfigurujte nastavenia siete karty tak, aby ste automaticky získali IP adresu pomocou DHCP;
- Pripojte počítač na akýkoľvek port okrem Ethernet1;
- Pripojte zariadenie k zdroju napájania;
- Použite WebFig v webovom prehliadači alebo konfiguračný nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Otvorte http://192.168.88.1 vo webovom prehliadači na spustenie nastavenia. Ak nie je k dispozícii IP adresa, použite *WinBox* a pripojte sa pomocou MAC adresy. Používateľské meno je "admin", a heslo nie je (alebo, pre niektoré modely, skontrolujte užívateľské a bezdrôtové heslá na štítku);
- Kliknite na tlačidlo "*Check for updates*" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" vo WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- Nastavte heslo pre váš router.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je určený na inštaláciu vo vnútri. Chráňte tento výrobok pred vodou, ohňom, vlhkosťou alebo horúcim prostredím.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťovej zástrčky zo zásuvky.
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.
Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.12 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom. Vse naprave MikroTik morajo biti strokovno nameščen.
:::

*To je omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Tehnične specifikacije, popolna izjava o skladnosti EU, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-59.png)

**Prvi koraki:**

- Prepričajte se, da vaš ponudnik internetnih storitev sprejema spremembe strojne opreme in samodejno dodeli naslov IP;
- Povežite kabel od ponudnika internetnih storitev v vrata Ethernet1;
- Konfigurirajte nastavitve omrežne kartice, da pridobite IP naslov avtomatično prek DHCP;
- Povežite računalnik s katerim koli vhodom razen Ethernet1;
- Napravo priključite na vir napajanja;
- Uporabite WebFig v spletni brskalniku ali konfiguracijsko orodje "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Odpri http://192.168.88.1 v spletnem brskalniku, da začneš s postavitvijo. Če IP naslov ni na voljo, uporabi *WinBox* in se poveži prek MAC naslova. Uporabniško ime je "admin", in ni gesla (ali, za nekatere modele, preveri uporabniška in brezžična gesla na nalepki);
- Kliknite na gumb "*Check for updates*" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico zagotovite optimalne zmogljivosti, stabilnost in varnostne posodobitve;
- Nastavite geslo za svoj usmerjevalnik.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen namestitvi v zaprtih prostorih. Izdelek hranite ločeno od vode, ognja, vlage ali vročega okolja.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da iztaknete napajalni kabel iz vtičnice.
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.
Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.12 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler. Alla MikroTik-enheter måste vara professionellt installerat.
:::

*Det här är nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, fullständig EU-försäkran om överensstämmelse, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-59.png)

**Första stegen:**

- Se till att din Internetleverantör accepterar hårdvaruändringar och tilldelar automatiskt en IP-adress;
- Anslut ISP-kabeln till Ethernet1-porten;
- Konfigurera nätverkskortsinställningarna för att automatiskt få IP-adressen med hjälp av DHCP;
- Anslut datorn till valfri port förutom Ethernet1;
- Anslut enheten till en strömkälla;
- Använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Öppna http://192.168.88.1 i en webbläsare för att starta uppställningen. Om IP-adressen inte är tillgänglig, använd *WinBox* och anslut med MAC-adressen. Användarnamnet är "admin", och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "*Check for updates*" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppdatera RouterOS-programvaran till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- Konfigurera lösenordet för din router.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att installeras inomhus. Håll produkten borta från vatten, eld, luftfuktighet eller heta miljöer.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur stickkontakten från eluttaget.
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.
Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.12或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规。所有 MikroTik 設備必須專業安裝
:::

*这是网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*技术规格、完整的欧盟符合性声明、手册以及有关产品的更多信息，请访问 [https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-59.png)

**第一步：**

- 确保您的ISP接受硬件更改，并会自动分配IP地址;
- 将ISP电缆连接到Ethernet1端口;
- 配置您的网络适配器以通过DHCP自动获取IP地址;
- 将计算机连接到除Ethernet1之外的任何端口;
- 将设备连接到电源;
- 在网络浏览器中使用 WebFig 或使用“WinBox”配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) **提供多种配置方法以确保可访问性；**
- 在Web浏览器中打开http://192.168.88.1 以开始设置。如果IP地址不可用，请使用 *WinBox* 并使用MAC地址连接。用户名为“*admin*”，没有密码（或者对于某些型号，请检查标签上的用户和无线密码）;
- 单击"*Check for updates*"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的“Files”菜单，并重新启动设备;
- 通过将RouterOS软件更新到最新版本，您可以确保最佳性能，稳定性和安全更新;
- 设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在安装在室内。 请将本产品远离水，火，潮湿或高温的环境。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 插座應安裝在設備附近，並應易於取用。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源插头。
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。
制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.12 или до последней версии, чтобы обеспечить соответствие требованиям местных органов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов. Все устройства MikroTik должны быть профессионально установлены.
:::

*Это сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, Полная декларация о соответствии требованиям ЕС, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-58.png)

**Первые шаги:**

- Убедитесь, что ваш провайдер принимает аппаратные изменения и автоматически назначит IP-адрес;
- Подключите кабель Интернет-провайдера к порту Ethernet1;
- Настройте параметры вашей сетевой карты для автоматического получения IP-адреса с использованием DHCP;
- Подключите компьютер к любому порту, кроме Ethernet1;
- Подключите устройство к источнику питания;
- Используйте WebFig в веб-браузере или инструмент настройки ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **существует несколько методов настройки для обеспечения доступности;**
- Откройте http://192.168.88.1 в веб-браузере, чтобы начать настройку. Если IP-адрес недоступен, используйте *WinBox* и подключитесь, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте пользовательские и беспроводные пароли на наклейке);
- Нажмите кнопку "*Check for updates*" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- Настройте пароль для вашего роутера.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Изделие предназначено для установки в помещении. Держите этот продукт вдали от воды, огня, влаги или жарких сред.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- Розетка должна быть установлена ​​рядом с оборудованием и должна быть легко доступна.
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.

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
Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. *Cм. на упаковке.*

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge-59.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.12 або останньої версії, щоб забезпечити відповідність нормам місцевої влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил. Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

*Це мережевий пристрій. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_14-4-59.badge-15.png)

**Перші кроки:**

- Переконайтеся, що ваш Інтернет-провайдер приймає зміни обладнання та автоматично призначить IP-адресу;
- Підключіть кабель Інтернет-провайдера до порту Ethernet1;
- Налаштуйте параметри вашої мережевої карти для автоматичного отримання IP-адреси за допомогою DHCP;
- Підключіть комп'ютер до будь-якого порту, крім Ethernet1;
- Підключіть пристрій до адаптеру електроживлення;
- Використовуйте WebFig у веб-браузері або інструмент конфігурації ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **існує декілька методів налаштування для забезпечення доступності;**
- Відкрийте http://192.168.88.1 в веб-браузері, щоб розпочати налаштування. Якщо IP-адреса немає, використовуйте *WinBox* та підключіться за допомогою MAC-адреси. Ім'я користувача - "admin", і пароля немає (або, для деяких моделей, перевірте паролі користувачів та бездротові паролі на етикетці);
- Натисніть кнопку "*Check for updates*" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- Встановіть свій пароль маршрутизатора в нижньому полі.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Це обладнання призначене для встановлення в приміщенні. Тримайте це обладнання подалі від води, вогню, вологи, або гарячого середовища.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик.
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити — від’єднати адаптер електроживлення від розетки. Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.
Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class B digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.
![](./img/fcc_logo_ez.badge-51.jpg)

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

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

## UKCA marking

![](./img/ukca_black_fill.badge-57.gif)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

hEX lite, hEX DC Jack PoE In Ethernet Port hEX PoE DC Jack PoE In Ethernet Port RB3011UiAS-RM, hEX S, RB450Gx4 DC Jack PoE In Ethernet Port RB4011iGS+RM DC Jack PoE In Ethernet Port
24 V / 0.38A 24 V / 2.5A 24 V / 1.2A 24 V / 1.5A
IP20 IP20 IP20 IP20
-40°..+60°C -20°..+60°C -40°..+60°C -40°..+70°C

RB450Gx4 - comes without a power adapter and without a case.

\#77988 #77989 #77990
