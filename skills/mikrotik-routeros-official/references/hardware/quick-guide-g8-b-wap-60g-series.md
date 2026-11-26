# Quick Guide G8-b - wAP 60G series

> Models: RBwAPG-60ad (wAP 60G), RBwAPG-60adkit (Wireless Wire), RBwAPG-60ad-SA (wAP 60Gx3 AP), RBwAPG-60ad-A (wAP 60G AP)

**Models: RBwAPG-60ad (wAP 60G), RBwAPG-60adkit (Wireless Wire), RBwAPG-60ad-SA (wAP 60Gx3 AP), RBwAPG-60ad-A (wAP 60G AP)**

![](./img/mt_logo_arrow_v2-02-63.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.10 or the latest stable version, to ensure compliance with local authority regulations!

It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-71.png)

**First steps:**

- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/WinBox](https://mt.lv/WinBox); **multiple configuration methods are available to ensure accessibility;**
- Download and open "*WinBox"*, and choose the "*Neighbors"* tab to find the device;
- Click on the MAC address. The username is "*admin"* and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- Secure your device and set a strong password;
- For more configuration information, please visit https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP units come pre-configured with WISP Bridge default configuration;
- Wireless Wire and wAP60G units come pre-configured with PTP Bridge default configuration;
- Wireless Wire devices have already, randomly generated, matching SSID, and Wireless passwords.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed both indoors and outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet. The socket-outlet shall be installed near the equipment and shall be easily accessible.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.
## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.10 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са задължени да следват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*

*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-69.png)

**Първи стъпки:**

- Свържете устройството към включения PoE инжектор с Ethernet кабел към края *"data+power"*;
- Свържете края за данни на PoE инжектора към компютъра;
- Свържете захранващия адаптер към PoE инжектора;
- Установете връзка чрез мобилно приложение. Алтернативно, използвайте WebFig в уеб браузър или инструмента за конфигуриране "WinBox" на [https://mt.lv/WinBox](https://mt.lv/WinBox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Изтеглете и отворете *"WinBox"* и изберете раздела *"Neighbors"*, за да намерите устройството;
- Кликнете върху MAC адреса. Потребителското име е *"admin"* и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Кликнете на бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Осигурете устройството си и задайте силна парола;
- За повече информация за конфигурацията, моля, посетете https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP единиците са предварително конфигурирани с конфигурация по подразбиране на WISP Bridge;
- Wireless Wire и wAP60G единиците са предварително конфигурирани с PTP Bridge конфигурация по подразбиране;
- Устройствата Wireless Wire вече са генерирани на случаен принцип съвпадащи парола за SSID и Wireless.

**Информация за безопасност:**

- Преди да работите с всяко MikroTik оборудване, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да бъде инсталиран както на закрито, така и на открито. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате корективни тон и хардуерната конфигурация или да се следват правилните процедури биха могли да доведат до опасна ситуация за хората и повреда на систем м.
- Не можем да гарантираме, че няма да възникнат злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта. Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се изисква да предприеме адекватни мерки!

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.
## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.10 nebo na nejnovější stabilní verzi!
Je na konečném uživateli, aby dodržoval místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*

*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-69.png)

**První kroky:**

- Připojte zařízení k dodávanému PoE injektoru pomocí ethernetového kabelu k datovému a napájecímu konci;
- Připojte zařízení k přiloženému PoE injektoru pomocí ethernetového kabelu do konce *"data+power"*;
- Připojte datový konec PoE injektoru k počítači;
- Připojte napájecí adaptér k PoE injektoru;
- Vytvořte spojení pomocí mobilní aplikace. Alternativně můžete použít WebFig v webovém prohlížeči nebo nástroj pro konfiguraci "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Stáhněte a otevřete *"WinBox"* a vyberte kartu *"Neighbors"*, abyste našli zařízení;
- Klikněte na MAC adresu. Uživatelské jméno je *"admin"* a není zde žádné heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Klepněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do menu "Files" ve WebFig nebo WinBox a restartujte zařízení;
- Zabezpečte zařízení a nastavte silné heslo;
- Další informace o konfiguraci naleznete na adrese https://manual.mikrotik.com/docs/wireless/w60g/;
- Jednotky AP wAP60G jsou předkonfigurovány s výchozí konfigurací mostu WISP;
- Jednotky Wireless Wire a wAP60G jsou předkonfigurovány s výchozí konfigurací PTP Bridge;
- Zařízení Wireless Wire již náhodně vygenerovala odpovídající SSID a bezdrátové heslo.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt lze instalovat uvnitř i venku. Před zahájením instalace si pozorně přečtěte montážní pokyny. Selhání použít Korekce t konfiguraci hardwaru a nebo dodržet správný postup může vést k nebezpečným situacím pro lidi a poškození syst m.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky. Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobovat rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření!

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne blíže než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.
## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.10 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*

*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-69.png)

**Første trin:**

- Tilslut enheden til den medfølgende PoE-injektor med et Ethernet-kabel til *"data+power"* -enden;
- Tilslut dataenden af ​​PoE-injektoren til computeren;
- Tilslut strømadapteren til PoE-injektoren;
- Opret forbindelse ved hjælp af en mobilapplikation. Alternativt kan du bruge WebFig i en webbrowser eller "WinBox" konfigurationsværktøjet på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Download og åbn *"WinBox"*, og vælg fanen *"Neighbors"* for at finde enheden;
- Klik på MAC-adressen. Brugernavnet er *"admin"*, og der er ingen adgangskode (eller, for nogle modeller, tjek brugeradgangskoder og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload downloadede pakker til WebFig eller WinBox "Files" menu og genstart enheden;
- Sikker din enhed, og indstil en stærk adgangskode;
- For mere konfigurationsinformation, se https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- enheder er forudkonfigureret med WISP Bridge-standardkonfiguration;
- Wireless Wire og wAP60G- enheder er forudkonfigureret med PTP Bridge-standardkonfiguration;
- Wireless Wire-enheder har allerede tilfældigt genereret matchende SSID og trådløs adgangskode.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende standardpraksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og begreber.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til denne installationsinstruktion. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt kan installeres både indendørs og udendørs. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten. Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.
- Dette er et produkt i klasse A. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren eventuelt skal træffe passende foranstaltninger!

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.
## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.10 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*

*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-69.png)

**Erste Schritte:**

