# Quick Guide - LtAP LR8 LTE kit

> Models: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit)

**Models: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit)**

![](./img/mt_logo_arrow_v2-02-84.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.10 or the latest stable version, to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

This "LtAP LR8 LTE" series Quick Guide covers models: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-93.png)

This Device accepts input of a 24V DC power adapter, which is provided in the original packaging of this device.

**First steps:**

- Open the bottom lid;
- Insert the SIM card into the SIM 2 slot (middle);
- Connect the device to the power source;
- Connect with your computer to the MikroTik wireless network;
- Open https://192.168.88.1 in your web browser to start the configuration;
- The user name: *admin* and there is no password set, by default;
- Once connected, in the QuickSet LTE AP menu, enter your PIN code https://mt.lv/configuration;
- Upgrade the RouterOS software to the latest version https://mt.lv/upgrade;
- Connect again and in the *QuickSet LTE AP* menu set your wireless network password;
- Choose your country on the left side of the screen, to apply country regulation settings;
- Secure your device and set a strong password;
- Find your *LR Gateway ID* on the label within the product and register it in your Network Server;
- The following RouterOS "npk" packages are required for the core functionality of the product: gps, lora, system.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 30 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

**Note:** For some models, check the user and wireless passwords on the sticker.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.10 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

Това „LtAP LR8 LTE“ серия Бързо ръководство обхваща модели: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-89.png)

Това устройство приема вход на 24V DC адаптер за захранване, който се предлага в оригиналната опаковка на това устройство.

**Първи стъпки:**

- Отворете долния капак;
- Поставете SIM картата в слота за SIM 2 (в средата);
- Свържете устройството към източника на захранване;
- Свържете се с компютъра си към безжичната мрежа MikroTik;
- Отворете https://192.168.88.1 във вашия уеб браузър, за да стартирате конфигурацията;
- Потребителското име: *admin* и по подразбиране няма зададена парола;
- След като се свържете, в менюто QuickSet LTE AP въведете своите PIN https://mt.lv/configuration-bg;
- Надстройте софтуера RouterOS до най-новата версия https://mt.lv/upgrade-bg;
- Свържете се отново и в менюто *QuickSet LTE AP* задайте паролата си за безжична мрежа;
- Изберете вашата страна в лявата част на екрана, за да приложите настройките за регулиране на страната;
- Защитете устройството си и задайте силна парола;
- Намерете своите *LR Gateway ID* на етикета в продукта и го регистрирайте във вашия мрежов сървър;
- Следните RouterOS "npk" пакети са необходими за основната функционалност на продукта: gps, lora, system.

**Информация за безопасност:**

- Преди да работите с което и да е оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да бъде инсталиран на открито. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате правилния хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се изисква да предприеме адекватни мерки.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 30 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

**Забележка:** За някои модели проверете потребителската и безжичната парола на стикера.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.10 nebo na nejnovější stabilní verzi!
Je na koncových uživatelích, aby dodržovali místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
Tato rychlá příručka „LtAP LR8 LTE“ zahrnuje modely: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-89.png)

Toto zařízení přijímá vstup 24 V DC napájecího adaptéru, který je dodáván v původním obalu tohoto zařízení.

**První kroky:**

- Otevřete spodní víko;
- Vložte SIM kartu do slotu pro SIM 2 (uprostřed);
- Připojte zařízení ke zdroji napájení;
- Připojte se k počítači k bezdrátové síti MikroTik;
- Otevřete ve svém webovém prohlížeči https://192.168.88.1 a spusťte konfiguraci;
- Uživatelské jméno: *admin* a ve výchozím nastavení není nastaveno žádné heslo;
- Po připojení v nabídce QuickSet LTE AP zadejte PIN https://mt.lv/configuration-cs;
- Upgradujte software RouterOS na nejnovější verzi https://mt.lv/upgrade-cs;
- Připojte se znovu a v nabídce *QuickSet LTE AP* nastavte heslo bezdrátové sítě;
- Chcete-li použít nastavení regulace země, vyberte svou zemi na levé straně obrazovky;
- Zabezpečte zařízení a nastavte silné heslo;
- Najděte svůj *LR Gateway ID* na štítku v produktu a zaregistrujte jej na síťovém serveru;
- Pro základní funkčnost produktu jsou vyžadovány následující balíčky RouterOS "npk": gps, lora, system.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt lze instalovat venku. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete správný hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobit rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 30 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

**Poznámka:** U některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.10 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-89.png)

Denne enhed accepterer input fra 24V DC-strømadapter, der leveres i denne enheds originale emballage.

**Første trin:**

- Åbn bundlåget;
- Indsæt SIM-kortet i SIM 2-stikket (i midten);
- Tilslut enheden til strømkilden;
- Opret forbindelse til din computer til det trådløse MikroTik-netværk;
- Åbn https://192.168.88.1 i din webbrowser for at starte konfigurationen;
- Brugernavnet: *admin,* og der er ikke angivet et kodeord som standard;
- Når du er oprettet, skal du i menuen QuickSet LTE AP indtaste din PIN https://mt.lv/configuration-da;
- Opgrader RouterOS-softwaren til den nyeste version https://mt.lv/upgrade-da;
- Opret forbindelse igen og indstil din trådløse netværksadgangskode i menuen *QuickSet LTE AP*;
- Vælg dit land på venstre side af skærmen for at anvende indstillinger for landegulering;
- Beskyt din enhed, og indstil en stærk adgangskode;
- Find din *LR Gateway ID* på etiketten i produktet, og registrer den på din netværksserver;
- Følgende RouterOS "npk"-pakker er nødvendige for produktets kernefunktionalitet: gps, lora, system.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt kan installeres udendørs. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den rigtige hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på systemet.
- Vi kan ikke garantere, at der ikke vil forekomme ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 30 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

**Bemærk:** For nogle modeller skal du kontrollere bruger- og trådløs adgangskoder på mærkaten.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.10 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-89.png)

Dieses Gerät akzeptiert den Eingang eines 24-V-Gleichstromadapters, das in der Originalverpackung dieses Geräts enthalten ist.

**Erste Schritte:**

