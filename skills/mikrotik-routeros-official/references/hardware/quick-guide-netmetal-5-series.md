# Quick Guide - NetMetal 5 series

> Models: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple)

**Models: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple)**

![](./img/mt_logo_arrow_v2-02-89.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.10.1 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
:::

This "NetMetal 5" series Quick Guide covers models: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-101.png)

Depending on the antenna used, you must set its gain and set the installation setting to '*Outdoor*'. This is to ensure that EIRP meets the limit set by the local authorities.

**First steps:**

- Open the upper cover and connect an external antenna (mandatory);
- Open the bottom cover and connect the device to the power source;
- Connect the device to the included PoE injector with an Ethernet cable to the *"data+power"* end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Navigate to the network connections section on your computer and locate the wireless network named "*MikroTik-...*". Proceed to connect to it (check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field;
- If you need to use a SIM card, open the case and install your desired modem into miniPCIe slot.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 255 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.10.1 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби, включително работата в рамките на законни честотни канали, извеждане на продукция изисквания за захранване, окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-96.png)

В зависимост от използваната антена, трябва да зададете нейното усилване и да зададете настройката за инсталиране на '*Outdoor*'. Това е за да се гарантира, че EIRP отговаря на ограничението, определено от местните власти.

**Първи стъпки:**

- Отворете горния капак и свържете външна антена (задължително);
- Отворете долния капак и свържете устройството към източника на захранване;
- Свържете устройството към включения PoE инжектор с Ethernet кабел към края *"data+power"*;
- Свържете края за данни на PoE инжектора към компютъра;
- Свържете захранващия адаптер към PoE инжектора;
- Отидете до секцията за мрежови връзки на вашия компютър и намерете безжичната мрежа с име "*MikroTik-...*". Продължете да се свързвате с него (проверете безжичните пароли на стикера);
- Установете връзка чрез мобилно приложение. Алтернативно, използвайте WebFig в уеб браузър или инструмента за конфигуриране "WinBox" на [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Начнете конфигурацията с избран инструмент, използвайки стандартния IP адрес 192.168.88.1. Ако IP адресът не е достъпен, използвайте WinBox и изберете раздела "Neighbors", за да намерите устройството;
- Продължете да се свързвате чрез MAC адреса. Потребителското име е "admin", и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Натиснете бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- В менюто "QuickSet" настройте следното: Изберете вашата държава, за да приложите настройките за страната;
- Настройте паролата на вашата безжична мрежа в лявото поле;
- Настройте паролата на вашия рутер в долното поле;
- Ако трябва да използвате SIM карта, отворете кутията и инсталирайте желания модем в miniPCIe слота.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоари, одобрени от производителя, и които могат да бъдат намерено аз n оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за монтиране на открито върху стълб. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате подходящия хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата на системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се изисква да предприеме адекватни мерки.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 255 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.10.1 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupů požadavky na napájení, kabeláž a dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být profesionálně nainstalován.
Tato rychlá příručka „NetMetal 5“ zahrnuje modely: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-96.png)

V závislosti na použité anténě musíte nastavit její zisk a nastavit instalační nastavení na „*Outdoor*“. Tím je zajištěno, že EIRP splňuje limit stanovený místními úřady.

**První kroky:**

- Otevřete horní kryt a připojte externí anténu (povinné);
- Otevřete spodní kryt a připojte zařízení ke zdroji napájení;
- Připojte zařízení k přiloženému PoE injektoru pomocí ethernetového kabelu do konce *"data+power"*;
- Připojte datový konec PoE injektoru k počítači;
- Připojte napájecí adaptér k PoE injektoru;
- Přejděte na vašem počítači do sekce síťových připojení a vyhledejte bezdrátovou síť s názvem „*MikroTik-...*“. Pokračujte v připojení (zkontrolujte hesla bezdrátového připojení na štítku);
- Vytvořte spojení pomocí mobilní aplikace. Alternativně můžete použít WebFig v webovém prohlížeči nebo nástroj pro konfiguraci "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Zahajte konfiguraci ve zvoleném nástroji s výchozí IP adresou 192.168.88.1. Pokud není IP adresa k dispozici, použijte WinBox a vyberte kartu "Neighbors", abyste zařízení našli;
- Pokračujte v připojení pomocí MAC adresy. Uživatelské jméno je "admin", a není žádné heslo (nebo, pro některé modely, zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Klikněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do nabídky "Files" na WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce "QuickSet" proveďte následující nastavení: Vyberte svou zemi, abyste aplikovali nastavení pro regulaci země;
- Nastavte heslo k bezdrátové síti v levém poli;
- Nastavte heslo k vašemu routeru v dolním poli;
- Pokud potřebujete použít SIM kartu, otevřete pouzdro a nainstalujte požadovaný modem do slotu miniPCIe.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájení a příslušenství schválené výrobcem, které může být nalezeno v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k montáži venku na sloup. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete odpovídající hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobit rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Abyste zabránili znečištění životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na určených místech. Seznamte se s postupy správné přepravy zařízení na určená sběrná místa ve vaší oblasti.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 255 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.10.1 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler, herunder drift inden for lovlige frekvenskanaler, output strøm, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal være professionelt installeret.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-96.png)

Afhængigt af den anvendte antenne skal du indstille dens forstærkning og indstille installationsindstillingen til '*Outdoor*'. Dette er for at sikre, at EIRP overholder den grænse, der er fastsat af de lokale myndigheder.

**Første trin:**

- Åbn det øvre låg og tilslut en ekstern antenne (obligatorisk);
- Åbn bunddækslet og tilslut enheden til strømkilden;
- Tilslut enheden til den medfølgende PoE-injektor med et Ethernet-kabel til *"data+power"*-enden;
- Tilslut dataenden af ​​PoE-injektoren til computeren;
- Tilslut strømadapteren til PoE-injektoren;
- Naviger til afsnittet om netværksforbindelser på din computer, og find det trådløse netværk med navnet "*MikroTik-...*". Fortsæt med at oprette forbindelse til den (tjek de trådløse adgangskoder på mærkaten);
- Opret forbindelse ved hjælp af en mobilapplikation. Alternativt kan du bruge WebFig i en webbrowser eller "WinBox" konfigurationsværktøjet på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Start konfigurationen inden for det valgte værktøj ved hjælp af standard IP-adressen 192.168.88.1. Hvis IP-adressen ikke er tilgængelig, skal du bruge WinBox og vælge fanen "Neighbors" for at finde enheden;
- Fortsæt med at oprette forbindelse ved at bruge MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload de downloadede pakker til WebFig eller WinBox "Files" menuen og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version sikrer du optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- I menuen "QuickSet" konfigurer følgende: Vælg dit land for at anvende landsreguleringsindstillinger;
- Indstil dit trådløse netværkspassword i det venstre felt;
- Indstil dit routerpassword i bundfeltet;
- Hvis du skal bruge et SIM-kort, skal du åbne etuiet og installere det ønskede modem i miniPCIe-slot.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og tilbehør godkendt af producenten, og som kan være fundet i den originale emballage af dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive monteret udendørs på en stang. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- For at undgå forurening af miljøet skal apparatet adskilles fra husholdningsaffald og bortskaffes på en sikker måde, f.eks. I bestemte områder. Bliv fortrolig med procedurer til korrekt transport af udstyr til udpegede indsamlingssteder i dit område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 255 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.10.1 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle und der Ausgabe Anforderungen an Stromversorgung, Verkabelung und dynamische Frequenzauswahl (Dynamic Frequency Selection, DFS). Alle MikroTik Funkgeräte müssen professionell installiert.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-96.png)

Abhängig von der verwendeten Antenne müssen Sie die Verstärkung einstellen und die Installationseinstellung auf „*Outdoor*“ stellen. Dies soll sicherstellen, dass EIRP die von den lokalen Behörden festgelegten Grenzwerte einhält.

**Erste Schritte:**