- Verbinden Sie das Gerät über ein Ethernet-Kabel mit dem *"data+power"* -Ende mit dem mitgelieferten PoE-Injektor;
- Verbinden Sie das Datenende des PoE-Injektors mit dem Computer;
- Schließen Sie das Netzteil an den PoE-Injektor an;
- Stellen Sie eine Verbindung mit einer mobilen Anwendung her. Alternativ können Sie WebFig in einem Webbrowser oder das "WinBox" Konfigurationswerkzeug unter [https://mt.lv/WinBox](https://mt.lv/WinBox) verwenden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- *Laden Sie "WinBox"* herunter, öffnen Sie es und wählen Sie die Registerkarte *"Neighbors",* um das Gerät zu finden;
- Klicken Sie auf die MAC-Adresse. Der Benutzername lautet *"admin"* und es gibt kein Passwort (bei einigen Modellen überprüfen Sie die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Sichern Sie Ihr Gerät und legen Sie ein sicheres Passwort fest;
- Weitere Konfigurationsinformationen finden Sie unter https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- Einheiten sind mit der Standardkonfiguration von WISP Bridge vorkonfiguriert.
- Wireless Wire- und wAP60G- Einheiten sind mit der PTP Bridge-Standardkonfiguration vorkonfiguriert.
- Wireless Wire-Geräte haben bereits zufällig eine übereinstimmende SSID und ein Wireless-Passwort generiert.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt kann sowohl drinnen als auch draußen installiert werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wird die correc zu verwenden t - Hardware und Konfiguration oder die richtigen Verfahren zu folgen in einer Gefahrensituation für Menschen und Schäden an den Syste führen könnten m.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen. Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen!

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.
## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.10 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*

*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια με τη διαμόρφωση, ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-69.png)

**Πρώτα βήματα:**

- Συνδέστε τη συσκευή στον παρεχόμενο εγχυτήρα PoE με ένα καλώδιο Ethernet στο άκρο *"data+power";*
- Συνδέστε το άκρο δεδομένων του εγχυτήρα PoE στον υπολογιστή;
- Συνδέστε το τροφοδοτικό στον εγχυτήρα PoE;
- Δημιουργήστε σύνδεση χρησιμοποιώντας μια κινητή εφαρμογή. Εναλλακτικά, μπορείτε να χρησιμοποιήσετε το WebFig σε έναν περιηγητή ή το εργαλείο διαμόρφωσης "WinBox" στη διεύθυνση [https://mt.lv/WinBox](https://mt.lv/WinBox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Κάντε λήψη και ανοίξτε το *"WinBox"* και επιλέξτε την καρτέλα *"Neighbors"* για να βρείτε τη συσκευή;
- Κάντε κλικ στη διεύθυνση MAC. Το όνομα χρήστη είναι *"admin"* και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματου δικτύου στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα κατεβασμένα πακέτα στο μενού "Files" του WebFig ή του WinBox και επανεκκινήστε τη συσκευή;
- Ασφαλίστε τη συσκευή σας και ορίστε έναν ισχυρό κωδικό πρόσβασης;
- Για περισσότερες πληροφορίες διαμόρφωσης, επισκεφθείτε τη διεύθυνση https://manual.mikrotik.com/docs/wireless/w60g/;
- Οι μονάδες wAP60G AP διαθέτουν προεπιλεγμένη ρύθμιση με προεπιλεγμένη διαμόρφωση WISP Bridge;
- Οι μονάδες Wireless Wire και wAP60G διαθέτουν προεπιλεγμένη ρύθμιση με προεπιλεγμένη διαμόρφωση PTP Bridge;
- Οι συσκευές Wireless Wire έχουν ήδη δημιουργήσει τυχαία αντίστοιχο SSID και Wireless κωδικό πρόσβασης.

**Πληροφορίες για την ασφάλεια:**

- Πριν εργαστείτε σε οποιονδήποτε εξοπλισμό MikroTik, προσέξτε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο το τροφοδοτικό και τα αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για να βεβαιωθεί ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κωδικούς. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν μπορεί να εγκατασταθεί τόσο σε εσωτερικούς όσο και σε εξωτερικούς χώρους. Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η αποτυχία να χρησιμοποιήσει το correc t υλικού και τη διαμόρφωση ή να ακολουθήσουν οι σωστές διαδικασίες θα μπορούσε να οδηγήσει σε μια επικίνδυνη κατάσταση για τους ανθρώπους και να βλάψει την syste μ.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα. Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Αυτό είναι προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει ραδιοπαρεμβολές, οπότε ο χρήστης ενδέχεται να υποχρεωθεί να λάβει επαρκή μέτρα!

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.
## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.10 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*

*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-70.png)

**Primeros pasos:**

- Conecte el dispositivo al inyector PoE incluido con un cable Ethernet al extremo *"data+power"*;
- Conecte el extremo de datos del inyector PoE a la computadora;
- Conecte el adaptador de corriente al inyector PoE;
- Establecer una conexión mediante una aplicación móvil. Alternativamente, puede utilizar WebFig en un navegador web o la herramienta de configuración "WinBox" en [https://mt.lv/WinBox](https://mt.lv/WinBox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Descargue y abra *"WinBox"* y elija la pestaña *"Neighbors"* para encontrar el dispositivo;
- Haga clic en la dirección MAC. El nombre de usuario es *"admin"* y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Sube los paquetes descargados al menú "Files" de WebFig o WinBox y reinicia el dispositivo;
- Asegure su dispositivo y establezca una contraseña segura;
- Para obtener más información sobre la configuración, visite https://manual.mikrotik.com/docs/wireless/w60g/;
- Las unidades wAP60G AP vienen preconfiguradas con la configuración predeterminada de WISP Bridge;
- Las unidades Wireless Wire y wAP60G vienen preconfiguradas con la configuración predeterminada del puente PTP;
- Los dispositivos inalámbricos Wire ya han generado aleatoriamente SSID y contraseña inalámbrica coincidentes.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desarmar, reparar o modificar el dispositivo.
- Este producto se puede instalar tanto en interiores como en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza la correc t hardware y configuración o de seguir los procedimientos correctos podrían dar lugar a una situación de peligro a las personas y daños a la syste m.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente. El tomacorriente se instalará cerca del equipo y será de fácil acceso.
- Este es un producto de clase A. ¡En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas!

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

Módulo WiGig integrado que funciona en la banda de 60 GHz, protocolo 802.11ad con antena direccional incorporada, ganancia máxima de 13.5 dBi.

Canales operacionales de WIGig 58.32 GHz, 60.48 GHz, 62.64 GHz. Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.
## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.10 või uusimale stabiilsele versioonile!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTiku raadioseadmed tuleb installida vastavalt juhistele.
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
**Esimesed sammud:**

![](./img/image2020-2-4_17-31-19.badge-69.png)

- Ühendage seade kaasasoleva PoE-pihustiga Etherneti kaabli abil *"data+power"* otsaga;
- Ühendage PoE-pihusti andmeots arvutiga;
- Ühendage toiteadapter PoE-pihustiga;
- Looge ühendus mobiilirakenduse abil. Alternatiivselt saate kasutada WebFig'i veebibrauseris või "WinBox" konfiguratsioonitööriista aadressil [https://mt.lv/WinBox](https://mt.lv/WinBox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Laadige alla ja avage *"WinBox"* ning valige seadme leidmiseks vahekaart "Neighbors";
- Klõpsake MAC-aadressil. Kasutajanimi on *"admin"* ja parool puudub (või mõne mudeli puhul kontrollige kleebiselt kasutaja ja traadita ühenduse paroole);
- Klõpsake nupul "Check for updates" ja ajakohastage RouterOS viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Lae allalaaditud paketid üles veebibrauseri WebFig või WinBox "Files" menüüsse ja taaskäivita seade;
- Turvaldage seade ja määrake kindel parool;
- Lisateavet konfiguratsiooni kohta leiate aadressilt https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- üksused on eelkonfigureeritud WISP Bridge'i vaikekonfiguratsiooniga;
- Wireless Wire ja wAP60G üksused on eelkonfigureeritud PTP Bridge vaikekonfiguratsiooniga;
- Wireless Wire seadmed on juba juhuslikult genereerinud sobivad SSID ja traadita parool.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt nendele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- Seda toodet saab paigaldada nii sise- kui välistingimustes. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Kasutamata jätmine correc t riistvara ja konfiguratsiooni või järgiks õigeid menetlusi võib põhjustada ohtlikke olukordi inimestele ja kahjustada kõrvamonitori m.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine. Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid - sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist!

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.10 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*

*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*Jos tarvitset ohjeita konfiguroinnissa, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-69.png)

**Ensiaskeleet:**

- Liitä laite mukana toimitettuun PoE-injektoriin Ethernet-kaapelilla *"data+power"* -päähän;
- Liitä PoE-injektorin datapää tietokoneeseen;
- Liitä virtalähde PoE-suuttimeen;
- Muodosta yhteys käyttämällä mobiilisovellusta. Vaihtoehtoisesti voit käyttää WebFigiä selaimessa tai "WinBox" konfiguraatiotyökalua osoitteessa [https://mt.lv/WinBox](https://mt.lv/WinBox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Lataa ja avaa *"WinBox"* ja etsi laite valitsemalla *"Neighbors" -* välilehti;
- Napsauta MAC-osoitetta. Käyttäjätunnus on *"admin"*, eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Napsauta "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFigin tai WinBoxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Suojaa laite ja aseta vahva salasana;
- Lisätietoja määritystiedoista on osoitteessa https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP -yksiköt ovat valmiiksi määritettyinä WISP Bridge -asetuksen oletusasetuksilla;
- Wireless Wire- ja wAP60G- yksiköt on esiasennettu PTP-sillan oletusasetuksiin;
- Wireless Wire laitteet ovat jo satunnaisesti luoneet vastaavan SSID: n ja langattoman salasanan.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote voidaan asentaa sekä sisä- että ulkotiloihin. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Käyttämättä jättäminen CORREC t laitteiston ja kokoonpanon tai noudattaa oikeita menettelytapoja voi johtaa vaarallisiin tilanteisiin ihmisille ja vahingoittaa syste m.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta. Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet!

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.
## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.10 ou la dernière version stable, pour assurer la conformité avec les réglementations des autorités locales!
Il est de la responsabilité de l'utilisateur final de suivre les réglementations nationales locales, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*

*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez chercher un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-69.png)

**Premiers pas:**

- Connectez l'appareil à l'injecteur PoE inclus avec un câble Ethernet à l' extrémité *"data+power"*;
- Connectez l'extrémité de données de l'injecteur PoE à l'ordinateur;
- Connectez l'adaptateur secteur à l'injecteur PoE;
- Établir une connexion à l'aide d'une application mobile. Vous pouvez également utiliser WebFig dans un navigateur Web ou l'outil de configuration "WinBox" à l'adresse [https://mt.lv/WinBox](https://mt.lv/WinBox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Téléchargez et ouvrez "WinBox" et *choisissez* l' onglet *"Neighbors"* pour trouver l'appareil;
- Cliquez sur l'adresse MAC. Le nom d'utilisateur est *"admin"* et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- Sécurisez votre appareil et définissez un mot de passe fort;
- Pour plus d'informations sur la configuration, veuillez visiter https://manual.mikrotik.com/docs/wireless/w60g/;
- Les unités AP wAP60G sont préconfigurées avec la configuration par défaut du pont WISP;
- Les unités Wireless Wire et wAP60G sont préconfigurées avec la configuration par défaut du pont PTP;
- Les périphériques Wireless Wire ont déjà généré de manière aléatoire un SSID et un mot de passe sans fil correspondants.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. L'installateur doit être familiarisé avec les structures, les termes et les concepts du réseau.
- N'utilisez que le bloc d'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit peut être installé à l'intérieur et à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Ne pas utiliser le correc matériel t et de configuration ou de suivre les procédures appropriées pourrait entraîner une situation dangereuse pour les personnes et les dommages aux systè m.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec précaution et le faire fonctionner à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant. La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- Il s'agit d'un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates!

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.
## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.10 ili najnoviju stabilnu verziju kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici obvezni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*

*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-69.png)

**Prvi koraci:**

- Spojite uređaj na priloženi PoE injektor pomoću Ethernet kabela na kraju *"data+power"*;
- Spojite podatkovni kraj PoE injektora na računalo;
- Spojite strujni adapter na PoE injektor;
- Uspostavite vezu pomoću mobilne aplikacije. Opcionalno, koristite WebFig u web pregledniku ili alat za konfiguraciju "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Preuzmite i otvorite *"WinBox"* i odaberite karticu *"Neighbors"* kako biste pronašli uređaj;
- Kliknite na MAC adresu. Korisničko ime je *"admin"* i nema zaporke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Kliknite na gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Prenesite preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Osigurajte svoj uređaj i postavite jaku lozinku;
- Više informacija o konfiguraciji potražite na https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP jedinice dolaze unaprijed konfigurirane sa zadanom konfiguracijom WISP Bridge;
- Jedinice Wireless Wire i wAP60G dolaze unaprijed konfigurirane sa zadanom konfiguracijom PTP Bridge;
- Uređaji Wireless Wire već su nasumično stvorili podudaranje SSID i bežične lozinke.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor koji je odobrio proizvođač, a koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili mijenjati uređaj.
- Ovaj proizvod može se instalirati i unutar i na otvorenom. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne upotrijebite korekcije t hardvera i konfiguracije ili slijediti ispravan postupak može dovesti do opasne situacije za ljude i oštećenja na Syste m.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja zbog nepropisne upotrebe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice. Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- Ovo je proizvod klase A. U domaćem okruženju, ovaj uređaj može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere!

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.
## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.10 vagy a legfrissebb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Minden MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*

*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-69.png)

