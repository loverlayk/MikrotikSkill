# Quick Guide G17-a - wAP LR8 kit

> Models: RBwAPR-2nD&R11e-LR8 (wAP LR8 kit)

**Models: RBwAPR-2nD&R11e-LR8 (wAP LR8 kit)**

![](./img/mt_logo_arrow_v2-02-47.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.11 or the latest version to ensure compliance with local authority regulations!

It is the end user's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
:::

*This is Wireless Network Device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-51.png)

*This Device accepts input from a 24V DC power adapter, which is provided in the original packaging of this device.*

**First steps:**

- Make sure your ISP is allowing hardware change and will issue an automatic IP address;
- Open the bottom lid;
- Connect an external antenna to the SMA connector;
- Connect the device to the power source;
- Connect your ISP cable to the Ethernet port;
- Navigate to the network connections section on your computer and locate the wireless network named *"MikroTik-..."*. Proceed to connect to it (check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/WinBox](https://mt.lv/WinBox); **multiple configuration methods are available to ensure accessibility;**
- Download and open *Winbox*, and choose the *Neighbors* tab to find the device;
- The default IP address is 192.168.88.1. Click on the IP address. If the IP is not available, use *Winbox* and connect using the MAC address. The username is *"admin"* and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the *WebFig or* *Winbox* *"Files"* menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the *"QuickSet"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field;
- Find *LR Gateway ID* on the label within the product and register it in your Network Server.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.11 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби, включително работата в рамките на законни честотни канали, извеждане на продукция изисквания за захранване, окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства на MikroTik трябва да бъдат професионално инсталиран.
:::

Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-50.png)

Това устройство приема вход на 24V DC адаптер за захранване, който се предлага в оригиналната опаковка на това устройство.

**Първи стъпки:**

- Уверете се, че вашият интернет доставчик позволява промяна на хардуера и ще издаде автоматичен IP адрес;
- Отворете долния капак;
- Свържете външна антена към SMA конектора;
- Свържете устройството към източника на захранване;
- Свържете вашия ISP кабел към Ethernet порта;
- Отидете до секцията за мрежови връзки на вашия компютър и намерете безжичната мрежа с име *"MikroTik-..."*. Продължете да се свързвате с него ( проверете безжичните пароли на стикера);
- Установете връзка чрез мобилно приложение. Алтернативно, използвайте WebFig в уеб браузър или инструмента за конфигуриране "WinBox" на [https://mt.lv/WinBox](https://mt.lv/WinBox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Изтеглете и отворете *Winbox* и изберете раздела *Neighbors*, за да намерите устройството;
- IP адресът по подразбиране е 192.168.88.1. Кликнете върху IP адреса. Ако IP не е наличен, използвайте *Winbox* и се свържете с MAC адреса. Потребителското име е *"admin"* и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Щракнете върху бутона *"Check for updates"* и актуализирайте RouterOS до най-новата версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто *WebFig или Winbox"Files"* и рестартирайте устройството;
- Чрез надграждане на софтуера на RouterOS до най-новата версия можете да осигурите оптимална производителност, стабилност и актуализации за сигурност;
- В менюто *"QuickSet"* настройте следното: Изберете вашата страна, за да приложите настройките за регулиране на страната;
- Настройте паролата за вашата безжична мрежа в лявото поле;
- Задайте паролата на вашия рутер в долното поле;
- Намерете *LR Gateway ID* на етикета в продукта и го регистрирайте във вашия мрежов сървър.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да бъде инсталиран на открито. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате правилния хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, в този случай от потребителя може да се наложи да предприеме адекватни мерки.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas iela 2, Рига, Латвия, LV1039.
## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.11 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupů požadavky na napájení, kabeláž a dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být profesionálně nainstalován.
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-50.png)

*Toto zařízení přijímá vstup 24 V DC napájecího adaptéru, který je součástí originálního balení tohoto zařízení.*

**První kroky:**

- Ujistěte se, že váš ISP povoluje hardwarovou změnu a vydá automatickou IP adresu;
- Otevřete spodní víko;
- Připojte externí anténu ke konektoru SMA;
- Připojte zařízení ke zdroji napájení;
- Připojte kabel ISP k portu Ethernet;
- Přejděte na svém počítači do části síťová připojení a vyhledejte bezdrátovou síť s názvem *"MikroTik-..."*. Pokračujte v připojení ( zkontrolujte hesla bezdrátového připojení na štítku);
- Vytvořte spojení pomocí mobilní aplikace. Alternativně můžete použít WebFig v webovém prohlížeči nebo nástroj pro konfiguraci "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Stáhněte a otevřete *Winbox* a vyberte kartu *Neighbors*, abyste našli zařízení;
- Výchozí IP adresa je 192.168.88.1. Klikněte na IP adresu. Pokud IP není k dispozici, použijte *Winbox* a připojte se pomocí MAC adresy. Uživatelské jméno je *"admin"* a není zde žádné heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Klikněte na tlačítko *"Check for updates"* a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do nabídky *WebFig nebo Winbox"Files"* a restartujte zařízení;
- Upgradováním softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce *"QuickSet"* nastavte následující: Vyberte svou zemi, chcete-li použít nastavení regulace země;
- V levém poli nastavte heslo bezdrátové sítě;
- Ve spodním poli nastavte heslo routeru;
- Najděte číslo *LR Gateway ID* na štítku v rámci produktu a zaregistrujte jej na svém síťovém serveru.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt lze instalovat venku. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete správný hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Abyste zabránili znečištění životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na určených místech. Seznamte se s postupy správné přepravy zařízení na určená sběrná místa ve vaší oblasti.
- Toto je výrobek třídy A. V domácím prostředí může tento výrobek způsobovat rušení rádiových vln. V takovém případě může být uživatel povinen přijmout odpovídající opatření.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.11 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler, herunder drift inden for lovlige frekvenskanaler, output strøm, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal være professionelt installeret.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-50.png)

*Denne enhed accepterer input fra 24V DC-strømadapter, der leveres i denne enheds originale emballage.*

**Første trin:**

- Sørg for, at din internetudbyder tillader hardwareændring og vil udstede en automatisk IP-adresse;
- Åbn bundlåget;
- Tilslut en ekstern antenne til SMA-stikket;
- Tilslut enheden til strømkilden;
- Tilslut dit ISP-kabel til Ethernet-porten;
- Naviger til afsnittet om netværksforbindelser på din computer, og find det trådløse netværk med navnet *"MikroTik-..."*. Fortsæt med at oprette forbindelse til den (tjek de trådløse adgangskoder på mærkaten);
- Opret forbindelse ved hjælp af en mobilapplikation. Alternativt kan du bruge WebFig i en webbrowser eller "WinBox" konfigurationsværktøjet på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Download og åbn *Winbox*, og vælg fanen *Neighbors* for at finde enheden;
- Standard IP-adressen er 192.168.88.1. Klik på IP-adressen. Hvis IP-adressen ikke er tilgængelig, skal du bruge *Winbox* og oprette forbindelse ved hjælp af MAC-adressen. Brugernavnet er *"admin"*, og der er ingen adgangskode (eller, for nogle modeller, tjek brugeradgangskoder og trådløse adgangskoder på mærkaten);
- Klik på knappen *"Check for updates"*, og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload downloadede pakker til menuen *WebFig eller Winbox"Files"* og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- I menuen *"QuickSet"* skal du indstille følgende: Vælg dit land for at anvende landereguleringsindstillinger;
- Indstil dit trådløse netværksadgangskode i venstre felt;
- Indstil din router-adgangskode i det nederste felt;
- Find *LR Gateway ID* på etiketten i produktet, og registrer den på din netværksserver.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt kan installeres udendørs. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den rigtige hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og beskadigelse af systemet.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- For at undgå forurening af miljøet skal apparatet adskilles fra husholdningsaffald og bortskaffes på en sikker måde, f.eks. I bestemte områder. Bliv fortrolig med procedurer til korrekt transport af udstyr til udpegede indsamlingssteder i dit område.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.11 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle und der Ausgabe Anforderungen an Stromversorgung, Verkabelung und dynamische Frequenzauswahl (Dynamic Frequency Selection, DFS). Alle MikroTik Funkgeräte müssen professionell installiert.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-50.png)

*Dieses Gerät akzeptiert den Eingang eines 24-V-Gleichstromadapters, das in der Originalverpackung dieses Geräts enthalten ist.*

**Erste Schritte:**

