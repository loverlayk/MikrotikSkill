# Quick Guide - ATL LTE18 kit

> Models: ATLGM&EG18-EA (ATL LTE18 kit)

**Models: ATLGM&EG18-EA (ATL LTE18 kit)**

![](./img/mt_logo_arrow_v2-02-2.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.7 or the latest stable version, to ensure compliance with local authority regulations!
It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

This Quick Guide covers the model: ATLGM&EG18-EA (ATL LTE18 kit).

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, brochures, and more info about products are at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-2.png)

**First steps:**

- Open the Ethernet port door;
- Insert a SIM card into the slot as indicated on the device;
- Connect the device to the included PoE injector with an Ethernet cable to the data+power end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Configure your device using a web browser through *WebFig* or the *WinBox* tool at [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility.**
- Access *WebFig* by opening http://192.168.188.1, and for *WinBox*, download the tool, navigate to the *Neighbors* tab, and click on the MAC address. The username is *"admin"* with no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version. Must have a valid SIM card inserted and active Internet connection;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.7 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

Този документ обхваща модела: ATLGM&EG18-EA (ATL LTE18 kit).

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-2.png)

**Първи стъпки:**

- Отворете вратата на Ethernet порта;
- Поставете SIM картата в слота, както е указано на устройството;
- Свържете устройството към включения PoE инжектор с Ethernet кабел към края data+power;
- Свържете края за данни на PoE инжектора към компютъра;
- Свържете захранващия адаптер към PoE инжектора;
- Конфигурирайте вашето устройство с помощта на уеб браузър чрез *WebFig* или инструмента *WinBox* на [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Достъп до *WebFig,* като отворите http://192.168.188.1, а за *WinBox* изтеглете инструмента, отидете до раздела *Neighbors* и щракнете върху MAC адреса. Потребителското име е *"admin"* без парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Натиснете бутона "Check for updates" и актуализирайте RouterOS до последната версия. Трябва да имате вкарана валидна SIM карта и активна интернет връзка;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- Задайте паролата на вашия рутер.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоари, одобрени от производителя, и които могат да бъдат намерено аз n оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за монтиране на открито върху стълб. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате подходящия хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата на системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се изисква да предприеме адекватни мерки.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.7 nebo na nejnovější stabilní verzi!
Je na koncových uživatelích, aby dodržovali místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
:::

Tento Stručný průvodce se týká modelu: ATLGM&EG18-EA (ATL LTE18 kit)

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto Stručného průvodce.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-2.png)

**První kroky:**

- Otevřete dvířka portu Ethernet;
- Vložte SIM kartu do slotu podle označení na zařízení;
- Připojte zařízení k přiloženému PoE injektoru pomocí ethernetového kabelu do konce data+power;
- Připojte datový konec PoE injektoru k počítači;
- Připojte napájecí adaptér k PoE injektoru;
- Nakonfigurujte své zařízení pomocí webového prohlížeče prostřednictvím *WebFig* nebo nástroje *WinBox* na [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Otevřete *WebFig* otevřením http://192.168.188.1 a pro *WinBox* si stáhněte nástroj, přejděte na kartu *Neighbors* a klikněte na MAC adresu. Uživatelské jméno je *"admin"* bez hesla (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Klikněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi. Musíte mít vloženou platnou SIM kartu a aktivní internetové připojení;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do nabídky "Files" na WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a aktualizace zabezpečení;
- Nastavte heslo pro váš router.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájení a příslušenství schválené výrobcem, které může být nalezeno v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k montáži venku na sloup. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete odpovídající hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobit rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření.
- Abyste zabránili znečištění životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na určených místech. Seznamte se s postupy správné přepravy zařízení na určená sběrná místa ve vaší oblasti.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.7 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

Dette dokument dækker modellen: ATLGM&EG18-EA (ATL LTE18 kit).

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-2.png)

**Første trin:**

- Åbn Ethernet-portdøren;
- Indsæt SIM-kortet i åbningen som angivet på enheden;
- Tilslut enheden til den medfølgende PoE-injektor med et Ethernet-kabel til data+power -enden;
- Tilslut dataenden af ​​PoE-injektoren til computeren;
- Tilslut strømadapteren til PoE-injektoren;
- Konfigurer din enhed ved hjælp af en webbrowser gennem *WebFig* eller *WinBox* -værktøjet på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Få adgang til *WebFig* ved at åbne http://192.168.188.1, og for *WinBox*, download værktøjet, naviger til fanen *Neighbors*, og klik på MAC-adressen. Brugernavnet er *"admin"* uden adgangskode (eller, for nogle modeller, tjek brugeradgangskoder og trådløse adgangskoder på mærkaten);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version. Du skal have et gyldigt SIM-kort indsat og aktiv internetforbindelse;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload de downloadede pakker til WebFig eller WinBox "Files" menuen og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version sikrer du optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil din routeradgangskode.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og tilbehør godkendt af producenten, og som kan være fundet i den originale emballage af dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive monteret udendørs på en stang. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.
- For at undgå forurening af miljøet skal apparatet adskilles fra husholdningsaffald og bortskaffes på en sikker måde, f.eks. I bestemte områder. Bliv fortrolig med procedurer til korrekt transport af udstyr til udpegede indsamlingssteder i dit område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.7 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
:::

Diese Kurzanleitung behandelt das Modell: ATLGM&EG18-EA (ATL LTE18 kit)

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-2.png)

**Erste Schritte:**