**Első lépések:**

- Csatlakoztassa az eszközt a mellékelt PoE befecskendezőhöz egy Ethernet-kábellel az *"data+power"-es* végéhez;
- Csatlakoztassa a PoE injektor adatvégét a számítógéphez;
- Csatlakoztassa a hálózati adaptert a PoE befecskendezőhöz;
- Kapcsolat létesítése mobilalkalmazás segítségével. Vagy használja a WebFig-et egy webböngészőben vagy a "WinBox" konfigurációs eszközt a [https://mt.lv/WinBox](https://mt.lv/WinBox) címen; **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Töltse le és nyissa meg *a "WinBox"-t*, majd válassza ki a *"Neighbors"* lapot az eszköz megkereséséhez;
- Kattintson a MAC-címre. A felhasználónév *"admin"*, és nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- Rögzítse a készüléket, és állítson be egy erős jelszót;
- A konfigurációval kapcsolatos további információkért kérjük, látogasson el a https://manual.mikrotik.com/docs/wireless/w60g/;
- A wAP60G AP egységek előre konfigurálva vannak a WISP Bridge alapértelmezett konfigurációjával;
- A Wireless Wire a wAP60G egységek előre konfigurálva vannak a PTP Bridge alapértelmezett konfigurációjával;
- A Wireless Wire eszközök már véletlenszerűen generáltak egyező SSID-t és vezeték nélküli jelszót.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik készüléken dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képzett személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket beltéren és kültéren is be lehet szerelni. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. Ha nem a korrekció t hardver és konfiguráció vagy kövesse a megfelelő eljárásokat vezethet veszélyes helyzetet az emberek és károsíthatja a ren m.
- Nem garantálhatjuk, hogy az eszköz nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból. Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználót szükség lehet megfelelő intézkedések megtételére!

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.
## ID - Indonesian. Panduan Cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.10 atau versi stabil terbaru, untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Pengguna akhir bertanggung jawab untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya keluaran, persyaratan perkabelan, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat radio MikroTik harus diinstal sesuai petunjuk.
:::

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama model produk pada label casing (ID).*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um](https://mt.lv/um) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Spesifikasi teknis, brosur, dan info lebih lanjut mengenai produk di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [https://mt.lv/help](https://mt.lv/help)*
*Jika Anda memerlukan bantuan dalam konfigurasi, silakan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/indonesian.badge-27.png)