- Öffnen Sie den unteren Deckel;
- Legen Sie die SIM-Karte in den SIM 2-Steckplatz (Mitte) ein;
- Schließen Sie das Gerät an die Stromquelle an;
- Stellen Sie mit Ihrem Computer eine Verbindung zum drahtlosen MikroTik-Netzwerk her;
- Öffnen Sie https://192.168.88.1 in Ihrem Webbrowser, um die Konfiguration zu starten;
- Der Benutzername: *admin* und standardmäßig ist kein Passwort festgelegt;
- Sobald die Verbindung hergestellt ist, geben Sie im Menü QuickSet LTE AP Ihre PIN https://mt.lv/configuration-de;
- Aktualisieren Sie die RouterOS-Software auf die neueste Version https://mt.lv/upgrade-de;
- Stellen Sie erneut eine Verbindung her und legen Sie im Menü *QuickSet LTE AP* Ihr Kennwort für das drahtlose Netzwerk fest;
- Wählen Sie Ihr Land auf der linken Seite des Bildschirms aus, um die Länderregulierungseinstellungen anzuwenden;
- Sichern Sie Ihr Gerät und legen Sie ein sicheres Passwort fest;
- Suchen Sie Ihre *LR Gateway ID* auf dem Etikett im Produkt und registrieren Sie sie auf Ihrem Netzwerkserver;
- Die folgenden RouterOS „npk“-Pakete sind für die Kernfunktionalität des Produkts erforderlich: gps, lora, system.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt kann im Freien installiert werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie nicht die richtige Hardware und Konfiguration verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zu Schäden am System führen.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 30 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

**Notiz:** Überprüfen Sie bei einigen Modellen die Benutzer- und Wireless-Passwörter auf dem Aufkleber.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.10 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
Αυτός ο γρήγορος οδηγός σειράς "LtAP LR8 LTE" καλύπτει μοντέλα: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια σχετικά με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-89.png)

Αυτή η συσκευή δέχεται είσοδο τροφοδοτικού DC 24V, ο οποίος παρέχεται στην αρχική συσκευασία αυτής της συσκευής.

**Πρώτα βήματα:**

- Ανοίξτε το κάτω καπάκι;
- Τοποθετήστε την κάρτα SIM στην υποδοχή SIM 2 (μεσαία);
- Συνδέστε τη συσκευή στην πηγή τροφοδοσίας;
- Συνδεθείτε με τον υπολογιστή σας στο ασύρματο δίκτυο MikroTik;
- Ανοίξτε το https://192.168.88.1 στο πρόγραμμα περιήγησής σας για να ξεκινήσετε τη διαμόρφωση;
- Το όνομα χρήστη: *admin* και δεν έχει οριστεί κωδικός πρόσβασης, από προεπιλογή;
- Μόλις συνδεθείτε, στο μενού QuickSet LTE AP, εισαγάγετε το PIN https://mt.lv/configuration-el;
- Αναβαθμίστε το λογισμικό RouterOS στην πιο πρόσφατη έκδοση https://mt.lv/upgrade-el;
- Συνδεθείτε ξανά και στο μενού *QuickSet LTE AP* ορίστε τον κωδικό πρόσβασης ασύρματου δικτύου;
- Επιλέξτε τη χώρα σας στην αριστερή πλευρά της οθόνης, για να εφαρμόσετε ρυθμίσεις ρύθμισης χώρας;
- Ασφαλίστε τη συσκευή σας και ορίστε έναν ισχυρό κωδικό πρόσβασης;
- Βρείτε τα *LR Gateway ID* σας στην ετικέτα μέσα στο προϊόν και καταχωρίστε το στον διακομιστή δικτύου σας;
- Τα ακόλουθα πακέτα RouterOS "npk" απαιτούνται για τη βασική λειτουργικότητα του προϊόντος: gps, lora, system.

**Πληροφορίες ασφάλειας:**

- Προτού εργαστείτε σε οποιονδήποτε εξοπλισμό MikroTik, προσέξτε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο το τροφοδοτικό και τα αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για να βεβαιωθεί ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κωδικούς. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν μπορεί να εγκατασταθεί σε εξωτερικούς χώρους. Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η μη χρήση του σωστού υλικού και της διαμόρφωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και ζημιά στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο γρηγορότερος τρόπος για να το κάνετε είναι αποσυνδέοντας το τροφοδοτικό από την πρίζα.
- Αυτό είναι προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει ραδιοπαρεμβολές, οπότε ο χρήστης ενδέχεται να υποχρεωθεί να λάβει επαρκή μέτρα.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 30 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

**Σημείωση:** Για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματης σύνδεσης στο αυτοκόλλητο.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.10 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-90.png)

Este dispositivo acepta la entrada del adaptador de alimentación de 24 V CC, que se proporciona en el embalaje original de este dispositivo.

**Primeros pasos:**

- Abra la tapa inferior;
- Inserte la tarjeta SIM en la ranura SIM 2 (centro);
- Conecte el dispositivo a la fuente de alimentación;
- Conéctese con su computadora a la red inalámbrica MikroTik;
- Abra https://192.168.88.1 en su navegador web para iniciar la configuración;
- El nombre de usuario: *admin* y no hay una contraseña establecida, por defecto;
- Una vez conectado, en el menú QuickSet LTE AP, ingrese su PIN https://mt.lv/configuration-es;
- Actualice el software RouterOS a la última versión https://mt.lv/upgrade-es;
- Conéctese nuevamente y en el menú *QuickSet LTE AP* configure su contraseña de red inalámbrica;
- Elija su país en el lado izquierdo de la pantalla, para aplicar la configuración de la regulación del país;
- Asegure su dispositivo y establezca una contraseña segura;
- Busque su *LR Gateway ID* en la etiqueta dentro del producto y regístrelo en su servidor de red;
- Se requieren los siguientes paquetes "npk" de RouterOS para la funcionalidad principal del producto: gps, lora, system.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desarmar, reparar o modificar el dispositivo.
- Este producto se puede instalar en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no utiliza el hardware y la configuración correctos o no sigue los procedimientos correctos, podría provocar una situación peligrosa para las personas y dañar el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Este es un producto de clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 30 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Nota:** Para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, protocolo 802.adminb/g/n con antena PCB incorporada, ganancia máxima de 2 dBi.

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

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
See "LtAP LR8 LTE" seeria lühijuhend hõlmab mudeleid: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*Kui vajate konfigureerimisel abi, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-89.png)