- Stellen Sie sicher, dass Ihr ISP Hardwareänderungen zulässt und eine automatische IP-Adresse vergibt;
- Öffne den unteren Deckel;
- Schließen Sie eine externe Antenne an den SMA-Anschluss an;
- Schließen Sie das Gerät an die Stromquelle an;
- Verbinden Sie Ihr ISP-Kabel mit dem Ethernet-Port;
- Navigieren Sie zum Abschnitt „Netzwerkverbindungen“ auf Ihrem Computer und suchen Sie das drahtlose Netzwerk mit dem Namen *"MikroTik-..."*. Stellen Sie eine Verbindung her (überprüfen Sie die WLAN-Passwörter auf dem Aufkleber);
- Stellen Sie eine Verbindung mit einer mobilen Anwendung her. Alternativ können Sie WebFig in einem Webbrowser oder das "WinBox" Konfigurationswerkzeug unter [https://mt.lv/WinBox](https://mt.lv/WinBox) verwenden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- *Laden Sie Winbox* herunter, öffnen Sie es und wählen Sie die Registerkarte *Neighbors*, um das Gerät zu finden;
- Die Standard-IP-Adresse ist 192.168.88.1. Klicken Sie auf die IP-Adresse. Wenn die IP nicht verfügbar ist, verwenden Sie *Winbox* und stellen Sie eine Verbindung über die MAC-Adresse her. Der Benutzername lautet *"admin"* und es gibt kein Passwort (oder überprüfen Sie bei einigen Modellen die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche *"Check for updates"* und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie heruntergeladene Pakete in das Menü *WebFig oder Winbox"Files"* hoch und starten Sie das Gerät neu;
- Durch ein Upgrade Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Richten Sie im Menü *"QuickSet"* Folgendes ein: Wählen Sie Ihr Land aus, um die länderspezifischen Regulierungseinstellungen anzuwenden;
- Richten Sie im linken Feld Ihr WLAN-Passwort ein;
- Richten Sie im unteren Feld Ihr Router-Passwort ein;
- Suchen Sie *LR Gateway ID* auf dem Etikett im Produkt und registrieren Sie es in Ihrem Netzwerkserver.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt kann im Freien installiert werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie nicht die richtige Hardware und Konfiguration verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zu Schäden am System führen.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Geräte zu bestimmten Sammelstellen in Ihrer Nähe vertraut.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.11 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών, συμπεριλαμβανομένης της λειτουργίας εντός των νόμιμων καναλιών συχνότητας, της παραγωγής ισχύ, απαιτήσεις καλωδίωσης και απαιτήσεις δυναμικής επιλογής συχνότητας (DFS). Όλες οι ασύρματες συσκευές MikroTik πρέπει να είναι επαγγελματικά εγκατεστημένο.
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-50.png)

*Αυτή η συσκευή δέχεται είσοδο τροφοδοτικού 24V DC, ο οποίος παρέχεται στην αρχική συσκευασία αυτής της συσκευής.*

**Πρώτα βήματα:**

- Βεβαιωθείτε ότι ο ISP σας επιτρέπει την αλλαγή υλικού και θα εκδώσει μια αυτόματη διεύθυνση IP.
- Ανοίξτε το κάτω καπάκι.
- Συνδέστε μια εξωτερική κεραία στην υποδοχή SMA.
- Συνδέστε τη συσκευή στην πηγή ρεύματος.
- Συνδέστε το καλώδιο ISP στη θύρα Ethernet.
- Μεταβείτε στην ενότητα συνδέσεις δικτύου στον υπολογιστή σας και εντοπίστε το ασύρματο δίκτυο με το όνομα *"MikroTik-..."*. Συνεχίστε να συνδεθείτε σε αυτό (ελέγξτε τους κωδικούς πρόσβασης ασύρματου δικτύου στο αυτοκόλλητο).
- Δημιουργήστε σύνδεση χρησιμοποιώντας μια κινητή εφαρμογή. Εναλλακτικά, μπορείτε να χρησιμοποιήσετε το WebFig σε έναν περιηγητή ή το εργαλείο διαμόρφωσης "WinBox" στη διεύθυνση [https://mt.lv/WinBox](https://mt.lv/WinBox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Κάντε λήψη και ανοίξτε το *Winbox* και επιλέξτε την καρτέλα *Neighbors* για να βρείτε τη συσκευή.
- Η προεπιλεγμένη διεύθυνση IP είναι 192.168.88.1. Κάντε κλικ στη διεύθυνση IP. Εάν η IP δεν είναι διαθέσιμη, χρησιμοποιήστε το *Winbox* και συνδεθείτε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι *"admin"* και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματης σύνδεσης στο αυτοκόλλητο).
- Κάντε κλικ στο κουμπί *"Check for updates"* και ενημερώστε το RouterOS στην πιο πρόσφατη έκδοση.
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού *WebFig ή Winbox"Files"* και επανεκκινήστε τη συσκευή.
- Αναβαθμίζοντας το λογισμικό RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας.
- Στο μενού *"QuickSet"* ρυθμίστε τα εξής: Επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις κανονισμού χώρας.
- Ρυθμίστε τον κωδικό πρόσβασης του ασύρματου δικτύου σας στο αριστερό πεδίο.
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο.
- Βρείτε το *LR Gateway ID* στην ετικέτα του προϊόντος και καταχωρίστε το στον διακομιστή δικτύου σας.

**Πληροφορίες για την ασφάλεια:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν μπορεί να εγκατασταθεί σε εξωτερικούς χώρους. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του σωστού υλικού και διαμόρφωσης ή η παρακολούθηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.
- Αυτό είναι ένα προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει ραδιοφωνικές παρεμβολές, οπότε ενδέχεται να απαιτείται από τον χρήστη να λάβει τα κατάλληλα μέτρα.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas iela 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.11 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales legales de frecuencia, salida alimentación, requisitos de cableado y requisitos de selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-50.png)

*Este dispositivo acepta la entrada del adaptador de alimentación de 24 V CC, que se proporciona en el embalaje original de este dispositivo.*

**Primeros pasos:**

- Asegúrese de que su ISP permita cambios de hardware y emita una dirección IP automática;
- Abra la tapa inferior;
- Conecte una antena externa al conector SMA;
- Conecte el dispositivo a la fuente de alimentación;
- Conecte el cable de su ISP al puerto Ethernet;
- Navegue hasta la sección de conexiones de red en su computadora y ubique la red inalámbrica llamada *"MikroTik-..."*. Proceda a conectarse (verifique las contraseñas inalámbricas en la etiqueta);
- Establecer una conexión mediante una aplicación móvil. Alternativamente, puede utilizar WebFig en un navegador web o la herramienta de configuración "WinBox" en [https://mt.lv/WinBox](https://mt.lv/WinBox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Descargue y abra *Winbox*, y elija la pestaña *Neighbors* para encontrar el dispositivo;
- La dirección IP predeterminada es 192.168.88.1. Haga clic en la dirección IP. Si la IP no está disponible, use *Winbox* y conéctese usando la dirección MAC. El nombre de usuario es *"admin"* y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Haga clic en el botón *"Check for updates"* y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú *WebFig o Winbox"Files"* y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento óptimo, estabilidad y actualizaciones de seguridad;
- En el menú *"QuickSet"* configure lo siguiente: Elija su país para aplicar la configuración de regulación del país;
- Configure la contraseña de su red inalámbrica en el campo izquierdo;
- Configure la contraseña de su enrutador en el campo inferior;
- Busque *LR Gateway ID* en la etiqueta del producto y regístrelo en su servidor de red.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto se puede instalar en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podría producir una situación peligrosa para las personas y dañar el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- El tomacorriente se instalará cerca del equipo y será de fácil acceso.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en las áreas designadas. Familiarícese con los procedimientos para transportar correctamente el equipo a los puntos de recolección designados en su área.
- Este es un producto de Clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso es posible que el usuario deba tomar las medidas adecuadas.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, protocolo 802.11b/g/n con antena PCB incorporada, ganancia máxima de 2 dBi.

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.11 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas toimimist seaduslikes sageduskanalites, väljund võimsus, kaabeldusnõuded ja dünaamilise sageduse valiku (DFS) nõuded. Kõik MikroTiku raadioseadmed peavad olema professionaalselt paigaldatud.
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-50.png)

*See seade aktsepteerib 24 V alalisvoolu adapteri sisendit, mis on esitatud selle seadme originaalpakendis.*

**Esimesed sammud:**