**Langkah pertama:**

- Hubungkan perangkat ke injektor PoE yang disertakan dengan kabel Ethernet ke ujung data+power;
- Hubungkan ujung data injektor PoE ke komputer;
- Hubungkan adaptor daya ke injektor PoE;
- Buat koneksi menggunakan aplikasi seluler. Alternatifnya, gunakan WebFig di browser web atau alat konfigurasi "WinBox" di [https://mt.lv/WinBox](https://mt.lv/WinBox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Unduh dan buka "WinBox", dan pilih tab "Neighbors" untuk menemukan perangkat;
- Klik pada alamat MAC. Nama penggunanya adalah "admin" dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu "Files" WebFig atau WinBox dan mulai ulang perangkat;
- Amankan perangkat Anda dan tetapkan kata sandi yang kuat;
- Untuk informasi konfigurasi lebih lanjut, silakan kunjungi https://manual.mikrotik.com/docs/wireless/w60g/;
- Unit AP wAP60G telah dikonfigurasi sebelumnya dengan konfigurasi default WISP Bridge;
- Unit Wireless Wire dan wAP60G telah dikonfigurasi sebelumnya dengan konfigurasi default PTP Bridge;
- Perangkat Kawat Nirkabel telah menghasilkan SSID dan kata sandi Nirkabel yang cocok secara acak.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, dan dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dapat dipasang baik di dalam maupun di luar ruangan. Harap baca petunjuk pemasangan dengan cermat sebelum memulai pemasangan. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem.
- Kami tidak dapat menjamin bahwa tidak akan terjadi kecelakaan atau kerusakan akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan pengoperasian dengan risiko Anda sendiri!
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut adaptor daya dari stopkontak. Stopkontak harus dipasang di dekat peralatan dan mudah dijangkau.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai!

**Paparan Radiasi Frekuensi Radio:** Peralatan MikroTik ini mematuhi batas paparan radiasi Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini sebaiknya dipasang dan dioperasikan tidak lebih dekat dari 20 sentimeter dari tubuh Anda, pengguna pekerjaan, atau masyarakat umum.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.
## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.10 o all'ultima versione stabile, per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento all'interno dei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*

*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, cerca un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-69.png)

**Primi passi:**

- Collegare il dispositivo all'iniettore PoE incluso con un cavo Ethernet all'estremità *"data+power"*;
- Collegare l'estremità dati dell'iniettore PoE al computer;
- Collegare l'alimentatore all'iniettore PoE;
- Stabilire una connessione tramite un'applicazione mobile. In alternativa, utilizza WebFig in un browser web o lo strumento di configurazione "WinBox" all'indirizzo [https://mt.lv/WinBox](https://mt.lv/WinBox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Scarica e apri *"WinBox"* e scegli la scheda *"Neighbors"* per trovare il dispositivo;
- Fare clic sull'indirizzo MAC. Il nome utente è *"admin"* e non è presente alcuna password (oppure, per alcuni modelli, controllare le password utente e wireless sull'adesivo);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Proteggi il tuo dispositivo e imposta una password complessa;
- Per ulteriori informazioni sulla configurazione, visitare https://manual.mikrotik.com/docs/wireless/w60g/;
- Le unità wAP60G AP sono preconfigurate con la configurazione predefinita di WISP Bridge;
- Le unità Wireless Wire e wAP60G sono preconfigurate con la configurazione predefinita di PTP Bridge;
- I dispositivi Wireless Wire hanno già generato casualmente SSID e password wireless corrispondenti.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto può essere installato sia all'interno che all'esterno. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo della correc t hardware e di configurazione o di seguire le procedure corrette potrebbe tradursi in una situazione di pericolo per le persone e danni al syste m.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente. La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate!

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.
## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.10 eða nýjustu stöðugu útgáfuna til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kröfur um kaðall og kröfur um Dynamic Frequency Val (DFS). Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*

*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products).*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is).*
*Ef þú þarft hjálp við stillingar skaltu leita til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-69.png)

**Fyrstu skrefin:**

- Tengdu tækið við meðfylgjandi PoE inndælingartæki með Ethernet snúru við enda *"data+power"*;
- Tengdu gagnaenda PoE inndælingartækisins við tölvuna;
- Tengdu straumbreytinn við PoE inndælingartækið;
- Búið til tengingu með því að nota farsímaforrit. Eða notaðu WebFig í vafra eða stilliverkfærið "WinBox" á [https://mt.lv/WinBox](https://mt.lv/WinBox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Sæktu og opnaðu "WinBox" og *veldu* "Neighbors" flipann *til* að finna tækið;
- Smelltu á MAC vistfangið. Notandanafnið er "admin" og það er ekkert lykilorð (eða, fyrir sumar gerðir, athugaðu notanda og þráðlausa lykilorð á límmiðanum);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum á WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Festu tækið þitt og stilltu sterkt lykilorð;
- Frekari upplýsingar um stillingar eru á https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP einingar eru fyrirfram stilltar með WISP Bridge sjálfgefna stillingu;
- Wireless Wire og wAP60G einingar eru fyrirfram stilltar með PTP Bridge sjálfgefna stillingu;
- Wireless Wire tæki hafa þegar búið til samsvarandi SSID og Wireless lykilorð.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja af þjálfuðu og hæfu starfsfólki samkvæmt þessum leiðbeiningum um uppsetningu. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við það eða breyta því.
- Hægt er að setja þessa vöru bæði innandyra og utandyra. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar að setja upp. Bilun til að nota correc t vélbúnaði og stillingar eða til að fylgja réttra aðferða gæti leitt til hættuástand á fólk og skemmt í syste m.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi. Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir!

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.
## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.10 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukernes ansvar å følge lokale landsbestemmelser, inkludert drift innenfor lovlige frekvenskanaler, utgangseffekt, kablingskrav og krav til dynamisk frekvensvalg (DFS). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*

*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-69.png)