- Öffnen Sie die obere Abdeckung und schließen Sie eine externe Antenne an (obligatorisch);
- Öffnen Sie die untere Abdeckung und schließen Sie das Gerät an die Stromquelle an;
- Verbinden Sie das Gerät über ein Ethernet-Kabel mit dem *"data+power"*- Ende mit dem mitgelieferten PoE-Injektor;
- Verbinden Sie das Datenende des PoE-Injektors mit dem Computer;
- Schließen Sie das Netzteil an den PoE-Injektor an;
- Navigieren Sie zum Abschnitt „Netzwerkverbindungen“ auf Ihrem Computer und suchen Sie das drahtlose Netzwerk mit dem Namen „*MikroTik-...*“. Stellen Sie eine Verbindung her (überprüfen Sie die WLAN-Passwörter auf dem Aufkleber);
- Stellen Sie eine Verbindung mit einer mobilen Anwendung her. Alternativ können Sie WebFig in einem Webbrowser oder das "WinBox" Konfigurationswerkzeug unter [https://mt.lv/winbox](https://mt.lv/winbox) verwenden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Starten Sie die Konfiguration im gewählten Tool mit der Standard-IP-Adresse 192.168.88.1. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie WinBox und wählen Sie die Registerkarte "Neighbors", um das Gerät zu finden;
- Fahren Sie fort, sich über die MAC-Adresse zu verbinden. Der Benutzername lautet "admin", und es gibt kein Passwort (oder, für einige Modelle, überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch das Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie eine optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Konfigurieren Sie im Menü "QuickSet" folgendes: Wählen Sie Ihr Land aus, um länderspezifische Einstellungen anzuwenden;
- Legen Sie Ihr drahtloses Netzwerkkennwort im linken Feld fest;
- Legen Sie Ihr Routerkennwort im unteren Feld fest;
- Wenn Sie eine SIM-Karte verwenden müssen, öffnen Sie das Gehäuse und installieren Sie Ihr gewünschtes Modem im miniPCIe-Steckplatz.

**Sicherheitsinformation:**

- Machen Sie sich vor Arbeiten an MikroTik-Geräten mit den Gefahren elektrischer Schaltkreise vertraut und machen Sie sich mit den üblichen Vorgehensweisen zur Unfallverhütung vertraut. Der Installateur sollte mit den Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das Netzteil und vom Hersteller zugelassenes Zubehör, und das kann sein gefunden In der Originalverpackung dieses Produkts.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Vorschriften für elektrische Geräte entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Montage im Freien an einer Stange vorgesehen. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie die richtige Hardware und Konfiguration nicht verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zur Beschädigung des Systems führen.
- Wir können nicht garantieren, dass durch unsachgemäßen Gebrauch des Geräts keine Unfälle oder Schäden entstehen. Bitte verwenden Sie dieses Produkt mit Vorsicht und betreiben Sie es auf eigenes Risiko!
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise geeignete Maßnahmen ergreifen.
- Im Falle eines Gerätefehlers trennen Sie das Gerät bitte von der Stromversorgung. Der schnellste Weg, dies zu tun, besteht darin, den Netzadapter aus der Steckdose zu ziehen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Geräte zu bestimmten Sammelstellen in Ihrer Nähe vertraut.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 255 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.10.1 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών, συμπεριλαμβανομένης της λειτουργίας εντός των νόμιμων καναλιών συχνότητας, της παραγωγής ισχύ, απαιτήσεις καλωδίωσης και απαιτήσεις δυναμικής επιλογής συχνότητας (DFS). Όλες οι ασύρματες συσκευές MikroTik πρέπει να είναι επαγγελματικά εγκατεστημένο.
Αυτός ο γρήγορος οδηγός σειράς "NetMetal 5" καλύπτει μοντέλα: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-96.png)

Ανάλογα με την κεραία που χρησιμοποιείται, πρέπει να ρυθμίσετε το κέρδος της και να ορίσετε τη ρύθμιση εγκατάστασης σε «*Outdoor*». Με τον τρόπο αυτό διασφαλίζεται ότι το EIRP πληροί το όριο που έχουν οριστεί από τις τοπικές αρχές.

**Πρώτα βήματα:**

- Ανοίξτε το επάνω κάλυμμα και συνδέστε μια εξωτερική κεραία (υποχρεωτικό);
- Ανοίξτε το κάτω κάλυμμα και συνδέστε τη συσκευή στην πηγή τροφοδοσίας;
- Συνδέστε τη συσκευή στον παρεχόμενο εγχυτήρα PoE με ένα καλώδιο Ethernet στο άκρο *"data+power";*
- Συνδέστε το άκρο δεδομένων του εγχυτήρα PoE στον υπολογιστή;
- Συνδέστε το τροφοδοτικό στον εγχυτήρα PoE;
- Μεταβείτε στην ενότητα συνδέσεις δικτύου στον υπολογιστή σας και εντοπίστε το ασύρματο δίκτυο με το όνομα "*MikroTik-...*". Συνεχίστε να συνδεθείτε σε αυτό (ελέγξτε τους κωδικούς πρόσβασης ασύρματου δικτύου στο αυτοκόλλητο);
- Δημιουργήστε σύνδεση χρησιμοποιώντας μια κινητή εφαρμογή. Εναλλακτικά, μπορείτε να χρησιμοποιήσετε το WebFig σε έναν περιηγητή ή το εργαλείο διαμόρφωσης "WinBox" στη διεύθυνση [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ξεκινήστε τη διαμόρφωση μέσα από το επιλεγμένο εργαλείο, χρησιμοποιώντας την προεπιλεγμένη διεύθυνση IP 192.168.88.1. Αν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το WinBox και επιλέξτε την καρτέλα "Neighbors" για να βρείτε τη συσκευή;
- Συνεχίστε να συνδέεστε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός (ή, για κάποια μοντέλα, ελέγξτε τους κωδικούς χρήστη και ασύρματους στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην πιο πρόσφατη έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού "Files" του WebFig ή WinBox και επανεκκινήστε τη συσκευή;
- Αναβαθμίζοντας το λογισμικό του RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Στο μενού "QuickSet" ρυθμίστε τα εξής: Επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις κανονισμού για τη χώρα;
- Ρυθμίστε τον κωδικό πρόσβασης του ασύρματου δικτύου σας στο αριστερό πεδίο;
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο;
- Εάν χρειάζεται να χρησιμοποιήσετε κάρτα SIM, ανοίξτε τη θήκη και εγκαταστήστε το μόντεμ που θέλετε στην υποδοχή miniPCIe.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την παροχή ρεύματος και αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και ποια μπορεί να είναι βρέθηκαν στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται να τοποθετηθεί σε εξωτερικό χώρο σε έναν πόλο. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του υλικού και των ρυθμίσεων διόρθωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Πρόκειται για προϊόν κλάσης Α. Σε οικιακό περιβάλλον, αυτό το προϊόν μπορεί να προκαλέσει ραδιοπαρεμβολές, οπότε ενδέχεται να χρειαστεί να ληφθούν τα κατάλληλα μέτρα από τον χρήστη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 255 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.10.1 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales legales de frecuencia, salida alimentación, requisitos de cableado y requisitos de selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-98.png)

Dependiendo de la antena utilizada, debe establecer su ganancia y establecer la configuración de instalación en '*Outdoor*'. Esto es para garantizar que el PIRE cumpla con el límite establecido por las autoridades locales.

**Primeros pasos:**

- Abra la tapa superior y conecte una antena externa (obligatorio);
- Abra la cubierta inferior y conecte el dispositivo a la fuente de alimentación;
- Conecte el dispositivo al inyector PoE incluido con un cable Ethernet al extremo *"data+power"*;
- Conecte el extremo de datos del inyector PoE a la computadora;
- Conecte el adaptador de corriente al inyector PoE;
- Navegue a la sección de conexiones de red en su computadora y localice la red inalámbrica llamada "*MikroTik-...*". Proceda a conectarse a él (verifique las contraseñas inalámbricas en la etiqueta);
- Establecer una conexión mediante una aplicación móvil. Alternativamente, puede utilizar WebFig en un navegador web o la herramienta de configuración "WinBox" en [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Inicie la configuración dentro de la herramienta seleccionada, utilizando la dirección IP predeterminada 192.168.88.1. Si la dirección IP no está disponible, utilice WinBox y elija la pestaña "Neighbors" para encontrar el dispositivo;
- Proceda a conectarse utilizando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú "Files" de WebFig o WinBox y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- En el menú "QuickSet" configure lo siguiente: Elija su país para aplicar configuraciones de regulación del país;
- Configure la contraseña de su red inalámbrica en el campo izquierdo;
- Configure la contraseña de su router en el campo inferior;
- Si necesita usar una tarjeta SIM, abra la carcasa e instale el módem deseado en la ranura miniPCIe.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Use solo la fuente de alimentación y accesorios aprobados por el fabricante, y que pueden ser encontró En el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para montarse en exteriores en un poste. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podrían producir situaciones peligrosas para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- Este es un producto de clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en las áreas designadas. Familiarícese con los procedimientos para transportar correctamente el equipo a los puntos de recolección designados en su área.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 255 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

Rango de frecuencia (potencia de salida máxima): 5725-5850 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.10.1 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas toimimist seaduslikes sageduskanalites, väljund võimsus, kaabeldusnõuded ja dünaamilise sageduse valiku (DFS) nõuded. Kõik MikroTiku raadioseadmed peavad olema professionaalselt paigaldatud.
See "NetMetal 5" seeria lühijuhend hõlmab mudeleid: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-96.png)

Sõltuvalt kasutatavast antennist peate määrama selle võimenduse ja seadma paigaldussäteteks '*Outdoor*'. Selle eesmärk on tagada, et EIRP vastaks kohalike omavalitsuste seatud piirmääradele.

**Esimesed sammud:**

- Avage ülemine kaas ja ühendage väline antenn (kohustuslik);
- Avage alumine kaas ja ühendage seade toiteallikaga;
- Ühendage seade kaasasoleva PoE-pihustiga Etherneti kaabli abil *"data+power"* otsaga;
- Ühendage PoE-pihusti andmeots arvutiga;
- Ühendage toiteadapter PoE-pihustiga;
- Liikuge oma arvutis võrguühenduste jaotisse ja leidke traadita võrk nimega "*MikroTik-...*". Jätkake sellega ühenduse loomist (kontrollige kleebis olevaid juhtmevabasid paroole);
- Looge ühendus mobiilirakenduse abil. Alternatiivselt saate kasutada WebFig'i veebibrauseris või "WinBox" konfiguratsioonitööriista aadressil [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Alustage konfiguratsiooni valitud tööriista abil, kasutades vaikimisi IP-aadressi 192.168.88.1. Kui IP-aadress pole saadaval, kasutage WinBoxi ja valige seade leidmiseks vahekaart "Neighbors";
- Jätkake ühendumist MAC-aadressi kasutades. Kasutajanimi on "admin" ja parooli pole (või mõne mudeli puhul kontrollige kasutaja ja traadita paroole kleebisel);
- Klõpsake nupul "Check for updates" ja värskendage RouterOS-i viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige allalaaditud paketid üles WebFig või WinBox "Files" menüüsse ja taaskäivitage seade;
- Uuendades RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Menüüs "QuickSet" konfigureerige järgmist: Valige oma riik, et rakendada riigipõhiseid seadeid;
- Seadke traadita võrgu parool vasakusse välja;
- Seadke ruuteri parool alumisse välja;
- Kui teil on vaja kasutada SIM-kaarti, avage ümbris ja paigaldage soovitud modem miniPCIe pessa.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult toiteallikat ja tootja poolt heaks kiidetud lisaseadmed, mis võivad olla leitud ma olen selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud paigaldamiseks välistingimustele. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Parandatud riistvara ja konfiguratsiooni kasutamata jätmine või õigete toimingute järgimata jätmine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist.
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja utiliseerige see ohutult, näiteks selleks ettenähtud kohtades. Tutvuge seadmete nõuetekohase transportimise protseduuridega teie piirkonnas asuvatesse kogumispunktidesse.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 255 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.10.1 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtö teho, kaapelointivaatimukset ja dynaamisen taajuuden valinnan (DFS) vaatimukset. Kaikkien MikroTik-radiolaitteiden on oltava ammattimaisesti asennettu.
Tämä "NetMetal 5" -sarjan pikaopas kattaa mallit: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi) Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-96.png)