- Veenduge, et teie Interneti-teenuse pakkuja lubaks riistvara muutmist ja väljastab automaatse IP-aadressi;
- Avage alumine kaas;
- Ühendage väline antenn SMA-pistikuga;
- Ühendage seade toiteallikaga;
- Ühendage oma ISP-kaabel Etherneti porti;
- Liikuge arvutis võrguühenduste jaotisesse ja leidke traadita võrk nimega *"MikroTik-..."*. Jätkake sellega ühenduse loomist (kontrollige kleebis olevaid juhtmevabasid paroole);
- Looge ühendus mobiilirakenduse abil. Alternatiivselt saate kasutada WebFig'i veebibrauseris või "WinBox" konfiguratsioonitööriista aadressil [https://mt.lv/WinBox](https://mt.lv/WinBox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Laadige alla ja avage *Winbox* ning valige seadme leidmiseks vahekaart *Neighbors*;
- Vaikimisi IP-aadress on 192.168.88.1. Klõpsake IP-aadressil. Kui IP pole saadaval, kasutage *Winbox* ja looge MAC-aadressi abil. Kasutajanimi on *"admin"* ja parool puudub (või mõne mudeli puhul kontrollige kleebiselt kasutaja ja traadita ühenduse paroole);
- Klõpsake nuppu *"Check for updates"* ja värskendage RouterOS uusimale versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige allalaaditud paketid üles menüüsse *WebFig või Winbox"Files"* ja taaskäivitage seade;
- Uuendades oma RouterOS-i tarkvara uusimale versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Menüüs *"QuickSet"* seadistage järgmine: Valige riik, et rakendada riigi reguleerimise sätteid;
- Seadistage vasakpoolsel väljal traadita võrgu parool;
- Seadistage alumisel väljal ruuteri parool;
- Otsige toote etiketilt üles number *LR Gateway ID* ja registreerige see oma võrguserveris.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- Seda toodet saab paigaldada välistingimustes. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Õige riistvara ja konfiguratsiooni kasutamata jätmine või õigete protseduuride mittejärgimine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja utiliseerige see ohutult, näiteks selleks ettenähtud kohtades. Tutvuge seadmete nõuetekohase transportimise protseduuridega teie piirkonnas asuvatesse kogumispunktidesse.
- See on A -klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, mille korral võib kasutaja nõuda piisavate meetmete võtmist.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas iela 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.11 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtö teho, kaapelointivaatimukset ja dynaamisen taajuuden valinnan (DFS) vaatimukset. Kaikkien MikroTik-radiolaitteiden on oltava ammattimaisesti asennettu.
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-50.png)

*Tämä laite hyväksyy 24 V DC -virtasovittimen tulon, joka toimitetaan laitteen alkuperäispakkauksessa.*

**Ensiaskeleet:**