**Første steg:**

- Koble enheten til den medfølgende PoE-injektoren med en Ethernet-kabel til *"data+power"* -enden;
- Koble dataenden av PoE-injektoren til datamaskinen;
- Koble strømadapteren til PoE-injektoren;
- Opprett forbindelse ved hjelp av en mobilapplikasjon. Alternativt kan du bruke WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Last ned og åpne *"WinBox"*, og velg fanen *"Neighbors"* for å finne enheten;
- Klikk på MAC-adressen. Brukernavnet er "admin" og det er ikke noe passord (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- Klikk på knappen "Check for updates" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig eller WinBox "Files"-menyen og start enheten på nytt;
- Sikre enheten din og sett et sterkt passord;
- For mer konfigurasjonsinformasjon, besøk https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- enheter er forhåndskonfigurert med WISP Bridge standardkonfigurasjon;
- Wireless Wire og wAP60G- enheter er forhåndskonfigurert med PTP Bridge-standardkonfigurasjon;
- Wireless Wire-enheter har allerede tilfeldig generert samsvarende SSID og trådløst passord.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet kan installeres både innendørs og utendørs. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke correc t maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til farlige situasjoner for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten. Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- Dette er et klasse A-produkt. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak!

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.
## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.10“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*

*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*Jei jums reikia pagalbos dėl konfigūravimo, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-68.png)

**Pirmieji žingsniai:**

- Prijunkite įrenginį prie pridedamo PoE purkštuko Ethernet kabeliu iki *"data+power"* galo;
- Prijunkite PoE purkštuko duomenų galą prie kompiuterio;
- Prijunkite maitinimo adapterį prie PoE purkštuko;
- Sukurkite ryšį naudodami mobilųjį programėlę. Alternatyviai naudokite WebFig naršyklėje arba konfigūracijos įrankį "WinBox" adresu [https://mt.lv/WinBox](https://mt.lv/WinBox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atsisiųskite ir atidarykite *"WinBox"* ir pasirinkite skirtuką *"Neighbors"*, kad surastumėte įrenginį;
- Spustelėkite MAC adresą. Vartotojo vardas yra *"admin"* ir nėra slaptažodžio (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite įrenginį iš naujo;
- Apsaugokite savo prietaisą ir nustatykite tvirtą slaptažodį;
- Norėdami gauti daugiau informacijos apie konfigūraciją, apsilankykite https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP vienetai yra iš anksto sukonfigūruoti su WISP Bridge numatytąja konfigūracija;
- Wireless Wire ir wAP60G įrenginiai iš anksto sukonfigūruoti naudojant „PTP Bridge“ numatytąją konfigūraciją;
- Wireless Wire įrenginiai jau atsitiktinai sugeneruoja suderinamą SSID ir belaidį slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įrangos montavimas atitiktų vietinius ir nacionalinius elektros reikalavimus. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šį gaminį galima montuoti tiek lauke, tiek lauke. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Nesugebėjimas naudotis Korekcijos t aparatūros ir konfigūraciją arba laikytis tinkamo procedūros gali sukelti pavojingas situacijas prie žmonių ir žalos syste m.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo. Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis produktas gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių!

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.
## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.10 stabilo vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijai.
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*

*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products).*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv).*
*Ja jums nepieciešama palīdzība ar konfigurēšanu, lūdzu, konsultējieties vietnē [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-69.png)

**Pirmie soļi:**

- Pievienojiet ierīci komplektā iekļautajam PoE inžektoram ar Ethernet kabeli pie "data+power" gala;
- Pievienojiet PoE inžektora datu galu datoram;
- Pievienojiet strāvas adapteri PoE inžektoram;
- Izveidojiet savienojumu, izmantojot mobilās lietotnes. Kā alternatīvu varat izmantot WebFig pārlūkprogrammā vai konfigurācijas rīku "WinBox" vietnē [https://mt.lv/WinBox](https://mt.lv/WinBox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Lejupielādējiet un atveriet *"WinBox"* un izvēlieties cilni *"Neighbors"*, lai atrastu ierīci;
- Noklikšķiniet uz MAC adreses. Lietotājvārds ir *"admin"* un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox "Files" izvēlni un pārstartējiet ierīci;
- Iestatiet drošu paroli lapas labajā pusē un apstipriniet;
- Lai iegūtu papildinformāciju par konfigurāciju, lūdzu, apmeklējiet vietni https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP iekārtas ir iepriekš konfigurētas ar WISP Bridge noklusējuma konfigurāciju;
- Wireless Wire un wAP60G iekārtas ir iepriekš konfigurētas ar PTP Bridge noklusējuma konfigurāciju;
- Wireless Wire ierīcēm ir no rūpnīcas uzstādīti atbilstoši SSID un bezvadu paroles.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi, kā novērst negadījumus. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šo izstrādājumu var uzstādīt gan telpās, gan ārpus tām. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nespēja izmantot pareizu aparatūru un konfigurāciju, vai sekot pareizās procedūras var izraisīt bīstamas situācijas un bojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas. Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi!

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.
## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.10 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż operazzjoni fi ħdan kanali tal-frekwenza legali, qawwa tal-ħruġ, rekwiżiti tal-kejbils u rekwiżiti tal-Għażla Dinamika tal-Frekwenza (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*

*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-69.png)

**L-ewwel passi:**