Käytettävän antennin mukaan sinun on asetettava sen vahvistus ja asetettava asennusasetukseksi "*Outdoor*". Tällä varmistetaan, että EIRP noudattaa paikallisten viranomaisten asettamia rajoituksia.

**Ensiaskeleet:**

- Avaa yläkansi ja kytke ulkoinen antenni (pakollinen);
- Avaa pohjakansi ja liitä laite virtalähteeseen;
- Liitä laite mukana toimitettuun PoE-injektoriin Ethernet-kaapelilla *"data+power"* - päähän;
- Liitä PoE-injektorin datapää tietokoneeseen;
- Liitä virtalähde PoE-suuttimeen;
- Siirry tietokoneesi verkkoyhteydet-osioon ja etsi langaton verkko nimeltä "*MikroTik-...*". Jatka yhteyden muodostamista siihen (tarkista tarrassa olevat langattomat salasanat);
- Muodosta yhteys käyttämällä mobiilisovellusta. Vaihtoehtoisesti voit käyttää WebFigiä selaimessa tai "WinBox" konfiguraatiotyökalua osoitteessa [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Aloita konfigurointi valitussa työkalussa käyttäen oletus-IP-osoitetta 192.168.88.1. Jos IP-osoite ei ole saatavilla, käytä WinBoxia ja valitse "Neighbors"-välilehti laitteen löytämiseksi;
- Jatka yhteyden muodostamista MAC-osoitteen avulla. Käyttäjänimi on "admin", eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjä- ja langattomat salasanat tarraan);
- Klikkaa "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFig- tai WinBox-"Files"-valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmiston uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- "QuickSet"-valikossa aseta seuraavat: Valitse maasi, jotta voit soveltaa maasääntelyasetuksia;
- Aseta langattoman verkkosi salasana vasempaan kenttään;
- Aseta reitittimesi salasana alaosaan;
- Jos tarvitset SIM-korttia, avaa kotelo ja asenna haluamasi modeemi miniPCIe-paikkaan.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain virtalähdettä ja valmistajan hyväksymät lisävarusteet, jotka voivat olla löydetty Olen tämän tuotteen alkuperäispakkaus.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi ulkona sauvaan. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet.
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla esimerkiksi määrätyillä alueilla. Tutustu toimenpiteisiin, joilla laite kuljetetaan asianmukaisesti alueellesi määritettyihin keräyspisteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 255 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.10.1 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la sortie les exigences d'alimentation, de câblage et de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installé professionnellement.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-96.png)

Selon l'antenne utilisée, vous devez régler son gain et régler le paramètre d'installation sur 'O *utdoor*'. Il s'agit de garantir que l'EIRP respecte la limite fixée par les autorités locales.

**Premiers pas:**

- Ouvrez le capot supérieur et connectez une antenne externe (obligatoire);
- Ouvrez le capot inférieur et connectez l'appareil à la source d'alimentation;
- Connectez l'appareil à l'injecteur PoE inclus avec un câble Ethernet à l' extrémité *"data+power"*;
- Connectez l'extrémité de données de l'injecteur PoE à l'ordinateur;
- Connectez l'adaptateur secteur à l'injecteur PoE;
- Accédez à la section des connexions réseau sur votre ordinateur et localisez le réseau sans fil nommé "*MikroTik-...*". Procédez à la connexion (vérifiez les mots de passe sans fil sur l'autocollant);
- Établir une connexion à l'aide d'une application mobile. Vous pouvez également utiliser WebFig dans un navigateur Web ou l'outil de configuration "WinBox" à l'adresse [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Démarrez la configuration dans l'outil choisi en utilisant l'adresse IP par défaut 192.168.88.1. Si l'adresse IP n'est pas disponible, utilisez WinBox et choisissez l'onglet "Neighbors" pour trouver le périphérique;
- Procédez à la connexion en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les paquets téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, une stabilité et des mises à jour de sécurité;
- Dans le menu "QuickSet", configurez ce qui suit: Choisissez votre pays pour appliquer les paramètres de régulation du pays;
- Configurez le mot de passe de votre réseau sans fil dans le champ de gauche;
- Configurez le mot de passe de votre routeur dans le champ inférieur;
- Si vous avez besoin d'utiliser une carte SIM, ouvrez le boîtier et installez le modem souhaité dans l'emplacement miniPCIe.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l' alimentation et accessoires approuvés par le fabricant, et qui peuvent être a trouvé dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être monté à l'extérieur sur un poteau. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration corrects ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Pour éviter la contamination de l'environnement, séparez l'appareil des déchets ménagers et éliminez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 255 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.10.1 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala zahtjevi za napajanje, kabliranje i zahtjevi za dinamički odabir frekvencije (DFS). Svi MikroTik radijski uređaji moraju biti profesionalno instaliran.
Ovaj kratki vodič serije "NetMetal 5" obuhvaća modele: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-96.png)

Ovisno o korištenoj anteni, morate postaviti njezino pojačanje i postaviti postavku instalacije na '*Outdoor*'. Time se osigurava da EIRP ispunjava ograničenje koje su postavile lokalne vlasti.

**Prvi koraci:**

- Otvorite gornji poklopac i spojite vanjsku antenu (obavezno);
- Otvorite donji poklopac i spojite uređaj na izvor napajanja;
- Spojite uređaj na priloženi PoE injektor pomoću Ethernet kabela na kraju *"data+power"*;
- Spojite podatkovni kraj PoE injektora na računalo;
- Spojite strujni adapter na PoE injektor;
- Idite do odjeljka mrežnih veza na računalu i pronađite bežičnu mrežu pod nazivom "*MikroTik-...*". Nastavite s povezivanjem s njim (provjerite bežične lozinke na naljepnici);
- Uspostavite vezu pomoću mobilne aplikacije. Opcionalno, koristite WebFig u web pregledniku ili alat za konfiguraciju "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Pokrenite konfiguraciju unutar odabranog alata, koristeći zadanu IP adresu 192.168.88.1. Ako IP adresa nije dostupna, koristite WinBox i odaberite karticu "Neighbors" da biste pronašli uređaj;
- Nastavite s povezivanjem putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Kliknite gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem RouterOS softvera na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U "QuickSet" izborniku postavite sljedeće: Odaberite svoju zemlju da biste primijenili postavke regulacije za tu zemlju;
- Postavite lozinku za svoju bežičnu mrežu u lijevo polje;
- Postavite lozinku za svoj usmjerivač u donje polje;
- Ako trebate koristiti SIM karticu, otvorite kućište i instalirajte željeni modem u miniPCIe utor.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobren od proizvođača, a može biti pronađeno Ja nisam originalno pakiranje ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen postavljanju vani na stup. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne slijedite ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere.
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Da biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na za to predviđena mjesta. Upoznajte se s postupcima pravilnog transporta opreme do određenih sabirnih mjesta u vašem području.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 255 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.10.1-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon keresztüli működést is teljesítményre, kábelezésre és dinamikus frekvenciaválasztásra (DFS) vonatkozó követelmények. Az összes MikroTik rádiókészüléknek lennie kell szakszerűen telepítve.
Ez a "NetMetal 5" sorozat Gyors útmutató a következő modellekre terjed ki: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-96.png)

A használt antennától függően be kell állítania annak erősítését, és a telepítési beállítást "*Outdoor*"-re kell állítani. Ennek célja annak biztosítása, hogy az EIRP megfeleljen a helyi hatóságok által meghatározott határértéknek.

**Első lépések:**