See seade aktsepteerib 24 V alalisvoolu adapteri sisendit, mis on esitatud selle seadme originaalpakendis.

**Esimesed sammud:**

- Avage alumine kaas;
- Sisestage SIM-kaart SIM 2 pesasse (keskel);
- Ühendage seade toiteallikaga;
- Ühendage oma arvutiga MikroTik traadita võrku;
- Seadistamise alustamiseks avage oma veebibrauseris aadress https://192.168.88.1;
- Kasutajanimi: *admin* ja vaikimisi pole parooli määratud;
- Pärast ühenduse loomist sisestage menüüs QuickSet LTE AP oma PIN https://mt.lv/configuration-et;
- Uuendage RouterOS tarkvara uusimale versioonile https://mt.lv/upgrade-et;
- Ühendage uuesti ja määrake menüüs *QuickSet LTE AP* oma traadita võrgu parool;
- Riigi reguleerimise sätete rakendamiseks valige ekraani vasakust servast oma riik;
- Kindlustage oma seade ja määrake kindel parool;
- Leidke oma *LR Gateway ID* toote tootesildilt ja registreerige see oma võrguserveris;
- Toote põhifunktsioonide jaoks on vajalikud järgmised RouterOS-i "npk" paketid: gps, lora, system.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- Seda toodet saab paigaldada välistingimustes. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Õige riistvara ja konfiguratsiooni kasutamata jätmine või õigete protseduuride mittejärgimine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 30 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

**Märge:** Mõne mudeli puhul kontrollige kleebis olevaid kasutaja- ja traadita ühenduse paroole.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.10 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
Tämä "LtAP LR8 LTE" -sarjan pikaopas kattaa mallit: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*Jos tarvitset ohjeita konfiguroinnissa, kysy neuvoa- antajalta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-89.png)

Tämä laite hyväksyy 24 V DC -virtasovittimen tulon, joka toimitetaan laitteen alkuperäispakkauksessa.

**Ensiaskeleet:**

- Avaa pohjakansi;
- Aseta SIM-kortti SIM 2 -paikkaan (keskelle);
- Liitä laite virtalähteeseen;
- Muodosta yhteys tietokoneeseesi langattomaan MikroTik-verkkoon;
- Aloita määritys avaamalla selaimessasi https://192.168.88.1;
- Käyttäjänimi: *admin* eikä salasanaa ole asetettu oletuksena;
- Kun yhteys on muodostettu, kirjoita QuickSet LTE AP-valikossa PIN https://mt.lv/configuration-fi;
- Päivitä RouterOS-ohjelmisto uusimpaan versioon https://mt.lv/upgrade-fi;
- Muodosta yhteys uudelleen ja aseta *QuickSet LTE AP-* valikossa langattoman verkon salasana;
- Valitse maa ruudun vasemmasta reunasta, jotta voit käyttää maan sääntelyasetuksia;
- Suojaa laitteesi ja aseta vahva salasana;
- Löydä *LR Gateway ID-* tuotteesi tuotteen etiketistä ja rekisteröi se verkkopalvelimellesi;
- Tuotteen ydintoimintoihin tarvitaan seuraavat RouterOS "npk" -paketit: gps, lora, system.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote voidaan asentaa ulkona. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 30 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

**Merkintä:** Joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.10 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-89.png)

Cet appareil accepte l'entrée d'un adaptateur d'alimentation 24 V CC, fourni dans l'emballage d'origine de cet appareil.

**Premiers pas:**

- Ouvrez le couvercle inférieur.
- Insérez la carte SIM dans la fente SIM 2 (au milieu);
- Connectez l'appareil à la source d'alimentation;
- Connectez-vous avec votre ordinateur au réseau sans fil MikroTik;
- Ouvrez https://192.168.88.1 dans votre navigateur Web pour démarrer la configuration;
- Le nom d'utilisateur: *admin* et aucun mot de passe n'est défini, par défaut;
- Une fois connecté, dans le menu QuickSet LTE AP, entrez votre PIN https://mt.lv/configuration-fr;
- Mettez à niveau le logiciel RouterOS vers la dernière version https://mt.lv/upgrade-fr;
- Connectez-vous à nouveau et dans le menu *QuickSet LTE AP*, définissez votre mot de passe de réseau sans fil;
- Choisissez votre pays sur le côté gauche de l'écran pour appliquer les paramètres de réglementation du pays;
- Sécurisez votre appareil et définissez un mot de passe fort;
- Trouvez votre *LR Gateway ID* sur l'étiquette du produit et enregistrez-le sur votre serveur réseau;
- Les packages RouterOS "npk" suivants sont requis pour la fonctionnalité principale du produit: gps, lora, system.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit peut être installé à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration appropriés ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 30 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

**Noter:** Pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.10 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
Ovaj kratki vodič serije "LtAP LR8 LTE" obuhvaća modele: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-89.png)

Ovaj uređaj prihvaća ulaz 24-strujnog mrežnog adaptera, koji je isporučen u originalnom pakiranju ovog uređaja.

**Prvi koraci:**

- Otvorite donji poklopac;
- Umetnite SIM karticu u utor za SIM 2 (srednji);
- Spojite uređaj na izvor napajanja;
- Povežite se s računalom na bežičnu mrežu MikroTik;
- Otvorite https://192.168.88.1 u svom web pregledniku da biste započeli konfiguraciju;
- Korisničko ime: *admin* i nije postavljena lozinka, prema zadanim postavkama;
- Nakon povezivanja, u izbornik QuickSet LTE AP unesite PIN https://mt.lv/configuration-hr;
- Nadogradite softver RouterOS na najnoviju verziju https://mt.lv/upgrade-hr;
- Ponovno se povežite i u izborniku *QuickSet LTE AP* postavite lozinku za bežičnu mrežu;
- Odaberite zemlju na lijevoj strani zaslona kako biste primijenili postavke regulacije zemlje;
- Osigurajte svoj uređaj i postavite jaku lozinku;
- Pronađite svoju *LR Gateway ID* na naljepnici u proizvodu i registrirajte je na mrežnom poslužitelju;
- Sljedeći paketi RouterOS "npk" potrebni su za temeljnu funkcionalnost proizvoda: gps, lora, system.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj se proizvod može instalirati na otvorenom. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne poštujete ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 30 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