- Qabbad l-apparat mal-injettur PoE inkluż b'kejbil Ethernet mat-tarf *"data+power"*;
- Qabbad it-tarf tad-dejta tal-injettur PoE mal-kompjuter;
- Qabbad l-adapter tal-enerġija mal-injettur PoE;
- Ewlenija bl-użu ta 'applikazzjoni mobbli. Bħala alternattiva, uża l-WebFig f'browser jew l-għodda ta' konfigurazzjoni "WinBox" fuq [https://mt.lv/WinBox](https://mt.lv/WinBox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Niżżel u tiftaħ *"WinBox"*, u agħżel it- tab *"Neighbors"* biex issib l-apparat;
- Ikklikkja fuq l-indirizz MAC. L-isem tal-utent huwa *"admin"* u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u mingħajr fili fuq l-istiker);
- Ikklikkja fuq il-buttuna "Check for updates" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Uploadja tal-pakketti miżjuda fil-menu "Files" ta' WebFig jew WinBox u rerew boot l-apparat;
- Sikura t-tagħmir tiegħek u stabbilixxa password qawwija;
- Għal aktar informazzjoni dwar il-konfigurazzjoni, jekk jogħġbok żur https://manual.mikrotik.com/docs/wireless/w60g/;
- L- unitajiet wAP60G AP jiġu kkonfigurati minn qabel bil-WISP Bridge konfigurazzjoni default;
- Wireless Wire u unitajiet wAP60G jiġu kkonfigurati minn qabel bil-konfigurazzjoni default tal-PTP Bridge;
- L-apparati tal-Wireless Wire diġà ġġeneraw bl-addoċċ l-SSID u l-password bla fili.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skond dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jassigura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott jista 'jiġi installat kemm ġewwa kif ukoll barra. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Nuqqas ta 'użu tal-correc ħardwer tu konfigurazzjoni jew li ssegwi l-proċeduri korretti jista' jwassal għal sitwazzjoni perikoluża għall-persuni u ħsara għall-syste m.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl. Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati!

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Ūnijas 2, Riga, il-Latvja, LV1039.
## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.10 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landregelgeving te volgen, inclusief bediening binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en Dynamic Frequency Selection (DFS) -vereisten. Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*

*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*Als u hulp nodig heeft bij de configuratie, zoek dan een adviseur [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-69.png)

**Eerste stappen:**