- Varmista, että Internet-palveluntarjoajasi sallii laitteiston muuttamisen ja antaa automaattisen IP-osoitteen.
- Avaa pohjakansi;
- Liitä ulkoinen antenni SMA-liittimeen;
- Liitä laite virtalähteeseen;
- Liitä ISP-kaapeli Ethernet-porttiin;
- Siirry tietokoneesi verkkoyhteydet-osioon ja etsi langaton verkko nimeltä *"MikroTik-..."*. Jatka yhteyden muodostamista siihen (tarkista tarrassa olevat langattomat salasanat);
- Muodosta yhteys käyttämällä mobiilisovellusta. Vaihtoehtoisesti voit käyttää WebFigiä selaimessa tai "WinBox" konfiguraatiotyökalua osoitteessa [https://mt.lv/WinBox](https://mt.lv/WinBox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Lataa ja avaa Winbox ja *etsi* laite valitsemalla *Neighbors-* välilehti;
- IP-oletusosoite on 192.168.88.1. Napsauta IP-osoitetta. Jos IP-osoite ei ole saatavilla, käytä *numeroa Winbox* ja muodosta yhteys MAC-osoitteen avulla. Käyttäjätunnus on *"admin"*, eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Napsauta *"Check for updates"-* painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit valikkoon *WebFig tai Winbox"Files"* ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja tietoturvapäivitykset;
- *"QuickSet"-* valikossa määritä seuraavat: Valitse maasi ottaaksesi käyttöön maakohtaiset asetukset;
- Aseta langattoman verkon salasana vasemmassa kentässä;
- Aseta reitittimen salasana alakenttään;
- Etsi *LR Gateway ID* tuotteen etiketistä ja rekisteröi se verkkopalvelimellesi.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote voidaan asentaa ulkona. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla esimerkiksi määrätyillä alueilla. Tutustu toimenpiteisiin, joilla laite kuljetetaan asianmukaisesti alueellesi määritettyihin keräyspisteisiin.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää voidaan joutua ryhtymään tarvittaviin toimenpiteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas iela 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.11 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la sortie les exigences d'alimentation, de câblage et de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installé professionnellement.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-50.png)

*Cet appareil accepte l'entrée d'un adaptateur d'alimentation 24 V CC, qui est fourni dans l'emballage d'origine de cet appareil.*

**Premiers pas:**

- Assurez-vous que votre FAI autorise le changement de matériel et émettra une adresse IP automatique;
- Ouvrez le couvercle inférieur;
- Connectez une antenne externe au connecteur SMA;
- Connectez l'appareil à la source d'alimentation;
- Connectez votre câble FAI au port Ethernet;
- Accédez à la section des connexions réseau sur votre ordinateur et localisez le réseau sans fil nommé *"MikroTik-..."*. Procédez à votre connexion (vérifiez les mots de passe sans fil sur l'autocollant);
- Établir une connexion à l'aide d'une application mobile. Vous pouvez également utiliser WebFig dans un navigateur Web ou l'outil de configuration "WinBox" à l'adresse [https://mt.lv/WinBox](https://mt.lv/WinBox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Téléchargez et ouvrez *Winbox*, puis choisissez l' onglet *Neighbors* pour trouver l'appareil;
- L'adresse IP par défaut est 192.168.88.1. Cliquez sur l'adresse IP. Si l'adresse IP n'est pas disponible, utilisez *Winbox* et connectez-vous en utilisant l'adresse MAC. Le nom d'utilisateur est *"admin"* et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton *"Check for updates"* et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu *WebFig ou Winbox"Files"* et redémarrez l'appareil;
- En mettant à niveau votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances, une stabilité et des mises à jour de sécurité optimales;
- Dans le menu *"QuickSet"*, configurez les éléments suivants: Choisissez votre pays pour appliquer les paramètres de réglementation du pays;
- Configurez le mot de passe de votre réseau sans fil dans le champ de gauche;
- Configurez le mot de passe de votre routeur dans le champ du bas;
- Recherchez *LR Gateway ID* sur l'étiquette du produit et enregistrez-le sur votre serveur réseau.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit peut être installé à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration appropriés ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Pour éviter la contamination de l'environnement, séparez l'appareil des déchets ménagers et éliminez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.
- Il s'agit d'un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas iela 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.11 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala zahtjevi za napajanje, kabliranje i zahtjevi za dinamički odabir frekvencije (DFS). Svi MikroTik radijski uređaji moraju biti profesionalno instaliran.
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-50.png)

*Ovaj uređaj prihvaća ulaz 24-strujnog mrežnog adaptera, koji je isporučen u originalnom pakiranju ovog uređaja.*

**Prvi koraci:**

- Provjerite dopušta li vaš ISP promjenu hardvera i da će izdati automatsku IP adresu;
- Otvorite donji kapak;
- Spojite vanjsku antenu na SMA konektor;
- Spojite uređaj na izvor napajanja;
- Spojite ISP kabel na Ethernet port;
- Dođite do odjeljka mrežnih veza na računalu i pronađite bežičnu mrežu pod nazivom *"MikroTik-..."*. Nastavite s povezivanjem s njim (provjerite bežične lozinke na naljepnici);
- Uspostavite vezu pomoću mobilne aplikacije. Opcionalno, koristite WebFig u web pregledniku ili alat za konfiguraciju "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Preuzmite i otvorite *Winbox* i odaberite karticu *Neighbors* kako biste pronašli uređaj;
- Zadana IP adresa je 192.168.88.1. Kliknite na IP adresu. Ako IP nije dostupan, koristite *Winbox* i povežite se pomoću MAC adrese. Korisničko ime je *"admin"* i nema zaporke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Pritisnite gumb *"Check for updates"* i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u izbornik *WebFig ili Winbox"Files"* i ponovno pokrenite uređaj;
- Nadogradnjom vašeg RouterOS softvera na najnoviju verziju, možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U izborniku *"QuickSet"* postavite sljedeće: Odaberite svoju zemlju za primjenu postavki propisa zemlje;
- U lijevom polju postavite lozinku bežične mreže;
- Postavite lozinku usmjerivača u donjem polju;
- Pronađite *LR Gateway ID* na naljepnici unutar proizvoda i registrirajte ga na svom mrežnom poslužitelju.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj se proizvod može instalirati na otvorenom. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne poštujete ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Da biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na za to predviđena mjesta. Upoznajte se s postupcima pravilnog transporta opreme do određenih sabirnih mjesta u vašem području.
- Ovo je proizvod klase A. U kućnom okruženju ovaj proizvod može uzrokovati radio smetnje, u tom slučaju od korisnika se može zahtijevati da poduzme odgovarajuće mjere.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.11-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon keresztüli működést is teljesítményre, kábelezésre és dinamikus frekvenciaválasztásra (DFS) vonatkozó követelmények. Az összes MikroTik rádiókészüléknek lennie kell szakszerűen telepítve.
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-50.png)

*Ez az eszköz elfogadja a 24 V-os egyenáramú adapter bemeneti adatait, amely a készülék eredeti csomagolásában található.*

**Első lépések:**

- Győződjön meg arról, hogy internetszolgáltatója engedélyezi a hardvercserét, és automatikus IP-címet ad ki;
- Nyissa ki az alsó fedelet;
- Csatlakoztasson egy külső antennát az SMA csatlakozóhoz;
- Csatlakoztassa a készüléket az áramforráshoz;
- Csatlakoztassa az ISP-kábelt az Ethernet-porthoz;
- Keresse meg számítógépén a hálózati kapcsolatok szakaszt, és keresse meg a *"MikroTik-..."* nevű vezeték nélküli hálózatot. Folytassa a csatlakozással (ellenőrizze a vezeték nélküli jelszavakat a matricán);
- Kapcsolat létesítése mobilalkalmazás segítségével. Vagy használja a WebFig-et egy webböngészőben vagy a "WinBox" konfigurációs eszközt a [https://mt.lv/WinBox](https://mt.lv/WinBox) címen; **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Töltse le és nyissa meg *a Winbox-at*, majd válassza ki a *Neighbors* lapot az eszköz megkereséséhez;
- Az alapértelmezett IP-cím 192.168.88.1. Kattintson az IP-címre. Ha az IP nem elérhető, használja *a Winbox-at*, és csatlakozzon a MAC-cím használatával. A felhasználónév *"admin"*, és nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a *"Check for updates"* gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a *WebFig vagy Winbox"Files"* menübe, és indítsa újra az eszközt;
- A RouterOS szoftverének a legújabb verzióra való frissítésével optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- A *"QuickSet"* menüben állítsa be a következőket: Válassza ki az országot az országszabályozási beállítások alkalmazásához;
- Állítsa be vezeték nélküli hálózati jelszavát a bal oldali mezőben;
- Állítsa be az útválasztó jelszavát az alsó mezőben;
- Keresse meg az *LR Gateway ID*-t a termék címkéjén, és regisztrálja a hálózati kiszolgálón.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ez a termék kültéren is telepíthető. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helytelen hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását okozhatja.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- A környezet szennyeződésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon dobja el, például a kijelölt területekre. Ismerje meg a berendezés megfelelő szállítási eljárásait a környéken található gyűjtőhelyekre.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználónak meg kell tennie a megfelelő intézkedéseket.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas iela 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan Cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.11 atau versi terbaru untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Pengguna akhir bertanggung jawab untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya keluaran, persyaratan perkabelan, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat radio MikroTik harus diinstal secara profesional.
:::

*Ini adalah Perangkat Jaringan Nirkabel. Anda dapat menemukan nama model produk pada label casing (ID).*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um](https://mt.lv/um) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis, brosur, dan info lebih lanjut mengenai produk di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [https://mt.lv/help](https://mt.lv/help)*
*Perangkat MikroTik ditujukan untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi silakan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/indonesian.badge-20.png)

*Perangkat ini menerima input dari adaptor daya 24V DC, yang disediakan dalam kemasan asli perangkat ini.*

**Langkah pertama:**

- Pastikan ISP Anda mengizinkan perubahan perangkat keras dan akan mengeluarkan alamat IP otomatis;
- Buka tutup bawah;
- Hubungkan antena eksternal ke konektor SMA;
- Hubungkan perangkat ke sumber listrik;
- Hubungkan kabel ISP Anda ke port Ethernet;
- Navigasikan ke bagian koneksi jaringan di komputer Anda dan temukan jaringan nirkabel bernama "*MikroTik*-...". Lanjutkan untuk menyambungkannya (periksa kata sandi nirkabel pada stiker);
- Buat koneksi menggunakan aplikasi seluler. Alternatifnya, gunakan WebFig di browser web atau alat konfigurasi "WinBox" di [https://mt.lv/WinBox](https://mt.lv/WinBox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Download dan buka *Winbox*, dan pilih tab *Neighbors* untuk menemukan perangkat;
- Alamat IP defaultnya adalah 192.168.88.1. Klik pada alamat IP. Jika IP tidak tersedia, gunakan *Winbox* dan sambungkan menggunakan alamat MAC. Nama penggunanya adalah "*admin*" dan tidak ada sandi (atau, untuk beberapa model, periksa sandi pengguna dan nirkabel pada stiker);
- Klik tombol "*Check for updates*" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu *WebFig* atau *Winbox*"*Files*" dan reboot perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Di menu "*QuickSet*" siapkan hal berikut: Pilih negara Anda, untuk menerapkan setelan peraturan negara;
- Atur kata sandi jaringan nirkabel Anda di kolom kiri;
- Atur kata sandi router Anda di kolom bawah;
- Temukan *ID LR Gateway* pada label di dalam produk dan daftarkan di Server Jaringan Anda.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, yang dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dapat dipasang di luar ruangan. Harap baca petunjuk pemasangan dengan cermat sebelum memulai pemasangan. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem.
- Stopkontak harus dipasang di dekat peralatan dan mudah dijangkau.
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut adaptor daya dari stopkontak.
- Untuk menghindari kontaminasi terhadap lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan cara yang aman, misalnya di tempat yang telah ditentukan. Pahami prosedur pengangkutan peralatan dengan benar ke tempat pengumpulan yang ditentukan di wilayah Anda.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai

**Paparan Radiasi Frekuensi Radio**: Peralatan MikroTik ini mematuhi batas paparan radiasi Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini sebaiknya dipasang dan dioperasikan tidak lebih dekat dari 20 sentimeter dari tubuh Anda, pengguna pekerjaan, atau masyarakat umum.

Pabrikan: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.11 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali, incluso il funzionamento nei canali di frequenza legali, in uscita requisiti di alimentazione, cablaggio e selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installato professionalmente.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-50.png)

*Questo dispositivo accetta l'ingresso dell'alimentatore 24 V CC, fornito nella confezione originale di questo dispositivo.*

**Primi passi:**

- Assicurati che il tuo ISP consenta la modifica dell'hardware e rilasci un indirizzo IP automatico;
- Aprire il coperchio inferiore;
- Collegare un'antenna esterna al connettore SMA;
- Collegare il dispositivo alla fonte di alimentazione;
- Collega il cavo del tuo ISP alla porta Ethernet;
- Passare alla sezione delle connessioni di rete sul computer e individuare la rete wireless denominata *"MikroTik-..."*. Procedere alla connessione (controllare le password wireless sull'adesivo);
- Stabilire una connessione tramite un'applicazione mobile. In alternativa, utilizza WebFig in un browser web o lo strumento di configurazione "WinBox" all'indirizzo [https://mt.lv/WinBox](https://mt.lv/WinBox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Scarica e apri *Winbox* e scegli la scheda *Neighbors* per trovare il dispositivo;
- L'indirizzo IP predefinito è 192.168.88.1. Fare clic sull'indirizzo IP. Se l'IP non è disponibile, utilizzare *Winbox* e connettersi utilizzando l'indirizzo MAC. Il nome utente è *"admin"* e non è presente alcuna password (o, per alcuni modelli, verificare utente e password wireless sull'adesivo);
- Fare clic sul pulsante *"Check for updates"* e aggiornare RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu *WebFig o Winbox"Files"* e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni, stabilità e aggiornamenti di sicurezza ottimali;
- Nel menu *"QuickSet"* imposta quanto segue: Scegli il tuo paese, per applicare le impostazioni della regolamentazione nazionale;
- Imposta la password della tua rete wireless nel campo a sinistra;
- Imposta la password del tuo router nel campo in basso;
- Trova *LR Gateway ID* sull'etichetta all'interno del prodotto e registralo nel tuo server di rete.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto può essere installato all'aperto. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Se non si utilizza l'hardware e la configurazione corretti o si seguono le procedure corrette, si potrebbero verificare situazioni pericolose per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio, in aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura ai punti di raccolta designati nella propria zona.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso l'utente potrebbe essere tenuto ad adottare misure adeguate.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas iela 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.11 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum, þar með talið rekstri innan löglegra tíðnisviða, framleiðsla afl, kaðall kröfur og Dynamic Frequency Val (DFS) kröfur. Öll MikroTik útvarpstæki verða að vera faglega sett upp.
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-50.png)

*Þetta tæki tekur við inngangi 24V DC rafmagns millistykki sem er að finna í upprunalegum umbúðum þessa tækis.*

**Fyrstu skrefin:**

- Gakktu úr skugga um að ISP þinn leyfi vélbúnaðarbreytingar og gefi út sjálfvirka IP tölu;
- Opnaðu botnlokið;
- Tengdu ytra loftnet við SMA tengið;
- Tengdu tækið við aflgjafa;
- Tengdu ISP snúruna við Ethernet tengið;
- Farðu í nettengingarhlutann á tölvunni þinni og finndu þráðlausa netið sem heitir *"MikroTik-...".* Haltu áfram að tengjast því (athugaðu þráðlausu lykilorðin á límmiðanum);
- Búið til tengingu með því að nota farsímaforrit. Eða notaðu WebFig í vafra eða stilliverkfærið "WinBox" á [https://mt.lv/WinBox](https://mt.lv/WinBox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Sæktu og opnaðu *Winbox* og veldu *Neighbors* flipann til að finna tækið;
- Sjálfgefið IP-tala er 192.168.88.1. Smelltu á IP töluna. Ef IP er ekki tiltækt, notaðu *Winbox* og tengdu með MAC vistfanginu. Notandanafnið er *"admin"* og það er ekkert lykilorð (eða, fyrir sumar gerðir, athugaðu notanda og þráðlausa lykilorð á límmiðanum);
- Smelltu á *"Check for updates"* hnappinn og uppfærðu RouterOS í nýjustu útgáfuna;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hladdu niður niðurhaluðum pakka í *WebFig eða Winbox"Files"* valmyndina og endurræstu tækið;
- Með því að uppfæra RouterOS hugbúnaðinn þinn í nýjustu útgáfuna geturðu tryggt hámarksafköst, stöðugleika og öryggisuppfærslur;
- Í *"QuickSet"* valmyndinni skaltu setja upp eftirfarandi: Veldu land þitt, til að beita landsreglustillingum;
- Settu upp lykilorðið þitt fyrir þráðlausa netið í vinstri reitnum;
- Settu upp lykilorðið þitt fyrir leiðina í neðsta reitnum;
- Finndu *LR Gateway ID* á merkimiðanum innan vörunnar og skráðu það á netþjóninn þinn.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Hægt er að setja þessa vöru utandyra. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Bilun í að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti valdið hættulegum aðstæðum fyrir fólk og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Til að koma í veg fyrir mengun umhverfisins skaltu aðskilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur til að flytja búnaðinn rétt til tilnefndra söfnunarstaða á þínu svæði.
- Þetta er vara í flokki A. Í heimalandi umhverfi gæti þessi vara valdið truflunum á útvarpi, en þá gæti þurft að gera notandann viðeigandi ráðstafanir.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas iela 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.11 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter, inkludert drift innen lovlige frekvenskanaler, output strøm, kabling og krav til dynamisk frekvensvalg (DFS). Alle MikroTik-radioenheter må være profesjonelt installert.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-50.png)

*Denne enheten godtar inngangen til 24V DC-strømadapter, som følger med originalemballasjen til denne enheten.*

**Første steg:**

- Sørg for at Internett-leverandøren din tillater maskinvareendringer og vil utstede en automatisk IP-adresse;
- Åpne bunnlokket;
- Koble en ekstern antenne til SMA-kontakten;
- Koble enheten til strømkilden;
- Koble ISP-kabelen til Ethernet-porten;
- Naviger til delen for nettverkstilkoblinger på datamaskinen og finn det trådløse nettverket som heter *"MikroTik-..."*. Fortsett å koble til den (sjekk de trådløse passordene på klistremerket);
- Opprett forbindelse ved hjelp av en mobilapplikasjon. Alternativt kan du bruke WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Last ned og åpne *Winbox*, og velg *Neighbors-* fanen for å finne enheten;
- Standard IP-adresse er 192.168.88.1. Klikk på IP-adressen. Hvis IP-en ikke er tilgjengelig, bruk *Winbox* og koble til med MAC-adressen. Brukernavnet er *"admin"* og det er ikke noe passord (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- Klikk på *"Check for updates"-* knappen og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last ned nedlastede pakker til *WebFig eller Winbox"Files"-* menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I *"QuickSet"-* menyen konfigurerer du følgende: Velg ditt land for å bruke landreguleringsinnstillinger;
- Sett opp passordet for det trådløse nettverket i venstre felt;
- Sett opp ruterpassordet ditt i det nederste feltet;
- Finn *LR Gateway ID* på etiketten i produktet og registrer den i nettverksserveren.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet kan installeres utendørs. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på systemet.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- For å unngå forurensning av miljøet, må du skille enheten fra husholdningsavfall og kaste den på en sikker måte, for eksempel i bestemte områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.
- Dette er et klasse A -produkt. I et hjemmemiljø kan dette produktet forårsake radioforstyrrelser. I så fall kan det være nødvendig at brukeren tar nødvendige tiltak.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.11“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi, įskaitant veikimą legaliais dažnių kanalais galios, kabelių ir dinaminio dažnio pasirinkimo (DFS) reikalavimai. Visi „MikroTik“ radijo prietaisai turi būti profesionaliai sumontuota.
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-50.png)

*Šis įrenginys priima 24 V nuolatinės srovės maitinimo adapterį, pateiktą originalioje šio prietaiso pakuotėje.*

**Pirmieji žingsniai:**

- Įsitikinkite, kad jūsų IPT leidžia keisti aparatinę įrangą ir išduos automatinį IP adresą;
- Atidarykite apatinį dangtį;
- Prijunkite išorinę anteną prie SMA jungties;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Prijunkite savo IPT kabelį prie Ethernet prievado;
- Kompiuteryje eikite į tinklo ryšių skyrių ir suraskite belaidį tinklą, pavadintą *"MikroTik-..."*. Prisijunkite prie jo (patikrinkite belaidžio ryšio slaptažodžius ant lipduko);
- Sukurkite ryšį naudodami mobilųjį programėlę. Alternatyviai naudokite WebFig naršyklėje arba konfigūracijos įrankį "WinBox" adresu [https://mt.lv/WinBox](https://mt.lv/WinBox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atsisiųskite ir atidarykite *Winbox* ir pasirinkite skirtuką *Neighbors*, kad surastumėte įrenginį;
- Numatytasis IP adresas yra 192.168.88.1. Spustelėkite IP adresą. Jei IP nėra, naudokite *Winbox* ir prisijunkite naudodami MAC adresą. Vartotojo vardas yra *"admin"* ir nėra slaptažodžio (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Spustelėkite mygtuką *"Check for updates"* ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkelkite atsisiųstus paketus į *WebFig arba Winbox"Files"* meniu ir perkraukite įrenginį;
- Atnaujinę RouterOS programinę įrangą į naujausią versiją, galite užtikrinti optimalų našumą, stabilumą ir saugos naujinimus;
- *"QuickSet"* meniu nustatykite šiuos veiksmus: Pasirinkite šalį, kad būtų taikomi šalies reguliavimo nustatymai;
- Kairiajame lauke nustatykite belaidžio tinklo slaptažodį;
- Apatiniame lauke nustatykite maršrutizatoriaus slaptažodį;
- Gaminio etiketėje raskite *LR Gateway ID* ir užregistruokite jį savo tinklo serveryje.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šį gaminį galima montuoti lauke. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite tinkamos aparatinės įrangos ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Kad išvengtumėte aplinkos užteršimo, atskirkite prietaisą nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trukdžius, todėl vartotojas gali imtis atitinkamų priemonių.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas iela 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.11 vai jaunāku versiju, lai nodrošinātu atbilstību vietējās likumdošanas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt profesionāli uzstādītām.
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-50.png)

*Šī darbojas ar 24 V līdzstrāvas barošanas adapteri, kas ir atrodas šīs ierīces oriģinālajā iepakojumā.*

**Pirmie soļi:**

- Pārliecinieties, vai jūsu ISP atļauj aparatūras maiņu un izsniegs automātisku IP adresi;
- Atveriet apakšējo vāku;
- Pievienojiet ārējo antenu SMA savienotājam;
- Pievienojiet ierīci strāvas avotam;
- Pievienojiet ISP kabeli Ethernet portam;
- Datorā atveriet tīkla savienojumus un meklējiet MikroTik bezvadu tīklu *"MikroTik-..."*. Turpiniet, un ar to izveidojiet savienojumu (atrodiet bezvadu tīklaparoli uz uzlīmes);
- Izveidojiet savienojumu, izmantojot mobilās lietotnes. Kā alternatīvu varat izmantot WebFig pārlūkprogrammā vai konfigurācijas rīku "WinBox" vietnē [https://mt.lv/WinBox](https://mt.lv/WinBox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Lejupielādējiet un atveriet *Winbox* un izvēlieties cilni *Neighbors*, lai atrastu ierīci;
- Noklusējuma IP adrese ir 192.168.88.1. Noklikšķiniet uz IP adreses. Ja IP nav pieejams, izmantojiet *Winbox* un izveidojiet savienojumu, izmantojot MAC adresi. Lietotājvārds ir *"admin"* un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas *Check for updates* un atjauniniet savu RouterOS programmatūru uz jaunāko versiju;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakas izvēlnē *WebFig* vai Winbox *"Files"* un restartējiet ierīci;
- RouterOS programmatūras atjaunināšana uz jaunāko versiju nodrošinās vislabāko veiktspēju, stabilitāti un drošību;
- Izvēlnē *"QuickSet"* iestatiet zemāk minētās leitas: Izvēlieties valsti, lai lietotu valsts likumā paredzētos iestatījumus;
- Kreisajā laukā iestatiet bezvadu tīkla paroli;
- Apakšējā laukā iestatiet maršrutētāja paroli;
- Atrodiet *LR Gateway ID* uz izstrādājuma etiķetes un reģistrējiet to savā tīkla serverī.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šo izstrādājumu var uzstādīt ārpus telpām. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Pareiza aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.
- Šis ir A klases produkts. Sadzīves vidē šis produkts var izraisīt radio traucējumus, tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas iela 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.11 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż l-operazzjoni fil-kanali tal-frekwenza legali, tal-ħruġ qawwa, ħtiġiet ta 'kejbils, u Reklamar ta' Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom ikunu installat professjonalment.
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-50.png)

*Dan l-Apparat jaċċetta input ta ’24V DC adapter power, li huwa pprovdut fl-imballaġġ oriġinali ta’ dan l-apparat.*

**L-ewwel passi:**

- Kun żgur li l-ISP tiegħek qed jippermetti bidla fil-ħardwer u se joħroġ indirizz IP awtomatiku;
- Iftaħ l-għatu tal-qiegħ;
- Qabbad antenna esterna mal-konnettur SMA;
- Qabbad l-apparat mas-sors tal-enerġija;
- Qabbad il-kejbil ISP tiegħek mal-port Ethernet;
- Innaviga lejn is-sezzjoni tal-konnessjonijiet tan-netwerk fuq il-kompjuter tiegħek u sib in-netwerk bla fili bl-isem *"MikroTik-..."*. Ipproċedi biex tikkonnettja magħha (iċċekkja l-passwords mingħajr fili fuq l-istiker);
- Ewlenija bl-użu ta 'applikazzjoni mobbli. Bħala alternattiva, uża l-WebFig f'browser jew l-għodda ta' konfigurazzjoni "WinBox" fuq [https://mt.lv/WinBox](https://mt.lv/WinBox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Niżżel u tiftaħ *Winbox*, u agħżel it- tab *Neighbors* biex issib l-apparat;
- L-indirizz IP default huwa 192.168.88.1. Ikklikkja fuq l-indirizz IP. Jekk l-IP ma jkunx disponibbli, uża *Winbox* u qabbad billi tuża l-indirizz MAC. L-isem tal-utent huwa *"admin"* u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u mingħajr fili fuq l-istiker);
- Ikklikkja l -buttuna *"Check for updates"* u aġġorna RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Tella' pakketti mniżżla fil- menu *WebFig jew Winbox"Files"* u reboot l-apparat;
- Billi taġġorna s-softwer RouterOS tiegħek għall-aħħar verżjoni, tista 'tiżgura l-aħjar prestazzjoni, stabbiltà u aġġornamenti tas-sigurtà;
- Fil- menu *"QuickSet"* waqqaf dan li ġej: Agħżel pajjiżek, biex tapplika s-settings tar-regolamentazzjoni tal-pajjiż;
- Issettja l-password tan-netwerk bla fili tiegħek fil-qasam tax-xellug;
- Issettja l-password tar-router tiegħek fil-qasam t'isfel;
- Sib *LR Gateway ID* fuq it-tikketta fi ħdan il-prodott u rreġistraha fis-Netwerk Server tiegħek.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott jista 'jiġi installat barra. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Jekk tonqos milli tuża l-hardware u l-konfigurazzjoni korretti jew issegwi l-proċeduri t-tajba tista ’tirriżulta f’sitwazzjoni perikoluża għan-nies u ħsara fis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza tar-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas iela 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.11 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften, inclusief werking binnen wettelijke frequentiekanalen, te volgen vermogen, bekabelingseisen en Dynamic Frequency Selection (DFS) -vereisten. Alle MikroTik-radioapparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-50.png)

*Dit apparaat accepteert invoer van een 24V DC-voedingsadapter, die wordt geleverd in de originele verpakking van dit apparaat.*

**Eerste stappen:**

- Zorg ervoor dat uw ISP hardwarewijzigingen toestaat en automatisch een IP-adres verstrekt;
- Open het onderste deksel;
- Sluit een externe antenne aan op de SMA-connector;
- Sluit het apparaat aan op de stroombron;
- Sluit uw ISP-kabel aan op de Ethernet-poort;
- Navigeer naar het gedeelte Netwerkverbindingen op uw computer en zoek het draadloze netwerk met de naam *"MikroTik-..."*. Ga verder met het verbinden (controleer de draadloze wachtwoorden op de sticker);
- Maak verbinding met behulp van een mobiele applicatie. Als alternatief kunt u WebFig gebruiken in een webbrowser of het configuratiehulpmiddel "WinBox" op [https://mt.lv/WinBox](https://mt.lv/WinBox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Download en open *Winbox* en kies het tabblad *Neighbors* om het apparaat te vinden;
- Het standaard IP-adres is 192.168.88.1. Klik op het IP-adres. Als het IP-adres niet beschikbaar is, gebruikt u *Winbox* en maakt u verbinding via het MAC-adres. De gebruikersnaam is *"admin"* en er is geen wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop *"Check for updates"* en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het menu *WebFig of Winbox"Files"* en start het apparaat opnieuw op;
- Door uw RouterOS-software te upgraden naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- In het *"QuickSet"-* menu stelt u het volgende in: Kies uw land om de landregelgevingsinstellingen toe te passen;
- Stel uw draadloze netwerkwachtwoord in het linkerveld in;
- Stel uw routerwachtwoord in het onderste veld in;
- Zoek *LR Gateway ID* op het etiket in het product en registreer het in uw netwerkserver.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product kan buitenshuis worden geïnstalleerd. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Het stopcontact moet in de buurt van de apparatuur worden geïnstalleerd en moet gemakkelijk toegankelijk zijn.
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.
- Dit is een klasse A-product. In een huiselijke omgeving kan dit product radiostoring veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen moet nemen.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.11 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości wymagania dotyczące zasilania, okablowania i dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być profesjonalnie zainstalowany.
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-50.png)

*To urządzenie akceptuje wejście zasilacza 24 V DC, który jest dostarczany w oryginalnym opakowaniu tego urządzenia.*

**Pierwsze kroki:**

- Upewnij się, że Twój dostawca usług internetowych pozwala na zmianę sprzętu i automatycznie przydzieli adres IP;
- Otwórz dolną pokrywę;
- Podłącz antenę zewnętrzną do złącza SMA;
- Podłącz urządzenie do źródła zasilania;
- Podłącz kabel ISP do portu Ethernet;
- Przejdź do sekcji połączeń sieciowych na swoim komputerze i zlokalizuj sieć bezprzewodową o nazwie *"MikroTik-..."*. Kontynuuj połączenie z nim (sprawdź hasła sieci bezprzewodowej na naklejce);
- Utwórz połączenie za pomocą aplikacji mobilnej. Alternatywnie użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox" pod adresem [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Pobierz i otwórz *Winbox* i wybierz zakładkę *Neighbors*, aby znaleźć urządzenie;
- Domyślny adres IP to 192.168.88.1. Kliknij adres IP. Jeśli adres IP nie jest dostępny, użyj *Winbox* i połącz się przy użyciu adresu MAC. Nazwa użytkownika to *"admin"* i nie ma hasła (lub, w przypadku niektórych modeli, sprawdź hasło użytkownika i hasło sieci bezprzewodowej na naklejce);
- Kliknij przycisk *"Check for updates"* i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Prześlij pobrane pakiety do menu *WebFig lub Winbox"Files"* i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, możesz zapewnić optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu *"QuickSet"* skonfiguruj następujące opcje: Wybierz swój kraj, aby zastosować ustawienia przepisów krajowych;
- Ustaw hasło do sieci bezprzewodowej w lewym polu;
- Ustaw hasło routera w dolnym polu;
- Znajdź numer *LR Gateway ID* na etykiecie produktu i zarejestruj go na serwerze sieciowym.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt można zainstalować na zewnątrz. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie prawidłowego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- Gniazdko powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w którym to przypadku użytkownik może być zobowiązany do podjęcia odpowiednich środków.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas iela 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.11 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais de frequência legal, saída requisitos de alimentação, cabeamento e Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalado profissionalmente.
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-50.png)

*Este dispositivo aceita a entrada do adaptador de energia de 24 Vcc, fornecido na embalagem original deste dispositivo.*

**Primeiros passos:**

- Certifique-se de que seu ISP esteja permitindo alterações de hardware e emitirá um endereço IP automático;
- Abra a tampa inferior;
- Conecte uma antena externa ao conector SMA;
- Conecte o dispositivo à fonte de alimentação;
- Conecte seu cabo ISP à porta Ethernet;
- Navegue até a seção de conexões de rede em seu computador e localize a rede sem fio chamada *"MikroTik-..."*. Prossiga para se conectar a ele (verifique as senhas wireless no adesivo);
- Estabelecer uma conexão usando um aplicativo móvel. Alternativamente, use o WebFig em um navegador da web ou a ferramenta de configuração "WinBox" em [https://mt.lv/WinBox](https://mt.lv/WinBox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Baixe e abra *Winbox* e escolha a aba *Neighbors* para encontrar o dispositivo;
- O endereço IP padrão é 192.168.88.1. Clique no endereço IP. Se o IP não estiver disponível, use *Winbox* e conecte-se usando o endereço MAC. O nome de usuário é *"admin"* e não há senha (ou, para alguns modelos, verifique as senhas de usuário e wireless no adesivo);
- Clique no botão *"Check for updates"* e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Carregue os pacotes baixados no menu *WebFig ou Winbox"Files"* e reinicie o dispositivo;
- Ao atualizar o software RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- No menu *"QuickSet"* configure o seguinte: Escolha o seu país, para aplicar as configurações de regulamentação do país;
- Configure a senha da sua rede wireless no campo esquerdo;
- Configure a senha do seu roteador no campo inferior;
- Encontre o *LR Gateway ID* na etiqueta do produto e registre-o em seu servidor de rede.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto pode ser instalado ao ar livre. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- A tomada deve ser instalada próxima ao equipamento e deve ser de fácil acesso.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.
- Este é um produto de Classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio, caso em que o usuário pode ser obrigado a tomar as medidas adequadas.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.11 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale cerințe de alimentare, cabluri și cerințe de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie să fie instalat profesional.
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-50.png)

*Acest dispozitiv acceptă introducerea adaptorului de curent continuu de 24V DC, care este prevăzut în ambalajul original al acestui dispozitiv.*

**Primii pasi:**

- Asigurați-vă că ISP-ul dvs. permite schimbarea hardware-ului și va emite o adresă IP automată;
- Deschideți capacul inferior;
- Conectați o antenă externă la conectorul SMA;
- Conectați dispozitivul la sursa de alimentare;
- Conectați cablul ISP la portul Ethernet;
- Navigați la secțiunea de conexiuni la rețea de pe computer și localizați rețeaua fără fir numită *"MikroTik-..."*. Continuați să vă conectați la acesta (verificați parolele wireless de pe autocolant);
- Stabiliți o conexiune folosind o aplicație mobilă. Alternativ, utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox" la [https://mt.lv/WinBox](https://mt.lv/WinBox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Descărcați și deschideți *Winbox* și alegeți fila *Neighbors* pentru a găsi dispozitivul;
- Adresa IP implicită este 192.168.88.1. Faceți clic pe adresa IP. Dacă IP-ul nu este disponibil, utilizați *Winbox* și conectați-vă folosind adresa MAC. Numele de utilizator este *"admin"* și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless pe autocolant);
- Faceți clic pe butonul *"Check for updates"* și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul *WebFig sau Winbox"Files"* și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanță optimă, stabilitate și actualizări de securitate;
- În meniul *"QuickSet"* configurați următoarele: Alegeți țara, pentru a aplica setările de reglementare a țării;
- Configurați parola rețelei wireless în câmpul din stânga;
- Configurați parola routerului în câmpul de jos;
- Găsiți *LR Gateway ID* pe eticheta produsului și înregistrați-l pe serverul de rețea.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs poate fi instalat în aer liber. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-le într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător al echipamentelor la punctele de colectare desemnate din zona dumneavoastră.
- Acesta este un produs de clasa A. Într-un mediu casnic, acest produs ar putea provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.11 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny, vrátane prevádzky v rámci legálnych frekvenčných kanálov a výstupov požiadavky na energiu, kabeláž a dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť profesionálne nainštalovaný.
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-50.png)

