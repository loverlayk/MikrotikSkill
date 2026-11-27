# Quick Guide - mANTBox 5 Series

> Models: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s)

**Models: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s)**

![](./img/mt_logo_arrow_v2-02-86.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS 7.10 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
:::

This "mANTBox 5" series Quick Guide covers models: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).

*This is Wireless Network Device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-98.png)

Depending on the antenna used, you must set its gain and set the installation setting to 'Outdoor'. This is to ensure that EIRP meets the limit set by the local authorities. This is done in the *Quickset, CPE* menu.

**First steps:**

- Open the bottom cover and connect the device to the PoE injector from the kit, using an Ethernet cable to the "data+power" end;
- Connect the data end of the PoE injector to the computer;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool [https://mt.lv/winbox](https://mt.lv/winbox);
- Start the configuration within the chosen tool and choose the "Neighbors" tab to find the device;
- Click on the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- For a manual update of the device, visit the products page at [https://mikrotik.com/products](https://mikrotik.com/products) to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the Winbox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet, CPE" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 35 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS 7.10 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби, включително работата в рамките на законни честотни канали, извеждане на продукция изисквания за захранване, окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-93.png)

В зависимост от използваната антена, трябва да настроите нейното усилване и да зададете настройката за инсталиране на '*Outdoor*'. Това е, за да се гарантира, че EIRP отговаря на ограничението, определено от местните власти. Това се прави в менюто *Quickset, CPE*.

**Първи стъпки:**

- Отворете долната капак и свържете устройството с приложения PoE инжектор от комплекта с Ethernet кабел към "data+power" край;
- Свържете края на данните на PoE инжектора към компютъра;
- Свържете адаптера за захранването към PoE инжектора;
- Изтеглете инструмента за конфигурация WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Стартирайте конфигурацията в избрания инструмент и изберете раздела "Neighbors", за да намерите устройството;
- Щракнете върху MAC адреса. Потребителското име е "admin", и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- За ръчно обновяване на устройството, посетете страницата с продукти на [https://mikrotik.com/products](https://mikrotik.com/products), за да намерите вашия продукт. Необходимите пакети са достъпни в менюто "Support&Downloads";
- Качете изтеглените пакети в менюто "Files" на Winbox и рестартирайте устройството;
- Като актуализирате софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации на сигурността;
- В менюто "QuickSet, CPE" настройте следното: Изберете вашата държава, за да приложите настройките за регулиране на държавата;
- Настройте парола за безжичната ви мрежа в лявото поле;
- Настройте парола за вашия рутер в долното поле.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоари, одобрени от производителя, и които могат да бъдат намерено аз n оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за монтиране на открито върху стълб. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате подходящия хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата на системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се изисква да предприеме адекватни мерки.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определени пунктове за събиране във вашия район.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 35 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS 7.10 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupů požadavky na napájení, kabeláž a dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být profesionálně nainstalován.
Tato rychlá příručka „mANTBox 5“ zahrnuje modely: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-93.png)

V závislosti na použité anténě musíte nastavit její zisk a nastavit instalační nastavení na „*Outdoor*“. To má zajistit, že EIRP splňuje limit stanovený místními úřady. To se provádí v nabídce *Quickset, CPE*.

**První kroky:**

- Otevřete spodní kryt a připojte zařízení k dodávanému PoE injektoru z balení pomocí ethernetového kabelu na konec "data+power“;
- Připojte konec datového vstřikovače PoE k počítači;
- Připojte adaptér k napájecímu vstřikovači PoE;
- Stáhněte konfigurační nástroj WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Spusťte konfiguraci v zvoleném nástroji a vyberte kartu "Neighbors", abyste našli zařízení;
- Klepněte na MAC adresu. Uživatelské jméno je "admin" a není žádné heslo (nebo, u některých modelů, zkontrolujte uživatelská a bezdrátová hesla na samolepce);
- Pro ruční aktualizaci zařízení navštivte stránku produktů na [https://mikrotik.com/products](https://mikrotik.com/products), abyste našli svůj produkt. Požadované balíčky jsou dostupné v nabídce "Support&Downloads";
- Nahrajte stažené balíčky do nabídky "Files" v aplikaci Winbox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce "QuickSet, CPE" nastavte následující: Vyberte svou zem, abyste aplikovali nastavení pro regulaci země;
- Nastavte heslo pro bezdrátovou síť v levém poli;
- Nastavte heslo pro váš router v dolním poli.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájení a příslušenství schválené výrobcem, které může být nalezeno v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k montáži venku na sloup. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete odpovídající hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobit rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- Abyste zabránili kontaminaci životního prostředí, oddělte zařízení od domovního odpadu a zlikvidujte jej bezpečným způsobem, například na místech k tomu určených. Seznamte se s postupy správné přepravy zařízení do určených sběrných míst ve vaší oblasti.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 35 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS 7.10 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler, herunder drift inden for lovlige frekvenskanaler, output strøm, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal være professionelt installeret.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-93.png)

Afhængigt af den anvendte antenne skal du indstille dens forstærkning og indstille installationsindstillingen til '*Outdoor*'. Dette er for at sikre, at EIRP overholder grænsen fastsat af de lokale myndigheder. Dette gøres i *Quickset, CPE*-menuen.

**Første trin:**

- Åbn bunddækslet og tilslut enheden til den medfølgende PoE-injektor fra sættet ved hjælp af et Ethernet-kabel til "data+power"-enden;
- Tilslut dataenden af PoE-injektoren til computeren;
- Tilslut strømadapteren til PoE-injektoren;
- Download WinBox-konfigurationsværktøjet [https://mt.lv/winbox](https://mt.lv/winbox);
- Start konfigurationen inden for det valgte værktøj og vælg fanen "*Neighbors*" for at finde enheden;
- Klepněte na MAC adresu. Uživatelské jméno je "admin", a není žádné heslo (nebo, u některých modelů, zkontrolujte uživatelská a bezdrátová hesla na samolepce);
- For en manuel opdatering af enheden, besøg produktsiden på [https://mikrotik.com/products](https://mikrotik.com/products) for at finde dit produkt. Požadované balíčky jsou dostupné v nabídce "Support&Downloads";
- Nahrajte stažené balíčky do nabídky "Files" v aplikaci Winbox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce "QuickSet, CPE" nastavte následující: Vyberte svou zem, abyste aplikovali nastavení pro regulaci země;
- Nastavte heslo pro bezdrátovou síť v levém poli;
- Nastavte heslo pro váš router v dolním poli.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og tilbehør godkendt af producenten, og som kan være fundet i den originale emballage af dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive monteret udendørs på en stang. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.
- For at undgå forurening af miljøet skal du adskille apparatet fra husholdningsaffald og bortskaffe det på en sikker måde, f.eks. i afmærkede områder. Bliv fortrolig med procedurer for korrekt transport af udstyret til udpegede indsamlingssteder i dit område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 35 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS 7.10 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle und der Ausgabe Anforderungen an Stromversorgung, Verkabelung und dynamische Frequenzauswahl (Dynamic Frequency Selection, DFS). Alle MikroTik Funkgeräte müssen professionell installiert.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-93.png)

Je nach verwendeter Antenne müssen Sie deren Verstärkung einstellen und die Installationseinstellung auf „*Outdoor*“ stellen. Dadurch soll sichergestellt werden, dass die EIRP den von den lokalen Behörden festgelegten Grenzwert einhält. Dies geschieht im *Quickset, CPE*-Menü.

**Erste Schritte:**

- Öffnen Sie die untere Abdeckung und schließen Sie das Gerät an den mitgelieferten PoE-Injektor mit einem Ethernet-Kabel am "data+power"-Ende an;
- Schließen Sie das Datenende des PoE-Injektors am Computer an;
- Schließen Sie den Netzadapter am PoE-Injektor an;
- Laden Sie das WinBox-Konfigurationstool herunter: [https://mt.lv/winbox](https://mt.lv/winbox);
- Starten Sie die Konfiguration mit dem ausgewählten Tool und wählen Sie den Tab "*Neighbors*", um das Gerät zu finden;
- Klicken Sie auf die MAC-Adresse. Der Benutzername ist "admin", und es gibt kein Passwort (oder überprüfen Sie bei einigen Modellen Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Für ein manuelles Update des Geräts besuchen Sie die Produktseite unter [https://mikrotik.com/products](https://mikrotik.com/products), um Ihr Produkt zu finden. Die erforderlichen Pakete finden Sie im Menü "Support&Downloads";
- Laden Sie die heruntergeladenen Pakete im Winbox-Menü "Dateien" hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie eine optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Im Menü "QuickSet, CPE" richten Sie folgendes ein: Wählen Sie Ihr Land, um die länderspezifischen Einstellungen anzuwenden;
- Richten Sie Ihr drahtloses Netzwerkkennwort im linken Feld ein;
- Richten Sie Ihr Router-Passwort im unteren Feld ein.

**Sicherheitsinformation:**

- Machen Sie sich vor Arbeiten an MikroTik-Geräten mit den Gefahren elektrischer Schaltkreise vertraut und machen Sie sich mit den üblichen Vorgehensweisen zur Unfallverhütung vertraut. Der Installateur sollte mit den Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das Netzteil und vom Hersteller zugelassenes Zubehör, und das kann sein gefunden In der Originalverpackung dieses Produkts.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Vorschriften für elektrische Geräte entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Montage im Freien an einer Stange vorgesehen. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie die richtige Hardware und Konfiguration nicht verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zur Beschädigung des Systems führen.
- Wir können nicht garantieren, dass durch unsachgemäßen Gebrauch des Geräts keine Unfälle oder Schäden entstehen. Bitte verwenden Sie dieses Produkt mit Vorsicht und betreiben Sie es auf eigenes Risiko!
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise geeignete Maßnahmen ergreifen.
- Im Falle eines Gerätefehlers trennen Sie das Gerät bitte von der Stromversorgung. Der schnellste Weg, dies zu tun, besteht darin, den Netzadapter aus der Steckdose zu ziehen.
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, beispielsweise an den dafür vorgesehenen Stellen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Ausrüstung zu ausgewiesenen Sammelstellen in Ihrer Nähe vertraut.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 35 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS 7.10 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών, συμπεριλαμβανομένης της λειτουργίας εντός των νόμιμων καναλιών συχνότητας, της παραγωγής ισχύ, απαιτήσεις καλωδίωσης και απαιτήσεις δυναμικής επιλογής συχνότητας (DFS). Όλες οι ασύρματες συσκευές MikroTik πρέπει να είναι επαγγελματικά εγκατεστημένο.
Αυτός ο γρήγορος οδηγός σειράς "mANTBox 5" καλύπτει μοντέλα: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-93.png)

Ανάλογα με την κεραία που χρησιμοποιείται, πρέπει να ρυθμίσετε το κέρδος της και να ορίσετε τη ρύθμιση εγκατάστασης σε «*Outdoor*». Αυτό γίνεται για να διασφαλιστεί ότι το EIRP πληροί το όριο που έχουν θέσει οι τοπικές αρχές. Αυτό γίνεται στο μενού *Quickset, CPE*.

**Πρώτα βήματα:**

- Ανοίξτε το κάτω κάλυμμα και συνδέστε τη συσκευή στον εγχυτήρα PoE από το κιτ, χρησιμοποιώντας ένα καλώδιο Ethernet στο άκρο "*data+power*".
- Συνδέστε το άκρο δεδομένων του εγχυτήρα PoE στον υπολογιστή.
- Συνδέστε το τροφοδοτικό στον εγχυτήρα PoE.
- Κατεβάστε το εργαλείο διαμόρφωσης WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Ξεκινήστε τη διαμόρφωση μέσα στο επιλεγμένο εργαλείο και επιλέξτε την καρτέλα "*Neighbors*" για να βρείτε τη συσκευή.
- Κάντε κλικ στη διεύθυνση MAC. Το όνομα χρήστη είναι "admin" και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματου δικτύου στο αυτοκόλλητο).
- Για μη αυτόματη ενημέρωση της συσκευής, επισκεφτείτε τη σελίδα προϊόντων στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products) για να βρείτε το προϊόν σας. Τα απαιτούμενα πακέτα είναι προσβάσιμα από το μενού *"Support&Downloads".*
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού *Winbox"Files"* και επανεκκινήστε τη συσκευή.
- Αναβαθμίζοντας το λογισμικό RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας.
- Στο μενού *"QuickSet, CPE"* ρυθμίστε τα εξής: Επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις κανονισμού χώρας.
- Ρυθμίστε τον κωδικό πρόσβασης του ασύρματου δικτύου σας στο αριστερό πεδίο.
- Ορίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την παροχή ρεύματος και αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και ποια μπορεί να είναι βρέθηκαν στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται να τοποθετηθεί σε εξωτερικό χώρο σε έναν πόλο. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του υλικού και των ρυθμίσεων διόρθωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Πρόκειται για προϊόν κλάσης Α. Σε οικιακό περιβάλλον, αυτό το προϊόν μπορεί να προκαλέσει ραδιοπαρεμβολές, οπότε ενδέχεται να χρειαστεί να ληφθούν τα κατάλληλα μέτρα από τον χρήστη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από τα οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένους χώρους. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 35 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS 7.10 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales legales de frecuencia, salida alimentación, requisitos de cableado y requisitos de selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-95.png)

Dependiendo de la antena utilizada, debe configurar su ganancia y establecer la configuración de instalación en '*Outdoor*'. Esto es para garantizar que EIRP cumpla con el límite establecido por las autoridades locales. Esto se hace en el menú *Quickset, CPE*.

**Primeros pasos:**

- Abra la tapa inferior y conecte el dispositivo al inyector PoE del kit, utilizando un cable Ethernet en el extremo "*data+power"*;
- Conecte el extremo de datos del inyector PoE a la computadora;
- Conecte el adaptador de corriente al inyector PoE;
- Descargue la herramienta de configuración de WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Inicie la configuración dentro de la herramienta elegida y elija la pestaña "*Neighbors*" para encontrar el dispositivo;
- Haga clic en la dirección MAC. El nombre de usuario es "admin" y no hay contraseña (o, en algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Para una actualización manual del dispositivo, visite la página de productos en [https://mikrotik.com/products](https://mikrotik.com/products) para encontrar su producto. Se puede acceder a los paquetes requeridos en el menú *"Support&Downloas*;
- Cargue los paquetes descargados en el menú *Winbox"Files"* y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento óptimo, estabilidad y actualizaciones de seguridad;
- En el menú *"QuickSet, CPE"* configure lo siguiente: Elija su país para aplicar la configuración de regulación del país;
- Configure la contraseña de su red inalámbrica en el campo izquierdo;
- Configure la contraseña de su enrutador en el campo inferior.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Use solo la fuente de alimentación y accesorios aprobados por el fabricante, y que pueden ser encontró En el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para montarse en exteriores en un poste. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podrían producir situaciones peligrosas para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- Este es un producto de clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- La toma de corriente se instalará cerca del equipo y será de fácil acceso.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de los residuos domésticos y deséchelo de forma segura, por ejemplo, en áreas designadas. Familiarícese con los procedimientos para transportar adecuadamente el equipo a los puntos de recolección designados en su área.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 35 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

*RB921GS-5HPacD-15S*: Módulo inalámbrico integrado que opera a 5 GHz, protocolo 802.11 a/n/ac con antena sectorial integrada, ganancia máxima 15 dBi.

*RB921GS-5HPacD-19S*: Módulo inalámbrico integrado que opera a 5 GHz, protocolo 802.11 a/n/ac con antena sectorial integrada, ganancia máxima 19 dBi.

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
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS 7.10 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas toimimist seaduslikes sageduskanalites, väljund võimsus, kaabeldusnõuded ja dünaamilise sageduse valiku (DFS) nõuded. Kõik MikroTiku raadioseadmed peavad olema professionaalselt paigaldatud.
See "mANTBox 5" seeria lühijuhend hõlmab mudeleid: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-93.png)

Olenevalt kasutatavast antennist peate määrama selle võimenduse ja seadma paigaldussäteteks '*Outdoor*'. Selle eesmärk on tagada, et EIRP järgiks kohalike võimude kehtestatud piirmäära. Seda tehakse menüüs *Quickset, CPE*.

**Esimesed sammud:**

- Avage alumine kaas ja ühendage seade komplekti kuuluva PoE-pihustiga, kasutades Etherneti kaablit " *data+power*" otsaga;
- Ühendage PoE-pihusti andmeots arvutiga;
- Ühendage toiteadapter PoE-pihustiga;
- Laadige alla WinBoxi seadistamise tööriist [https://mt.lv/winbox](https://mt.lv/winbox);
- Käivitage valitud tööriistas konfigureerimine ja valige seadme leidmiseks vahekaart "*Neighbors*";
- Klõpsake MAC-aadressil. Kasutajanimi on "admin" ja parool puudub (või mõne mudeli puhul kontrollige kleebiselt kasutaja ja traadita ühenduse paroole);
- Seadme käsitsi värskendamiseks külastage oma toote leidmiseks toodete lehte aadressil [https://mikrotik.com/products](https://mikrotik.com/products). Vajalikud paketid on kättesaadavad menüüst *"Support&Downloads"*;
- Laadige allalaaditud paketid üles menüüsse *Winbox"Files"* ja taaskäivitage seade;
- Uuendades oma RouterOS-i tarkvara uusimale versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Menüüs *"QuickSet, CPE"* seadistage järgmine: Valige oma riik, et rakendada riigi reguleerimise sätteid;
- Seadistage vasakpoolsel väljal traadita võrgu parool;
- Seadistage alumisel väljal ruuteri parool.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult toiteallikat ja tootja poolt heaks kiidetud lisaseadmed, mis võivad olla leitud ma olen selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud paigaldamiseks välistingimustele. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Parandatud riistvara ja konfiguratsiooni kasutamata jätmine või õigete toimingute järgimata jätmine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist.
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja visake see ohutul viisil, näiteks selleks ettenähtud kohtadesse. Tutvuge seadmete õige transportimise protseduuridega teie piirkonnas määratud kogumispunktidesse.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 35 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS 7.10 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtö teho, kaapelointivaatimukset ja dynaamisen taajuuden valinnan (DFS) vaatimukset. Kaikkien MikroTik-radiolaitteiden on oltava ammattimaisesti asennettu.
Tämä "mANTBox 5" -sarjan pikaopas kattaa mallit: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi) Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-93.png)

Käytetystä antennista riippuen sinun on asetettava sen vahvistus ja asetettava asennusasetukseksi "*Outdoor*". Tällä varmistetaan, että EIRP täyttää paikallisten viranomaisten asettaman rajan. Tämä tehdään *Quickset, CPE* -valikossa.

**Ensiaskeleet:**

- Avaa pohjakansi ja liitä laite sarjan PoE-injektoriin Ethernet-kaapelilla "*data+power*"-päähän;
- Liitä PoE-injektorin datapää tietokoneeseen;
- Liitä virtalähde PoE-suuttimeen;
- Lataa WinBox-määritystyökalu [https://mt.lv/winbox](https://mt.lv/winbox);
- Aloita konfigurointi valitussa työkalussa ja etsi laite valitsemalla Naapurit-välilehti;
- Napsauta MAC-osoitetta. Käyttäjätunnus on "admin", eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Jos haluat päivittää laitteen manuaalisesti, vieraile tuotesivulla osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products) löytääksesi tuotteesi. Tarvittavat paketit löytyvät *"Support&Downloads*" -valikosta;
- Lataa ladatut paketit *Winbox"Files"* -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja tietoturvapäivitykset;
- *Määritä "QuickSet, CPE"-* valikossa seuraavat: Valitse maasi ottaaksesi käyttöön maakohtaiset asetukset;
- Aseta langattoman verkon salasana vasemmassa kentässä;
- Aseta reitittimen salasana alakenttään.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain virtalähdettä ja valmistajan hyväksymät lisävarusteet, jotka voivat olla löydetty Olen tämän tuotteen alkuperäispakkaus.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi ulkona sauvaan. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet.
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla, esimerkiksi niille osoitetuille alueille. Tutustu menetelmiin, joilla laitteet kuljetetaan asianmukaisesti alueellasi oleviin keräyspisteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on ja Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 35 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS 7.10 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la sortie les exigences d'alimentation, de câblage et de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installé professionnellement.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-93.png)

En fonction de l'antenne utilisée, vous devez régler son gain et régler le paramètre d'installation sur '*Outdoor*'. Il s'agit de s'assurer que l'EIRP respecte la limite fixée par les autorités locales. Cela se fait dans le menu *Quickset, CPE*.

**Premiers pas:**

- Ouvrez le capot inférieur;
- Ouvrez le capot inférieur et connectez l'appareil à l'injecteur PoE du kit, à l'aide d'un câble Ethernet à l'extrémité "*data+power"*;
- Connectez l'extrémité des données de l'injecteur PoE à l'ordinateur;
- Connectez l'adaptateur secteur à l'injecteur PoE;
- Téléchargez l'outil de configuration WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Démarrez la configuration au sein de l'outil choisi et choisissez l'onglet "*Neighbors*" pour rechercher l'appareil;
- Cliquez sur l'adresse MAC. Le nom d'utilisateur est "admin" et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Pour une mise à jour manuelle de l'appareil, visitez la page des produits sur [https://mikrotik.com/products](https://mikrotik.com/products) pour trouver votre produit. Les forfaits requis sont accessibles sous le menu *"Support&Downloads"*;
- Téléchargez les packages téléchargés dans le menu *Winbox"Files"* et redémarrez l'appareil;
- En mettant à niveau votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances, une stabilité et des mises à jour de sécurité optimales;
- Dans le menu *"QuickSet, CPE",* configurez les éléments suivants: Choisissez votre pays pour appliquer les paramètres de réglementation du pays;
- Configurez le mot de passe de votre réseau sans fil dans le champ de gauche;
- Configurez le mot de passe de votre routeur dans le champ du bas.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l' alimentation et accessoires approuvés par le fabricant, et qui peuvent être a trouvé dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être monté à l'extérieur sur un poteau. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration corrects ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- Pour éviter toute contamination de l'environnement, séparez l'appareil des déchets ménagers et jetez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures permettant de transporter correctement l'équipement vers les points de collecte désignés dans votre région.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 35 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS 7.10 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala zahtjevi za napajanje, kabliranje i zahtjevi za dinamički odabir frekvencije (DFS). Svi MikroTik radijski uređaji moraju biti profesionalno instaliran.
Ovaj kratki vodič serije "mANTBox 5" obuhvaća modele: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-93.png)

Ovisno o korištenoj anteni, morate postaviti njezino pojačanje i postaviti postavku instalacije na '*Outdoor*'. Time se osigurava da EIRP zadovoljava ograničenje koje su postavile lokalne vlasti. To se radi u *Quickset, CPE* izborniku.

**Prvi koraci:**

- Otvorite donji poklopac i spojite uređaj na PoE injektor iz kompleta, koristeći Ethernet kabel na "*data+power*" kraj;
- Spojite podatkovni kraj PoE injektora na računalo;
- Spojite strujni adapter na PoE injektor;
- Preuzmite WinBox konfiguracijski alat [https://mt.lv/winbox](https://mt.lv/winbox);
- Pokrenite konfiguraciju unutar odabranog alata i odaberite karticu "*Neighbors*" kako biste pronašli uređaj;
- Kliknite na MAC adresu. Korisničko ime je "admin", a nema zaporke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Za ručno ažuriranje uređaja posjetite stranicu proizvoda na [https://mikrotik.com/products](https://mikrotik.com/products) kako biste pronašli svoj proizvod. Traženi paketi dostupni su u izborniku *"Support&Downloads"*;
- Učitajte preuzete pakete u izbornik *Winbox"Files"* i ponovno pokrenite uređaj;
- Nadogradnjom vašeg RouterOS softvera na najnoviju verziju, možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U izborniku *"QuickSet, CPE"* postavite sljedeće: Odaberite svoju državu kako biste primijenili postavke propisa zemlje;
- U lijevom polju postavite lozinku bežične mreže;
- Postavite zaporku vašeg usmjerivača u donjem polju.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobren od proizvođača, a može biti pronađeno Ja nisam originalno pakiranje ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen postavljanju vani na stup. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne slijedite ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere.
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- Kako biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, primjerice, na za to predviđenim mjestima. Upoznajte se s postupcima za pravilan transport opreme do određenih sabirnih mjesta u vašem području.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 35 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS 7.10-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon keresztüli működést is teljesítményre, kábelezésre és dinamikus frekvenciaválasztásra (DFS) vonatkozó követelmények. Az összes MikroTik rádiókészüléknek lennie kell szakszerűen telepítve.
Ez a "mANTBox 5" sorozat Gyors útmutató a következő modellekre terjed ki: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-93.png)

A használt antennától függően be kell állítania az erősítést, és a telepítési beállítást "*Outdoor*"-re kell állítani. Ezzel biztosítható, hogy az EIRP megfeleljen a helyi hatóságok által meghatározott határértéknek. Ez a *Quickset, CPE* menüben történik.

**Első lépések:**

- Nyissa fel az alsó fedelet, és csatlakoztassa az eszközt a készlet PoE befecskendezőjéhez Ethernet-kábellel az "*data+power"* végéhez;
- Csatlakoztassa a PoE injektor adatvégét a számítógéphez;
- Csatlakoztassa a hálózati adaptert a PoE befecskendezőhöz;
- Töltse le a WinBox konfigurációs eszközt [https://mt.lv/winbox](https://mt.lv/winbox);
- Indítsa el a konfigurációt a kiválasztott eszközön belül, és válassza a "*Neighbors*" fület az eszköz megkereséséhez;
- Kattintson a MAC-címre. A felhasználónév "admin", és nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Az eszköz kézi frissítéséhez keresse fel a termékek oldalát a [https://mikrotik.com/products](https://mikrotik.com/products) címen, és keresse meg termékét. *A szükséges csomagok a "Support&Downloads"* menü alatt érhetők el;
- Töltse fel a letöltött csomagokat a *Winbox"Files"* menübe, és indítsa újra az eszközt;
- A RouterOS szoftverének a legújabb verzióra való frissítésével optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- A *"QuickSet, CPE"* menüben állítsa be a következőket: Válassza ki az országot az országszabályozási beállítások alkalmazásához;
- Állítsa be vezeték nélküli hálózati jelszavát a bal oldali mezőben;
- Állítsa be az útválasztó jelszavát az alsó mezőben.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak az áramellátást használja és a gyártó által jóváhagyott kiegészítők, amelyek lehetnek megtalált A termék eredeti csomagolása.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket szabadon, egy oszlopra kell felszerelni. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helyes hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását eredményezheti.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, amely esetben a felhasználót fel kell kérni a megfelelő intézkedések megtételére.
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- A környezet szennyeződésének elkerülése érdekében a készüléket különítse el a háztartási hulladéktól, és biztonságos módon, például a kijelölt helyen dobja ki. Ismerkedjen meg a berendezés megfelelő szállítási eljárásaival az Ön területén található kijelölt gyűjtőhelyekre.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 35 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS 7.10 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali, incluso il funzionamento nei canali di frequenza legali, in uscita requisiti di alimentazione, cablaggio e selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installato professionalmente.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-93.png)

A seconda dell'antenna utilizzata, è necessario impostarne il guadagno e impostare l'impostazione di installazione su '*Outdoor*'. Questo per garantire che l'EIRP soddisfi il limite fissato dalle autorità locali. Questo viene fatto nel menu *Quickset, CPE*.

**Primi passi:**

- Aprire il coperchio inferiore e collegare il dispositivo all'iniettore PoE presente nel kit, utilizzando un cavo Ethernet all'estremità "*data+power*";
- Collegare l'estremità dati dell'iniettore PoE al computer;
- Collegare l'adattatore di alimentazione all'iniettore PoE;
- Scarica lo strumento di configurazione WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Avvia la configurazione all'interno dello strumento scelto e scegli la scheda "*Neighbors*" per trovare il dispositivo;
- Fare clic sull'indirizzo MAC. Il nome utente è "admin" e non è presente alcuna password (o, per alcuni modelli, controllare l'utente e le password wireless sull'adesivo);
- Per un aggiornamento manuale del dispositivo, visita la pagina dei prodotti su [https://mikrotik.com/products](https://mikrotik.com/products) per trovare il tuo prodotto. I pacchetti richiesti sono accessibili dal menu *"Support&Downloads"*;
- Carica i pacchetti scaricati nel menu *Winbox"Files"* e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni, stabilità e aggiornamenti di sicurezza ottimali;
- Nel menu *"QuickSet, CPE"* impostare quanto segue: Scegli il tuo paese, per applicare le impostazioni della regolamentazione nazionale;
- Imposta la password della tua rete wireless nel campo a sinistra;
- Imposta la password del tuo router nel campo in basso.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l' alimentatore e accessori approvati dal produttore e quali possono essere trovato nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è progettato per essere montato all'esterno su un'asta. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il rispetto delle procedure corrette potrebbe comportare una situazione pericolosa per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio nelle aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura nei punti di raccolta designati nella propria zona.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 35 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS 7.10 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum, þar með talið rekstri innan löglegra tíðnisviða, framleiðsla afl, kaðall kröfur og Dynamic Frequency Val (DFS) kröfur. Öll MikroTik útvarpstæki verða að vera faglega sett upp.
Þessi „mANTBox 5“ röð snöggvísunar nær yfir módel: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-93.png)

Það fer eftir loftnetinu sem er notað, þú verður að stilla styrk þess og stilla uppsetningarstillinguna á '*Outdoor*'. Þetta er til að tryggja að EIRP standist þau mörk sem sveitarfélögin setja. Þetta er gert í *Quickset, CPE* valmyndinni.

**Fyrstu skrefin:**

- Opnaðu botnlokið og tengdu tækið við PoE inndælingartækið úr settinu með því að nota Ethernet snúru að "*data+power"* endanum;
- Tengdu gagnaenda PoE inndælingartækisins við tölvuna;
- Tengdu straumbreytinn við PoE inndælingartækið;
- Sækja WinBox stillingar tól [https://mt.lv/winbox](https://mt.lv/winbox);
- Byrjaðu uppsetninguna í völdu tólinu og veldu "*Neighbors*" flipann til að finna tækið;
- Smelltu á MAC vistfangið. Notandanafnið er "admin" og það er ekkert lykilorð (eða, fyrir sumar gerðir, athugaðu notenda- og þráðlaus lykilorð á límmiðanum);
- Til að fá handvirka uppfærslu á tækinu skaltu fara á vörusíðuna á [https://mikrotik.com/products](https://mikrotik.com/products) til að finna vöruna þína. Nauðsynlegir pakkar eru aðgengilegir undir *"Support&Downloads"* valmyndinni;
- Hladdu niður niðurhaluðum pakka í *Winbox"Files"* valmyndina og endurræstu tækið;
- Með því að uppfæra RouterOS hugbúnaðinn þinn í nýjustu útgáfuna geturðu tryggt hámarksafköst, stöðugleika og öryggisuppfærslur;
- Í *"QuickSet, CPE"* valmyndinni skaltu setja upp eftirfarandi: Veldu land þitt, til að beita landsreglustillingum;
- Settu upp lykilorðið þitt fyrir þráðlausa netið í vinstri reitnum;
- Settu upp lykilorðið þitt fyrir leiðina í neðsta reitnum.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihlutir sem framleiðandi hefur samþykkt og hver getur verið Fundið i n upprunalegu umbúðir þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að vera úti á stöng. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar að setja upp. Bilun í að nota leiðréttan vélbúnað og stillingar eða fylgja réttum aðferðum gæti leitt til hættulegra aðstæðna fyrir fólki og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir.
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Til að forðast mengun umhverfisins skal skilja tækið frá heimilissorpi og farga því á öruggan hátt, td á afmörkuðum svæðum. Kynntu þér verklagsreglur um að flytja búnaðinn á viðeigandi söfnunarstaði á þínu svæði.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 35 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS 7.10 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter, inkludert drift innen lovlige frekvenskanaler, output strøm, kabling og krav til dynamisk frekvensvalg (DFS). Alle MikroTik-radioenheter må være profesjonelt installert.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-93.png)

Avhengig av antennen som brukes, må du stille inn forsterkningen og sette installasjonsinnstillingen til "*Outdoor*". Dette for å sikre at EIRP holder grensen fastsatt av lokale myndigheter. Dette gjøres i *Quickset, CPE*-menyen.

**Første steg:**

- Åpne bunndekselet og koble enheten til PoE-injektoren fra settet ved hjelp av en Ethernet-kabel til "*data+power* "-enden;
- Koble dataenden av PoE-injektoren til datamaskinen;
- Koble strømadapteren til PoE-injektoren;
- Last ned WinBox-konfigurasjonsverktøy [https://mt.lv/winbox](https://mt.lv/winbox);
- Start konfigurasjonen i det valgte verktøyet og velg fanen "*Neighbors*" for å finne enheten;
- Klikk på MAC-adressen. Brukernavnet er "admin", og det er ikke noe passord (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- For en manuell oppdatering av enheten, besøk produktsiden på [https://mikrotik.com/products](https://mikrotik.com/products) for å finne produktet ditt. De nødvendige pakkene er tilgjengelige under *"Support&Downloads"*-menyen;
- Last ned nedlastede pakker til *Winbox"Files"-* menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I *"QuickSet, CPE"-* menyen konfigurerer du følgende: Velg ditt land for å bruke landreguleringsinnstillinger;
- Sett opp passordet for det trådløse nettverket i venstre felt;
- Sett opp ruterpassordet i det nederste feltet.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehør godkjent av produsenten, og som kan være funnet i n den originale emballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å være montert utendørs på en stolpe. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke den rette maskinvaren og konfigurasjonen eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak.
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- For å unngå forurensning av miljøet, separer enheten fra husholdningsavfallet og kast den på en sikker måte, for eksempel i anviste områder. Gjør deg kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 35 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS 7.10“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi, įskaitant veikimą legaliais dažnių kanalais galios, kabelių ir dinaminio dažnio pasirinkimo (DFS) reikalavimai. Visi „MikroTik“ radijo prietaisai turi būti profesionaliai sumontuota.
Is „mANTBox 5“ serijos trumpasis vadovas apima modelius: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-92.png)

Priklausomai nuo naudojamos antenos, turite nustatyti jos stiprinimą ir nustatyti diegimo nustatymą į „*Outdoor*“. Taip siekiama užtikrinti, kad EIRP atitiktų vietos valdžios institucijų nustatytą ribą. Tai atliekama meniu *Quickset, CPE*.

**Pirmieji žingsniai:**

- Atidarykite apatinį dangtelį ir prijunkite įrenginį prie PoE purkštuko iš rinkinio, naudodami eterneto kabelį prie "*data+power"* galo;
- Prijunkite PoE purkštuko duomenų galą prie kompiuterio;
- Prijunkite maitinimo adapterį prie PoE purkštuko;
- Atsisiųskite "WinBox" konfigūravimo įrankį [https://mt.lv/winbox](https://mt.lv/winbox);
- Pradėkite konfigūraciją pasirinktame įrankyje ir pasirinkite skirtuką "*Neighbors*", kad surastumėte įrenginį;
- Spustelėkite MAC adresą. Vartotojo vardas yra "admin", o slaptažodžio nėra (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Norėdami rankiniu būdu atnaujinti įrenginį, apsilankykite produktų puslapyje adresu [https://mikrotik.com/products](https://mikrotik.com/products) ir suraskite savo gaminį. Reikalingus paketus rasite meniu *"Support&Downloads"*;
- Įkelkite atsisiųstus paketus į *Winbox"Files"* meniu ir perkraukite įrenginį;
- Atnaujinę RouterOS programinę įrangą į naujausią versiją, galite užtikrinti optimalų našumą, stabilumą ir saugos naujinimus;
- Meniu *"QuickSet, CPE"* nustatykite šiuos veiksmus: Pasirinkite šalį, kad pritaikytumėte šalies reguliavimo nustatymus;
- Kairiajame lauke nustatykite belaidžio tinklo slaptažodį;
- Apatiniame lauke nustatykite maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik maitinimo šaltinį ir gamintojo patvirtinti priedai, kurie gali būti rasta i originali šio gaminio pakuotė.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas skirtas montuoti lauke ant stulpo. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite pataisytos aparatūros ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių.
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Kad išvengtumėte aplinkos užteršimo, atskirkite įrenginį nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 35 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS 7.10 vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt profesionāli uzstādītām.
Šī īsā rokasgrāmata paredzēta modelim: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-93.png)

Atkarībā no izmantotās antenas ir jāiestata tās pastiprinājums un instalācijas iestatījums uz '*Outdoor*'. Tas ir paredzēts, lai nodrošinātu, ka EIRP atbilst vietējo iestāžu noteiktajam ierobežojumam. Tas tiek darīts izvēlnē *Quickset, CPE*.

**Pirmie soļi:**

- Atveriet apakšējo vāku un pievienojiet ierīci komplektā iekļautajam PoE inžektoram ar Ethernet kabeli pie "data+power" gala;
- Pievienojiet PoE inžektora datu galu datoram;
- Pievienojiet strāvas adapteri PoE inžektoram;
- Lejupielādēt WinBox konfigurācijas rīku [https://mt.lv/winbox](https://mt.lv/winbox);
- Sāciet konfigurēšanu izvēlētajā rīkā un izvēlieties cilni "*Neighbors*", lai atrastu ierīci;
- Noklikšķiniet uz MAC adreses. Lietotājvārds ir "admin", bez paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Lai manuāli atjauninātu ierīci, apmeklējiet produktu lapu vietnē [https://mikrotik.com/products](https://mikrotik.com/products), lai atrastu savu produktu. Nepieciešamie faili ir pieejami izvēlnē "Support&Downloads";
- Augšupielādējiet lejupielādētos failus izvēlnē *Winbox "* Files" un restartējiet ierīci;
- Jauninot savu RouterOS programmatūru uz jaunāko versiju, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Izvēlnē *"QuickSet, CPE"* iestatiet sekojošo: Izvēlieties savu valsti, lai piemērotu valsts regulējuma iestatījumus;
- Kreisajā laukā iestatiet bezvadu tīkla paroli;
- Apakšējā laukā iestatiet maršrutētāja paroli.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprināto barošanas adapteri un piederumus, kas iekļauti šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai ārā uz staba. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nepareizas aparatūras un konfigurācijas nelietošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sabojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un izmetiet to drošā veidā, piemēram, tam paredzētās vietās. Iepazīstieties ar procedūrām, kā pareizi transportēt aprīkojumu uz norādītajiem savākšanas punktiem jūsu reģionā.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 35 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS 7.10 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż l-operazzjoni fil-kanali tal-frekwenza legali, tal-ħruġ qawwa, ħtiġiet ta 'kejbils, u Reklamar ta' Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom ikunu installat professjonalment.
Din is-serje "mANTBox 5" Gwida ta 'malajr tkopri mudelli: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-93.png)

Skont l-antenna użata, trid issettja l-gwadann tagħha u ssettja l-issettjar tal-installazzjoni għal '*Outdoor*'. Dan biex jiġi żgurat li l-EIRP jilħaq il-limitu stabbilit mill-awtoritajiet lokali. Dan isir fil-*Quickset*, menu *CPE*.

**L-ewwel passi:**

- Iftaħ il-qoxra tal-qiegħ u qabbad l-apparat mal-injettur PoE mill-kit, billi tuża kejbil Ethernet mat-tarf "*data+power*";
- Qabbad it-tarf tad-dejta tal-injettur PoE mal-kompjuter;
- Qabbad l-adapter tal-enerġija mal-injettur PoE;
- Niżżel l-għodda tal-konfigurazzjoni WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Ibda l-konfigurazzjoni fi ħdan l-għodda magħżula u agħżel it-tab "*Neighbors"* biex issib l-apparat;
- Ikklikkja fuq l-indirizz MAC. L-isem tal-utent huwa "admin", u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja passwords tal-utent u wireless fuq l-istiker);
- Għal aġġornament manwali tal-apparat, żur il-paġna tal-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products) biex issib il-prodott tiegħek. Il-pakketti meħtieġa huma aċċessibbli taħt il-menu *"Support&Downloads"*;
- Ittella pakketti mniżżla fil- menu *Winbox"Files"* u reboot l-apparat;
- Billi taġġorna s-softwer RouterOS tiegħek għall-aħħar verżjoni, tista 'tiżgura l-aħjar prestazzjoni, stabbiltà u aġġornamenti tas-sigurtà;
- Fil- menu *"QuickSet, CPE"* waqqaf dan li ġej: Agħżel pajjiżek, biex tapplika s-settings tar-regolamentazzjoni tal-pajjiż;
- Issettja l-password tan-netwerk bla fili tiegħek fil-qasam tax-xellug;
- Issettja l-password tar-router tiegħek fil-qasam t'isfel.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il - provvista tal- enerġija u aċċessorji approvati mill-manifattur, u li jistgħu jiġu sibt i n l-imballaġġ oriġinali ta 'dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jintrama fuq barra fuq arblu. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar b’attenzjoni qabel tibda l-installazzjoni. Jekk tonqos milli tuża l- hardware u l-konfigurazzjoni korretta jew issegwi l-proċeduri t-tajba tista 'tirriżulta f'sitwazzjoni perikoluża għan-nies u tagħmel ħsara lis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Biex tevita l-kontaminazzjoni tal-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sikur, pereżempju, f'żoni magħżula. Kun familjari mal-proċeduri għat-trasport kif suppost tat-tagħmir lejn punti ta' ġbir magħżula fiż-żona tiegħek.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 35 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS 7.10 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften, inclusief werking binnen wettelijke frequentiekanalen, te volgen vermogen, bekabelingseisen en Dynamic Frequency Selection (DFS) -vereisten. Alle MikroTik-radioapparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-93.png)

Afhankelijk van de gebruikte antenne, moet u de versterking instellen en de installatie-instelling op '*Outdoor*' zetten. Dit om ervoor te zorgen dat EIRP voldoet aan de door de lokale autoriteiten gestelde grens. Dit doet u in het *Quickset*, *CPE*-menu.

**Eerste stappen:**

- Open de onderkant en sluit het apparaat aan op de PoE-injector uit de set, met behulp van een Ethernet-kabel naar het "*data+power"*-uiteinde;
- Sluit het data-uiteinde van de PoE-injector aan op de computer;
- Sluit de voedingsadapter aan op de PoE-injector;
- Download de WinBox-configuratietool [https://mt.lv/winbox](https://mt.lv/winbox);
- Start de configuratie binnen de gekozen tool en kies het tabblad "*Neighbors*" om het apparaat te vinden;
- Klik op het MAC-adres. De gebruikersnaam is "admin", en er is geen wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Voor een handmatige update van het apparaat gaat u naar de productpagina op [https://mikrotik.com/products](https://mikrotik.com/products) om uw product te vinden. De benodigde pakketten zijn toegankelijk onder het menu *"Support&Downloads"*;
- Upload gedownloade pakketten naar het menu *Winbox"Files"* en start het apparaat opnieuw op;
- Door uw RouterOS-software te upgraden naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- In het menu *"QuickSet, CPE"* stelt u het volgende in: Kies uw land om de landregelgevingsinstellingen toe te passen;
- Stel uw draadloze netwerkwachtwoord in het linkerveld in;
- Stel uw routerwachtwoord in het onderste veld in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures voor het voorkomen van ongevallen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires goedgekeurd door de fabrikant, en die kunnen zijn gevonden i n de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om buiten op een paal te worden gemonteerd. Lees de montage-instructies zorgvuldig voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Dit is een Klasse A-product. In een huishoudelijke omgeving kan dit product radiostoring veroorzaken. In dat geval moet de gebruiker mogelijk passende maatregelen nemen.
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stroomadapter uit het stopcontact te halen.
- Het stopcontact moet dichtbij de apparatuur worden geïnstalleerd en gemakkelijk toegankelijk zijn.
- Om vervuiling van het milieu te voorkomen, moet u het apparaat scheiden van het huishoudelijk afval en het op een veilige manier weggooien, bijvoorbeeld op de daarvoor bestemde plaatsen. Zorg ervoor dat u bekend bent met de procedures voor het correct transporteren van de apparatuur naar de aangewezen inzamelpunten bij u in de buurt.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 35 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS 7.10 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości wymagania dotyczące zasilania, okablowania i dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być profesjonalnie zainstalowany.
Niniejsza skrócona instrukcja „mANTBox 5” obejmuje modele: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-93.png)

W zależności od używanej anteny należy ustawić jej wzmocnienie i ustawić ustawienie instalacji na '*Outdoor*'. Ma to na celu zapewnienie, że EIRP spełnia limit ustalony przez władze lokalne. Odbywa się to w menu *Quickset*, *CPE*.

**Pierwsze kroki:**

- Otwórz dolną pokrywę i podłącz urządzenie do iniektora PoE z zestawu, używając kabla Ethernet do końca "*data+power"*;
- Podłącz końcówkę danych wtryskiwacza PoE do komputera;
- Podłącz zasilacz do wtryskiwacza PoE;
- Pobierz narzędzie konfiguracyjne WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Rozpocznij konfigurację w wybranym narzędziu i wybierz zakładkę "Sąsiedzi", aby znaleźć urządzenie;
- Kliknij adres MAC. Nazwa użytkownika to "admin" i nie ma hasła (lub, w przypadku niektórych modeli, sprawdź hasło użytkownika i hasło sieci bezprzewodowej na naklejce);
- Aby ręcznie zaktualizować urządzenie, odwiedź stronę produktów pod adresem [https://mikrotik.com/products](https://mikrotik.com/products) i znajdź swój produkt. Wymagane pakiety są dostępne w menu *"Support&Downloads"*;
- Prześlij pobrane pakiety do menu *Winbox"Files"* i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, możesz zapewnić optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu *"QuickSet, CPE"* skonfiguruj następujące opcje: Wybierz swój kraj, aby zastosować ustawienia przepisów krajowych;
- Ustaw hasło do sieci bezprzewodowej w lewym polu;
- Skonfiguruj hasło routera w dolnym polu.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj tylko zasilacza i akcesoria zatwierdzone przez producenta, i które mogą być znaleziony w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Produkt przeznaczony jest do montażu na zewnątrz na słupie. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie odpowiedniego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe. W takim przypadku użytkownik może zostać zobowiązany do podjęcia odpowiednich kroków.
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- Gniazdko elektryczne powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- Aby uniknąć skażenia środowiska, urządzenie należy oddzielić od odpadów domowych i utylizować w bezpieczny sposób, np. w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 35 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS 7.10 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais de frequência legal, saída requisitos de alimentação, cabeamento e Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalado profissionalmente.
Este Guia Rápido da série "mANTBox 5" abrange modelos: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-93.png)

Dependendo da antena usada, você deve definir seu ganho e definir a configuração de instalação para '*Outdoor*'. Isso é para garantir que o EIRP atenda ao limite estabelecido pelas autoridades locais. Isso é feito no menu *Quickset*, *CPE*.

**Primeiros passos:**

- Abra a tampa inferior e conecte o dispositivo ao injetor PoE do kit, utilizando um cabo Ethernet até a extremidade "*data+power"*;
- Conecte a extremidade de dados do injetor PoE ao computador;
- Conecte o adaptador de energia ao injetor PoE;
- Baixe a ferramenta de configuração do WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Inicie a configuração dentro da ferramenta escolhida e escolha a aba “*Neighbors*” para encontrar o dispositivo;
- Clique no endereço MAC. O nome de usuário é “admin” e não há senha (ou, para alguns modelos, verifique as senhas de usuário e wireless no adesivo);
- Para uma atualização manual do dispositivo, visite a página de produtos em [https://mikrotik.com/products](https://mikrotik.com/products) para encontrar o seu produto. Os pacotes necessários estão acessíveis no menu *"Support&Downloads"*;
- Carregue os pacotes baixados no menu *Winbox"Files"* e reinicie o dispositivo;
- Ao atualizar o software RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- No menu *"QuickSet, CPE"* configure o seguinte: Escolha o seu país, para aplicar as configurações de regulamentação do país;
- Configure a senha da sua rede wireless no campo esquerdo;
- Configure a senha do seu roteador no campo inferior.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação acessórios aprovados pelo fabricante e que podem ser encontrado na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser montado ao ar livre em um poste. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou do não cumprimento dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas.
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- A tomada deverá ser instalada próxima ao equipamento e deverá ser de fácil acesso.
- Para evitar a contaminação do meio ambiente, separe o aparelho do lixo doméstico e descarte-o de forma segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para transportar adequadamente o equipamento para pontos de coleta designados em sua área.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 35 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS 7.10 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale cerințe de alimentare, cabluri și cerințe de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie să fie instalat profesional.
Acest Ghid rapid seria "mANTBox 5" acoperă modele: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-91.png)

În funcție de antena utilizată, trebuie să setați câștigul acesteia și să setați setarea de instalare la „*Outdoor*”. Acest lucru este pentru a ne asigura că EIRP îndeplinește limita stabilită de autoritățile locale. Acest lucru se face în meniul *Quickset*, *CPE*.

**Primii pasi:**

- Deschideți capacul inferior și conectați dispozitivul la injectorul PoE din kit, folosind un cablu Ethernet la capătul "*data+power"*;
- Conectați capătul de date al injectorului PoE la computer;
- Conectați adaptorul de alimentare la injectorul PoE;
- Descărcați instrumentul de configurare WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Începeți configurația în cadrul instrumentului ales și alegeți fila "*Neighbors"* pentru a găsi dispozitivul;
- Faceți clic pe adresa MAC. Numele de utilizator este "admin", și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless pe autocolant);
- Pentru o actualizare manuală a dispozitivului, vizitați pagina de produse la [https://mikrotik.com/products](https://mikrotik.com/products) pentru a găsi produsul dvs. Pachetele necesare sunt accesibile în meniul *"Support&Downloads""*;
- Încărcați pachetele descărcate în meniul *Winbox"Files"* și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanță optimă, stabilitate și actualizări de securitate;
- În meniul *"QuickSet, CPE"* configurați următoarele: Alegeți țara, pentru a aplica setările de reglementare a țării;
- Configurați parola rețelei wireless în câmpul din stânga;
- Configurați parola routerului în câmpul de jos.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesorii aprobate de producător și care pot fi găsite Am n ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie montat în aer liber pe un stâlp. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-l într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător a echipamentului la punctele de colectare desemnate din zona dumneavoastră.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 35 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS 7.10 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny, vrátane prevádzky v rámci legálnych frekvenčných kanálov a výstupov požiadavky na energiu, kabeláž a dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť profesionálne nainštalovaný.
Táto stručná príručka „mANTBox 5“ zahŕňa modely: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-93.png)

V závislosti od použitej antény musíte nastaviť jej zisk a nastaviť inštalačné nastavenie na „*Outdoor*“. To má zabezpečiť, aby EIRP spĺňal limit stanovený miestnymi orgánmi. Toto sa vykonáva v ponuke *Quickset*, *CPE*.

**Prvé kroky:**

- Otvorte spodný kryt a pripojte zariadenie k PoE injektoru zo súpravy pomocou ethernetového kábla do konca "*data+power"*;
- Pripojte dátový koniec PoE injektora k počítaču;
- Pripojte napájací adaptér k PoE injektoru;
- Stiahnite si konfiguračný nástroj WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Spustite konfiguráciu vo vybranom nástroji a vyberte kartu "*Neighbors"*, aby ste našli zariadenie;
- Kliknite na MAC adresu. Používateľské meno je "admin" a neexistuje žiadne heslo (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslá na nálepke);
- Pre manuálnu aktualizáciu zariadenia navštívte stránku produktov na [https://mikrotik.com/products](https://mikrotik.com/products), kde nájdete svoj produkt. Požadované balíky sú dostupné v menu "*Support&Downloads"*;
- Nahrajte stiahnuté balíčky do ponuky *Winbox "Files"* a reštartujte zariadenie;
- Inováciou softvéru RouterOS na najnovšiu verziu môžete zaistiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- V ponuke "*QuickSet, CPE"* nastavte nasledovné: Vyberte svoju krajinu, ak chcete použiť nastavenia regulácie krajiny;
- V ľavom poli nastavte heslo bezdrôtovej siete;
- V spodnom poli nastavte heslo smerovača.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájanie a príslušenstvo schválené výrobcom, ktoré môže byť nájdených v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na montáž vonku na stĺp. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať správne, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- Aby ste predišli kontaminácii životného prostredia, oddeľte zariadenie od domáceho odpadu a zlikvidujte ho bezpečným spôsobom, napríklad na miestach na to určených. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 35 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS 7.10 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom, vključno z delovanjem v legalnih frekvenčnih kanalih, za doseganje rezultatov napajanje, zahteve za kabliranje in zahteve za dinamično izbiro frekvence (DFS). Vse radijske naprave MikroTik morajo biti strokovno nameščen.
Ta hitri vodnik serije "mANTBox 5" zajema modele: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-93.png)

Glede na uporabljeno anteno morate nastaviti njeno ojačenje in nastavitev namestitve na "*Outdoor*". S tem zagotovimo, da EIRP ustreza omejitvi, ki so jo določile lokalne oblasti. To se naredi v meniju *Quickset*, *CPE*.

**Prvi koraki:**

- Odprite spodnji pokrov in povežite napravo z injektorjem PoE iz kompleta z ethernetnim kablom na koncu "*data+power*";
- Priključite podatkovni konec injektorja PoE na računalnik;
- Priključite napajalnik na injektor PoE;
- Prenesite konfiguracijsko orodje WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Zaženite konfiguracijo znotraj izbranega orodja in izberite zavihek "*Neighbors*", da poiščete napravo;
- Kliknite naslov MAC. Uporabniško ime je "admin" in ni gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Za ročno posodobitev naprave obiščite stran z izdelki na [https://mikrotik.com/products](https://mikrotik.com/products) in poiščite svoj izdelek. Zahtevani paketi so dostopni v meniju "*Support&Downloads"*;
- Naložite prenesene pakete v meni *Winbox"Files"* in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno zmogljivost, stabilnost in varnostne posodobitve;
- V meniju *"QuickSet, CPE"* nastavite naslednje: izberite svojo državo, da uporabite nastavitve državnih predpisov;
- V levem polju nastavite geslo za brezžično omrežje;
- V spodnjem polju nastavite geslo usmerjevalnika.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatki, ki jih je odobril proizvajalec, in ki so lahko najdeno i n originalna embalaža tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen za namestitev na prostem na drog. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba ustrezne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe.
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- Da preprečite onesnaženje okolja, ločite napravo od gospodinjskih odpadkov in jo odvrzite na varen način, na primer na za to namenjenih mestih. Seznanite se s postopki za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 35 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS 7.10 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, output kraft, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste vara professionellt installerat.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-93.png)

Beroende på vilken antenn som används måste du ställa in dess förstärkning och ställa in installationsinställningen till "*Outdoor*". Detta för att säkerställa att EIRP uppfyller den gräns som de lokala myndigheterna har satt. Detta görs i *Quickset*, *CPE*-menyn.

**Första stegen:**

- Öppna bottenlocket och anslut enheten till PoE-injektorn från satsen, med en Ethernet-kabel till "*data+power*"-änden;
- Anslut dataänden på PoE-injektorn till datorn;
- Anslut strömadaptern till PoE-injektorn;
- Ladda ner WinBox konfigurationsverktyg [https://mt.lv/winbox](https://mt.lv/winbox);
- Starta konfigurationen inom det valda verktyget och välj fliken "*Neighbors*" för att hitta enheten;
- Klicka på MAC-adressen. Användarnamnet är "admin", och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- För en manuell uppdatering av enheten, besök produktsidan på [https://mikrotik.com/products](https://mikrotik.com/products) för att hitta din produkt. De nödvändiga paketen är tillgängliga under menyn *"Support&Downloads";*
- Ladda ner nedladdade paket till *Winbox"Files"* - menyn och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I *"QuickSet, CPE"* -menyn ställer du in följande: Välj ditt land, för att tillämpa inställningarna för landsbestämmelser;
- Ställ in lösenordet för ditt trådlösa nätverk i det vänstra fältet;
- Ställ in ditt routerlösenord i det nedre fältet.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast strömförsörjningen och tillbehör som godkänts av tillverkaren, och som kan vara hittades i den ursprungliga förpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att monteras utomhus på en stolpe. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på syste m.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- För att undvika kontaminering av miljön, separera enheten från hushållsavfallet och kassera den på ett säkert sätt, till exempel i avsedda områden. Bekanta dig med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsplatser i ditt område.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 35 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS 7.10或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规，包括在合法频道内操作，输出 电源，布线要求和动态频率选择（DFS）要求。 所有MikroTik无线电设备必须 专业安装。
此“ mANTBox 5”系列快速指南涵盖以下型号：RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-94.png)

根據使用的天線，您必須設置其增益並將安裝設置設置為“Outdoor”。這是為了確保 EIRP 滿足地方當局設定的限制。這是在 Quickset、CPE 菜單中完成的。**第一步：**

- 打开底盖，将设备连接到套件中的 PoE 注入器，使用以太网线连接到“ *data+power* ”端；
- 将PoE供电器的数据端连接至电脑；
- 将电源适配器连接至 PoE 供电器；
- 下载WinBox配置工具[https://mt.lv/winbox](https://mt.lv/winbox)
- 在所选工具中启动配置，然后选择“邻居”选项卡来查找设备；
- 单击 MAC 地址。用户名是“admin”，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）；
- 如需手动更新设备，请访问产品页面[https://mikrotik.com/products](https://mikrotik.com/products) 查找您的产品。所需的软件包可在 *"Support&Downloads"* 菜单下访问；
- 将下载的包上传到 *Winbox "Files"* 菜单并重启设备；
- 通过将 RouterOS 软件升级到最新版本，您可以确保最佳性能、稳定性和安全更新；
- *在"QuickSet, CPE"* 菜单中进行以下设置： 选择您所在的国家/地区，以应用国家/地区法规设置；
- 在左侧字段中设置您的无线网络密码；
- 在底部字段中设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用 电源 和制造商认可的配件, 可以 发现 在此产品的原包装中。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在户外安装在杆子上。 在开始安装之前，请仔细阅读安装说明。 不使用正确的硬件和配置或未遵循正确的程序可能会导致人员受伤和系统损坏 。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 这是A类产品。 在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施。
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 插座应安装在设备附近且易于插拔的位置。
- 为避免污染环境，请将设备与生活垃圾分开并以安全方式进行处置，例如在指定区域进行处置。熟悉将设备正确运输到您所在地区指定收集点的程序。

**射频辐射暴露**：此 MikroTik 设备符合针对不受控制的环境规定的欧盟辐射暴露限制。此 MikroTik 设备的安装和使用距离您的身体、专业用户或公众不得超过 35 厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS 7.10 или до последней версии, чтобы обеспечить соответствие требованиям местных органов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, вывод требования к питанию, кабелям и динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть профессионально установлены.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-92.png)

В зависимости от используемой антенны необходимо настроить ее коэффициент усиления и установить настройку установки на «*Outdoor*». Это делается для того, чтобы EIRP соответствовал пределу, установленному местными властями. Делается это в меню *Quickset*, *CPE*.

**Первые шаги:**

- Откройте нижнюю крышку и подключите устройство к PoE-инжектору из комплекта, используя Ethernet-кабель к концу "*data+power*";
- Подключите конец данных PoE-инжектора к компьютеру;
- Подключите адаптер питания к PoE-инжектору;
- Загрузите инструмент настройки WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Запустите настройку с помощью выбранного инструмента и выберите вкладку "Neighbors", чтобы найти устройство;
- Нажмите на MAC-адрес. Имя пользователя - *"admin"*, пароль отсутствует (или, для некоторых моделей, проверьте пароль пользователя и пароль беспроводной сети на наклейке);
- Для обновления устройства вручную посетите страницу продуктов по адресу [https://mikrotik.com/products](https://mikrotik.com/products), чтобы найти свой продукт. Необходимые пакеты доступны в меню *"Support&Downloads"*;
- Загрузите скачанные пакеты в меню *Winbox"Files"* и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню *"QuickSet, CPE"* настройте следующее: Выберите свою страну, чтобы применить настройки регулирования страны;
- Установите пароль беспроводной сети в левом поле;
- Установите пароль маршрутизатора в нижнем поле.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт предназначен для установки на открытом воздухе столба. Пожалуйста, внимательно прочтите инструкцию по монтажу перед началом установки. Несоблюдение правил использования аппаратного обеспечения и конфигурации или следования правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
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

**Воздействие радиочастотного излучения.** Это устройство MikroTik должно быть установлено и эксплуатироваться не ближе 35 сантиметров от вашего тела, профессионального пользователя или широкой публики.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Частотный диапазон: 5150-5350 МГц, 5850-6100 МГц. Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

![](./img/image2020-1-24_7-55-5.badge-96.png)

Во избежание загрязнения окружающей среды необходимо отделить устройство от бытовых отходов и утилизировать его безопасным способом, например в специально отведенных местах. Ознакомьтесь с процедурами надлежащей транспортировки оборудования к специальным местам утилизации в вашем регионе.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS 7.10 або останньої версії, щоб забезпечити відповідність місцевим нормам влади!

Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей короткий посібник серії mANTBox 5 охоплює моделі: RB921GS-5HPacD-15S (mANTBox 15s), RB921GS-5HPacD-19S (mANTBox 19s).

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-39.png)

Залежно від використовуваної антени, ви повинні встановити її посилення та встановити для параметра встановлення значення «Outdoor». Це необхідно для того, щоб EIRP відповідав ліміту, встановленим місцевою владою. Це робиться в меню Quickset, CPE.

**Перші кроки:**

- Відкрийте нижню кришку та підключіть пристрій до PoE-інжектора, що входить до комплекту, за допомогою кабелю Ethernet до кінця передачі даних+живлення *"data+power"*;
- Підключіть кінець даних PoE-інжектора до комп’ютера;
- Підключіть адаптер живлення до PoE-інжектора;
- Завантажте інструмент налаштування WinBox [https://mt.lv/winbox](https://mt.lv/winbox);
- Запустіть налаштування у вибраному інструменті та виберіть вкладку "Neighbors", щоб знайти пристрій;
- Натисніть на MAC-адресу. Ім’я користувача - *"admin"* і немає пароля (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою [https://mikrotik.com/products](https://mikrotik.com/products), щоб знайти свій продукт. Необхідні пакети доступні в меню *"Support&Downloads"*;
- Завантажте завантажені пакети в меню *Winbox"Files"* і перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви зможете забезпечити оптимальну продуктивність, стабільність і оновлення безпеки;
- У меню *"QuickSet, CPE"* налаштуйте наступне: Виберіть свою країну, щоб застосувати налаштування країни;
- Налаштуйте пароль бездротової мережі в лівому полі;
- У нижньому полі встановіть пароль маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей виріб призначений для встановлення надворі на стовп. Будь ласка, уважно прочитайте інструкції зі встановлення перед початком роботи. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки.
- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів і утилізуйте його безпечним способом, наприклад, у спеціально відведених місцях. Ознайомтеся з процедурами належного транспортування обладнання до призначених пунктів збору у вашому регіоні.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 35 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

Справжнім Mikrotikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.
![](./img/fcc_logo_ez.badge-83.jpg)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Antenna Installation WARNING**: It is the installer's responsibility to ensure that when using the authorized antennas in the USA (or where FCC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

LIST OF APPROVED 5 GHz ANTENNAS:

- 7 dBi Omni Directional (Model: HGO-antenna-OUT)
- 15 dBi Sector Antenna (Model: MTAS-5G-15D120)
- 19 dBi Sector Antenna (Model: MTAS-5G-19D120)
The same type of antenna and lower antenna gain than those listed above may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 35 centimeters from your body, occupational user, or the general public.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

Antenna Installation WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

LIST OF APPROVED 5 GHz ANTENNAS:

- 7 dBi Omni Directional (Model: HGO-antenna-OUT)
- 15 dBi Sector Antenna (Model: MTAS-5G-15D120)
- 19 dBi Sector Antenna (Model: MTAS-5G-19D120)
The same type of antenna and lower antenna gain than those listed above may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 35 centimeters from your body, occupational user, or the general public.

## UKCA marking

![](./img/ukca_black_fill.badge-92.gif)

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
      
      5150-5250 MHz/ 23 dBm
    
    5250-5350 MHz / 20 dBm
    5470-5725 MHz / 27 dBm
  

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](./img/picto-21.png)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Current, A

DC Jack (8-30 V DC) PoE In Ethernet Port (12 - 28 V DC)
24
0.8
IP54
-33°..+50°C

:::warning
Please, test your antenna with our device in the accreditation laboratory to be in compliance with EU rules.
:::
\#72822
