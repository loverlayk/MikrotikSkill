# Quick Guide - LtAP series

> Models: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit)

**Models: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit)**

![](./img/image2020-2-5_9-24-15-11.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v6.49.7 or the latest stable version, to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

This Quick Guide covers models: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-95.png)

This Device accepts input of 24V DC, 1.2 A power adapter, which is provided in the original packaging of this device. Alternatively, it's possible to use a PoE injector together with the power source in the range of 12-30 V (direct current) or an Automotive DC port together with a power source of 12-30 V (direct current).

**First steps:**

- Unscrew two screws and remove the cover;
- Connect your Internet cable to the Ethernet port (this is optional if using LTE as the primary connection);
- Insert the SIM card into the SIM 2 slot (middle);
- Connect GPS antenna (optional);
- Connect to the power source;
- Set your computer IP configuration to automatic (DHCP);
- From your computer connect to the wireless network;
- Open the https://192.168.88.1 in your web browser, for *LtAP model* Download the WinBox configuration tool [https://mt.lv/winbox](https://mt.lv/winbox), there is no default IP address set, use the Neighbors tab and connect through the MAC address;
- User name: *admin*, and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Use the check for update option to upgrade the device to the latest version. You must have an active SIM card with available data;
- The device will reboot;
- Connect again and in the *QuickSet* menu set your country, to apply country regulation settings;
- Secure your device and set a strong password;
- The *LtAP* device comes without a modem, install it before inserting a SIM card.
- The following RouterOS "npk" packages are required for the core functionality of the product: gps, system.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v6.49.7 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-90.png)

Това устройство приема вход на 24V DC, 1.2 A адаптер за захранване, който се предлага в оригиналната опаковка на това устройство. Освен това е възможно да използвате PoE инжектор заедно с източника на захранване в диапазон 12-30 V (постоянен ток) или Automotive DC порт заедно с източник на захранване 12-30 V (постоянен ток).

**Първи стъпки:**

- Развийте два винта и отстранете капака;
- Свържете вашия интернет кабел към Ethernet порта (това не е задължително, ако използвате LTE като основна връзка);
- Поставете SIM картата в слота за SIM 2 (в средата);
- Свържете GPS антена (по избор);
- Свържете се към източника на захранване;
- Задайте автоматична IP конфигурация на вашия компютър (DHCP);
- От вашия компютър се свържете към безжичната мрежа;
- Отворете https://192.168.88.1 във вашия уеб браузър, за LtAP модел Изтеглете инструмента за конфигуриране на WinBox [https://mt.lv/winbox](https://mt.lv/winbox), няма зададен IP адрес по подразбиране, използвайте раздела Съседи и се свържете през MAC адреса;
- Потребителско име: *admin* и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Използвайте опция за проверка за актуализация, за да надстроите устройството до най-новата версия. Трябва да имате активна SIM карта с налични данни;
- Устройството ще се рестартира;
- Свържете се отново и в менюто *QuickSet* задайте вашата страна, за да приложите настройките за регулиране на страната;
- Осигурете устройството си и задайте силна парола;
- *LtAP* без модем, инсталирайте го преди да поставите SIM карта.
- Следните RouterOS "npk" пакети са необходими за основната функционалност на продукта: gps, system.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за монтиране на открито върху стълб. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате правилния хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация FCC, IC и Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Brivibas gatve 214i Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v6.49.7 nebo na nejnovější stabilní verzi!
Je na koncových uživatelích, aby dodržovali místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
Tento Stručný průvodce zahrnuje modely: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*

![](./img/image2020-2-4_17-16-42.badge-90.png)

Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.

Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)

*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*

Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)

*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Toto zařízení přijímá vstup 24 V DC, 1,2 A napájecí adaptér, který je dodáván v originálním balení tohoto zařízení. Alternativně je možné použít vstřikovač PoE společně se zdrojem energie v rozsahu 12-30 V (stejnosměrný proud) nebo automobilovým stejnosměrným portem společně se zdrojem energie 12-30 V (stejnosměrný proud).

**První kroky:**

- Odšroubujte dva šrouby a sejměte kryt;
- Připojte svůj internetový kabel k ethernetovému portu (je to volitelné, pokud používáte LTE jako primární připojení);
- Vložte SIM kartu do slotu SIM 2 (uprostřed);
- Připojte anténu GPS (volitelné);
- Připojte se ke zdroji energie;
- Nastavte IP adresu počítače na automatickou (DHCP);
- Z počítače se připojte k bezdrátové síti;
- Otevřete ve svém webovém prohlížeči https://192.168.88.1, pro model LtAP Stáhněte si konfigurační nástroj WinBox [https://mt.lv/winbox](https://mt.lv/winbox), není nastavena žádná výchozí IP adresa, použijte kartu Neighbors a připojte se přes MAC adresu;
- Uživatelské jméno: *admin* a není zde žádné heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Chcete-li upgradovat zařízení na nejnovější verzi, použijte možnost Zkontrolovat aktualizaci. Musíte mít aktivní SIM kartu s dostupnými daty;
- Zařízení se restartuje;
- Připojte se znovu a v nabídce *QuickSet* nastavte svou zemi, abyste použili nastavení regulace země;
- Zabezpečte zařízení a nastavte silné heslo;
- Zařízení *LtAP* jsou dodávána bez modemu, nainstalujte je před vložením SIM karty.
- Pro základní funkčnost produktu jsou vyžadovány následující balíčky RouterOS "npk": gps, system.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k montáži venku na sloup. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete správný hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření FCC, IC a Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Brivibas gatve 214i Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v6.49.7 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*

![](./img/image2020-2-4_17-13-55.badge-90.png)

Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.

Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)

*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*

Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)

*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Denne enhed accepterer indgang på 24V DC, 1,2 A strømadapter, der leveres i denne enheds originale emballage. Alternativt er det muligt at bruge PoE-injektor sammen med strømkilden i området 12-30 V (jævnstrøm) eller Automotive DC-port sammen med strømkilden 12-30 V (jævnstrøm).

**Første trin:**

- Skru af to skruer, og fjern dækslet;
- Tilslut dit internetkabel til Ethernet-porten (dette er valgfrit, hvis du bruger LTE som den primære forbindelse);
- Indsæt SIM-kortet i SIM 2-åbningen (i midten);
- Tilslut GPS-antenne (valgfrit);
- Tilslut til strømkilden;
- Indstil din computers IP-konfiguration til automatisk (DHCP);
- Fra din computer skal du oprette forbindelse til det trådløse netværk;
- Åbn https://192.168.88.1 i din webbrowser, for LtAP-model Download WinBox-konfigurationsværktøjet [https://mt.lv/winbox](https://mt.lv/winbox), der er ingen standard IP-adresse, brug fanen Naboer og tilslut via MAC-adressen;
- Brugernavn: *admin*, og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløs adgangskoder på mærkaten);
- Brug check for opdateringsindstilling for at opgradere enheden til den nyeste version. Du skal have et aktivt SIM-kort med tilgængelige data;
- Enheden genstarter;
- Opret forbindelse igen, og indstil dit land i *QuickSet* menuen for at anvende indstillinger for landegulering;
- Sikker din enhed, og indstil en stærk adgangskode;
- *LtAP* enheder leveres uden et modem, installer det, før du indsætter et SIM-kort.
- Følgende RouterOS "npk"-pakker er nødvendige for produktets kernefunktionalitet: gps, system.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive monteret udendørs på en stang. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den rigtige hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og beskadigelse af systemet.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder FCC, IC og EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Brivibas gatve 214i Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v6.49.7 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
Diese Kurzanleitung behandelt Modelle: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*

![](./img/image2020-2-4_17-20-45.badge-90.png)

Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.

Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)

*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*

Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)

*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Dieses Gerät akzeptiert den Eingang von 24 V DC, 1,2 A Netzteil, das in der Originalverpackung dieses Geräts enthalten ist. Alternativ ist es möglich, den PoE-Injektor zusammen mit der Stromquelle im Bereich von 12 bis 30 V (Gleichstrom) oder den Kfz-Gleichstromanschluss zusammen mit der Stromquelle 12 bis 30 V (Gleichstrom) zu verwenden.

**Erste Schritte:**