*Toto zariadenie prijíma vstup 24V DC napájacieho adaptéra, ktorý je súčasťou originálneho balenia tohto zariadenia.*

**Prvé kroky:**

- Uistite sa, že váš ISP povoľuje zmenu hardvéru a vydá automatickú IP adresu;
- Otvorte spodné veko;
- Pripojte externú anténu ku konektoru SMA;
- Pripojte zariadenie k zdroju napájania;
- Pripojte kábel ISP k portu Ethernet;
- V počítači prejdite do časti sieťové pripojenia a nájdite bezdrôtovú sieť s názvom *"MikroTik-..."*. Pripojte sa k nemu (skontrolujte bezdrôtové heslá na nálepke);
- Vytvorte pripojenie pomocou mobilnej aplikácie. Alternatívne použite WebFig v webovom prehliadači alebo nástroj na konfiguráciu "WinBox" na adrese [https://mt.lv/WinBox](https://mt.lv/WinBox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Stiahnite si a otvorte *Winbox* a vyberte kartu *Neighbors*, aby ste našli zariadenie;
- Predvolená adresa IP je 192.168.88.1. Kliknite na IP adresu. Ak IP nie je k dispozícii, použite *Winbox* a pripojte sa pomocou adresy MAC. Používateľské meno je *"admin"* a neexistuje žiadne heslo (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslo na nálepke);
- Kliknite na tlačidlo *"Check for updates"* a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíčky do ponuky *WebFig alebo Winbox"Files"* a reštartujte zariadenie;
- Inováciou softvéru RouterOS na najnovšiu verziu môžete zaistiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- V ponuke *"QuickSet"* nastavte nasledovné: Vyberte svoju krajinu, ak chcete použiť nastavenia regulácie krajiny;
- V ľavom poli nastavte heslo bezdrôtovej siete;
- V spodnom poli nastavte heslo smerovača;
- Nájdite číslo *LR Gateway ID* na štítku v rámci produktu a zaregistrujte ho na svojom sieťovom serveri.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je možné nainštalovať vonku. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať podľa správnych postupov, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.
- Toto je výrobok triedy A. V domácom prostredí môže tento výrobok spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa vyžadované prijatie primeraných opatrení.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.11 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom, vključno z delovanjem v legalnih frekvenčnih kanalih, za doseganje rezultatov napajanje, zahteve za kabliranje in zahteve za dinamično izbiro frekvence (DFS). Vse radijske naprave MikroTik morajo biti strokovno nameščen.
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-50.png)