- Sluit het apparaat aan op de meegeleverde PoE-injector met een Ethernet-kabel aan het *"data+power"*-uiteinde;
- Sluit het gegevensuiteinde van de PoE-injector aan op de computer;
- Sluit de voedingsadapter aan op de PoE-injector;
- Maak verbinding met behulp van een mobiele applicatie. Als alternatief kunt u WebFig gebruiken in een webbrowser of het configuratiehulpmiddel "WinBox" op [https://mt.lv/WinBox](https://mt.lv/WinBox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Download en open *"WinBox"* en kies het tabblad *"Neighbors"* om het apparaat te vinden;
- Klik op het MAC-adres. De gebruikersnaam is "admin" en er is geen wachtwoord (of, voor sommige modellen, controleer gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Beveilig uw apparaat en stel een sterk wachtwoord in;
- Ga voor meer configuratie-informatie naar https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- units worden vooraf geconfigureerd met standaard WISP Bridge-configuratie;
- Wireless Wire en wAP60G- units zijn vooraf geconfigureerd met standaardconfiguratie van PTP Bridge;
- Wireless Wire-apparaten hebben al willekeurig gegenereerde overeenkomende SSID en draadloos wachtwoord.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die zich in de originele verpakking van dit product bevinden.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product kan zowel binnen als buiten worden geïnstalleerd. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Als u de correctie te gebruiken t hardware en configuratie of het volgen van de juiste procedures kan resulteren in een gevaarlijke situatie aan mensen en schade aan de syste m.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stroomadapter uit het stopcontact te halen. Het stopcontact moet in de buurt van de apparatuur worden geïnstalleerd en moet gemakkelijk toegankelijk zijn.
- Dit is een Klasse A-product. In een huiselijke omgeving kan dit product radio-interferentie veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen dient te nemen!

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.
## PL - Polskie. Szybka porada

:::warning
To urządzenie wymaga aktualizacji do RouterOS v7.10 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Obowiązkiem użytkowników końcowych jest przestrzeganie lokalnych przepisów krajowych, w tym pracy w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być zainstalowane zgodnie z instrukcją.
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*

*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy przy konfiguracji, skontaktuj się z konsultantem [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-69.png)

**Pierwsze kroki:**

- Podłącz urządzenie do dołączonego wtryskiwacza PoE za pomocą kabla Ethernet do końca *"data+power"*;
- Podłącz końcówkę danych wtryskiwacza PoE do komputera;
- Podłącz zasilacz do iniektora PoE;
- Utwórz połączenie za pomocą aplikacji mobilnej. Alternatywnie użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox" pod adresem [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Pobierz i otwórz *"WinBox"*, a następnie wybierz kartę *"Neighbors"*, aby znaleźć urządzenie;
- Kliknij adres MAC. Nazwa użytkownika to *"admin"* i nie ma hasła (lub, w przypadku niektórych modeli, sprawdź hasło użytkownika i hasła sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Prześlij pobrane paczki do menu "Files" WebFig lub WinBox i zrestartuj urządzenie;
- Zabezpiecz swoje urządzenie i ustaw silne hasło;
- Aby uzyskać więcej informacji o konfiguracji, odwiedź https://manual.mikrotik.com/docs/wireless/w60g/;
- Urządzenia wAP60G AP są fabrycznie skonfigurowane z domyślną konfiguracją WISP Bridge;
- Urządzenia Wireless Wire i wAP60G są wstępnie skonfigurowane z domyślną konfiguracją mostka PTP;
- Urządzenia Wireless Wire już losowo wygenerowały pasujący identyfikator SSID i hasło sieci bezprzewodowej.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy na jakimkolwiek sprzęcie MikroTik należy być świadomym zagrożeń związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien znać struktury, terminy i pojęcia sieciowe.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być instalowane przez przeszkolony i wykwalifikowany personel, zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie próbuj rozbierać, naprawiać ani modyfikować urządzenia.
- Ten produkt może być instalowany zarówno wewnątrz, jak i na zewnątrz. Przeczytaj uważnie instrukcję montażu przed rozpoczęciem instalacji. Niewykorzystanie correc t i konfigurację sprzętu lub postępować zgodnie z procedurami, może doprowadzić do niebezpiecznych sytuacji dla ludzi i uszkodzić do syste m.
- Nie możemy zagwarantować, że w wyniku niewłaściwego użytkowania urządzenia nie dojdzie do wypadków ani szkód. Używaj tego produktu ostrożnie i działaj na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego. Gniazdko powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w takim przypadku użytkownik może być zobowiązany do podjęcia odpowiednich środków!

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.
## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.10 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*

*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)* 
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-69.png)

**Primeiros passos:**

- Conecte o dispositivo ao injetor PoE incluído com um cabo Ethernet na extremidade *"data+power"*;
- Conecte a extremidade de dados do injetor PoE ao computador;
- Conecte o adaptador de energia ao injetor PoE;
- Estabelecer uma conexão usando um aplicativo móvel. Alternativamente, use o WebFig em um navegador da web ou a ferramenta de configuração "WinBox" em [https://mt.lv/WinBox](https://mt.lv/WinBox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Faça o download e abra *"WinBox"* e escolha a guia *"Neighbors"* para encontrar o dispositivo;
- Clique no endereço MAC. O nome de usuário é *"admin"* e não há senha (ou, para alguns modelos, verifique as senhas de usuário e wireless no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Faça o upload dos pacotes baixados para o menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Proteja seu dispositivo e defina uma senha forte;
- Para mais informações de configuração, visite https://manual.mikrotik.com/docs/wireless/w60g/;
- As unidades wAP60G AP vêm pré-configuradas com a configuração padrão WISP Bridge;
- As unidades Wireless Wire e wAP60G vêm pré-configuradas com a configuração padrão do PTP Bridge;
- Os dispositivos sem fio já geraram aleatoriamente SSID e senha sem fio correspondentes.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e familiarize-se com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto pode ser instalado em ambientes internos e externos. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização da correc hardware t e configuração ou para seguir os procedimentos correctos pode resultar numa situação perigosa para as pessoas e para danificar o syste m.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por seu próprio risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada. A tomada deve ser instalada próxima ao equipamento e deve ser de fácil acesso.
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas!

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.
## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.10 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să respecte reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*

*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-68.png)

**Primii pasi:**

- Conectați dispozitivul la injectorul PoE inclus cu un cablu Ethernet la capătul *"data+power"*;
- Conectați capătul de date al injectorului PoE la computer;
- Conectați adaptorul de alimentare la injectorul PoE;
- Stabiliți o conexiune folosind o aplicație mobilă. Alternativ, utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox" la [https://mt.lv/WinBox](https://mt.lv/WinBox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Descărcați și deschideți *"WinBox"* și alegeți fila *"Neighbors"* pentru a găsi dispozitivul;
- Faceți clic pe adresa MAC. Numele de utilizator este *"admin"* și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Asigurați-vă dispozitivul și setați o parolă puternică;
- Pentru mai multe informații despre configurare, accesați https://manual.mikrotik.com/docs/wireless/w60g/;
- Unitățile wAP60G AP sunt pre-configurate cu configurația implicită WISP Bridge;
- Unitățile Wireless Wire i wAP60G sunt pre-configurate cu configurația implicită a podului PTP;
- Dispozitivele Wireless Wire au generat deja la întâmplare, potrivire SSID și parolă wireless.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs poate fi instalat atât în ​​interior cât și în exterior. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică. Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate!

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.
## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.10 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných užívateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*

*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-69.png)

**Prvé kroky:**

- Pripojte zariadenie k priloženému PoE injektoru pomocou ethernetového kábla ku koncu *"data+power"*;
- Pripojte dátový koniec PoE injektora k počítaču;
- Pripojte napájací adaptér k PoE injektoru;
- Vytvorte pripojenie pomocou mobilnej aplikácie. Alternatívne použite WebFig v webovom prehliadači alebo nástroj na konfiguráciu "WinBox" na adrese [https://mt.lv/WinBox](https://mt.lv/WinBox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Stiahnite si a otvorte *"WinBox"* a vyberte kartu *"Neighbors"*, aby ste našli zariadenie;
- Kliknite na MAC adresu. Používateľské meno je *"admin"* a neexistuje žiadne heslo (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslo na nálepke);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" vo WebFig alebo WinBox a reštartujte zariadenie;
- Zabezpečte svoje zariadenie a nastavte silné heslo;
- Viac informácií o konfigurácii nájdete na stránke https://manual.mikrotik.com/docs/wireless/w60g/;
- Jednotky wAP60G AP sú predkonfigurované s predvolenou konfiguráciou mosta WISP;
- Jednotky Wireless Wire a wAP60G sú predkonfigurované s predvolenou konfiguráciou PTP Bridge;
- Zariadenia Wireless Wire už náhodne vygenerovali zodpovedajúce SSID a bezdrôtové heslo.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať ani upravovať.
- Tento produkt je možné nainštalovať vo vnútri aj vonku. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Zlyhanie použiť Korekcia t konfiguráciu hardvéru a alebo dodržať správny postup môže viesť k nebezpečným situáciám pre ľudí a poškodenia syst m.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky. Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia!

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie blížej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.
## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.10 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so odgovorni za upoštevanje lokalnih predpisov, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
**Prvi koraki:**

![](./img/image2020-2-5_9-46-47.badge-69.png)

- Povežite napravo s priloženim injektorjem PoE z ethernetnim kablom na koncu *"data+power"*;
- Priključite podatkovni konec injektorja PoE na računalnik;
- Priključite napajalnik na injektor PoE;
- Ustvarite povezavo z uporabo mobilne aplikacije. Kot alternativo uporabite WebFig v spletnem brskalniku ali orodje za konfiguracijo "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Prenesite in odprite *"WinBox"* ter izberite zavihek *"Neighbors"*, da poiščete napravo;
- Kliknite naslov MAC. Uporabniško ime je *"admin"* in ni gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Kliknite na gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" WebFig ali WinBox in znova zaženite napravo;
- Zavarujte svojo napravo in nastavite močno geslo;
- Za več informacij o konfiguraciji obiščite https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP enote so predhodno konfigurirane s privzeto konfiguracijo WISP Bridge;
- Wireless Wire enote WAP60G so predhodno konfigurirane s privzeto konfiguracijo PTP Bridge;
- Naprave Wireless Wireless so že naključno ustvarile ujemajoča se gesla SSID in Wireless.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti električnega tokokroga in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec, in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje, skladno s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Ne poskušajte razstaviti, popraviti ali spremeniti naprave.
- Ta izdelek lahko namestite tako v zaprtih prostorih kot na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Če ne uporabite correc t strojne opreme in konfiguracija ali sledite pravilni postopki lahko povzroči nevarne situacije za ljudi in škodo na Syste m.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice. Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje; v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe!

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*

*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-69.png)

**Första stegen:**

- Anslut enheten till den medföljande PoE-injektorn med en Ethernet-kabel till *"data+power"* -änden;
- Anslut dataänden på PoE-injektorn till datorn;
- Anslut strömadaptern till PoE-injektorn;
- Skapa en anslutning med hjälp av en mobilapplikation. Alternativt använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Ladda ner och öppna *"WinBox"* och välj fliken *"Neighbors"* för att hitta enheten;
- Klicka på MAC-adressen. Användarnamnet är *"admin"* och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Säkra din enhet och ställa in ett starkt lösenord;
- För mer konfigurationsinformation, besök https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP- enheter är förkonfigurerade med WISP Bridge standardkonfiguration;
- Wireless Wire och wAP60G- enheter är förkonfigurerade med PTP Bridge-standardkonfiguration;
- Wireless Wire-enheter har redan slumpmässigt genererat matchande SSID och trådlöst lösenord.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast strömförsörjningen och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt kan installeras både inomhus och utomhus. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på syste m.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och hantera på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget. Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder!

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.
## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.10或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道中运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*

*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)* 
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请寻求顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-69.png)

**第一步：**