- Nyissa ki a felső fedelet, és csatlakoztasson egy külső antennát (kötelező);
- Nyissa ki az alsó fedelet, és csatlakoztassa a készüléket az áramforráshoz;
- Csatlakoztassa az eszközt a mellékelt PoE befecskendezőhöz egy Ethernet-kábellel az *"data+power" - es* végéhez;
- Csatlakoztassa a PoE injektor adatvégét a számítógéphez;
- Csatlakoztassa a hálózati adaptert a PoE befecskendezőhöz;
- Keresse meg számítógépén a hálózati kapcsolatok szakaszt, és keresse meg a „*MikroTik-...*” nevű vezeték nélküli hálózatot. Folytassa a csatlakozással (ellenőrizze a vezeték nélküli jelszavakat a matricán);
- Kapcsolat létesítése mobilalkalmazás segítségével. Vagy használja a WebFig-et egy webböngészőben vagy a "WinBox" konfigurációs eszközt a [https://mt.lv/winbox](https://mt.lv/winbox) címen; **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Indítsa el a konfigurációt az választott eszközön, az alapértelmezett 192.168.88.1 IP-cím használatával. Ha az IP-cím nem érhető el, használja a WinBoxot, és válassza ki a "Neighbors" lapot az eszköz megtalálásához;
- Folytassa a kapcsolatot a MAC cím használatával. A felhasználónév "admin", és nincs jelszó (vagy néhány modell esetén ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- A RouterOS szoftver frissítésével a legújabb verzióra optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- A "QuickSet" menüben állítsa be a következőket: Válassza ki az országát a szabályozási beállítások alkalmazásához;
- Állítsa be a vezeték nélküli hálózati jelszavát a bal oldali mezőben;
- Állítsa be a router jelszavát az alsó mezőben;
- Ha SIM-kártyát szeretne használni, nyissa ki a tokot, és helyezze be a kívánt modemet a miniPCIe nyílásba.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak az áramellátást használja és a gyártó által jóváhagyott kiegészítők, amelyek lehetnek megtalált A termék eredeti csomagolása.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket szabadon, egy oszlopra kell felszerelni. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helyes hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását eredményezheti.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, amely esetben a felhasználót fel kell kérni a megfelelő intézkedések megtételére.
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- A környezet szennyeződésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon dobja el, például a kijelölt területekre. Ismerje meg a berendezés megfelelő szállítási eljárásait a környéken található gyűjtőhelyekre.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 255 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan cepat

*Perangkat ini harus diperbarui ke RouterOS v7.10.1 atau versi terbaru untuk mematuhi peraturan otoritas setempat.*

*Pengguna akhir bertanggung jawab untuk mematuhi peraturan setempat setempat, termasuk pengoperasian di saluran frekuensi resmi, daya keluaran, pemasangan kabel, dan persyaratan pemilihan frekuensi dinamis (DFS). Semua perangkat radio MikroTik harus dipasang secara profesional.*

Panduan mulai cepat seri "NetMetal 5" ini mencakup model: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM ( NetMetal 5SHP tiga kali lipat).
![](./img/image2020-1-31_12-4-32.badge-101.png)

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama model produk pada label casing (ID).*

*Kunjungi halaman panduan pengguna di [https://mt.lv/um-id](https://mt.lv/um-id) untuk panduan pengguna yang diperbarui sepenuhnya. Atau pindai kode QR dengan ponsel Anda.*

*Spesifikasi teknis, brosur, dan informasi produk lainnya di [https://mikrotik.com/products](https://mikrotik.com/products)*

*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Memulai Cepat ini.*

*Panduan konfigurasi software dalam bahasa Anda dengan informasi tambahan tersedia di [https://mt.lv/help-id](https://mt.lv/help-id)*

*Perangkat MikroTik untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi, konsultasikan dengan konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

*Bergantung pada antena yang digunakan, Anda perlu menyetel penguatannya dan menyetel setelan penginstalan ke 'Outdoor'. Ini untuk memastikan bahwa EIRP memenuhi batas yang ditetapkan oleh otoritas lokal.*

**Langkah pertama:**

- Buka penutup atas dan sambungkan antena eksternal (wajib);
- Buka penutup bawah dan sambungkan perangkat ke sumber listrik;
- Hubungkan perangkat ke injektor PoE yang disertakan dengan kabel Ethernet ke ujung *"data+power"*;
- Hubungkan ujung data injektor PoE ke komputer;
- Hubungkan adaptor daya ke injektor PoE;
- Arahkan ke bagian koneksi jaringan di komputer Anda dan temukan jaringan nirkabel bernama "*MikroTik-...*". Lanjutkan untuk menghubungkannya (periksa kata sandi nirkabel pada stiker);
- Buat koneksi menggunakan aplikasi seluler. Alternatifnya, gunakan WebFig dalam peramban web atau alat konfigurasi "WinBox" di [https://mt.lv/winbox](https://mt.lv/winbox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Mulai konfigurasi dalam alat yang dipilih, menggunakan alamat IP default 192.168.88.1. Jika alamat IP tidak tersedia, gunakan WinBox dan pilih tab "Neighbors" untuk menemukan perangkat;
- Lanjutkan untuk terhubung menggunakan alamat MAC. Nama pengguna adalah "admin," dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket-paket yang diunduh ke menu "Files" WebFig atau WinBox dan reboot perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Di menu "QuickSet" atur hal berikut: Pilih negara Anda, untuk menerapkan pengaturan regulasi negara;
- Atur kata sandi jaringan nirkabel Anda di bidang kiri;
- Atur kata sandi router Anda di bidang bawah;
- Jika Anda perlu menggunakan kartu SIM, buka casing dan pasang modem yang Anda inginkan ke dalam slot miniPCIe.

**Informasi keselamatan:**

- Sebelum mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik dan pahami praktik standar untuk pencegahan kecelakaan. Pemasang harus terbiasa dengan struktur, istilah, dan konsep jaringan.
- Hanya gunakan catu daya dan aksesori yang disetujui oleh produsen dan yang dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan memenuhi syarat, sesuai dengan petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dirancang untuk dipasang di luar ruangan pada sebuah tiang. Baca instruksi perakitan dengan hati-hati sebelum memulai instalasi. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan merusak sistem.
- Kami tidak dapat menjamin bahwa tidak ada kecelakaan atau kerusakan yang akan terjadi karena penggunaan perangkat yang tidak tepat. Gunakan produk ini dengan hati-hati dan operasikan dengan risiko Anda sendiri!
- Ini adalah produk kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu melakukan tindakan yang memadai.
- Jika terjadi kegagalan perangkat, lepaskan dari catu daya. Cara tercepat untuk melakukannya adalah mencabut adaptor daya dari stopkontak.
- Untuk menghindari kontaminasi lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan aman, misalnya di area yang ditentukan. Biasakan diri Anda dengan prosedur untuk mengangkut peralatan Anda dengan benar ke titik pengumpulan yang ditentukan di area Anda.

**Paparan Radiasi Frekuensi Radio:** Peralatan MikroTik ini mematuhi batas paparan radiasi Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini harus dipasang dan digunakan dengan jarak tidak kurang dari 255 sentimeter dari tubuh Anda, pengguna profesional atau umum.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.10.1 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali, incluso il funzionamento nei canali di frequenza legali, in uscita requisiti di alimentazione, cablaggio e selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installato professionalmente.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-96.png)

A seconda dell'antenna utilizzata, è necessario impostare il suo guadagno e impostare l'impostazione di installazione su '*Outdoor*'. Questo per garantire che l'EIRP soddisfi il limite fissato dalle autorità locali.

**Primi passi:**

- Aprire il coperchio superiore e collegare un'antenna esterna (obbligatoria);
- Aprire il coperchio inferiore e collegare il dispositivo alla fonte di alimentazione;
- Collegare il dispositivo all'iniettore PoE incluso con un cavo Ethernet all'estremità *"data+power"*;
- Collegare l'estremità dati dell'iniettore PoE al computer;
- Collegare l'alimentatore all'iniettore PoE;
- Passare alla sezione delle connessioni di rete sul computer e individuare la rete wireless denominata "*MikroTik-...*". Procedi alla connessione ( controlla le password wireless sull'adesivo);
- Stabilire una connessione tramite un'applicazione mobile. In alternativa, utilizza WebFig in un browser web o lo strumento di configurazione "WinBox" all'indirizzo [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Inizia la configurazione all'interno dello strumento scelto, utilizzando l'indirizzo IP predefinito 192.168.88.1. Se l'indirizzo IP non è disponibile, utilizza WinBox e scegli la scheda "Neighbors" per trovare il dispositivo;
- Prosegui per connetterti utilizzando l'indirizzo MAC. Il nome utente è "admin," e non c'è alcuna password (o, per alcuni modelli, controlla le password dell'utente e wireless sull'etichetta);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Nel menu "QuickSet" imposta quanto segue: Scegli il tuo paese per applicare le impostazioni di regolamentazione nazionale;
- Imposta la password della tua rete wireless nel campo sinistro;
- Imposta la password del tuo router nel campo inferiore;
- Se è necessario utilizzare una scheda SIM, aprire la custodia e installare il modem desiderato nello slot miniPCIe.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l' alimentatore e accessori approvati dal produttore e quali possono essere trovato nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è progettato per essere montato all'esterno su un'asta. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il rispetto delle procedure corrette potrebbe comportare una situazione pericolosa per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio, in aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura ai punti di raccolta designati nella propria zona.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 255 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.10.1 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum, þar með talið rekstri innan löglegra tíðnisviða, framleiðsla afl, kaðall kröfur og Dynamic Frequency Val (DFS) kröfur. Öll MikroTik útvarpstæki verða að vera faglega sett upp.
Þessi „NetMetal 5“ röð snöggvísunar nær yfir módel: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-96.png)

Það fer eftir loftnetinu sem er notað, þú verður að stilla styrk þess og stilla uppsetningarstillinguna á '*Outdoor*'. Þetta er til að tryggja að EIRP uppfylli þau mörk sem sveitarfélögin hafa sett.

**Fyrstu skrefin:**

- Opnaðu efri hlífina og tengdu ytra loftnet (skylda);
- Opnaðu botnlokið og tengdu tækið við aflgjafa;
- Tengdu tækið við meðfylgjandi PoE inndælingartæki með Ethernet snúru við enda *"data+power"*;
- Tengdu gagnaenda PoE inndælingartækisins við tölvuna;
- Tengdu straumbreytinn við PoE inndælingartækið;
- Farðu í nettengingarhlutann á tölvunni þinni og finndu þráðlausa netið sem heitir "*MikroTik-...*". Haltu áfram að tengjast því (athugaðu þráðlausu lykilorðin á límmiðanum);
- Opprett forbindelse ved hjelp av en mobilapplikasjon. Alternativt kan du bruke WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Start konfigurasjonen innenfor det valgte verktøyet ved hjelp av standard IP-adresse 192.168.88.1. Hvis IP-adressen ikke er tilgjengelig, bruk WinBox og velg fanen "Neighbors" for å finne enheten;
- Fortsett å koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på "Check for updates" -knappen og oppdater RouterOS til den nyeste versjonen;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Last opp nedlastede pakker til WebFig- eller WinBox-"Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen, kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I "QuickSet" -menyen setter du opp følgende: Velg landet ditt for å bruke landsreguleringsinnstillinger;
- Sett opp passordet for det trådløse nettverket ditt i det venstre feltet;
- Sett opp passordet for ruteren din i det nedre feltet;
- Ef þú þarft að nota SIM-kort skaltu opna hulstrið og setja það mótald sem þú vilt í miniPCIe rauf.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihlutir sem framleiðandi hefur samþykkt og hver getur verið Fundið i n upprunalegu umbúðir þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að vera úti á stöng. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar að setja upp. Bilun í að nota leiðréttan vélbúnað og stillingar eða fylgja réttum aðferðum gæti leitt til hættulegra aðstæðna fyrir fólki og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir.
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Til að koma í veg fyrir mengun umhverfisins skaltu aðskilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur til að flytja búnaðinn rétt til tilnefndra söfnunarstaða á þínu svæði.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 255 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.10.1 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter, inkludert drift innen lovlige frekvenskanaler, output strøm, kabling og krav til dynamisk frekvensvalg (DFS). Alle MikroTik-radioenheter må være profesjonelt installert.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-96.png)

Avhengig av hvilken antenne du bruker, må du stille inn dens forsterkning og sette installasjonsinnstillingen til "*Outdoor*". Dette for å sikre at EIRP oppfyller grensen satt av lokale myndigheter.

**Første steg:**

- Åpne det øvre dekselet og koble til en ekstern antenne (obligatorisk);
- Åpne bunndekselet og koble enheten til strømkilden;
- Koble enheten til den medfølgende PoE-injektoren med en Ethernet-kabel til *"data+power"*-enden;
- Koble dataenden av PoE-injektoren til datamaskinen;
- Koble strømadapteren til PoE-injektoren;
- Naviger til delen for nettverkstilkoblinger på datamaskinen og finn det trådløse nettverket kalt "*MikroTik-...*". Fortsett å koble til den (sjekk de trådløse passordene på klistremerket);
- Opprett forbindelse ved hjelp av en mobilapplikasjon. Alternativt kan du bruke WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Start konfigurasjonen innenfor det valgte verktøyet ved hjelp av standard IP-adresse 192.168.88.1. Hvis IP-adressen ikke er tilgjengelig, bruk WinBox og velg fanen "Neighbors" for å finne enheten;
- Fortsett å koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på "Check for updates" -knappen og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig- eller WinBox-"Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen, kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I "QuickSet" -menyen setter du opp følgende: Velg landet ditt for å bruke landsreguleringsinnstillinger;
- Sett opp passordet for det trådløse nettverket ditt i det venstre feltet;
- Sett opp passordet for ruteren din i det nedre feltet;
- Hvis du trenger å bruke et SIM-kort, åpne dekselet og installer ønsket modem i miniPCIe-sporet.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehør godkjent av produsenten, og som kan være funnet i n den originale emballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å være montert utendørs på en stolpe. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke den rette maskinvaren og konfigurasjonen eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak.
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- For å unngå forurensning av miljøet, må du skille enheten fra husholdningsavfall og kaste den på en sikker måte, for eksempel i bestemte områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 255 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.10.1“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi, įskaitant veikimą legaliais dažnių kanalais galios, kabelių ir dinaminio dažnio pasirinkimo (DFS) reikalavimai. Visi „MikroTik“ radijo prietaisai turi būti profesionaliai sumontuota.
Is „NetMetal 5“ serijos trumpasis vadovas apima modelius: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-95.png)

Priklausomai nuo naudojamos antenos, turite nustatyti jos stiprinimą ir nustatyti diegimo nustatymą į „*Outdoor*“. Tuo siekiama užtikrinti, kad EIRP atitiktų vietos valdžios nustatytą ribą.

**Pirmieji žingsniai:**

- Atidarykite viršutinį dangtelį ir prijunkite išorinę anteną (privaloma);
- Atidarykite apatinį dangtelį ir prijunkite įrenginį prie maitinimo šaltinio;
- Prijunkite įrenginį prie pridedamo PoE purkštuko Ethernet kabeliu iki *"data+power"* galo;
- Prijunkite PoE purkštuko duomenų galą prie kompiuterio;
- Prijunkite maitinimo adapterį prie PoE purkštuko;
- Kompiuteryje eikite į tinklo jungčių skyrių ir suraskite belaidį tinklą pavadinimu „*MikroTik-...*“. Prisijunkite prie jo (patikrinkite belaidžio ryšio slaptažodžius ant lipduko);
- Sukurkite ryšį naudodami mobilųjį programėlę. Alternatyviai naudokite WebFig naršyklėje arba konfigūracijos įrankį "WinBox" adresu [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Pradėkite konfigūraciją pasirinktame įrankyje, naudodami numatytąją IP adresą 192.168.88.1. Jei IP adresas nepasiekiamas, naudokite WinBox ir pasirinkite skirtuką "Neighbors", kad rastumėte įrenginį;
- Tęskite prisijungdami naudodami MAC adresą. Vartotojo vardas yra "admin", ir nėra slaptažodžio (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Paspauskite mygtuką "Check for updates" ir atnaujinkite RouterOS iki naujausios versijos;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite prietaisą iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Meniu "QuickSet" nustatykite šiuos parametrus: Pasirinkite savo šalį, kad galėtumėte taikyti šalies reguliavimo nustatymus;
- Nustatykite belaidžio tinklo slaptažodį kairėje srityje;
- Nustatykite maršruto slaptažodį apačioje esančioje srityje;
- Jei reikia naudoti SIM kortelę, atidarykite dėklą ir įdėkite norimą modemą į miniPCIe lizdą.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik maitinimo šaltinį ir gamintojo patvirtinti priedai, kurie gali būti rasta i originali šio gaminio pakuotė.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas skirtas montuoti lauke ant stulpo. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite pataisytos aparatūros ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių.
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Kad išvengtumėte aplinkos užteršimo, atskirkite prietaisą nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 255 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.10.1 vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt profesionāli uzstādītām.
Šī īsā rokasgrāmata paredzēta modelim: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-96.png)

Atkarībā no izmantotās antenas jums jāiestata tās pastiprinājums un instalācijas iestatījums uz '*Outdoor*'. Tas ir paredzēts, lai EIRP atbilstu vietējo iestāžu noteiktajiem ierobežojumiem.

**Pirmie soļi:**

- Atveriet augšējo vāku un pievienojiet ārējo antenu (obligāti);
- Atveriet apakšējo vāku un pievienojiet ierīci strāvas avotam;
- Pievienojiet ierīci komplektā iekļautajam PoE inžektoram ar Ethernet kabeli līdz *"data+power"* galam;
- Pievienojiet PoE inžektora datu galu datoram;
- Pievienojiet strāvas adapteri PoE inžektoram;
- Datorā dodieties uz tīkla savienojumu sadaļu un atrodiet bezvadu tīklu ar nosaukumu "*MikroTik-...*". Turpiniet ar to izveidot savienojumu (pārbaudiet bezvadu paroles uz uzlīmes);
- Izveidojiet savienojumu, izmantojot mobilās lietotnes. Kā alternatīvu varat izmantot WebFig pārlūkprogrammā vai konfigurācijas rīku "WinBox" vietnē [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Sāciet konfigurēt izvēlētajā rīkā, izmantojot noklusēto IP adresi 192.168.88.1. Ja IP adrese nav pieejama, izmantojiet WinBox un izvēlieties cilni "Neighbors", lai atrastu ierīci;
- Turpiniet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjauniniet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamos pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox sadaļu "Files" un pārstartējiet ierīci;
- Atjauninot savu RouterOS programmatūru līdz jaunākajai versijai, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Sadaļā "QuickSet" iestatiet šādi: Izvēlieties savu valsti, lai piemērotu valsts regulējuma iestatījumus;
- Iestatiet savu bezvadu tīkla paroli kreisajā laukumā;
- Iestatiet savu maršrutētāja paroli apakšējā laukumā;
- Ja nepieciešams izmantot SIM karti, atveriet korpusu un ievietojiet vēlamo modemu miniPCIe slotā.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprināto barošanas adapteri un piederumus, kas iekļauti šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai ārā uz staba. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nepareizas aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 255 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.10.1 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż l-operazzjoni fil-kanali tal-frekwenza legali, tal-ħruġ qawwa, ħtiġiet ta 'kejbils, u Reklamar ta' Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom ikunu installat professjonalment.
Din is-serje "NetMetal 5" Gwida ta 'malajr tkopri mudelli: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-96.png)

Jiddependi fuq l-antenna użata, trid tissettja l-gwadann tagħha u ssettja l-issettjar tal-installazzjoni għal '*Outdoor*'. Dan biex jiżgura li l-EIRP jilħaq il-limitu stabbilit mill-awtoritajiet lokali.

**L-ewwel passi:**

- Iftaħ il-qoxra ta 'fuq u qabbad antenna esterna (obbligatorju);
- Iftaħ il-qoxra tal-qiegħ u qabbad l-apparat mas-sors tal-enerġija;
- Qabbad l-apparat mal-injettur PoE inkluż b'kejbil Ethernet mat-tarf *"data+power"*;
- Qabbad it-tarf tad-dejta tal-injettur PoE mal-kompjuter;
- Qabbad l-adapter tal-enerġija mal-injettur PoE;
- Innaviga lejn is-sezzjoni tal-konnessjonijiet tan-netwerk fuq il-kompjuter tiegħek u sib in-netwerk bla fili bl-isem "*MikroTik-...*". Ipproċedi biex tikkonnettja magħha (iċċekkja l-passwords mingħajr fili fuq l-istiker);
- Ewlenija bl-użu ta 'applikazzjoni mobbli. Bħala alternattiva, uża l-WebFig f'browser jew l-għodda ta' konfigurazzjoni "WinBox" fuq [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Ibda l-konfigurazzjoni fi ħdan l-għażla tal-għodda, bl-użu tal-indirizz IP predefinit 192.168.88.1. Jekk l-indirizz IP mhux disponibbli, uża l-WinBox u għażel it-tab "Neighbors" biex issib id-dispożitt;
- Żomm mill-quddiem biex tikkolet b'indirizz MAC. L-username huwa "admin," u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-kodiċijiet tal-utent u t-tal-wi-fi fuq l-isticker);
- Ikklikkja fuq il-buttuna "Check for updates" u agħġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Żid id-pakketti li dawn tniżżel fil-meni "Files" ta 'WebFig jew WinBox u rirreboot l-apparat;
- Billi taġġorna l-software RouterOS għall-aħħar verżjoni, tista 'tiżgura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Fl-menù "QuickSet" iwaqqaf l-iskont segwenti: Agħżel pajjiżek biex tapplika settings tar-regolazzjoni tal-pajjiż;
- Isetta il-password tal-netwerk tal-wi-fi tiegħek fis-suq;
- Isetta il-password tar-router tiegħek fis-suq;
- Jekk għandek bżonn tuża SIM card, iftaħ il-każ u installa l-modem mixtieq tiegħek fis-slot miniPCIe.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il - provvista tal- enerġija u aċċessorji approvati mill-manifattur, u li jistgħu jiġu sibt i n l-imballaġġ oriġinali ta 'dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jintrama fuq barra fuq arblu. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar b’attenzjoni qabel tibda l-installazzjoni. Jekk tonqos milli tuża l- hardware u l-konfigurazzjoni korretta jew issegwi l-proċeduri t-tajba tista 'tirriżulta f'sitwazzjoni perikoluża għan-nies u tagħmel ħsara lis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 255 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.10.1 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften, inclusief werking binnen wettelijke frequentiekanalen, te volgen vermogen, bekabelingseisen en Dynamic Frequency Selection (DFS) -vereisten. Alle MikroTik-radioapparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-96.png)

Afhankelijk van de gebruikte antenne, moet u de versterking instellen en de installatie-instelling op '*Outdoor*' zetten. Dit is om ervoor te zorgen dat EIRP voldoet aan de limiet die door de lokale autoriteiten is vastgesteld.

**Eerste stappen:**

- Open de bovenklep en sluit een externe antenne aan (verplicht);
- Open de onderklep en sluit het apparaat aan op de stroombron;
- Sluit het apparaat aan op de meegeleverde PoE-injector met een Ethernet-kabel aan het *"data+power" -* uiteinde;
- Sluit het gegevensuiteinde van de PoE-injector aan op de computer;
- Sluit de voedingsadapter aan op de PoE-injector;
- Navigeer naar het gedeelte met netwerkverbindingen op uw computer en zoek het draadloze netwerk met de naam "*MikroTik-...*". Ga verder om er verbinding mee te maken (controleer de draadloze wachtwoorden op de sticker);
- Maak verbinding met behulp van een mobiele applicatie. Als alternatief kunt u WebFig gebruiken in een webbrowser of het configuratiehulpmiddel "WinBox" op [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Start de configuratie binnen het gekozen gereedschap met het standaard IP-adres 192.168.88.1. Als het IP-adres niet beschikbaar is, gebruik WinBox en kies het tabblad "Neighbors" om het apparaat te vinden;
- Ga verder met verbinden met behulp van het MAC-adres. De gebruikersnaam is "admin" en er is geen wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- In het "QuickSet"-menu stelt u het volgende in: Kies uw land om landreguleringsinstellingen toe te passen;
- Stel uw draadloze netwerkwachtwoord in het linker veld in;
- Stel uw routerwachtwoord in het onderste veld in;
- Als u een simkaart moet gebruiken, opent u de behuizing en installeert u de gewenste modem in het miniPCIe-slot.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures voor het voorkomen van ongevallen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires goedgekeurd door de fabrikant, en die kunnen zijn gevonden i n de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om buiten op een paal te worden gemonteerd. Lees de montage-instructies zorgvuldig voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Dit is een Klasse A-product. In een huishoudelijke omgeving kan dit product radiostoring veroorzaken. In dat geval moet de gebruiker mogelijk passende maatregelen nemen.
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stroomadapter uit het stopcontact te halen.
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 255 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.10.1 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości wymagania dotyczące zasilania, okablowania i dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być profesjonalnie zainstalowany.
Niniejsza skrócona instrukcja „NetMetal 5” obejmuje modele: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-96.png)

W zależności od zastosowanej anteny należy ustawić jej wzmocnienie i ustawić ustawienie instalacji na '*Outdoor*'. Ma to na celu zapewnienie, że EIRP spełnia limit określony przez władze lokalne.

**Pierwsze kroki:**

- Otwórz górną pokrywę i podłącz antenę zewnętrzną (obowiązkowo);
- Otwórz dolną pokrywę i podłącz urządzenie do źródła zasilania;
- Podłącz urządzenie do dołączonego wtryskiwacza PoE za pomocą kabla Ethernet do końca *"data+power"*;
- Podłącz końcówkę danych wtryskiwacza PoE do komputera;
- Podłącz zasilacz do iniektora PoE;
- Przejdź do sekcji połączeń sieciowych na swoim komputerze i zlokalizuj sieć bezprzewodową o nazwie „*MikroTik-...*”. Kontynuuj, aby się z nim połączyć (sprawdź hasła sieci bezprzewodowej na naklejce);
- Utwórz połączenie za pomocą aplikacji mobilnej. Alternatywnie użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox" pod adresem [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Rozpocznij konfigurację w wybranym narzędziu, używając domyślnego adresu IP 192.168.88.1. Jeśli adres IP nie jest dostępny, użyj WinBoxa i wybierz zakładkę "Neighbors", aby odnaleźć urządzenie;
- Przejdź do połączenia za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła brak (lub, dla niektórych modeli, sprawdź hasła użytkownika i do sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Wgraj pobrane pakiety do menu "Files" w WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu "QuickSet" skonfiguruj następujące: Wybierz swój kraj, aby zastosować ustawienia regulacji krajowej;
- Skonfiguruj hasło do swojej sieci bezprzewodowej w lewym polu;
- Skonfiguruj hasło do routera w dolnym polu;
- Jeśli potrzebujesz użyć karty SIM, otwórz obudowę i zainstaluj żądany modem w gnieździe miniPCIe.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj tylko zasilacza i akcesoria zatwierdzone przez producenta, i które mogą być znaleziony w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Produkt przeznaczony jest do montażu na zewnątrz na słupie. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie odpowiedniego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe. W takim przypadku użytkownik może zostać zobowiązany do podjęcia odpowiednich kroków.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 255 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.10.1 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais de frequência legal, saída requisitos de alimentação, cabeamento e Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalado profissionalmente.
Este Guia Rápido da série "NetMetal 5" abrange modelos: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-96.png)

Dependendo da antena usada, você deve definir seu ganho e definir a configuração de instalação para '*Outdoor*'. Isso é para garantir que o PIRP atenda ao limite estabelecido pelas autoridades locais.

**Primeiros passos:**

- Abra a tampa superior e conecte uma antena externa (obrigatório);
- Abra a tampa inferior e conecte o dispositivo à fonte de alimentação;
- Conecte o dispositivo ao injetor PoE incluído com um cabo Ethernet na extremidade *"data+power"*;
- Conecte a extremidade de dados do injetor PoE ao computador;
- Conecte o adaptador de energia ao injetor PoE;
- Navegue até a seção de conexões de rede em seu computador e localize a rede sem fio chamada "*MikroTik-...*". Prossiga para conectar-se a ele (verifique as senhas wireless no adesivo);
- Estabelecer uma conexão usando um aplicativo móvel. Alternativamente, use o WebFig em um navegador da web ou a ferramenta de configuração "WinBox" em [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Inicie a configuração dentro da ferramenta escolhida, usando o endereço IP padrão 192.168.88.1. Se o endereço IP não estiver disponível, use o WinBox e escolha a guia "Neighbors" para encontrar o dispositivo;
- Prossiga para se conectar usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique as senhas do usuário e sem fio no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Carregue os pacotes baixados no menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar seu software RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- No menu "QuickSet", configure o seguinte: Escolha o seu país para aplicar as configurações de regulamentação do país;
- Configure a senha da sua rede sem fio no campo esquerdo;
- Configure a senha do seu roteador no campo inferior;
- Se você precisar usar um cartão SIM, abra o gabinete e instale o modem desejado no slot miniPCIe.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação acessórios aprovados pelo fabricante e que podem ser encontrado na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser montado ao ar livre em um poste. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou do não cumprimento dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 255 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.10.1 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale cerințe de alimentare, cabluri și cerințe de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie să fie instalat profesional.
Acest Ghid rapid seria "NetMetal 5" acoperă modele: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-94.png)

În funcție de antena folosită, trebuie să setați câștigul acesteia și să setați setarea de instalare la „*Outdoor*”. Acest lucru se asigură că EIRP respectă limita stabilită de autoritățile locale.

**Primii pasi:**

- Deschideți capacul superior și conectați o antenă externă (obligatoriu);
- Deschideți capacul inferior și conectați dispozitivul la sursa de alimentare;
- Conectați dispozitivul la injectorul PoE inclus cu un cablu Ethernet la capătul *"data+power"*;
- Conectați capătul de date al injectorului PoE la computer;
- Conectați adaptorul de alimentare la injectorul PoE;
- Navigați la secțiunea de conexiuni la rețea de pe computer și localizați rețeaua fără fir numită „*MikroTik-...*”. Continuați să vă conectați la acesta (verificați parolele wireless de pe autocolant);
- Stabiliți o conexiune folosind o aplicație mobilă. Alternativ, utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox" la [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Începeți configurarea în instrumentul ales, utilizând adresa IP implicită 192.168.88.1. Dacă adresa IP nu este disponibilă, utilizați WinBox și alegeți fila "Neighbors" pentru a găsi dispozitivul;
- Continuați să vă conectați utilizând adresa MAC. Numele de utilizator este "admin", și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless de pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- În meniul "QuickSet" configurați următoarele: Alegeți țara pentru a aplica setările de reglementare ale țării;
- Configurați parola rețelei wireless în câmpul din stânga;
- Configurați parola routerului în câmpul de jos;
- Dacă trebuie să utilizați o cartelă SIM, deschideți carcasa și instalați modemul dorit în slotul miniPCIe.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesorii aprobate de producător și care pot fi găsite Am n ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie montat în aer liber pe un stâlp. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-le într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător al echipamentelor la punctele de colectare desemnate din zona dumneavoastră.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 255 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.10.1 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny, vrátane prevádzky v rámci legálnych frekvenčných kanálov a výstupov požiadavky na energiu, kabeláž a dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť profesionálne nainštalovaný.
Táto stručná príručka „NetMetal 5“ zahŕňa modely: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-96.png)

V závislosti od použitej antény musíte nastaviť jej zisk a nastaviť inštalačné nastavenie na „*Outdoor*“. Tým sa zabezpečí, aby EIRP spĺňal limit stanovený miestnymi orgánmi.

**Prvé kroky:**

- Otvorte horný kryt a pripojte externú anténu (povinné);
- Otvorte spodný kryt a pripojte zariadenie k zdroju napájania;
- Pripojte zariadenie k priloženému PoE injektoru pomocou ethernetového kábla ku koncu *"data+power"*;
- Pripojte dátový koniec PoE injektora k počítaču;
- Pripojte napájací adaptér k PoE injektoru;
- Prejdite do sekcie sieťových pripojení na vašom počítači a nájdite bezdrôtovú sieť s názvom „*MikroTik-...*“. Pripojte sa k nemu (skontrolujte bezdrôtové heslá na nálepke);
- Vytvorte pripojenie pomocou mobilnej aplikácie. Alternatívne použite WebFig v webovom prehliadači alebo nástroj na konfiguráciu "WinBox" na adrese [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Spustite konfiguráciu vo vybranom nástroji s predvolenou IP adresou 192.168.88.1. Ak adresa IP nie je k dispozícii, použite WinBox a vyberte kartu "Neighbors", aby ste zariadenie našli;
- Pokračujte v pripájaní pomocou MAC adresy. Užívateľské meno je "admin" a nie je žiadne heslo (alebo, pre niektoré modely, skontrolujte užívateľské a bezdrôtové heslá na štítku);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v aplikácii WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a bezpečnostné aktualizácie;
- V menu "QuickSet" nastavte nasledujúce: Vyberte svoju krajinu, aby ste aplikovali nastavenia regulácie krajiny;
- Nastavte heslo k vašej bezdrôtovej sieti v ľavom poli;
- Nastavte heslo k vášmu routeru v dolnom poli;
- Ak potrebujete použiť SIM kartu, otvorte puzdro a nainštalujte požadovaný modem do slotu miniPCIe.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájanie a príslušenstvo schválené výrobcom, ktoré môže byť nájdených v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na montáž vonku na stĺp. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať správne, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 255 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.10.1 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom, vključno z delovanjem v legalnih frekvenčnih kanalih, za doseganje rezultatov napajanje, zahteve za kabliranje in zahteve za dinamično izbiro frekvence (DFS). Vse radijske naprave MikroTik morajo biti strokovno nameščen.
Ta hitri vodnik serije "NetMetal 5" zajema modele: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-96.png)

Glede na uporabljeno anteno morate nastaviti njeno ojačanje in nastavitev namestitve na "*Outdoor*". Tako bi zagotovili, da bo EIRP izpolnjeval omejitev, ki so jo postavile lokalne oblasti.

**Prvi koraki:**

- Odprite zgornji pokrov in priključite zunanjo anteno (obvezno);
- Odprite spodnji pokrov in priključite napravo na vir napajanja;
- Povežite napravo s priloženim injektorjem PoE z ethernetnim kablom na koncu *"data+power"*;
- Priključite podatkovni konec injektorja PoE na računalnik;
- Priključite napajalnik na injektor PoE;
- Pomaknite se do razdelka za omrežne povezave na vašem računalniku in poiščite brezžično omrežje z imenom "*MikroTik-...*". Nadaljujte s povezavo (preverite brezžična gesla na nalepki);
- Ustvarite povezavo z uporabo mobilne aplikacije. Kot alternativo uporabite WebFig v spletnem brskalniku ali orodje za konfiguracijo "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Začnite konfiguracijo znotraj izbranega orodja, uporabite privzeti IP naslov 192.168.88.1. Če IP naslov ni na voljo, uporabite WinBox in izberite zavihek "Neighbors", da najdete napravo;
- Nadaljujte s povezovanjem z uporabo MAC naslova. Uporabniško ime je "admin," in gesla ni (ali, za nekatere modele, preverite gesla za uporabnika in brezžična gesla na nalepki);
- Kliknite gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" v aplikaciji WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno delovanje, stabilnost in posodobitve varnosti;
- V meniju "QuickSet" nastavite naslednje: Izberite svojo državo, da uporabite nastavitve regulacije države;
- Nastavite geslo za svoje brezžično omrežje v levem polju;
- Nastavite geslo za svoj usmerjevalnik v spodnjem polju;
- Če morate uporabiti kartico SIM, odprite ohišje in namestite želeni modem v režo miniPCIe.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatki, ki jih je odobril proizvajalec, in ki so lahko najdeno i n originalna embalaža tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen za namestitev na prostem na drog. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba ustrezne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 255 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10.1 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, output kraft, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste vara professionellt installerat.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-96.png)

Beroende på vilken antenn som används måste du ställa in förstärkningen och ställa in installationsinställningen till "*Outdoor*". Detta för att säkerställa att EIRP uppfyller gränsen som fastställts av de lokala myndigheterna.

**Första stegen:**

- Öppna den övre luckan och anslut en extern antenn (obligatoriskt);
- Öppna bottenluckan och anslut enheten till strömkällan;
- Anslut enheten till den medföljande PoE-injektorn med en Ethernet-kabel till *"data+power"* - änden;
- Anslut dataänden på PoE-injektorn till datorn;
- Anslut strömadaptern till PoE-injektorn;
- Navigera till avsnittet för nätverksanslutningar på din dator och leta reda på det trådlösa nätverket som heter "*MikroTik-...*". Fortsätt att ansluta till den (kontrollera de trådlösa lösenorden på klistermärket);
- Skapa en anslutning med hjälp av en mobilapplikation. Alternativt använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" på [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Påbörja konfigurationen inom det valda verktyget med standard IP-adress 192.168.88.1. Om IP-adressen inte är tillgänglig, använd WinBox och välj fliken "Neighbors" för att hitta enheten;
- Fortsätt att ansluta med hjälp av MAC-adressen. Användarnamnet är "admin" och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I menyn "QuickSet" konfigurerar du följande: Välj ditt land för att tillämpa landsregleringsinställningar;
- Ställ in ditt trådlösa nätverkslösenord i det vänstra fältet;
- Ställ in ditt routerlösenord i det nedre fältet;
- Om du behöver använda ett SIM-kort, öppna fodralet och installera önskat modem i miniPCIe-kortplatsen.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast strömförsörjningen och tillbehör som godkänts av tillverkaren, och som kan vara hittades i den ursprungliga förpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att monteras utomhus på en stolpe. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på syste m.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 255 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.10.1或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规，包括在合法频道内操作，输出 电源，布线要求和动态频率选择（DFS）要求。 所有MikroTik无线电设备必须 专业安装。
此“ NetMetal 5”系列快速指南涵盖以下型号：RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*

![](./img/image2020-2-5_9-49-44.badge-97.png)

请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。

有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)

*该产品最重要的技术规格可在本快速指南的最后一页找到。*

可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)

MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)

根據使用的天線，您必須設置其增益並將安裝設置設置為“*Outdoor*”。 这是为了确保EIRP符合地方当局设定的限制。

**第一步：**

- 打开上盖，外接天线（必备）；
- 打开底盖，连接设备电源；
- *使用连接到"data+power"* 端的以太网电缆将设备连接到随附的 PoE 注入器 ；
- 将PoE供电器的数据端连接到电脑；
- 将电源适配器连接到 PoE 供电器；
- 导航到计算机上的网络连接部分，找到名为“ *MikroTik-...*”的无线网络。继续连接（检查标签上的无线密码）；
- 使用移动应用程序建立连接。或者，使用WebFig在Web浏览器中或在[https://mt.lv/winbox](https://mt.lv/winbox) 上的"WinBox"配置工具; **提供多种配置方法以确保可访问性；**
- 在所选工具中使用默认IP地址192.168.88.1开始配置。如果IP地址不可用，请使用WinBox并选择“邻居”选项卡查找设备;
- 继续使用MAC地址进行连接。用户名为"admin"，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）;
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的"Files"菜单，并重新启动设备;
- 通过将RouterOS软件升级到最新版本，可以确保最佳性能、稳定性和安全更新;
- 在"QuickSet"菜单中设置以下内容: 选择您的国家以应用国家法规设置;
- 在左侧字段中设置您的无线网络密码;
- 在底部字段中设置您的路由器密码。；
- 如果您需要使用SIM卡，请打开外壳并将您需要的调制解调器安装到miniPCIe插槽中。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用 电源 和制造商认可的配件, 可以 发现 在此产品的原包装中。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在户外安装在杆子上。 在开始安装之前，请仔细阅读安装说明。 不使用正确的硬件和配置或未遵循正确的程序可能会导致人员受伤和系统损坏 。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 这是A类产品。 在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。

**射频辐射暴露：** 该 MikroTik 设备符合针对不受控制的环境规定的欧盟辐射暴露限制。 此 MikroTik 设备的安装和使用距离您的身体、专业用户或公众不得超过 255 厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.10.1 или до последней версии, чтобы обеспечить соответствие требованиям местных органов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, вывод требования к питанию, кабелям и динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть профессионально установлены.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru) чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-95.png)