- Lösen Sie zwei Schrauben und entfernen Sie die Abdeckung;
- Schließen Sie Ihr Internetkabel an den Ethernet-Port an (dies ist optional, wenn Sie LTE als primäre Verbindung verwenden);
- Legen Sie die SIM-Karte in den SIM 2-Steckplatz (Mitte) ein;
- GPS-Antenne anschließen (optional);
- An die Stromquelle anschließen;
- Stellen Sie die IP-Konfiguration Ihres Computers auf automatisch (DHCP) ein;
- Stellen Sie von Ihrem Computer aus eine Verbindung zum drahtlosen Netzwerk her;
- Öffnen Sie https://192.168.88.1 in Ihrem Webbrowser, für das LtAP-Modell Laden Sie das WinBox-Konfigurationstool [https://mt.lv/winbox](https://mt.lv/winbox) herunter, es ist keine Standard-IP-Adresse festgelegt, verwenden Sie die Registerkarte „Nachbarn“ und stellen Sie eine Verbindung über die MAC-Adresse her;
- Benutzername: *admin*, und es gibt kein Passwort (oder überprüfen Sie bei einigen Modellen die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Verwenden Sie die Option Nach Updates suchen, um das Gerät auf die neueste Version zu aktualisieren. Sie müssen über eine aktive SIM-Karte mit verfügbaren Daten verfügen;
- Das Gerät wird neu gestartet;
- *Stellen* Sie erneut eine Verbindung her und legen Sie im *QuickSet* Menü Ihr Land fest, um die Länderregulierungseinstellungen anzuwenden;
- Sichern Sie Ihr Gerät und legen Sie ein sicheres Passwort fest;
- Die *LtAP* Geräte werden ohne Modem geliefert. Installieren Sie es, bevor Sie eine SIM-Karte einlegen.
- Die folgenden RouterOS „npk“-Pakete sind für die Kernfunktionalität des Produkts erforderlich: gps, system.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Montage im Freien an einer Stange vorgesehen. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie nicht die richtige Hardware und Konfiguration verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zu Schäden am System führen.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den FCC-, IC- und EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v6.49.7 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
Αυτός ο γρήγορος οδηγός καλύπτει μοντέλα: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*

![](./img/image2020-2-4_17-25-41.badge-90.png)

Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.

Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)

*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*

Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)

*Εάν χρειάζεστε βοήθεια σχετικά με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Αυτή η συσκευή δέχεται είσοδο τροφοδοτικού 24V DC, 1.2 A, ο οποίος παρέχεται στην αρχική συσκευασία αυτής της συσκευής. Εναλλακτικά, είναι δυνατή η χρήση εγχυτήρα PoE μαζί με την πηγή ισχύος στην περιοχή 12-30 V (συνεχές ρεύμα) ή τη θύρα DC αυτοκινήτου μαζί με την πηγή ισχύος 12-30 V (συνεχές ρεύμα).

**Πρώτα βήματα:**

- Ξεβιδώστε δύο βίδες και αφαιρέστε το κάλυμμα.
- Συνδέστε το καλώδιο Internet στη θύρα Ethernet (αυτό είναι προαιρετικό εάν χρησιμοποιείτε το LTE ως κύρια σύνδεση).
- Τοποθετήστε την κάρτα SIM στην υποδοχή SIM 2 (μεσαία).
- Συνδέστε την κεραία GPS (προαιρετικά).
- Συνδεθείτε στην πηγή τροφοδοσίας.
- Ρυθμίστε τη διαμόρφωση IP του υπολογιστή σας σε αυτόματη (DHCP).
- Από τον υπολογιστή σας, συνδεθείτε στο ασύρματο δίκτυο.
- Ανοίξτε το https://192.168.88.1 στο πρόγραμμα περιήγησής σας στον ιστό, για το μοντέλο LtAP Κατεβάστε το εργαλείο διαμόρφωσης WinBox [https://mt.lv/winbox](https://mt.lv/winbox), δεν έχει οριστεί προεπιλεγμένη διεύθυνση IP, χρησιμοποιήστε την καρτέλα Neighbors και συνδεθείτε μέσω της διεύθυνσης MAC;
- Όνομα χρήστη: *admin* και δεν υπάρχει κωδικός πρόσβασης.
- Χρησιμοποιήστε την επιλογή check for update για να αναβαθμίσετε τη συσκευή στην πιο πρόσφατη έκδοση. Πρέπει να έχετε μια ενεργή κάρτα SIM με διαθέσιμα δεδομένα.
- Η συσκευή θα επανεκκινήσει.
- Συνδεθείτε ξανά και στο μενού *QuickSet* ορίστε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις κανονισμού χώρας.
- Ασφαλίστε τη συσκευή σας και ορίστε έναν ισχυρό κωδικό πρόσβασης;
- Οι συσκευές *LtAP* έρχονται χωρίς μόντεμ, τοποθετήστε το πριν τοποθετήσετε μια κάρτα SIM.
- Τα ακόλουθα πακέτα RouterOS "npk" απαιτούνται για τη βασική λειτουργικότητα του προϊόντος: gps, system.

**Πληροφορίες για την ασφάλεια:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται να τοποθετηθεί σε εξωτερικό χώρο σε έναν πόλο. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του σωστού υλικού και διαμόρφωσης ή η παρακολούθηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας FCC, IC και Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Brivibas gatve 214i Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v6.49.7 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
Esta guía rápida cubre los modelos: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*

![](./img/image2020-2-4_17-27-25.badge-92.png)

Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.

Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)

*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*

Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)

*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Este dispositivo acepta la entrada de 24 V CC, un adaptador de alimentación de 1,2 A, que se proporciona en el embalaje original de este dispositivo. Alternativamente, es posible usar el inyector PoE junto con la fuente de alimentación en el rango de 12-30 V (corriente continua) o el puerto DC automotriz junto con la fuente de alimentación de 12-30 V (corriente continua).

**Primeros pasos:**

- Desatornille dos tornillos y retire la cubierta;
- Conecte su cable de Internet al puerto Ethernet (esto es opcional si usa LTE como conexión principal);
- Inserte la tarjeta SIM en la ranura SIM 2 (centro);
- Conecte la antena GPS (opcional);
- Conéctese a la fuente de alimentación;
- Establezca la configuración de IP de su computadora en automática (DHCP);
- Desde su computadora, conéctese a la red inalámbrica;
- Abra https://192.168.88.1 en su navegador web, para el modelo LtAP Descargue la herramienta de configuración de WinBox [https://mt.lv/winbox](https://mt.lv/winbox), no hay una dirección IP predeterminada establecida, use la pestaña Vecinos y conéctese a través de la dirección MAC;
- Nombre de usuario: *admin*, y no hay contraseña;
- Use la opción Buscar actualización para actualizar el dispositivo a la última versión. Debe tener una tarjeta SIM activa con datos disponibles;
- El dispositivo se reiniciará;
- Conéctese nuevamente y en el menú *QuickSet* configure su país, para aplicar la configuración de la regulación del país;
- Asegure su dispositivo y establezca una contraseña segura;
- El dispositivo *LtAP* viene sin módem, instálelo antes de insertar una tarjeta SIM.
- Se requieren los siguientes paquetes "npk" de RouterOS para la funcionalidad principal del producto: gps, system.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para montarse en exteriores en un poste. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podría producir una situación peligrosa para las personas y dañar el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la FCC, IC y la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Brivibas gatve 214i Riga, Letonia, LV1039.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, protocolo 802.11b / g / n con antena PCB incorporada, ganancia máxima de 2.5 dBi.

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Brivibas gatve 214i, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v6.49.7 või uusimale stabiilsele versioonile!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTiku raadioseadmed tuleb installida vastavalt juhistele.
See kiirjuhend hõlmab mudeleid: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*

![](./img/image2020-2-4_17-31-19.badge-90.png)

Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.

Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)

*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*

Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)

*Kui vajate konfigureerimisel abi, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

See seade võtab vastu 24 V alalisvoolu, 1,2 toiteadapterit, mis on selle seadme originaalpakendis. Teise võimalusena on võimalik kasutada PoE-injektorit koos toiteallikaga vahemikus 12-30 V (alalisvool) või autotööstuse alalisvoolu porti koos toiteallikaga 12-30 V (alalisvoolu).

**Esimesed sammud:**