*Ta naprava sprejme vhod 24V napajalnika, ki je na voljo v originalni embalaži te naprave.*

**Prvi koraki:**

- Prepričajte se, da vaš ponudnik internetnih storitev dovoljuje spremembo strojne opreme in bo izdal samodejni naslov IP;
- Odprite spodnji pokrov;
- Priključite zunanjo anteno na priključek SMA;
- Priključite napravo na vir napajanja;
- Priključite kabel ponudnika internetnih storitev na vrata Ethernet;
- Pomaknite se do razdelka za omrežne povezave v računalniku in poiščite brezžično omrežje z imenom *"MikroTik-..."*. Nadaljujte s povezavo (preverite brezžična gesla na nalepki);
- Ustvarite povezavo z uporabo mobilne aplikacije. Kot alternativo uporabite WebFig v spletnem brskalniku ali orodje za konfiguracijo "WinBox" na [https://mt.lv/WinBox](https://mt.lv/WinBox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Prenesite in odprite *Winbox* ter izberite zavihek *Neighbors*, da poiščete napravo;
- Privzeti naslov IP je 192.168.88.1. Kliknite naslov IP. Če IP ni na voljo, uporabite *Winbox* in se povežite z naslovom MAC. Uporabniško ime je *"admin"* in ni gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Kliknite gumb *"Check for updates"* in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Prenesene pakete naložite v meni *WebFig ali Winbox"Files"* in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno zmogljivost, stabilnost in varnostne posodobitve;
- V meniju *"QuickSet"* nastavite naslednje: Izberite svojo državo, da uporabite nastavitve državnih predpisov;
- V levem polju nastavite geslo za brezžično omrežje;
- V spodnjem polju nastavite geslo usmerjevalnika;
- Poiščite *LR Gateway ID* na nalepki v izdelku in ga registrirajte v svojem omrežnem strežniku.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek lahko namestite na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba pravilne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru bo uporabnik morda moral sprejeti ustrezne ukrepe.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.11 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, output kraft, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste vara professionellt installerat.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-50.png)