**Bilješka:** Za neke modele provjerite korisničku i bežičnu lozinku na naljepnici.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.10-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
Ez a "LtAP LR8 LTE" sorozat Gyors útmutató a következő modellekre terjed ki: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-89.png)

Ez az eszköz elfogadja a 24 V-os egyenáramú adapter bemeneti adatait, amely a készülék eredeti csomagolásában található.

**Első lépések:**

- Nyissa ki az alsó fedelet;
- Helyezze be a SIM-kártyát a SIM 2 nyílásba (középen);
- Csatlakoztassa a készüléket az áramforráshoz;
- Csatlakozzon számítógépével a MikroTik vezeték nélküli hálózathoz;
- Nyissa meg a https://192.168.88.1 böngészőt a konfiguráció megkezdéséhez;
- A felhasználónév: *admin,* és alapértelmezés szerint nincs beállítva jelszó;
- Miután csatlakozott, a QuickSet LTE AP menüben írja be a PIN https://mt.lv/configuration-hu;
- Frissítse a RouterOS szoftvert a legújabb verzióra: https://mt.lv/upgrade-hu;
- Csatlakozzon újra, és a *QuickSet LTE AP* menüben állítsa be a vezeték nélküli hálózati jelszót;
- Válassza ki az országot a képernyő bal oldalán az országszabályozási beállítások alkalmazásához;
- Biztonságos készülékét és erős jelszót állítson be;
- Keresse meg *LR Gateway ID* -es számát a termék címkéjén, és regisztrálja a hálózati szerveren;
- A következő RouterOS "npk" csomagok szükségesek a termék alapvető funkcióihoz: gps, lora, system.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik készüléken dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ez a termék kültéren is telepíthető. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helytelen hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását okozhatja.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, amely esetben a felhasználót fel kell kérni a megfelelő intézkedések megtételére.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 30 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

**Jegyzet:** Egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.10 o all'ultima versione stabile, per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento all'interno dei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, cerca un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-89.png)

Questo dispositivo accetta l'ingresso dell'alimentatore 24 V CC, fornito nella confezione originale di questo dispositivo.

**Primi passi:**

- Apri il coperchio inferiore;
- Inserire la scheda SIM nello slot SIM 2 (centrale);
- Collegare il dispositivo alla fonte di alimentazione;
- Connettiti con il tuo computer alla rete wireless MikroTik;
- Apri https://192.168.88.1 nel tuo browser web per avviare la configurazione;
- Il nome utente: *admin* e non è impostata alcuna password per impostazione predefinita;
- Una volta connesso, nel menu QuickSet LTE AP, inserisci il tuo PIN https://mt.lv/configuration-it;
- Aggiorna il software RouterOS all'ultima versione https://mt.lv/upgrade-it;
- Connettiti di nuovo e nel menu *QuickSet LTE AP* imposta la password della rete wireless;
- Scegli il tuo paese sul lato sinistro dello schermo, per applicare le impostazioni relative alle normative nazionali;
- Proteggi il tuo dispositivo e imposta una password complessa;
- Trova il tuo *LR Gateway ID* sull'etichetta all'interno del prodotto e registralo nel tuo server di rete;
- I seguenti pacchetti RouterOS "npk" sono richiesti per le funzionalità principali del prodotto: gps, lora, system.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto può essere installato all'aperto. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Se non si utilizza l'hardware e la configurazione corretti o non si seguono le procedure corrette, si potrebbero verificare situazioni pericolose per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 30 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

**Nota:** Per alcuni modelli, controlla le password utente e wireless sull'adesivo.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.10 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
Þessi „LtAP LR8 LTE“ röð flýtileiðbeiningar ná yfir gerðir: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*Ef þú þarft hjálp við stillingar, vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-89.png)

Þetta tæki tekur við inngangi 24V DC rafmagns millistykki sem er að finna í upprunalegum umbúðum þessa tækis.

**Fyrstu skrefin:**

- Opnaðu botnlokið;
- Settu SIM-kortið í SIM 2 raufina (miðju);
- Tengdu tækið við aflgjafa;
- Tengdu tölvuna þína við MikroTik þráðlaust net;
- Opnaðu https://192.168.88.1 í vafranum þínum til að hefja stillingarnar;
- Notandanafnið: *admin* og það er ekkert lykilorð stillt, sjálfgefið;
- Þegar þú hefur tengst, skaltu slá inn PIN https://mt.lv/configuration-is í QuickSet LTE AP valmyndinni;
- Uppfærðu RouterOS hugbúnaðinn í nýjustu útgáfuna https://mt.lv/upgrade-is;
- Tengdu aftur og stilltu lykilorð þráðlausa símans í *QuickSet LTE AP* valmyndinni;
- Veldu land þitt vinstra megin á skjánum til að beita stillingum landsreglugerðar;
- Tryggðu tækið þitt og settu sterkt lykilorð;
- Finndu *LR Gateway ID* á merkimiðanum innan vörunnar og skráðu þá á netþjóninn þinn;
- Eftirfarandi RouterOS „npk“ pakkar eru nauðsynlegir fyrir kjarnavirkni vörunnar: gps, lora, system.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Hægt er að setja þessa vöru utandyra. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Bilun í að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti valdið hættulegum aðstæðum fyrir fólk og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 30 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

**Athugið:** Athugaðu notanda- og þráðlausa lykilorðin á límmiðanum fyrir sumar gerðir.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.10 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukerens ansvar å følge lokale landsbestemmelser, inkludert drift innen lovlige frekvenskanaler, utgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-89.png)

Denne enheten godtar inngangen til 24V DC-strømadapter, som følger med originalemballasjen til denne enheten.

**Første steg:**