- Keerake kaks kruvi lahti ja eemaldage kaas;
- Ühendage oma Interneti-kaabel Etherneti pordiga (see on valikuline, kui primaarühendusena kasutatakse LTE);
- Sisestage SIM-kaart SIM 2 pesasse (keskel);
- Ühendage GPS-antenn (valikuline);
- Ühendage toiteallikaga;
- Seadke arvuti IP-konfiguratsioon automaatseks (DHCP);
- Ühendage arvutist traadita võrguga;
- Avage oma veebibrauseris https://192.168.88.1, LtAP mudeli jaoks Laadige alla WinBoxi konfiguratsioonitööriist [https://mt.lv/winbox](https://mt.lv/winbox), vaike IP-aadressi pole määratud, kasutage vahekaarti Naabrid ja ühendage MAC-aadressi kaudu;
- Kasutajanimi: *admin* ja parool puudub;
- Seadme värskendamiseks uusimale versioonile kasutage värskenduse kontrollimise võimalust. Teil peab olema aktiivne saadaolevate andmetega SIM-kaart;
- Seade taaskäivitatakse;
- Ühendage uuesti ja seadistage oma riigis riigi seadistuste seadistamiseks menüü *QuickSet*;
- Turvaldage seade ja määrake kindel parool;
- *LtAP* tulevad ilma modemita, installige see enne SIM-kaardi sisestamist.
- Toote põhifunktsioonide jaoks on vajalikud järgmised RouterOS-i "npk" paketid: gps, system.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud paigaldamiseks välistingimustele. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Õige riistvara ja konfiguratsiooni kasutamata jätmine või õigete protseduuride mittejärgimine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab FCC, IC ja Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Brivibas gatve 214i Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v6.49.7 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
Tämä pikaopas kattaa mallit: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*

![](./img/image2020-2-4_17-33-3.badge-90.png)

Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.

Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)

*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*

Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)

*Jos tarvitset ohjeita konfiguroinnissa, kysy neuvoa- antajalta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Tämä laite hyväksyy 24 V DC: n, 1.2 A: n virtalähteen tulon, joka toimitetaan laitteen alkuperäispakkauksessa. Vaihtoehtoisesti on mahdollista käyttää PoE-injektoria yhdessä teholähteen kanssa alueella 12-30 V (tasavirta) tai Automotive DC-porttia yhdessä teholähteen 12-30 V (tasavirta) kanssa.

**Ensiaskeleet:**

- Kierrä kaksi ruuvia irti ja poista kansi;
- Kytke Internet-kaapeli Ethernet-porttiin (tämä on valinnainen, jos ensisijaisena yhteytenä käytetään LTE);
- Aseta SIM-kortti SIM 2 -korttipaikkaan (keskelle);
- Liitä GPS-antenni (valinnainen);
- Kytke virtalähteeseen;
- Aseta tietokoneesi IP-määritykset automaattiseksi (DHCP);
- Yhdistä tietokoneeltasi langattomaan verkkoon;
- Avaa verkkoselaimessa https://192.168.88.1. LtAP-malli Lataa WinBox-määritystyökalu [https://mt.lv/winbox](https://mt.lv/winbox), oletus-IP-osoitetta ei ole asetettu, käytä Naapurit-välilehteä ja muodosta yhteys MAC-osoitteen kautta.;
- Käyttäjätunnus: *admin*, eikä salasanaa ole;
- Päivitä laite uusimpaan versioon käyttämällä päivitysvaihtoehtoa. Sinulla on oltava aktiivinen SIM-kortti, jossa on käytettävissä olevia tietoja;
- Laite käynnistyy uudelleen;
- Yhdistä uudelleen ja aseta maa *QuickSet* valikossa soveltaaksesi maan sääntelyasetuksia;
- Suojaa laite ja aseta vahva salasana;
- *LtAP* laitteet toimitetaan ilman modeemia, asenna se ennen SIM-kortin asettamista.
- Tuotteen ydintoimintoihin tarvitaan seuraavat RouterOS "npk" -paketit: gps, system.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi ulkona sauvaan. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on FCC: n, IC: n ja Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Brivibas gatve 214i Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v6.49.7 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*

![](./img/image2020-2-4_17-35-53.badge-90.png)

Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.

Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)

*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*

Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)

*Si vous avez besoin d'aide pour la configuration, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Cet appareil accepte l'entrée d'un adaptateur d'alimentation 24 V CC, 1,2 A, fourni dans l'emballage d'origine de cet appareil. Alternativement, il est possible d'utiliser l' injecteur PoE avec la source d'alimentation dans la plage 12-30 V (courant continu) ou le port DC automobile avec la source d'alimentation 12-30 V (courant continu).

**Premiers pas:**

- Dévissez les deux vis et retirez le couvercle;
- Connectez votre câble Internet au port Ethernet (ceci est facultatif si vous utilisez LTE comme connexion principale);
- Insérez la carte SIM dans la fente SIM 2 (au milieu);
- Connectez l'antenne GPS (en option);
- Connectez-vous à la source d'alimentation;
- Définissez la configuration IP de votre ordinateur sur automatique (DHCP);
- De votre ordinateur, connectez-vous au réseau sans fil;
- Ouvrez https://192.168.88.1 dans votre navigateur Web, pour le modèle LtAP Téléchargez l'outil de configuration WinBox [https://mt.lv/winbox](https://mt.lv/winbox), aucune adresse IP par défaut n'est définie, utilisez l'onglet Voisins et connectez-vous via l'adresse MAC;
- Nom d'utilisateur: *admin*, et il n'y a pas de mot de passe;
- Utilisez l'option Vérifier la mise à jour pour mettre à niveau l'appareil vers la dernière version. Vous devez avoir une carte SIM active avec les données disponibles;
- L'appareil va redémarrer;
- Connectez-vous à nouveau et définissez votre pays dans le menu *QuickSet* pour appliquer les paramètres de réglementation du pays;
- Sécurisez votre appareil et définissez un mot de passe fort;
- Les appareils *LtAP* sont livrés sans modem, installez-le avant d'insérer une carte SIM.
- Les packages RouterOS "npk" suivants sont requis pour la fonctionnalité principale du produit: gps, system.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être monté à l'extérieur sur un poteau. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration appropriés ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements FCC, IC et Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v6.49.7 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
Ovaj kratki vodič obuhvaća modele: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*

![](./img/image2020-2-4_17-37-28.badge-90.png)

Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.

Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)

*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*

Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)

*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Ovaj uređaj prihvaća ulaz od 24 V DC, 1,2 A ispravljač struje, koji je isporučen u originalnom pakiranju ovog uređaja. Alternativno, moguće je koristiti PoE injektor zajedno sa izvorom napajanja u rasponu 12-30 V (istosmjerna struja) ili Automotive DC port zajedno s izvorom napajanja 12-30 V (istosmjerna struja).

**Prvi koraci:**

- Odvijte dva vijka i uklonite poklopac;
- Povežite internetski kabel s Ethernet priključkom (to nije obavezno ako koristite LTE kao primarnu vezu);
- Umetnite SIM karticu u utor za SIM 2 (u sredini);
- Spojite GPS antenu (opcija);
- Spojite se na izvor napajanja;
- Postavite IP konfiguraciju vašeg računala na automatsku (DHCP);
- Povežite se s računalom s bežičnom mrežom;
- Otvorite https://192.168.88.1 u svom web pregledniku, za LtAP model. Preuzmite WinBox konfiguracijski alat [https://mt.lv/winbox](https://mt.lv/winbox), nije postavljena zadana IP adresa, koristite karticu Susjedi i povežite se putem MAC adrese;
- Korisničko ime: *admin*, a lozinka nema;
- Upotrijebite mogućnost provjere ažuriranja za nadogradnju uređaja na najnoviju verziju. Morate imati aktivnu SIM karticu s dostupnim podacima;
- Uređaj će se ponovno pokrenuti;
- Ponovo se povežite i u izborniku *QuickSet* postavite svoju zemlju da biste primijenili postavke regulacije zemlje;
- Osigurajte svoj uređaj i postavite jaku lozinku;
- Uređaji *LtAP* dolaze bez modema, instalirajte ga prije nego što umetnete SIM karticu.
- Sljedeći paketi RouterOS "npk" potrebni su za temeljnu funkcionalnost proizvoda: gps, system.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen postavljanju vani na stup. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne poštujete ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju FCC, IC i Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v6.49.7-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
Ez a Gyors útmutató a következő modellekre terjed ki: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*

![](./img/image2020-2-5_9-0-20.badge-90.png)

Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.

Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)

*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*

Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)