*Denna enhet accepterar ingång från 24V DC-nätadapter, som finns i originalförpackningen på denna enhet.*

**Första stegen:**

- Se till att din internetleverantör tillåter maskinvaruändring och kommer att utfärda en automatisk IP-adress;
- Öppna bottenlocket;
- Anslut en extern antenn till SMA-kontakten;
- Anslut enheten till strömkällan;
- Anslut din ISP-kabel till Ethernet-porten;
- Navigera till avsnittet nätverksanslutningar på din dator och leta reda på det trådlösa nätverket som heter *"MikroTik-..."*. Fortsätt att ansluta till den (kontrollera de trådlösa lösenorden på klistermärket);
- Skapa en anslutning med hjälp av en mobilapplikation. Alternativt använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" på [https://mt.lv/WinBox](https://mt.lv/WinBox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Ladda ner och öppna *Winbox* och välj fliken *Neighbors* för att hitta enheten;
- Standard-IP-adressen är 192.168.88.1. Klicka på IP-adressen. Om IP-adressen inte är tillgänglig, använd *Winbox* och anslut med MAC-adressen. Användarnamnet är *"admin"* och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen *"Check for updates"* och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda ner nedladdade paket till menyn *WebFig eller Winbox"Files"* och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I *"QuickSet"* -menyn ställer du in följande: Välj ditt land för att tillämpa inställningar för landsföreskrifter;
- Ställ in lösenordet för ditt trådlösa nätverk i det vänstra fältet;
- Ställ in ditt routerlösenord i det nedre fältet;
- Hitta *LR Gateway ID* på etiketten i produkten och registrera den i din nätverksserver.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt kan installeras utomhus. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på systemet.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.
- Detta är en klass A -produkt. I hemmet kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.11或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规，包括在合法频道内操作，输出 电源，布线要求和动态频率选择（DFS）要求。 所有MikroTik无线电设备必须 专业安装。
此“ wAP LR8”系列快速指南涵盖以下型号：RBwAPR-2nD＆R11e-LR8（wAP LR8 kit）。
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-50.png)