В зависимости от используемой антенны, вы должны установить ее усиление и установить настройку установки на «*Outdoor*». Это должно гарантировать соответствие EIRP пределу, установленному местными властями.

**Первые шаги:**

- Откройте верхнюю крышку и подключите внешнюю антенну (обязательно);
- Откройте нижнюю крышку и подключите устройство к источнику питания;
- Подключите устройство к PoE-инжектору, который входит в комплект при помощью кабеля Ethernet к *"data+power"*;
- Подключите конец данных инжектора PoE к компьютеру;
- Подключите адаптер питания к PoE инжектору;
- Перейдите в раздел сетевых подключений на вашем компьютере и найдите беспроводную сеть с именем "*MikroTik-...*" Подключитесь к ней (проверьте пароль беспроводной сети на наклейке);
- Установите соединение с помощью мобильного приложения. В качестве альтернативы используйте WebFig в веб-браузере или инструмент конфигурации "WinBox" доступный по адресу [https://mt.lv/winbox](https://mt.lv/winbox); **существует несколько методов настройки для обеспечения доступности;**
- Начните настройку в выбранном инструменте, используя стандартный IP-адрес 192.168.88.1. Если IP-адрес недоступен, используйте WinBox и выберите вкладку "Neighbors", чтобы найти устройство;
- Продолжайте подключение, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте пользовательские и беспроводные пароли на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" в WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню "QuickSet" настройте следующее: выберите свою страну, чтобы применить настройки регулирования страны;
- Установите пароль для вашей беспроводной сети в левом поле;
- Установите пароль для вашего роутера в нижнем поле;
- Если вам нужно использовать SIM-карту, откройте корпус и установите нужный модем в слот miniPCIe.

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
Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 255 сантиметров от человека.*

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 5150-5350 МГц, 5650-5850 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge-99.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.10.1 або останньої версії, щоб забезпечити відповідність місцевим нормам влади!

Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей короткий посібник серії NetMetal 5 охоплює моделі: RB922UAGS-5HPacT-NM (NetMetal 5 triple), RB922UAGS-5HPacD-NM (NetMetal 5), RB921UAGS-5SHPacD-NM (NetMetal 5SHP), RB921UAGS-5SHPacT-NM (NetMetal 5SHP triple).

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help-ua](https://mt.lv/help-ua)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_14-4-59.badge-19.png)

Залежно від використовуваної антени, потрібно встановити її посилення та встановити для параметра встановлення значення «Outdoor». Це потрібно для того, щоб EIRP відповідав межі, встановленій місцевою владою.

**Перші кроки:**

- Відкрийте верхню кришку і підключіть зовнішню антену (обов'язково);
- Відкрийте нижню кришку і підключіть пристрій до джерела живлення;
- Під’єднайте пристрій до PoE-інжектора, що входить до комплекту, за допомогою кабелю Ethernet до кінця передачі даних+живлення *"data+power"*;
- Підключіть кінець даних PoE-інжектора до комп’ютера;
- Підключіть адаптер живлення до PoE-інжектора;
- Перейдіть до розділу мережевих підключень на вашому комп’ютері та знайдіть бездротову мережу назвою "*MikroTik-...*". Підключіться до цієї мережі (перевірте пароль бездротової мережі на наклейці);
- Встановіть з'єднання за допомогою мобільного додатка. Альтернативно, використовуйте WebFig у веб-браузері, або інструмент конфігурації "WinBox", доступний за адресою [https://mt.lv/winbox](https://mt.lv/winbox); **існує декілька методів налаштування для забезпечення доступності;**
- Розпочніть конфігурацію за допомогою обраного інструменту, використовуючи стандартну IP-адресу 192.168.88.1. Якщо IP-адреса недоступна, використовуйте WinBox і виберіть вкладку "Neighbors", щоб знайти пристрій;
- Продовжуйте підключення, використовуючи MAC-адресу. Ім'я користувача - "admin", і немає пароля (або, для деяких моделей, перевірте паролі користувача та бездротові паролі на наклейці);
- Клацніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" у WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- У меню "QuickSet" встановіть наступне: виберіть свою країну, щоб застосувати налаштування регулювання країни;
- Налаштуйте пароль для вашої бездротової мережі в лівому полі;
- Налаштуйте пароль для вашого маршрутизатора;
- Якщо вам потрібно використовувати SIM-карту, відкрийте корпус і встановіть потрібний модем у слот miniPCIe.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей виріб призначений для монтажу надворі на стовп. Будь ласка, уважно прочитайте інструкції з монтажу перед початком встановлення. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик.
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити - від’єднати адаптер електроживлення від розетки.
- Це продукт класу А. У домашніх умовах цей продукт може призвести до появи радіоперешкод, і в цьому випадку користувачеві може знадобитися вжити належних заходів.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 255 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 5470-5725 МГц (27 дБм).

Справжнім Mikrotikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

![](./img/5b0555ad40518a25f1ceeda790bc115c.badge-14.jpg)

## Federal Communication Commission Interference Statement

![](./img/fcc_logo_ez.badge-86.jpg)
This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Antenna Installation WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in the USA (or where FCC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

Approved Antenna Table:

| Antenna Model | Type | Antenna gain, dBi |
| --- | --- | --- |
| **UNII-1 (5150-5250 MHz) and UNII-3 (5725-5850MHz)** | | |
| MT-482016/N/A | Omnidirectional | 8.5 |
| PA58-24-ANT | Panel | 24 |
| HDDA5W-32-DP2 | Dish | 32 |
| **UNII-2A (5250-5350 MHz) and UNII-2C (5470-5725MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7 |
| MTAS-5G-19D120 | Sector | 19 |

The same type of antenna and lower antenna gain than those listed above in the table may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 255 centimeters from your body, occupational user, or the general public.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

**Antenna Installation WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

Approved Antenna Table:

| Antenna Model | Type | Antenna gain, dBi |
| --- | --- | --- |
| **UNII-1 (5150-5250 MHz) and UNII-3 (5725-5850MHz)** | | |
| MT-482016/N/A | Omnidirectional | 8.5 |
| PA58-24-ANT | Panel | 24 |
| HDDA5W-32-DP2 | Dish | 32 |
| **UNII-2 (5250-5350 MHz) and UNII-2-Extended (5490-5600 MHz, 5650-5730 MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7 |
| MTAS-5G-19D120 | Sector | 19 |

The same type of antenna and lower antenna gain than those listed above may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 255 centimeters from your body, occupational user, or the general public.

## UKCA marking

![](./img/ukca_black_fill.badge-95.gif)

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
      
      5470-5725 MHz / 27 dBm
    
  

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

PoE In Ethernet Port
24 V / 1.2
IP54
-33°..+70°C

:::warning
Please, test your antenna with our device in the accreditation laboratory to be in compliance with EU rules.
:::
\#73191