- Åpne bunndekselet;
- Sett inn SIM-kortet i SIM 2-sporet (i midten);
- Koble enheten til strømkilden;
- Koble til datamaskinen til det trådløse MikroTik-nettverket;
- Åpne https://192.168.88.1 i nettleseren din for å starte konfigurasjonen;
- Brukernavnet: *admin* og det er ikke angitt noe passord som standard;
- Når du er tilkoblet, i QuickSet LTE AP-menyen, skriv inn PIN https://mt.lv/configuration-no;
- Oppgrader RouterOS-programvaren til den nyeste versjonen https://mt.lv/upgrade-no;
- Koble til igjen, og angi passordet for det trådløse nettverket i *QuickSet LTE AP-* menyen;
- Velg ditt land på venstre side av skjermen for å bruke innstillinger for landsregulering;
- Sikre enheten og angi et sterkt passord;
- Finn dine *LR Gateway ID* på etiketten i produktet og registrer den på nettverksserveren;
- Følgende RouterOS "npk"-pakker kreves for kjernefunksjonaliteten til produktet: gps, lora, system.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet kan installeres utendørs. Les monteringsanvisningene nøye før installasjonen begynner. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på systemet.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 30 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

**Merk:** For noen modeller, sjekk bruker- og trådløse passord på klistremerket.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.10“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.
Šis „LtAP LR8 LTE“ serijos trumpasis vadovas apima modelius: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*Jei jums reikia pagalbos dėl konfigūravimo, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-88.png)

Šis įrenginys priima 24 V nuolatinės srovės maitinimo adapterį, pateiktą originalioje šio prietaiso pakuotėje.

**Pirmieji žingsniai:**

- Atidarykite apatinį dangtį;
- Įdėkite SIM kortelę į SIM 2 angą (viduryje);
- Prijunkite prietaisą prie maitinimo šaltinio;
- Prisijunkite prie savo kompiuterio prie „MikroTik“ belaidžio tinklo;
- Norėdami pradėti konfigūraciją, savo interneto naršyklėje atidarykite https://192.168.88.1;
- Vartotojo vardas: *admin* ir pagal nutylėjimą nenustatytas slaptažodis;
- Prisijungę, QuickSet LTE AP meniu įveskite PIN https://mt.lv/configuration-lt;
- Atnaujinkite „RouterOS“ programinę įrangą į naujausią versiją https://mt.lv/upgrade-lt;
- Prisijunkite dar kartą ir meniu *QuickSet LTE AP* nustatykite belaidžio tinklo slaptažodį;
- Norėdami pritaikyti šalies reguliavimo parametrus, kairėje ekrano pusėje pasirinkite savo šalį;
- Apsaugokite savo įrenginį ir nustatykite tvirtą slaptažodį;
- Produkto etiketėje suraskite savo *LR Gateway ID* ir užregistruokite jį savo tinklo serveryje;
- Pagrindiniam produkto funkcionalumui reikalingi šie RouterOS „npk“ paketai: gps, lora, sistema.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šį gaminį galima montuoti lauke. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite tinkamos aparatinės įrangos ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 30 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

**Pastaba:** Kai kuriuose modeliuose patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.10 stabilo vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijai.
Šī īsā rokasgrāmata paredzēta modeļiem: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*Ja jums nepieciešama palīdzība ar konfigurēšanu, lūdzu, konsultējieties vietnē [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-89.png)

Šī ierīce darbojas ar 24 V līdzstrāvas barošanas adapteri, kas atrodas šīs ierīces oriģinālajā iepakojumā.

**Pirmie soļi:**

- Atveriet apakšējo vāku;
- Ievietojiet SIM karti SIM 2 slotā (vidū);
- Pievienojiet ierīci strāvas avotam;
- Savienojiet savu datoru ar MikroTik bezvadu tīklu;
- Lai sāktu konfigurēšanu, savā tīmekļa pārlūkprogrammā atveriet vietni https://192.168.88.1;
- Lietotājvārds: *admin* un pēc noklusējuma parole nav iestatīta;
- Kad esat izveidojis savienojumu, izvēlnē QuickSet LTE AP ievadiet PIN https://mt.lv/configuration-lv;
- Atjauniniet RouterOS programmatūru uz jaunāko versiju https://mt.lv/upgrade-lv;
- Savienojieties vēlreiz un izvēlnē *QuickSet LTE AP* iestatiet bezvadu tīkla paroli;
- Lai lietotu valsts noteiktos iestatījumus, ekrāna kreisajā pusē izvēlieties savu valsti;
- Iestatiet spēcīgu paroli ierīces lietotājam, zemāk;
- Atrodiet savu *LR Gateway ID* uz produkta etiķetes un reģistrējiet to tīkla serverī;
- Produkta pamatfunkcionalitātei ir nepieciešamas šādas RouterOS "npk" pakotnes: gps, lora, system.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar nelaimes gadījumu novēršanas standarta praksi. Uzstādītājam ir jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šo produktu var uzstādīt ārpus telpām. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Pareiza aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 30 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

**Piezīme:** Attiecīgiem modeļiem, uz korpusa uzlīmes pārbaudiet lietotāja un bezvadu tīkla paroles.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.10 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż operazzjoni fi ħdan kanali tal-frekwenza legali, qawwa tal-ħruġ, rekwiżiti tal-kejbils u rekwiżiti tal-Għażla tal-Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
Din is-serje "LtAP LR8 LTE" Gwida ta 'malajr tkopri mudelli: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).

:::

-

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-89.png)

Dan l-Apparat jaċċetta input ta ’24V DC adapter power, li huwa pprovdut fl-imballaġġ oriġinali ta’ dan l-apparat.

**L-ewwel passi:**