- *使用连接到"data+power"* 端的以太网电缆将设备连接到随附的 PoE 注入器 ；
- 将PoE供电器的数据端连接到电脑；
- 将电源适配器连接到 PoE 供电器；
- 使用移动应用程序建立连接。或者，使用WebFig在Web浏览器中或在[https://mt.lv/WinBox](https://mt.lv/WinBox) 上的"WinBox"配置工具; **提供多种配置方法以确保可访问性；**
- 下载并打开 *"WinBox"* ，选择 *"Neighbors"* 选项 卡找到设备；
- 单击 MAC 地址。 用户名是 *"admin"* 并且没有密码 **（或者，对于某些型号，检查标签上的用户和无线密码）**；
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的“Files”菜单，并重新启动设备;
- 保护您的设备并设置安全密码；
- 有关更多配置信息，请访问 https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP 单元已预先配置了WISP Bridge默认配置；
- Wireless Wire 和 wAP60G 单元已预先配置了PTP Bridge默认配置。
- 无线有线设备 Wireless Wire 已经随机生成了匹配的SSID和无线密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和配件，这些电源和配件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。安装程序负责确保设备的安装符合当地和国家的电气法规。请勿尝试拆卸，修理或修改设备。
- 该产品可以安装在室内和室外。在开始安装之前，请仔细阅读安装说明。若未使用correc 牛逼的硬件和配置，或者按照正确的程序可能会导致危险情况的人并伤害到SYSTE 米。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。请谨慎使用本产品，风险自负！
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。插座應安裝在設備附近，並應易於取用。
- 这是A类产品。在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施！

**射频辐射暴露：** 该 MikroTik 设备符合针对不受控制的环境规定的欧盟辐射暴露限制。 此 MikroTik 设备的安装和使用距离您的身体、专业用户或公众不得超过 20 厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。
## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.10 или последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, выходной мощности, требований к кабельным системам и требований к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*

*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)* 
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-68.png)

**Первые шаги:**

- Подключите устройство к PoE инжектору, который входит в комплект, при помощью кабеля Ethernet к *"data+power"*;
- Подключите конец данных инжектора PoE к компьютеру;
- Подключите адаптер питания к PoE инжектору;
- Установите соединение с помощью мобильного приложения. В качестве альтернативы используйте WebFig в веб-браузере или инструмент конфигурации "WinBox" по адресу [https://mt.lv/WinBox](https://mt.lv/WinBox); **существует несколько методов настройки для обеспечения доступности;**
- Загрузите и откройте *"WinBox"* и выберите вкладку *"Neighbors"*, чтобы найти устройство;
- Нажмите на MAC-адрес. Имя пользователя *"admin"* и пароль отсутствует (или, для некоторых моделей, проверьте пароль пользователя и беспроводной сети на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" WebFig или WinBox и перезагрузите устройство;
- Защитите свое устройство и установите надежный пароль;
- Для получения дополнительной информации о конфигурации, пожалуйста, посетите https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP поставляются с предварительно сконфигурированной конфигурацией WISP Bridge по умолчанию;
- Устройства Wireless Wire и wAP60G поставляются с предварительно настроенной конфигурацией по умолчанию для моста PTP;
- Устройства Wireless Wire уже случайно сгенерировали совпадающие SSID и пароль Wireless.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать как в помещении, так и на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки. Розетка должна быть установлена ​​рядом с оборудованием и должна быть легко доступна.
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
Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 20 сантиметров от человека.*

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge-69.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:
## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.10 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!

Кінцеві користувачі несуть відповідальність за дотримання місцевих норм, включаючи роботу в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-24.png)

**Перші кроки:**

- Під’єднайте пристрій до PoE-інжектора, що входить до комплекту, за допомогою кабелю Ethernet до кінця передачі даних+живлення *"data+power"*;
- Підключіть кінець даних PoE-інжектора до комп’ютера;
- Підключіть адаптер живлення до PoE-інжектора;
- Встановіть з'єднання за допомогою мобільного додатка. В іншому випадку використовуйте WebFig у веб-браузері, або інструмент конфігурації "WinBox" за адресою [https://mt.lv/WinBox](https://mt.lv/WinBox); **існує декілька методів налаштування для забезпечення доступності;**
- Завантажте та відкрийте *"WinBox"* і виберіть вкладку *"Neighbors"*, щоб знайти пристрій;
- Натисніть на MAC-адресу. Ім’я користувача - *"admin"* і немає пароля (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Натисніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" WebFig або WinBox та перезавантажте пристрій;
- Захистіть свій пристрій і встановіть надійний пароль;
- Для отримання додаткової інформації про конфігурацію, відвідайте https://manual.mikrotik.com/docs/wireless/w60g/;
- wAP60G AP поставляються заздалегідь з конфігурацією за замовчуванням WISP Bridge;
- Пристрої Wireless Wire та wAP60G поставляються заздалегідь з конфігурацією за замовчуванням PTP Bridge;
- Пристрої Wireless Wire вже випадково генерують відповідні паролі SSID та Wireless.

**Інформація про безпеку:**

- Перш ніж працювати над будь-яким обладнанням MikroTik, пам’ятайте про небезпеки, пов'язані з електричною схемою, та ознайомтеся зі стандартними методами запобігання аварій. Інсталятор повинен бути знайомий з мережевими структурами, термінами та поняттями.
- Використовуйте тільки джерело живлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Це обладнання можна встановлювати як в приміщенні, так і на вулиці. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик.
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки. Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- Це продукт класу А. У побутових умовах цей продукт може спричинити радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити належних заходів!

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.
## Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| RBwAPG-60adkit | TV7WAPG60AD |
| RBwAPG-60ad | TV7WAPG60AD |
| RBwAPG-60ad-A | TV7WAPG60AD |
| RBwAPG-60ad-SA | TV7WAPG60ADM |

![](./img/fcc_logo_ez.badge-61.jpg)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

This device is not to be operated on aircraft except for the conditions listed on FCC CFR §15.255 (b)

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| RBwAPG-60adkit | 7442A-WAPG60AD |
| RBwAPG-60ad | 7442A-WAPG60AD |
| RBwAPG-60ad-A | 7442A-WAPG60AD |
| RBwAPG-60ad-SA | 7442A-WAPG60ADM |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

This device is not to be operated on aircraft except for the conditions listed on ISED RSS-210 Annex J.1.

Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## UKCA marking

![](./img/ukca_black_fill.badge-67.gif)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RouterBOARD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RouterBOARD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen RouterBOARD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp RouterBOARD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός RouterBOARD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type RouterBOARD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RouterBOARD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp RouterBOARD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RouterBOARD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type RouterBOARD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RouterBOARD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a RouterBOARD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio RouterBOARD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að RouterBOARD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas RouterBOARD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RouterBOARD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju RouterBOARD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur RouterBOARD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret RouterBOARD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RouterBOARD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RouterBOARD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RouterBOARD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RouterBOARD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme RouterBOARD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RouterBOARD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products) |

This device meets the Maximum TX power limit per ETSI regulations. The frequency and the maximum transmitted power in the EU are listed below: 57 - 66 GHz: 17.95 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:
![](./img/tab-4.png)

#

## WiGig

| Operational channels / Maximum output power Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность | 58.32 GHz / 40 dBm |
| --- | --- |
| 60.48 GHz / 40 dBm | |
| 62.64 GHz / 40 dBm | |

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

DC Jack PoE In Ethernet Port
24 V / 0.38
IP55
-33°..+70°C

\#72848