*本设备接受本设备原始包装中提供的24V DC电源适配器的输入。*

**第一步：**

- 确保您的 ISP 允许硬件更改并会发布自动 IP 地址；
- 打开底盖；
- 将外部天线连接到 SMA 连接器；
- 将设备连接至电源；
- 将 ISP 电缆连接到以太网端口；
- 导航到计算机上的网络连接部分，找到名为 *"MikroTik-..."* 的无线网络。继续连接（检查贴纸上的无线密码）；
- 使用移动应用程序建立连接。或者，使用WebFig在Web浏览器中或在[https://mt.lv/WinBox](https://mt.lv/WinBox) 上的"WinBox"配置工具; **提供多种配置方法以确保可访问性；**
- 下载并打开 *Winbox*， 选择 *Neighbors* 选项卡查找设备；
- 默认 IP 地址是 192.168.88.1。单击 IP 地址。如果 IP 不可用，请使用 *Winbox* 并使用 MAC 地址进行连接。用户名是 *"admin"*，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）；
- 点击 *"Check for updates"* 按钮，将RouterOS更新到最新版本；
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的包上传到 *WebFig 或 Winbox"Files"* 菜单并重启设备；
- 通过将 RouterOS 软件升级到最新版本，您可以确保最佳性能、稳定性和安全更新；
- 在 *"QuickSet"* 菜单中进行以下设置： 选择您所在的国家/地区，以应用国家/地区法规设置；
- 在左侧字段中设置您的无线网络密码；
- 在底部字段中设置您的路由器密码；
- 在产品标签上找到LR Gateway ID并将其注册到您的网络服务器中。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品可以安装在室外。 在开始安装之前，请仔细阅读安装说明。 未能使用正确的硬件和配置或未遵循正确的步骤可能会导致人员受伤和系统损坏。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 插座應安裝在設備附近，並應易於取用。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。
- 这是A类产品。在家庭环境中，本产品可能会造成无线电干扰，在这种情况下，用户可能需要采取足够的措施 。
此MikroTik设备符合欧盟针对不受控制的环境所规定的辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业使用者或公众不得小于20厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas iela 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.11 или до последней версии, чтобы обеспечить соответствие требованиям местных нормативов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, вывод требования к питанию, кабелям и динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть профессионально установлены.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-49.png)

*Данное устройство допускает ввод адаптера питания 24 В постоянного тока, который входит в оригинальную упаковку данного устройства.*

**Первые шаги:**

- Убедитесь, что ваш интернет-провайдер разрешает замену оборудования и автоматически выдает IP-адрес;
- Откройте нижнюю крышку;
- Подключите внешнюю антенну к разъему SMA;
- Подключите устройство к источнику питания;
- Подключите кабель интернет-провайдера к порту Ethernet;
- Перейдите в раздел сетевых подключений на своем компьютере и найдите беспроводную сеть с именем *"MikroTik-..."*. Приступайте к подключению (проверьте пароли беспроводной сети на наклейке);
- Установите соединение с помощью мобильного приложения. В качестве альтернативы используйте WebFig в веб-браузере или инструмент конфигурации "WinBox" по адресу [https://mt.lv/WinBox](https://mt.lv/WinBox); **существует несколько методов настройки для обеспечения доступности;**
- Загрузите и откройте *Winbox* и выберите вкладку *Neighbors*, чтобы найти устройство;
- IP-адрес по умолчанию - 192.168.88.1. Нажмите на IP-адрес. Если IP-адрес недоступен, используйте *Winbox* и подключитесь по MAC-адресу. Имя пользователя - *"admin"*, пароль отсутствует (или, для некоторых моделей, проверьте пароль пользователя и пароль беспроводной сети на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню *WebFig или Winbox"Files"* и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню *"QuickSet"* настройте следующее: Выберите свою страну, чтобы применить настройки регулирования страны;
- Установите пароль беспроводной сети в левом поле;
- Установите пароль маршрутизатора в нижнем поле;
- Найдите *LR Gateway ID* на этикетке внутри продукта и зарегистрируйте его на своем сетевом сервере.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
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
Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 20 сантиметров от человека.*

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 864-870 МГц, 2400-2483.5 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge-50.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.11 або останньої версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-18.png)

*Цей пристрій приймає вхід 24В адаптера живлення постійного струму, який надається в оригінальній упаковці цього пристрою.*

**Перші кроки:**

- Переконайтеся, що ваш постачальник послуг Інтернету дозволяє змінити апаратне забезпечення та видасть автоматичну IP-адресу;
- Відкрийте нижню кришку;
- Підключіть зовнішню антену до роз'єму SMA;
- Підключити пристрій до джерела живлення;
- Підключіть кабель провайдера до порту Ethernet;
- Перейдіть до розділу мережевих підключень на вашому комп’ютері та знайдіть бездротову мережу під назвою *"MikroTik-..."*. Перейдіть до підключення до нього (перевірте бездротові паролі на наклейці);
- Встановіть з'єднання за допомогою мобільного додатка. В іншому випадку використовуйте WebFig у веб-браузері, або інструмент конфігурації "WinBox" за адресою [https://mt.lv/WinBox](https://mt.lv/WinBox); **існує декілька методів налаштування для забезпечення доступності;**
- Завантажте та відкрийте *Winbox* і виберіть вкладку *Neighbors*, щоб знайти пристрій;
- IP-адреса за замовчуванням 192.168.88.1. Натисніть на IP-адресу. Якщо IP-адреса недоступна, використовуйте *Winbox* і підключіться за MAC-адресою. Ім’я користувача – *"admin"* і немає пароля (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Натисніть кнопку *"Check for updates"* і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню *WebFig або Winbox"Files"* і перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви зможете забезпечити оптимальну продуктивність, стабільність і оновлення безпеки;
- У меню *"QuickSet"* налаштуйте наступне: Виберіть свою країну, щоб застосувати налаштування країни;
- Налаштуйте пароль бездротової мережі в лівому полі;
- В нижньому полі встановіть пароль маршрутизатора;
- Знайдіть ідентифікатор *LR Gateway ID* на етикетці продукту та зареєструйте його на своєму мережевому сервері.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей виріб можна встановити на відкритому повітрі. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.
- Це продукт класу А. У домашньому середовищі цей виріб може спричиняти радіоперешкоди. В цьому випадку від користувача може знадобитися вжити відповідних заходів.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas iela 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 864-870 МГц (14 дБм) 2400-2483.5 МГц (20 дБм).

## UKCA marking

![](./img/ukca_black_fill.badge-48.gif)

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
  

This MikroTik device meets Maximum transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistung Grenzwerte gemäß ETSI-Vorschriften. Weitere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance de transmission maximale conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti di potenza massima di trasmissione in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los valores límite de potencia máxima de transmisión de acuerdo con la normativa ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует предельным значениям максимальной мощности передачи в соответствии с правилами ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

DC Jack (9-30 V DC) PoE In Ethernet Port (9-30 V DC) Automotive (9-30 V DC)
24 V / 0.8
IP54
-40°..+60°C

\#73662