- Iftaħ l-għatu tal-qiegħ;
- Daħħal is-SIM card fl-islott SIM 2 (fin-nofs);
- Qabbad l-apparat mas-sors tal-enerġija;
- Qabbad mal-kompjuter tiegħek man-netwerk wireless MikroTik;
- Iftaħ https://192.168.88.1 fil-web browser tiegħek biex tibda l-konfigurazzjoni;
- L-isem tal-utent: *admin* u m'hemm l-ebda password issettjata, awtomatikament;
- Ladarba konness, fit-QuickSet LTE AP menu, daħħal it-PIN https://mt.lv/configuration-mt; tiegħek;
- Aġġorna s-softwer RouterOS għall-aħħar verżjoni https://mt.lv/upgrade-mt;
- Qabbad mill-ġdid u fil- menu *QuickSet LTE AP* issettja l-password tan-netwerk wireless tiegħek;
- Agħżel il-pajjiż tiegħek fuq in-naħa tax-xellug tal-iskrin, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Sigura t-tagħmir tiegħek u ssettja password qawwija;
- Sib is- *LR Gateway ID* tiegħek fuq it-tikketta fil-prodott u rreġistraha fin-Network Server tiegħek;
- Il-pakketti RouterOS "npk" li ġejjin huma meħtieġa għall-funzjonalità ewlenija tal-prodott: gps, lora, system.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott jista 'jiġi installat barra. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Jekk tonqos milli tuża l-hardware u l-konfigurazzjoni korretti jew issegwi l-proċeduri t-tajba tista ’tirriżulta f’sitwazzjoni perikoluża għan-nies u ħsara fis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 30 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

**Nota:** Għal xi mudelli, iċċekkja l-utent u l-passwords mingħajr fili fuq l-istiker.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.10 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, inclusief de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*Als je hulp nodig hebt bij het configureren, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-89.png)

Dit apparaat accepteert invoer van een 24V DC-voedingsadapter, die wordt geleverd in de originele verpakking van dit apparaat.

**Eerste stappen:**

- Open het onderste deksel;
- Plaats de simkaart in de SIM 2-sleuf (midden);
- Sluit het apparaat aan op de voedingsbron;
- Maak verbinding met uw computer met het draadloze MikroTik-netwerk;
- Open https://192.168.88.1 in uw webbrowser om de configuratie te starten;
- De gebruikersnaam: *admin* en er is standaard geen wachtwoord ingesteld;
- Eenmaal verbonden, voert u in het menu QuickSet LTE AP uw PIN https://mt.lv/configuration-nl;
- Upgrade de RouterOS-software naar de nieuwste versie https://mt.lv/upgrade-nl;
- Maak opnieuw verbinding en stel in het menu *QuickSet LTE AP* uw draadloze netwerkwachtwoord in;
- Kies uw land aan de linkerkant van het scherm om de landregelgeving toe te passen;
- Beveilig uw apparaat en stel een sterk wachtwoord in;
- Zoek uw *LR Gateway ID* op het label in het product en registreer deze op uw netwerkserver;
- De volgende RouterOS "npk"-pakketten zijn vereist voor de kernfunctionaliteit van het product: gps, lora, system.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product kan buitenshuis worden geïnstalleerd. Lees de montage-instructies zorgvuldig voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.
- Dit is een Klasse A-product. In een huiselijke omgeving kan dit product radio-interferentie veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen dient te nemen.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 30 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

**Opmerking:** Controleer bij sommige modellen de gebruikers- en draadloze wachtwoorden op de sticker.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.10 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik należy zainstalować zgodnie z instrukcjami.
Niniejsza skrócona instrukcja „LtAP LR8 LTE” obejmuje modele: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy w konfiguracji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-89.png)

To urządzenie akceptuje wejście zasilacza 24 V DC, który jest dostarczany w oryginalnym opakowaniu tego urządzenia.

**Pierwsze kroki:**

- Otwórz dolną pokrywę;
- Włóż kartę SIM do gniazda SIM 2 (środkowe);
- Podłącz urządzenie do źródła zasilania;
- Połącz się ze swoim komputerem z siecią bezprzewodową MikroTik;
- Otwórz https://192.168.88.1 w swojej przeglądarce internetowej, aby rozpocząć konfigurację;
- Nazwa użytkownika: *admin* i domyślnie nie ma hasła;
- Po nawiązaniu połączenia w QuickSet LTE AP menu wprowadź PIN https://mt.lv/configuration-pl;
- Zaktualizuj oprogramowanie RouterOS do najnowszej wersji https://mt.lv/upgrade-pl;
- Połącz ponownie iw menu *QuickSet LTE AP* ustaw hasło sieci bezprzewodowej;
- Wybierz swój kraj po lewej stronie ekranu, aby zastosować ustawienia przepisów krajowych;
- Zabezpiecz swoje urządzenie i ustaw silne hasło;
- Znajdź swój *LR Gateway ID* na etykiecie produktu i zarejestruj go na serwerze sieciowym.
- Następujące pakiety „npk” RouterOS są wymagane do podstawowej funkcjonalności produktu: gps, lora, system.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt można zainstalować na zewnątrz. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie prawidłowego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe. W takim przypadku użytkownik może zostać zobowiązany do podjęcia odpowiednich kroków.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 30 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

**Opmerking:** W przypadku niektórych modeli sprawdź hasło użytkownika i hasło do sieci bezprzewodowej na naklejce.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.10 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
Este guia rápido da série "LtAP LR8 LTE" abrange os modelos: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-89.png)

Este dispositivo aceita a entrada do adaptador de energia de 24 Vcc, fornecido na embalagem original deste dispositivo.

**Primeiros passos:**

- Abra a tampa inferior;
- Insira o cartão SIM no slot SIM 2 (meio);
- Conecte o dispositivo à fonte de alimentação;
- Conecte seu computador à rede wireless MikroTik;
- Abra https://192.168.88.1 em seu navegador para iniciar a configuração;
- O nome de usuário: *admin* e não há senha definida, por padrão;
- Uma vez conectado, no menu QuickSet LTE AP, digite PIN https://mt.lv/configuration-pt;
- Atualize o software RouterOS para a versão mais recente https://mt.lv/upgrade-pt;
- Conecte-se novamente e no menu *QuickSet LTE AP* defina sua senha de rede sem fio;
- Escolha seu país no lado esquerdo da tela para aplicar as configurações de regulamentação do país;
- Proteja seu dispositivo e defina uma senha forte;
- Encontre seu *LR Gateway ID* na etiqueta do produto e registre-o no servidor de rede;
- Os seguintes pacotes "npk" do RouterOS são necessários para a funcionalidade principal do produto: gps, lora, system.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e familiarize-se com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto pode ser instalado ao ar livre. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 30 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

**Nota:** Para alguns modelos, verifique as senhas de usuário e sem fio no adesivo.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.10 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
Acest Ghid rapid seria "LtAP LR8 LTE" acoperă modele: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-87.png)