- Öffnen Sie die Ethernet-Port-Tür;
- Setzen Sie die SIM-Karte in den Steckplatz ein, wie auf dem Gerät angegeben;
- Verbinden Sie das Gerät über ein Ethernet-Kabel mit dem data+power -Ende mit dem mitgelieferten PoE-Injektor;
- Verbinden Sie das Datenende des PoE-Injektors mit dem Computer;
- Schließen Sie das Netzteil an den PoE-Injektor an;
- Konfigurieren Sie Ihr Gerät mit einem Webbrowser über *WebFig* oder das *WinBox*-Tool unter [https://mt.lv/winbox](https://mt.lv/winbox); **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Greifen Sie auf *WebFig* zu, indem Sie http://192.168.188.1 öffnen. Laden Sie für *WinBox* das Tool herunter, navigieren Sie zur Registerkarte *Neighbors* und klicken Sie auf die MAC-Adresse. Der Benutzername lautet *"admin"* ohne Passwort (oder überprüfen Sie bei einigen Modellen die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version. Es muss eine gültige SIM-Karte eingelegt und eine aktive Internetverbindung vorhanden sein;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch das Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie eine optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Legen Sie Ihr Routerpasswort fest.

**Sicherheitsinformation:**

- Machen Sie sich vor Arbeiten an MikroTik-Geräten mit den Gefahren elektrischer Schaltkreise vertraut und machen Sie sich mit den üblichen Vorgehensweisen zur Unfallverhütung vertraut. Der Installateur sollte mit den Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das Netzteil und vom Hersteller zugelassenes Zubehör, und das kann sein gefunden In der Originalverpackung dieses Produkts.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Vorschriften für elektrische Geräte entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Montage im Freien an einer Stange vorgesehen. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie die richtige Hardware und Konfiguration nicht verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zur Beschädigung des Systems führen.
- Wir können nicht garantieren, dass durch unsachgemäßen Gebrauch des Geräts keine Unfälle oder Schäden entstehen. Bitte verwenden Sie dieses Produkt mit Vorsicht und betreiben Sie es auf eigenes Risiko!
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Im Falle eines Gerätefehlers trennen Sie das Gerät bitte von der Stromversorgung. Der schnellste Weg, dies zu tun, besteht darin, den Netzadapter aus der Steckdose zu ziehen.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise geeignete Maßnahmen ergreifen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Geräte zu bestimmten Sammelstellen in Ihrer Nähe vertraut.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.7 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
:::

Αυτός ο γρήγορος οδηγός καλύπτει το μοντέλο: ATLGM&EG18-EA (ATL LTE18 kit)

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-2.png)

**Πρώτα βήματα:**

- Ανοίξτε την πόρτα της θύρας Ethernet;
- Τοποθετήστε την κάρτα SIM στην υποδοχή, όπως υποδεικνύεται στη συσκευή;
- Συνδέστε τη συσκευή στον παρεχόμενο εγχυτήρα PoE με ένα καλώδιο Ethernet στο άκρο data+power;
- Συνδέστε το άκρο δεδομένων του εγχυτήρα PoE στον υπολογιστή;
- Συνδέστε το τροφοδοτικό στον εγχυτήρα PoE;
- Διαμορφώστε τη συσκευή σας χρησιμοποιώντας ένα πρόγραμμα περιήγησης ιστού μέσω *του WebFig* ή του εργαλείου *WinBox* στη διεύθυνση [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Αποκτήστε πρόσβαση *στο WebFig* ανοίγοντας το http://192.168.188.1 και για το *WinBox*, κατεβάστε το εργαλείο, μεταβείτε στην καρτέλα *Neighbors* και κάντε κλικ στη διεύθυνση MAC. Το όνομα χρήστη είναι *"admin"* χωρίς κωδικό πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματου δικτύου στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην πιο πρόσφατη έκδοση. Πρέπει να υπάρχει εισαγμένη έγκυρη κάρτα SIM και ενεργή σύνδεση στο internet;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού "Files" του WebFig ή WinBox και επανεκκινήστε τη συσκευή;
- Αναβαθμίζοντας το λογισμικό του RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Ορίστε τον κωδικό πρόσβασης του δρομολογητή σας.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την παροχή ρεύματος και αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και ποια μπορεί να είναι βρέθηκαν στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται να τοποθετηθεί σε εξωτερικό χώρο σε έναν πόλο. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του υλικού και των ρυθμίσεων διόρθωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.
- Πρόκειται για προϊόν κλάσης Α. Σε οικιακό περιβάλλον, αυτό το προϊόν μπορεί να προκαλέσει ραδιοπαρεμβολές, οπότε ενδέχεται να χρειαστεί να ληφθούν τα κατάλληλα μέτρα από τον χρήστη.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.7 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
:::

Esta guía rápida cubre el modelo: ATLGM&EG18-EA (ATL LTE18 kit)

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-2.png)

**Primeros pasos:**

- Abra la puerta del puerto Ethernet;
- Inserte la tarjeta SIM en la ranura según se indica en el dispositivo;
- Conecte el dispositivo al inyector PoE incluido con un cable Ethernet hasta el extremo data+power;
- Conecte el extremo de datos del inyector PoE a la computadora;
- Conecte el adaptador de corriente al inyector PoE;
- Configure su dispositivo usando un navegador web a través de *WebFig* o la herramienta *WinBox* en [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Acceda *a WebFig* abriendo http://192.168.188.1 y, para *WinBox*, descargue la herramienta, navegue hasta la pestaña *Neighbors* y haga clic en la dirección MAC. El nombre de usuario es *"admin"* sin contraseña (o, para algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión. Debe tener una tarjeta SIM válida insertada y una conexión a Internet activa;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú "Files" de WebFig o WinBox y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- Configura la contraseña de tu enrutador.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Use solo la fuente de alimentación y accesorios aprobados por el fabricante, y que pueden ser encontró En el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para montarse en exteriores en un poste. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podrían producir situaciones peligrosas para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- El tomacorriente se instalará cerca del equipo y será de fácil acceso.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Este es un producto de clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en las áreas designadas. Familiarícese con los procedimientos para transportar correctamente el equipo a los puntos de recolección designados en su área.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.7 või uusimale stabiilsele versioonile!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTiku raadioseadmed tuleb installida vastavalt juhistele.
:::

See lühijuhend hõlmab mudelit: ATLGM&EG18-EA (ATL LTE18 kit)

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*Kui vajate seadistamisel abi, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-2.png)

**Esimesed sammud:**