*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Ez az eszköz 24 V DC, 1.2 A tápfeszültség adaptert fogad be, amelyet a készülék eredeti csomagolásában talál. Alternatív megoldásként a PoE befecskendező szelep is használható a 12-30 V (egyenáramú) áramforrással vagy az autóipari DC porttal együtt a 12-30 V (egyenáram) áramforrással.

**Első lépések:**

- Csavarja ki két csavart és vegye le a fedelet;
- Csatlakoztassa internetkábelét az Ethernet porthoz (ez opcionális, ha az LTE-t használja elsődleges kapcsolatként);
- Helyezze a SIM-kártyát a SIM 2 nyílásba (középen);
- Csatlakoztassa a GPS antennát (opcionális);
- Csatlakoztassa az áramforrást;
- Állítsa a számítógép IP-konfigurációját automatikusra (DHCP);
- Csatlakoztassa a számítógépet a vezeték nélküli hálózathoz;
- Nyissa meg a https://192.168.88.1 címet a webböngészőjében, LtAP modell esetén Töltse le a WinBox konfigurációs eszközt [https://mt.lv/winbox](https://mt.lv/winbox), nincs alapértelmezett IP-cím beállítva, használja a Neighbors lapot, és csatlakozzon a MAC-címen keresztül;
- Felhasználónév: *admin*, és nincs jelszó;
- Használja a frissítés ellenőrzése lehetőséget az eszköz frissítéséhez a legújabb verzióra. A rendelkezésre álló adatokkal rendelkező aktív SIM-kártyának kell lennie;
- A készülék újraindul;
- Csatlakozzon újra, és a *QuickSet* menüben állítsa be az országot, hogy alkalmazza az országszabályozási beállításokat;
- Rögzítse a készüléket és állítson be egy erős jelszót;
- A *LtAP* készülékek modem nélkül szállíthatók, telepítse a SIM-kártya behelyezése előtt.
- A következő RouterOS "npk" csomagok szükségesek a termék alapvető funkcióihoz: gps, system.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket szabadon, egy oszlopra kell felszerelni. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helytelen hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását okozhatja.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az FCC, IC és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettország, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v6.49.7 o all'ultima versione stabile, per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
Questa Guida rapida copre i modelli: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*

![](./img/image2020-2-5_9-11-13.badge-90.png)

Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.

Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)

*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*

Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)

*Se hai bisogno di aiuto con la configurazione, cerca un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Questo dispositivo accetta l'ingresso di un alimentatore da 24 V CC, 1,2 A, fornito nella confezione originale di questo dispositivo. In alternativa, è possibile utilizzare l' iniettore PoE insieme alla fonte di alimentazione nel range 12-30 V (corrente continua) o la porta DC automobilistica insieme alla fonte di alimentazione 12-30 V (corrente continua).

**Primi passi:**

- Svitare le due viti e rimuovere il coperchio;
- Connetti il ​​tuo cavo Internet alla porta Ethernet (questo è facoltativo se usi LTE come connessione primaria);
- Inserire la carta SIM nello slot SIM 2 (al centro);
- Collegare l'antenna GPS (opzionale);
- Collegare alla fonte di alimentazione;
- Imposta la configurazione IP del tuo computer su automatica (DHCP);
- Dal tuo computer connettiti alla rete wireless;
- Apri https://192.168.88.1 nel tuo browser web, per il modello LtAP Scarica lo strumento di configurazione WinBox [https://mt.lv/winbox](https://mt.lv/winbox), non è impostato alcun indirizzo IP predefinito, utilizza la scheda Neighbors e connettiti tramite l'indirizzo MAC;
- Nome utente: *admin*, e non c'è password;
- Utilizzare l'opzione Controlla aggiornamento per aggiornare il dispositivo all'ultima versione. È necessario disporre di una scheda SIM attiva con i dati disponibili;
- Il dispositivo si riavvierà;
- Connetti di nuovo e nel menu *QuickSet* imposta il tuo Paese, per applicare le impostazioni relative al Paese;
- Proteggi il tuo dispositivo e imposta una password complessa.
- I seguenti pacchetti RouterOS "npk" sono richiesti per le funzionalità principali del prodotto: gps, system.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è progettato per essere montato all'esterno su un'asta. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Se non si utilizza l'hardware e la configurazione corretti o si seguono le procedure corrette, si potrebbero verificare situazioni pericolose per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni FCC, IC e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v6.49.7 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
Þessi fljótlega leiðarvísir nær yfir gerðir: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*

![](./img/image2020-2-5_9-12-32.badge-90.png)

Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.

Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)

*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*

Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)

*Ef þú þarft hjálp við stillingar, vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Þetta tæki tekur við inngangi 24V DC, 1,2 rafmagns millistykki, sem er að finna í upprunalegum umbúðum þessa tækis. Einnig er mögulegt að nota PoE inndælingartæki ásamt aflgjafa á bilinu 12-30 V (jafnstraumur) eða Automotive DC tengi ásamt aflgjafa 12-30 V (jafnstraumur).

**Fyrstu skrefin:**

- Skrúfaðu tvær skrúfur og fjarlægðu hlífina;
- Tengdu netsnúruna þína við Ethernet tengið (þetta er valfrjálst ef þú notar LTE sem aðal tengingu);
- Settu SIM-kortið í SIM 2 raufina (miðja);
- Tengdu GPS loftnet (valfrjálst);
- Tengdu við aflgjafann;
- Stilltu IP stillingu tölvunnar þinnar á sjálfvirka (DHCP);
- Í tölvunni þinni skaltu tengjast þráðlausa netinu;
- Opnaðu https://192.168.88.1 í vafranum þínum, fyrir LtAP líkan Sæktu WinBox stillingartólið [https://mt.lv/winbox](https://mt.lv/winbox), það er ekkert sjálfgefið IP-tala sett, notaðu Nágranna-flipann og tengdu í gegnum MAC vistfangið;
- Notandanafn: *admin*, og það er ekkert lykilorð;
- Notaðu stöðva fyrir uppfærslumöguleika til að uppfæra tækið í nýjustu útgáfuna. Þú verður að hafa virkt SIM-kort með fyrirliggjandi gögnum;
- Tækið mun endurræsa;
- Tengdu aftur og stilltu land þitt í *QuickSet* valmyndinni til að beita stillingum landsreglugerðar;
- Festu tækið þitt og stilltu sterkt lykilorð;
- *LtAP* tækin eru án mótalds, settu það upp áður en SIM-kort er sett í.
- Eftirfarandi RouterOS „npk“ pakkar eru nauðsynlegir fyrir kjarnavirkni vörunnar: gps, system.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvituð um hættuna sem fylgir rafrásum og kynntu þér venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að vera úti á stöng. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar að setja upp. Bilun í að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti valdið hættulegum aðstæðum fyrir fólk og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við FCC, IC og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v6.49.7 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukerens ansvar å følge lokale landsbestemmelser, inkludert drift innen lovlige frekvenskanaler, utgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*

![](./img/image2020-2-5_9-13-45.badge-90.png)

Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.

Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)

*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*

Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)

*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Denne enheten godtar inngangen til 24V DC, 1,2 A strømadapter, som følger med originalemballasjen til denne enheten. Alternativt er det mulig å bruke PoE-injektor sammen med strømkilden i området 12-30 V (likestrøm) eller Automotive DC-port sammen med strømkilden 12-30 V (likestrøm).

**Første steg:**

- Skru ut to skruer og fjern dekselet;
- Koble Internett-kabelen til Ethernet-porten (dette er valgfritt hvis du bruker LTE som den primære tilkoblingen);
- Sett SIM-kortet inn i SIM 2-sporet (midten);
- Koble til GPS-antenne (valgfritt);
- Koble til strømkilden;
- Sett datamaskinens IP-konfigurasjon til automatisk (DHCP);
- Fra datamaskinen din kobler du til det trådløse nettverket;
- Åpne https://192.168.88.1 i nettleseren din, for LtAP-modell Last ned WinBox-konfigurasjonsverktøyet [https://mt.lv/winbox](https://mt.lv/winbox), det er ingen standard IP-adresse satt, bruk Naboer-fanen og koble til via MAC-adressen;
- Brukernavn: *admin*, og det er ikke noe passord;
- Bruk sjekk for oppdateringsalternativ for å oppgradere enheten til den nyeste versjonen. Du må ha et aktivt SIM-kort med tilgjengelige data;
- Enheten vil starte på nytt;
- Koble til igjen og sett inn ditt land i *QuickSet* menyen for å bruke innstillinger for landregulering;
- Sikre enheten din og sett et sterkt passord;
- *LtAP* enheter kommer uten modem, installer den før du setter inn et SIM-kort.
- Følgende RouterOS "npk"-pakker kreves for kjernefunksjonaliteten til produktet: gps, system.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å være montert utendørs på en stolpe. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på systemet.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med FCC, IC og EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v6.49.7“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.
Šis trumpasis vadovas apima modelius: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*