Acest dispozitiv acceptă introducerea adaptorului de curent continuu de 24V DC, care este prevăzut în ambalajul original al acestui dispozitiv.

**Primii pasi:**

- Deschideți capacul inferior;
- Introduceți cartela SIM în slotul SIM 2 (mijloc);
- Conectați dispozitivul la sursa de alimentare;
- Conectați-vă cu computerul la rețeaua fără fir MikroTik;
- Deschideți https://192.168.88.1 în browserul dvs. web pentru a începe configurarea;
- Numele de utilizator: *admin* și nu există nici o parolă setată, în mod implicit;
- Odată conectat, în meniul QuickSet LTE AP, introduceți PIN https://mt.lv/configuration-ro;
- Actualizați software-ul RouterOS la cea mai recentă versiune https://mt.lv/upgrade-ro;
- Conectați-vă din nou și în meniul *QuickSet LTE AP* setați parola rețelei fără fir;
- Alegeți țara dvs. în partea stângă a ecranului, pentru a aplica setările de reglementare a țării;
- Asigurați-vă dispozitivul și setați o parolă puternică;
- Găsiți-vă *LR Gateway ID* pe etichetă în produs și înregistrați-l în serverul de rețea;
- Următoarele pachete RouterOS „npk” sunt necesare pentru funcționalitatea de bază a produsului: gps, lora, system.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs poate fi instalat în aer liber. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 30 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Notă:** Pentru unele modele, verificați parolele de utilizator și wireless pe autocolant.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.10 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných používateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
Táto príručka „LtAP LR8 LTE“ zahŕňa modely: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-89.png)

Toto zariadenie prijíma vstup 24V DC napájacieho adaptéra, ktorý je súčasťou originálneho balenia tohto zariadenia.

**Prvé kroky:**

- Otvorte spodné viečko;
- Vložte SIM kartu do zásuvky SIM 2 (v strede);
- Pripojte zariadenie k zdroju napájania;
- Pripojte sa k počítaču k bezdrôtovej sieti MikroTik;
- Otvorte vo svojom webovom prehliadači https://192.168.88.1 a konfigurácia sa spustí;
- Používateľské meno: *admin* a predvolene nie je nastavené žiadne heslo;
- Po pripojení zadajte v ponuke QuickSet LTE AP svojich PIN https://mt.lv/configuration-sk;
- Aktualizujte softvér RouterOS na najnovšiu verziu https://mt.lv/upgrade-sk;
- Znova sa pripojte a v ponuke *QuickSet LTE AP* nastavte heslo bezdrôtovej siete;
- Ak chcete použiť nastavenia regulácie krajiny, vyberte svoju krajinu na ľavej strane obrazovky;
- Zabezpečte svoje zariadenie a nastavte silné heslo;
- Nájdite svojich *LR Gateway ID* na štítku v rámci produktu a zaregistrujte ich na svojom sieťovom serveri;
- Nasledujúce balíky RouterOS "npk" sú potrebné pre základnú funkčnosť produktu: gps, lora, system.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je možné nainštalovať vonku. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať podľa správnych postupov, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 30 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

**Poznámka:** Pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslá na nálepke.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.10 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so odgovorni za upoštevanje lokalnih predpisov, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
Ta hitri vodnik serije "LtAP LR8 LTE" zajema modele: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-89.png)

Ta naprava sprejme vhod 24V napajalnika, ki je na voljo v originalni embalaži te naprave.

**Prvi koraki:**

- Odprite spodnji pokrov;
- Vstavite kartico SIM v režo SIM 2 (sredina);
- Napravo priključite na vir napajanja;
- Povežite se z računalnikom v brezžično omrežje MikroTik;
- Odprite https://192.168.88.1 v spletnem brskalniku, da začnete konfiguracijo;
- Uporabniško ime: *admin* in privzeto ni nastavljeno geslo;
- Ko ste povezani, v meniju QuickSet LTE AP vnesite PIN https://mt.lv/configuration-sl;
- Nadgradite programsko opremo RouterOS na najnovejšo različico https://mt.lv/upgrade-sl;
- Ponovno se povežite in v meniju *QuickSet LTE AP* nastavite geslo za brezžično omrežje;
- Izberite državo na levi strani zaslona in uporabite nastavitve za urejanje države;
- Zavarujte svojo napravo in nastavite močno geslo;
- Poiščite svojo *LR Gateway ID* na nalepki v izdelku in jo registrirajte v svojem omrežnem strežniku;
- Za osnovno funkcionalnost izdelka so potrebni naslednji paketi RouterOS "npk": gps, lora, system.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti električnega tokokroga in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek lahko namestite na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba pravilne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 30 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

**Opomba:** Pri nekaterih modelih preverite uporabniška in brezžična gesla na nalepki.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-89.png)

Denna enhet accepterar ingång från 24V DC-nätadapter, som finns i originalförpackningen på denna enhet.

Följande RouterOS "npk"-paket krävs för produktens kärnfunktionalitet: gps, lora, system.

**Första stegen:**

- Öppna bottenlocket;
- Sätt i SIM-kortet i SIM 2-kortplatsen (i mitten);
- Anslut enheten till strömkällan;
- Anslut med din dator till MikroTik trådlösa nätverk;
- Öppna https://192.168.88.1 i din webbläsare för att starta konfigurationen;
- Användarnamnet: *admin* och det finns inget lösenord som standard;
- När du är ansluten, ange din PIN https://mt.lv/configuration-sv; i QuickSet LTE AP-menyn;
- Uppgradera RouterOS-programvaran till den senaste versionen https://mt.lv/upgrade-sv;
- Anslut igen och ställ in ditt trådlösa nätverkslösenord i *QuickSet LTE AP-* menyn;
- Välj ditt land till vänster på skärmen för att tillämpa landets regleringsinställningar;
- Säkra din enhet och ställ in ett starkt lösenord;
- Hitta dina *LR Gateway ID* på etiketten i produkten och registrera den på din nätverksserver;
- Följande RouterOS "npk"-paket krävs för produktens kärnfunktionalitet: gps, lora, system.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt kan installeras utomhus. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på systemet.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 30 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