- Avage Etherneti pordi uks;
- Sisestage SIM-kaart pesasse vastavalt seadmel märgitule;
- Ühendage seade kaasasoleva PoE-pihustiga Etherneti kaabli abil data+power otsaga;
- Ühendage PoE-pihusti andmeots arvutiga;
- Ühendage toiteadapter PoE-pihustiga;
- Seadistage oma seade veebibrauseri abil *WebFig* või *WinBox* tööriista kaudu aadressil [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Juurdepääs *numbrile WebFig*, avades numbri http://192.168.188.1, ja *WinBox* jaoks laadige tööriist alla, navigeerige vahekaardile *Neighbors* ja klõpsake MAC-aadressil. Kasutajanimi on *"admin"* ilma paroolita (või mõne mudeli puhul kontrollige kasutaja ja traadita ühenduse paroole kleebiselt);
- Klõpsake nupul "Check for updates" ja värskendage RouterOS-i viimasele versioonile. Peab olema sisestatud kehtiv SIM-kaart ja aktiivne Interneti-ühendus;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige allalaaditud paketid üles WebFig või WinBox "Files" menüüsse ja taaskäivitage seade;
- Uuendades RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadista ruuteri parool.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult toiteallikat ja tootja poolt heaks kiidetud lisaseadmed, mis võivad olla leitud ma olen selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud välitingimustes vardale paigaldamiseks. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhiseid. Õige riistvara ja konfiguratsiooni mittekasutamine või õigete protseduuride järgimata jätmine võib põhjustada inimestele ohtliku olukorra ja kahjustada süsteemi.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja utiliseerige see ohutult, näiteks selleks ettenähtud kohtades. Tutvuge seadmete nõuetekohase transportimise protseduuridega teie piirkonnas asuvatesse kogumispunktidesse.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.7 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
:::

Tämä pikaopas kattaa mallin: ATLGM&EG18-EA (ATL LTE18 kit)

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*Jos tarvitset apua konfiguroinnissa, kysy neuvoa- antajalta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-2.png)

**Ensiaskeleet:**

- Avaa Ethernet-portin ovi;
- Aseta SIM-kortti paikkaan laitteen merkintöjen mukaisesti;
- Liitä laite mukana toimitettuun PoE-injektoriin Ethernet-kaapelilla data+power - päähän;
- Liitä PoE-injektorin datapää tietokoneeseen;
- Liitä virtalähde PoE-suuttimeen;
- Määritä laitteesi verkkoselaimella *WebFig*- tai *WinBox*-työkalulla osoitteessa [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Käytä *WebFigiä* avaamalla http://192.168.188.1 ja lataa *WinBox*-työkalu, siirry *Neighbors*-välilehdelle ja napsauta MAC-osoitetta. Käyttäjätunnus on *"admin"* ilman salasanaa (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Klikkaa "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon. Sinun on oltava kelvollinen SIM-kortti asennettuna ja aktiivinen Internet-yhteys;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFig- tai WinBox-"Files"-valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmiston uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- Aseta reitittimesi salasana.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain virtalähdettä ja valmistajan hyväksymät lisävarusteet, jotka voivat olla löydetty Olen tämän tuotteen alkuperäispakkaus.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi ulos pylvääseen. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikean laitteiston ja kokoonpanon käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi johtaa ihmisille vaaralliseen tilanteeseen ja järjestelmän vaurioitumiseen.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla esimerkiksi määrätyillä alueilla. Tutustu toimenpiteisiin, joilla laite kuljetetaan asianmukaisesti alueellesi määritettyihin keräyspisteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.7 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

Ce document couvre le modèle: ATLGM&EG18-EA (ATL LTE18 kit).

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-2.png)

**Premiers pas:**

- Ouvrez la porte du port Ethernet;
- Insérez la carte SIM dans le logement comme indiqué sur l’appareil;
- Connectez l'appareil à l'injecteur PoE inclus avec un câble Ethernet à l' extrémité data+power;
- Connectez l'extrémité des données de l'injecteur PoE à l'ordinateur;
- Connectez l'adaptateur secteur à l'injecteur PoE;
- Configurez votre appareil à l'aide d'un navigateur Web via *WebFig* ou l' outil *WinBox* sur [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Accédez *à WebFig* en ouvrant http://192.168.188.1 et pour *WinBox*, téléchargez l'outil, accédez à l' onglet *Neighbors* et cliquez sur l'adresse MAC. Le nom d'utilisateur est *"admin"* sans mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version. Vous devez avoir une carte SIM valide insérée et une connexion Internet active;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les paquets téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, une stabilité et des mises à jour de sécurité;
- Configurez le mot de passe de votre routeur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l' alimentation et accessoires approuvés par le fabricant, et qui peuvent être a trouvé dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être monté à l'extérieur sur un poteau. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration corrects ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.
- Pour éviter la contamination de l'environnement, séparez l'appareil des déchets ménagers et éliminez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.7 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
:::

Ovaj kratki vodič pokriva model: ATLGM&EG18-EA (ATL LTE18 kit)

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-2.png)

**Prvi koraci:**

- Otvorite vrata za Ethernet vrata;
- Umetnite SIM karticu u utor kako je označeno na uređaju;
- Spojite uređaj na priloženi PoE injektor pomoću Ethernet kabela na kraju data+power;
- Spojite podatkovni kraj PoE injektora na računalo;
- Spojite strujni adapter na PoE injektor;
- Konfigurirajte svoj uređaj pomoću web preglednika putem *WebFig* ili alata *WinBox* na [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Pristupite *WebFig* otvaranjem http://192.168.188.1, a za *WinBox* preuzmite alat, idite na karticu *Neighbors* i kliknite na MAC adresu. Korisničko ime je *"admin"* bez lozinke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Kliknite gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju. Morate imati umetnutu važeću SIM karticu i aktivnu internetsku vezu;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem RouterOS softvera na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- Postavite lozinku za svoj usmjerivač.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobren od proizvođača, a može biti pronađeno Ja nisam originalno pakiranje ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen postavljanju vani na stup. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne slijedite ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere.
- Da biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na za to predviđena mjesta. Upoznajte se s postupcima pravilnog transporta opreme do određenih sabirnih mjesta u vašem području.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.7-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
:::

Ez a Gyors útmutató a következőre vonatkozik: ATLGM&EG18-EA (ATL LTE18 kit)

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-2.png)

**Első lépések:**

