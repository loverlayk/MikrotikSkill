# Quick Guide G20 - 5GHz RouterBOARD series

> Models: RB911G-5HPnD, RB912UAG-5HPnD, RB922UAGS-5HPacD, RB911G-5HPacD, RB911-5HnD (911 Lite5 dual), RB911-5HacD (911 Lite5 ac), RB911-5Hn (911 Lite5)

**Models:** RB911G-5HPnD, RB912UAG-5HPnD, RB922UAGS-5HPacD, RB911G-5HPacD, RB911-5HnD (911 Lite5 dual), RB911-5HacD (911 Lite5 ac), RB911-5Hn (911 Lite5)

![MikroTik](./img/mt_logo_arrow_v2-02-57.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.10.2 or the latest stable version, to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik devices must be installed according to instructions.
:::

*This is a wireless network device. You can find the product model name on the label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-64.png)

Depending on the antenna used, you need to set its gain and set "*Installation*" to " *Indoor*" or "Outdoor", depending on the type of use. This is to ensure that the EIRP complies with the limit set by the local authorities. This is done in the Quickset menu.

**First Use:**

- This product comes without enclosure and is designed to be installed into the users' end products or enclosures. Compatible MikroTik enclosure for this product can be found at [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- The device comes in ESD protective packaging. When handling electrical equipment please observe the following safety precautions: Use a wrist grounding strap when unpacking and working with electrical components to avoid electrical discharge (ESD) damage;
- After unpacking please place the router on the anti-static mat;
- When mounting the unit make sure there are no objects that can damage or touch the PCB plate;
- The device can be mounted in your desired location using the factory-provided holes in a PCB plate, located on each side of the device;
- Before connecting the device to the power source, please attach the antennas to the connectors;
- Connect the device to the power source;
- Connect your PC to the Ethernet port;
- Configuration should be made using a web browser WebFig or the WinBox configuration tool [https://mt.lv/WinBox](https://mt.lv/WinBox); **multiple configuration methods are available to ensure accessibility;**
- Open [http://192.168.88.1](http://192.168.88.1) in a web browser to start setup. If the IP address is unavailable, use WinBox and connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "*QuickSet"* menu set up the *"PTP Bridge AP"* mode and choose your country, to apply country regulation settings;
- Set the antenna gain, depending on the antenna used;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- The product comes without enclosure and is meant to be installed into the enclosure by trained and qualified personnel. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes.
- Do not attempt to disassemble, repair, or modify the device. If service is needed, please contact MikroTik support.
- This product can be used both indoors and outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow correct procedures could result in hazardous situation to people and damage to the system. To install outdoors make sure to use at least IP54 rating enclosure.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- The socket-outlet shall be installed near the equipment and shall be easily accessible.
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures
- To avoid contamination of the environment, separate the device from household waste and dispose of it in a safe manner, for example, in designated areas. Become familiar with procedures for properly transporting the equipment to designated collection points in your area.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 330 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.10.2 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички устройства на MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

*Това е безжично мрежово устройство. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)

![](./img/image2020-2-4_17-15-57.badge-62.png)

В зависимост от използваната антена, трябва да настроите нейното усилване и „*Installation*“ на „*Indoor*“ или „*Outdoor*“, в зависимост от типа на използване. Това е, за да се гарантира, че EIRP отговаря на ограничението, определено от местните власти. Това се прави в менюто Quickset.

**Първа употреба:**

- Този продукт се предлага без корпус и е предназначен за инсталиране в крайни продукти или кутии на потребителите. Съвместим корпус MikroTik за този продукт можете да намерите на [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Устройството се доставя в ESD защитна опаковка. Когато работите с електрическо оборудване, спазвайте следните предпазни мерки:Използвайте заземяваща лента за китката, когато разопаковате и работите с електрически компоненти, за да избегнете повреда от електрически разряд (ESD);
- След като разопаковате, поставете рутера върху антистатичната подложка;
- Когато монтирате устройството, уверете се, че няма предмети, които могат да повредят или докоснат плочата на печатната платка;
- Устройството може да се монтира на желаното от вас място с помощта на фабрично осигурените отвори в печатна платка, разположени от всяка страна на устройството;
- Преди да свържете устройството към източника на захранване, моля, прикрепете антените към конекторите;
- Свържете устройството към източника на захранване;
- Свържете вашия компютър към Ethernet порта;
- Конфигурацията трябва да се извършва с помощта на уеб браузър WebFig или инструмента за конфигурация WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Отворете [http://192.168.88.1](http://192.168.88.1) в уеб браузъра, за да започнете настройката. Ако IP адресът не е достъпен, използвайте WinBox и се свържете чрез MAC адреса. Потребителското име е "admin", а парола няма (или за някои модели проверете потребителските и безжични пароли на стикера);
- Кликнете на бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- В менюто *"QuickSet"* настройте режима *"PTP Bridge AP"* и изберете вашата държава, за да приложите настройките за регулиране на страната;
- Задайте усилването на антената в зависимост от използваната антена;
- Задайте паролата на вашия рутер в долното поле.

**Информация за безопасност:**

- Преди да работите с каквото и да е оборудване MikroTik, имайте предвид опасностите, свързани с електрическите вериги, и се запознайте със стандартните практики за предотвратяване на инциденти. Инсталаторът трябва да е запознат с мрежовите структури, термини и концепции.
- Продуктът се доставя без корпус и е предназначен за инсталиране в корпуса от обучен и квалифициран персонал. Инсталаторът е отговорен да се увери, че инсталацията на оборудването е в съответствие с местните и националните електрически кодекси. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Използвайте само захранване и аксесоари, одобрени от производителя и които могат да бъдат намерени в оригиналната опаковка на този продукт.
- Това оборудване трябва да бъде инсталирано от обучен и квалифициран персонал, съгласно тези инструкции за монтаж. Инсталаторът е отговорен да се увери, че инсталирането на оборудването е в съответствие с местните и националните електрически кодекси.
- Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството. Ако е необходимо обслужване, моля, свържете се с поддръжката на MikroTik.
- Този продукт може да се използва както на закрито, така и на открито. Моля, прочетете внимателно инструкциите за монтаж, преди да започнете монтажа. Неизползването на правилния хардуер и конфигурация или неизпълнението на правилните процедури може да доведе до опасна ситуация за хората и повреда на системата. За да инсталирате на открито, уверете се, че използвате корпус с класификация най-малко IP54.
- Не можем да гарантираме, че няма да възникнат инциденти или щети поради неправилна употреба на устройството. Моля, използвайте този продукт внимателно и работете на свой собствен риск!
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е като изключите захранващия адаптер от контакта.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, в който случай може да се наложи потребителят да вземе адекватни мерки.
- За да избегнете замърсяване на околната среда, отделете устройството от битовите отпадъци и го изхвърлете по безопасен начин, например в обособени за това места. Запознайте се с процедурите за правилно транспортиране на оборудването до определени пунктове за събиране във вашия район.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация FCC, IC и Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 330 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.
## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.10.2 nebo na nejnovější stabilní verzi!
Je na koncových uživatelích, aby dodržovali místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna zařízení MikroTik musí být nainstalována podle pokynů.
:::

*Toto je bezdrátové síťové zařízení*. *Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-62.png)

V závislosti na použité anténě musíte nastavit její zisk a „*Installation*“ na „*Indoor*“ nebo „*Outdoor*“, v závislosti na typu použití. To má zajistit, že EIRP splňuje limit stanovený místními úřady. To se provádí v nabídce Quickset.

**První použití:**

- Tento produkt je dodáván bez krytu a je navržen pro instalaci do koncových produktů nebo krytů uživatelů. Kompatibilní kryt MikroTik pro tento produkt naleznete na [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Zařízení je dodáváno v ESD ochranném obalu. Při manipulaci s elektrickým zařízením dodržujte následující bezpečnostní opatření:Při vybalování a práci s elektrickými součástmi používejte uzemňovací pásek na zápěstí, aby nedošlo k poškození elektrickým výbojem (ESD);
- Po vybalení položte router na antistatickou podložku;
- Při montáži jednotky se ujistěte, že na desce nejsou žádné předměty, které by mohly poškodit nebo se dotýkat desky plošných spojů;
- Zařízení lze namontovat na požadované místo pomocí továrně dodávaných otvorů v desce plošných spojů, které se nacházejí na každé straně zařízení;
- Před připojením zařízení ke zdroji napájení připojte antény ke konektorům;
- Připojte zařízení ke zdroji napájení;
- Připojte svůj počítač k portu Ethernet;
- Konfigurace by měla být provedena pomocí webového prohlížeče WebFig nebo nástroje pro konfiguraci WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Otevřete [http://192.168.88.1](http://192.168.88.1) v webovém prohlížeči pro spuštění nastavení. Pokud není k dispozici IP adresa, použijte WinBox a připojte se pomocí MAC adresy. Uživatelské jméno je "admin" a heslo není (nebo pro některé modely zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Klepněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stáhnuté balíčky do menu "Files" ve WinBoxu a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce *"QuickSet"* nastavte režim *"PTP Bridge AP"* a vyberte svou zemi pro použití nastavení regulace země;
- Nastavte zisk antény v závislosti na použité anténě;
- Ve spodním poli nastavte heslo routeru.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si nebezpečí spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalační technik by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Výrobek je dodáván bez krytu a je určen k instalaci do krytu vyškoleným a kvalifikovaným personálem. Instalační technik je odpovědný za ujištění, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat nebo upravovat.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které naleznete v originálním balení tohoto výrobku.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle tohoto návodu k instalaci. Instalační technik je odpovědný za to, že instalace zařízení odpovídá místním a národním elektrickým předpisům.
- Nepokoušejte se zařízení rozebírat, opravovat nebo upravovat. Pokud je potřeba servis, kontaktujte podporu MikroTik.
- Tento produkt lze použít jak uvnitř, tak venku. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nebudete používat správný hardware a konfiguraci nebo nebudete dodržovat správné postupy, může dojít k nebezpečné situaci pro lidi a poškození systému. Při venkovní instalaci se ujistěte, že používáte krytí alespoň IP54.
- Nemůžeme zaručit, že nedojde k žádné nehodě nebo poškození v důsledku nesprávného použití zařízení. Používejte tento produkt opatrně a provozujte jej na vlastní nebezpečí!
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejší způsob, jak toho dosáhnout, je odpojit napájecí adaptér ze zásuvky.
- Jedná se o produkt třídy A. V domácím prostředí může tento produkt způsobovat rádiové rušení, v takovém případě může být uživatel požádán, aby přijal odpovídající opatření.
- Abyste zabránili kontaminaci životního prostředí, oddělte zařízení od domácího odpadu a zlikvidujte jej bezpečným způsobem, například na vyhrazených místech. Seznamte se s postupy správné přepravy zařízení do určených sběrných míst ve vaší oblasti.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření FCC, IC a Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 330 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.10.2 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-enheder skal installeres i henhold til instruktionerne.
:::

*Dette er en trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*Tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-62.png)

Afhængigt af den anvendte antenne skal du indstille dens forstærkning og '*Installation*' til '*Indoor*' eller '*Outdoor*', afhængigt af brugstypen. Dette er for at sikre, at EIRP overholder grænsen fastsat af de lokale myndigheder. Dette gøres i Quickset-menuen.

**Første brug:**

- Dette produkt leveres uden indkapsling og er designet til at blive installeret i brugernes slutprodukter eller kabinetter. Kompatibel MikroTik-kabinet til dette produkt kan findes på [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Enheden leveres i ESD-beskyttende emballage. Ved håndtering af elektrisk udstyr skal du overholde følgende sikkerhedsforanstaltninger:Brug en håndledsjordstrop, når du pakker ud og arbejder med elektriske komponenter for at undgå skader på elektrisk udladning (ESD);
- Efter udpakning skal du placere routeren på den antistatiske måtte;
- Når du monterer enheden, skal du sørge for, at der ikke er genstande, der kan beskadige eller røre ved printpladen;
- Enheden kan monteres på det ønskede sted ved hjælp af de fabriksleverede huller i en PCB-plade, placeret på hver side af enheden;
- Før du tilslutter enheden til strømkilden, skal du tilslutte antennerne til stikkene;
- Tilslut enheden til strømkilden;
- Tilslut din pc til Ethernet-porten;
- Konfigurationen skal foretages ved hjælp af webbrowseren WebFig eller konfigurationsværktøjet WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Åbn [http://192.168.88.1](http://192.168.88.1) i en webbrowser for at starte opsætningen. Hvis IP-adressen ikke er tilgængelig, skal du bruge WinBox og forbinde ved hjælp af MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Overfør de downloadede pakker til WinBox "Files" menuen og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil *"PTP Bridge AP"-* tilstanden i *"QuickSet"-* menuen og vælg dit land for at anvende landereguleringsindstillinger;
- Indstil antenneforstærkningen afhængigt af den anvendte antenne;
- Indstil din router-adgangskode i det nederste felt.

**Sikkerhedsoplysninger:**

- Før du arbejder på MikroTik-udstyr, skal du være opmærksom på de farer, der er forbundet med elektriske kredsløb, og være bekendt med standardpraksis for forebyggelse af ulykker. Installatøren skal være fortrolig med netværksstrukturer, termer og koncepter.
- Produktet leveres uden kabinet og er beregnet til at blive installeret i kabinettet af uddannet og kvalificeret personale. Installatøren er ansvarlig for at sikre, at installationen af udstyret er i overensstemmelse med lokale og nationale elektriske regler. Forsøg ikke at adskille, reparere eller ændre enheden.
- Brug kun den strømforsyning og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af udstyret er i overensstemmelse med lokale og nationale elektriske regler.
- Forsøg ikke at adskille, reparere eller ændre enheden. Hvis der er brug for service, skal du kontakte MikroTiks support.
- Dette produkt kan bruges både indendørs og udendørs. Læs monteringsvejledningen omhyggeligt, før du begynder installationen. Hvis du ikke bruger den korrekte hardware og konfiguration eller ikke følger de korrekte procedurer, kan det resultere i farlige situationer for mennesker og skader på systemet. Hvis du vil installere udendørs, skal du sørge for at bruge et kabinet med mindst IP54-klassificering.
- Vi kan ikke garantere, at der ikke sker ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med forsigtighed og på eget ansvar!
- Stikkontakten skal være installeret i nærheden af udstyret og skal være let tilgængelig.
- I tilfælde af fejl på enheden skal den kobles fra strømmen. Den hurtigste måde at gøre det på er ved at trække strømadapteren ud af stikkontakten.
- Dette er et klasse A-produkt. I et boligmiljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger.
- For at undgå forurening af miljøet skal du adskille enheden fra husholdningsaffald og bortskaffe den på en sikker måde, f.eks. i dertil indrettede områder. Bliv fortrolig med procedurerne for korrekt transport af udstyret til udpegede indsamlingssteder i dit område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder FCC, IC og EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 330 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.10.2 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Geräte müssen gemäß den Anweisungen installiert werden.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-62.png)

Je nach verwendeter Antenne müssen Sie deren Gewinn und die '*Installation*' je nach Nutzungsart auf '*Indoors*' oder '*Outdoors*' einstellen. Dadurch soll sichergestellt werden, dass die EIRP den von den lokalen Behörden festgelegten Grenzwert einhält. Dies geschieht im Quickset-Menü.

**Erste Benutzung:**

- Dieses Produkt wird ohne Gehäuse geliefert und ist für den Einbau in die Endprodukte oder Gehäuse des Benutzers konzipiert. Kompatible MikroTik-Gehäuse für dieses Produkt finden Sie unter [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Das Gerät wird in einer ESD-Schutzverpackung geliefert. Beachten Sie beim Umgang mit elektrischen Geräten bitte die folgenden Sicherheitsvorkehrungen:Verwenden Sie beim Auspacken und Arbeiten mit elektrischen Komponenten ein Erdungsarmband, um Schäden durch elektrische Entladung (ESD) zu vermeiden.
- Bitte legen Sie den Router nach dem Auspacken auf die Antistatikmatte;
- Stellen Sie bei der Montage des Geräts sicher, dass keine Gegenstände vorhanden sind, die die Platine beschädigen oder berühren können.
- Das Gerät kann mithilfe der werkseitig vorgesehenen Löcher in einer Leiterplatte, die sich auf jeder Seite des Geräts befindet, an der gewünschten Stelle montiert werden.
- Bevor Sie das Gerät an die Stromquelle anschließen, befestigen Sie bitte die Antennen an den Anschlüssen;
- Schließen Sie das Gerät an die Stromquelle an;
- Verbinden Sie Ihren PC mit dem Ethernet-Port;
- Die Konfiguration sollte mit dem Webbrowser WebFig oder dem WinBox-Konfigurationstool [https://mt.lv/WinBox](https://mt.lv/WinBox) durchgeführt werden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Öffnen Sie [http://192.168.88.1](http://192.168.88.1) in einem Webbrowser, um die Einrichtung zu starten. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie WinBox und stellen Sie eine Verbindung über die MAC-Adresse her. Der Benutzername ist "admin", und es gibt kein Passwort (oder für einige Modelle überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das Menü "Files" von WinBox hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Richten Sie im Menü *"QuickSet"* den *"PTP Bridge AP"*-Modus ein und wählen Sie Ihr Land aus, um die Länderregulierungseinstellungen anzuwenden;
- Stellen Sie den Antennengewinn je nach verwendeter Antenne ein;
- Richten Sie im unteren Feld Ihr Router-Passwort ein.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, machen Sie sich über die Gefahren bewusst, die mit elektrischen Schaltkreisen verbunden sind, und machen Sie sich mit den Standardverfahren zur Unfallverhütung vertraut. Der Installateur sollte mit Netzwerkstrukturen, -begriffen und -konzepten vertraut sein.
- Das Produkt wird ohne Gehäuse geliefert und soll von geschultem und qualifiziertem Personal in das Gehäuse eingebaut werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Elektrovorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das sich in der Originalverpackung dieses Produkts befindet.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich, sicherzustellen, dass die Installation des Geräts den örtlichen und nationalen Elektrovorschriften entspricht.
- Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren. Wenn ein Service erforderlich ist, wenden Sie sich bitte an den MikroTik-Support.
- Dieses Produkt kann sowohl drinnen als auch draußen verwendet werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn nicht die richtige Hardware und Konfiguration verwendet oder die richtigen Verfahren nicht befolgt werden, kann dies zu gefährlichen Situationen für Personen und Schäden am System führen. Stellen Sie bei der Installation im Freien sicher, dass Sie ein Gehäuse mit mindestens der Schutzart IP54 verwenden.
- Wir können nicht garantieren, dass es bei unsachgemäßer Verwendung des Geräts nicht zu Unfällen oder Schäden kommt. Bitte verwenden Sie dieses Produkt mit Vorsicht und betreiben Sie es auf eigenes Risiko!
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.
- Im Falle eines Geräteausfalls trennen Sie das Gerät bitte vom Stromnetz. Am schnellsten geht das, indem Sie das Netzteil aus der Steckdose ziehen.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise geeignete Maßnahmen ergreifen.
- Um eine Kontamination der Umwelt zu vermeiden, trennen Sie das Gerät vom Hausmüll und entsorgen Sie es auf sichere Weise, z. B. in den dafür vorgesehenen Bereichen. Machen Sie sich mit den Verfahren für den ordnungsgemäßen Transport der Ausrüstung zu ausgewiesenen Sammelstellen in Ihrer Nähe vertraut.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den FCC-, IC- und EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 330 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.10.2 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
:::

*Αυτή είναι μια συσκευή ασύρματου δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια σχετικά με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-62.png)

Ανάλογα με την κεραία που χρησιμοποιείται, πρέπει να ρυθμίσετε την απολαβή της και την '*Installation*' σε '*Indoor*' ή '*Outdoor*', ανάλογα με τον τύπο χρήσης. Αυτό γίνεται για να διασφαλιστεί ότι το EIRP πληροί το όριο που έχουν θέσει οι τοπικές αρχές. Αυτό γίνεται στο μενού Quickset.

**Πρώτη χρήση:**

- Αυτό το προϊόν διατίθεται χωρίς περίβλημα και έχει σχεδιαστεί για εγκατάσταση στα τελικά προϊόντα ή στα περιβλήματα των χρηστών. Το συμβατό περίβλημα MikroTik για αυτό το προϊόν βρίσκεται στη διεύθυνση [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Η συσκευή διατίθεται σε προστατευτική συσκευασία ESD. Όταν χειρίζεστε ηλεκτρικό εξοπλισμό, τηρείτε τις ακόλουθες προφυλάξεις ασφαλείας:Χρησιμοποιήστε έναν ιμάντα γείωσης καρπού όταν αποσυσκευάζετε και εργάζεστε με ηλεκτρικά εξαρτήματα για να αποφύγετε ζημιά από ηλεκτρική εκφόρτιση (ESD);
- Μετά την αποσυσκευασία, τοποθετήστε το δρομολογητή στο αντιστατικό στρώμα;
- Κατά την τοποθέτηση της μονάδας βεβαιωθείτε ότι δεν υπάρχουν αντικείμενα που μπορούν να προκαλέσουν ζημιά ή να αγγίξουν την πλάκα PCB;
- Η συσκευή μπορεί να τοποθετηθεί στην επιθυμητή θέση χρησιμοποιώντας τις οπές που παρέχονται από το εργοστάσιο σε μια πλάκα PCB, που βρίσκεται σε κάθε πλευρά της συσκευής;
- Πριν συνδέσετε τη συσκευή στην πηγή ρεύματος, συνδέστε τις κεραίες στις υποδοχές.
- Συνδέστε τη συσκευή στην πηγή ρεύματος.
- Συνδέστε τον υπολογιστή σας στη θύρα Ethernet.
- Η ρύθμιση πρέπει να γίνει χρησιμοποιώντας τον περιηγητή WebFig ή το εργαλείο ρύθμισης WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ανοίξτε το [http://192.168.88.1](http://192.168.88.1) σε έναν περιηγητή για να ξεκινήσετε τη ρύθμιση. Εάν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το WinBox και συνδεθείτε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τα χρήστη και τα ασύρματα κωδικούς πρόσβασης στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Ανεβάστε τα κατεβασμένα πακέτα στο μενού "Files" του WinBox και επανεκκινήστε τη συσκευή;
- Με την αναβάθμιση του λογισμικού RouterOS στην τελευταία έκδοση, μπορείτε να διασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Στο μενού *"QuickSet"* ρυθμίστε τη λειτουργία *"PTP Bridge AP"* και επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις ρύθμισης χώρας.
- Ρυθμίστε το κέρδος κεραίας, ανάλογα με την κεραία που χρησιμοποιείται.
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο.

**Πληροφορίες ασφάλειας:**

- Πριν εργαστείτε σε οποιονδήποτε εξοπλισμό MikroTik, να γνωρίζετε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και να εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης θα πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Το προϊόν διατίθεται χωρίς περίβλημα και προορίζεται για εγκατάσταση στο περίβλημα από εκπαιδευμένο και εξειδικευμένο προσωπικό. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση ότι η εγκατάσταση του εξοπλισμού είναι συμβατή με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Χρησιμοποιείτε μόνο το τροφοδοτικό και τα αξεσουάρ που είναι εγκεκριμένα από τον κατασκευαστή και τα οποία βρίσκονται στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος να διασφαλίσει ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες.
- Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή. Εάν απαιτείται σέρβις, επικοινωνήστε με την υποστήριξη της MikroTik.
- Αυτό το προϊόν μπορεί να χρησιμοποιηθεί τόσο σε εσωτερικούς όσο και σε εξωτερικούς χώρους. Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η μη χρήση του σωστού υλικού και της σωστής διαμόρφωσης ή η μη τήρηση των σωστών διαδικασιών θα μπορούσε να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και ζημιά στο σύστημα. Για εγκατάσταση σε εξωτερικό χώρο, βεβαιωθείτε ότι χρησιμοποιείτε τουλάχιστον περίβλημα αξιολόγησης IP54.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από το ρεύμα. Ο πιο γρήγορος τρόπος για να το κάνετε αυτό είναι αποσυνδέοντας το τροφοδοτικό από την πρίζα.
- Αυτό είναι προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν μπορεί να προκαλέσει ραδιοπαρεμβολές, οπότε ο χρήστης μπορεί να χρειαστεί να λάβει τα κατάλληλα μέτρα.
- Για να αποφύγετε τη μόλυνση του περιβάλλοντος, διαχωρίστε τη συσκευή από τα οικιακά απορρίμματα και απορρίψτε την με ασφαλή τρόπο, για παράδειγμα, σε καθορισμένες περιοχές. Εξοικειωθείτε με τις διαδικασίες για τη σωστή μεταφορά του εξοπλισμού σε καθορισμένα σημεία συλλογής στην περιοχή σας.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας FCC, IC και Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 330 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.10.2 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos MikroTik deben instalarse de acuerdo con las instrucciones.
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-63.png)

Dependiendo de la antena utilizada, debe configurar su ganancia y la '*Installation*' en '*Indoor*' o '*Outdoor*', según el tipo de uso. Esto es para garantizar que EIRP cumpla con el límite establecido por las autoridades locales. Esto se hace en el menú Quickset.

**Primer uso:**

- Este producto viene sin gabinete y está diseñado para instalarse en los productos finales o gabinetes de los usuarios. La carcasa MikroTik compatible para este producto se puede encontrar en [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- El dispositivo se entrega en un embalaje protector ESD. Al manipular equipos eléctricos, observe las siguientes precauciones de seguridad:Utilice una muñequera con conexión a tierra al desembalar y trabajar con componentes eléctricos para evitar daños por descarga eléctrica (ESD);
- Después de desembalar, coloque el enrutador sobre la alfombra antiestática;
- Al montar la unidad asegúrese de que no haya objetos que puedan dañar o tocar la placa PCB;
- El dispositivo se puede montar en la ubicación deseada utilizando los orificios provistos de fábrica en una placa PCB, ubicada a cada lado del dispositivo;
- Antes de conectar el dispositivo a la fuente de alimentación, conecte las antenas a los conectores;
- Conecte el dispositivo a la fuente de alimentación;
- Conecte su PC al puerto Ethernet;
- La configuración debe realizarse con el navegador web WebFig o la herramienta de configuración WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Abra [http://192.168.88.1](http://192.168.88.1) en un navegador web para iniciar la configuración. Si la dirección IP no está disponible, utilice WinBox y conéctese utilizando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifique los usuarios y contraseñas inalámbricas en la pegatina);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú "Files" de WinBox y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- En el menú *"QuickSet"* configure el modo *"PTP Bridge AP"* y elija su país, para aplicar la configuración de la regulación del país;
- Establezca la ganancia de la antena, según la antena utilizada;
- Configure la contraseña de su enrutador en el campo inferior.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los peligros que implican los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras, términos y conceptos de la red.
- El producto viene sin gabinete y debe ser instalado en el gabinete por personal capacitado y calificado. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar ni modificar el dispositivo.
- Utilice únicamente la fuente de alimentación y los accesorios aprobados por el fabricante y que se encuentran en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales.
- No intente desmontar, reparar ni modificar el dispositivo. Si necesita servicio, comuníquese con el soporte de MikroTik.
- Este producto se puede utilizar tanto en interior como en exterior. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. No utilizar el hardware y la configuración correctos o no seguir los procedimientos correctos podría provocar situaciones peligrosas para las personas y daños al sistema. Para instalar en exteriores, asegúrese de utilizar al menos una carcasa con clasificación IP54.
- No podemos garantizar que no se produzcan accidentes o daños debido al uso inadecuado del dispositivo. Utilice este producto con cuidado y utilícelo bajo su propia responsabilidad.
- La toma de corriente se instalará cerca del equipo y será de fácil acceso.
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de corriente de la toma de corriente.
- Este es un producto Clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso es posible que se requiera que el usuario tome las medidas adecuadas.
- Para evitar la contaminación del medio ambiente, separe el dispositivo de los residuos domésticos y deséchelo de forma segura, por ejemplo, en áreas designadas. Familiarícese con los procedimientos para transportar adecuadamente el equipo a los puntos de recolección designados en su área.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la FCC, IC y la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 330 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

Rango de frecuencia: 5725-5850 MHz. Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.10.2 või uusimale stabiilsele versioonile!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTik seadmed tuleb installida vastavalt juhistele.
:::

*See on traadita võrgu seade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*Kui vajate konfigureerimisel abi, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-62.png)

Olenevalt kasutatavast antennist peate määrama selle võimenduse ja '*Installation*' väärtuseks '*Indoors*' või '*Outdoors*', olenevalt kasutustüübist. Selle eesmärk on tagada, et EIRP järgiks kohalike võimude kehtestatud piirmäära. Seda tehakse menüüs Quickset.

**Esimene kasutamine:**

- See toode on ilma korpuseta ja on mõeldud paigaldamiseks kasutaja lõpptoodetesse või korpustesse. Selle toote jaoks ühilduva MikroTiku korpuse leiate aadressilt [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Seade on ESD kaitsepakendis. Elektriseadmete käsitsemisel järgige järgmisi ettevaatusabinõusid:Elektrilahenduste (ESD) kahjustuste vältimiseks kasutage lahtipakkimisel ja elektriliste komponentidega töötamisel randme maandusrihma;
- Pärast lahtipakkimist asetage ruuter antistaatilisele matile;
- Seadme paigaldamisel veenduge, et seal pole esemeid, mis võivad PCB plaati kahjustada või puudutada;
- Seadme saab paigaldada soovitud kohta, kasutades tehases ette nähtud auke PCB plaadil, mis asuvad seadme mõlemal küljel;
- Enne seadme ühendamist toiteallikaga ühendage antennid pistikutesse;
- Ühendage seade toiteallikaga;
- Ühendage arvuti Etherneti porti;
- Konfigureerimine tuleb teha veebibrauseri WebFig või WinBox konfigureerimisriista [https://mt.lv/WinBox](https://mt.lv/WinBox) abil; **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Avage [http://192.168.88.1](http://192.168.88.1) veebibrauseris, et alustada seadistamist. Kui IP-aadress pole saadaval, kasutage WinBoxi ja ühendage MAC-aadressi kasutades. Kasutajanimi on "admin" ja parooli pole (või mõne mudeli puhul kontrollige kasutaja ja traadita paroole kleepsul);
- Klõpsake nupul "Check for updates" ja ajakohastage RouterOS viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige alla laaditud paketid WinBoxi "Files" menüüsse ja taaskäivitage seade;
- Värskendades oma RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadistage menüüs *"QuickSet"* *režiim* *"PTP Bridge AP"* ja valige riigi reguleerimise sätete rakendamiseks oma riik;
- Määrake antenni võimendus sõltuvalt kasutatavast antennist;
- Seadistage alumisel väljal ruuteri parool.

**Ohutusteave:**

- Enne MikroTiku seadme kallal töötamist olge teadlik elektriskeemiga kaasnevatest ohtudest ja olge kursis õnnetuste vältimise standardsete tavadega. Paigaldaja peaks olema tuttav võrgustruktuuride, terminite ja mõistetega.
- Toode tarnitakse ilma korpuseta ja selle paigaldavad korpusesse koolitatud ja kvalifitseeritud töötajad. Paigaldaja vastutab selle eest, et seadmete paigaldamine vastaks kohalikele ja riiklikele elektrieeskirjadele. Ärge püüdke seadet lahti võtta, parandada ega muuta.
- Kasutage ainult tootja poolt heakskiidetud toiteallikat ja tarvikuid, mis leiate selle toote originaalpakendist.
- Selle seadme peavad paigaldama koolitatud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmete paigaldamine vastaks kohalikele ja riiklikele elektrieeskirjadele.
- Ärge püüdke seadet lahti võtta, parandada ega muuta. Kui vajate hooldust, võtke ühendust MikroTiku klienditoega.
- Seda toodet saab kasutada nii sise- kui ka välistingimustes. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhiseid. Õige riistvara ja konfiguratsiooni mittekasutamine või õigete protseduuride järgimata jätmine võib põhjustada ohtlikke olukordi inimestele ja kahjustada süsteemi. Välistingimustes paigaldamisel kasutage kindlasti vähemalt IP54 kaitset.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja omal vastutusel!
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.
- Seadme rikke korral ühendage see vooluvõrgust lahti. Kiireim viis seda teha on toiteadapteri pistikupesast eemaldamine.
- See on A-klassi toode. Kodukeskkonnas võib see toode põhjustada raadiohäireid, mille puhul kasutajalt võidakse nõuda piisavate meetmete võtmist.
- Keskkonna saastumise vältimiseks eraldage seade olmeprügist ja visake see ohutul viisil, näiteks selleks ettenähtud kohtadesse. Tutvuge seadmete õige transportimise protseduuridega teie piirkonnas määratud kogumispunktidesse.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab FCC, IC ja Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 330 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.10.2 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-laitteet on asennettava ohjeiden mukaan.
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*Jos tarvitset ohjeita konfiguroinnissa, kysy neuvoa- antajalta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-62.png)

Käytetystä antennista riippuen sen vahvistukseksi ja '*Installation*' on asetettava '*Indoors*' tai 'O *utdoors*' käyttötyypistä riippuen. Tällä varmistetaan, että EIRP täyttää paikallisten viranomaisten asettaman rajan. Tämä tehdään Quickset-valikossa.

**Ensimmäinen käyttö:**

- Tämä tuote toimitetaan ilman koteloa ja se on suunniteltu asennettavaksi käyttäjien lopputuotteisiin tai koteloihin. Tälle tuotteelle yhteensopiva MikroTik-kotelo löytyy osoitteesta [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Laite toimitetaan ESD-suojapakkauksessa. Noudata sähkölaitteita käsitellessäsi seuraavia turvaohjeita:Käytä maadoitusrannehihnaa, kun purat pakkauksesta ja työskentelet sähkökomponenttien kanssa välttääksesi sähköpurkausvauriot (ESD);
- Aseta reititin pakkauksesta purkamisen jälkeen antistaattiselle matolle.
- Kun asennat yksikköä, varmista, että siinä ei ole esineitä, jotka voivat vahingoittaa tai koskettaa piirilevyä;
- Laite voidaan asentaa haluamaasi paikkaan käyttämällä tehtaalla toimitettuja reikiä piirilevyssä, jotka sijaitsevat laitteen molemmilla puolilla;
- Ennen kuin liität laitteen virtalähteeseen, kiinnitä antennit liittimiin;
- Liitä laite virtalähteeseen;
- Liitä tietokoneesi Ethernet-porttiin;
- Kokoonpano tulee tehdä käyttäen verkkoselainta WebFig tai konfiguraatiotyökalua WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Avaa [http://192.168.88.1](http://192.168.88.1) verkkoselaimessa aloittaaksesi asennuksen. Jos IP-osoite ei ole käytettävissä, käytä WinBoxia ja yhdistä MAC-osoitetta käyttäen. Käyttäjätunnus on "admin", eikä salasanaa ole (tai joillakin malleilla tarkista käyttäjä- ja langattomat salasanat tarrasta);
- Napsauta "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WinBoxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- Aseta *"QuickSet"-* valikossa *"PTP Bridge AP"-* tila ja valitse maasi, jotta maakohtaiset asetukset otetaan käyttöön;
- Aseta antennin vahvistus käytetyn antennin mukaan;
- Aseta reitittimen salasana alakenttään.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden parissa, ole tietoinen sähköpiirien vaaroista ja tunne tavallisia käytäntöjä onnettomuuksien ehkäisemiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Tuote toimitetaan ilman koteloa, ja koulutetun ja pätevän henkilöstön on tarkoitus asentaa koteloon. Asentaja on vastuussa siitä, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka ovat tämän tuotteen alkuperäisessä pakkauksessa.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentaja on vastuussa siitä, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen.
- Älä yritä purkaa, korjata tai muokata laitetta. Jos tarvitset huoltoa, ota yhteyttä MikroTikin tukeen.
- Tätä tuotetta voidaan käyttää sekä sisällä että ulkona. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikean laitteiston ja kokoonpanon käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi johtaa ihmisille vaarallisiin tilanteisiin ja järjestelmän vaurioitumiseen. Ulkoasennuksessa varmista, että käytät vähintään IP54-suojausta.
- Emme voi taata, että laitteen väärästä käytöstä johtuen ei tapahdu onnettomuuksia tai vahinkoja. Käytä tätä tuotetta varoen ja omalla vastuullasi!
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.
- Jos laite epäonnistuu, irrota se virtalähteestä. Nopein tapa tehdä se on irrottaa virtalähde pistorasiasta.
- Tämä on A-luokan tuote. Kotiympäristössä tämä tuote saattaa aiheuttaa radiohäiriöitä, jolloin käyttäjän on ehkä ryhdyttävä asianmukaisiin toimenpiteisiin.
- Ympäristön saastumisen välttämiseksi erota laite kotitalousjätteestä ja hävitä se turvallisella tavalla, esimerkiksi niille osoitetuille alueille. Tutustu menettelyihin, joilla laitteet kuljetetaan asianmukaisesti alueellasi oleviin keräyspisteisiin.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on FCC: n, IC: n ja Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 330 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.10.2 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils MikroTik doivent être installés conformément aux instructions.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-62.png)

Selon l'antenne utilisée, vous devez régler son gain et l''*Installation*' sur '*Indoor*' ou '*Outdoor*', selon le type d'utilisation. Il s'agit de s'assurer que l'EIRP respecte la limite fixée par les autorités locales. Cela se fait dans le menu Quickset.

**Première utilisation:**

- Ce produit est livré sans boîtier et est conçu pour être installé dans les produits finaux ou les boîtiers des utilisateurs. Le boîtier MikroTik compatible pour ce produit peut être trouvé sur [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- L'appareil est livré dans un emballage de protection ESD. Lors de la manipulation d'équipements électriques, veuillez respecter les précautions de sécurité suivantes:Utilisez un bracelet de mise à la terre lors du déballage et du travail avec des composants électriques pour éviter les dommages causés par les décharges électriques (ESD);
- Après le déballage, veuillez placer le routeur sur le tapis antistatique;
- Lors du montage de l'unité, assurez-vous qu'aucun objet ne puisse endommager ou toucher la plaque PCB;
- L'appareil peut être monté à l'emplacement souhaité à l'aide des trous prévus en usine dans une plaque PCB, située de chaque côté de l'appareil;
- Avant de connecter l'appareil à la source d'alimentation, veuillez fixer les antennes aux connecteurs;
- Connectez l'appareil à la source d'alimentation;
- Connectez votre PC au port Ethernet;
- La configuration doit être effectuée à l'aide du navigateur WebFig ou de l'outil de configuration WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Ouvrez [http://192.168.88.1](http://192.168.88.1) dans un navigateur web pour commencer la configuration. Si l'adresse IP n'est pas disponible, utilisez WinBox et connectez-vous en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, la stabilité et les mises à jour de sécurité;
- Dans le menu *"QuickSet"*, configurez le mode *"PTP Bridge AP"* et choisissez votre pays pour appliquer les paramètres de réglementation du pays;
- Réglez le gain de l'antenne en fonction de l'antenne utilisée;
- Configurez le mot de passe de votre routeur dans le champ inférieur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. L'installateur doit être familier avec les structures, les termes et les concepts du réseau.
- Le produit est livré sans boîtier et est destiné à être installé dans le boîtier par un personnel formé et qualifié. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, de réparer ou de modifier l'appareil.
- Utilisez uniquement l'alimentation électrique et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux.
- N'essayez pas de démonter, de réparer ou de modifier l'appareil. Si un service est nécessaire, veuillez contacter le support MikroTik.
- Ce produit peut être utilisé aussi bien à l'intérieur qu'à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration appropriés ou de suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système. Pour une installation à l'extérieur, assurez-vous d'utiliser au moins un boîtier classé IP54.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne surviendra en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec précaution et à vos propres risques!
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.
- En cas de panne de l'appareil, veuillez le débrancher de l'alimentation. Le moyen le plus rapide de procéder consiste à débrancher l'adaptateur secteur de la prise de courant.
- Il s'agit d'un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.
- Pour éviter toute contamination de l'environnement, séparez l'appareil des déchets ménagers et jetez-le de manière sûre, par exemple dans des zones désignées. Familiarisez-vous avec les procédures permettant de transporter correctement l'équipement vers les points de collecte désignés dans votre région.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements FCC, IC et Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 330 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.10.2 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik uređaji moraju biti instalirani prema uputama.
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-62.png)

Ovisno o korištenoj anteni, morate postaviti njezino pojačanje i '*Installation*' na '*Indoors*' ili '*Outdoors*', ovisno o vrsti upotrebe. Time se osigurava da EIRP zadovoljava ograničenje koje su postavile lokalne vlasti. To se radi u izborniku Quickset.

**Prva upotreba:**

- Ovaj proizvod dolazi bez kućišta i dizajniran je za ugradnju u krajnje proizvode ili kućišta korisnika. Kompatibilno MikroTik kućište za ovaj proizvod možete pronaći na [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Uređaj dolazi u ESD zaštitnom pakiranju. Prilikom rukovanja električnom opremom pridržavajte se sljedećih sigurnosnih mjera opreza:Koristite vrpcu za uzemljenje prilikom raspakiranja i rada s električnim komponentama kako biste izbjegli oštećenje uslijed električnog pražnjenja (ESD);
- Nakon raspakiranja ruter stavite na antistatičku podlogu;
- Prilikom postavljanja jedinice pazite da nema predmeta koji bi mogli oštetiti ili dodirnuti PCB ploču;
- Uređaj se može montirati na željeno mjesto pomoću tvornički isporučenih rupa na PCB ploči, koje se nalaze sa svake strane uređaja;
- Prije spajanja uređaja na izvor napajanja, priključite antene na konektore;
- Spojite uređaj na izvor napajanja;
- Spojite svoje računalo na Ethernet priključak;
- Konfiguracija se mora obaviti pomoću web preglednika WebFig ili alata za konfiguraciju WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Otvorite [http://192.168.88.1](http://192.168.88.1) u web pregledniku kako biste započeli postavljanje. Ako IP adresa nije dostupna, koristite WinBox i povežite se putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Kliknite na gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u izbornik "Files" WinBoxa i ponovno pokrenite uređaj;
- Ažuriranjem softvera RouterOS na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U izborniku *"QuickSet"* postavite način rada *"PTP Bridge AP"* i odaberite svoju državu kako biste primijenili postavke propisa zemlje;
- Postavite pojačanje antene, ovisno o korištenoj anteni;
- U donjem polju postavite lozinku za usmjerivač.

**Sigurnosne informacije:**

- Prije nego počnete raditi na bilo kojoj MikroTik opremi, budite svjesni opasnosti povezanih s električnim sklopovima i upoznajte se sa standardnim postupcima za sprječavanje nezgoda. Instalater bi trebao biti upoznat s mrežnim strukturama, terminima i konceptima.
- Proizvod dolazi bez kućišta i namijenjen je za ugradnju u kućište od strane obučenog i kvalificiranog osoblja. Instalater je odgovoran za osiguranje da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastaviti, popraviti ili modificirati uređaj.
- Koristite samo napajanje i dodatke koje je odobrio proizvođač i koji se nalaze u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba instalirati obučeno i kvalificirano osoblje, prema ovim uputama za instalaciju. Instalater je odgovoran za osiguravanje da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima.
- Ne pokušavajte rastaviti, popraviti ili modificirati uređaj. Ako je potreban servis, kontaktirajte MikroTik podršku.
- Ovaj proizvod se može koristiti u zatvorenom i na otvorenom. Prije početka instalacije pažljivo pročitajte upute za montažu. Neupotreba ispravnog hardvera i konfiguracije ili poštivanje ispravnih postupaka može rezultirati opasnom situacijom za ljude i oštećenjem sustava. Za instalaciju na otvorenom obavezno koristite kućište s ocjenom najmanje IP54.
- Ne možemo jamčiti da neće doći do nezgoda ili štete zbog nepravilne uporabe uređaja. Pažljivo koristite ovaj proizvod i radite na vlastitu odgovornost!
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.
- U slučaju kvara uređaja, isključite ga iz struje. Najbrži način da to učinite je isključivanjem adaptera iz strujne utičnice.
- Ovo je proizvod A klase. U kućnom okruženju, ovaj proizvod može uzrokovati radio smetnje u kojem slučaju korisnik može morati poduzeti odgovarajuće mjere.
- Kako biste izbjegli onečišćenje okoliša, odvojite uređaj od kućnog otpada i odložite ga na siguran način, na primjer, na određenim mjestima. Upoznajte se s postupcima za pravilan transport opreme do određenih sabirnih mjesta u vašem području.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju FCC, IC i Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 330 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.10.2-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik eszközt az utasításoknak megfelelően kell telepíteni.
:::

*Ez egy vezeték nélküli hálózati eszköz.* *A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*Műszaki leírások, brosúrák és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-62.png)

A használt antennától függően az erősítést és az '*Installation*'-t '*Indoor*' vagy '*Outdoor*' értékre kell állítani, a használat típusától függően. Ezzel biztosítható, hogy az EIRP megfeleljen a helyi hatóságok által meghatározott határértéknek. Ez a Gyorsbeállítás menüben történik.

**Első használat:**

- Ez a termék burkolat nélkül érkezik, és a felhasználók végtermékeibe vagy burkolataiba történő beépítésre készült. A termékhez kompatibilis MikroTik burkolat a [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures) oldalon található.
- A készülék ESD védőcsomagolásban érkezik. Az elektromos berendezések kezelésekor tartsa be a következő biztonsági óvintézkedéseket:Kicsomagoláskor és az elektromos alkatrészekkel végzett munka során használjon földelő csuklópántot, hogy elkerülje az elektromos kisülés (ESD) okozta károsodást;
- Kicsomagolás után helyezze a routert az antisztatikus szőnyegre;
- Az egység felszerelésekor ügyeljen arra, hogy ne legyenek olyan tárgyak, amelyek megsérthetik vagy megérinthetik a PCB lemezt;
- Az eszköz a kívánt helyre szerelhető a gyárilag biztosított NYÁK-lemez furataival, amelyek a készülék mindkét oldalán találhatók;
- Mielőtt csatlakoztatná a készüléket az áramforráshoz, csatlakoztassa az antennákat a csatlakozókhoz;
- Csatlakoztassa a készüléket az áramforráshoz;
- Csatlakoztassa számítógépét az Ethernet porthoz;
- A konfigurációt a WebFig webböngésző vagy a WinBox konfigurációs eszköz használatával kell elvégezni [https://mt.lv/WinBox](https://mt.lv/WinBox); **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Nyissa meg a [http://192.168.88.1](http://192.168.88.1) címet egy webböngészőben a beállítások elindításához. Ha az IP-cím nem elérhető, használja a WinBoxot, és csatlakozzon a MAC-cím használatával. A felhasználónév "admin", és nincs jelszó (vagy néhány modell esetében ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson az "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WinBox "Files" menübe, majd indítsa újra az eszközt;
- Az RouterOS szoftver frissítésével a legújabb verzióra biztosíthatja az optimális teljesítményt, stabilitást és biztonsági frissítéseket;
- A *"QuickSet"* menüben állítsa be a *"PTP Bridge AP"* módot, és válassza ki az országot az országszabályozási beállítások alkalmazásához;
- Állítsa be az antenna erősítését a használt antennától függően;
- Állítsa be az útválasztó jelszavát az alsó mezőben.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozna, legyen tisztában az elektromos áramkörökkel járó veszélyekkel, és ismerje meg a balesetek megelőzésére vonatkozó szabványos gyakorlatokat. A telepítőnek ismernie kell a hálózati struktúrákat, kifejezéseket és fogalmakat.
- A terméket burkolat nélkül szállítjuk, és képzett és képesített személyzetnek kell beszerelnie a szekrénybe. A telepítő felelős azért, hogy megbizonyosodjon arról, hogy a berendezés telepítése megfelel a helyi és országos elektromos előírásoknak. Ne kísérelje meg szétszerelni, javítani vagy módosítani a készüléket.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használja, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a berendezést képzett és szakképzett személyzetnek kell telepítenie a jelen szerelési útmutató szerint. A telepítő felelős azért, hogy megbizonyosodjon arról, hogy a berendezés beszerelése megfelel a helyi és nemzeti elektromos előírásoknak.
- Ne kísérelje meg szétszerelni, javítani vagy módosítani a készüléket. Ha szervizre van szüksége, forduljon a MikroTik ügyfélszolgálatához.
- Ez a termék beltéren és kültéren is használható. Kérjük, a telepítés megkezdése előtt figyelmesen olvassa el a szerelési útmutatót. A megfelelő hardver és konfiguráció használatának elmulasztása, illetve a megfelelő eljárások betartásának elmulasztása emberekre veszélyes helyzetet és a rendszer károsodását okozhatja. A kültéri telepítéshez győződjön meg arról, hogy legalább IP54 védettségű burkolatot használ.
- Nem tudjuk garantálni, hogy a készülék nem rendeltetésszerű használatából eredő baleset vagy kár nem következik be. Kérjük, használja ezt a terméket körültekintően, és saját felelősségére működjön!
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.
- A készülék meghibásodása esetén áramtalanítsa. Ennek leggyorsabb módja, ha kihúzza a hálózati adaptert a konnektorból.
- Ez egy A osztályú termék. Otthoni környezetben ez a termék rádióinterferenciát okozhat, amely esetben a felhasználónak megfelelő intézkedéseket kell tennie.
- A környezet szennyezésének elkerülése érdekében különítse el a készüléket a háztartási hulladéktól, és biztonságos módon, például a kijelölt helyeken dobja ki. Ismerkedjen meg a berendezés megfelelő gyűjtőhelyre történő szállításának eljárásával.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az FCC, IC és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 330 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan Cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.10.2 atau versi stabil terbaru, untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Pengguna akhir bertanggung jawab untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya keluaran, persyaratan perkabelan, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat MikroTik harus diinstal sesuai petunjuk.
:::

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama model produk pada label (ID).*

*Kunjungi halaman panduan pengguna di [https://mt.lv/um-id](https://mt.lv/um-id) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis, brosur, dan info lebih lanjut mengenai produk di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [https://mt.lv/help-id](https://mt.lv/help-id)*
*Jika Anda memerlukan bantuan dalam konfigurasi, silakan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/indonesian.badge-24.png)

Tergantung pada antena yang digunakan, Anda perlu mengatur penguatannya dan mengatur "Instalasi" ke "Indoor" atau "Outdoor", tergantung pada jenis penggunaan. Hal ini untuk memastikan bahwa EIRP mematuhi batas yang ditetapkan oleh otoritas setempat. Ini dilakukan di menu Quickset.

**Penggunaan Pertama:**

- Produk ini hadir tanpa penutup dan dirancang untuk dipasang ke produk akhir atau penutup pengguna. Enklosur MikroTik yang kompatibel untuk produk ini dapat ditemukan di [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Perangkat ini hadir dalam kemasan pelindung ESD. Saat menangani peralatan listrik harap perhatikan tindakan pencegahan keselamatan berikut:
- Gunakan tali pengikat pergelangan tangan saat membuka kemasan dan menangani komponen listrik untuk menghindari kerusakan pelepasan listrik (ESD);
- Setelah membongkar, harap letakkan router di atas alas antistatis;
- Saat memasang unit pastikan tidak ada benda yang dapat merusak atau menyentuh pelat PCB;
- Perangkat dapat dipasang di lokasi yang Anda inginkan menggunakan lubang yang disediakan pabrik pada pelat PCB, yang terletak di setiap sisi perangkat;
- Sebelum menyambungkan perangkat ke sumber listrik, harap pasang antena ke konektor;
- Hubungkan perangkat ke sumber listrik;
- Hubungkan PC Anda ke port Ethernet;
- Konfigurasi harus dilakukan menggunakan peramban web WebFig atau alat konfigurasi WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Buka [http://192.168.88.1](http://192.168.88.1) di peramban web untuk memulai pengaturan. Jika alamat IP tidak tersedia, gunakan WinBox dan hubungkan menggunakan alamat MAC. Nama pengguna adalah "admin", dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang sudah diunduh ke menu "Files" WinBox dan reboot perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja optimal, stabilitas, dan pembaruan keamanan;
- Di menu "QuickSet" siapkan mode "PTP Bridge AP" dan pilih negara Anda, untuk menerapkan setelan peraturan negara;
- Atur penguatan antena, tergantung antena yang digunakan;
- Siapkan kata sandi router Anda di kolom bawah.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Produk ini hadir tanpa penutup dan dimaksudkan untuk dipasang ke dalam penutup oleh personel yang terlatih dan berkualifikasi. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, dan dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional.
- Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat. Jika diperlukan servis, silakan hubungi support MikroTik.
- Produk ini dapat digunakan baik di dalam maupun di luar ruangan. Harap baca petunjuk pemasangan dengan cermat sebelum memulai pemasangan. Kegagalan dalam menggunakan hardware dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem. Untuk memasang di luar ruangan, pastikan untuk menggunakan setidaknya penutup berperingkat IP54.
- Kami tidak dapat menjamin bahwa tidak akan terjadi kecelakaan atau kerusakan akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan operasikan dengan risiko yang Anda tanggung sendiri!
- Stopkontak harus dipasang di dekat peralatan dan mudah dijangkau.
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut adaptor daya dari stopkontak.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai.
- Untuk menghindari kontaminasi terhadap lingkungan, pisahkan perangkat dari limbah rumah tangga dan buang dengan cara yang aman, misalnya, di tempat yang telah ditentukan. Pahami prosedur pengangkutan peralatan dengan benar ke tempat pengumpulan yang ditentukan di wilayah Anda.

**Paparan Radiasi Frekuensi Radio:** Peralatan MikroTik ini mematuhi batas paparan radiasi FCC, IC, dan Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini sebaiknya dipasang dan dioperasikan tidak lebih dekat dari 330 sentimeter dari tubuh Anda, pengguna pekerjaan, atau masyarakat umum.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.10.2 o all'ultima versione stabile, per garantire la conformità con le normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi MikroTik devono essere installati secondo le istruzioni.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, cerca un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-62.png)

A seconda dell'antenna utilizzata, è necessario impostare il suo guadagno e *'Installation'* su '*Indoor*' o '*Outdoor*', a seconda del tipo di utilizzo. Questo per garantire che l'EIRP soddisfi il limite fissato dalle autorità locali. Questo viene fatto nel menu Quickset.

**Primo utilizzo:**

- Questo prodotto viene fornito senza custodia ed è progettato per essere installato nei prodotti finali o nelle custodie degli utenti. La custodia MikroTik compatibile per questo prodotto è disponibile su [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Il dispositivo viene fornito in un imballaggio protettivo ESD. Quando si maneggiano apparecchiature elettriche, osservare le seguenti precauzioni di sicurezza:Utilizzare un braccialetto con messa a terra quando si disimballa e si lavora con componenti elettrici per evitare danni da scariche elettriche (ESD);
- Dopo aver disimballato, posizionare il router sul tappetino antistatico;
- Durante il montaggio dell'unità assicurarsi che non siano presenti oggetti che possano danneggiare o toccare la piastra PCB;
- Il dispositivo può essere montato nella posizione desiderata utilizzando i fori forniti in fabbrica su una piastra PCB, situata su ciascun lato del dispositivo;
- Prima di collegare il dispositivo alla fonte di alimentazione, collegare le antenne ai connettori;
- Collegare il dispositivo alla fonte di alimentazione;
- Collega il tuo PC alla porta Ethernet;
- La configurazione deve essere effettuata utilizzando lo strumento di configurazione *"WinBox"* [https://mt.lv/winbox](https://mt.lv/winbox);
- La configurazione deve essere effettuata utilizzando il browser WebFig o lo strumento di configurazione WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Apri [http://192.168.88.1](http://192.168.88.1) in un browser web per avviare la configurazione. Se l'indirizzo IP non è disponibile, utilizza WinBox e connettiti utilizzando l'indirizzo MAC. Il nome utente è "admin", e non c'è alcuna password (o, per alcuni modelli, controlla gli utenti e le password wireless sull'adesivo);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Nel menu *"QuickSet"* impostare la modalità *"PTP Bridge AP"* e scegliere il proprio paese, per applicare le impostazioni della normativa nazionale;
- Impostare il guadagno dell'antenna, a seconda dell'antenna utilizzata;
- Imposta la password del tuo router nel campo in basso.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, sii consapevole dei rischi connessi ai circuiti elettrici e acquisisci familiarità con le pratiche standard per prevenire gli incidenti. L'installatore deve avere familiarità con le strutture, i termini e i concetti della rete.
- Il prodotto viene fornito senza custodia ed è destinato a essere installato all'interno della custodia da personale addestrato e qualificato. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme alle normative elettriche locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo le presenti istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme alle normative elettriche locali e nazionali.
- Non tentare di smontare, riparare o modificare il dispositivo. Se è necessaria assistenza, contattare il supporto MikroTik.
- Questo prodotto può essere utilizzato sia all'interno che all'esterno. Si prega di leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il mancato rispetto delle procedure corrette potrebbero causare situazioni pericolose per le persone e danni al sistema. Per l'installazione all'aperto assicurarsi di utilizzare un involucro con classificazione almeno IP54.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e di operare a proprio rischio e pericolo!
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate.
- Per evitare la contaminazione dell'ambiente, separa il dispositivo dai rifiuti domestici e smaltiscilo in modo sicuro, ad esempio nelle aree designate. Acquisire familiarità con le procedure per trasportare correttamente l'attrezzatura nei punti di raccolta designati nella propria zona.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni FCC, IC e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 330 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.10.2 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik tæki verða að vera sett upp samkvæmt leiðbeiningum.
:::

*Þetta er þráðlaust nettæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*Ef þú þarft hjálp við stillingar, vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-62.png)

Það fer eftir loftnetinu sem notað er, þú verður að stilla styrk þess og '*Installation*' á '*Indoor*' eða '*Outdoor*', allt eftir notkunartegundinni. Þetta er til að tryggja að EIRP standist þau mörk sem sveitarfélögin setja. Þetta er gert í Quickset valmyndinni.

**Fyrsta notkun:**

- Þessi vara kemur án girðingar og er hönnuð til að vera sett upp í lokavörur eða girðingar notenda. Samhæft MikroTik girðing fyrir þessa vöru er að finna á [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Tækið kemur í ESD hlífðarumbúðum. Við meðhöndlun rafbúnaðar vinsamlegast fylgdu eftirfarandi öryggisráðstöfunum:Notaðu úlnliðsjarðband þegar þú tekur upp og vinnur með rafmagnsíhluti til að forðast skemmdir á rafhleðslu (ESD);
- Eftir að hafa pakkað niður vinsamlegast settu beininn á andstæðingur-truflanir mottuna;
- Þegar einingin er sett upp skaltu ganga úr skugga um að það séu engir hlutir sem geta skemmt eða snert PCB plötuna;
- Hægt er að festa tækið á viðkomandi stað með því að nota verksmiðjugötin á PCB plötu, staðsett á hvorri hlið tækisins;
- Áður en tækið er tengt við aflgjafann skaltu tengja loftnetin við tengin;
- Tengdu tækið við aflgjafa;
- Tengdu tölvuna þína við Ethernet tengið;
- Stillingin þarf að vera framkvæmd með WebFig eða WinBox stillingartólun [https://mt.lv/WinBox](https://mt.lv/WinBox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Opnið [http://192.168.88.1](http://192.168.88.1) í vafra til að byrja uppsetningu. Ef IP-talan er ekki tiltæki, notið WinBox og tengist með MAC-tölvu. Notendanafnið er „admin“, og lykilorð er ekki til (eða, fyrir sumar gerðir, athugaðu notendur og þráðlaus lykilorð á merki);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pakka í WinBox "Files" valkostinn og endurræsa tækið;
- Með því að uppfæra hugbúnaðinn á RouterOS í nýjustu útgáfu getur þú tryggjað bestu mögulegu afköst, stöðugleika og öryggisuppfærslur;
- Í *"QuickSet"* valmyndinni skaltu setja upp *"PTP Bridge AP"* ham og velja land þitt, til að beita landsreglustillingum;
- Stilltu loftnetsstyrkinn, eftir því hvaða loftnet er notað;
- Settu upp lykilorðið þitt fyrir leiðina í neðsta reitnum.

**Öryggisupplýsingar:**

- Áður en þú vinnur á MicroTik búnaði skaltu vera meðvitaður um hætturnar sem fylgja rafrásum og þekkja staðlaðar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að þekkja netkerfi, hugtök og hugtök.
- Varan kemur án girðingar og er ætlað að vera sett upp í girðinguna af þjálfuðu og hæfu starfsfólki. Uppsetningaraðilinn er ábyrgur fyrir því að ganga úr skugga um að uppsetning búnaðarins sé í samræmi við staðbundin og landsbundin rafmagnsreglur. Ekki reyna að taka í sundur, gera við eða breyta tækinu.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þennan búnað á að setja upp af þjálfuðu og hæfu starfsfólki, samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn er ábyrgur fyrir að ganga úr skugga um að uppsetning búnaðarins sé í samræmi við staðbundnar og landsbundnar rafmagnsreglur.
- Ekki reyna að taka í sundur, gera við eða breyta tækinu. Ef þörf er á þjónustu, vinsamlegast hafðu samband við þjónustudeild MikroTik.
- Þessa vöru er hægt að nota bæði inni og úti. Vinsamlegast lestu uppsetningarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Misbrestur á að nota réttan vélbúnað og uppsetningu eða fylgja réttum verklagsreglum gæti leitt til hættulegra aðstæðna fyrir fólk og skemmda á kerfinu. Til að setja upp utandyra, vertu viss um að nota að minnsta kosti IP54 flokkunarhólf.
- Við getum ekki ábyrgst að engin slys eða skemmdir eigi sér stað vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og vinnið á eigin ábyrgð!
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.
- Ef tækið bilar, vinsamlegast aftengdu það frá rafmagni. Fljótlegasta leiðin til að gera það er með því að taka straumbreytinn úr sambandi.
- Þetta er vara í flokki A. Í heimilisumhverfi gæti þessi vara valdið útvarpstruflunum og þá gæti notandinn þurft að grípa til viðeigandi ráðstafana.
- Til að forðast mengun umhverfisins skaltu skilja tækið frá heimilissorpi og farga því á öruggan hátt, til dæmis á afmörkuðum svæðum. Kynntu þér verklagsreglur um að flytja búnaðinn á viðeigandi söfnunarstaði á þínu svæði.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við FCC, IC og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 330 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10.2 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-enheter måste installeras enligt instruktionerna.
:::

*Dette er en trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-62.png)

Avhengig av antennen som brukes, må du stille inn forsterkningen og '*Installation*' til '*Indoor*' eller '*Outdoor*', avhengig av brukstypen. Dette for å sikre at EIRP holder grensen fastsatt av lokale myndigheter. Dette gjøres i Quickset-menyen.

**Första användningen:**

- Dette produktet kommer uten kapsling og er designet for å installeres i brukernes sluttprodukter eller kabinetter. Kompatibel MikroTik-kabinett for dette produktet finner du på [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Enheten kommer i ESD-beskyttende emballasje. Ved håndtering av elektrisk utstyr, vær oppmerksom på følgende sikkerhetsregler:Bruk en jordingsstropp når du pakker ut og arbeider med elektriske komponenter for å unngå skade på elektrisk utladning (ESD);
- Etter utpakking, plasser ruteren på den antistatiske matten;
- Når du monterer enheten, sørg for at det ikke er gjenstander som kan skade eller berøre PCB-platen;
- Enheten kan monteres på ønsket sted ved å bruke de fabrikkleverte hullene i en PCB-plate, plassert på hver side av enheten;
- Før du kobler enheten til strømkilden, må du feste antennene til kontaktene;
- Koble enheten til strømkilden;
- Koble PC-en til Ethernet-porten;
- Konfigurasjonen må gjøres ved hjelp av nettleseren WebFig eller konfigurasjonsverktøyet WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Åpne [http://192.168.88.1](http://192.168.88.1) i en nettleser for å starte oppsettet. Hvis IP-adressen ikke er tilgjengelig, bruk WinBox og koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på knappen "Check for updates" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WinBox "Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I *"QuickSet"-* menyen setter du opp *"PTP Bridge AP"-* modus og velger ditt land for å bruke landreguleringsinnstillinger;
- Still inn antenneforsterkningen, avhengig av antennen som brukes;
- Sett opp ruterpassordet ditt i det nederste feltet.

**Säkerhetsinformation:**

- Før du arbeider med noe MikroTik-utstyr, må du være klar over farene forbundet med elektriske kretser, og være kjent med standard praksis for å forhindre ulykker. Installatøren bør være kjent med nettverksstrukturer, termer og konsepter.
- Produktet leveres uten kapsling og er ment å installeres i kabinettet av opplært og kvalifisert personell. Installatøren er ansvarlig for å sørge for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske forskrifter. Ikke forsøk å demontere, reparere eller modifisere enheten.
- Bruk kun strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av opplært og kvalifisert personell, i henhold til disse installasjonsinstruksjonene. Installatøren er ansvarlig for å sørge for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske forskrifter.
- Ikke forsøk å demontere, reparere eller modifisere enheten. Hvis service er nødvendig, vennligst kontakt MikroTik-støtte.
- Dette produktet kan brukes både innendørs og utendørs. Vennligst les monteringsanvisningen nøye før du starter installasjonen. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller følge riktige prosedyrer kan føre til farlige situasjoner for mennesker og skade på systemet. For å installere utendørs, sørg for å bruke minst IP54-klassifisert kapsling.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk på egen risiko!
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.
- Ved feil på enheten, koble den fra strømmen. Den raskeste måten å gjøre det på er ved å koble strømadapteren fra strømuttaket.
- Dette er et klasse A-produkt. I et hjemmemiljø kan dette produktet forårsake radioforstyrrelser, i så fall kan brukeren bli pålagt å ta tilstrekkelige tiltak.
- For å unngå forurensning av miljøet, separer enheten fra husholdningsavfallet og kast den på en sikker måte, for eksempel i anviste områder. Bli kjent med prosedyrer for riktig transport av utstyret til utpekte innsamlingssteder i ditt område.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med FCC, IC og EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 330 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.10.2“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ įrenginiai turi būti įdiegti pagal instrukcijas.
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*Jei jums reikia pagalbos dėl konfigūravimo, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-62.png)

Priklausomai nuo naudojamos antenos, turite nustatyti jos stiprinimą ir nustatymą „*Installation*“ į „*Indoors*“ arba „*outdoors*“, priklausomai nuo naudojimo tipo. Taip siekiama užtikrinti, kad EIRP atitiktų vietos valdžios institucijų nustatytą ribą. Tai atliekama „Quickset“ meniu.

**Pirmasis naudojimas:**

- Šis gaminys tiekiamas be gaubto ir yra skirtas montuoti į galutinius naudotojo gaminius arba korpusus. Šiam gaminiui suderinamą MikroTik korpusą rasite adresu [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Prietaisas yra ESD apsauginėje pakuotėje. Dirbdami su elektros įranga, laikykitės šių saugos priemonių:Išpakuodami ir dirbdami su elektros komponentais naudokite riešo įžeminimo dirželį, kad išvengtumėte elektros iškrovos (ESD) pažeidimų;
- Išpakavę maršruto parinktuvą padėkite ant antistatinio kilimėlio;
- Montuodami įrenginį įsitikinkite, kad nėra daiktų, galinčių pažeisti arba liesti PCB plokštę;
- Įrenginį galima montuoti norimoje vietoje naudojant gamykloje numatytas skyles PCB plokštėje, esančias kiekvienoje įrenginio pusėje;
- Prieš prijungdami įrenginį prie maitinimo šaltinio, prijunkite antenas prie jungčių;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Prijunkite kompiuterį prie Ethernet prievado;
- Konfigūracija turi būti atlikta naudojant naršyklę WebFig arba konfigūravimo įrankį WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Atidarykite [http://192.168.88.1](http://192.168.88.1) naršyklėje, kad pradėtumėte nustatymus. Jei IP adresas nepasiekiamas, naudokite WinBox ir prisijunkite naudodami MAC adresą. Prisijungimo vardas yra "admin", ir nėra slaptažodžio (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite parsisiųstus paketus į WinBox "Files" meniu ir paleiskite įrenginį iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- *"QuickSet"* meniu nustatykite *"PTP Bridge AP"* režimą ir pasirinkite savo šalį, kad pritaikytumėte šalies reguliavimo nustatymus;
- Nustatykite antenos stiprinimą, priklausomai nuo naudojamos antenos;
- Apatiniame lauke nustatykite maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš dirbdami su bet kokia „MikroTik“ įranga, atkreipkite dėmesį į pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine nelaimingų atsitikimų prevencijos praktika. Montuotojas turi būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Gaminys tiekiamas be gaubto ir yra skirtas montuoti apmokytiems ir kvalifikuotiems darbuotojams. Montuotojas yra atsakingas už tai, kad įrangos montavimas atitiktų vietinius ir nacionalinius elektros kodeksus. Nebandykite išardyti, taisyti ar modifikuoti įrenginio.
- Naudokite tik gamintojo patvirtintą maitinimo šaltinį ir priedus, kuriuos rasite originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokytas ir kvalifikuotas personalas, kaip nurodyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad būtų užtikrinta, jog įrangos montavimas atitiktų vietinius ir nacionalinius elektros kodeksus.
- Nebandykite išardyti, taisyti ar modifikuoti įrenginio. Jei reikia techninės priežiūros, susisiekite su MikroTik techninės pagalbos tarnyba.
- Šis produktas gali būti naudojamas tiek viduje, tiek lauke. Prieš pradėdami montuoti, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite tinkamos aparatinės įrangos ir konfigūracijos arba nesilaikysite tinkamų procedūrų, gali kilti pavojingų situacijų žmonėms ir sugadinti sistemą. Jei norite montuoti lauke, naudokite bent IP54 įvertinimo korpusą.
- Negalime garantuoti, kad dėl netinkamo prietaiso naudojimo neįvyks nelaimingų atsitikimų ar žalos. Naudokite šį gaminį atsargiai ir rizikuokite!
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.
- Įrenginio gedimo atveju atjunkite jį nuo maitinimo šaltinio. Greičiausias būdas tai padaryti – ištraukti maitinimo adapterį iš maitinimo lizdo.
- Tai A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trukdžius, tokiu atveju naudotojui gali tekti imtis atitinkamų priemonių.
- Kad išvengtumėte aplinkos užteršimo, atskirkite įrenginį nuo buitinių atliekų ir saugiai išmeskite, pavyzdžiui, tam skirtose vietose. Susipažinkite su procedūromis, kaip tinkamai transportuoti įrangą į paskirtus surinkimo punktus jūsų vietovėje.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka FCC, IC ir Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 330 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.10.2 vai jaunāku stabilo versiju, lai nodrošinātu atbilstību vietējās valsts likumdošanai.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik ierīcēm jābūt uzstādītām atbilstoši instrukcijām.
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products).*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv).*
*Ja jums nepieciešama palīdzība ar ierīces konfigurēšanu, lūdzu, konsultējieties ar konsultantiem, kontaktinformācija atrodama vietnē [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-62.png)

Atkarībā no izmantotās antenas ir jāiestata tās pastiprinājums un '*Installation*' uz '*Indoor*' vai '*Outdoor*' atkarībā no lietošanas veida. Tas ir paredzēts, lai nodrošinātu, ka EIRP atbilst vietējo iestāžu noteiktajam ierobežojumam. Tas tiek darīts Quickset izvēlnē.

**Pirmā lietošana:**

- Šis produkts tiek piegādāts bez korpusa un ir paredzēts uzstādīšanai lietotāju galaproduktos vai korpusos. Šim produktam saderīgu MikroTik korpusu var atrast vietnē [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Ierīce tiek piegādāta ESD aizsargājošā iepakojumā. Strādājot ar elektriskajām iekārtām, lūdzu, ievērojiet šādus drošības pasākumus:Izpakojot un strādājot ar elektriskajām sastāvdaļām, izmantojiet plaukstas zemējuma siksnu, lai izvairītos no elektriskās izlādes (ESD) bojājumiem;
- Pēc izpakošanas, lūdzu, novietojiet maršrutētāju uz antistatiskā paklājiņa;
- Uzstādot ierīci, pārliecinieties, vai tajā nav priekšmetu, kas varētu sabojāt PCB plāksni vai pieskarties tai;
- Ierīci var uzstādīt vēlamajā vietā, izmantojot rūpnīcā paredzētos caurumus PCB plāksnē, kas atrodas katrā ierīces pusē;
- Pirms ierīces pievienošanas strāvas avotam, lūdzu, pievienojiet antenas savienotājiem;
- Pievienojiet ierīci strāvas avotam;
- Pievienojiet datoru Ethernet portam;
- Konfigurāciju ir jāveic, izmantojot WebFig pārlūku vai WinBox konfigurācijas rīku [https://mt.lv/WinBox](https://mt.lv/WinBox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Atveriet [http://192.168.88.1](http://192.168.88.1) pārlūkprogrammā, lai sāktu iestatīšanu. Ja IP adrese nav pieejama, izmantojiet WinBox un izveidojiet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav paroles (vai, dažiem modeļiem, pārbaudiet lietotāju un bezvadu paroles uz līmējuma);
- Noklikšķiniet uz pogas "Check for updates" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Ielādējiet lejupielādētās pakotnes WinBox "Files" izvēlnē un restartējiet ierīci;
- Jauninot RouterOS programmatūru uz jaunāko versiju, jūs varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Izvēlnē *"QuickSet"* iestatiet *"PTP Bridge AP"* režīmu un izvēlieties savu valsti, lai piemērotu likumā noteiktos iestatījumus;
- Iestatiet antenas pastiprinājumu atkarībā no izmantotās antenas;
- Apakšējā laukā iestatiet maršrutētāja paroli.

**Drošības informācija:**

- Pirms strādājat pie jebkuras MikroTik iekārtas, apzinieties ar elektriskajām shēmām saistītos riskus un iepazīstieties ar standarta praksi negadījumu novēršanai. Instalētājam jāpārzina tīkla struktūras, termini un jēdzieni.
- Produkts tiek piegādāts bez korpusa, un tas ir paredzēts, lai apmācīts un kvalificēts personāls to uzstādītu korpusā. Uzstādītājs ir atbildīgs par to, lai iekārtas uzstādīšana atbilstu vietējiem un valsts elektriskajiem noteikumiem. Nemēģiniet izjaukt, salabot vai pārveidot ierīci.
- Izmantojiet tikai ražotāja apstiprināto barošanas bloku un piederumus, kas ir atrodami šī izstrādājuma oriģinālajā iepakojumā.
- Šis aprīkojums ir jāuzstāda apmācītam un kvalificētam personālam saskaņā ar šiem uzstādīšanas norādījumiem. Uzstādītājs ir atbildīgs par to, lai nodrošinātu, ka iekārtas uzstādīšana atbilst vietējiem un valsts elektriskajiem noteikumiem.
- Nemēģiniet izjaukt, salabot vai pārveidot ierīci. Ja nepieciešams serviss, lūdzu, sazinieties ar MikroTik atbalsta dienestu.
- Šo produktu var izmantot gan iekštelpās, gan ārā. Pirms uzstādīšanas, lūdzu, rūpīgi izlasiet montāžas instrukcijas. Pareizas aparatūras un konfigurācijas neizmantošana vai pareizu procedūru neievērošana var radīt bīstamas situācijas cilvēkiem un sabojāt sistēmu. Lai uzstādītu ārpus telpām, noteikti izmantojiet vismaz IP54 novērtējuma korpusu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ nenotiks negadījumi vai bojājumi. Lūdzu, izmantojiet šo produktu uzmanīgi un riskējiet!
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas padeves. Ātrākais veids, kā to izdarīt, ir atvienot strāvas adapteri no strāvas kontaktligzdas.
- Šis ir A klases produkts. Mājas vidē šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.
- Lai izvairītos no vides piesārņošanas, atdaliet ierīci no sadzīves atkritumiem un izmetiet to drošā veidā, piemēram, tam paredzētās vietās. Iepazīstieties ar procedūrām, kā pareizi transportēt aprīkojumu uz norādītajiem savākšanas punktiem jūsu reģionā.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst FCC, IC un Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 330 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.10.2 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż it-tħaddim fil-kanali tal-frekwenza legali, l-enerġija tal-ħruġ, ir-rekwiżiti tal-kejbils u r-rekwiżiti tal-Għażla Dinamika tal-Frekwenza (DFS). L-apparati kollha MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-62.png)

Skont l-antenna użata, trid issettja l-gwadann tagħha u l-'*Installation*' għal '*Indoor*' jew '*Outdoor*', skond it-tip ta' użu. Dan biex jiġi żgurat li l-EIRP jilħaq il-limitu stabbilit mill-awtoritajiet lokali. Dan isir fil-menu Quickset.

**L-Ewwel Użu:**

- Dan il-prodott jiġi mingħajr egħluq u huwa ddisinjat biex jiġi installat fil-prodotti finali jew fil-kompartimenti tal-utenti. Egħluq MikroTik kompatibbli għal dan il-prodott jista' jinstab fuq [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- L-apparat jiġi f'ippakkjar protettiv ESD. Meta timmaniġġja tagħmir elettriku jekk jogħġbok osserva l-prekawzjonijiet ta 'sigurtà li ġejjin:Uża ċinga ta 'l-ert tal-polz meta tneħħi l-ippakkjar u taħdem ma' komponenti elettriċi biex tevita ħsara ta 'skarigu elettriku (ESD);
- Wara li tneħħi l-ippakkjar jekk jogħġbok poġġi r-router fuq it-tapit anti-statiku;
- Meta twaħħal l-unità kun żgur li ma jkunx hemm oġġetti li jistgħu jagħmlu ħsara jew imissu l-pjanċa tal-PCB;
- L-apparat jista 'jiġi mmuntat fil-post mixtieq tiegħek billi tuża t-toqob ipprovduti mill-fabbrika fi pjanċa tal-PCB, li tinsab fuq kull naħa tal-apparat;
- Qabel ma tgħaqqad l-apparat mas-sors tal-enerġija, jekk jogħġbok waħħal l-antenni mal-konnetturi;
- Qabbad l-apparat mas-sors tal-enerġija;
- Qabbad il-PC tiegħek mal-port Ethernet;
- Il-konfigurazzjoni għandha tkun mfassla bl-użu ta 'WebFig jew l-għodda tal-konfigurazzjoni WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Għaġġar [http://192.168.88.1](http://192.168.88.1) f'browser web biex tibda l-iżvilupp. Jekk l-indirizz IP mhux disponibbli, uża l-WinBox u konnettiti billi tuża l-indirizz MAC. L-username huwa "admin", u m'hemmx password (jew, għal xi mudelli, iċċekkja l-passwords tal-utenti u tal-wireless fuq it-tickietta);
- Ikklikkja fuq il-buttuna "Check for updates" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Ipposta l-pakketti li jużaw lura fil-meni "Files" tal-WinBox u reboot l-apparat;
- Billi taġġorna l-softwer tal-RouterOS għall-aħħar verżjoni, tista 'tissikura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Fil- menu *"QuickSet"* waqqaf il -mod *"PTP Bridge AP"* u agħżel pajjiżek, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Issettja l-gwadann tal-antenna, skont l-antenna użata;
- Issettja l-password tar-router tiegħek fil-qasam t'isfel.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti maċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni tal-inċidenti. L-installatur għandu jkun familjari mal-istrutturi, it-termini u l-kunċetti tan-netwerk.
- Il-prodott jiġi mingħajr egħluq u huwa maħsub biex jiġi installat fil-kompartiment minn persunal imħarreġ u kwalifikat. L-installatur huwa responsabbli biex jiżgura li l-Installazzjoni tat-tagħmir tkun konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, isewwi jew timmodifika l-apparat.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li jistgħu jinstabu fl-ippakkjar oriġinali ta 'dan il-prodott.
- Dan it-tagħmir għandu jiġi installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli biex jiżgura li l-Installazzjoni tat-tagħmir tkun konformi mal-kodiċijiet elettriċi lokali u nazzjonali.
- Tippruvax tiżżarma, isewwi jew timmodifika l-apparat. Jekk ikun meħtieġ is-servizz, jekk jogħġbok ikkuntattja l-appoġġ ta' MikroTik.
- Dan il-prodott jista 'jintuża kemm ġewwa kif ukoll barra. Jekk jogħġbok aqra bir-reqqa l-istruzzjonijiet tal-immuntar qabel tibda l-installazzjoni. Nuqqas li tuża l-hardware u l-konfigurazzjoni korretti jew li ssegwi proċeduri korretti jista' jirriżulta f'sitwazzjoni perikoluża għan-nies u ħsara lis-sistema. Biex tinstalla barra kun żgur li tuża mill-inqas egħluq tal-klassifikazzjoni IP54.
- Ma nistgħux niggarantixxu li ma jseħħu l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u opera bir-riskju tiegħek!
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok skonnettjah mill-enerġija. L-aktar mod mgħaġġel biex tagħmel dan huwa billi tneħħi l-plagg tal-adapter tal-enerġija mill-iżbokk tad-dawl.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza tar-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.
- Biex tevita l-kontaminazzjoni tal-ambjent, issepara l-apparat mill-iskart domestiku u armih b'mod sikur, pereżempju, f'żoni magħżula. Kun familjari mal-proċeduri għat-trasport kif suppost tat-tagħmir lejn punti ta' ġbir magħżula fiż-żona tiegħek.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta 'FCC, IC u l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 330 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.10.2 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, waaronder de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-apparaten moeten volgens de instructies worden geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*Technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*Als je hulp nodig hebt bij het configureren, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-62.png)

Afhankelijk van de gebruikte antenne, moet u de versterking en de '*Installation*' instellen op '*Indoor*' of '*Outdoor*', afhankelijk van het gebruikstype. Dit om ervoor te zorgen dat EIRP voldoet aan de door de lokale autoriteiten gestelde grens. Dit doe je in het Quickset-menu.

**Eerste gebruik:**

- Dit product wordt geleverd zonder behuizing en is ontworpen om te worden geïnstalleerd in de eindproducten of behuizingen van de gebruiker. Compatibele MikroTik-behuizing voor dit product vindt u op [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Het apparaat wordt geleverd in een ESD-beschermende verpakking. Neem bij het hanteren van elektrische apparatuur de volgende veiligheidsmaatregelen in acht:Gebruik een aardingspolsband bij het uitpakken en werken met elektrische componenten om schade door elektrische ontladingen (ESD) te voorkomen;
- Plaats de router na het uitpakken op de antistatische mat;
- Zorg er bij het monteren van de unit voor dat er geen voorwerpen zijn die de printplaat kunnen beschadigen of aanraken;
- Het apparaat kan op de door u gewenste locatie worden gemonteerd met behulp van de in de fabriek aangebrachte gaten in een PCB-plaat, gelegen aan elke kant van het apparaat;
- Voordat u het apparaat op de stroombron aansluit, sluit u de antennes aan op de connectoren;
- Sluit het apparaat aan op de stroombron;
- Sluit uw pc aan op de Ethernet-poort;
- Configuratie moet worden gedaan met behulp van de WebFig-webbrowser of het WinBox-configuratiehulpprogramma [https://mt.lv/WinBox](https://mt.lv/WinBox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Open [http://192.168.88.1](http://192.168.88.1) in een webbrowser om de installatie te starten. Als het IP-adres niet beschikbaar is, gebruik WinBox en maak verbinding met het MAC-adres. De gebruikersnaam is "admin", en er is geen wachtwoord (of, voor sommige modellen, controleer gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WinBox "Files" menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Stel in het menu *"QuickSet"* de modus *"PTP Bridge AP"* in en kies uw land om de instellingen voor landregulering toe te passen;
- Stel de antenneversterking in, afhankelijk van de gebruikte antenne;
- Stel uw routerwachtwoord in het onderste veld in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur gaat werken, moet u zich bewust zijn van de gevaren die gepaard gaan met elektrische circuits en bekend zijn met de standaardpraktijken om ongelukken te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Het product wordt geleverd zonder behuizing en is bedoeld om door opgeleid en gekwalificeerd personeel in de behuizing te worden geïnstalleerd. De installateur is er verantwoordelijk voor dat de installatie van de apparatuur in overeenstemming is met de lokale en nationale elektriciteitsvoorschriften. Probeer het apparaat niet te demonteren, repareren of wijzigen.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektriciteitsvoorschriften.
- Probeer het apparaat niet te demonteren, repareren of wijzigen. Als service nodig is, neem dan contact op met MikroTik-ondersteuning.
- Dit product kan zowel binnen als buiten worden gebruikt. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Als u niet de juiste hardware en configuratie gebruikt of de juiste procedures volgt, kan dit leiden tot gevaarlijke situaties voor mensen en schade aan het systeem. Als u buitenshuis installeert, zorg er dan voor dat u een behuizing met minimaal IP54-classificatie gebruikt.
- Wij kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en gebruik het op eigen risico!
- Het stopcontact moet dichtbij de apparatuur worden geïnstalleerd en gemakkelijk toegankelijk zijn.
- Mocht er een apparaatstoring optreden, koppel deze dan los van de stroomvoorziening. De snelste manier om dit te doen is door de voedingsadapter uit het stopcontact te halen.
- Dit is een klasse A-product. In een huiselijke omgeving kan dit product radio-interferentie veroorzaken. In dat geval moet de gebruiker mogelijk adequate maatregelen nemen.
- Om besmetting van het milieu te voorkomen, moet u het apparaat scheiden van huishoudelijk afval en het op een veilige manier weggooien, bijvoorbeeld op de daarvoor bestemde plaatsen. Zorg ervoor dat u bekend bent met de procedures voor het correct transporteren van de apparatuur naar de aangewezen inzamelpunten bij u in de buurt.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de FCC-, IC- en EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 330 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.10.2 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia MikroTik muszą zostać zainstalowane zgodnie z instrukcjami.
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy w konfiguracji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-62.png)

W zależności od używanej anteny należy ustawić jej wzmocnienie i „*Installation*” na „*Indoor*” lub „*Outdoor*”, w zależności od typu użytkowania. Ma to na celu zapewnienie, że EIRP spełnia limit ustalony przez władze lokalne. Odbywa się to w menu Quickset.

**Pierwsze kroki:**

- Ten produkt jest dostarczany bez obudowy i jest przeznaczony do montażu w produktach końcowych lub obudowach użytkowników. Kompatybilną obudowę MikroTik dla tego produktu można znaleźć na stronie [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Urządzenie jest dostarczane w opakowaniu ochronnym ESD. Podczas obchodzenia się ze sprzętem elektrycznym należy przestrzegać następujących środków ostrożności:Podczas rozpakowywania i pracy z elementami elektrycznymi należy nosić pasek uziemiający na nadgarstku, aby uniknąć uszkodzeń spowodowanych wyładowaniami elektrycznymi (ESD);
- Po rozpakowaniu router należy położyć na macie antystatycznej;
- Podczas montażu urządzenia należy upewnić się, że nie ma żadnych przedmiotów, które mogłyby uszkodzić lub dotknąć płytki PCB;
- Urządzenie można zamontować w wybranym miejscu, korzystając z fabrycznie dostarczonych otworów w płytce PCB, znajdujących się po obu stronach urządzenia;
- Przed podłączeniem urządzenia do źródła zasilania należy podłączyć anteny do złączy;
- Podłącz urządzenie do źródła zasilania;
- Podłącz swój komputer do portu Ethernet;
- Konfiguracja powinna być dokonywana za pomocą przeglądarki internetowej WebFig lub narzędzia konfiguracyjnego WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Otwórz [http://192.168.88.1](http://192.168.88.1) w przeglądarce internetowej, aby rozpocząć konfigurację. Jeśli adres IP nie jest dostępny, użyj WinBox i połącz się za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła nie ma (lub, dla niektórych modeli, sprawdź hasła użytkowników i bezprzewodowe na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Wgraj pobrane pakiety do menu "Files" w WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu *"QuickSet"* ustaw tryb *"PTP Bridge AP"* i wybierz swój kraj, aby zastosować ustawienia przepisów krajowych;
- Ustaw wzmocnienie anteny w zależności od używanej anteny;
- Skonfiguruj hasło routera w dolnym polu.

**Informacje dotyczące bezpieczeństwa:**

- Zanim zaczniesz pracować na jakimkolwiek sprzęcie MikroTik, bądź świadomy zagrożeń związanych z obwodami elektrycznymi i zapoznaj się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien znać struktury sieciowe, terminy i koncepcje.
- Produkt jest dostarczany bez obudowy i przeznaczony jest do montażu w obudowie przez przeszkolony i wykwalifikowany personel. Instalator jest odpowiedzialny za upewnienie się, że instalacja sprzętu jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie próbuj demontować, naprawiać ani modyfikować urządzenia.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta i znajdujących się w oryginalnym opakowaniu tego produktu.
- Urządzenie to powinno być instalowane przez przeszkolony i wykwalifikowany personel, zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja sprzętu jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi.
- Nie próbuj demontować, naprawiać ani modyfikować urządzenia. Jeśli potrzebny jest serwis, skontaktuj się z pomocą techniczną MikroTik.
- Produkt ten można stosować zarówno wewnątrz, jak i na zewnątrz. Przed rozpoczęciem instalacji prosimy o dokładne zapoznanie się z instrukcją montażu. Niezastosowanie odpowiedniego sprzętu i konfiguracji lub nieprzestrzeganie właściwych procedur może spowodować niebezpieczną sytuację dla ludzi i uszkodzenie systemu. Aby zainstalować na zewnątrz, należy użyć obudowy o stopniu ochrony co najmniej IP54.
- Nie możemy zagwarantować, że na skutek nieprawidłowego użytkowania urządzenia nie dojdzie do żadnych wypadków ani uszkodzeń. Używaj tego produktu ostrożnie i obsługuj go na własne ryzyko!
- Gniazdko elektryczne powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.
- W przypadku awarii urządzenia należy odłączyć je od zasilania. Najszybszym sposobem na to jest odłączenie zasilacza od gniazdka elektrycznego.
- Jest to produkt klasy A. W środowisku domowym produkt ten może powodować zakłócenia radiowe, w takim przypadku użytkownik może być zobowiązany do podjęcia odpowiednich środków.
- Aby uniknąć skażenia środowiska, urządzenie należy oddzielić od odpadów domowych i utylizować w bezpieczny sposób, np. w wyznaczonych miejscach. Zapoznaj się z procedurami prawidłowego transportu sprzętu do wyznaczonych punktów zbiórki w Twojej okolicy.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie FCC, IC i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 330 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.10.2 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos MikroTik devem ser instalados de acordo com as instruções.
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-62.png)

Dependendo da antena utilizada, deve-se configurar seu ganho e a '*Installation*' para '*Indoor*' ou '*Outdoor*', dependendo do tipo de uso. Isso é para garantir que o EIRP atenda ao limite estabelecido pelas autoridades locais. Isso é feito no menu Quickset.

**Primeiro uso:**

- Este produto vem sem caixa e foi projetado para ser instalado em produtos finais ou casos de usuário. O gabinete MikroTik compatível para este produto pode ser encontrado em [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- O dispositivo vem em uma embalagem protetora contra ESD. Ao manusear equipamentos elétricos, observe as seguintes precauções de segurança:Use uma pulseira de aterramento ao desembalar e trabalhar com componentes elétricos para evitar danos por descarga elétrica (ESD);
- Após desembalar, coloque o roteador sobre o tapete antiestático;
- Ao montar a unidade, certifique-se de que não haja objetos que possam danificar ou tocar a placa PCB;
- O dispositivo pode ser montado no local desejado através dos furos fornecidos de fábrica em uma placa PCB, localizada em cada lado do dispositivo;
- Antes de conectar o dispositivo à fonte de alimentação, conecte as antenas aos conectores;
- Conecte o dispositivo à fonte de alimentação;
- Conecte seu PC à porta Ethernet;
- A configuração deve ser feita usando o navegador da Web WebFig ou a ferramenta de configuração WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Abra [http://192.168.88.1](http://192.168.88.1) em um navegador da Web para iniciar a configuração. Se o endereço IP não estiver disponível, use o WinBox e conecte-se usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique as senhas de usuário e sem fio no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Faça o upload dos pacotes baixados no menu "Files" do WinBox e reinicie o dispositivo;
- Ao atualizar o software do RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- No menu “QuickSet”, configure o modo “PTP Bridge AP” e escolha o seu país, para aplicar as configurações regulatórias do país;
- Definir um gancho de antena, dependendo da antena utilizada;
- Configure uma senha do roteador no campo inferior.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos perigos envolvidos nos circuitos elétricos e familiarize-se com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- O produto vem sem gabinete e deve ser instalado no gabinete por pessoal treinado e qualificado. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Utilize somente fonte de alimentação e acessórios aprovados pelo fabricante e que se encontram na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, conforme estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais.
- Não tente desmontar, reparar ou modificar o dispositivo. Se for necessário serviço, entre em contato com o suporte MikroTik.
- Este produto pode ser usado tanto em ambientes internos quanto externos. Leia atentamente as instruções de montagem antes de iniciar a instalação. A falha em usar o hardware e a configuração corretos ou em seguir os procedimentos corretos pode resultar em situações perigosas para as pessoas e danos ao sistema. Para instalar ao ar livre, certifique-se de usar pelo menos um gabinete com classificação IP54.
- Não podemos garantir que nenhum acidente ou dano ocorrerá devido ao uso indevido do dispositivo. Use este produto com cuidado e opere por sua conta e risco!
- A tomada deverá ser instalada próxima ao equipamento e deverá ser de fácil acesso.
- Em caso de falha do dispositivo, desconecte-o da alimentação. A maneira mais rápida de fazer isso é desconectar o adaptador de energia da tomada.
- Este é um produto Classe A. Num ambiente doméstico, este produto pode causar interferências radioeléctricas, caso em que o utilizador poderá ser obrigado a tomar medidas adequadas.
- Para evitar a contaminação do meio ambiente, separe o dispositivo do lixo doméstico e descarte-o de maneira segura, por exemplo, em áreas designadas. Familiarize-se com os procedimentos para transportar adequadamente o equipamento para pontos de coleta designados em sua área.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da FCC, IC e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 330 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.10.2 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele MikroTik trebuie instalate conform instrucțiunilor.
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-61.png)

În funcție de antena utilizată, trebuie să setați câștigul acesteia și „*Installation*” la „*Indoor*” sau „*Outdoor*”, în funcție de tipul de utilizare. Acest lucru este pentru a ne asigura că EIRP îndeplinește limita stabilită de autoritățile locale. Acest lucru se face în meniul Quickset.

**Prima utilizare:**

- Acest produs vine fără carcasă și este proiect pentru a fi instalat în produs final sau în carcasele utilisadores. Carcasa compatibilă MikroTik pentru acest produs poate fi găsită la [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Dispositiful vine în ambalaj de protecție ESD. Când manipulați echipamente electrice, vă rugăm să respectați următoarele măsuri de siguranță:Utilizați o cure de impământare pentru multetura mandeii when despachetati și workați cu componentele electrice pentru a evita deteriorarea prin electriquerea dischargea (ESD);
- Dupa despachetare, asezati routerul pe capacul antistatic;
- Când montați unitatea, asigurați-vă că există obiecte care pot deteriora PCB-ul;
- Dispositiful poate fi montat în locația dorită using orificiile furnizate din fabrică pe o placă PCB, situată pe fiecare parte a dispozitiv;
- Înainte de a conecta dispozitivul la sursa de alimentare, vă rugăm să atașați antenele la conectori;
- Conectați dispozitivul la sursa de alimentare;
- Conectați computerul la portul Ethernet;
- Configurarea trebuie efectuată cu ajutorul browserului web WebFig sau a instrumentului de configurare WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Deschideți [http://192.168.88.1](http://192.168.88.1) într-un browser web pentru a începe configurarea. Dacă adresa IP nu este disponibilă, utilizați WinBox și conectați-vă folosind adresa MAC. Numele de utilizator este "admin", și nu există parolă (sau, pentru unele modele, verificați parolele de utilizator și fără fir pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" din WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- Din meniul "QuickSet", configurați modul „PTP Bridge AP” și alegeți țara dvs., pentru a aplica setările de reglementare ale țării;
- Defina o ganho da antenna, in functie de antena folosita;
- Configurați un senha do roteador no campo inferior.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștient de pericolele implicate de circuitele electrice și familiarizați-vă cu practicile standard pentru prevenirea accidentelor. Instalatorul trebuie să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Produsul vine fără carcasă și este menit să fie instalat în carcasă de către personal instruit și calificat. Instalatorul este responsabil să se asigure că instalarea echipamentului este conformă cu codurile electrice locale și naționale. Nu încercați să dezasamblați, să reparați sau să modificați dispozitivul.
- Utilizați numai sursa de alimentare și accesoriile aprobate de producător și care se găsesc în ambalajul original al acestui produs.
- Acest echipament trebuie instalat de către personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului este conformă cu codurile electrice locale și naționale.
- Nu încercați să dezasamblați, să reparați sau să modificați dispozitivul. Dacă este nevoie de service, vă rugăm să contactați asistența MikroTik.
- Acest produs poate fi folosit atât în ​​interior, cât și în exterior. Vă rugăm să citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Neutilizarea hardware-ului și a configurației corecte sau nerespectarea procedurilor corecte poate duce la situații periculoase pentru oameni și deteriorarea sistemului. Pentru a instala în aer liber asigurați-vă că utilizați cel puțin carcasă cu rating IP54.
- Nu putem garanta că nu vor avea loc accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și operați pe propriul risc!
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.
- În cazul defecțiunii dispozitivului, vă rugăm să deconectați-l de la curent. Cel mai rapid mod de a face acest lucru este deconectarea adaptorului de alimentare de la priză.
- Acesta este un produs de clasa A. Într-un mediu domestic, acest produs poate provoca interferențe radio, caz în care utilizatorului i se poate cere să ia măsuri adecvate.
- Pentru a evita contaminarea mediului, separați dispozitivul de deșeurile menajere și aruncați-l într-un mod sigur, de exemplu, în zonele desemnate. Familiarizați-vă cu procedurile pentru transportul corespunzător a echipamentului la punctele de colectare desemnate din zona dumneavoastră.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații FCC, IC și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 330 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.10.2 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných užívateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky zariadenia MikroTik musia byť nainštalované podľa pokynov.
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-62.png)

V závislosti od použitej antény musíte nastaviť jej zisk a „*Installation*“ na „*Indoor*“ alebo „*Outdoor*“ v závislosti od typu použitia. To má zabezpečiť, aby EIRP spĺňal limit stanovený miestnymi orgánmi. Toto sa vykonáva v ponuke Quickset.

**Prvé kroky:**

- Tento produkt sa dodáva bez krytu a je navrhnutý na inštaláciu do koncových produktov alebo krytov používateľov. Kompatibilný kryt MikroTik pre tento produkt nájdete na [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Zariadenie je dodávané v ESD ochrannom obale. Pri manipulácii s elektrickým zariadením dodržiavajte nasledujúce bezpečnostné opatrenia:Pri vybaľovaní a práci s elektrickými komponentmi používajte uzemňovací pásik na zápästie, aby ste predišli poškodeniu elektrickým výbojom (ESD);
- Po vybalení položte router na antistatickú podložku;
- Pri montáži jednotky sa uistite, že v nej nie sú žiadne predmety, ktoré by mohli poškodiť alebo sa dotknúť dosky plošných spojov;
- Zariadenie je možné namontovať na požadované miesto pomocou továrenských otvorov v doske PCB, ktoré sa nachádzajú na každej strane zariadenia;
- Pred pripojením zariadenia k zdroju napájania pripojte antény ku konektorom;
- Pripojte zariadenie k zdroju napájania;
- Pripojte počítač k portu Ethernet;
- Konfiguráciu treba vykonať pomocou webového prehliadača WebFig alebo nástroja na konfiguráciu WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Otvorte [http://192.168.88.1](http://192.168.88.1) vo webovom prehliadači na spustenie nastavenia. Ak nie je k dispozícii IP adresa, použite WinBox a pripojte sa pomocou MAC adresy. Používateľské meno je "admin", a heslo nie je (alebo, pre niektoré modely, skontrolujte užívateľské a bezdrôtové heslá na štítku);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- V ponuke *"QuickSet"* nastavte režim *"PTP Bridge AP"* a vyberte svoju krajinu, aby ste použili nastavenia regulácie krajiny;
- Nastavte zisk antény v závislosti od použitej antény;
- V spodnom poli nastavte heslo smerovača.

**Bezpečnostné informácie:**

- Skôr než začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si nebezpečenstvá spojené s elektrickými obvodmi a oboznámte sa so štandardnými postupmi na predchádzanie nehodám. Inštalátor by mal poznať sieťové štruktúry, termíny a koncepty.
- Produkt sa dodáva bez krytu a je určený na inštaláciu do krytu vyškoleným a kvalifikovaným personálom. Inštalatér je zodpovedný za uistenie sa, že inštalácia zariadenia je v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v originálnom balení tohto produktu.
- Toto zariadenie musí inštalovať vyškolený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalačný technik je zodpovedný za uistenie sa, že inštalácia zariadenia je v súlade s miestnymi a národnými elektrickými predpismi.
- Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať. Ak je potrebný servis, kontaktujte podporu MikroTik.
- Tento produkt je možné použiť v interiéri aj exteriéri. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Nepoužitie správneho hardvéru a konfigurácie alebo nedodržanie správnych postupov môže viesť k nebezpečnej situácii pre ľudí a poškodeniu systému. Pri inštalácii vonku sa uistite, že používate kryt s krytím aspoň IP54.
- Nemôžeme zaručiť, že v dôsledku nesprávneho používania zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento produkt používajte opatrne a prevádzkujte na vlastné riziko!
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejší spôsob, ako to urobiť, je odpojiť napájací adaptér zo zásuvky.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie, v takom prípade môže byť potrebné, aby používateľ prijal primerané opatrenia.
- Aby ste predišli kontaminácii životného prostredia, oddeľte zariadenie od domáceho odpadu a zlikvidujte ho bezpečným spôsobom, napríklad na vyhradených miestach. Oboznámte sa s postupmi správnej prepravy zariadenia na určené zberné miesta vo vašej oblasti.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu FCC, IC a Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 330 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.10.2 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so dolžni upoštevati lokalne predpise, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse naprave MikroTik morajo biti nameščene v skladu z navodili.
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-62.png)

Odvisno od uporabljene antene, morate nastaviti njeno ojačanje in '*Installation*' na '*Indoor*' ali '*Outdoor*', odvisno od vrste uporabe. S tem zagotovimo, da EIRP ustreza omejitvi, ki so jo določile lokalne oblasti. To naredite v meniju Quickset.

**Prvi koraki:**

- Ta izdelek je na voljo brez ohišja in je zasnovan za vgradnjo v končne izdelke ali ohišja uporabnikov. Združljivo ohišje MikroTik za ta izdelek lahko najdete na [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Naprava je v ESD zaščitni embalaži. Pri ravnanju z električno opremo upoštevajte naslednje varnostne ukrepe:Pri razpakiranju in delu z električnimi komponentami uporabljajte zapestni ozemljitveni trak, da preprečite poškodbe zaradi električne razelektritve (ESD);
- Po razpakiranju postavite usmerjevalnik na antistatično podlogo;
- Pri nameščanju enote se prepričajte, da ni nobenih predmetov, ki bi lahko poškodovali ali se dotaknili plošče PCB;
- Napravo lahko namestite na želeno mesto s pomočjo tovarniško predvidenih lukenj v plošči PCB, ki se nahajajo na vsaki strani naprave;
- Preden napravo priključite na vir napajanja, priključite antene na priključke;
- Priključite napravo na vir napajanja;
- Priključite računalnik na vrata Ethernet;
- Konfiguracijo je treba izvesti s pomočjo spletnega brskalnika WebFig ali orodja za konfiguracijo WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Odpri [http://192.168.88.1](http://192.168.88.1) v spletnem brskalniku, da začneš s postavitvijo. Če IP naslov ni na voljo, uporabi WinBox in se poveži prek MAC naslova. Uporabniško ime je "admin", in ni gesla (ali, za nekatere modele, preveri uporabniška in brezžična gesla na nalepki);
- Kliknite na gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" v WinBoxu in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico zagotovite optimalne zmogljivosti, stabilnost in varnostne posodobitve;
- V meniju *"QuickSet"* nastavite način *"PTP Bridge AP"* in izberite svojo državo, da uporabite nastavitve državnih predpisov;
- Nastavite ojačanje antene glede na uporabljeno anteno;
- V spodnjem polju nastavite geslo usmerjevalnika.

**Varnostne informacije:**

- Preden začnete delati na kateri koli opremi MikroTik, se zavedajte nevarnosti, povezanih z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Izdelek je na voljo brez ohišja in je namenjen za vgradnjo v ohišje s strani usposobljenega in kvalificiranega osebja. Monter je odgovoren za zagotovitev, da je namestitev opreme skladna z lokalnimi in nacionalnimi električnimi predpisi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Uporabljajte le napajalnik in dodatke, ki jih je odobril proizvajalec in jih najdete v originalni embalaži tega izdelka.
- To opremo mora namestiti usposobljeno in kvalificirano osebje v skladu s temi navodili za namestitev. Monter je odgovoren za zagotovitev, da je namestitev opreme skladna z lokalnimi in nacionalnimi električnimi predpisi.
- Naprave ne poskušajte razstaviti, popraviti ali spremeniti. Če potrebujete servis, se obrnite na podporo MikroTik.
- Ta izdelek se lahko uporablja tako v zaprtih prostorih kot na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba pravilne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarno situacijo za ljudi in škodo na sistemu. Za namestitev na prostem se prepričajte, da uporabljate vsaj ohišje z oznako IP54.
- Ne moremo zagotoviti, da zaradi nepravilne uporabe naprave ne bo prišlo do nesreč ali škode. Prosimo, uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.
- V primeru okvare naprave jo izključite iz napajanja. Najhitreje to storite tako, da napajalnik izključite iz vtičnice.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru pa bo uporabnik morda moral ustrezno ukrepati.
- Da preprečite onesnaženje okolja, ločite napravo od gospodinjskih odpadkov in jo odvrzite na varen način, na primer na za to namenjenih območjih. Seznanite se s postopki za pravilen prevoz opreme do določenih zbirnih mest na vašem območju.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju FCC, IC in Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 330 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10.2 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-enheter måste installeras enligt instruktionerna.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-62.png)

Beroende på vilken antenn som används måste du ställa in dess förstärkning och '*Installation*' till '*Indoor*' eller '*Outdoor*', beroende på användningstyp. Detta för att säkerställa att EIRP uppfyller den gräns som de lokala myndigheterna har satt. Detta görs i snabbinställningsmenyn.

**Första stegen:**

- Denna produkt kommer utan kapsling och är designad för att installeras i användarens slutprodukter eller kapslingar. Kompatibel MikroTik-kapsling för denna produkt finns på [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Enheten kommer i ESD-skyddande förpackning. Vid hantering av elektrisk utrustning vänligen observera följande säkerhetsföreskrifter:Använd ett jordningsband för handleden när du packar upp och arbetar med elektriska komponenter för att undvika skador på elektrisk urladdning (ESD);
- Efter uppackning, placera routern på den antistatiska mattan;
- När du monterar enheten se till att det inte finns några föremål som kan skada eller vidröra PCB-plattan;
- Enheten kan monteras på önskad plats med hjälp av de fabriksförsedda hålen i en PCB-platta, placerad på varje sida av enheten;
- Innan du ansluter enheten till strömkällan, vänligen anslut antennerna till kontakterna;
- Anslut enheten till strömkällan;
- Anslut din dator till Ethernet-porten;
- Konfigurationen bör göras med hjälp av webbläsaren WebFig eller konfigurationsverktyget WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Öppna [http://192.168.88.1](http://192.168.88.1) i en webbläsare för att starta uppställningen. Om IP-adressen inte är tillgänglig, använd WinBox och anslut med MAC-adressen. Användarnamnet är "admin", och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WinBox "Files" -menyn och starta om enheten;
- Genom att uppdatera RouterOS-programvaran till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I *"QuickSet" -* menyn, ställ in *"PTP Bridge AP" -* läget och välj ditt land för att tillämpa inställningarna för landsbestämmelser;
- Ställ in antennförstärkningen, beroende på vilken antenn som används;
- Ställ in ditt routerlösenord i det nedre fältet.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning, var medveten om farorna med elektriska kretsar och bekanta dig med standardpraxis för att förebygga olyckor. Installatören bör vara bekant med nätverksstrukturer, termer och koncept.
- Produkten levereras utan kapsling och är avsedd att installeras i kapslingen av utbildad och kvalificerad personal. Installatören är ansvarig för att se till att installationen av utrustningen är förenlig med lokala och nationella elektriska bestämmelser. Försök inte att plocka isär, reparera eller modifiera enheten.
- Använd endast strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen till denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören är ansvarig för att se till att installationen av utrustningen följer lokala och nationella elregler.
- Försök inte att plocka isär, reparera eller modifiera enheten. Om service behövs, kontakta MikroTik support.
- Denna produkt kan användas både inomhus och utomhus. Läs monteringsinstruktionerna noggrant innan du påbörjar installationen. Underlåtenhet att använda rätt hårdvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på systemet. För att installera utomhus, se till att använda minst IP54-klassade kapsling.
- Vi kan inte garantera att inga olyckor eller skador inträffar på grund av felaktig användning av enheten. Använd den här produkten med försiktighet och använd på egen risk!
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.
- I händelse av fel på enheten, koppla bort den från strömmen. Det snabbaste sättet att göra det är genom att koppla ur nätadaptern från eluttaget.
- Detta är en klass A-produkt. I en hemmiljö kan denna produkt orsaka radiostörningar i vilket fall användaren kan behöva vidta lämpliga åtgärder.
- För att undvika kontaminering av miljön, separera enheten från hushållsavfallet och kassera den på ett säkert sätt, till exempel i avsedda områden. Bekanta dig med procedurer för korrekt transport av utrustningen till utsedda uppsamlingsplatser i ditt område.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med FCC, IC och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 330 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.10.2或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须根据说明安装所有MikroTik设备。
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*有关产品的技术规格，手册和更多信息， 请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请寻求顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-62.png)

根據使用的天線，您必須將其增益和“*Installation*”設置為“*Indoor*”或“*Outdoor*”，具體取決於使用類型。這是為了確保 EIRP 滿足地方當局設定的限制。這是在快速設置菜單中完成的。

**首次使用：**

- 该产品不带外壳，设计用于安装到用户的最终产品或外壳中。可在[https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures) 找到与本产品兼容的 MikroTik 外壳
- 该设备采用 ESD 防护包装。处理电气设备时，请遵守以下安全预防措施:打开包装和操作电气元件时，请使用接地腕带，以避免放电 (ESD) 损坏；
- 打开包装后请将路由器放置在防静电垫上；
- 安装设备时，确保没有任何物体会损坏或接触 PCB 板；
- 可以使用位于设备两侧的 PCB 板上工厂提供的孔将设备安装在您所需的位置；
- 在将设备连接到电源之前，请将天线连接到连接器上；
- 将设备连接至电源；
- 将您的 PC 连接到以太网端口；
- 配置应使用WebFig浏览器或WinBox配置工具[https://mt.lv/WinBox](https://mt.lv/WinBox) 完成; **提供多种配置方法以确保可访问性；**
- 在Web浏览器中打开[http://192.168.88.1](http://192.168.88.1) 以开始设置。如果IP地址不可用，请使用WinBox并使用MAC地址连接。用户名为“admin”，没有密码（或者对于某些型号，请检查标签上的用户和无线密码）;
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WinBox的"Files"菜单并重新启动设备;
- 通过将RouterOS软件更新到最新版本，您可以确保最佳性能，稳定性和安全更新;
- 在 *"QuickSet"* 菜单中设置 *"PTP Bridge AP"* 模式，选择你的国家，应用国家法规设置；
- 根据使用的天线设置天线增益；
- 在底部字段中设置您的路由器密码。

**安全信息：**

- 在使用任何 MikroTik 设备之前，请注意电路所涉及的危险，并熟悉预防事故的标准做法。安装人员应熟悉网络结构、术语和概念。
- 该产品不带外壳，应由经过培训的合格人员安装到外壳中。安装人员负责确保设备的安装符合当地和国家电气规范。请勿尝试拆卸、修理或改装设备。
- 仅使用制造商认可的电源和配件，这些可在本产品的原包装中找到。
- 该设备应由经过培训的合格人员按照这些安装说明进行安装。安装人员负责确保设备的安装符合当地和国家电气规范。
- 请勿尝试拆卸、修理或改装设备。如果需要服务，请联系 MikroTik 支持。
- 该产品可在室内和室外使用。开始安装前请仔细阅读安装说明。未能使用正确的硬件和配置或遵循正确的程序可能会导致人员面临危险并损坏系统。要在室外安装，请确保使用至少 IP54 等级的外壳。
- 我们不能保证不会因设备使用不当而发生事故或损坏。请谨慎使用本产品，操作风险自负！
- 插座应安装在设备附近并易于插拔。
- 如果设备发生故障，请断开电源。最快的方法是从电源插座上拔下电源适配器。
- 这是 A 类产品。在家庭环境中，本产品可能会造成无线电干扰，在这种情况下，用户可能需要采取适当的措施。
- 为避免污染环境，请将设备与生活垃圾分开并以安全方式进行处理，例如在指定区域进行处理。熟悉将设备正确运输到您所在地区指定收集点的程序。

**射频辐射暴露：** 此MikroTik设备符合针对不受控制的环境所设定的FCC，IC和欧盟辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业用户或公众的距离不得超过330厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.10.2 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все устройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru) чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-61.png)

В зависимости от используемой антенны вы должны установить ее усиление и «*Installation*» на «*Indoor*» или «*Outdoor*», в зависимости от типа использования. Это делается для того, чтобы EIRP соответствовал пределу, установленному местными властями. Делается это в меню Quickset.

**Первые шаги:**

- Этот продукт поставляется без корпуса и предназначен для установки в конечные продукты или корпуса пользователей. Совместимый корпус MikroTik для этого продукта можно найти по адресу [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures).
- Устройство поставляется в упаковке с защитой от электростатического разряда. При обращении с электрооборудованием соблюдайте следующие меры предосторожности:Используйте заземляющий браслет при распаковке и работе с электрическими компонентами, чтобы избежать повреждения электрическим разрядом (ESD);
- После распаковки поместите маршрутизатор на антистатический коврик;
- При монтаже устройства убедитесь, что нет предметов, которые могут повредить или коснуться платы печатной платы;
- Устройство можно установить в желаемом месте, используя предусмотренные на заводе отверстия в пластине печатной платы, расположенные с каждой стороны устройства;
- Перед подключением устройства к источнику питания, подключите антенны к разъемам;
- Подключите устройство к источнику питания;
- Подключите компьютер к порту Ethernet;
- Конфигурация должна выполняться с использованием веб-браузера WebFig или инструмента конфигурации WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **существует несколько методов настройки для обеспечения доступности;**
- Откройте [http://192.168.88.1](http://192.168.88.1) в веб-браузере, чтобы начать настройку. Если IP-адрес недоступен, используйте WinBox и подключитесь, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте пользовательские и беспроводные пароли на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню *"QuickSet"* настройте режим *"PTP Bridge AP"* и выберите свою страну, чтобы применить настройки регулирования страны;
- Установите коэффициент усиления антенны в зависимости от используемой антенны;
- Установите пароль маршрутизатора в нижнем поле.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Храните этот продукт вдали от воды, огня, влажности или жарких сред.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.
- В домашних условиях этот продукт может вызывать радиопомехи, и в этом случае пользователю может потребоваться принять адекватные меры.
- Это продукт класса А. В домашних условиях этот продукт может вызвать радиопомехи, и в этом случае пользователю может потребоваться принять соответствующие меры.

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
Воздействие радиочастотного излучения. *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 330 сантиметров от человека.*

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 5150-5350 МГц, 5650-5850 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Производитель: Mikrotikls SIA, ул. Униас, 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. Cм. на упаковке.

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.
Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](./img/image2020-1-24_7-55-5.badge-62.png)

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.10.2 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help-ua](https://mt.lv/help-ua)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-20.png)

Залежно від використовуваної антени, ви повинні встановити її коефіцієнт підсилення та параметр «*Installation*» на «*Indoor*» або «*Outdoor*», залежно від типу використання. Це необхідно для того, щоб EIRP відповідав ліміту, встановленим місцевою владою. Це робиться в меню Quickset.

**Перші кроки:**

- Цей продукт поставляється без корпусу та призначений для встановлення в кінцеві продукти або корпуси користувачів. Сумісний корпус MikroTik для цього продукту можна знайти за адресою [https://mikrotik.com/products/group/enclosures](https://mikrotik.com/products/group/enclosures)
- Пристрій поставляється в антистатичній упаковці. Під час роботи з електричним обладнанням дотримуйтесь наступних заходів безпеки:Використовуйте ремінець заземлення під час розпакування та роботи з електричними компонентами, щоб уникнути пошкодження електричним розрядом (ESD);
- Після розпакування покладіть маршрутизатор на антистатичний килимок;
- Під час монтажу пристрою переконайтеся, що немає предметів, які можуть пошкодити або торкнутися пластини друкованої плати;
- Пристрій можна встановити у бажаному місці за допомогою заводських отворів у пластині друкованої плати, розташованих з кожного боку пристрою;
- Перед підключенням пристрою до джерела живлення, приєднайте антени до роз’ємів;
- Підключіть пристрій до джерела живлення;
- Підключіть ПК до порту Ethernet;
- Конфігурацію слід виконувати за допомогою веб-браузера WebFig або інструменту конфігурації WinBox [https://mt.lv/WinBox](https://mt.lv/WinBox); **існує декілька методів налаштування для забезпечення доступності;**
- Відкрийте [http://192.168.88.1](http://192.168.88.1) в веб-браузері, щоб розпочати налаштування. Якщо IP-адреса немає, використовуйте WinBox та підключіться за допомогою MAC-адреси. Ім'я користувача - "admin", і пароля немає (або, для деяких моделей, перевірте паролі користувачів та бездротові паролі на етикетці);
- Натисніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" WinBox та перезапустіть пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- У меню *"QuickSet"* встановіть режим *"PTP Bridge AP"* і виберіть свою країну, щоб застосувати налаштування регулювані у вашій країні;
- Встановіть рівень посилення антени залежно від використовуваної антени;
- У нижньому полі встановіть пароль маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Продукт постачається без корпусу та призначений для встановлення в корпус навченим та кваліфікованим персоналом.
- Використовуйте лише джерело живлення та аксесуари, схвалені виробником і які можна знайти в оригінальній упаковці цього продукту.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам.
- Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій. Якщо потрібне обслуговування, зверніться до служби підтримки MikroTik.
- Цей продукт можна використовувати як у приміщенні, так і на вулиці. Перед початком монтажу уважно прочитайте інструкції з монтажу. Невикористання відповідного обладнання або недотримання правильних процедур може призвести до небезпеки для людей та пошкодження системи. Для встановлення на відкритому повітрі обов’язково використовуйте корпус із рейтингом не менше IP54.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- У разі несправності пристрою відключіть його від живлення. Найшвидший спосіб зробити це — від’єднати адаптер живлення від розетки.
- Це продукт класу А. У домашньому середовищі цей продукт може спричиняти радіоперешкоди, і в цьому випадку користувачеві може знадобитися вжити відповідних заходів.
![](./img/ua.badge-22.jpg)
- Щоб уникнути забруднення навколишнього середовища, відокремте пристрій від побутових відходів і утилізуйте його безпечним способом, наприклад, у спеціально відведених місцях. Ознайомтеся з процедурами належного транспортування обладнання до призначених пунктів збору у вашому регіоні.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення FCC, IC та Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 5150-5250 МГц (23 дБм); 5250-5350 МГц (20 дБм); 5470-5725 МГц (27дБм).

Справжнім Mikrotikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## Federal Communication Commission Interference Statement

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.
![](./img/fcc_logo_ez.badge-54.jpg)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 330 centimeters from your body, occupational user, or the general public.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC and IC radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 330 centimeters from your body, occupational user, or the general public.

**Exposition aux rayonnements radiofréquences:** Cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements FCC et IC établies pour un environnement non contrôlé. Cet appareil MikroTik ne doit pas être installé et utilisé à moins de 330 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

## UKCA marking

![](./img/ukca_black_fill.badge-60.gif)

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
      
      5150-5250 MHz / 23 dBm (only for RB911-5HacD)
    
    5250-5350 MHz / 20 dBm (only for RB911-5HacD)
    5470-5725 MHz / 27 dBm
  

:::warning
This MikroTik device meets Maximum transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen Sendeleistung Grenzwerte gemäß ETSI-Vorschriften. Weitere Informationen finden Sie oben in der Konformitätserklärung / Cet appareil MikroTik respecte les limites de puissance de transmission maximale conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti di potenza massima di trasmissione in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los valores límite de potencia máxima de transmisión de acuerdo con la normativa ETSI. Para obtener información más detallada, consulte la Declaración de conformidad anterior / Это устройство MikroTik соответствует предельным значениям максимальной мощности передачи в соответствии с правилами ETSI. Для получения более подробной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](./img/picto-14.png)
:::

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

RB911G-5HPnD: DC Jack (8-28 V DC),PoE In Ethernet Port (8-28 V DC);RB911-5Hn: PoE In Ethernet (8-30 V DC);RB912UAG-5HPnD, RB922UAGS-5HPacD,RB911G-5HPacD: DC Jack (8-30 V DC),PoE In Ethernet Port (8-30 V DC);RB911-5HnD: PoE In Ethernet (6-30 V DC);RB911-5HacD: PoE In Ethernet (10-30 V DC)
-
-40°..+70°C

\#73356