![](./img/image2020-2-5_9-15-30.badge-89.png)

Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.

Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)

*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*

Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)

*Jei jums reikia pagalbos dėl konfigūravimo, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Šis prietaisas priima 24 V DC, 1,2 A maitinimo adapterį, pateiktą originalioje šio prietaiso pakuotėje. Taip pat galima naudoti „ PoE“ purkštuvą kartu su energijos šaltiniu, kurio diapazonas yra 12–30 V (nuolatinė srovė), arba automobilinės nuolatinės srovės prievadą, kartu su 12–30 V (nuolatinės srovės) maitinimo šaltiniu.

**Pirmieji žingsniai:**

- Atsukite du varžtus ir nuimkite dangtį;
- Prijunkite savo interneto kabelį prie Ethernet prievado (tai neprivaloma, jei pagrindiniu ryšiu naudojate LTE);
- Įdėkite SIM kortelę į SIM 2 lizdą (vidurį);
- Prijunkite GPS anteną (pasirinktinai);
- Prijunkite prie maitinimo šaltinio;
- Nustatykite kompiuterio IP konfigūraciją į automatinę (DHCP);
- Iš savo kompiuterio prisijunkite prie belaidžio tinklo;
- Žiniatinklio naršyklėje atidarykite https://192.168.88.1, skirtą LtAP modeliui. Atsisiųskite „WinBox“ konfigūravimo įrankį [https://mt.lv/winbox](https://mt.lv/winbox), nenustatytas numatytasis IP adresas, naudokite skirtuką „Kaimynai“ ir prisijunkite naudodami MAC adresą;
- Vartotojo vardas: *admin*, o slaptažodžio nėra;
- Norėdami atnaujinti įrenginį į naujausią versiją, naudokite atnaujinimo tikrinimo parinktį. Turite turėti aktyvią SIM kortelę su turimais duomenimis;
- Įrenginys bus paleistas iš naujo;
- Vėl prisijunkite ir „ *QuickSet“* meniu nustatykite savo šalį, kad galėtumėte pritaikyti šalies reguliavimo parametrus;
- Apsaugokite savo prietaisą ir nustatykite tvirtą slaptažodį;
- Irenginiai *„LtAP“* pateikiami be modemo, prieš įdėdami SIM kortelę, įdiekite jį.
- Pagrindiniam produkto funkcionalumui reikalingi šie RouterOS „npk“ paketai: gps, lora, sistema.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas skirtas montuoti lauke ant stulpo. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite tinkamos aparatinės įrangos ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka FCC, IC ir Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Brivibas gatve 214i Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v6.49.7 vai jaunāku stabilo versiju, lai nodrošinātu atbilstību vietējās valsts likumdošanai.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijām.
Šī īsā rokasgrāmata aptver modeļus: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*

![](./img/image2020-2-5_9-18-11.badge-90.png)

Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.

Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)

*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*

Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)

*Ja jums nepieciešama palīdzība ar ierīces konfigurēšanu, lūdzu, konsultējieties ar konsultantiem, kontaktinformācija atrodama vietnē [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Šī ierīce darbojas ar 24 V, 1.2 A, līdzstrāvas barošanas adapteri, kas ir pieejams šīs ierīces oriģinālajā iepakojumā. PoE inžektoru kas pievienots līdzstrāvas enerģijas avotam, diapazonā no 12 līdz 30 V, vai transportlīdzekļa līdzstrāvas elektriskajā ķēdē, 12-30 V diapazonā.

**Pirmie soļi:**

- Atskrūvējiet divas skrūves un noņemiet vāku;
- Pievienojiet Interneta kabeli Ethernet portam (tas nav obligāti, ja par primāro savienojumu izmantojat LTE);
- Ievietojiet SIM karti SIM 2 slotā (vidējais);
- Pievienojiet GPS antenu (pēc izvēles);
- Pievienojiet ierīci strāvas avotam;
- Iestatiet datora IP konfigurāciju automātisku (DHCP);
- No datora izveidojiet savienojumu ar bezvadu tīklu;
- Tīmekļa pārlūkprogrammā atveriet https://192.168.88.1, LtAP modelim Lejupielādējiet WinBox konfigurācijas rīku [https://mt.lv/winbox](https://mt.lv/winbox), nav iestatīta noklusējuma IP adrese, izmantojiet cilni Kaimiņi un izveidojiet savienojumu, izmantojot MAC adresi.;
- Lietotājvārds: *admin*, un parole nav uzstādīta;
- Izmantojiet iespēju - pārbaudīt iekārtas programmatūras versiju, lai atjauninātu ierīces programmatūru uz jaunāko versiju. Jums jābūt aktīvai SIM kartei ar pieejamajiem datiem;
- Ierīce tiks restartēta;
- Pievienojieties vēlreiz un izvēlnē *QuickSet* iestatiet savu valsti, lai lietotu valsts regulēšanas iestatījumus;
- Iestatiet drošu paroli, tā tiks izmantota, lai pieteiktos nākamreiz;
- *LtAP* ierīces tiek piegādātas bez modema, pirms SIM kartes ievietošanas ieinstalējiet savu modemu.
- Produkta pamatfunkcionalitātei ir nepieciešamas šādas RouterOS "npk" pakotnes: gps, system.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai ārpus telpām. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Pareiza aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst FCC, IC un Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Brīvības gatve 214i Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v6.49.7 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż it-tħaddim fil-kanali tal-frekwenza legali, l-enerġija tal-ħruġ, ir-rekwiżiti tal-kejbils u r-rekwiżiti tal-Għażla Dinamika tal-Frekwenza (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
Din il-Gwida Quick tkopri mudelli: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*

![](./img/image2020-2-5_9-20-59.badge-90.png)

Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.

Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)

*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*

Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)

*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Dan l-Apparat jaċċetta input ta ’24V DC, 1.2 A adapter tal-enerġija, li huwa pprovdut fl-imballaġġ oriġinali ta’ dan l-apparat. Alternattivament, huwa possibbli li tuża injettur PoE flimkien mas-sors ta 'enerġija fil-firxa 12-30 V (kurrent dirett) jew il-port tal-Karozzi DC flimkien mas-sors ta' enerġija 12-30 V (kurrent dirett).

**L-ewwel passi:**

- Ħoll żewġ viti u neħħi l-għatu;
- Qabbad il-kejbil tal-Internet tiegħek mal-port Ethernet (dan mhux obbligatorju jekk tuża LTE bħala l-konnessjoni primarja);
- Daħħal il-biljett SIM fl-islott SIM 2 (fin-nofs);
- Qabbad antenna GPS (mhux obbligatorja);
- Qabbad mas-sors tal-enerġija;
- Issettja l-konfigurazzjoni IP tal-kompjuter tiegħek għal awtomatika (DHCP);
- Mill-kompjuter tiegħek qabbad man-netwerk bla fili;
- Iftaħ https://192.168.88.1 fil-web browser tiegħek, għall-mudell LtAP Niżżel l-għodda ta’ konfigurazzjoni WinBox [https://mt.lv/winbox](https://mt.lv/winbox), m’hemm l-ebda indirizz IP default stabbilit, uża t-tab Neighbours u qabbad permezz tal-indirizz MAC;
- Isem tal-utent: *admin*, u m'hemm l-ebda password;
- Uża verifika għall-għażla ta 'aġġornament biex taġġorna l-apparat għall-aħħar verżjoni. Irid ikollok SIM card attiva bid-dejta disponibbli;
- L-apparat se jerġa 'jibda;
- Qabbad mill-ġdid u fil- menu *QuickSet* issettja pajjiżek, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Sikura t-tagħmir tiegħek u stabbilixxa password qawwija:
- L- apparat *LtAP* jiġi mingħajr modem, tinstallah qabel ma tiddaħħal SIM card.
- Il-pakketti RouterOS "npk" li ġejjin huma meħtieġa għall-funzjonalità ewlenija tal-prodott: gps, system.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jintrama fuq barra fuq arblu. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Jekk tonqos milli tuża l-hardware u l-konfigurazzjoni korretti jew issegwi l-proċeduri t-tajba tista ’tirriżulta f’sitwazzjoni perikoluża għan-nies u ħsara fis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta 'FCC, IC u l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Brivibas Gve 214i Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v6.49.7 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, waaronder de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
Deze beknopte handleiding behandelt modellen: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*