- Nyissa ki az Ethernet port ajtaját;
- Helyezze be a SIM-kártyát a foglalatba az eszközön jelzett módon;
- Csatlakoztassa az eszközt a mellékelt PoE befecskendezőhöz egy Ethernet-kábellel az data+power-es végéhez;
- Csatlakoztassa a PoE injektor adatvégét a számítógéphez;
- Csatlakoztassa a hálózati adaptert a PoE befecskendezőhöz;
- Konfigurálja készülékét webböngészővel a *WebFig* vagy a *WinBox* eszköz segítségével a [https://mt.lv/winbox](https://mt.lv/winbox) oldalon; **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- *A WebFig* eléréséhez nyissa meg a http://192.168.188.1 számot, és *WinBox* esetén töltse le az eszközt, lépjen a *Neighbors* lapra, és kattintson a MAC-címre. A felhasználónév *"admin"*, jelszó nélkül (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra. Érvényes SIM kártyának kell lennie a helyén, és aktív internetkapcsolatnak kell lennie;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- A RouterOS szoftver frissítésével a legújabb verzióra optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- Állítsa be a router jelszavát.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak az áramellátást használja és a gyártó által jóváhagyott kiegészítők, amelyek lehetnek megtalált A termék eredeti csomagolása.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ez a termék kültéren, oszlopra szerelhető. Kérjük, a telepítés megkezdése előtt figyelmesen olvassa el a szerelési útmutatót. A megfelelő hardver és konfiguráció használatának elmulasztása, illetve a megfelelő eljárások betartásának elmulasztása emberekre veszélyes helyzetet és a rendszer károsodását okozhatja.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, amely esetben a felhasználót fel kell kérni a megfelelő intézkedések megtételére.
- A környezet szennyeződésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon dobja el, például a kijelölt területekre. Ismerje meg a berendezés megfelelő szállítási eljárásait a környéken található gyűjtőhelyekre.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.7 atau versi stabil terbaru, untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Pengguna akhir bertanggung jawab untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya keluaran, persyaratan perkabelan, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat radio MikroTik harus diinstal sesuai petunjuk.
:::

Panduan Cepat ini mencakup model: ATLGM&EG18-EA (kit ATL LTE18)

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama model produk pada label casing (ID).*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um-id](https://mt.lv/um-id) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Spesifikasi teknis, brosur, dan info lebih lanjut mengenai produk ada di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [https://mt.lv/help-id](https://mt.lv/help-id)*
*Jika Anda memerlukan bantuan dalam konfigurasi, silakan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/id.badge.png)

**Langkah pertama:**

- Buka pintu port Ethernet;
- Masukkan kartu SIM ke dalam slot sesuai petunjuk pada perangkat;
- Sambungkan perangkat ke PoE injector yang disertakan dengan kabel Ethernet ke ujung data+power;
- Sambungkan ujung data PoE injector ke komputer;
- Sambungkan adaptor daya ke PoE injector;
- Konfigurasi perangkat Anda menggunakan peramban web melalui WebFig atau alat WinBox di [https://mt.lv/winbox](https://mt.lv/winbox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Akses WebFig dengan membuka http://192.168.188.1, dan untuk WinBox, unduh alatnya, buka tab Neighbors, dan klik pada alamat MAC. Nama pengguna adalah "admin" tanpa kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru. Harus ada kartu SIM yang valid dan koneksi Internet aktif;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu "Files" WebFig atau WinBox dan reboot perangkat;
- Dengan meng-upgrade perangkat lunak RouterOS ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Atur kata sandi router Anda.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, yang dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dimaksudkan untuk dipasang di luar ruangan pada tiang. Harap baca petunjuk pemasangan dengan cermat sebelum memulai pemasangan. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem.
- Kami tidak dapat menjamin bahwa tidak akan terjadi kecelakaan atau kerusakan akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan pengoperasian dengan risiko Anda sendiri!
- Stopkontak harus dipasang di dekat peralatan dan mudah dijangkau.
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut adaptor daya dari stopkontak.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai.
- Untuk menghindari kontaminasi terhadap lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan cara yang aman, misalnya di tempat yang telah ditentukan. Pahami prosedur pengangkutan peralatan dengan benar ke tempat pengumpulan yang ditentukan di wilayah Anda.

**Paparan Radiasi Frekuensi Radio:** Peralatan MikroTik ini mematuhi batas paparan radiasi Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini sebaiknya dipasang dan dioperasikan tidak lebih dekat dari 20 sentimeter dari tubuh Anda, pengguna pekerjaan, atau masyarakat umum.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.7 o all'ultima versione stabile, per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
:::

Questa guida rapida copre il modello: ATLGM&EG18-EA (ATL LTE18 kit)

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, consulta un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-2.png)

**Primi passi:**

- Aprire la porta della porta Ethernet;
- Inserire la scheda SIM nello slot come indicato sul dispositivo;
- Collega il dispositivo all'iniettore PoE incluso con un cavo Ethernet all'estremità data+power;
- Collegare l'estremità dati dell'iniettore PoE al computer;
- Collegare l'adattatore di alimentazione all'iniettore PoE;
- Configura il tuo dispositivo utilizzando un browser web tramite *WebFig* o lo strumento *WinBox* su [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Accedi *a WebFig* aprendo http://192.168.188.1 e, per *WinBox*, scarica lo strumento, vai alla scheda *Neighbors* e fai clic sull'indirizzo MAC. Il nome utente è *"admin"* senza password (o, per alcuni modelli, verificare utente e password wireless sull'adesivo);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione. Deve essere inserita una scheda SIM valida e una connessione Internet attiva;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Imposta la password del tuo router.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l' alimentatore e accessori approvati dal produttore e quali possono essere trovato nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è progettato per essere montato all'esterno su un'asta. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il rispetto delle procedure corrette potrebbe comportare una situazione pericolosa per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio, in aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura ai punti di raccolta designati nella propria zona.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.7 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
:::

Þessi snögga leiðarvísi nær yfir líkanið: ATLGM&EG18-EA (ATL LTE18 kit)

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*Ef þú þarft hjálp við stillingar, vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-2.png)

**Fyrstu skrefin:**

- Opnaðu Ethernet tengihurðina;
- Settu SIM-kortið í raufina eins og sýnt er á tækinu;
- Tengdu tækið við meðfylgjandi PoE inndælingartæki með Ethernet snúru við enda data+power;
- Tengdu gagnaenda PoE inndælingartækisins við tölvuna;
- Tengdu straumbreytinn við PoE inndælingartækið;
- Stilltu tækið þitt með því að nota vafra í gegnum *WebFig* eða *WinBox* tólið á [https://mt.lv/winbox](https://mt.lv/winbox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Fáðu aðgang að *WebFig* með því að opna http://192.168.188.1 og fyrir *WinBox* skaltu hlaða niður tólinu, fara á *Neighbors* flipann og smella á MAC vistfangið. Notandanafnið er *"admin"* án lykilorðs (eða, fyrir sumar gerðir, athugaðu notanda og þráðlausa lykilorð á límmiðanum);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS í nýjustu útgáfu. Þú verður að hafa gilt SIM-kort stungið inn og virkt netengingu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum í WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Með því að uppfæra RouterOS hugbúnaðinn á nýjustu útgáfu getur þú tryggt besta árangur, stöðugleika og öryggisuppfærslur;
- Stilla lykilorðið á routerinum þínu.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihlutir sem framleiðandi hefur samþykkt og hver getur verið Fundið i n upprunalegu umbúðir þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessi vara er ætluð til að festa utandyra á stöng. Vinsamlegast lestu uppsetningarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Misbrestur á að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti valdið hættulegum aðstæðum fyrir fólk og skemmdir á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir.
- Til að koma í veg fyrir mengun umhverfisins skaltu aðskilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur til að flytja búnaðinn rétt til tilnefndra söfnunarstaða á þínu svæði.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.7 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukerens ansvar å følge lokale landsbestemmelser, inkludert drift innen lovlige frekvenskanaler, utgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

Denne hurtigveiledningen dekker modellen: ATLGM&EG18-EA (ATL LTE18 kit).

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-2.png)