**Notera:** För vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.10或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
此“ LtAP LR8 LTE”系列快速指南涵盖以下型号： RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请寻求顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-89.png)

本设备接受本设备原始包装中提供的24V DC电源适配器的输入。

**第一步：**

- 打开底盖；
- 将SIM卡插入SIM 2插槽（中）；
- 将设备连接到电源；
- 将您的计算机连接到MikroTik无线网络；
- 在网络浏览器中打开https://192.168.88.1 以开始配置；
- 用户名：*admin*，默认情况下未设置密码；
- 连接后，在QuickSet LTE AP菜单中输入PIN https://mt.lv/configuration-zh
- 将RouterOS软件升级到最新版本 https://mt.lv/upgrade-zh
- 再次连接，然后在 *QuickSet LTE AP* 菜单中设置您的无线网络密码;
- 在屏幕左侧选择您的国家/地区，以应用国家/地区法规设置;
- 保护您的设备并设置安全密码;
- 在产品标签上找到 *LR Gateway ID*，并在网络服务器中注册;
- 产品的核心功能需要以下 RouterOS“npk”包：gps、lora、system。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和配件，这些电源和配件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。安装程序负责确保设备的安装符合当地和国家的电气法规。请勿尝试拆卸，修理或修改设备。
- 该产品可以安装在户外。开始安装之前，请仔细阅读安装说明。未能使用正确的硬件和配置或未遵循正确的步骤可能会导致人员伤亡和系统损坏。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。请谨慎使用本产品，并自行承担风险！
- 如果设备发生故障，请断开电源。最快的方法是从电源插座上拔下电源适配器。
- 这是A类产品。在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施。
此MikroTik设备符合欧盟针对不受控制的环境所规定的辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业使用者或公众不得小于30厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

**笔记:** 对于某些型号，请检查标签上的用户密码和无线密码。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.10 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-87.png)

Данное устройство допускает ввод адаптера питания 24 В постоянного тока, который входит в оригинальную упаковку данного устройства.

**Первые шаги:**

- Откройте нижнюю крышку;
- Вставьте SIM-карту в слот SIM 2 (посередине);
- Подключите устройство к источнику питания;
- Подключите компьютер к беспроводной сети MikroTik;
- Откройте https://192.168.88.1 в своем браузере, чтобы начать настройку;
- Имя пользователя: *admin*, по умолчанию пароль не установлен;
- После подключения в меню QuickSet LTE AP введите свои PIN https://mt.lv/configuration-ru;
- Обновите программное обеспечение RouterOS до последней версии https://mt.lv/upgrade-ru;
- Подключитесь снова и в меню *QuickSet LTE AP* установите пароль беспроводной сети;
- Выберите свою страну в левой части экрана, чтобы применить настройки регулирования страны;
- Защитите свое устройство и установите надежный пароль;
- Найдите свой *LR Gateway ID* на этикетке внутри продукта и зарегистрируйте его на своем сетевом сервере;
- Следующие пакеты «npk» RouterOS необходимы для основных функций продукта: gps, lora, system.

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
Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 30 сантиметров от человека.*

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 864-870 МГц, 2400-2483.5 МГц. | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge-91.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

**Примечание**: Для некоторых моделей проверьте пользовательские и беспроводные пароли на наклейке.

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.10 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
Цей короткий посібник серії "LtAP LR8 LTE" охоплює моделі: RBLtAP-2HnD&R11e-LTE&R11e-LR8 (LtAP LR8 LTE kit).
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-37.png)

Цей пристрій приймає вхід 24В адаптера живлення постійного струму, який надається в оригінальній упаковці цього пристрою.

**Перші кроки:**

- Відкрийте нижню кришку;
- Вставте SIM-карту в SIM-слот 2 (середній);
- Підключіть пристрій до адаптеру живлення;
- Підключіть свій комп’ютер до бездротової мережі MikroTik;
- Відкрийте адресу https://192.168.88.1 у веб-браузері, щоб розпочати конфігурацію;
- Ім'я користувача: *admin* і за замовчуванням не встановлено пароль;
- Після підключення в меню *QuickSet* *LTE AP* введіть свій PIN https://mt.lv/configuration-ua;
- Оновіть програмне забезпечення RouterOS до останньої версії https://mt.lv/upgrade-ua;
- Підключіться ще раз і в меню *QuickSet LTE AP* встановіть пароль бездротової мережі;
- Виберіть свою країну та застосуйте налаштування регулювання країни;
- Захистіть свій пристрій і встановіть надійний пароль;
- Знайдіть свій *LR Gateway ID* на етикетці прострою та зареєструйте його на своєму мережевому сервері;
- Для основної функціональності продукту потрібні такі пакети RouterOS "npk": gps, lora, system.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Інсталятор повинен бути знайомий із мережевими структурами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Це обладнання може бути встановлене на відкритому повітрі. Будь ласка, уважно прочитайте інструкцію з монтажу перед початком установки. Недотримання правил використання апаратного забезпечення і конфігурації або проходження правильним процедурам може призвести до небезпечної ситуації для людей і пошкодження системи.
- Ми не можемо гарантувати, що в результаті неправильного використання пристрою не станеться нещасних випадків або пошкоджень. Будь ласка, використовуйте цей продукт з обережністю і дійте на свій страх і ризик!
- У разі збою пристрою відключіть його від живлення. Найшвидший спосіб зробити це - від'єднати адаптер живлення від електричної розетки.
- Це продукт класу А. У побутових умовах цей продукт може спричинити радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити належних заходів.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 30 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 864-870 МГц (14 дБм) 2400-2483.5 МГц (20 дБм).

**Примітка:** Для деяких моделей перевірте пароль користувача та пароль бездротової мережі на наклейці.

## UKCA marking

![](./img/ukca_black_fill.badge-88.gif)

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

## WLAN

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      WLAN
      2400-2483.5 MHz / 20 dBm
    
    **LR (SRD)**863-870 MHz / 14 dBm
  

This MikroTik device meets Maximum WLAN and LTE transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

DC Jack (12-30 V DC) PoE In Ethernet Port (12-30 V DC) Automotive (12-27 V DC)
24 V / 1.2
IP54
-40°..+70°C

\#72998