![](./img/image2020-2-5_9-22-25.badge-90.png)

Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.

Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)

*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*

Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)

*Als je hulp nodig hebt bij het configureren, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Dit apparaat accepteert invoer van 24 V DC, 1,2 A voedingsadapter, die wordt geleverd in de originele verpakking van dit apparaat. Als alternatief is het mogelijk om de PoE-injector samen met de stroombron in het bereik van 12-30 V (gelijkstroom) of Automotive DC-poort samen met de stroombron 12-30 V (gelijkstroom) te gebruiken.

**Eerste stappen:**

- Draai de twee schroeven los en verwijder het deksel;
- Sluit uw internetkabel aan op de Ethernet-poort (dit is optioneel als u LTE als primaire verbinding gebruikt);
- Plaats de simkaart in de sim 2-sleuf (midden);
- Sluit GPS-antenne aan (optioneel);
- Maak verbinding met de stroombron;
- Stel de IP-configuratie van uw computer in op automatisch (DHCP);
- Maak vanaf uw computer verbinding met het draadloze netwerk;
- Open https://192.168.88.1 in uw webbrowser, voor LtAP-model Download de WinBox-configuratietool [https://mt.lv/winbox](https://mt.lv/winbox), er is geen standaard IP-adres ingesteld, gebruik het tabblad Buren en maak verbinding via het MAC-adres;
- Gebruikersnaam: *admin*, en er is geen wachtwoord;
- Gebruik de optie controleren op update om het apparaat te upgraden naar de nieuwste versie. U moet een actieve simkaart hebben met beschikbare gegevens;
- Het apparaat start opnieuw op;
- Maak opnieuw verbinding en stel in het *QuickSet* menu uw land in om de *landregelgevinginstellingen toe* te passen;
- Beveilig uw apparaat en stel een sterk wachtwoord in;
- De *LtAP* apparaten worden zonder modem geleverd, installeer deze voordat u een simkaart plaatst.
- De volgende RouterOS "npk"-pakketten zijn vereist voor de kernfunctionaliteit van het product: gps, system.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om buiten op een paal te worden gemonteerd. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de FCC-, IC- en EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Brivibas gatve 214i Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v6.49.7 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik należy zainstalować zgodnie z instrukcjami.
Niniejszy Krótki przewodnik obejmuje modele: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).

:::

-

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*

![](./img/image2020-2-5_9-39-6.badge-90.png)

Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.

Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)

*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*

Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)

*Jeśli potrzebujesz pomocy w konfiguracji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

To urządzenie akceptuje napięcie wejściowe zasilacza 24 V DC, 1,2 A, który znajduje się w oryginalnym opakowaniu tego urządzenia. Alternatywnie można zastosować wtryskiwacz PoE ze źródłem zasilania w zakresie 12–30 V (prąd stały) lub samochodowy port DC wraz ze źródłem zasilania 12–30 V (prąd stały).

**Pierwsze kroki:**

- Odkręć dwie śruby i zdejmij pokrywę;
- Podłącz kabel internetowy do portu Ethernet (jest to opcjonalne, jeśli używasz LTE jako podstawowego połączenia);
- Włóż kartę SIM do gniazda SIM 2 (środek);
- Podłącz antenę GPS (opcjonalnie);
- Podłącz do źródła zasilania;
- Ustaw konfigurację IP komputera na automatyczną (DHCP);
- Z komputera połącz się z siecią bezprzewodową;
- Otwórz https://192.168.88.1 w przeglądarce internetowej, dla modelu LtAP Pobierz narzędzie konfiguracyjne WinBox [https://mt.lv/winbox](https://mt.lv/winbox), nie ma ustawionego domyślnego adresu IP, użyj zakładki Sąsiedzi i połącz się przez adres MAC;
- Nazwa użytkownika: *admin* i nie ma hasła;
- Użyj opcji Sprawdź dostępność aktualizacji, aby zaktualizować urządzenie do najnowszej wersji. Musisz mieć aktywną kartę SIM z dostępnymi danymi;
- Urządzenie uruchomi się ponownie;
- Połącz ponownie iw menu *QuickSet* ustaw swój kraj, aby zastosować ustawienia przepisów krajowych;
- Zabezpiecz swoje urządzenie i ustaw silne hasło;
- Product *LtAP* jest dostarczany bez modemu, zainstaluj go przed włożeniem karty SIM.
- Następujące pakiety „npk” RouterOS są wymagane do podstawowej funkcjonalności produktu: gps, system.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Produkt przeznaczony jest do montażu na zewnątrz na słupie. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie prawidłowego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie FCC, IC i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Brivibas gatve 214i Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v6.49.7 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
Este Guia rápido abrange os modelos: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*

![](./img/image2020-2-5_9-40-42.badge-90.png)

Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.

Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)

*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*

O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)

*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Este dispositivo aceita a entrada de um adaptador de energia de 24 Vcc, 1,2 A, fornecido na embalagem original deste dispositivo. Como alternativa, é possível usar o injetor PoE em conjunto com a fonte de energia na faixa de 12 a 30 V (corrente contínua) ou a porta CC automotiva, juntamente com a fonte de energia de 12 a 30 V (corrente contínua).

**Primeiros passos:**

- Solte os dois parafusos e remova a tampa;
- Conecte o cabo da Internet à porta Ethernet (isso é opcional se estiver usando LTE como a conexão principal);
- Insira o cartão SIM no slot do SIM 2 (meio);
- Conecte a antena GPS (opcional);
- Conecte-se à fonte de energia;
- Defina a configuração IP do computador como automática (DHCP);
- No seu computador, conecte-se à rede sem fio;
- Abra o https://192.168.88.1 em seu navegador da web, para o modelo LtAP Baixe a ferramenta de configuração do WinBox [https://mt.lv/winbox](https://mt.lv/winbox), não há endereço IP padrão definido, use a guia Vizinhos e conecte-se através do endereço MAC;
- Nome de usuário: *admin* e não há senha;
- Use a opção verificar atualização para atualizar o dispositivo para a versão mais recente. Você deve ter um cartão SIM ativo com os dados disponíveis;
- O dispositivo irá reiniciar;
- Conecte-se novamente e, no menu *QuickSet,* defina seu país, para aplicar as configurações de regulamentação do país;
- Proteja seu dispositivo e defina uma senha forte;
- Os dispositivos *LtAP* vêm sem um modem, instale-o antes de inserir um cartão SIM.
- Os seguintes pacotes "npk" do RouterOS são necessários para a funcionalidade principal do produto: gps, system.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser montado ao ar livre em um poste. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da FCC, IC e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Brivibas gatve 214i Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v6.49.7 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
Acest Ghid rapid acoperă modele: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*

![](./img/image2020-2-5_9-42-33.badge-88.png)

Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.

Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products).

*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*

Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro).

*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Acest dispozitiv acceptă introducerea de 24V DC, 1.2 A adaptor de alimentare, care este prevăzut în ambalajul original al acestui dispozitiv. În mod alternativ, este posibil să utilizați injectorul PoE împreună cu sursa de alimentare în intervalul 12-30 V (curent continuu) sau portul CC automobilist împreună cu sursa de alimentare 12-30 V (curent continuu).

**Primii pasi:**