**Første steg:**

- Åpne Ethernet-portdøren;
- Sett SIM-kortet inn i sporet slik det er angitt på enheten;
- Koble enheten til den medfølgende PoE-injektoren med en Ethernet-kabel til data+power -enden;
- Koble dataenden av PoE-injektoren til datamaskinen;
- Koble strømadapteren til PoE-injektoren;
- Konfigurer enheten din ved å bruke en nettleser via *WebFig* eller *WinBox-* verktøyet på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Få tilgang til *WebFig* ved å åpne http://192.168.188.1, og for *WinBox*, last ned verktøyet, naviger til *Neighbors-* fanen og klikk på MAC-adressen. Brukernavnet er *"admin"* uten passord (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- Klikk på "Check for updates" -knappen og oppdater RouterOS til den nyeste versjonen. Det må være satt inn et gyldig SIM-kort og aktiv internettilkobling;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig- eller WinBox-"Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen, kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- Sett opp passordet for ruteren din.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehør godkjent av produsenten, og som kan være funnet i n den originale emballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å være montert utendørs på en stolpe. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke den rette maskinvaren og konfigurasjonen eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak.
- For å unngå forurensning av miljøet, må du skille enheten fra husholdningsavfall og kaste den på en sikker måte, for eksempel i bestemte områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

*Šį įrenginį reikia atnaujinti į „RouterOS v7.7“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!*

*Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.*

Šis trumpasis vadovas apima modelį: ATLGM&EG18-EA (ATL LTE18 kit)

-

![](./img/image2020-2-5_9-15-30.badge-2.png)

*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*

*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*

*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*

*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*

*Jei jums reikia pagalbos dėl konfigūracijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

**Pirmieji žingsniai:**

