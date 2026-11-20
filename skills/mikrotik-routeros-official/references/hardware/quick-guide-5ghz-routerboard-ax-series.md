# Quick Guide - 5GHz RouterBOARD ax series

> This Quick Guide covers the model: L11UG-5HaxD.

![](./img/mt_logo_arrow_v2-02.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.14.2 or the latest version to ensure compliance with local authority regulations!
It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
:::

This Quick Guide covers the model: L11UG-5HaxD.

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*It is the responsibility of the installer to ensure the use of authorized antennas; only those antennas certified with the product should be used. The installer must configure the antenna output power level in accordance with national regulations and each antenna type. Professional installation of connector equipment is required to ensure compliance with health and safety.*

![](./img/image2020-1-31_12-4-32.badge.png)

**First steps:**

- This product comes without enclosure and is designed to be installed into the users' end products or enclosures. Compatible MikroTik enclosure for this product can be found at [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- The device comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions:Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the router on the anti-static mat;
- When mounting the unit make sure there are no objects that can damage or touch the PCB plate;
- The device can be mounted in your desired location using the factory-provided holes in a PCB plate, located on each side of the device;
- Before connecting the device to the power source, please attach the antennas to the connectors;
- Connect the device to the power source;
- Connect your PC to the Ethernet port;
- Configuration should be made using a web browser WebFig or the WinBox configuration tool [https://mt.lv/WinBox](https://mt.lv/WinBox); **multiple configuration methods are available to ensure accessibility;**
- Download and open "*WinBox"*, and choose the "*Neighbors"* tab to find the device;
- Click on the MAC address. The username is "*admin"* and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device. By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "*QuickSet"* menu set up the *"PTP Bridge AP"* mode and choose your country, to apply country regulation settings;
- Set the antenna gain, depending on the antenna used;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- The product comes without enclosure and is meant to be installed into the enclosure by trained and qualified personnel. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair or modify the device.
- Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- Keep this device away from water, fire, humidity, or hot environments.
- Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage. After unpacking please place the router on the anti-static mat. When mounting the unit make sure there are no objects that can damage or touch the PCB plate.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.14.2 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства на MikroTik трябва да бъдат професионално инсталирани.
:::

Този документ обхваща модела: L11UG-5HaxD.

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на този документ.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Отговорност на монтажника е да осигури използването на оторизирани антени; трябва да се използват само тези антени, сертифицирани с продукта. Инсталаторът трябва да конфигурира нивото на изходна мощност на антената в съответствие с националните разпоредби и всеки тип антена. Необходима е професионална инсталация на съединителното оборудване, за да се гарантира съответствие със здравето и безопасността.*

![](./img/image2020-2-4_17-15-57.badge.png)

**Първи стъпки:**

- Този продукт се предлага без корпус и е предназначен за инсталиране в крайни продукти или кутии на потребителите. Съвместим корпус MikroTik за този продукт можете да намерите на [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Устройството се доставя в ESD защитна опаковка. Когато работите с електрическо оборудване, спазвайте следните предпазни мерки:Използвайте заземяваща лента за китката, когато разопаковате и работите с електрически компоненти, за да избегнете повреда от електрически разряд (ESD);
- След като разопаковате, поставете рутера върху антистатичната подложка;
- Когато монтирате устройството, уверете се, че няма предмети, които могат да повредят или докоснат плочата на печатната платка;
- Устройството може да се монтира на желаното от вас място с помощта на фабрично осигурените отвори в печатна платка, разположени от всяка страна на устройството;
- Преди да свържете устройството към източника на захранване, моля, прикрепете антените към конекторите;
- Свържете устройството към източника на захранване;
- Свържете вашия компютър към Ethernet порта;
- Конфигурацията трябва да се извършва с помощта на уеб браузър WebFig или инструмента за конфигурация WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Изтеглете и отворете *"WinBox"* и изберете раздела *"Neighbors"*, за да намерите устройството;
- Кликнете върху MAC адреса. Потребителското име е *"admin"* и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Кликнете на бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството. Чрез надграждане на софтуера на RouterOS до най-новата версия можете да осигурите оптимална производителност, стабилност и актуализации за сигурност;
- В менюто *"QuickSet"* настройте режима *"PTP Bridge AP"* и изберете вашата държава, за да приложите настройките за регулиране на страната;
- Задайте усилването на антената в зависимост от използваната антена;
- Задайте паролата на вашия рутер в долното поле.

**Информация за безопасност:**

- Преди да работите с каквото и да е оборудване на MikroTik, имайте предвид опасностите, свързани с електрическите вериги, и се запознайте със стандартните практики за предотвратяване на инциденти. Инсталаторът трябва да е запознат с мрежовите структури, термини и концепции.
- Продуктът се доставя без корпус и е предназначен за инсталиране в корпуса от обучен и квалифициран персонал. Инсталаторът е отговорен да се увери, че инсталацията на оборудването е в съответствие с местните и националните електрически кодекси. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Моля, прочетете внимателно инструкциите за монтаж, преди да започнете монтажа. Неизползването на правилния хардуер и конфигурация или неизпълнението на правилните процедури може да доведе до опасна ситуация за хората и повреда на системата.
- Дръжте това устройство далеч от вода, огън, влага или горещи среди.
- Използвайте заземяваща лента за китката, когато разопаковате и работите с електрически компоненти, за да избегнете повреда от електрически разряд (ESD). След като разопаковате, поставете рутера върху антистатичната подложка. Когато монтажният модул се уверява, че няма предмети, които могат да повредят или докоснат плочата на печатната платка.
- Не можем да гарантираме, че няма да възникнат инциденти или щети поради неправилна употреба на устройството. Моля, използвайте този продукт внимателно и работете на свой собствен риск!
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например на определени места. Запознайте се с процедурите за правилно транспортиране на оборудването до определените пунктове за събиране във вашия район.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, в този случай от потребителя може да се наложи да предприеме адекватни мерки.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.14.2 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být profesionálně nainstalována.
:::

Tento dokument se týká modelu: L11UG-5HaxD.

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu naleznete na poslední straně tohoto dokumentu.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Je na odpovědnosti instalačního technika, aby zajistil použití autorizovaných antén; měly by být používány pouze antény certifikované s výrobkem. Instalační technik musí nakonfigurovat výstupní výkon antény v souladu s národními předpisy a každým typem antény. Pro zajištění dodržování BOZP je nutná odborná montáž konektorového zařízení.*

![](./img/image2020-2-4_17-16-42.badge.png)

**První kroky:**

- Tento produkt je dodáván bez krytu a je navržen pro instalaci do koncových produktů nebo krytů uživatelů. Kompatibilní kryt MikroTik pro tento produkt naleznete na [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Zařízení je dodáváno v ESD ochranném obalu. Při manipulaci s elektrickým zařízením dodržujte následující bezpečnostní opatření:Při vybalování a práci s elektrickými součástmi používejte uzemňovací pásek na zápěstí, aby nedošlo k poškození elektrickým výbojem (ESD);
- Po vybalení položte router na antistatickou podložku;
- Při montáži jednotky se ujistěte, že na desce nejsou žádné předměty, které by mohly poškodit nebo se dotýkat desky plošných spojů;
- Zařízení lze namontovat na požadované místo pomocí továrně dodávaných otvorů v desce plošných spojů, které se nacházejí na každé straně zařízení;
- Před připojením zařízení ke zdroji napájení připojte antény ke konektorům;
- Připojte zařízení ke zdroji napájení;
- Připojte svůj počítač k portu Ethernet;
- Konfigurace by měla být provedena pomocí webového prohlížeče WebFig nebo nástroje pro konfiguraci WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Stáhněte a otevřete *"WinBox"* a vyberte kartu *"Neighbors"*, abyste našli zařízení;
- Klikněte na MAC adresu. Uživatelské jméno je *"admin"* a není zde žádné heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Klepněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do nabídky "Files" na WebFig nebo WinBox a restartujte zařízení. Upgradováním softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce *"QuickSet"* nastavte režim *"PTP Bridge AP"* a vyberte svou zemi pro použití nastavení regulace země;
- Nastavte zisk antény v závislosti na použité anténě;
- Ve spodním poli nastavte heslo routeru.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si nebezpečí spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalační program by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Výrobek je dodáván bez krytu a je určen k instalaci do krytu vyškoleným a kvalifikovaným personálem. Instalační technik je odpovědný za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat nebo upravovat.
- Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete správný hardware a konfiguraci nebo nedodržíte správné postupy, může dojít k nebezpečné situaci pro lidi a poškození systému.
- Udržujte toto zařízení mimo dosah vody, ohně, vlhkosti nebo horkého prostředí.
- Při vybalování a práci s elektrickými součástmi používejte uzemňovací pásek na zápěstí, aby nedošlo k poškození elektrickým výbojem (ESD). Po vybalení položte router na antistatickou podložku. Když montážní jednotka zajišťuje, že na desce nejsou žádné předměty, které by mohly poškodit nebo se dotknout desky plošných spojů.
- Nemůžeme zaručit, že nedojde k žádným nehodám nebo škodám v důsledku nesprávného použití zařízení. Používejte prosím tento výrobek opatrně a provozujte jej na vlastní nebezpečí!
- Abyste zabránili znečištění životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na určených místech. Seznamte se s postupy správné přepravy zařízení na určená sběrná místa ve vaší oblasti.
- Toto je výrobek třídy A. V domácím prostředí může tento výrobek způsobovat rušení rádiových vln. V takovém případě může být uživatel povinen přijmout odpovídající opatření.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.14.2 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal være professionelt installeret.
:::

Dette dokument dækker modellen: L11UG-5HaxD.

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt kan findes på sidste side i dette dokument.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Det er installatørens ansvar at sikre brugen af ​​autoriserede antenner; kun de antenner, der er certificeret med produktet, bør bruges. Installatøren skal konfigurere antennens udgangseffektniveau i overensstemmelse med nationale bestemmelser og hver antennetype. Professionel installation af konnektorudstyr er påkrævet for at sikre overholdelse af sundhed og sikkerhed.*

![](./img/image2020-2-4_17-13-55.badge.png)

**Første skridt:**

- Dette produkt leveres uden indkapsling og er designet til at blive installeret i brugernes slutprodukter eller kabinetter. Kompatibel MikroTik-kabinet til dette produkt kan findes på [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Enheden leveres i ESD-beskyttende emballage. Ved håndtering af elektrisk udstyr skal du overholde følgende sikkerhedsforanstaltninger:Brug en håndledsjordstrop, når du pakker ud og arbejder med elektriske komponenter for at undgå skader på elektrisk udladning (ESD);
- Efter udpakning skal du placere routeren på den antistatiske måtte;
- Når du monterer enheden, skal du sørge for, at der ikke er genstande, der kan beskadige eller røre ved printpladen;
- Enheden kan monteres på det ønskede sted ved hjælp af de fabriksleverede huller i en PCB-plade, placeret på hver side af enheden;
- Før du tilslutter enheden til strømkilden, skal du tilslutte antennerne til stikkene;
- Tilslut enheden til strømkilden;
- Tilslut din pc til Ethernet-porten;
- Konfigurationen skal foretages ved hjælp af webbrowseren WebFig eller konfigurationsværktøjet WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Download og åbn *"WinBox"*, og vælg fanen *"Neighbors"* for at finde enheden;
- Klik på MAC-adressen. Brugernavnet er *"admin"*, og der er ingen adgangskode (eller, for nogle modeller, tjek brugeradgangskoder og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload de downloadede pakker til WebFig eller WinBox "Files" menuen og genstart enheden. Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil *"PTP Bridge AP"*-tilstanden i *"QuickSet"*-menuen og vælg dit land for at anvende landereguleringsindstillinger;
- Indstil antenneforstærkningen afhængigt af den anvendte antenne;
- Indstil din router-adgangskode i det nederste felt.

**Sikkerhedsoplysninger:**

- Før du arbejder på noget MikroTik-udstyr, skal du være opmærksom på de farer, der er forbundet med elektriske kredsløb, og være bekendt med standardpraksis til at forebygge ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, termer og koncepter.
- Produktet leveres uden indkapsling og er beregnet til at blive installeret i kabinettet af uddannet og kvalificeret personale. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske regler. Forsøg ikke at adskille, reparere eller modificere enheden.
- Læs venligst monteringsvejledningen omhyggeligt, før installationen påbegyndes. Manglende brug af den korrekte hardware og konfiguration eller overholdelse af de korrekte procedurer kan resultere i en farlig situation for mennesker og beskadigelse af systemet.
- Hold denne enhed væk fra vand, ild, fugt eller varme omgivelser.
- Brug en håndledsjordingsstrop, når du pakker ud og arbejder med elektriske komponenter for at undgå skader på elektrisk udladning (ESD). Efter udpakning skal du placere routeren på den antistatiske måtte. Når en monteringsenhed sørger for, at der ikke er genstande, der kan beskadige eller røre ved printpladen.
- Vi kan ikke garantere, at der ikke vil ske uheld eller skader på grund af forkert brug af enheden. Brug venligst dette produkt med omhu og brug på egen risiko!
- For at undgå forurening af miljøet skal apparatet adskilles fra husholdningsaffald og bortskaffes på en sikker måde, f.eks. I bestemte områder. Bliv fortrolig med procedurer til korrekt transport af udstyr til udpegede indsamlingssteder i dit område.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.14.2 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen professionell installiert werden.
:::

Dieses Dokument behandelt das Modell: L11UG-5HaxD.

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten zu diesem Produkt finden Sie auf der letzten Seite dieses Dokuments.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Es liegt in der Verantwortung des Installateurs sicherzustellen, dass zugelassene Antennen verwendet werden; Es sollten nur die mit dem Produkt zertifizierten Antennen verwendet werden. Der Installateur muss den Antennenausgangsleistungspegel gemäß den nationalen Vorschriften und jedem Antennentyp konfigurieren. Die fachgerechte Installation von Anschlussgeräten ist erforderlich, um die Einhaltung von Gesundheit und Sicherheit zu gewährleisten.*

![](./img/image2020-2-4_17-20-45.badge.png)

**Erste Schritte:**

- Dieses Produkt wird ohne Gehäuse geliefert und ist für den Einbau in die Endprodukte oder Gehäuse des Benutzers konzipiert. Kompatible MikroTik-Gehäuse für dieses Produkt finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Das Gerät wird in einer ESD-Schutzverpackung geliefert. Beachten Sie beim Umgang mit elektrischen Geräten bitte die folgenden Sicherheitsvorkehrungen:Verwenden Sie beim Auspacken und Arbeiten mit elektrischen Komponenten ein Erdungsarmband, um Schäden durch elektrische Entladung (ESD) zu vermeiden.
- Bitte legen Sie den Router nach dem Auspacken auf die Antistatikmatte;
- Stellen Sie bei der Montage des Geräts sicher, dass keine Gegenstände vorhanden sind, die die Platine beschädigen oder berühren können.
- Das Gerät kann mithilfe der werkseitig vorgesehenen Löcher in einer Leiterplatte, die sich auf jeder Seite des Geräts befindet, an der gewünschten Stelle montiert werden.
- Bevor Sie das Gerät an die Stromquelle anschließen, befestigen Sie bitte die Antennen an den Anschlüssen;
- Schließen Sie das Gerät an die Stromquelle an;
- Verbinden Sie Ihren PC mit dem Ethernet-Port;
- Die Konfiguration sollte mit dem Webbrowser WebFig oder dem WinBox-Konfigurationstool [https://mt.lv/WinBox](https://mt.lv/WinBox) durchgeführt werden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Laden Sie *"WinBox"* herunter, öffnen Sie es und wählen Sie die Registerkarte *"Neighbors"*, um das Gerät zu finden.
- Klicken Sie auf die MAC-Adresse. Der Benutzername lautet *"admin"* und es gibt kein Passwort (bei einigen Modellen überprüfen Sie die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu. Durch ein Upgrade Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Richten Sie im Menü *"QuickSet"* den *"PTP Bridge AP"*-Modus ein und wählen Sie Ihr Land aus, um die Länderregulierungseinstellungen anzuwenden;
- Stellen Sie den Antennengewinn je nach verwendeter Antenne ein;
- Richten Sie im unteren Feld Ihr Router-Passwort ein.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, machen Sie sich über die Gefahren bewusst, die mit elektrischen Schaltkreisen verbunden sind, und machen Sie sich mit den Standardverfahren zur Unfallverhütung vertraut. Der Installateur sollte mit Netzwerkstrukturen, -begriffen und -konzepten vertraut sein.
- Das Produkt wird ohne Gehäuse geliefert und soll von geschultem und qualifiziertem Personal in das Gehäuse eingebaut werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Elektrovorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn nicht die richtige Hardware und Konfiguration verwendet oder die richtigen Verfahren nicht befolgt werden, kann dies zu einer Gefahrensituation für Personen und zu Schäden am System führen.
- Halten Sie dieses Gerät von Wasser, Feuer, Feuchtigkeit oder heißen Umgebungen fern.
- Verwenden Sie beim Auspacken und Arbeiten mit elektrischen Komponenten ein Erdungsarmband, um Schäden durch elektrische Entladung (ESD) zu vermeiden. Bitte legen Sie den Router nach dem Auspacken auf die Antistatikmatte. Bei einer Montageeinheit wird sichergestellt, dass keine Gegenstände vorhanden sind, die die Leiterplatte beschädigen oder berühren können.
- Wir können nicht garantieren, dass es durch unsachgemäßen Gebrauch des Gerätes nicht zu Unfällen oder Schäden kommt. Bitte verwenden Sie dieses Produkt mit Vorsicht und betreiben Sie es auf eigene Gefahr!
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Geräte zu bestimmten Sammelstellen in Ihrer Nähe vertraut.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.14.2 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ασύρματες συσκευές MikroTik πρέπει να είναι επαγγελματικά εγκατεστημένες.
:::

Αυτό το έγγραφο καλύπτει το μοντέλο: L11UG-5HaxD.

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του εγγράφου.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Είναι ευθύνη του εγκαταστάτη να διασφαλίσει τη χρήση εξουσιοδοτημένων κεραιών. θα πρέπει να χρησιμοποιούνται μόνο οι κεραίες που είναι πιστοποιημένες με το προϊόν. Ο τεχνικός εγκατάστασης πρέπει να διαμορφώσει το επίπεδο ισχύος εξόδου της κεραίας σύμφωνα με τους εθνικούς κανονισμούς και κάθε τύπο κεραίας. Απαιτείται επαγγελματική εγκατάσταση του εξοπλισμού σύνδεσης για τη διασφάλιση της συμμόρφωσης με την υγεία και την ασφάλεια.*

![](./img/image2020-2-4_17-25-41.badge.png)

**Πρώτα βήματα:**

- Αυτό το προϊόν διατίθεται χωρίς περίβλημα και έχει σχεδιαστεί για εγκατάσταση στα τελικά προϊόντα ή στα περιβλήματα των χρηστών. Το συμβατό περίβλημα MikroTik για αυτό το προϊόν βρίσκεται στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Η συσκευή διατίθεται σε προστατευτική συσκευασία ESD. Όταν χειρίζεστε ηλεκτρικό εξοπλισμό, τηρείτε τις ακόλουθες προφυλάξεις ασφαλείας:Χρησιμοποιήστε έναν ιμάντα γείωσης καρπού όταν αποσυσκευάζετε και εργάζεστε με ηλεκτρικά εξαρτήματα για να αποφύγετε ζημιά από ηλεκτρική εκφόρτιση (ESD);
- Μετά την αποσυσκευασία, τοποθετήστε το δρομολογητή στο αντιστατικό στρώμα;
- Κατά την τοποθέτηση της μονάδας βεβαιωθείτε ότι δεν υπάρχουν αντικείμενα που μπορούν να προκαλέσουν ζημιά ή να αγγίξουν την πλάκα PCB;
- Η συσκευή μπορεί να τοποθετηθεί στην επιθυμητή θέση χρησιμοποιώντας τις οπές που παρέχονται από το εργοστάσιο σε μια πλάκα PCB, που βρίσκεται σε κάθε πλευρά της συσκευής;
- Πριν συνδέσετε τη συσκευή στην πηγή ρεύματος, συνδέστε τις κεραίες στις υποδοχές.
- Συνδέστε τη συσκευή στην πηγή ρεύματος.
- Συνδέστε τον υπολογιστή σας στη θύρα Ethernet.
- Η ρύθμιση πρέπει να γίνει χρησιμοποιώντας τον περιηγητή WebFig ή το εργαλείο ρύθμισης WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Κάντε λήψη και ανοίξτε το *"WinBox"* και επιλέξτε την καρτέλα *"Neighbors"* για να βρείτε τη συσκευή.
- Κάντε κλικ στη διεύθυνση MAC. Το όνομα χρήστη είναι *"admin"* και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματου δικτύου στο αυτοκόλλητο).
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού "Files" του WebFig ή WinBox και επανεκκινήστε τη συσκευή. Αναβαθμίζοντας το λογισμικό RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας.
- Στο μενού *"QuickSet"* ρυθμίστε τη λειτουργία *"PTP Bridge AP"* και επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις ρύθμισης χώρας.
- Ρυθμίστε το κέρδος κεραίας, ανάλογα με την κεραία που χρησιμοποιείται.
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο.

**Οδηγίες ασφαλείας:**

- Πριν εργαστείτε σε οποιονδήποτε εξοπλισμό της MikroTik, να γνωρίζετε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και να εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης θα πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Το προϊόν διατίθεται χωρίς περίβλημα και προορίζεται για εγκατάσταση στο περίβλημα από εκπαιδευμένο και εξειδικευμένο προσωπικό. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση ότι η εγκατάσταση του εξοπλισμού είναι συμβατή με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η αποτυχία χρήσης του σωστού υλικού και διαμόρφωσης ή η μη τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και ζημιά στο σύστημα.
- Κρατήστε αυτή τη συσκευή μακριά από νερό, φωτιά, υγρασία ή ζεστό περιβάλλον.
- Χρησιμοποιήστε έναν ιμάντα γείωσης καρπού όταν αποσυσκευάζετε και εργάζεστε με ηλεκτρικά εξαρτήματα για να αποφύγετε ζημιά από ηλεκτρική εκφόρτιση (ESD). Μετά την αποσυσκευασία, τοποθετήστε το ρούτερ στο αντιστατικό στρώμα. Όταν μια μονάδα στερέωσης βεβαιωθεί ότι δεν υπάρχουν αντικείμενα που μπορούν να προκαλέσουν ζημιά ή να αγγίξουν την πλάκα PCB.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.
- Αυτό είναι ένα προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει ραδιοφωνικές παρεμβολές, οπότε ενδέχεται να απαιτείται από τον χρήστη να λάβει τα κατάλληλα μέτρα.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.14.2 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalados profesionalmente.
:::

Este documento cubre el modelo: L11UG-5HaxD.

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se encuentran en la última página de este documento.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Es responsabilidad del instalador asegurar el uso de antenas autorizadas; solo se deben utilizar aquellas antenas certificadas con el producto. El instalador debe configurar el nivel de potencia de salida de la antena de acuerdo con la normativa nacional y cada tipo de antena. Se requiere la instalación profesional de equipos de conectores para garantizar el cumplimiento de las normas de salud y seguridad.*

![](./img/image2020-2-4_17-27-25.badge.png)

**Primeros pasos:**

- Este producto viene sin gabinete y está diseñado para instalarse en los productos finales o gabinetes de los usuarios. La carcasa MikroTik compatible para este producto se puede encontrar en [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- El dispositivo se entrega en un embalaje protector ESD. Al manipular equipos eléctricos, observe las siguientes precauciones de seguridad:Utilice una muñequera con conexión a tierra al desembalar y trabajar con componentes eléctricos para evitar daños por descarga eléctrica (ESD);
- Después de desembalar, coloque el enrutador sobre la alfombra antiestática;
- Al montar la unidad asegúrese de que no haya objetos que puedan dañar o tocar la placa PCB;
- El dispositivo se puede montar en la ubicación deseada utilizando los orificios provistos de fábrica en una placa PCB, ubicada a cada lado del dispositivo;
- Antes de conectar el dispositivo a la fuente de alimentación, conecte las antenas a los conectores;
- Conecte el dispositivo a la fuente de alimentación;
- Conecte su PC al puerto Ethernet;
- La configuración debe realizarse con el navegador web WebFig o la herramienta de configuración WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Descargue y abra *"WinBox"* y elija la pestaña *"Neighbors"* para encontrar el dispositivo;
- Haga clic en la dirección MAC. El nombre de usuario es *"admin"* y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú "Files" de WebFig o WinBox y reinicie el dispositivo. Al actualizar su software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- En el menú *"QuickSet"* configure el modo *"PTP Bridge AP"* y elija su país, para aplicar la configuración de la regulación del país;
- Establezca la ganancia de la antena, según la antena utilizada;
- Configure la contraseña de su enrutador en el campo inferior.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los peligros relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras, los términos y los conceptos de la red.
- El producto viene sin caja y está diseñado para ser instalado en la caja por personal capacitado y calificado. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desarmar, reparar o modificar el dispositivo.
- Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o si no se siguen los procedimientos correctos, se podría producir una situación peligrosa para las personas y daños al sistema.
- Mantenga este dispositivo alejado del agua, el fuego, la humedad o los ambientes calientes.
- Use una muñequera de conexión a tierra cuando desembale y trabaje con componentes eléctricos para evitar daños por descargas eléctricas (ESD). Después de desempacar, coloque el enrutador sobre la alfombra antiestática. Cuando una unidad de montaje asegúrese de que no haya objetos que puedan dañar o tocar la placa de circuito impreso.
- No podemos garantizar que no se produzcan accidentes o daños debido al uso inadecuado del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- Para evitar la contaminación del medio ambiente, separe el dispositivo de la basura doméstica y deséchelo de manera segura, por ejemplo, en las áreas designadas. Familiarícese con los procedimientos para transportar correctamente el equipo a los puntos de recolección designados en su área.
- Este es un producto de Clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso es posible que el usuario deba tomar las medidas adecuadas.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

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
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.14.2 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTiku raadioseadmed peavad olema professionaalselt paigaldatud.
:::

See dokument hõlmab mudelit: L11UG-5HaxD.

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle dokumendi viimaselt leheküljelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Paigaldaja kohustus on tagada volitatud antennide kasutamine; kasutada tuleks ainult neid antenne, mis on tootega sertifitseeritud. Paigaldaja peab konfigureerima antenni väljundvõimsuse vastavalt riiklikele eeskirjadele ja igale antennitüübile. Pistikuseadmete professionaalne paigaldamine on vajalik tervise ja ohutuse tagamiseks.*

![](./img/image2020-2-4_17-31-19.badge.png)

**Esimesed sammud:**

- See toode on ilma korpuseta ja on mõeldud paigaldamiseks kasutaja lõpptoodetesse või korpustesse. Selle toote jaoks ühilduva MikroTiku korpuse leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Seade on ESD kaitsepakendis. Elektriseadmete käsitsemisel järgige järgmisi ettevaatusabinõusid:Elektrilahenduste (ESD) kahjustuste vältimiseks kasutage lahtipakkimisel ja elektriliste komponentidega töötamisel randme maandusrihma;
- Pärast lahtipakkimist asetage ruuter antistaatilisele matile;
- Seadme paigaldamisel veenduge, et seal pole esemeid, mis võivad PCB plaati kahjustada või puudutada;
- Seadme saab paigaldada soovitud kohta, kasutades tehases ette nähtud auke PCB plaadil, mis asuvad seadme mõlemal küljel;
- Enne seadme ühendamist toiteallikaga ühendage antennid pistikutesse;
- Ühendage seade toiteallikaga;
- Ühendage arvuti Etherneti porti;
- Konfigureerimine tuleb teha veebibrauseri WebFig või WinBox konfigureerimisriista [https://mt.lv/WinBox](https://mt.lv/WinBox) abil; **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Laadige alla ja avage *"WinBox"* ning valige seadme leidmiseks vahekaart "Neighbors"*;*
- Klõpsake MAC-aadressil. Kasutajanimi on *"admin"* ja parool puudub (või mõne mudeli puhul kontrollige kleebiselt kasutaja ja traadita ühenduse paroole);
- Klõpsake nupul "Check for updates" ja ajakohastage RouterOS viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige allalaaditud paketid üles WebFig või WinBox "Files" menüüsse ja taaskäivitage seade. Uuendades oma RouterOS-i tarkvara uusimale versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadistage menüüs *"QuickSet"* *režiim* *"PTP Bridge AP"* ja valige riigi reguleerimise sätete rakendamiseks oma riik;
- Määrake antenni võimendus sõltuvalt kasutatavast antennist;
- Seadistage alumisel väljal ruuteri parool.

**Ohutusteave:**

- Enne MikroTiku seadmega töötamist olge teadlik elektriskeemiga kaasnevatest ohtudest ja tutvuge õnnetuste ärahoidmise tavapäraste tavadega. Paigaldaja peaks olema tuttav võrgustruktuuride, terminite ja mõistetega.
- Toode tarnitakse ilma korpuseta ja selle paigaldavad korpusesse koolitatud ja kvalifitseeritud töötajad. Paigaldaja vastutab selle eest, et seadmete paigaldamine vastaks kohalikele ja riiklikele elektrieeskirjadele. Ärge püüdke seadet lahti võtta, parandada ega muuta.
- Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhiseid. Õige riistvara ja konfiguratsiooni mittekasutamine või õigete protseduuride mittejärgimine võib põhjustada inimestele ohtliku olukorra ja kahjustada süsteemi.
- Hoidke seda seadet veest, tulest, niiskusest või kuumast keskkonnast eemal.
- Elektrilahenduse (ESD) kahjustuste vältimiseks kasutage lahtipakkimisel ja elektriliste komponentidega töötamisel randmemaandusrihma. Pärast lahtipakkimist asetage ruuter antistaatilisele matile. Kui paigaldusüksus tagab, et pole esemeid, mis võivad PCB plaati kahjustada või puudutada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja omal vastutusel!
- Keskkonna saastumise vältimiseks eraldage seade olmejäätmetest ja utiliseerige see ohutult, näiteks selleks ettenähtud kohtades. Tutvuge seadmete nõuetekohase transportimise protseduuridega teie piirkonnas asuvatesse kogumispunktidesse.
- See on A -klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, mille korral võib kasutaja nõuda piisavate meetmete võtmist.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.14.2 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikkien MikroTik-radiolaitteiden on oltava ammattimaisesti asennettuja.
:::

Tämä asiakirja kattaa mallin: L11UG-5HaxD.

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi) Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän asiakirjan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Asentajan vastuulla on varmistaa valtuutettujen antennien käyttö; tulee käyttää vain tuotteen kanssa sertifioituja antenneja. Asentajan on määritettävä antennin lähtötehotaso kansallisten määräysten ja kunkin antennityypin mukaisesti. Liitinlaitteiden ammattimainen asennus vaaditaan terveyden ja turvallisuuden varmistamiseksi.*

![](./img/image2020-2-4_17-33-3.badge.png)

**Ensiaskeleet:**

- Tämä tuote toimitetaan ilman koteloa ja se on suunniteltu asennettavaksi käyttäjien lopputuotteisiin tai koteloihin. Tälle tuotteelle yhteensopiva MikroTik-kotelo löytyy osoitteesta [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Laite toimitetaan ESD-suojapakkauksessa. Noudata sähkölaitteita käsitellessäsi seuraavia turvaohjeita:Käytä maadoitusrannehihnaa, kun purat pakkauksesta ja työskentelet sähkökomponenttien kanssa välttääksesi sähköpurkausvauriot (ESD);
- Aseta reititin pakkauksesta purkamisen jälkeen antistaattiselle matolle.
- Kun asennat yksikköä, varmista, että siinä ei ole esineitä, jotka voivat vahingoittaa tai koskettaa piirilevyä;
- Laite voidaan asentaa haluamaasi paikkaan käyttämällä tehtaalla toimitettuja reikiä piirilevyssä, jotka sijaitsevat laitteen molemmilla puolilla;
- Ennen kuin liität laitteen virtalähteeseen, kiinnitä antennit liittimiin;
- Liitä laite virtalähteeseen;
- Liitä tietokoneesi Ethernet-porttiin;
- Kokoonpano tulee tehdä käyttäen verkkoselainta WebFig tai konfiguraatiotyökalua WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Lataa ja avaa *"WinBox"* ja etsi laite valitsemalla *"Neighbors"*-välilehti;
- Napsauta MAC-osoitetta. Käyttäjätunnus on *"admin"*, eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Napsauta "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFig- tai WinBox-"Files"-valikkoon ja käynnistä laite uudelleen. Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja tietoturvapäivitykset;
- Aseta *"QuickSet"*-valikossa *"PTP Bridge AP"*-tila ja valitse maasi, jotta maakohtaiset asetukset otetaan käyttöön;
- Aseta antennin vahvistus käytetyn antennin mukaan;
- Aseta reitittimen salasana alakenttään.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden parissa, ole tietoinen sähköpiirien vaaroista ja tunne tavallisia käytäntöjä onnettomuuksien ehkäisemiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Tuote toimitetaan ilman koteloa, ja koulutetun ja pätevän henkilöstön on tarkoitus asentaa koteloon. Asentaja on vastuussa siitä, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Jos laitteistoa ja kokoonpanoa ei käytetä tai oikeita menettelyjä ei noudateta, seurauksena voi olla ihmisille vaarallinen tilanne ja järjestelmän vaurioituminen.
- Pidä tämä laite poissa vedestä, tulesta, kosteudesta tai kuumista ympäristöistä.
- Käytä maadoitusrannehihnaa, kun purat pakkauksesta ja työskentelet sähkökomponenttien kanssa välttääksesi sähköpurkausvauriot (ESD). Aseta reititin pakkauksesta purkamisen jälkeen antistaattiselle matolle. Kun asennusyksikkö varmistaa, että siinä ei ole esineitä, jotka voivat vahingoittaa tai koskettaa piirilevyä.
- Emme voi taata, että laitteen väärästä käytöstä johtuen ei tapahdu onnettomuuksia tai vahinkoja. Käytä tätä tuotetta varoen ja toimi omalla vastuullasi!
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla esimerkiksi määrätyillä alueilla. Tutustu toimenpiteisiin, joilla laite kuljetetaan asianmukaisesti alueellesi määritettyihin keräyspisteisiin.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää voidaan joutua ryhtymään tarvittaviin toimenpiteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.14.2 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés professionnellement.
:::

Ce document couvre le modèle: L11UG-5HaxD.

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes pour ce produit se trouvent à la dernière page de ce document.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Il est de la responsabilité de l'installateur de s'assurer de l'utilisation d'antennes autorisées; seules les antennes certifiées avec le produit doivent être utilisées. L'installateur doit configurer le niveau de puissance de sortie de l'antenne conformément aux réglementations nationales et à chaque type d'antenne. L'installation professionnelle de l'équipement de connexion est nécessaire pour assurer le respect de la santé et de la sécurité.*

![](./img/image2020-2-4_17-35-53.badge.png)

**Premiers pas:**

- Ce produit est livré sans boîtier et est conçu pour être installé dans les produits finaux ou les boîtiers des utilisateurs. Le boîtier MikroTik compatible pour ce produit peut être trouvé sur [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- L'appareil est livré dans un emballage de protection ESD. Lors de la manipulation d'équipements électriques, veuillez respecter les précautions de sécurité suivantes:Utilisez un bracelet de mise à la terre lors du déballage et du travail avec des composants électriques pour éviter les dommages causés par les décharges électriques (ESD);
- Après le déballage, veuillez placer le routeur sur le tapis antistatique;
- Lors du montage de l'unité, assurez-vous qu'aucun objet ne puisse endommager ou toucher la plaque PCB;
- L'appareil peut être monté à l'emplacement souhaité à l'aide des trous prévus en usine dans une plaque PCB, située de chaque côté de l'appareil;
- Avant de connecter l'appareil à la source d'alimentation, veuillez fixer les antennes aux connecteurs;
- Connectez l'appareil à la source d'alimentation;
- Connectez votre PC au port Ethernet;
- La configuration doit être effectuée à l'aide du navigateur WebFig ou de l'outil de configuration WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Téléchargez et ouvrez "WinBox" et *choisissez* l' onglet *"Neighbors"* pour trouver l'appareil;
- Cliquez sur l'adresse MAC. Le nom d'utilisateur est *"admin"* et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les paquets téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil. En mettant à niveau votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances, une stabilité et des mises à jour de sécurité optimales;
- Dans le menu *"QuickSet"*, configurez le mode *"PTP Bridge AP"* et choisissez votre pays pour appliquer les paramètres de réglementation du pays;
- Réglez le gain de l'antenne en fonction de l'antenne utilisée;
- Configurez le mot de passe de votre routeur dans le champ inférieur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des risques liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. L'installateur doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Le produit est livré sans boîtier et est destiné à être installé dans le boîtier par du personnel formé et qualifié. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration appropriés ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Gardez cet appareil à l'écart de l'eau, du feu, de l'humidité ou des environnements chauds.
- Utilisez un bracelet de mise à la terre lors du déballage et de l'utilisation de composants électriques pour éviter les dommages causés par les décharges électriques (ESD). Après le déballage, placez le routeur sur le tapis antistatique. Lorsqu'une unité de montage s'assure qu'aucun objet ne peut endommager ou toucher la plaque PCB.
- Nous ne pouvons pas garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec précaution et à vos risques et périls!
- Pour éviter la contamination de l'environnement, séparez l'appareil des déchets ménagers et éliminez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures pour transporter correctement l'équipement vers les points de collecte désignés dans votre région.
- Il s'agit d'un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union Européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.14.2 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radijski uređaji moraju biti profesionalno instalirani.
:::

Ovaj dokument pokriva model: L11UG-5HaxD.

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod nalaze se na zadnjoj stranici ovog dokumenta.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Odgovornost je instalatera osigurati korištenje ovlaštenih antena; smiju se koristiti samo one antene certificirane s proizvodom. Instalater mora konfigurirati razinu izlazne snage antene u skladu s nacionalnim propisima i svakim tipom antene. Potrebna je profesionalna instalacija priključne opreme kako bi se osigurala usklađenost sa zdravljem i sigurnošću.*

![](./img/image2020-2-4_17-37-28.badge.png)

**Prvi koraci:**

- Ovaj proizvod dolazi bez kućišta i dizajniran je za ugradnju u krajnje proizvode ili kućišta korisnika. Kompatibilno MikroTik kućište za ovaj proizvod možete pronaći na [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Uređaj dolazi u ESD zaštitnom pakiranju. Prilikom rukovanja električnom opremom pridržavajte se sljedećih sigurnosnih mjera opreza:Koristite vrpcu za uzemljenje prilikom raspakiranja i rada s električnim komponentama kako biste izbjegli oštećenje uslijed električnog pražnjenja (ESD);
- Nakon raspakiranja ruter stavite na antistatičku podlogu;
- Prilikom postavljanja jedinice pazite da nema predmeta koji bi mogli oštetiti ili dodirnuti PCB ploču;
- Uređaj se može montirati na željeno mjesto pomoću tvornički isporučenih rupa na PCB ploči, koje se nalaze sa svake strane uređaja;
- Prije spajanja uređaja na izvor napajanja, priključite antene na konektore;
- Spojite uređaj na izvor napajanja;
- Spojite svoje računalo na Ethernet priključak;
- Konfiguracija se mora obaviti pomoću web preglednika WebFig ili alata za konfiguraciju WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Preuzmite i otvorite *"WinBox"* i odaberite karticu *"Neighbors"* kako biste pronašli uređaj;
- Kliknite na MAC adresu. Korisničko ime je *"admin"* i nema zaporke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Kliknite na gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj. Nadogradnjom vašeg RouterOS softvera na najnoviju verziju, možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U izborniku *"QuickSet"* postavite način rada *"PTP Bridge AP"* i odaberite svoju državu kako biste primijenili postavke propisa zemlje;
- Postavite pojačanje antene, ovisno o korištenoj anteni;
- U donjem polju postavite lozinku za usmjerivač.

**Sigurnosne informacije:**

- Prije nego počnete raditi na bilo kojoj MikroTik opremi, budite svjesni opasnosti povezanih s električnim sklopovima i upoznajte se sa standardnim postupcima za sprječavanje nezgoda. Instalater bi trebao biti upoznat s mrežnim strukturama, terminima i konceptima.
- Proizvod dolazi bez kućišta i namijenjen je za ugradnju u kućište od strane obučenog i kvalificiranog osoblja. Instalater je odgovoran za osiguranje da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastaviti, popraviti ili modificirati uređaj.
- Prije početka instalacije pažljivo pročitajte upute za montažu. Neupotreba ispravnog hardvera i konfiguracije ili poštivanje ispravnih postupaka može rezultirati opasnom situacijom za ljude i oštećenjem sustava.
- Držite ovaj uređaj dalje od vode, vatre, vlage ili vrućih okruženja.
- Koristite vrpcu za uzemljenje prilikom raspakiranja i rada s električnim komponentama kako biste izbjegli oštećenje uslijed električnog pražnjenja (ESD). Nakon raspakiranja ruter stavite na antistatičku podlogu. Kada montažna jedinica osigurava da nema predmeta koji bi mogli oštetiti ili dodirnuti PCB ploču.
- Ne možemo jamčiti da neće doći do nezgoda ili štete zbog nepravilne uporabe uređaja. Pažljivo koristite ovaj proizvod i radite na vlastitu odgovornost!
- Da biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na za to predviđena mjesta. Upoznajte se s postupcima pravilnog transporta opreme do određenih sabirnih mjesta u vašem području.
- Ovo je proizvod klase A. U kućnom okruženju ovaj proizvod može uzrokovati radio smetnje, u tom slučaju od korisnika se može zahtijevati da poduzme odgovarajuće mjere.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.14.2-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket szakszerűen kell telepíteni.
:::

Ez a dokumentum a következő modellre vonatkozik: L11UG-5HaxD.

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki adatai a dokumentum utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*A telepítő felelőssége az engedélyezett antennák használatának biztosítása; csak a termékhez tanúsított antennákat szabad használni. A telepítőnek az antenna kimeneti teljesítményszintjét a nemzeti előírásoknak és az egyes antennatípusoknak megfelelően kell konfigurálnia. Az egészségügyi és biztonsági előírások betartása érdekében a csatlakozóberendezések szakszerű telepítése szükséges.*

![](./img/image2020-2-5_9-0-20.badge.png)

**Első lépések:**

- Ez a termék burkolat nélkül érkezik, és a felhasználók végtermékeibe vagy burkolataiba történő beépítésre készült. A termékhez kompatibilis MikroTik burkolat a [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures oldalon található.
- A készülék ESD védőcsomagolásban érkezik. Az elektromos berendezések kezelésekor tartsa be a következő biztonsági óvintézkedéseket:Kicsomagoláskor és az elektromos alkatrészekkel végzett munka során használjon földelő csuklópántot, hogy elkerülje az elektromos kisülés (ESD) okozta károsodást;
- Kicsomagolás után helyezze a routert az antisztatikus szőnyegre;
- Az egység felszerelésekor ügyeljen arra, hogy ne legyenek olyan tárgyak, amelyek megsérthetik vagy megérinthetik a PCB lemezt;
- Az eszköz a kívánt helyre szerelhető a gyárilag biztosított NYÁK-lemez furataival, amelyek a készülék mindkét oldalán találhatók;
- Mielőtt csatlakoztatná a készüléket az áramforráshoz, csatlakoztassa az antennákat a csatlakozókhoz;
- Csatlakoztassa a készüléket az áramforráshoz;
- Csatlakoztassa számítógépét az Ethernet porthoz;
- A konfigurációt a WebFig webböngésző vagy a WinBox konfigurációs eszköz használatával kell elvégezni [https://mt.lv/WinBox](https://mt.lv/WinBox); **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Töltse le és nyissa meg *a "WinBox"-t*, majd válassza ki a *"Neighbors"* lapot az eszköz megkereséséhez;
- Kattintson a MAC-címre. A felhasználónév *"admin"*, és nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson az "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt. A RouterOS szoftverének a legújabb verzióra való frissítésével optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- A *"QuickSet"* menüben állítsa be a *"PTP Bridge AP"* módot, és válassza ki az országot az országszabályozási beállítások alkalmazásához;
- Állítsa be az antenna erősítését a használt antennától függően;
- Állítsa be az útválasztó jelszavát az alsó mezőben.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozna, legyen tisztában az elektromos áramkörökkel járó veszélyekkel, és ismerje meg a balesetek megelőzésére vonatkozó szabványos gyakorlatokat. A telepítőnek ismernie kell a hálózati struktúrákat, kifejezéseket és fogalmakat.
- A terméket burkolat nélkül szállítjuk, és képzett és képesített személyzetnek kell beszerelnie a szekrénybe. A telepítő felelős azért, hogy megbizonyosodjon arról, hogy a berendezés telepítése megfelel a helyi és országos elektromos előírásoknak. Ne kísérelje meg szétszerelni, javítani vagy módosítani a készüléket.
- Kérjük, a telepítés megkezdése előtt figyelmesen olvassa el a szerelési útmutatót. A megfelelő hardver és konfiguráció használatának elmulasztása, illetve a megfelelő eljárások betartásának elmulasztása emberekre veszélyes helyzetet és a rendszer károsodását okozhatja.
- Tartsa távol a készüléket víztől, tűztől, nedvességtől vagy forró környezettől.
- Kicsomagoláskor és az elektromos alkatrészekkel végzett munka során használjon földelő csuklópántot, hogy elkerülje az elektromos kisülés (ESD) okozta károsodást. Kicsomagolás után helyezze a routert az antisztatikus szőnyegre. Amikor a szerelőegység gondoskodik arról, hogy ne legyenek olyan tárgyak, amelyek megsérthetik vagy megérinthetik a nyomtatott áramköri lapot.
- Nem tudjuk garantálni, hogy a készülék nem rendeltetésszerű használatából eredő baleset vagy kár nem következik be. Kérjük, használja ezt a terméket körültekintően és saját felelősségére használja!
- A környezet szennyeződésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon dobja el, például a kijelölt területekre. Ismerje meg a berendezés megfelelő szállítási eljárásait a környéken található gyűjtőhelyekre.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználónak meg kell tennie a megfelelő intézkedéseket.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia - Panduan Cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.14.2 atau versi stabil terbaru, untuk memastikan kepatuhan terhadap peraturan otoritas lokal!
:::

Merupakan tanggung jawab pengguna akhir untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya output, persyaratan pemasangan kabel, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat radio MikroTik harus dipasang secara profesional. Dokumen ini berlaku untuk model berikut: L11UG-5HaxD.

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama jenis produk pada label (ID) casing.*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um](https://mt.lv/um) untuk panduan pengguna terbaru yang lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis, Deklarasi Kesesuaian UE Lengkap, brosur, dan info lebih lanjut tentang produk di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Data teknis terpenting dari produk dapat ditemukan di halaman terakhir dokumen.*
*Panduan konfigurasi untuk software dalam bahasa Anda dengan informasi tambahan dapat ditemukan di [https://mt.lv/help](https://mt.lv/help)*
*Perangkat MikroTik untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi silahkan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Pemasang bertanggung jawab untuk memastikan penggunaan antena yang disetujui; hanya antena bersertifikat untuk produk ini yang boleh digunakan. Pemasang harus mengonfigurasi tingkat daya keluaran antena sesuai dengan peraturan nasional dan setiap jenis antena. Untuk mematuhi peraturan kesehatan dan keselamatan, peralatan sambungan harus dipasang secara profesional.*

![](./img/image2020-1-31_12-4-32.badge.png)

**Langkah pertama:**

- Produk ini hadir tanpa penutup dan dirancang untuk dipasang ke produk akhir atau penutup pengguna. Enklosur MikroTik yang kompatibel untuk produk ini dapat ditemukan di [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Perangkat ini hadir dalam kemasan pelindung ESD. Saat menangani peralatan listrik harap perhatikan tindakan pencegahan keselamatan berikut:Gunakan tali pengikat pergelangan tangan saat membuka kemasan dan menangani komponen listrik untuk menghindari kerusakan pelepasan listrik (ESD);
- Setelah membongkar, harap letakkan router di atas alas antistatis;
- Saat memasang unit pastikan tidak ada benda yang dapat merusak atau menyentuh pelat PCB;
- Perangkat dapat dipasang di lokasi yang Anda inginkan menggunakan lubang yang disediakan pabrik pada pelat PCB, yang terletak di setiap sisi perangkat;
- Sebelum menyambungkan perangkat ke sumber listrik, harap pasang antena ke konektor;
- Hubungkan perangkat ke injektor PoE yang disertakan dengan kabel Ethernet ke ujung *"data+power"*;
- Hubungkan ujung data injektor PoE ke komputer;
- Hubungkan adaptor daya ke injektor PoE;
- Konfigurasi harus dilakukan menggunakan peramban web WebFig atau alat konfigurasi WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Unduh dan buka *"WinBox"*, dan pilih tab *"Neighbors"* untuk menemukan perangkat;
- Klik pada alamat MAC. Nama pengguna adalah *"admin"* dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket-paket yang diunduh ke menu "Files" WebFig atau WinBox dan reboot perangkat. Dengan memutakhirkan perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan pembaruan kinerja, stabilitas, dan keamanan yang optimal;
- Di menu *"QuickSet"* atur mode *"PTP Bridge AP"* dan pilih negara Anda, untuk menerapkan pengaturan peraturan negara;
- Atur penguatan antena, tergantung pada antena yang digunakan;
- Siapkan kata sandi router Anda di kolom bawah.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan kenali praktik standar untuk mencegah kecelakaan. Pemasang harus terbiasa dengan struktur, istilah, dan konsep jaringan.
- Produk datang tanpa penutup dan dimaksudkan untuk dipasang ke dalam penutup oleh personel yang terlatih dan berkualifikasi. Pemasang bertanggung jawab untuk memastikan, bahwa Pemasangan peralatan tersebut sesuai dengan peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Silakan baca petunjuk pemasangan dengan hati-hati sebelum memulai pemasangan. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem.
- Jauhkan perangkat ini dari air, api, kelembapan, atau lingkungan yang panas.
- Gunakan tali pengikat pergelangan tangan saat membongkar dan bekerja dengan komponen listrik untuk menghindari kerusakan pelepasan muatan listrik (ESD). Setelah membongkar, harap letakkan router di alas anti-statis. Saat memasang unit pastikan tidak ada benda yang dapat merusak atau menyentuh pelat PCB.
- Kami tidak dapat menjamin bahwa tidak ada kecelakaan atau kerusakan yang akan terjadi karena penggunaan perangkat yang tidak tepat. Silakan gunakan produk ini dengan hati-hati dan operasikan dengan risiko Anda sendiri!
- Untuk menghindari kontaminasi lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan cara yang aman, misalnya di area yang ditentukan. Pelajari prosedur yang tepat untuk mengangkut peralatan Anda ke tempat pengumpulan di area Anda.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio yang mengharuskan pengguna mengambil tindakan yang memadai.

**Paparan Frekuensi Radio:** Perangkat MikroTik ini mematuhi batas paparan Uni Eropa untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini harus dipasang dan dioperasikan dengan jarak maksimal 20 centimeter dari tubuh, pengguna di tempat kerja atau publik.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.14.2 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati professionalmente.
:::

Questo documento riguarda il modello: L11UG-5HaxD.

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questo documento.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*È responsabilità dell'installatore garantire l'uso delle antenne autorizzate; devono essere utilizzate solo le antenne certificate con il prodotto. L'installatore deve configurare il livello di potenza di uscita dell'antenna in conformità con le normative nazionali e ogni tipo di antenna. L'installazione professionale dell'attrezzatura del connettore è necessaria per garantire il rispetto della salute e della sicurezza.*

![](./img/image2020-2-5_9-11-13.badge.png)

**Primi passi:**

- Questo prodotto viene fornito senza custodia ed è progettato per essere installato nei prodotti finali o nelle custodie degli utenti. La custodia MikroTik compatibile per questo prodotto è disponibile su [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Il dispositivo viene fornito in un imballaggio protettivo ESD. Quando si maneggiano apparecchiature elettriche, osservare le seguenti precauzioni di sicurezza:Utilizzare un braccialetto con messa a terra quando si disimballa e si lavora con componenti elettrici per evitare danni da scariche elettriche (ESD);
- Dopo aver disimballato, posizionare il router sul tappetino antistatico;
- Durante il montaggio dell'unità assicurarsi che non siano presenti oggetti che possano danneggiare o toccare la piastra PCB;
- Il dispositivo può essere montato nella posizione desiderata utilizzando i fori forniti in fabbrica su una piastra PCB, situata su ciascun lato del dispositivo;
- Prima di collegare il dispositivo alla fonte di alimentazione, collegare le antenne ai connettori;
- Collegare il dispositivo alla fonte di alimentazione;
- Collega il tuo PC alla porta Ethernet;
- La configurazione deve essere effettuata utilizzando il browser WebFig o lo strumento di configurazione WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Scarica e apri *"WinBox"* e scegli la scheda *"Neighbors"* per trovare il dispositivo;
- Fare clic sull'indirizzo MAC. Il nome utente è *"admin"* e non è presente alcuna password (oppure, per alcuni modelli, controllare le password utente e wireless sull'adesivo);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo. Aggiornando il software RouterOS all'ultima versione, puoi garantire prestazioni, stabilità e aggiornamenti di sicurezza ottimali;
- Nel menu *"QuickSet"* impostare la modalità *"PTP Bridge AP"* e scegliere il proprio paese, per applicare le impostazioni della normativa nazionale;
- Impostare il guadagno dell'antenna, a seconda dell'antenna utilizzata;
- Imposta la password del tuo router nel campo in basso.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, essere consapevoli dei pericoli connessi con i circuiti elettrici e acquisire familiarità con le pratiche standard per la prevenzione degli incidenti. L'installatore deve avere familiarità con le strutture, i termini e i concetti della rete.
- Il prodotto viene fornito senza custodia ed è pensato per essere installato all'interno della custodia da personale addestrato e qualificato. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il mancato rispetto delle procedure corrette potrebbe causare situazioni pericolose per le persone e danni al sistema.
- Tenere questo dispositivo lontano da acqua, fuoco, umidità o ambienti caldi.
- Utilizzare un cinturino da polso per la messa a terra quando si disimballa e si lavora con componenti elettrici per evitare danni da scariche elettriche (ESD). Dopo aver disimballato, posizionare il router sul tappetino antistatico. Quando un'unità di montaggio si assicura che non vi siano oggetti che possano danneggiare o toccare la piastra PCB.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e operare a proprio rischio!
- Per evitare la contaminazione dell'ambiente, separare il dispositivo dai rifiuti domestici e smaltirlo in modo sicuro, ad esempio, in aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura ai punti di raccolta designati nella propria zona.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso l'utente potrebbe essere tenuto ad adottare misure adeguate.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.14.2 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera faglega sett upp.
:::

Þetta skjal nær yfir gerð: L11UG-5HaxD.

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessa skjals.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Asentajan vastuulla on varmistaa valtuutettujen antennien käyttö; tulee käyttää vain tuotteen kanssa sertifioituja antenneja. Asentajan on määritettävä antennin lähtötehotaso kansallisten määräysten ja kunkin antennityypin mukaisesti. Liitinlaitteiden ammattimainen asennus vaaditaan terveyden ja turvallisuuden varmistamiseksi.*

![](./img/image2020-2-5_9-12-32.badge.png)

**Fyrstu skrefin:**

- Þessi vara kemur án girðingar og er hönnuð til að vera sett upp í lokavörur eða girðingar notenda. Samhæft MikroTik girðing fyrir þessa vöru er að finna á [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Tækið kemur í ESD hlífðarumbúðum. Við meðhöndlun rafbúnaðar vinsamlegast fylgdu eftirfarandi öryggisráðstöfunum:Notaðu úlnliðsjarðband þegar þú tekur upp og vinnur með rafmagnsíhluti til að forðast skemmdir á rafhleðslu (ESD);
- Eftir að hafa pakkað niður vinsamlegast settu beininn á andstæðingur-truflanir mottuna;
- Þegar einingin er sett upp skaltu ganga úr skugga um að það séu engir hlutir sem geta skemmt eða snert PCB plötuna;
- Hægt er að festa tækið á viðkomandi stað með því að nota verksmiðjugötin á PCB plötu, staðsett á hvorri hlið tækisins;
- Áður en tækið er tengt við aflgjafann skaltu tengja loftnetin við tengin;
- Tengdu tækið við aflgjafa;
- Tengdu tölvuna þína við Ethernet tengið;
- Stillingin þarf að vera framkvæmd með WebFig eða WinBox stillingartólun [https://mt.lv/WinBox](https://mt.lv/WinBox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Sæktu og opnaðu "WinBox" og *veldu* "Neighbors" flipann *til* að finna tækið;
- Smelltu á MAC vistfangið. Notandanafnið er *"admin"* og það er ekkert lykilorð (eða, fyrir sumar gerðir, athugaðu notanda og þráðlausa lykilorð á límmiðanum);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum í WebFig eða WinBox "Files" valmynd og endurræsa tækið. Með því að uppfæra RouterOS hugbúnaðinn þinn í nýjustu útgáfuna geturðu tryggt hámarksafköst, stöðugleika og öryggisuppfærslur;
- Í *"QuickSet"* valmyndinni skaltu setja upp *"PTP Bridge AP"* ham og velja land þitt, til að beita landsreglustillingum;
- Stilltu loftnetsstyrkinn, eftir því hvaða loftnet er notað;
- Settu upp lykilorðið þitt fyrir leiðina í neðsta reitnum.

**Öryggisupplýsingar:**

- Áður en þú vinnur á MicroTik búnaði skaltu vera meðvitaður um hætturnar sem fylgja rafrásum og þekkja staðlaðar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að þekkja netkerfi, hugtök og hugtök.
- Varan kemur án girðingar og er ætlað að vera sett upp í girðinguna af þjálfuðu og hæfu starfsfólki. Uppsetningaraðilinn er ábyrgur fyrir því að ganga úr skugga um að uppsetning búnaðarins sé í samræmi við staðbundnar og landsbundnar rafmagnsreglur. Ekki reyna að taka í sundur, gera við eða breyta tækinu.
- Vinsamlegast lestu uppsetningarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Misbrestur á að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti valdið hættulegum aðstæðum fyrir fólk og skemmdir á kerfinu.
- Haltu þessu tæki í burtu frá vatni, eldi, raka eða heitu umhverfi.
- Notaðu úlnliðsjarðband þegar þú tekur upp og vinnur með rafmagnsíhluti til að forðast skemmdir á rafhleðslu (ESD). Eftir að hafa verið pakkað upp skaltu setja beininn á andstæðingur-truflanir mottunnar. Þegar uppsetningareining er viss um að engir hlutir geti skemmt eða snert PCB plötuna.
- Við getum ekki ábyrgst að engin slys eða skemmdir eigi sér stað vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og notaðu á eigin ábyrgð!
- Til að koma í veg fyrir mengun umhverfisins skaltu aðskilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur til að flytja búnaðinn rétt til tilnefndra söfnunarstaða á þínu svæði.
- Þetta er vara í flokki A. Í heimalandi umhverfi gæti þessi vara valdið truflunum á útvarpi, en þá gæti þurft að gera notandann viðeigandi ráðstafanir.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.14.2 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter, inkludert drift innen lovlige frekvenskanaler, utgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheter må være profesjonelt installert.
:::

Dette dokumentet dekker modellen: L11UG-5HaxD.

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i dette dokumentet.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Det er installatørens ansvar å sørge for bruk av autoriserte antenner; kun de antennene som er sertifisert med produktet skal brukes. Installatøren må konfigurere antennens utgangseffektnivå i samsvar med nasjonale forskrifter og hver antennetype. Profesjonell installasjon av koblingsutstyr er nødvendig for å sikre samsvar med helse og sikkerhet.*

![](./img/image2020-2-5_9-13-45.badge.png)

**Første steg:**

- Dette produktet kommer uten kapsling og er designet for å installeres i brukernes sluttprodukter eller kabinetter. Kompatibel MikroTik-kabinett for dette produktet finner du på [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Enheten kommer i ESD-beskyttende emballasje. Ved håndtering av elektrisk utstyr, vær oppmerksom på følgende sikkerhetsregler:Bruk en jordingsstropp når du pakker ut og arbeider med elektriske komponenter for å unngå skade på elektrisk utladning (ESD);
- Etter utpakking, plasser ruteren på den antistatiske matten;
- Når du monterer enheten, sørg for at det ikke er gjenstander som kan skade eller berøre PCB-platen;
- Enheten kan monteres på ønsket sted ved å bruke de fabrikkleverte hullene i en PCB-plate, plassert på hver side av enheten;
- Før du kobler enheten til strømkilden, må du feste antennene til kontaktene;
- Koble enheten til strømkilden;
- Koble PC-en til Ethernet-porten;
- Konfigurasjonen må gjøres ved hjelp av nettleseren WebFig eller konfigurasjonsverktøyet WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Last ned og åpne *"WinBox"*, og velg fanen *"Neighbors"* for å finne enheten;
- Klikk på MAC-adressen. Brukernavnet er *"admin"* og det er ikke noe passord (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- Klikk på knappen "Check for updates" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig- eller WinBox-"Files" -menyen og start enheten på nytt. Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I *"QuickSet"*-menyen setter du opp *"PTP Bridge AP"*-modus og velger ditt land for å bruke landreguleringsinnstillinger;
- Still inn antenneforsterkningen, avhengig av antennen som brukes;
- Sett opp ruterpassordet ditt i det nederste feltet.

**Sikkerhetsinformasjon:**

- Før du arbeider på noe MikroTik-utstyr, må du være klar over farene forbundet med elektriske kretser, og være kjent med standard praksis for å forhindre ulykker. Installatøren bør være kjent med nettverksstrukturer, termer og konsepter.
- Produktet leveres uten kapsling og er ment å installeres i kabinettet av opplært og kvalifisert personell. Installatøren er ansvarlig for å sørge for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske forskrifter. Ikke forsøk å demontere, reparere eller modifisere enheten.
- Vennligst les monteringsanvisningen nøye før du begynner installasjonen. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på systemet.
- Hold denne enheten unna vann, brann, fuktighet eller varme omgivelser.
- Bruk en jordingsstropp når du pakker ut og arbeider med elektriske komponenter for å unngå skade på elektrisk utladning (ESD). Etter utpakking, plasser ruteren på den antistatiske matten. Når en monteringsenhet sørger for at det ikke er gjenstander som kan skade eller berøre PCB-platen.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk på egen risiko!
- For å unngå forurensning av miljøet, må du skille enheten fra husholdningsavfall og kaste den på en sikker måte, for eksempel i bestemte områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.
- Dette er et klasse A -produkt. I et hjemmemiljø kan dette produktet forårsake radioforstyrrelser. I så fall kan det være nødvendig at brukeren tar nødvendige tiltak.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.14.2“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi, įskaitant veikimą legaliais dažnių kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo prietaisai turi būti profesionaliai sumontuoti.
:::

Šis dokumentas apima modelius: L11UG-5HaxD.

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas rasite paskutiniame šio dokumento puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Montuotojas yra atsakingas už leistinų antenų naudojimą; turėtų būti naudojamos tik su gaminiu sertifikuotos antenos. Montuotojas turi sukonfigūruoti antenos išėjimo galios lygį pagal nacionalinius reglamentus ir kiekvieno antenos tipą. Norint užtikrinti atitiktį sveikatai ir saugai, reikalingas profesionalus jungčių įrangos montavimas.*

![](./img/image2020-2-5_9-15-30.badge.png)

**Pirmieji žingsniai:**

- Šis gaminys tiekiamas be gaubto ir yra skirtas montuoti į galutinius naudotojo gaminius arba korpusus. Šiam gaminiui suderinamą MikroTik korpusą rasite adresu [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Prietaisas yra ESD apsauginėje pakuotėje. Dirbdami su elektros įranga, laikykitės šių saugos priemonių:Išpakuodami ir dirbdami su elektros komponentais naudokite riešo įžeminimo dirželį, kad išvengtumėte elektros iškrovos (ESD) pažeidimų;
- Išpakavę maršruto parinktuvą padėkite ant antistatinio kilimėlio;
- Montuodami įrenginį įsitikinkite, kad nėra daiktų, galinčių pažeisti arba liesti PCB plokštę;
- Įrenginį galima montuoti norimoje vietoje naudojant gamykloje numatytas skyles PCB plokštėje, esančias kiekvienoje įrenginio pusėje;
- Prieš prijungdami įrenginį prie maitinimo šaltinio, prijunkite antenas prie jungčių;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Prijunkite kompiuterį prie Ethernet prievado;
- Konfigūracija turi būti atlikta naudojant naršyklę WebFig arba konfigūravimo įrankį WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atsisiųskite ir atidarykite *"WinBox"* ir pasirinkite skirtuką *"Neighbors"*, kad surastumėte įrenginį;
- Spustelėkite MAC adresą. Vartotojo vardas yra *"admin"* ir nėra slaptažodžio (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite prietaisą iš naujo. Atnaujinę RouterOS programinę įrangą į naujausią versiją, galite užtikrinti optimalų našumą, stabilumą ir saugos naujinimus;
- *"QuickSet"* meniu nustatykite *"PTP Bridge AP"* režimą ir pasirinkite savo šalį, kad pritaikytumėte šalies reguliavimo nustatymus;
- Nustatykite antenos stiprinimą, priklausomai nuo naudojamos antenos;
- Apatiniame lauke nustatykite maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš dirbdami su bet kokia „MikroTik“ įranga, atkreipkite dėmesį į pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine nelaimingų atsitikimų prevencijos praktika. Montuotojas turi būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Gaminys tiekiamas be gaubto ir yra skirtas montuoti apmokytiems ir kvalifikuotiems darbuotojams. Montuotojas yra atsakingas už tai, kad įrangos montavimas atitiktų vietinius ir nacionalinius elektros kodeksus. Nebandykite išardyti, taisyti ar modifikuoti įrenginio.
- Prieš pradėdami montuoti, atidžiai perskaitykite montavimo instrukcijas. Nenaudojant tinkamos aparatūros ir konfigūracijos arba nesilaikant tinkamų procedūrų, gali kilti pavojinga situacija žmonėms ir gali būti sugadinta sistema.
- Saugokite šį įrenginį nuo vandens, ugnies, drėgmės ar karštos aplinkos.
- Išpakuodami ir dirbdami su elektros komponentais naudokite riešo įžeminimo dirželį, kad išvengtumėte elektros iškrovos (ESD) žalos. Išpakavę maršruto parinktuvą padėkite ant antistatinio kilimėlio. Kai montavimo blokas užtikrina, kad nėra objektų, galinčių pažeisti PCB plokštę arba ją liesti.
- Negalime garantuoti, kad dėl netinkamo prietaiso naudojimo neįvyks nelaimingų atsitikimų ar žalos. Prašome naudoti šį gaminį atsargiai ir rizikuoti!
- Kad išvengtumėte aplinkos užteršimo, atskirkite prietaisą nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trukdžius, todėl vartotojas gali imtis atitinkamų priemonių.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.14.2 vai jaunāku versiju, lai nodrošinātu atbilstību vietējai likumdošanai.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt profesionāli uzstādītām.
:::

-

Šis dokuments attiecas uz modeli: L11UG-5HaxD.

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarīgākās šī izstrādājuma tehniskās specifikācijas ir atrodamas dokumenta pēdējā lapā.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Uzstādītāja pienākums ir nodrošināt autorizētu antenu izmantošanu; jāizmanto tikai tās antenas, kas ir sertificētas kopā ar produktu. Uzstādītājam jākonfigurē antenas izejas jaudas līmenis saskaņā ar valsts noteikumiem un katru antenas veidu. Lai nodrošinātu atbilstību veselības un drošības prasībām, ir nepieciešama savienotāju aprīkojuma profesionāla uzstādīšana.*

![](./img/image2020-2-5_9-18-11.badge.png)

**Pirmie soļi:**

- Šis produkts tiek piegādāts bez korpusa un ir paredzēts uzstādīšanai lietotāju galaproduktos vai korpusos. Šim produktam saderīgu MikroTik korpusu var atrast vietnē [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Ierīce tiek piegādāta ESD aizsargājošā iepakojumā. Strādājot ar elektriskajām iekārtām, lūdzu, ievērojiet šādus drošības pasākumus:Izpakojot un strādājot ar elektriskajām sastāvdaļām, izmantojiet plaukstas zemējuma siksnu, lai izvairītos no elektriskās izlādes (ESD) bojājumiem;
- Pēc izpakošanas, lūdzu, novietojiet maršrutētāju uz antistatiskā paklājiņa;
- Uzstādot ierīci, pārliecinieties, vai tajā nav priekšmetu, kas varētu sabojāt PCB plāksni vai pieskarties tai;
- Ierīci var uzstādīt vēlamajā vietā, izmantojot rūpnīcā paredzētos caurumus PCB plāksnē, kas atrodas katrā ierīces pusē;
- Pirms ierīces pievienošanas strāvas avotam, lūdzu, pievienojiet antenas savienotājiem;
- Pievienojiet ierīci strāvas avotam;
- Pievienojiet datoru Ethernet portam;
- Konfigurāciju ir jāveic, izmantojot WebFig pārlūku vai WinBox konfigurācijas rīku [https://mt.lv/WinBox](https://mt.lv/WinBox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Lejupielādējiet un atveriet *"WinBox"* un izvēlieties cilni *"Neighbors"*, lai atrastu ierīci;
- Noklikšķiniet uz MAC adreses. Lietotājvārds ir *"admin"* un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox sadaļu "Files" un pārstartējiet ierīci. Jauninot savu RouterOS programmatūru uz jaunāko versiju, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Izvēlnē *"QuickSet"* iestatiet *"PTP Bridge AP"* režīmu un izvēlieties savu valsti, lai piemērotu likumā noteiktos iestatījumus;
- Iestatiet antenas pastiprinājumu atkarībā no izmantotās antenas;
- Apakšējā laukā iestatiet maršrutētāja paroli.

**Drošības informācija:**

- Pirms strādājat pie jebkuras MikroTik iekārtas, apzinieties ar elektriskajām shēmām saistītos riskus un iepazīstieties ar standarta praksi negadījumu novēršanai. Instalētājam jāpārzina tīkla struktūras, termini un jēdzieni.
- Izstrādājums tiek piegādāts bez korpusa, to ir paredzēts uzstādīt korpusā. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Pirms uzstādīšanas, lūdzu, rūpīgi izlasiet montāžas instrukcijas. Pareizas aparatūras un konfigurācijas neizmantošana vai pareizu procedūru neievērošana var izraisīt bīstamu situāciju cilvēkiem un sistēmas bojājumus.
- Sargājiet šo ierīci no ūdens, uguns, mitruma vai karstas vides.
- Izpakojot un strādājot ar elektriskajām sastāvdaļām, izmantojiet plaukstas zemējuma siksnu, lai izvairītos no elektriskās izlādes (ESD) bojājumiem. Pēc izpakošanas, lūdzu, novietojiet maršrutētāju uz antistatiskā paklājiņa. Kad montāžas vienība nodrošina, ka tajā nav priekšmetu, kas varētu sabojāt PCB plāksni vai pieskarties tai.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ nenotiks negadījumi vai bojājumi. Lūdzu, izmantojiet šo produktu uzmanīgi un riskējiet!
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un atbrīvojieties no tās drošā un paredzētā veidā, piemēram, noteiktās vietās. Iepazīstieties ar kārtību, kā pareizi transportēt aprīkojumu uz noteiktajiem savākšanas punktiem jūsu apkārtnē.
- Šis ir A klases produkts. Sadzīves vidē šis produkts var izraisīt radio traucējumus, tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.14.2 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż it-tħaddim fil-kanali tal-frekwenza legali, l-enerġija tal-ħruġ, ir-rekwiżiti tal-kejbils u r-rekwiżiti tal-Għażla Dinamika tal-Frekwenza (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati professjonalment.
:::

Dan id-dokument ikopri l-mudell: L11UG-5HaxD.

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-aktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'dan id-dokument.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Hija r-responsabbiltà ta 'l-installatur li jiżgura l-użu ta' antenni awtorizzati; għandhom jintużaw biss dawk l-antenni ċċertifikati mal-prodott. L-installatur għandu jikkonfigura l-livell tal-qawwa tal-ħruġ tal-antenna skont ir-regolamenti nazzjonali u kull tip ta 'antenna. L-installazzjoni professjonali tat-tagħmir tal-konnettur hija meħtieġa biex tiżgura l-konformità mas-saħħa u s-sigurtà.*

![](./img/image2020-2-5_9-20-59.badge.png)

**L-ewwel passi:**

- Dan il-prodott jiġi mingħajr egħluq u huwa ddisinjat biex jiġi installat fil-prodotti finali jew fil-kompartimenti tal-utenti. Egħluq MikroTik kompatibbli għal dan il-prodott jista' jinstab fuq [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- L-apparat jiġi f'ippakkjar protettiv ESD. Meta timmaniġġja tagħmir elettriku jekk jogħġbok osserva l-prekawzjonijiet ta 'sigurtà li ġejjin:Uża ċinga ta 'l-ert tal-polz meta tneħħi l-ippakkjar u taħdem ma' komponenti elettriċi biex tevita ħsara ta 'skarigu elettriku (ESD);
- Wara li tneħħi l-ippakkjar jekk jogħġbok poġġi r-router fuq it-tapit anti-statiku;
- Meta twaħħal l-unità kun żgur li ma jkunx hemm oġġetti li jistgħu jagħmlu ħsara jew imissu l-pjanċa tal-PCB;
- L-apparat jista 'jiġi mmuntat fil-post mixtieq tiegħek billi tuża t-toqob ipprovduti mill-fabbrika fi pjanċa tal-PCB, li tinsab fuq kull naħa tal-apparat;
- Qabel ma tgħaqqad l-apparat mas-sors tal-enerġija, jekk jogħġbok waħħal l-antenni mal-konnetturi;
- Qabbad l-apparat mas-sors tal-enerġija;
- Qabbad il-PC tiegħek mal-port Ethernet;
- Il-konfigurazzjoni għandha tkun mfassla bl-użu ta 'WebFig jew l-għodda tal-konfigurazzjoni WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Niżżel u tiftaħ *"WinBox"*, u agħżel it- tab *"Neighbors"* biex issib l-apparat;
- Ikklikkja fuq l-indirizz MAC. L-isem tal-utent huwa *"admin"* u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u mingħajr fili fuq l-istiker);
- Ikklikkja fuq il-buttuna "Check for updates" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Żid id-pakketti li dawn tniżżel fil-meni "Files" ta 'WebFig jew WinBox u rirreboot l-apparat. Billi taġġorna s-softwer RouterOS tiegħek għall-aħħar verżjoni, tista 'tiżgura l-aħjar prestazzjoni, stabbiltà u aġġornamenti tas-sigurtà;
- Fil- menu *"QuickSet"* waqqaf il -mod *"PTP Bridge AP"* u agħżel pajjiżek, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Issettja l-gwadann tal-antenna, skont l-antenna użata;
- Issettja l-password tar-router tiegħek fil-qasam t'isfel.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni tal-inċidenti. L-installatur għandu jkun familjari mal-istrutturi, it-termini u l-kunċetti tan-netwerk.
- Il-prodott jiġi mingħajr egħluq u huwa maħsub biex jiġi installat fl-għeluq minn persunal imħarreġ u kwalifikat. L-installatur huwa responsabbli biex jiżgura li l-Installazzjoni tat-tagħmir tkun konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax iżarma, isewwi jew timmodifika l-apparat.
- Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. In-nuqqas li tuża l-ħardwer u l-konfigurazzjoni korretti jew li ssegwi l-proċeduri korretti jista 'jirriżulta f'sitwazzjoni perikoluża għan-nies u ħsara lis-sistema.
- Żomm dan l-apparat 'il bogħod mill-ilma, nar, umdità, jew ambjenti sħan.
- Uża ċinga ta 'l-ert tal-polz meta tneħħi l-ippakkjar u taħdem ma' komponenti elettriċi biex tevita ħsara minn skarigu elettriku (ESD). Wara li tneħħi l-ippakkjar jekk jogħġbok poġġi r-router fuq it-tapit anti-statiku. Meta unità ta 'immuntar tiżgura li ma jkunx hemm oġġetti li jistgħu jagħmlu ħsara jew imissu l-pjanċa tal-PCB.
- Ma nistgħux niggarantixxu li ma jseħħu l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u topera għar-riskju tiegħek!
- Biex tevita l-kontaminazzjoni ta 'l-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sigur, per eżempju, f'żoni magħżula. Sir familjari mal-proċeduri biex it-tagħmir jiġi ttrasportat sewwa għal punti magħżula tal-ġbir fl-inħawi tiegħek.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza tar-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.14.2 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, waaronder de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparatuur moet professioneel geïnstalleerd zijn.
:::

Dit document heeft betrekking op het model: L11UG-5HaxD.

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties van dit product vindt u op de laatste pagina van dit document.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Odgovornost je instalatera osigurati korištenje ovlaštenih antena; smiju se koristiti samo one antene certificirane s proizvodom. Instalater mora konfigurirati razinu izlazne snage antene u skladu s nacionalnim propisima i svakim tipom antene. Potrebna je profesionalna instalacija priključne opreme kako bi se osigurala usklađenost sa zdravljem i sigurnošću.*

![](./img/image2020-2-5_9-22-25.badge.png)

**Eerste stappen:**

- Dit product wordt geleverd zonder behuizing en is ontworpen om te worden geïnstalleerd in de eindproducten of behuizingen van de gebruiker. Compatibele MikroTik-behuizing voor dit product vindt u op [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Het apparaat wordt geleverd in een ESD-beschermende verpakking. Neem bij het hanteren van elektrische apparatuur de volgende veiligheidsmaatregelen in acht:Gebruik een aardingspolsband bij het uitpakken en werken met elektrische componenten om schade door elektrische ontladingen (ESD) te voorkomen;
- Plaats de router na het uitpakken op de antistatische mat;
- Zorg er bij het monteren van de unit voor dat er geen voorwerpen zijn die de printplaat kunnen beschadigen of aanraken;
- Het apparaat kan op de door u gewenste locatie worden gemonteerd met behulp van de in de fabriek aangebrachte gaten in een PCB-plaat, gelegen aan elke kant van het apparaat;
- Voordat u het apparaat op de stroombron aansluit, sluit u de antennes aan op de connectoren;
- Sluit het apparaat aan op de stroombron;
- Sluit uw pc aan op de Ethernet-poort;
- Configuratie moet worden gedaan met behulp van de WebFig-webbrowser of het WinBox-configuratiehulpprogramma [https://mt.lv/WinBox](https://mt.lv/WinBox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Download en open *"WinBox"* en kies het tabblad *"Neighbors"* om het apparaat te vinden;
- Klik op het MAC-adres. De gebruikersnaam is *"admin"* en er is geen wachtwoord (of, voor sommige modellen, controleer gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat. Door uw RouterOS-software te upgraden naar de nieuwste versie, kunt u zorgen voor optimale prestaties, stabiliteit en beveiligingsupdates;
- Stel in het menu *"QuickSet"* de modus *"PTP Bridge AP"* in en kies uw land om de instellingen voor landregulering toe te passen;
- Stel de antenneversterking in, afhankelijk van de gebruikte antenne;
- Stel uw routerwachtwoord in het onderste veld in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur gaat werken, dient u zich bewust te zijn van de gevaren van elektrische circuits en vertrouwd te zijn met de standaardprocedures voor het voorkomen van ongevallen. De installateur moet bekend zijn met netwerkstructuren, termen en concepten.
- Het product wordt geleverd zonder behuizing en is bedoeld om door getraind en gekwalificeerd personeel in de behuizing te worden geïnstalleerd. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektriciteitsvoorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het niet volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- Houd dit apparaat uit de buurt van water, vuur, vochtigheid of hete omgevingen.
- Gebruik een aardingspolsband bij het uitpakken en werken met elektrische componenten om schade door elektrische ontlading (ESD) te voorkomen. Plaats de router na het uitpakken op de antistatische mat. Wanneer een montage-unit ervoor zorgt dat er geen objecten zijn die de printplaat kunnen beschadigen of raken.
- We kunnen niet garanderen dat er geen ongelukken of schade ontstaan ​​door oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Om milieuverontreiniging te voorkomen, dient u het apparaat van het huisvuil te scheiden en op een veilige manier af te voeren, bijvoorbeeld in daarvoor bestemde ruimtes. Zorg dat u vertrouwd raakt met de procedures voor het correct vervoeren van de apparatuur naar aangewezen inzamelpunten in uw omgeving.
- Dit is een klasse A-product. In een huiselijke omgeving kan dit product radiostoring veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen moet nemen.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.14.2 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być profesjonalnie zainstalowane.
:::

Ten dokument dotyczy modelu: L11UG-5HaxD.

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu znajdują się na ostatniej stronie tego dokumentu.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Instalator jest odpowiedzialny za zapewnienie użycia autoryzowanych anten; należy używać wyłącznie anten certyfikowanych wraz z produktem. Instalator musi skonfigurować poziom mocy wyjściowej anteny zgodnie z przepisami krajowymi i każdym typem anteny. Aby zapewnić przestrzeganie zasad BHP, wymagana jest profesjonalna instalacja sprzętu połączeniowego.*

![](./img/image2020-2-5_9-39-6.badge.png)

**Pierwsze kroki:**

- Ten produkt jest dostarczany bez obudowy i jest przeznaczony do montażu w produktach końcowych lub obudowach użytkowników. Kompatybilną obudowę MikroTik dla tego produktu można znaleźć na stronie [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Urządzenie jest dostarczane w opakowaniu ochronnym ESD. Podczas obchodzenia się ze sprzętem elektrycznym należy przestrzegać następujących środków ostrożności:Podczas rozpakowywania i pracy z elementami elektrycznymi należy nosić pasek uziemiający na nadgarstku, aby uniknąć uszkodzeń spowodowanych wyładowaniami elektrycznymi (ESD);
- Po rozpakowaniu router należy położyć na macie antystatycznej;
- Podczas montażu urządzenia należy upewnić się, że nie ma żadnych przedmiotów, które mogłyby uszkodzić lub dotknąć płytki PCB;
- Urządzenie można zamontować w wybranym miejscu, korzystając z fabrycznie dostarczonych otworów w płytce PCB, znajdujących się po obu stronach urządzenia;
- Przed podłączeniem urządzenia do źródła zasilania należy podłączyć anteny do złączy;
- Podłącz urządzenie do źródła zasilania;
- Podłącz swój komputer do portu Ethernet;
- Konfiguracja powinna być dokonywana za pomocą przeglądarki internetowej WebFig lub narzędzia konfiguracyjnego WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Pobierz i otwórz *"WinBox"*, a następnie wybierz kartę *"Neighbors"*, aby znaleźć urządzenie;
- Kliknij adres MAC. Nazwa użytkownika to *"admin"* i nie ma hasła (lub, w przypadku niektórych modeli, sprawdź hasło użytkownika i hasła sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Wgraj pobrane pakiety do menu "Files" w WebFig lub WinBox i zrestartuj urządzenie. Aktualizując oprogramowanie RouterOS do najnowszej wersji, możesz zapewnić optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu *"QuickSet"* ustaw tryb *"PTP Bridge AP"* i wybierz swój kraj, aby zastosować ustawienia przepisów krajowych;
- Ustaw wzmocnienie anteny w zależności od używanej anteny;
- Skonfiguruj hasło routera w dolnym polu.

**Informacje dotyczące bezpieczeństwa:**

- Zanim zaczniesz pracować na jakimkolwiek sprzęcie MikroTik, bądź świadomy zagrożeń związanych z obwodami elektrycznymi i zapoznaj się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien znać struktury sieci, terminy i koncepcje.
- Produkt jest dostarczany bez obudowy i jest przeznaczony do montażu w obudowie przez przeszkolony i wykwalifikowany personel. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie próbuj demontować, naprawiać ani modyfikować urządzenia.
- Przed przystąpieniem do instalacji prosimy o uważne przeczytanie instrukcji montażu. Niewłaściwe użycie sprzętu i konfiguracji lub nieprzestrzeganie właściwych procedur może spowodować niebezpieczną sytuację dla ludzi i uszkodzenie systemu.
- Trzymaj to urządzenie z dala od wody, ognia, wilgoci lub gorących środowisk.
- Podczas rozpakowywania i pracy z komponentami elektrycznymi używaj opaski uziemiającej na nadgarstek, aby uniknąć uszkodzenia spowodowanego wyładowaniem elektrycznym (ESD). Po rozpakowaniu należy umieścić router na macie antystatycznej. Kiedy jednostka montażowa upewnia się, że nie ma żadnych przedmiotów, które mogłyby uszkodzić lub dotknąć płytki PCB.
- Nie możemy zagwarantować, że w wyniku niewłaściwego użytkowania urządzenia nie wystąpią żadne wypadki ani szkody. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- Aby uniknąć zanieczyszczenia środowiska, oddziel urządzenie od odpadów domowych i utylizuj je w bezpieczny sposób, na przykład w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w którym to przypadku użytkownik może być zobowiązany do podjęcia odpowiednich środków.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.14.2 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados profissionalmente.
:::

Este documento abrange o modelo: L11UG-5HaxD.

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes deste produto encontram-se na última página deste documento.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*É responsabilidade do instalador garantir o uso de antenas autorizadas; somente as antenas certificadas com o produto devem ser usadas. O instalador deve configurar o nível de potência de saída da antena de acordo com os regulamentos nacionais e cada tipo de antena. A instalação profissional do equipamento conector é necessária para garantir a conformidade com a saúde e a segurança.*

![](./img/image2020-2-5_9-40-42.badge.png)

**Primii pasi:**

- Este produto vem sem caixa e foi projetado para ser instalado em produtos finais ou casos de usuário. O gabinete MikroTik compatível para este produto pode ser encontrado em [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- O dispositivo vem em uma embalagem protetora contra ESD. Ao manusear equipamentos elétricos, observe as seguintes precauções de segurança:Use uma pulseira de aterramento ao desembalar e trabalhar com componentes elétricos para evitar danos por descarga elétrica (ESD);
- Após desembalar, coloque o roteador sobre o tapete antiestático;
- Ao montar a unidade, certifique-se de que não haja objetos que possam danificar ou tocar a placa PCB;
- O dispositivo pode ser montado no local desejado através dos furos fornecidos de fábrica em uma placa PCB, localizada em cada lado do dispositivo;
- Antes de conectar o dispositivo à fonte de alimentação, conecte as antenas aos conectores;
- Conecte o dispositivo à fonte de alimentação;
- Conecte seu PC à porta Ethernet;
- A configuração deve ser feita usando o navegador da Web WebFig ou a ferramenta de configuração WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Baixe e abra o “WinBox” e escolha o guia “Vizinhos” para encontrar um dispositivo;
- Clique no endereço MAC. O nome de usuário é “admin” e não há senha (ou, para alguns modelos, verifique se a senha do usuário é wireless sem adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Carregue os pacotes baixados no menu "Files" do WebFig ou WinBox e reinicie o dispositivo. Ao atualizar o software RouterOS para a versão mais recente, você pode garantir desempenho ideal, estabilidade e atualizações de segurança;
- No menu “QuickSet”, configure o modo “PTP Bridge AP” e escolha o seu país, para aplicar as configurações regulatórias do país;
- Definir um gancho de antena, dependendo da antena utilizada;
- Configure uma senha do roteador no campo inferior.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos perigos envolvidos com circuitos elétricos e familiarize-se com as práticas padrão para prevenir acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- O produto vem sem invólucro e deve ser instalado no invólucro por pessoal treinado e qualificado. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Leia atentamente as instruções de montagem antes de iniciar a instalação. A falha em usar o hardware e configuração corretos ou em seguir os procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danos ao sistema.
- Mantenha este dispositivo longe de água, fogo, umidade ou ambientes quentes.
- Use uma pulseira de aterramento ao desembalar e trabalhar com componentes elétricos para evitar danos por descarga elétrica (ESD). Depois de desembalar, coloque o roteador no tapete antiestático. Quando uma unidade de montagem garante que não haja objetos que possam danificar ou tocar a placa PCB.
- Não podemos garantir que não ocorram acidentes ou danos devido ao uso indevido do aparelho. Por favor, use este produto com cuidado e opere por sua conta e risco!
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para o transporte adequado do equipamento aos pontos de coleta designados em sua área.
- Este é um produto de Classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio, caso em que o usuário pode ser obrigado a tomar as medidas adequadas.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.14.2 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie să fie instalate profesional.
:::

Acest document acoperă modelul: L11UG-5HaxD.

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui document.*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Este responsabilitatea instalatorului să asigure utilizarea antenelor autorizate; trebuie folosite doar acele antene certificate cu produsul. Instalatorul trebuie să configureze nivelul puterii de ieșire a antenei în conformitate cu reglementările naționale și cu fiecare tip de antenă. Instalarea profesională a echipamentelor de conectare este necesară pentru a asigura conformitatea cu sănătatea și securitatea.*

![](./img/image2020-2-5_9-42-33.badge.png)

**Primii pasi:**

- Acest produs vine fără carcasă și este proiect pentru a fi instalat în produs final sau în carcasele utilisadores. Carcasa compatibilă MikroTik pentru acest produs poate fi găsită la [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Dispositiful vine în ambalaj de protecție ESD. Când manipulați echipamente electrice, vă rugăm să respectați următoarele măsuri de siguranță:Utilizați o cure de impământare pentru multetura mandeii when despachetati și workați cu componentele electrice pentru a evita deteriorarea prin electriquerea dischargea (ESD);
- Dupa despachetare, asezati routerul pe capacul antistatic;
- Când montați unitatea, asigurați-vă că există obiecte care pot deteriora PCB-ul;
- Dispositiful poate fi montat în locația dorită using orificiile furnizate din fabrică pe o placă PCB, situată pe fiecare parte a dispozitiv;
- Înainte de a conecta dispozitivul la sursa de alimentare, vă rugăm să atașați antenele la conectori;
- Conectați dispozitivul la sursa de alimentare;
- Conectați computerul la portul Ethernet;
- Configurarea trebuie efectuată cu ajutorul browserului web WebFig sau a instrumentului de configurare WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Faça o download e abra "WinBox" and scolha a guide "Neighbours" pentru a găsi o dispozitiv;
- Clic fără adresa MAC. O nome de ususivo é "admin" e não há senha (ou, para alguns modelos, verificare as senhas de ususivo e wireless no adesivo);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul. Actualizându-vă software-ul RouterOS la cea mai recentă versiune, puteți garanta performanță optimă, stabilitate și actualizări de securitate;
- Din meniul „QuickSet”, configurați modul „PTP Bridge AP” și alegeți țara dvs., pentru a aplica setările de reglementare ale țării;
- Defina o ganho da antenna, in functie de antena folosita;
- Configurați un senha do roteador no campo inferior.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștient de pericolele implicate de circuitele electrice și familiarizați-vă cu practicile standard pentru prevenirea accidentelor. Instalatorul trebuie să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Produsul vine fără carcasă și este menit să fie instalat în carcasă de către personal instruit și calificat. Instalatorul este responsabil să se asigure că instalarea echipamentului este conformă cu codurile electrice locale și naționale. Nu încercați să dezasamblați, să reparați sau să modificați dispozitivul.
- Vă rugăm să citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Neutilizarea hardware-ului și configurației corecte sau nerespectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului.
- Țineți acest dispozitiv departe de apă, foc, umiditate sau medii fierbinți.
- Utilizați o curea de împământare pentru încheietura mâinii atunci când despachetați și lucrați cu componentele electrice pentru a evita deteriorarea prin descărcarea electrică (ESD). După despachetare, așezați routerul pe covorașul antistatic. Când o unitate de montare se asigură că nu există obiecte care pot deteriora sau atinge placa PCB.
- Nu putem garanta că nu vor avea loc accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să utilizați pe propriul risc!
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-le într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător al echipamentelor la punctele de colectare desemnate din zona dumneavoastră.
- Acesta este un produs de clasa A. Într-un mediu casnic, acest produs ar putea provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.14.2 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť profesionálne nainštalované.
:::

Tento dokument sa vzťahuje na model: L11UG-5HaxD.

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto dokumentu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Je zodpovednosťou inštalatéra zabezpečiť používanie autorizovaných antén; mali by sa používať iba antény certifikované s produktom. Inštalačný technik musí nakonfigurovať výstupný výkon antény v súlade s národnými predpismi a každým typom antény. Na zabezpečenie súladu so BOZP je potrebná odborná montáž konektorového zariadenia.*

![](./img/image2020-2-5_9-44-55.badge.png)

**Prvé kroky:**

- Tento produkt sa dodáva bez krytu a je navrhnutý na inštaláciu do koncových produktov alebo krytov používateľov. Kompatibilný kryt MikroTik pre tento produkt nájdete na [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Zariadenie je dodávané v ESD ochrannom obale. Pri manipulácii s elektrickým zariadením dodržiavajte nasledujúce bezpečnostné opatrenia:Pri vybaľovaní a práci s elektrickými komponentmi používajte uzemňovací pásik na zápästie, aby ste predišli poškodeniu elektrickým výbojom (ESD);
- Po vybalení položte router na antistatickú podložku;
- Pri montáži jednotky sa uistite, že v nej nie sú žiadne predmety, ktoré by mohli poškodiť alebo sa dotknúť dosky plošných spojov;
- Zariadenie je možné namontovať na požadované miesto pomocou továrenských otvorov v doske PCB, ktoré sa nachádzajú na každej strane zariadenia;
- Pred pripojením zariadenia k zdroju napájania pripojte antény ku konektorom;
- Pripojte zariadenie k zdroju napájania;
- Pripojte počítač k portu Ethernet;
- Konfiguráciu treba vykonať pomocou webového prehliadača WebFig alebo nástroja na konfiguráciu WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Stiahnite si a otvorte *"WinBox"* a vyberte kartu *"Neighbors"*, aby ste našli zariadenie;
- Kliknite na MAC adresu. Používateľské meno je *"admin"* a neexistuje žiadne heslo (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslo na nálepke);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v aplikácii WebFig alebo WinBox a reštartujte zariadenie. Inováciou softvéru RouterOS na najnovšiu verziu môžete zaistiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- V ponuke *"QuickSet"* nastavte režim *"PTP Bridge AP"* a vyberte svoju krajinu, aby ste použili nastavenia regulácie krajiny;
- Nastavte zisk antény v závislosti od použitej antény;
- V spodnom poli nastavte heslo smerovača.

**Bezpečnostné informácie:**

- Skôr ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si nebezpečenstvá spojené s elektrickými obvodmi a oboznámte sa so štandardnými postupmi na predchádzanie nehodám. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, termínmi a konceptmi.
- Produkt sa dodáva bez krytu a je určený na inštaláciu do krytu vyškoleným a kvalifikovaným personálom. Inštalatér je zodpovedný za uistenie sa, že inštalácia zariadenia je v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Nepoužitie správneho hardvéru a konfigurácie alebo nedodržanie správnych postupov môže viesť k nebezpečnej situácii pre ľudí a poškodeniu systému.
- Udržujte toto zariadenie mimo dosahu vody, ohňa, vlhkosti alebo horúceho prostredia.
- Pri vybaľovaní a práci s elektrickými komponentmi používajte uzemňovací pásik na zápästie, aby ste predišli poškodeniu elektrickým výbojom (ESD). Po vybalení položte router na antistatickú podložku. Keď sa montážna jednotka ubezpečuje, že neexistujú žiadne predmety, ktoré by mohli poškodiť alebo sa dotknúť dosky plošných spojov.
- Nemôžeme zaručiť, že v dôsledku nesprávneho používania zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a prevádzkujte ho na vlastné riziko!
- Aby ste zabránili kontaminácii životného prostredia, odpojte prístroj od domáceho odpadu a zneškodnite ho bezpečným spôsobom, napríklad na určených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.
- Toto je výrobok triedy A. V domácom prostredí môže tento výrobok spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa vyžadované prijatie primeraných opatrení.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.14.2 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom, vključno z delovanjem v legalnih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami za dinamično izbiro frekvence (DFS). Vse radijske naprave MikroTik morajo biti strokovno nameščene.
:::

Ta dokument zajema model: L11UG-5HaxD.

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega dokumenta.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Za zagotovitev uporabe pooblaščenih anten je odgovoren monter; uporabljajte samo tiste antene, ki so certificirane z izdelkom. Monter mora konfigurirati izhodno moč antene v skladu z nacionalnimi predpisi in vsako vrsto antene. Za zagotovitev skladnosti z zdravjem in varnostjo je potrebna profesionalna namestitev priključne opreme.*

![](./img/image2020-2-5_9-46-47.badge.png)

**Prvi koraki:**

- Ta izdelek je na voljo brez ohišja in je zasnovan za vgradnjo v končne izdelke ali ohišja uporabnikov. Združljivo ohišje MikroTik za ta izdelek lahko najdete na [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Naprava je v ESD zaščitni embalaži. Pri ravnanju z električno opremo upoštevajte naslednje varnostne ukrepe:Pri razpakiranju in delu z električnimi komponentami uporabljajte zapestni ozemljitveni trak, da preprečite poškodbe zaradi električne razelektritve (ESD);
- Po razpakiranju postavite usmerjevalnik na antistatično podlogo;
- Pri nameščanju enote se prepričajte, da ni nobenih predmetov, ki bi lahko poškodovali ali se dotaknili plošče PCB;
- Napravo lahko namestite na želeno mesto s pomočjo tovarniško predvidenih lukenj v plošči PCB, ki se nahajajo na vsaki strani naprave;
- Preden napravo priključite na vir napajanja, priključite antene na priključke;
- Priključite napravo na vir napajanja;
- Priključite računalnik na vrata Ethernet;
- Konfiguracijo je treba izvesti s pomočjo spletnega brskalnika WebFig ali orodja za konfiguracijo WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Prenesite in odprite *"WinBox"* ter izberite zavihek *"Neighbors"*, da poiščete napravo;
- Kliknite naslov MAC. Uporabniško ime je *"admin"* in ni gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Kliknite na gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" v aplikaciji WebFig ali WinBox in znova zaženite napravo. Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno zmogljivost, stabilnost in varnostne posodobitve;
- V meniju *"QuickSet"* nastavite način *"PTP Bridge AP"* in izberite svojo državo, da uporabite nastavitve državnih predpisov;
- Nastavite ojačanje antene glede na uporabljeno anteno;
- V spodnjem polju nastavite geslo usmerjevalnika.

**Varnostne informacije:**

- Preden začnete delati na kateri koli opremi MikroTik, se zavedajte nevarnosti, povezanih z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Izdelek je na voljo brez ohišja in je namenjen za vgradnjo v ohišje s strani usposobljenega in kvalificiranega osebja. Monter je odgovoren za zagotovitev, da je namestitev opreme skladna z lokalnimi in nacionalnimi električnimi predpisi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba pravilne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarno situacijo za ljudi in škodo na sistemu.
- Napravo hranite stran od vode, ognja, vlage ali vročih okolij.
- Pri razpakiranju in delu z električnimi komponentami uporabite zapestni ozemljitveni trak, da se izognete poškodbam zaradi električne razelektritve (ESD). Po razpakiranju postavite usmerjevalnik na antistatično podlogo. Ko montažna enota poskrbi, da ni predmetov, ki bi lahko poškodovali ali se dotaknili plošče PCB.
- Ne moremo zagotoviti, da zaradi nepravilne uporabe naprave ne bo prišlo do nesreč ali škode. Prosimo, uporabljajte ta izdelek previdno in delajte na lastno odgovornost!
- Da se izognete onesnaženju okolja, napravo ločite od gospodinjskih odpadkov in jo varno odvrzite, na primer na določena mesta. Spoznajte postopke za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru bo uporabnik morda moral sprejeti ustrezne ukrepe.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.14.2 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste vara professionellt installerade.
:::

Detta dokument täcker modellen: L11UG-5HaxD.

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på sista sidan i detta dokument.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Det är installatörens ansvar att säkerställa användningen av auktoriserade antenner; endast de antenner som är certifierade med produkten ska användas. Installatören måste konfigurera antennens uteffektnivå i enlighet med nationella bestämmelser och varje antenntyp. Professionell installation av anslutningsutrustning krävs för att säkerställa överensstämmelse med hälsa och säkerhet.*

![](./img/image2020-2-5_9-47-44.badge.png)

**Första stegen:**

- Denna produkt kommer utan kapsling och är designad för att installeras i användarens slutprodukter eller kapslingar. Kompatibel MikroTik-kapsling för denna produkt finns på [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Enheten kommer i ESD-skyddande förpackning. Vid hantering av elektrisk utrustning vänligen observera följande säkerhetsföreskrifter:Använd ett jordningsband för handleden när du packar upp och arbetar med elektriska komponenter för att undvika skador på elektrisk urladdning (ESD);
- Efter uppackning, placera routern på den antistatiska mattan;
- När du monterar enheten se till att det inte finns några föremål som kan skada eller vidröra PCB-plattan;
- Enheten kan monteras på önskad plats med hjälp av de fabriksförsedda hålen i en PCB-platta, placerad på varje sida av enheten;
- Innan du ansluter enheten till strömkällan, vänligen anslut antennerna till kontakterna;
- Anslut enheten till strömkällan;
- Anslut din dator till Ethernet-porten;
- Konfigurationen bör göras med hjälp av webbläsaren WebFig eller konfigurationsverktyget WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Ladda ner och öppna *"WinBox"* och välj fliken *"Neighbors"* för att hitta enheten;
- Klicka på MAC-adressen. Användarnamnet är *"admin"* och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten. Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I *"QuickSet"*-menyn, ställ in *"PTP Bridge AP"*-läget och välj ditt land för att tillämpa inställningarna för landsbestämmelser;
- Ställ in antennförstärkningen, beroende på vilken antenn som används;
- Ställ in ditt routerlösenord i det nedre fältet.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning, var medveten om farorna med elektriska kretsar och bekanta dig med standardpraxis för att förebygga olyckor. Installatören bör vara bekant med nätverksstrukturer, termer och koncept.
- Produkten levereras utan kapsling och är avsedd att installeras i kapslingen av utbildad och kvalificerad personal. Installatören är ansvarig för att se till att installationen av utrustningen är förenlig med lokala och nationella elektriska bestämmelser. Försök inte att demontera, reparera eller modifiera enheten.
- Läs monteringsinstruktionerna noggrant innan du påbörjar installationen. Underlåtenhet att använda rätt hårdvara och konfiguration eller att följa de korrekta procedurerna kan resultera i en farlig situation för människor och skada på systemet.
- Håll den här enheten borta från vatten, eld, fukt eller heta miljöer.
- Använd ett jordningsband för handleden när du packar upp och arbetar med elektriska komponenter för att undvika skador på elektrisk urladdning (ESD). Efter uppackning, placera routern på den antistatiska mattan. När en monteringsenhet ser till att det inte finns några föremål som kan skada eller vidröra PCB-plattan.
- Vi kan inte garantera att inga olyckor eller skador inträffar på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd på egen risk!
- För att undvika förorening av miljön, separera enheten från hushållsavfall och kassera den på ett säkert sätt, till exempel i avsedda områden. Bli bekant med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsställen i ditt område.
- Detta är en klass A -produkt. I hemmet kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.14.2或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规，包括在合法频道内操作、输出功率、布线要求和动态频率选择（DFS）要求。所有 MikroTik 无线电设备必须专业安装。
:::

本文档涵盖型号：L11UG-5HaxD。

*这是无线网络设备。您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。或使用手机扫描QR码。*
*有关产品的技术规格，手册和更多信息，请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*本产品最重要的技术规格可在本文档的最后一页找到。*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*安裝人員有責任確保使用授權的天線；只能使用經產品認證的天線。安裝人員必鬚根據國家法規和每種天線類型配置天線輸出功率電平。需要專業安裝連接器設備以確保符合健康和安全要求。*

![](./img/image2020-2-5_9-49-44.badge.png)

**第一步：**

- 该产品不带外壳，设计用于安装到用户的最终产品或外壳中。可在[https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures 找到与本产品兼容的 MikroTik 外壳
- 该设备采用 ESD 防护包装。处理电气设备时，请遵守以下安全预防措施:打开包装和操作电气元件时，请使用接地腕带，以避免放电 (ESD) 损坏；
- 打开包装后请将路由器放置在防静电垫上；
- 安装设备时，确保没有任何物体会损坏或接触 PCB 板；
- 可以使用位于设备两侧的 PCB 板上工厂提供的孔将设备安装在您所需的位置；
- 在将设备连接到电源之前，请将天线连接到连接器上；
- 将设备连接至电源；
- 将您的 PC 连接到以太网端口；
- 应使用 *"WinBox"* 配置工具[https://mt.lv/winbox](https://mt.lv/winbox) 进行配置；
- 下载并打开 *"WinBox"*，选择 *"Neighbors"* 选项卡找到设备；
- 单击 MAC 地址。用户名是 *"admin"* 并且没有密码（或者，对于某些型号，检查标签上的用户和无线密码）；
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 如需手动更新设备，请访问产品页面[https://mikrotik.com/products](https://mikrotik.com/products) 查找您的产品。所需的软件包可在 "Support&Downloads" 菜单下获取；
- 将下载的包上传到 *"WinBox Files"* 菜单并重新启动设备。通过将您的 RouterOS 软件升级到最新版本，您可以确保最佳性能、稳定性和安全更新；
- 在 *"QuickSet"* 菜单中设置 *"PTP Bridge AP"* 模式，选择你的国家，应用国家法规设置；
- 根据使用的天线设置天线增益；
- 在底部字段中设置您的路由器密码。

**安全信息：**

- 在您使用任何 MikroTik 設備之前，請注意與電路有關的危險，並熟悉預防事故的標準做法。安裝人員應熟悉網絡結構、術語和概念。
- 該產品不帶外殼，應由經過培訓的合格人員安裝到外殼中。安裝人員負責確保設備的安裝符合當地和國家電氣規範。請勿嘗試拆卸、修理或改裝設備。
- 開始安裝前請仔細閱讀安裝說明。未能使用正確的硬件和配置或未遵循正確的程序可能會導致人身傷害和系統損壞。
- 使本設備遠離水、火、濕氣或熱環境。
- 打開包裝和使用電氣組件時，請使用接地腕帶以避免放電 (ESD) 損壞。開箱後請將路由器放在防靜電墊上。當安裝單元確保沒有可能損壞或接觸 PCB 板的物體時。
- 我們不能保證不會因設備使用不當而發生事故或損壞。請謹慎使用本產品，操作風險自負！
- 为避免污染环境，请将设备与生活垃圾分开，并以安全的方式进行处置，例如在指定区域。熟悉将设备正确运输到您所在地区指定收集点的过程。
- 这是 A 类产品。在家庭环境中，本产品可能会造成无线电干扰，在这种情况下，用户可能需要采取足够的措施

**射频辐射暴露：** 此 MikroTik 设备符合针对不受控制的环境规定的欧盟辐射暴露限制。 此 MikroTik 设备的安装和使用距离您的身体、专业用户或公众不得超过 20 厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.14.2 или до последней версии, чтобы обеспечить соответствие требованиям местных органов власти.
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, выходной мощности, требований к кабелям и требований к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть профессионально установлены.
:::

Краткое руководство охватывает модель: L11UG-5HaxD.

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого документа.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ответственность за использование авторизованных антенн лежит на установщике; следует использовать только те антенны, которые сертифицированы для данного продукта. Установщик должен настроить уровень выходной мощности антенны в соответствии с национальным законодательством и каждым типом антенны. Профессиональная установка соединительного оборудования необходима для обеспечения соблюдения требований охраны здоровья и безопасности.*

![](./img/image-2022-12-9_12-38-55.badge.png)

**Первые шаги:**

- Этот продукт поставляется без корпуса и предназначен для установки в конечные продукты или корпуса пользователей. Совместимый корпус MikroTik для этого продукта можно найти по адресу [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures.
- Устройство поставляется в упаковке с защитой от электростатического разряда. При обращении с электрооборудованием соблюдайте следующие меры предосторожности:Используйте заземляющий браслет при распаковке и работе с электрическими компонентами, чтобы избежать повреждения электрическим разрядом (ESD);
- После распаковки поместите маршрутизатор на антистатический коврик;
- При монтаже устройства убедитесь, что нет предметов, которые могут повредить или коснуться платы печатной платы;
- Устройство можно установить в желаемом месте, используя предусмотренные на заводе отверстия в пластине печатной платы, расположенные с каждой стороны устройства;
- Перед подключением устройства к источнику питания, подключите антенны к разъемам;
- Подключите устройство к источнику питания;
- Подключите компьютер к порту Ethernet;
- Конфигурация должна выполняться с использованием веб-браузера WebFig или инструмента конфигурации WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **существует несколько методов настройки для обеспечения доступности;**
- Загрузите и откройте *"WinBox"* и выберите вкладку *"Neighbors"*, чтобы найти устройство;
- Нажмите на MAC-адрес. Имя пользователя *"admin"* и пароль отсутствует (или, для некоторых моделей, проверьте пароль пользователя и беспроводной сети на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" в WebFig или WinBox и перезагрузите устройство. Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню *"QuickSet"* настройте режим *"PTP Bridge AP"* и выберите свою страну, чтобы применить настройки регулирования страны;
- Установите коэффициент усиления антенны в зависимости от используемой антенны;
- Установите пароль маршрутизатора в нижнем поле.

**Информация по технике безопасности:**

- Прежде чем приступить к работе с любым оборудованием MikroTik, ознакомьтесь с опасностями, связанными с электрическими схемами, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком со структурой сети, терминами и понятиями.
- Продукт поставляется без корпуса и предназначен для установки в корпус обученным и квалифицированным персоналом. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Перед началом установки внимательно прочтите инструкции по монтажу. Неправильное использование аппаратного обеспечения и конфигурации или несоблюдение правильных процедур может привести к возникновению опасной ситуации для людей и повреждению системы.
- Держите это устройство вдали от воды, огня, влаги или горячих сред.
- Используйте заземляющий браслет при распаковке и работе с электрическими компонентами, чтобы избежать повреждения электрическим разрядом (ЭСР). После распаковки положите маршрутизатор на антистатический коврик. Когда монтажный блок проверяет, нет ли предметов, которые могут повредить или коснуться платы печатной платы.
- Мы не можем гарантировать отсутствие несчастных случаев или повреждений из-за неправильного использования устройства. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
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

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 5150-5350 МГц, 5650-5850 МГц | ≤100 мВт |

Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 20 сантиметров от человека.*

Производитель: Mikrotikls SIA, улица Унияс 2. Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

![](./img/image2020-1-24_7-55-5.badge.png)

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.14.2 або останньої версії, щоб забезпечити відповідність нормам місцевої влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи використання пристрою в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей документ стосується моделі: L11UG-5HaxD.

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього продукту можна знайти на останній сторінці цього документа.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Відповідальність за використання авторизованих антен несе установник; слід використовувати лише ті антени, які сертифіковані разом із продуктом. Установник повинен налаштувати рівень вихідної потужності антени відповідно до національних правил і кожного типу антени. Для забезпечення відповідності вимогам безпеки та здоров’я необхідний професійний монтаж з’єднувального обладнання.*

![](./img/image-2022-12-9_12-48-16.badge.png)

**Перші кроки:**

- Цей продукт поставляється без корпусу та призначений для встановлення в кінцеві продукти або корпуси користувачів. Сумісний корпус MikroTik для цього продукту можна знайти за адресою [https://mikrotik.com/products](https://mikrotik.com/products)/group/enclosures
- Пристрій поставляється в антистатичній упаковці. Під час роботи з електричним обладнанням дотримуйтесь наступних заходів безпеки:Використовуйте ремінець заземлення під час розпакування та роботи з електричними компонентами, щоб уникнути пошкодження електричним розрядом (ESD);
- Після розпакування покладіть маршрутизатор на антистатичний килимок;
- Під час монтажу пристрою переконайтеся, що немає предметів, які можуть пошкодити або торкнутися пластини друкованої плати;
- Пристрій можна встановити у бажаному місці за допомогою заводських отворів у пластині друкованої плати, розташованих з кожного боку пристрою;
- Перед підключенням пристрою до джерела живлення, приєднайте антени до роз’ємів;
- Підключіть пристрій до джерела живлення;
- Підключіть ПК до порту Ethernet;
- Конфігурацію слід виконувати за допомогою веб-браузера WebFig або інструменту конфігурації WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **існує декілька методів налаштування для забезпечення доступності;**
- Завантажте та відкрийте *"WinBox"* і виберіть вкладку *"Neighbors"*, щоб знайти пристрій;
- Натисніть на MAC-адресу. Ім’я користувача – *"admin"* і немає пароля (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Натисніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" у WebFig або WinBox та перезавантажте пристрій. Оновивши програмне забезпечення RouterOS до останньої версії, ви зможете забезпечити оптимальну продуктивність, стабільність і оновлення безпеки;
- У меню *"QuickSet"* встановіть режим *"PTP Bridge AP"* і виберіть свою країну, щоб застосувати налаштування регулювані у вашій країні;
- Встановіть рівень посилення антени залежно від використовуваної антени;
- У нижньому полі встановіть пароль маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Продукт поставляється без корпусу та призначений для встановлення в кінцеві продукти або корпуси користувачів навченим та кваліфікованим персоналом відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Перед початком монтажу уважно прочитайте інструкції з монтажу. Невикористання належного апаратного забезпечення та конфігурації або дотримання правильних процедур може призвести до небезпечної ситуації для людей і пошкодження системи.
- Тримайте цей пристрій подалі від води, вогню, вологи або гарячого середовища.
- Використовуйте ремінець заземлення під час розпакування та роботи з електричними компонентами, щоб уникнути пошкодження електричним розрядом (ESD). Після розпакування покладіть маршрутизатор на антистатичний килимок. Під час монтажу пристрою переконайтеся, що немає предметів, які можуть пошкодити або торкнутися пластини друкованої плати.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів та утилізуйте його безпечним способом, наприклад, у відведених місцях. Ознайомтесь із процедурами належного транспортування обладнання до визначених пунктів збору у вашому районі.
- Це продукт класу А. У побутових умовах цей виріб може викликати радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити відповідних заходів.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та використовувати на відстані не ближче 20 сантиметрів від вашого тіла, професійного користувача чи інших людей.

Виробник: "Мікротіклс СІА" Вулиця Уніяс 2, Рига, ЛВ-1039, Латвія;

Технічні характеристики бездротового мережевого зв’язку:

| **Частотний діапазон** | **Вихідна потужність (макс.)** |
| --- | --- |
| 5150-5250 МГц | 23 дБм |
| 5250-5350 МГц | 23 дБм |
| 5470-5725 МГц | 30 дБм |
| 5725-5850 МГц | 14 dBm |
| 5850-5895 МГц | 14 dBm |

Справжнім Mikrotikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Експлуатація цього радіообладнання у зазначеному складі та технічними характеристиками здійснюється за дозволом на експлуатацію (Рішення НКРЗІ No844 від 23.12.2014 р. зареєстровано у Міністерстві юстиції України 19.02.2015 р. за No 201/26646), з урахуванням змін до положення про порядок і форму ведення реєстру радіоелектронних засобів та випромінювальних пристроїв, що можуть застосовуватися на території України в смугах радіочастот загального користування, затвердженого рішенням НКРЗІ 03.04.2018 р. за No 188, зареєстрованого Міністерстві Юстиції України 07.06.2018 р. за No 688/32140. Надання виробником радіообладнання інформації для споживачів (користувачів) щодо наявності вимог отримання дозволу на експлуатацію згідно рішення НКРЗІ No77 від 13.02.2018 р., зареєстроване Міністерстві Юстиції України 12.03.2018р. за No 284/31736.

![](./img/5b0555ad40518a25f1ceeda790bc115c.badge.jpg)

## Federal Communication Commission Interference Statement

| Model | FCC ID |
| --- | --- |
| L11UG-5HaxD-US | TV7L11AX5 |

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.
![](./img/fcc_logo_ez.badge.jpg)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Antenna Installation WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in the USA (or where FCC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

Approved Antenna Table:

| Antenna Model | Type | Antenna gain, dBi |
| --- | --- | --- |
| UNII-1 (5150-5250 MHz) | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 28 |
| UNII-2A (5250-5350 MHz) | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |
| **UNII-2C (5470-5725MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |
| **UNII-3 (5725-5850MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |

The same type of antenna and lower antenna gain than those listed above in the table may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

## Innovation, Science and Economic Development Canada

| Model | IC |
| --- | --- |
| L11UG-5HaxD-US | 7442A-L11AX5 |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux

**Antenna Installation WARNING:** It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

Approved Antenna Table:

| Antenna Model | Type | Antenna gain, dBi |
| --- | --- | --- |
| UNII-2 (5250-5350 MHz) | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |
| **UNII-2 Extended (5470-5600MHz, 5650-5725 MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |
| **UNII-3 (5725-5850MHz)** | | |
| HGO-antenna-OUT | Omnidirectional | 7.1 |
| MTAS-5G-19D120 | Sector | 19 |
| MTAD-5G-30D3 | Dish | 30 |

The same type of antenna and lower antenna gain than those listed above in the table may also be used in accordance with certification.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

**Exposition aux rayonnements de radiofréquence:** Cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements de l'IC établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à moins de 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

## UKCA marking

![](./img/ukca_black_fill.badge.gif)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение L11UG-5HaxD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení L11UG-5HaxD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen L11UG-5HaxD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp L11UG-5HaxD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός L11UG-5HaxD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type L11UG-5HaxD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico L11UG-5HaxD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp L11UG-5HaxD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi L11UG-5HaxD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type L11UG-5HaxD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa L11UG-5HaxD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a L11UG-5HaxD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio L11UG-5HaxD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að L11UG-5HaxD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas L11UG-5HaxD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta L11UG-5HaxD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju L11UG-5HaxD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur L11UG-5HaxD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret L11UG-5HaxD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego L11UG-5HaxD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio L11UG-5HaxD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio L11UG-5HaxD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu L11UG-5HaxD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme L11UG-5HaxD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning L11UG-5HaxD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products) |

## WLAN

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      WLAN 5 GHz
      5150-5250 MHz /23 dBm
    
    WLAN 5 GHz5250-5350 MHz / 23 dBm
    WLAN 5 GHz5470-5725 MHz / 30 dBm
    WLAN 5 GHz5725-5850 MHz / 14 dBm
    WLAN 5 GHz5850-5895 MHz / 14 dBm
  

This MikroTik device meets Maximum TX power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistungsgrenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben in der Konformitätserklärung. Nähere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance TX maximale via les réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik soddisfa i limiti di potenza massima TX tramite le normative ETSI. Per informazioni più dettagliate consultare la Dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia TX a través de las normas ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует ограничениям максимальной мощности передачи согласно правилам ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](./img/tab.png)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) Degrees of protection provided by enclosure (IP Code)(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Current, A

DC Jack (12-28 VDC)PoE IN Ethernet (18-28 VDC)
24
1.2
-
-40°..+70°C

:::warning
Please, test your antenna with our device in the accreditation laboratory to be in compliance with EU rules.
:::

\#71867