- Deșurubați două șuruburi și scoateți capacul;
- Conectați cablul de internet la portul Ethernet (este opțional dacă utilizați LTE ca conexiune principală);
- Introduceți cartela SIM în slotul SIM 2 (mijloc);
- Conectați antena GPS (opțional);
- Conectați-vă la sursa de alimentare;
- Setați configurația IP a computerului la automată (DHCP);
- De la computer conectați-vă la rețeaua wireless;
- Deschideți https://192.168.88.1 în browserul dvs. web, pentru modelul LtAP Descărcați instrumentul de configurare WinBox [https://mt.lv/winbox](https://mt.lv/winbox), nu există o adresă IP implicită setată, utilizați fila Vecini și conectați-vă prin adresa MAC;
- Nume utilizator: *admin* și nu există nicio parolă;
- Utilizați opțiunea de verificare pentru actualizare pentru a actualiza dispozitivul la cea mai recentă versiune. Trebuie să aveți o cartelă SIM activă cu datele disponibile;
- Dispozitivul se va reporni;
- Conectați-vă din nou și în meniul *QuickSet* setați țara dvs., pentru a aplica setările de reglementare a țării;
- Asigurați-vă dispozitivul și setați o parolă puternică;
- Dispozitivele *LtAP* vin fără modem, instalează-l înainte de a introduce o cartelă SIM.
- Următoarele pachete RouterOS „npk” sunt necesare pentru funcționalitatea de bază a produsului: gps, system.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie montat în aer liber pe un stâlp. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații FCC, IC și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Brivibas gatve 214i Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v6.49.7 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných užívateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
Táto Stručná príručka sa týka modelov: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*

![](./img/image2020-2-5_9-44-55.badge-90.png)

Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.

Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)

*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*

Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk).

*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Toto zariadenie akceptuje vstup 24 V DC, 1,2 A napájací adaptér, ktorý sa dodáva v pôvodnom balení tohto zariadenia. Alternatívne je možné použiť vstrekovač PoE spolu so zdrojom energie v rozsahu 12-30 V (jednosmerný prúd) alebo automobilovým jednosmerným portom spolu so zdrojom energie 12-30 V (jednosmerný prúd).

**Prvé kroky:**

- Odskrutkujte dve skrutky a odstráňte kryt;
- Pripojte svoj internetový kábel k ethernetovému portu (je to voliteľné, ak používate LTE ako primárne pripojenie);
- Vložte SIM kartu do slotu SIM 2 (uprostred);
- Pripojte anténu GPS (voliteľné);
- Pripojte sa k zdroju napájania;
- Nastavte IP adresu počítača na automatickú (DHCP);
- Z počítača sa pripojte k bezdrôtovej sieti;
- Otvorte https://192.168.88.1 vo svojom webovom prehliadači, pre model LtAP Stiahnite si konfiguračný nástroj WinBox [https://mt.lv/winbox](https://mt.lv/winbox), nie je nastavená žiadna predvolená adresa IP, použite kartu Neighbors a pripojte sa cez MAC adresu;
- Používateľské meno: *admin* a neexistuje žiadne heslo;
- Pomocou možnosti Skontrolovať dostupnosť aktualizujte zariadenie na najnovšiu verziu. Musíte mať aktívnu SIM kartu s dostupnými údajmi;
- Zariadenie sa reštartuje;
- Pripojte sa znova av ponuke *QuickSet* nastavte svoju krajinu, aby ste použili nastavenia regulácie krajiny;
- Zabezpečte svoje zariadenie a nastavte silné heslo;
- *Z* ariadenia *LtAP* dodávajú bez modemu, pred vložením karty SIM ho nainštalujte.
- Nasledujúce balíky RouterOS "npk" sú potrebné pre základnú funkčnosť produktu: gps, system.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na montáž vonku na stĺp. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať podľa správnych postupov, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu FCC, IC a Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Brivibas gatve 214i Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v6.49.7 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so dolžni upoštevati lokalne predpise, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
Ta hitri vodnik zajema modele: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*

![](./img/image2020-2-5_9-46-47.badge-90.png)

Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.

Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)

*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*

Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)

*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Ta naprava sprejme vhod 24V DC, 1,2 A napajalnika, ki je na voljo v originalni embalaži te naprave. Lahko pa uporabite PoE injektor skupaj z virom energije v območju 12-30 V (enosmerni tok) ali avtomobilskim enosmernim priključkom skupaj z virom napajanja 12-30 V (enosmerni tok).

**Prvi koraki:**

- Odvijte dva vijaka in odstranite pokrov;
- Priključite internetni kabel na vrata Ethernet (to je izbirno, če kot primarno povezavo uporabljate LTE);
- Vstavite kartico SIM v režo SIM 2 (na sredini);
- Povežite GPS anteno (neobvezno);
- Priključite se na vir napajanja;
- Nastavite konfiguracijo IP računalnika na samodejno (DHCP);
- Iz računalnika se povežite z brezžičnim omrežjem;
- Odprite https://192.168.88.1 v svojem spletnem brskalniku, za model LtAP Prenesite konfiguracijsko orodje WinBox [https://mt.lv/winbox](https://mt.lv/winbox), privzeti naslov IP ni nastavljen, uporabite zavihek Sosedje in se povežite prek naslova MAC;
- Uporabniško ime: *admin* in ni gesla;
- Uporabite možnost Preveri možnost posodobitve, da napravo nadgradite na najnovejšo različico. Imeti morate aktivno kartico SIM z razpoložljivimi podatki;
- Naprava se bo znova zagnala;
- Ponovno se povežite in v meniju *QuickSet* nastavite svojo državo in uporabite nastavitve ureditve države;
- Zavarujte svojo napravo in nastavite močno geslo;
- Naprave *LtAP* prihajajo brez modema, namestite ga pred vstavitvijo kartice SIM.
- Za osnovno funkcionalnost izdelka so potrebni naslednji paketi RouterOS "npk": gps, system.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen za namestitev na prostem na drog. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba pravilne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju FCC, IC in Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v6.49.7 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*

![](./img/image2020-2-5_9-47-44.badge-90.png)

Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.

Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)

*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*

Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)

*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Denna enhet accepterar ingång från 24V DC, 1,2 A strömadapter, som finns i originalförpackningen på denna enhet. Alternativt är det möjligt att använda PoE-injektor tillsammans med kraftkällan i området 12-30 V (likström) eller Automotive DC-port tillsammans med strömkällan 12-30 V (likström).

**Första stegen:**

- Skruva loss två skruvar och ta bort locket.
- Anslut din Internet-kabel till Ethernet-porten (detta är valfritt om du använder LTE som den primära anslutningen);
- Sätt i SIM-kortet i SIM 2-kortplatsen (mitt);
- Anslut GPS-antenn (valfritt);
- Anslut till strömkällan;
- Ställ in din dators IP-konfiguration på automatisk (DHCP);
- Anslut till det trådlösa nätverket från din dator;
- Öppna https://192.168.88.1 i din webbläsare, för LtAP-modell Ladda ner WinBox-konfigurationsverktyget [https://mt.lv/winbox](https://mt.lv/winbox), det finns ingen standard-IP-adress, använd fliken Grannar och anslut via MAC-adressen;
- Användarnamn: *admin*, och det finns inget lösenord;
- Använd kontrollera för uppdateringsalternativ för att uppgradera enheten till den senaste versionen. Du måste ha ett aktivt SIM-kort med tillgänglig data;
- Enheten startar om;
- Anslut igen och *ställ* in ditt land i *QuickSet* menyn för att tillämpa landsregleringsinställningar;
- Säkra din enhet och ställa in ett starkt lösenord;
- *LtAP* enheter kommer utan modem, installera den innan du sätter i ett SIM-kort.
- Följande RouterOS "npk"-paket krävs för produktens kärnfunktionalitet: gps, system.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att monteras utomhus på en stolpe. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på systemet.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med FCC, IC och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v6.49.7或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
本快速指南涵盖以下型号: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*

![](./img/image2020-2-5_9-49-44.badge-91.png)

请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。

有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)

*该产品最重要的技术规格可在本快速指南的最后一页找到。*

可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)

*如果您需要配置方面的帮助，请寻求顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

本设备接受24V DC，1.2 A电源适配器的输入，该输入在该设备的原始包装中提供。另外，也可以将 PoE注入器与12-30 V（直流）范围内的电源一起使用，或将汽车DC端口与12-30 V（直流电）之间的电源一起使用。

**第一步：**