- Atidarykite Ethernet prievado duris;
- Įdėkite SIM kortelę į lizdą taip, kaip nurodyta įrenginyje;
- Prijunkite įrenginį prie pridedamo PoE purkštuko Ethernet kabeliu iki data+power galo;
- Prijunkite PoE purkštuko duomenų galą prie kompiuterio;
- Prijunkite maitinimo adapterį prie PoE purkštuko;
- Sukonfigūruokite įrenginį naudodami žiniatinklio naršyklę naudodami *WebFig* arba *WinBox* įrankį adresu [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Pasiekite *WebFig* atidarę http://192.168.188.1 ir *WinBox* atsisiųskite įrankį, eikite į skirtuką *Neighbors* ir spustelėkite MAC adresą. Vartotojo vardas yra *"admin"* be slaptažodžio (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Paspauskite mygtuką "Check for updates" ir atnaujinkite RouterOS iki naujausios versijos. Turi būti įdėta galiojanti SIM kortelė ir aktyvus interneto ryšys;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite prietaisą iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Nustatykite savo maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik maitinimo šaltinį ir gamintojo patvirtinti priedai, kurie gali būti rasta i originali šio gaminio pakuotė.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas skirtas montuoti lauke ant stulpo. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite pataisytos aparatūros ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių.
- Kad išvengtumėte aplinkos užteršimo, atskirkite prietaisą nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.7 stabilo vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijai.
:::

Šī īsā rokasgrāmata attiecas uz modeli: ATLGM&EG18-EA (ATL LTE18 kit)

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs ātrās rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*Ja jums ir nepieciešama palīdzība ierīces uzstādīšanā, lūdzu, konsultējieties ar konsultantiem [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-2.png)

**Pirmie soļi:**

- Atveriet Ethernet porta vāku;
- Ievietojiet SIM karti slotā, kā norādīts uz ierīces;
- Pievienojiet ierīci komplektā iekļautajam PoE inžektoram, izmantojot Ethernet kabeli un pieslēdzot to pie data+power izvades;
- Pievienojiet PoE inžektora datu galu datoram;
- Pievienojiet strāvas adapteri PoE inžektoram;
- Konfigurējiet savu ierīci, izmantojot tīmekļa pārlūkprogrammu, izmantojot *WebFig* vai *WinBox* rīku vietnē [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Pieslēdzieties ierīcei izmantojot *WebFig*, atverot savā pārlūkā http://192.168.188.1, vai lejupielādējiet rīku *WinBox* un dodieties uz cilni *Neighbors* un noklikšķiniet uz MAC adreses. Lietotājvārds ir *"admin"* bez paroles (vai dažiem modeļiem atrodiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjauniniet RouterOS līdz jaunākajai versijai. Jābūt ievietotai derīgai SIM karti un aktīvai interneta savienojumam;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamos pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox sadaļu "Files" un pārstartējiet ierīci;
- Atjauninot savu RouterOS programmatūru līdz jaunākajai versijai, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Iestatiet sava maršrutētāja paroli.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprināto barošanas adapteri un piederumus, kas iekļauti šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai ārā uz staba. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nepareizas aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.7 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż operazzjoni fi ħdan kanali tal-frekwenza legali, qawwa tal-ħruġ, rekwiżiti tal-kejbils u rekwiżiti tal-Għażla tal-Frekwenza Dynamic (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
:::

Din il-Gwida Quick tkopri l-mudell: ATLGM&EG18-EA (ATL LTE18 kit)

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-2.png)

**L-ewwel passi:**

- Iftaħ il-bieb tal-port Ethernet;
- Daħħal is-SIM card fl-islott kif indikat fuq l-apparat;
- Qabbad l-apparat mal-injettur PoE inkluż b'kejbil Ethernet mat-tarf data+power;
- Qabbad it-tarf tad-dejta tal-injettur PoE mal-kompjuter;
- Qabbad l-adapter tal-enerġija mal-injettur PoE;
- Ikkonfigura t-tagħmir tiegħek billi tuża web browser permezz ta' *WebFig* jew l -għodda *WinBox* fuq [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Aċċessa *WebFig* billi tiftaħ http://192.168.188.1, u għal *WinBox*, niżżel l-għodda, innaviga fit- tab *Neighbors*, u kklikkja fuq l-indirizz MAC. L-isem tal-utent huwa *"admin"* mingħajr password (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u mingħajr fili fuq l-istiker);
- Ikklikkja fuq il-buttuna "Check for updates" u agħġorna l-RouterOS għall-aħħar verżjoni. Għandek tkun hemm karta SIM valida imfassla u konnessjoni attiva tal-Internet;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Żid id-pakketti li dawn tniżżel fil-meni "Files" ta 'WebFig jew WinBox u rirreboot l-apparat;
- Billi taġġorna l-software RouterOS għall-aħħar verżjoni, tista 'tiżgura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Iffurmat il-password tar-router tiegħek.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il - provvista tal- enerġija u aċċessorji approvati mill-manifattur, u li jistgħu jiġu sibt i n l-imballaġġ oriġinali ta 'dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jintrama fuq barra fuq arblu. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar b’attenzjoni qabel tibda l-installazzjoni. Jekk tonqos milli tuża l- hardware u l-konfigurazzjoni korretta jew issegwi l-proċeduri t-tajba tista 'tirriżulta f'sitwazzjoni perikoluża għan-nies u tagħmel ħsara lis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.7 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, inclusief de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
:::

Deze beknopte handleiding behandelt het model: ATLGM&EG18-EA (ATL LTE18 kit).

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties van dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*Als u hulp nodig heeft bij het configureren, zoek dan een adviseur [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-2.png)

**Eerste stappen:**

- Open de ethernetpoortdeur;
- Plaats de SIM-kaart in de sleuf zoals aangegeven op het apparaat;
- Sluit het apparaat aan op de meegeleverde PoE-injector met een Ethernet-kabel aan het data+power- uiteinde;
- Sluit het data-uiteinde van de PoE-injector aan op de computer;
- Sluit de voedingsadapter aan op de PoE-injector;
- Configureer uw apparaat met behulp van een webbrowser via *WebFig* of de *WinBox*-tool op [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- U krijgt toegang tot *WebFig* door http://192.168.188.1 te openen. Voor *WinBox* downloadt u de tool, navigeert u naar het tabblad *Neighbors* en klikt u op het MAC-adres. De gebruikersnaam is *"admin"* zonder wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie. Er moet een geldige SIM-kaart zijn ingevoegd en een actieve internetverbinding zijn;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Stel het wachtwoord van uw router in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures voor het voorkomen van ongevallen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires goedgekeurd door de fabrikant, en die kunnen zijn gevonden i n de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om buiten op een paal te worden gemonteerd. Lees de montage-instructies zorgvuldig voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Het stopcontact moet in de buurt van de apparatuur worden geïnstalleerd en moet gemakkelijk toegankelijk zijn.
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stroomadapter uit het stopcontact te halen.
- Dit is een Klasse A-product. In een huishoudelijke omgeving kan dit product radiostoring veroorzaken. In dat geval moet de gebruiker mogelijk passende maatregelen nemen.
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.7 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik należy zainstalować zgodnie z instrukcjami.
:::

Niniejszy Krótki przewodnik obejmuje model: ATLGM&EG18-EA (ATL LTE18 kit)

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy w konfiguracji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-2.png)

**Pierwsze kroki:**

- Otwórz drzwiczki portu Ethernet;
- Włóż kartę SIM do gniazda zgodnie z oznaczeniami na urządzeniu;
- Podłącz urządzenie do dołączonego wtryskiwacza PoE za pomocą kabla Ethernet do końca data+power;
- Podłącz końcówkę danych wtryskiwacza PoE do komputera;
- Podłącz zasilacz do wtryskiwacza PoE;
- Skonfiguruj swoje urządzenie za pomocą przeglądarki internetowej za pomocą narzędzia *WebFig* lub *WinBox* pod adresem [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Uzyskaj dostęp do *WebFig,* otwierając http://192.168.188.1, a w przypadku *WinBox* pobierz narzędzie, przejdź do karty *Neighbors* i kliknij adres MAC. Nazwa użytkownika to *"admin"* bez hasła (lub, w przypadku niektórych modeli, sprawdź hasło użytkownika i hasło sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji. Musi być włożona ważna karta SIM i aktywne połączenie internetowe;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Wgraj pobrane pakiety do menu "Files" w WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- Skonfiguruj hasło do routera.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj tylko zasilacza i akcesoria zatwierdzone przez producenta, i które mogą być znaleziony w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Produkt przeznaczony jest do montażu na zewnątrz na słupie. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie odpowiedniego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- Gniazdko powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe. W takim przypadku użytkownik może zostać zobowiązany do podjęcia odpowiednich kroków.
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.7 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
:::

Este Guia Rápido abrange o modelo: ATLGM&EG18-EA (ATL LTE18 kit)

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-2.png)

**Primeiros passos:**

- Abra a porta da porta Ethernet;
- Insira o cartão SIM no slot conforme indicado no dispositivo;
- Conecte o dispositivo ao injetor PoE incluído com um cabo Ethernet na extremidade data+power;
- Conecte a extremidade de dados do injetor PoE ao computador;
- Conecte o adaptador de energia ao injetor PoE;
- Configure seu dispositivo usando um navegador da web através do *WebFig* ou da ferramenta *WinBox* em [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Acesse *WebFig* abrindo http://192.168.188.1, e para *WinBox*, baixe a ferramenta, navegue até a aba *Neighbors* e clique no endereço MAC. O nome de usuário é *"admin"* sem senha (ou, para alguns modelos, verifique as senhas de usuário e wireless no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente. Deve ter um cartão SIM válido inserido e uma conexão de Internet ativa;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Carregue os pacotes baixados no menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar seu software RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- Configure a senha do seu roteador.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação acessórios aprovados pelo fabricante e que podem ser encontrado na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser montado ao ar livre em um poste. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou do não cumprimento dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- A tomada deve ser instalada próxima ao equipamento e deve ser de fácil acesso.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.7 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țărilor, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
:::

Acest Ghid rapid acoperă modelul: ATLGM&EG18-EA (ATL LTE18 kit)

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-2.png)

**Primii pasi:**

- Deschideți portul Ethernet;
- Introduceți cartela SIM în slot conform indicațiilor de pe dispozitiv;
- Conectați dispozitivul la injectorul PoE inclus cu un cablu Ethernet la capătul data+power;
- Conectați capătul de date al injectorului PoE la computer;
- Conectați adaptorul de alimentare la injectorul PoE;
- Configurați dispozitivul folosind un browser web prin *WebFig* sau instrumentul *WinBox* la [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Accesați *WebFig* deschizând http://192.168.188.1, iar pentru *WinBox*, descărcați instrumentul, navigați la fila *Neighbors* și faceți clic pe adresa MAC. Numele de utilizator este *"admin"* fără parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune. Trebuie să aveți o cartelă SIM validă inserată și o conexiune la internet activă;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- Setați parola routerului.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesorii aprobate de producător și care pot fi găsite Am n ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie montat în aer liber pe un stâlp. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-le într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător al echipamentelor la punctele de colectare desemnate din zona dumneavoastră.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.7 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných užívateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
:::

Táto Stručná príručka sa týka modelu: ATLGM&EG18-EA (ATL LTE18 kit)

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej stránke tohto stručného sprievodcu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-2.png)

**Prvé kroky:**

- Otvorte dvere portu Ethernet;
- Vložte SIM kartu do slotu podľa označenia na zariadení;
- Pripojte zariadenie k priloženému PoE injektoru pomocou ethernetového kábla ku koncu data+power;
- Pripojte dátový koniec PoE injektora k počítaču;
- Pripojte napájací adaptér k PoE injektoru;
- Nakonfigurujte svoje zariadenie pomocou webového prehliadača cez *WebFig* alebo nástroj *WinBox* na [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Prejdite na *číslo WebFig* otvorením http://192.168.188.1 a pre *číslo WinBox* si stiahnite nástroj, prejdite na kartu *Neighbors* a kliknite na adresu MAC. Používateľské meno je *"admin"* bez hesla (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslo na nálepke);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu. Musí byť vložená platná SIM karta a aktívne internetové pripojenie;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v aplikácii WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a bezpečnostné aktualizácie;
- Nastavte heslo pre váš router.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájanie a príslušenstvo schválené výrobcom, ktoré môže byť nájdených v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na montáž vonku na stĺp. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať správne, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia.
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.7 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so odgovorni za upoštevanje lokalnih predpisov, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
:::

Ta hitri vodnik zajema model: ATLGM&EG18-EA (ATL LTE18 kit)

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani teh hitrih navodil.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-2.png)

**Prvi koraki:**

- Odprite vrata vrat Ethernet;
- Vstavite kartico SIM v režo, kot je označeno na napravi;
- Povežite napravo s priloženim injektorjem PoE z ethernetnim kablom na koncu data+power;
- Priključite podatkovni konec injektorja PoE na računalnik;
- Priključite napajalnik na injektor PoE;
- Konfigurirajte svojo napravo s spletnim brskalnikom prek *WebFig* ali orodja *WinBox* na [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Dostopite do *WebFig* tako, da odprete http://192.168.188.1, za *WinBox* pa prenesite orodje, pojdite na zavihek *Neighbors* in kliknite naslov MAC. Uporabniško ime je *"admin"* brez gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Kliknite gumb "Check for updates" in posodobite RouterOS na najnovejšo različico. Vstaviti morate veljavno SIM kartico in imeti aktiven internetni priključek;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" v aplikaciji WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno delovanje, stabilnost in posodobitve varnosti;
- Nastavite geslo za svoj usmerjevalnik.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatki, ki jih je odobril proizvajalec, in ki so lahko najdeno i n originalna embalaža tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen za namestitev na prostem na drog. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba ustrezne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe.
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.7 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

Detta dokument täcker modellen: ATLGM&EG18-EA (ATL LTE18 kit).

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfiguration, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-2.png)

**Första stegen:**

- Öppna Ethernet-portdörren;
- Sätt i SIM-kortet i facket enligt anvisningarna på enheten;
- Anslut enheten till den medföljande PoE-injektorn med en Ethernet-kabel till data+power -änden;
- Anslut dataänden på PoE-injektorn till datorn;
- Anslut strömadaptern till PoE-injektorn;
- Konfigurera din enhet med en webbläsare via *WebFig* eller verktyget *WinBox* på [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Gå till *WebFig* genom att öppna http://192.168.188.1 och för *WinBox* ladda ner verktyget, navigera till fliken *Neighbors* och klicka på MAC-adressen. Användarnamnet är *"admin"* utan lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen. Det måste finnas ett giltigt SIM-kort isatt och en aktiv internetanslutning;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- Ställ in lösenordet för din router.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast strömförsörjningen och tillbehör som godkänts av tillverkaren, och som kan vara hittades i den ursprungliga förpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att monteras utomhus på en stolpe. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på syste m.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.7或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求以及动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
:::

本快速指南介绍了以下型号：ATLGM&EG18-EA (ATL LTE18 kit)

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请咨询顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-2.png)

**第一步：**

- 打开以太网端口门；
- 按照设备上的指示将 SIM 卡插入卡槽中；
- 用以太网线将设备连接到附带的 PoE 注入器的data+power端；
- 将PoE供电器的数据端连接至电脑；
- 将电源适配器连接至 PoE 供电器；
- 使用网络浏览器通过 *WebFig* 或 *WinBox* 工具（[https://mt.lv/winbox](https://mt.lv/winbox) ）配置您的设备； **提供多种配置方法以确保可访问性；**
- 通过打开http://192.168.188.1 访问 *WebFig*，对于 *WinBox*，下载该工具，导航到 *Neighbors* 选项卡，然后单击 MAC 地址。用户名是 *"admin"*，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）；
- 单击"Check for updates"按钮并将RouterOS更新到最新版本。必须插入有效的SIM卡并具有活动的互联网连接;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的"Files"菜单，并重新启动设备;
- 通过将RouterOS软件升级到最新版本，可以确保最佳性能、稳定性和安全更新;
- 设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用 电源 和制造商认可的配件, 可以 发现 在此产品的原包装中。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 本产品旨在安装在户外的杆子上。 开始安装前请仔细阅读安装说明。 如果不使用正确的硬件和配置或不遵循正确的程序，可能会导致人身危险和系统损坏。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 插座應安裝在設備附近，並應易於取用。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 这是A类产品。 在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施。
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。

**射频辐射暴露：** 此MikroTik设备符合针对不受控制的环境所设定的和欧盟辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业用户或公众的距离不得超过20厘米。

制造商：Mikrotikls SIA，拉脱维亚, Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.7 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

Краткое руководство охватывает модель: ATLGM&EG18-EA (ATL LTE18 kit)

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge.png)

**Первые шаги:**

- Откройте дверь порта Ethernet;
- Вставьте SIM-карту в слот в соответствии с обозначениями на устройстве;
- Подключите устройство к входящему в комплект PoE-инжектору с помощью кабеля Ethernet к концу data+power;
- Подключите конец данных PoE-инжектора к компьютеру;
- Подключите адаптер питания к PoE-инжектору;
- Настройте свое устройство при помощи веб-браузера и *WebFig* или утилиты *WinBox*[https://mt.lv/winbox](https://mt.lv/winbox); **существует несколько методов настройки для обеспечения доступности;**
- Откройте адрес в веб-браузере http://192.168.188.1, или, используя *WinBox* перейдите на вкладку *Neighbors* и нажмите на MAC-адрес. Имя пользователя - *"admin"* без пароля (или, для некоторых моделей, проверьте пароль пользователя и пароль беспроводной сети на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии. Должна быть вставлена действующая SIM-карта и активное интернет-подключение;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" в WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- Установите пароль для вашего маршрутизатора.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только блок питания и аксессуары, утвержденные производителем, и которые можно найти в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт предназначен для установки на открытом воздухе на столбе. Пожалуйста, внимательно прочитайте инструкцию по монтажу перед началом установки. Несоблюдение правил использования аппаратного обеспечения и конфигурации или следования правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- Розетка должна быть установлена ​​рядом с оборудованием и должна быть легко доступна.
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - отсоединить адаптер питания от электрической розетки.
- Это продукт класса А. В домашних условиях этот продукт может вызывать радиопомехи, и в этом случае пользователю может потребоваться принять надлежащие меры.

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

**Воздействие радиочастотного излучения.** Это устройство MikroTik должно быть установлено и эксплуатироваться не ближе 20 сантиметров от вашего тела, профессионального пользователя или широкой публики.

Производитель: Mikrotikls SIA, улица Унияс 2 Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Во избежание загрязнения окружающей среды необходимо отделить устройство от бытовых отходов и утилизировать его безопасным способом, например в специально отведенных местах. Ознакомьтесь с процедурами надлежащей транспортировки оборудования к специальным местам утилизации в вашем регионе.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве

Продукция MikroTik, поставляемая в Евразийский таможенный союз, оценивается согласно соответствующим требованиям и маркируется знаком EAC.

![](./img/image2020-1-24_7-55-5.badge-2.png)

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.7 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей короткий посібник стосується моделі: ATLGM&EG18-EA (ATL LTE18 kit)

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help-ua](https://mt.lv/help-ua)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/ukraina.badge.png)

**Перші кроки:**

- Відкрийте кришку для доступу до портів Ethernet;
- Вставте SIM-картку в слот відповідно до позначень на пристрої;
- Під’єднайте пристрій до PoE-інжектора, що входить до комплекту, за допомогою кабелю Ethernet до кінця передачі даних+живлення *"data+power"*;
- Підключіть кінець даних PoE-інжектора до комп’ютера;
- Підключіть адаптер живлення до PoE-інжектора;
- Налаштуйте свій пристрій за допомогою веб-браузера через *WebFig,* або інструменту *WinBox* [https://mt.lv/winbox](https://mt.lv/winbox); **існує декілька методів налаштування для забезпечення доступності;**
- Відкритйе адресу http://192.168.188.1 у *WebFig*, або перейдіть на вкладку *Neighbors* у *WinBox*, і натисніть на MAC-адресу. Ім’я користувача *"admin"* без пароля (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Клацніть кнопку "Check for updates" і оновіть RouterOS до останньої версії. Має бути вставлена дійсна SIM-карта і активне Інтернет-з'єднання;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" у WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- Встановіть пароль для вашого маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей продукт призначений для встановлення на вулиці на стовпі. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик.
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити — від’єднати адаптер електроживлення від розетки.
- Це продукт класу А. У домашніх умовах цей продукт може призвести до появи радіоперешкод, і в цьому випадку користувачеві може знадобитися вжити належних заходів.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

## UKCA marking

![](./img/ukca_black_fill.badge.png)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение ATLGM&EG18-EA е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení ATLGM&EG18-EA je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen ATLGM&EG18-EA er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp ATLGM&EG18-EA der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός ATLGM&EG18-EA πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type ATLGM&EG18-EA is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico ATLGM&EG18-EA es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp ATLGM&EG18-EA vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi ATLGM&EG18-EA on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type ATLGM&EG18-EA est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa ATLGM&EG18-EA u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a ATLGM&EG18-EA típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio ATLGM&EG18-EA è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að ATLGM&EG18-EA er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas ATLGM&EG18-EA atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta ATLGM&EG18-EA atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju ATLGM&EG18-EA huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur ATLGM&EG18-EA conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret ATLGM&EG18-EA er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego ATLGM&EG18-EA jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio ATLGM&EG18-EA está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio ATLGM&EG18-EA este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu ATLGM&EG18-EA je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme ATLGM&EG18-EA skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning ATLGM&EG18-EA överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products) |

## WCDMA/LTE

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      WCDMA Band I
      2100 MHz / 25dBm
    
    WCDMA Band III1800 MHz / 25dBm
    WCDMA Band VIII900 MHz / 24.5dBm
    LTE Band 12100 MHz / 24.5dBm
    LTE Band 31700 MHz / 24.5dBm
    LTE Band 72600 MHz / 24.5dBm
    LTE Band 8900 MHz / 24.5dBm
    LTE Band 20800 MHz / 24.5dBm
    LTE Band 28700 MHz / 24.5dBm
    LTE Band 382600 MHz / 24.5dBm
    LTE Band 402300 MHz / 24.5dBm
  

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Current, A

PoE In Ethernet Port (12 - 57 V DC)
24
0.8
IP54
-40°..+70°C

\#72755