- 松开两颗螺丝并拆下盖子；
- 将您的Internet电缆连接到以太网端口（如果使用LTE作为主要连接，则这是可选的）；
- 将SIM卡插入SIM 2插槽（中）；
- 连接GPS天线（可选）；
- 连接电源；
- 将您的计算机IP配置设置为自动（DHCP）；
- 从您的计算机连接到无线网络；
- 在网络浏览器中打开 https://192.168.88.1，对于 LtAP 模型下载 WinBox 配置工具 [https://mt.lv/winbox](https://mt.lv/winbox)，没有设置默认 IP 地址，使用邻居选项卡并通过 MAC 地址连接;
- 用户名：*admin*，没有密码；
- 使用检查更新选项将设备升级到最新版本。您必须拥有一个具有可用数据的活动SIM卡；
- 设备将重新启动；
- 再次连接，然后在 *QuickSet* 菜单中设置您的国家/地区，以应用国家/地区法规设置；
- 保护您的设备并设置安全密码;
- *LtAP* 设备不带调制解调器，请在插入SIM卡之前进行安装。
- 产品的核心功能需要以下 RouterOS“npk”包：gps, system。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在户外安装在杆子上。 在开始安装之前，请仔细阅读安装说明。 未能使用正确的硬件和配置或未遵循正确的步骤可能会导致人员受伤和系统损坏。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。

**射频辐射暴露：** 此MikroTik设备符合针对不受控制的环境所设定的FCC，IC和欧盟辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业用户或公众的距离不得超过20厘米。

制造商：Mikrotikls SIA，拉脱维亚Brivibas gatve 214i Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v6.49.7 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

Это краткое руководство охватывает модели: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*

![](./img/image2020-2-5_9-51-14.badge-89.png)

Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.

Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)

*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*

Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)

*Если вам нужна помощь с настройкой, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Это устройство принимает вход 24 В постоянного тока, адаптер питания 1,2 А, который входит в оригинальную упаковку этого устройства. В качестве альтернативы можно использовать инжектор PoE вместе с источником питания в диапазоне 12-30 В (постоянный ток) или автомобильный порт постоянного тока вместе с источником питания 12-30 В (постоянный ток).

**Первые шаги:**

- Откручиваем два винта и снимаем крышку;
- Подключите интернет-кабель к порту Ethernet (это необязательно, если в качестве основного соединения используется LTE);
- Вставьте SIM-карту в слот SIM 2 (посередине);
- Подключить GPS антенну (опционально);
- Подключиться к источнику питания;
- Настройте IP-конфигурацию вашего компьютера на автоматическую (DHCP);
- Со своего компьютера подключитесь к беспроводной сети;
- Откройте https://192.168.88.1 в веб-браузере, для модели LtAP Загрузите инструмент настройки WinBox [https://mt.lv/winbox](https://mt.lv/winbox), IP-адрес по умолчанию не установлен, используйте вкладку «Соседи» и подключитесь через MAC-адрес;
- Имя пользователя: *admin*, и нет пароля;
- Используйте опцию проверки наличия обновлений, чтобы обновить устройство до последней версии. У вас должна быть активная SIM-карта с доступными данными;
- Устройство перезагрузится;
- Подключитесь снова и в меню *QuickSet* установите свою страну, чтобы применить настройки регулирования страны;
- Защитите свое устройство и установите надежный пароль;
- Устройства *LtAP* поставляются без модема, установите его перед установкой SIM-карты.
- Следующие пакеты «npk» RouterOS необходимы для основных функций продукта: gps, system.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать как в помещении, так и на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.
- В домашних условиях этот продукт может вызывать радиопомехи, и в этом случае пользователю может потребоваться принять адекватные меры.

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

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 2400-2483.5 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, Бривибас гатве 214i Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две
последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

![](./img/image2020-1-24_7-55-5.badge-93.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Yкраїнська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v6.49.7 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
Цей короткий посібник стосується моделей: RBLtAP-2HnD (LtAP), RBLtAP-2HnD&R11e-LTE (LtAP LTE kit), RBLtAP-2HnD&R11e-4G (LtAP 4G kit), RBLtAP-2HnD&R11e-LTE6 (LtAP LTE6 kit).
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*

![](./img/image2020-2-5_9-51-14.badge-89.png)

Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.

Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)

*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*

Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)

*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

Цей пристрій приймає вхід 24 В постійного струму, 1,2 А адаптер живлення, який надається в оригінальній упаковці цього пристрою. Крім того, можливо використовувати інжектор PoE разом із джерелом живлення в діапазоні 12-30 В (постійний струм) або автомобільним порту постійного струму разом із джерелом живлення 12-30 В (постійний струм).

**Перші кроки:**

- Викрутіть два гвинта та зніміть кришку;
- Підключіть свій Інтернет-кабель до порту Ethernet (це необов'язково, якщо ви використовуєте LTE в якості основного з'єднання);
- Вставте SIM-карту в слот SIM 2 (посередині);
- Підключіть GPS-антену (додатково);
- Підключення до джерела живлення;
- Встановіть конфігурацію IP вашого комп'ютера на автоматичну (DHCP);
- З комп'ютера підключіться до бездротової мережі;
- Відкрийте https://192.168.88.1 у своєму веб-браузері, для моделі LtAP. Завантажте інструмент конфігурації WinBox [https://mt.lv/winbox](https://mt.lv/winbox), IP-адреса за замовчуванням не встановлена, скористайтеся вкладкою Сусіди та підключіться через MAC-адресу;
- Ім'я користувача: *admin*, і немає пароля;
- Використовуйте опцію перевірки на оновлення, щоб оновити пристрій до останньої версії. Ви повинні мати активну SIM-карту з наявними даними;
- Пристрій перезавантажиться;
- Знову підключіться та в меню *QuickSet* встановіть свою країну, щоб застосувати настройки регулювання країни;
- Захистіть свій пристрій і встановіть надійний пароль;
- Пристрої *LtAP* поставляються без модему, встановіть його перед тим, як вставити SIM-карту.
- Для основної функціональності продукту потрібні такі пакети RouterOS "npk": gps, system.

**Інформація про безпеку:**

- Перш ніж працювати над будь-яким обладнанням MikroTik, пам’ятайте про небезпеки, пов'язані з електричною схемою, та ознайомтеся зі стандартними методами запобігання аварій. Інсталятор повинен бути знайомий з мережевими структурами, термінами та поняттями.
- Використовуйте тільки джерело живлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання повинно встановлюватися кваліфікованим та кваліфікованим персоналом відповідно до цих інструкцій з монтажу. Інсталятор несе відповідальність за те, щоб Установка обладнання відповідала місцевим та національним електричним кодам. Не намагайтеся розбирати, ремонтувати чи змінювати пристрій.
- Цей виріб призначений для монтажу надворі на стовп. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати, що через неправильне використання пристрою не трапляються аварії та пошкодження. Будь ласка, використовуйте цей продукт обережно та працюйте на свій страх і ризик!
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення FCC, IC та Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм).

## Federal Communication Commission Interference Statement

| Model | FCC ID | Contains FCC ID |
| --- | --- | --- |
| RBLtAP-2HnD | TV7LTAP2HND | None |
| RBLtAP-2HnD&R11e-4G | TV7LTAP2HND | TV7R11E4G |
| RBLtAP-2HnD&R11e-LTE6 | TV7LTAP2HND | TV7R11ELTE6 |

![](./img/fcc_logo_ez.badge-80.jpg)
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

| Model | IC | Contains IC |
| --- | --- | --- |
| RBLtAP-2HnD | 7442A-LTAP2HND | None |
| RBLtAP-2HnD&R11e-4G | 7442A-LTAP2HND | 7442A-R11E4G |
| RBLtAP-2HnD&R11e-LTE6 | 7442A-LTAP2HND | 7442A-R11ELTE6 |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## UKCA marking

![](./img/ukca_black_fill.badge-89.gif)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RBLtAP-2HnD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RBLtAP-2HnD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen RBLtAP-2HnD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp RBLtAP-2HnD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός RBLtAP-2HnD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type RBLtAP-2HnD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RBLtAP-2HnD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp RBLtAP-2HnD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RBLtAP-2HnD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type RBLtAP-2HnD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RBLtAP-2HnD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a RBLtAP-2HnD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio RBLtAP-2HnD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að RBLtAP-2HnD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas RBLtAP-2HnD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RBLtAP-2HnD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju RBLtAP-2HnD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur RBLtAP-2HnD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret RBLtAP-2HnD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RBLtAP-2HnD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RBLtAP-2HnD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RBLtAP-2HnD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RBLtAP-2HnD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme RBLtAP-2HnD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RBLtAP-2HnD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products) |

## WLAN / 2G / 3G / LTE

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      WLAN
      2400-2483.5 MHz / 20 dBm
    
  

This MikroTik device meets Maximum WLAN and LTE transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Варианты входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

DC Jack PoE In Ethernet Port Automotive
24 V / 1.2
IP54
-40°..+70°C

\#66938
