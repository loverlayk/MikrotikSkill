# Quick Guide - nRAY series

> Models: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY)

**Models: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY)**

![](./img/mt_logo_arrow_v2-02-90.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.10 or the latest stable version, to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

*This "nRAY" series Quick Guide covers models: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).*

*This is a wireless network device. You can find the product model name on the case label (ID).*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Please visit the user manual page on [[https://mt.lv/um](https://mt.lv/um)](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [[https://mt.lv/help](https://mt.lv/help)](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-103.png)

**First steps:**

- Take the Ethernet port cover from the package;
- Guide Ethernet cable through the opening;
- Plug into the Ethernet port and screw clockwise tightly, to ensure water protection;
- Connect the PoE injector into the computer;
- Connect the power adapter to the PoE injector;
- Download WinBox configuration tool [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Default IP: 192.168.88.1, user name: *admin* and there is no password, for the paired models IP: 192.168.88.2/192.168.88.3, please find the password on the sticker;
- Once connected, configure the device, so it has an active Internet connection https://mt.lv/configuration;
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update, visit the products page at [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) to find your product. The required packages are accessible under the "Support&Downloads" menu;
- Upload downloaded packages to the Winbox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Connect again and select your Region in the Wireless menu, W60G tab, to apply country regulation settings;
- For *nRAY 60G* models, set up your router password in the QuickSet menu, to the right and repeat it, it will be used to log in next time.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be mounted outdoors on a pole but can also be installed indoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 53 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.10 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Моля, посетете страницата с ръководството за потребителя на [[https://mt.lv/um-bg](https://mt.lv/um-bg)](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Технически спецификации, брошури и повече информация за продуктите на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [[https://mt.lv/help-bg](https://mt.lv/help-bg)](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигуриране, моля, потърсете консултант [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-98.png)

**Първи стъпки:**

- Вземете капака на Ethernet порт от пакета;
- Направляващ отвор за Ethernet кабел през отвора;
- Включете Ethernet порта и завийте плътно по посока на часовниковата стрелка, за да осигурите защита от вода;
- Свържете PoE инжектора в компютъра;
- Свържете захранващия адаптер към PoE инжектора;
- Изтеглете инструмент за конфигуриране на WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP по подразбиране: 192.168.88.1, потребителско име: *admin* и няма парола, за сдвоените модели IP: 192.168.88.2/192.168.88.3, моля, намерете паролата на стикера;
- Веднъж свързан конфигурира устройството, така че то има активна интернет връзка https://mt.lv/configuration-bg;
- Кликнете на бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчна актуализация, посетете страницата с продукти на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), за да намерите вашия продукт. Необходимите пакети са достъпни в менюто "Support&Downloads";
- Качете изтеглените пакети в менюто "Files" на Winbox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- Свържете се отново и изберете региона си в менюто Wireless, W60G, за да приложите настройките за регулиране на страната;
- За единични модели задайте паролата на рутера в менюто QuickSet вдясно и я повторете, ще използвате d за влизане следващия път.

**Информация за безопасност:**

- Преди да работите с което и да е оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за монтиране на открито върху стълб, но може да се монтира и на закрито. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате корективни тон и хардуерната конфигурация или да се следват правилните процедури биха могли да доведат до опасна ситуация за хората и повреда на систем м.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, като в този случай от потребителя може да се наложи да предприеме адекватни мерки!

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 53 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.10 nebo na nejnovější stabilní verzi!
Je na konečném uživateli, aby dodržoval místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
Tento Stručný průvodce „nRAY“ zahrnuje modely: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [[https://mt.lv/um-cs](https://mt.lv/um-cs)](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Technické specifikace, brožury a další informace o produktech na adrese [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [[https://mt.lv/help-cs](https://mt.lv/help-cs)](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-98.png)

**První kroky:**

- Vezměte kryt ethernetového portu z balíčku;
- Vedení ethernetového kabelu skrz otevření;
- Připojte se k portu Ethernet a pevně přišroubujte ve směru hodinových ručiček, abyste zajistili ochranu vody;
- Připojte injektor PoE k počítači;
- Připojte napájecí adaptér k injektoru PoE;
- Stáhněte si konfigurační nástroj WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Výchozí IP: 192.168.88.1, uživatelské jméno: *admin* a neexistuje žádné heslo, u spárovaných modelů IP: 192.168.88.2/192.168.88.3 najdete heslo na nálepce;
- Po připojení nakonfigurujte zařízení tak, aby mělo aktivní připojení k internetu https://mt.lv/configuration-cs;
- Klepněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro ruční aktualizaci navštivte stránku produktů na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), abyste našli váš produkt. Požadované balíčky jsou dostupné v menu "Support&Downloads";
- Nahrajte stáhnuté balíčky do menu "Files" ve Winboxu a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- Připojte se znovu a vyberte svůj region v nabídce Wireless připojení, karta W60G, pro použití nastavení regulace země;
- U jednotlivých modelů nastavte heslo routeru v nabídce QuickSet napravo a opakujte jej, při příštím přihlášení se použije d.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k montáži venku na sloup, ale lze jej instalovat i uvnitř. Před zahájením instalace si pozorně přečtěte montážní pokyny. Selhání použít Korekce t konfiguraci hardwaru a nebo dodržet správný postup může vést k nebezpečným situacím pro lidi a poškození syst m.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Toto je produkt třídy A. V domácím prostředí může tento produkt způsobovat rádiové rušení. V takovém případě může být uživatel požádán, aby přijal odpovídající opatření!

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno blíže než 53 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.10 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [[https://mt.lv/um-da](https://mt.lv/um-da)](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, brochurer og mere info om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [[https://mt.lv/help-da](https://mt.lv/help-da)](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, bedes du kontakte en konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-98.png)

**Første trin:**

- Tag Ethernet-portdækslet fra pakken;
- Guide Ethernet-kabel gennem åbning;
- Tilslut Ethernet-porten og skru med uret med uret for at sikre vandbeskyttelse;
- Tilslut PoE-injektoren til computeren;
- Tilslut strømadapteren til PoE-injektoren;
- Download WinBox-konfigurationsværktøj [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Standard IP: 192.168.88.1, brugernavn: *admin* og der er ingen adgangskode, for de parrede modeller IP: 192.168.88.2/192.168.88.3 skal du finde adgangskoden på klistermærket;
- Når først enheden er tilsluttet, konfigureres enheden, så den har en aktiv internetforbindelse https://mt.lv/configuration-da;
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- Til en manuel opdatering af enheden, besøg produktsiden på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) for at finde dit produkt. De påkrævede pakker er tilgængelige under menuen "Support&Downloads";
- Overfør de downloadede pakker til Winbox "Files" menuen og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Forbind igen og vælg din region i menuen Wireless, fanen W60G, for at anvende indstillinger for landegulering;
- For enkeltmodeller skal du indstille din routeradgangskode i QuickSet-menuen til højre og gentage den. Den bruges d til at logge ind næste gang.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive monteret udendørs på en stang, men kan også installeres indendørs. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og skade på syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger!

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 53 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.10 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*

*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [[https://mt.lv/um-de](https://mt.lv/um-de)](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [[https://mt.lv/help-de](https://mt.lv/help-de)](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-98.png)

**Erste Schritte:**

- Nehmen Sie die Ethernet-Anschlussabdeckung aus der Verpackung;
- Führung des Ethernet-Kabels durch die Öffnung;
- Schließen Sie den Ethernet-Anschluss an und schrauben Sie ihn fest im Uhrzeigersinn, um den Wasserschutz zu gewährleisten;
- Schließen Sie den PoE-Injektor an den Computer an;
- Schließen Sie das Netzteil an den PoE-Injektor an;
- Laden Sie das WinBox-Konfigurationstool [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox) herunter;
- Standard-IP: 192.168.88.1, Benutzername: *admin* und es gibt kein Passwort. Für die gekoppelten Modelle IP: 192.168.88.2/192.168.88.3 finden Sie das Passwort auf dem Aufkleber;
- Sobald die Verbindung hergestellt ist, konfigurieren Sie das Gerät so, dass eine aktive Internetverbindung besteht. Https://mt.lv/configuration-de
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update besuchen Sie die Produktseite unter [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), um Ihr Produkt zu finden. Die erforderlichen Pakete finden Sie im Menü "Support&Downloads";
- Laden Sie die heruntergeladenen Pakete in das Menü "Files" von Winbox hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Stellen Sie erneut eine Verbindung her und wählen Sie Ihre Region im Menü Wireless auf der Registerkarte W60G aus, um die Länderregulierungseinstellungen anzuwenden;
- Richten Sie für einzelne Modelle Ihr Router-Passwort im QuickSet-Menü rechts ein und wiederholen Sie es. Beim nächsten Anmelden wird es mit d verwendet.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Montage im Freien an einer Stange vorgesehen, kann aber auch im Innenbereich installiert werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wird die correc zu verwenden t - Hardware und Konfiguration oder die richtigen Verfahren zu folgen in einer Gefahrensituation für Menschen und Schäden an den Syste führen könnten m.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen!

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 53 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.10 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
Αυτός ο γρήγορος οδηγός σειράς "nRAY" καλύπτει μοντέλα: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [[https://mt.lv/um-el](https://mt.lv/um-el)](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [[https://mt.lv/help-el](https://mt.lv/help-el)](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια σχετικά με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-98.png)

**Πρώτα βήματα:**

- Πάρτε το κάλυμμα της θύρας Ethernet από το πακέτο;
- Οδηγός ανοίγματος μέσω καλωδίου Ethernet;
- Συνδέστε τη θύρα Ethernet και βιδώστε σφιχτά δεξιόστροφα, για να διασφαλίσετε την προστασία του νερού;
- Συνδέστε τον εγχυτήρα PoE στον υπολογιστή;
- Συνδέστε το τροφοδοτικό στον εγχυτήρα PoE;
- Λήψη του εργαλείου διαμόρφωσης WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Προεπιλεγμένη διεύθυνση IP: 192.168.88.1, όνομα χρήστη: *διαχειριστής* και δεν υπάρχει κωδικός πρόσβασης, για τα ζευγαρωμένα μοντέλα IP: 192.168.88.2/192.168.88.3, βρείτε τον κωδικό πρόσβασης στο αυτοκόλλητο;
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Αναβαθμίστε το λογισμικό RouterOS στην πιο πρόσφατη έκδοση https://mt.lv/upgrade-el;
- Για μη αυτόματη ενημέρωση της συσκευής, επισκεφτείτε τη σελίδα προϊόντων στο [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) για να βρείτε το προϊόν σας. Τα απαιτούμενα πακέτα είναι προσβάσιμα στο μενού "Support&Downloads";
- Ανεβάστε τα κατεβασμένα πακέτα στο μενού "Files" του Winbox και επανεκκινήστε τη συσκευή;
- Με την αναβάθμιση του λογισμικού RouterOS στην τελευταία έκδοση, μπορείτε να διασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Συνδεθείτε ξανά και επιλέξτε την περιοχή σας στο μενού Wireless, καρτέλα W60G, για να εφαρμόσετε τις ρυθμίσεις κανονισμού χώρας;
- Για μεμονωμένα μοντέλα, ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο μενού QuickSet, στα δεξιά και επαναλάβετε τον, θα χρησιμοποιηθεί d για να συνδεθείτε την επόμενη φορά.

**Πληροφορίες ασφάλειας:**

- Προτού εργαστείτε σε οποιονδήποτε εξοπλισμό MikroTik, προσέξτε τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο το τροφοδοτικό και τα αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για να βεβαιωθεί ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κωδικούς. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επισκευάσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν προορίζεται να τοποθετηθεί σε εξωτερικούς χώρους σε στύλο, αλλά μπορεί επίσης να εγκατασταθεί σε εσωτερικούς χώρους. Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η αποτυχία να χρησιμοποιήσει το correc t υλικού και τη διαμόρφωση ή να ακολουθήσουν οι σωστές διαδικασίες θα μπορούσε να οδηγήσει σε μια επικίνδυνη κατάσταση για τους ανθρώπους και να βλάψει την syste μ.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο γρηγορότερος τρόπος για να το κάνετε είναι αποσυνδέοντας το τροφοδοτικό από την πρίζα.
- Αυτό είναι προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει παρεμβολές ραδιοφώνου, οπότε ενδέχεται να απαιτείται από τον χρήστη να λάβει επαρκή μέτρα!

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 53 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.10 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*

*Visite la página del manual del usuario en [[https://mt.lv/um-es](https://mt.lv/um-es)](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [[https://mt.lv/help-es](https://mt.lv/help-es)](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-100.png)

**Primeros pasos:**

- Saque la tapa del puerto Ethernet del paquete;
- Guía de apertura del canal del cable Ethernet;
- Enchúfelo en el puerto Ethernet y atorníllelo en sentido horario, para garantizar la protección del agua;
- Conecte el inyector PoE a la computadora;
- Conecte el adaptador de corriente al inyector PoE;
- Descargue la herramienta de configuración de WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP predeterminada: 192.168.88.1, nombre de usuario: *admin* y no hay contraseña, para los modelos emparejados IP: 192.168.88.2/192.168.88.3, busque la contraseña en la etiqueta;
- Una vez conectado, configure el dispositivo para que tenga una conexión a Internet activa https://mt.lv/configuration-es;
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para una actualización manual del dispositivo, visite la página de productos en [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) para encontrar su producto. Los paquetes necesarios están disponibles en el menú "Support&Downloads";
- Cargue los paquetes descargados en el menú "Files" de Winbox y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- Conéctese nuevamente y seleccione su Región en el menú Wireless, pestaña W60G, para aplicar la configuración de la regulación del país;
- Para modelos individuales, configure la contraseña de su enrutador en el menú QuickSet, a la derecha y repítala, se usará d para iniciar sesión la próxima vez.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desarmar, reparar o modificar el dispositivo.
- Este producto está diseñado para montarse en exteriores en un poste, pero también puede instalarse en interiores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza la correc t hardware y configuración o de seguir los procedimientos correctos podrían dar lugar a una situación de peligro a las personas y daños a la syste m.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Este es un producto de clase A. ¡En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas!

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 53 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

**Información México:**

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
See "nRAY" seeria lühijuhend hõlmab mudeleid: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [[https://mt.lv/um-et](https://mt.lv/um-et)](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [[https://mt.lv/help-et](https://mt.lv/help-et)](https://mt.lv/help-et)*
*Kui vajate konfigureerimisel abi, pöörduge konsultandi poole [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-98.png)

**Esimesed sammud:**

- Võtke pakendilt Etherneti pordi kate;
- Juht Etherneti kaabli läbiva ava;
- Ühendage Etherneti pordiga ja keerake veekaitse tagamiseks tihedalt päripäeva;
- Ühendage PoE-injektor arvutiga;
- Ühendage toiteadapter PoE-injektoriga;
- Laadige alla WinBoxi seadistusriist [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Vaikimisi IP: 192.168.88.1, kasutajanimi: *admin* ja parooli pole, paaritud mudelite IP: 192.168.88.2/192.168.88.3 jaoks leidke parool kleebiselt;
- Pärast ühenduse loomist seadistage seade, nii et sellel on aktiivne Interneti-ühendus https://mt.lv/configuration-et;
- Klõpsake nupul "Check for updates" ja ajakohastage RouterOS viimasele versioonile;
- Käsitsi seadme värskendamiseks külastage toodete lehte aadressil [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), et leida oma toode. Vajalikud paketid on saadaval menüüs "Support&Downloads";
- Laadige alla laaditud paketid Winboxi "Files" menüüsse ja taaskäivitage seade;
- Värskendades oma RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Ühendage uuesti ja valige raadiosidemenüü Wireless, W60G oma piirkond, et rakendada riigi reguleerimise sätteid;
- Üksikute mudelite korral seadke oma ruuteri parool menüüst QuickSet paremale ja korrake seda, järgmine kord sisselogimiseks kasutatakse d nuppu.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud monteerimiseks välistingimustes, kuid seda saab paigaldada ka siseruumides. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Kasutamata jätmine correc t riistvara ja konfiguratsiooni või järgiks õigeid menetlusi võib põhjustada ohtlikke olukordi inimestele ja kahjustada kõrvamonitori m.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- See on A-klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid - sel juhul võidakse kasutajalt nõuda asjakohaste meetmete võtmist!

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 53 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.10 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
Tämä "nRAY" -sarjan pikaopas kattaa mallit: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [[https://mt.lv/um-fi](https://mt.lv/um-fi)](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [[https://mt.lv/help-fi](https://mt.lv/help-fi)](https://mt.lv/help-fi)*
*Jos tarvitset ohjeita konfiguroinnissa, kysy neuvoa [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-98.png)

**Ensiaskeleet:**

- Ota Ethernet-portin kansi pakkauksesta;
- Ohjaa Ethernet-kaapelin läpi aukko;
- Kytke Ethernet-porttiin ja ruuvaa myötäpäivään tiukasti veden suojauksen varmistamiseksi;
- Kytke PoE-injektori tietokoneeseen;
- Kytke verkkolaite PoE-injektoriin;
- Lataa WinBox-määritystyökalu [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Oletus-IP: 192.168.88.1, käyttäjänimi: *admin* ja salasanaa ei ole. Paritut mallit IP: 192.168.88.2/192.168.88.3 löytyvät tarrasta;
- Kun yhteys on muodostettu, määritä laite, joten sillä on aktiivinen Internet-yhteys https://mt.lv/configuration-fi;
- Napsauta "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Manuaalista päivitystä varten vieraile tuotesivulla osoitteessa [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) löytääksesi tuotteesi. Tarvittavat paketit ovat saatavilla valikossa "Support&Downloads";
- Lataa ladatut paketit Winboxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- Yhdistä uudelleen ja valitse alueesi Wireless-valikossa, W60G-välilehdessä, jotta voit käyttää maan sääntelyasetuksia;
- Aseta yksittäisten mallien kohdalla reitittimen salasana QuickSet-valikossa oikealle ja toista se, sitä käytetään kirjautumaan sisään seuraavalla kerralla.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi ulkona pylvääseen, mutta voidaan myös asentaa sisätiloihin. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Käyttämättä jättäminen CORREC t laitteiston ja kokoonpanon tai noudattaa oikeita menettelytapoja voi johtaa vaarallisiin tilanteisiin ihmisille ja vahingoittaa syste m.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää saatetaan joutua toteuttamaan riittävät toimenpiteet!

**Altistuminen radiotaajuiselle säteilylle:** Tämä MikroTik-laite noudattaa Euroopan unionin säteilyaltistusrajoja, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulee asentaa ja käyttää vähintään 53 senttimetriä kehostasi, ammattikäyttäjästä tai suuresta yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.10 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il incombe aux utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [[https://mt.lv/um-fr](https://mt.lv/um-fr)](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [[https://mt.lv/help-fr](https://mt.lv/help-fr)](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez consulter un consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-98.png)

**Premiers pas:**

- Prenez le couvercle du port Ethernet de l'emballage;
- Guide ouverture de la goulotte de câbles Ethernet;
- Branchez le port Ethernet et vissez fermement dans le sens des aiguilles d'une montre pour assurer la protection contre l'eau;
- Connectez l'injecteur PoE à l'ordinateur;
- Connectez l'adaptateur d'alimentation à l'injecteur PoE;
- Téléchargez l'outil de configuration WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP par défaut: 192.168.88.1, nom d'utilisateur: *admin* et il n'y a pas de mot de passe, pour les modèles jumelés IP: 192.168.88.2/192.168.88.3, veuillez trouver le mot de passe sur l'autocollant;
- Une fois connecté, configurez l'appareil pour qu'il dispose d'une connexion Internet active https://mt.lv/configuration-fr;
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, visitez la page des produits sur [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) pour trouver votre produit. Les paquets nécessaires sont accessibles sous le menu "Support&Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de Winbox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, la stabilité et les mises à jour de sécurité;
- Connectez-vous à nouveau et sélectionnez votre région dans le menu Wireless fil, onglet W60G, pour appliquer les paramètres de réglementation du pays;
- Pour les modèles simples, configurez le mot de passe de votre routeur dans le menu QuickSet, à droite et répétez-le, il sera utilisé pour vous connecter la prochaine fois.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être monté à l'extérieur sur un poteau, mais peut également être installé à l'intérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Ne pas utiliser le correc matériel t et de configuration ou de suivre les procédures appropriées pourrait entraîner une situation dangereuse pour les personnes et les dommages aux systè m.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- Ceci est un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates!

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 53 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.10 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
Ovaj kratki vodič serije "nRAY" obuhvaća modele: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [[https://mt.lv/um-hr](https://mt.lv/um-hr)](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [[https://mt.lv/help-hr](https://mt.lv/help-hr)](https://mt.lv/help-hr)*
*Ako vam je potrebna pomoć u vezi s konfiguracijom, potražite konzultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-98.png)

**Prvi koraci:**

- Izvadite poklopac Ethernet porta iz paketa;
- Otvor kroz otvor Ethernet kabela;
- Uključite Ethernet priključak i čvrsto zavijte u smjeru kazaljke na satu kako biste osigurali zaštitu od vode;
- Spojite PoE injektor u računalo;
- Priključite ispravljač na PoE injektor;
- Preuzmite alat za konfiguraciju WinBox-a [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Zadani IP: 192.168.88.1, korisničko ime: *admin* i nema lozinke, za uparene modele IP: 192.168.88.2/192.168.88.3, lozinku potražite na naljepnici;
- Nakon spajanja konfigurirajte uređaj tako da ima aktivnu internetsku vezu https://mt.lv/configuration-hr;
- Kliknite na gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručno ažuriranje uređaja, posjetite stranicu proizvoda na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) kako biste pronašli svoj proizvod. Potrebni paketi dostupni su u izborniku "Support&Downloads";
- Učitajte preuzete pakete u izbornik "Files" Winboxa i ponovno pokrenite uređaj;
- Ažuriranjem softvera RouterOS na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- Ponovo se povežite i odaberite svoju regiju na izborniku Wireless, kartica W60G, da biste primijenili postavke regulacije zemlje;
- Za pojedinačne modele postavite lozinku usmjerivača u QuickSet izborniku s desne strane i ponovite je, koristit će se d za sljedeću prijavu.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen postavljanju vani na stup, ali može se ugraditi i u zatvorenom prostoru. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne upotrijebite korekcije t hardvera i konfiguracije ili slijediti ispravan postupak može dovesti do opasne situacije za ljude i oštećenja na Syste m.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Ovo je proizvod klase A. U domaćem okruženju, ovaj proizvod može prouzročiti radio smetnje. U tom slučaju se od korisnika može tražiti da poduzme odgovarajuće mjere!

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 53 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.10-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
Ez a "nRAY" sorozat Gyors útmutató a következő modellekre terjed ki: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [[https://mt.lv/um-hu](https://mt.lv/um-hu)](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki leírások, brosúrák és további információk a termékekről a [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [[https://mt.lv/help-hu](https://mt.lv/help-hu)](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfigurálás során, kérjen tanácsadót a [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-98.png)

**Első lépések:**

- Vegye ki az Ethernet port borítását a csomagból;
- Vezető Ethernet kábel a nyíláson keresztül;
- Dugja be az Ethernet portba és csavarja be szorosan az óramutató járásával megegyező irányban a vízvédelem biztosítása érdekében;
- Csatlakoztassa a PoE injektort a számítógéphez;
- Csatlakoztassa a hálózati adaptert a PoE injektorhoz;
- Töltse le a WinBox konfigurációs eszközt: [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Alapértelmezett IP: 192.168.88.1, felhasználói név: *admin* és nincs jelszó, a párosított modellekhez kérjük IP: 192.168.88.2/192.168.88.3, keresse meg a jelszót a matricán;
- A csatlakoztatás után konfigurálja az eszközt, tehát aktív internetkapcsolattal rendelkezik: https://mt.lv/configuration-hu;
- Kattintson az "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- A készülék kézi frissítéséhez látogasson el a [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) termékei oldalra, hogy megtalálja a termékét. A szükséges csomagok elérhetők a "Support&Downloads" menüpont alatt;
- Töltse fel a letöltött csomagokat a Winbox "Files" menübe, majd indítsa újra az eszközt;
- Az RouterOS szoftver frissítésével a legújabb verzióra biztosíthatja az optimális teljesítményt, stabilitást és biztonsági frissítéseket;
- Csatlakozzon ismét és válassza ki a Régiót a Wireless nélküli menü W60G fülén az országszabályozási beállítások alkalmazásához;
- Egyedi modellek esetén állítsa be az útválasztó jelszavát a QuickSet menüből jobbra, és ismételje meg, a d gomb használatával jelentkezik be legközelebb.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket szabadon, rúdra történő felszerelésre tervezték, de beltérben is fel lehet szerelni. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. Ha nem a korrekció t hardver és konfiguráció vagy kövesse a megfelelő eljárásokat vezethet veszélyes helyzetet az emberek és károsíthatja a ren m.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználót szükség lehet megfelelő intézkedések megtételére!

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 53 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan cepat

:::warning
Perangkat ini perlu ditingkatkan ke RouterOS v7.10 atau versi stabil terbaru, untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Pengguna akhir bertanggung jawab untuk mengikuti peraturan negara setempat, termasuk pengoperasian dalam saluran frekuensi resmi, daya keluaran, persyaratan perkabelan, dan persyaratan Pemilihan Frekuensi Dinamis (DFS). Semua perangkat radio MikroTik harus diinstal sesuai petunjuk.
Panduan Cepat seri "nRAY" ini mencakup model: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Kabel Nirkabel nRAY).
:::

*Ini adalah perangkat jaringan nirkabel. Anda dapat menemukan nama model produk pada label casing (ID).*
*Spesifikasi teknis terpenting untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Kunjungi halaman panduan pengguna di [[https://mt.lv/um](https://mt.lv/um)](https://mt.lv/um) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis, brosur, dan info lebih lanjut mengenai produk di [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [[https://mt.lv/help](https://mt.lv/help)](https://mt.lv/help)*
*Jika Anda memerlukan bantuan dalam konfigurasi, silakan mencari konsultan [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/indonesian.badge-35.png)

**Langkah pertama:**

- Ambil penutup port Ethernet dari paket;
- Pandu kabel Ethernet melalui lubang;
- Colokkan ke port Ethernet dan sekrup searah jarum jam dengan kencang, untuk memastikan perlindungan terhadap air;
- Sambungkan PoE injector ke komputer;
- Sambungkan adaptor daya ke PoE injector;
- Unduh alat konfigurasi WinBox di [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP default: 192.168.88.1, nama pengguna: admin, dan tidak ada kata sandi. Untuk model berpasangan IP: 192.168.88.2/192.168.88.3, cari kata sandi pada stiker;
- Setelah terhubung, konfigurasi perangkat untuk memiliki koneksi Internet aktif di https://mt.lv/configuration;
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual, kunjungi halaman produk di [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) untuk menemukan produk Anda. Paket yang diperlukan dapat diakses di bawah menu "Support&Downloads";
- Unggah paket yang diunduh ke menu "Files" Winbox dan reboot perangkat;
- Dengan meng-upgrade perangkat lunak RouterOS ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Sambungkan kembali dan pilih Wilayah Anda di menu Nirkabel, tab W60G, untuk menerapkan pengaturan regulasi negara;
- Untuk model nRAY 60G, atur kata sandi router Anda di menu QuickSet, ke kanan dan ulangi, ini akan digunakan untuk masuk pada kesempatan berikutnya.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, yang dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dimaksudkan untuk dipasang di luar ruangan pada tiang tetapi juga dapat dipasang di dalam ruangan. Harap baca petunjuk pemasangan dengan cermat sebelum memulai pemasangan. Kegagalan dalam menggunakan perangkat keras dan konfigurasi yang benar atau mengikuti prosedur yang benar dapat mengakibatkan situasi berbahaya bagi manusia dan kerusakan pada sistem.
- Kami tidak dapat menjamin bahwa tidak akan terjadi kecelakaan atau kerusakan akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan pengoperasian dengan risiko Anda sendiri!
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut adaptor daya dari stopkontak.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai!

**Paparan Radiasi Frekuensi Radio:** Peralatan MikroTik ini mematuhi batas paparan radiasi Uni Eropa yang ditetapkan untuk lingkungan yang tidak terkendali. Perangkat MikroTik ini sebaiknya dipasang dan dioperasikan tidak lebih dekat dari 53 sentimeter dari tubuh Anda, pengguna pekerjaan, atau masyarakat umum.

Pabrikan: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.10 o all'ultima versione stabile, per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Visitare la pagina del manuale dell'utente su [[https://mt.lv/um-it](https://mt.lv/um-it)](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [[https://mt.lv/help-it](https://mt.lv/help-it)](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, cerca un consulente [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-98.png)

**Primi passi:**

- Prendere il coperchio della porta Ethernet dalla confezione;
- Guida cavo Ethernet attraverso apertura;
- Collegare alla porta Ethernet e avvitare saldamente in senso orario, per garantire la protezione dell'acqua;
- Collegare l'iniettore PoE al computer;
- Collegare l'alimentatore all'iniettore PoE;
- Scarica lo strumento di configurazione WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP predefinito: 192.168.88.1, nome utente: *admin* e non c'è password, per i modelli accoppiati IP: 192.168.88.2/192.168.88.3, trovare la password sull'adesivo;
- Una volta connesso, configura il dispositivo, quindi ha una connessione Internet attiva https://mt.lv/configuration-it;
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per un aggiornamento manuale del dispositivo, visita la pagina dei prodotti su [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) per trovare il tuo prodotto. I pacchetti richiesti sono accessibili nel menu "Support&Downloads";
- Carica i pacchetti scaricati nel menu "Files" di Winbox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Connettiti di nuovo e seleziona la tua regione nel menu Wireless, scheda W60G, per applicare le impostazioni di regolamentazione del paese;
- Per i modelli singoli, impostare la password del router nel menu QuickSet, a destra e ripeterla, verrà utilizzata d per accedere la prossima volta.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è progettato per essere montato all'esterno su un'asta ma può anche essere installato all'interno. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo della correc t hardware e di configurazione o di seguire le procedure corrette potrebbe tradursi in una situazione di pericolo per le persone e danni al syste m.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso all'utente potrebbe essere richiesto di adottare misure adeguate!

**Esposizione alle radiazioni in radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a non meno di 53 centimetri dal corpo, dall'utente professionale o dal pubblico in generale.

Produttore: Mikrotikls SIA, Unijas 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.10 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
Þessi „nRAY“ röð skyndihandbók nær yfir gerðir: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [[https://mt.lv/um-is](https://mt.lv/um-is)](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [[https://mt.lv/help-is](https://mt.lv/help-is)](https://mt.lv/help-is)*
*Ef þú þarft hjálp við stillingar, vinsamlegast leitaðu til ráðgjafa [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-98.png)

**Fyrstu skrefin:**

- Taktu Ethernet-porthlífina úr pakkanum;
- Leiðbeiningar Ethernet snúru með lágmarksopnun;
- Stingdu í Ethernet tengið og skrúfaðu réttsælis til að tryggja vatnsvernd;
- Tengdu PoE inndælingartækið við tölvuna;
- Tengdu rafmagnsinnstunguna við PoE inndælingartækið;
- Sæktu WinBox stillitól [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Sjálfgefið IP: 192.168.88.1, notandanafn: *admin* og það er ekkert lykilorð, fyrir pöruð módel IP: 192.168.88.2/192.168.88.3, vinsamlegast finndu lykilorðið á límmiðanum;
- Þegar tækið er tengt er það stillt þannig að það er með virka internettengingu https://mt.lv/configuration-is;
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Fyrir handvirk uppfærslu á tækinu, heimsaðu á vefsíðuna á [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) til að finna vöruna þína. Nauðsynlegir pakkar eru aðgengilegir í "Support&Downloads" valkostnum;
- Hlaða niður pakka í Winbox "Files" valkostinn og endurræsa tækið;
- Með því að uppfæra hugbúnaðinn á RouterOS í nýjustu útgáfu getur þú tryggjað bestu mögulegu afköst, stöðugleika og öryggisuppfærslur;
- Tengdu aftur og veldu land þitt vinstra megin á skjánum til að beita stillingum landsreglugerðar;
- Fyrir stakar gerðir, settu upp leiðarlykilorðið þitt í QuickSet valmyndinni, til hægri og endurtakið það, það verður að nota d til að skrá þig inn næst.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að fyrirbyggja slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að vera úti á stöng en einnig er hægt að setja hana innandyra. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar að setja upp. Bilun til að nota correc t vélbúnaði og stillingar eða til að fylgja réttra aðferða gæti leitt til hættuástand á fólk og skemmt í syste m.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Tengdu aftur og veldu svæðið þitt í þráðlausu Wireless, W60G flipanum, til að beita stillingum landsreglugerðar;
- Þetta er A-vara. Í innlendu umhverfi gæti þessi vara valdið truflunum á útvarpi og þá gæti verið krafist þess að notandinn geri viðeigandi ráðstafanir!

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 53 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.10 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukerens ansvar å følge lokale landsbestemmelser, inkludert drift innenfor lovlige frekvenskanaler, utgangseffekt, kablingskrav og krav til dynamisk frekvensvalg (DFS). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [[https://mt.lv/um-no](https://mt.lv/um-no)](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [[https://mt.lv/help-no](https://mt.lv/help-no)](https://mt.lv/help-no)*
*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-98.png)

**Første steg:**

- Ta Ethernet-portdekselet fra pakken;
- Guide Ethernet-kabel gjennom åpning;
- Plugg inn Ethernet-porten og skru den med klokka for å sikre vannbeskyttelse;
- Koble PoE-injektoren til datamaskinen;
- Koble strømadapteren til PoE-injektoren;
- Last ned konfigurasjonsverktøyet WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Standard IP: 192.168.88.1, brukernavn: *admin,* og det er ikke noe passord. For de sammenkoblede modellene IP: 192.168.88.2/192.168.88.3, vennligst finn passordet på klistremerket;
- Når du er tilkoblet, konfigurer enheten, så den har en aktiv Internett-tilkobling https://mt.lv/configuration-no;
- Klikk på knappen "Check for updates" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, besøk produktsiden på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) for å finne produktet ditt. De nødvendige pakkene er tilgjengelige under "Support&Downloads" -menyen;
- Last opp nedlastede pakker til Winbox "Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- Koble til igjen og velg din region i Wireless-menyen, W60G-fanen, for å bruke innstillinger for landsregulering;
- For enkeltmodeller, sett opp rutepassordet ditt i QuickSet-menyen, til høyre og gjenta det, det vil bruke d til å logge inn neste gang.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å være montert utendørs på en stolpe, men kan også installeres innendørs. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke den rette maskinvaren og konfigurasjonen eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- Dette er et produkt i klasse A. I hjemlige omgivelser kan dette produktet forårsake radioforstyrrelser, i hvilket tilfelle brukeren kan bli pålagt å treffe tilstrekkelige tiltak!

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 53 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.10“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.
Šis „nRAY“ serijos trumpasis vadovas apima modelius: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [[https://mt.lv/um-lt](https://mt.lv/um-lt)](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [[https://mt.lv/help-lt](https://mt.lv/help-lt)](https://mt.lv/help-lt)*
*Jei jums reikia pagalbos dėl konfigūravimo, kreipkitės į konsultantą [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-97.png)

**Pirmieji žingsniai:**

- Paimkite Ethernet prievado dangtelį iš pakuotės;
- Kreipiamojo eterneto kabelio angos atidarymas;
- Įkiškite į eterneto prievadą ir tvirtai prisukite pagal laikrodžio rodyklę, kad užtikrintumėte vandens apsaugą;
- Prijunkite „PoE“ purkštuvą prie kompiuterio;
- Prijunkite maitinimo adapterį prie „PoE“ purkštuko;
- Atsisiųskite „WinBox“ konfigūravimo įrankį [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Numatytasis IP: 192.168.88.1, vartotojo vardas: *admin* ir nėra slaptažodžio, suporuotų modelių IP: 192.168.88.2/192.168.88.3 slaptažodį rasite ant lipduko;
- Prijungę sukonfigūruokite įrenginį, taigi jis turi aktyvų interneto ryšį https://mt.lv/configuration-lt;
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norint rankiniu būdu atnaujinti įrenginį, apsilankykite produkto puslapyje adresu [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), kad rastumėte savo produktą. Reikalingi paketai prieinami "Support&Downloads" meniu;
- Įkraukite parsisiųstus paketus į Winbox "Files" meniu ir paleiskite įrenginį iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Vėl prisijunkite ir pasirinkite savo regioną belaidžio Wireless meniu, skirtuke W60G, kad pritaikytumėte šalies reguliavimo parametrus;
- Atskiriems modeliams nustatykite maršrutizatoriaus slaptažodį „QuickSet“ meniu dešinėje ir pakartokite jį, jis bus naudojamas d norint prisijungti kitą kartą.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas yra skirtas montuoti lauke ant stulpo, bet taip pat gali būti montuojamas viduje. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Nesugebėjimas naudotis Korekcijos t aparatūros ir konfigūraciją arba laikytis tinkamo procedūros gali sukelti pavojingas situacijas prie žmonių ir žalos syste m.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis produktas gali sukelti radijo trikdžius; tokiu atveju gali reikėti vartotojo imtis tinkamų priemonių!

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 53 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.10 stabilo vai jaunāku versiju, lai nodrošinātu atbilstību vietējās varas noteikumiem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijai.
Šī īsā rokasgrāmata paredzēta modeļiem: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [[https://mt.lv/um-lv](https://mt.lv/um-lv)](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [[https://mt.lv/help-lv](https://mt.lv/help-lv)](https://mt.lv/help-lv)*
*Ja jums nepieciešama palīdzība ar konfigurēšanu, lūdzu, konsultējieties vietnē [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-98.png)

**Pirmie soļi:**

- Atrodiet Ethernet porta vāciņu iepakojumā;
- Izvelciet Ethernet kabeli cauri vākam, tam paredzētajam atvērumam;
- Pievienojiet Ethernet kabeli portam, aizveriet vāku un cieši pieskrūvējiet pulksteņrādītāja virzienā, lai nodrošinātu ūdens aizsardzību;
- Pievienojiet PoE inžektoru datoram;
- Pievienojiet strāvas adapteri PoE inžektoram;
- Lejupielādējiet WinBox konfigurācijas rīku [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Noklusējuma IP: 192.168.88.1, lietotājvārds: *admin* un parole nav uzstādīta, modeļi, kuri tirgojās pāros IP: 192.168.88.2/192.168.88.3, lūdzu, meklējiet paroli uz uzlīmes;
- Pēc savienojuma konfigurējiet ierīci, lai tai būtu aktīvs Interneta savienojums https://mt.lv/configuration-lv;
- Noklikšķiniet uz pogas "Check for updates" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Manuālai ierīces atjaunināšanai apmeklējiet produktu lapu vietnē [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), lai atrastu savu produktu. Nepieciešamie pakotnes ir pieejamas sadaļā "Support&Downloads";
- Ielādējiet lejupielādētās pakotnes Winbox "Files" izvēlnē un restartējiet ierīci;
- Jauninot RouterOS programmatūru uz jaunāko versiju, jūs varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Pievienojieties vēlreiz un izvēlnē Wireless, cilnē W60G, atlasiet savu reģionu, lai lietotu valsts regulēšanas iestatījumus;
- *nRAY 60G* modeļiem iestatiet maršrutētāja paroli izvēlnē QuickSet labajā pusē un atkārtojiet to, tā tiks izmantota, lai pieteiktos nākamreiz.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar nelaimes gadījumu novēršanas standarta praksi. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai ārtelpās, bet to var uzstādīt arī telpās. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nespēja izmantot pareizu aparatūru un konfigurāciju, vai sekot pareizās procedūras var izraisīt bīstamas situācijas uz cilvēkiem, un sabojāt ar sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Šis ir A klases produkts. Sadzīves apstākļos šis izstrādājums var izraisīt radio traucējumus, un tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi!

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 53 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Ūnijas 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.10 jew l-aħħar verżjoni stabbli, sabiex tkun żgurata konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż operazzjoni fi ħdan kanali tal-frekwenza legali, qawwa tal-ħruġ, rekwiżiti tal-kejbils u rekwiżiti tal-Għażla tal-Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [[https://mt.lv/um-mt](https://mt.lv/um-mt)](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [[https://mt.lv/help-mt](https://mt.lv/help-mt)](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna fil-konfigurazzjoni, jekk jogħġbok tfittex konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-98.png)

**L-ewwel passi:**

- Oħroġ il-kopertura tal-port Ethernet mill-pakkett;
- Gwida tal-ftuħ tal-kejbil Ethernet permezz tal-ftuħ;
- Ipplaggja fil-port Ethernet u kamin sewwa mal-arloġġ, biex tiżgura l-protezzjoni tal-ilma;
- Qabbad l-injettur PoE fil-kompjuter;
- Qabbad l-adapter tal-qawwa mal-injettur PoE;
- Niżżel l-għodda ta 'konfigurazzjoni WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP Default: 192.168.88.1, isem tal-utent: *admin* u m'hemm l-ebda password, għall-mudelli paired IP: 192.168.88.2/192.168.88.3, jekk jogħġbok sib il-password fuq l-istiker;
- Ladarba jkun ikkonfigurat it-tagħmir, huwa għandu konnessjoni tal-internet attiva https://mt.lv/configuration-mt;
- Ikklikkja fuq il-buttuna "Check for updates" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur il-paġna tal-prodotti fuq [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) biex issib il-prodott tiegħek. Il-pakketti meħtieġa huma aċċessibbli taħt il-meni "Support&Downloads";
- Ipposta l-pakketti li jużaw lura fil-meni "Files" tal-Winbox u reboot l-apparat;
- Billi taġġorna l-softwer tal-RouterOS għall-aħħar verżjoni, tista 'tissikura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Qabbad mill-ġdid u agħżel ir-Reġjun tiegħek fil-menu Wireless, tab W60G, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Għal mudelli singoli, waqqaf il-password tar-router tiegħek fil-menu QuickSet, fuq il-lemin u rrepetiha, se tuża d biex tidħol il-ħin li jmiss.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jiġi mmuntat fuq barra fuq arblu iżda jista 'jiġi installat ukoll ġewwa. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Nuqqas ta 'użu tal-correc ħardwer tu konfigurazzjoni jew li ssegwi l-proċeduri korretti jista' jwassal għal sitwazzjoni perikoluża għall-persuni u ħsara għall-syste m.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza bir-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati!

**Espożizzjoni għal Radjazzjoni ta' Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' espożizzjoni għar-radjazzjoni tal-Unjoni Ewropea stabbiliti għal ambjent mhux ikkontrollat. Dan l-apparat MikroTik għandu jiġi installat u mħaddem mhux eqreb minn 53 ċentimetru minn ġismek, mill-utent okkupazzjonali, jew mill-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.10 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, waaronder de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [[https://mt.lv/um-nl](https://mt.lv/um-nl)](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, brochures en meer informatie over producten op [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [[https://mt.lv/help-nl](https://mt.lv/help-nl)](https://mt.lv/help-nl)*
*Als je hulp nodig hebt bij het configureren, zoek dan een consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-98.png)

**Eerste stappen:**

- Haal het deksel van de Ethernet-poort uit de verpakking;
- Gids Ethernet-kabel door opening;
- Sluit hem aan op de Ethernet-poort en draai hem rechtsom vast om waterbescherming te garanderen;
- Sluit de PoE-injector aan op de computer;
- Sluit de voedingsadapter aan op de PoE-injector;
- Configuratietool WinBox downloaden [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Standaard IP: 192.168.88.1, gebruikersnaam: *admin* en er is geen wachtwoord, voor de gekoppelde modellen IP: 192.168.88.2/192.168.88.3 vindt u het wachtwoord op de sticker;
- Eenmaal verbonden, configureert u het apparaat, zodat het een actieve internetverbinding heeft https://mt.lv/configuration-nl;
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, bezoek de productpagina op [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) om uw product te vinden. De benodigde pakketten zijn toegankelijk onder het menu "Support&Downloads";
- Upload gedownloade pakketten naar het Winbox "Files" menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Maak opnieuw verbinding en selecteer uw regio in het menu Wireless, tabblad W60G, om de regelgevingsinstellingen van het land toe te passen;
- Stel voor enkele modellen uw routerwachtwoord in het QuickSet-menu in aan de rechterkant en herhaal het, het wordt gebruikt om de volgende keer in te loggen.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om buiten op een paal te worden gemonteerd, maar kan ook binnenshuis worden geïnstalleerd. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Als u de correctie te gebruiken t hardware en configuratie of het volgen van de juiste procedures kan resulteren in een gevaarlijke situatie aan mensen en schade aan de syste m.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.
- Dit is een Klasse A-product. In een huiselijke omgeving kan dit product radio-interferentie veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen moet nemen!

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 53 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.10 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik należy zainstalować zgodnie z instrukcjami.
Niniejsza skrócona instrukcja „nRAY” obejmuje modele: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [[https://mt.lv/um-pl](https://mt.lv/um-pl)](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [[https://mt.lv/help-pl](https://mt.lv/help-pl)](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy w konfiguracji, poszukaj konsultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-98.png)

**Pierwsze kroki:**

- Wyjmij osłonę portu Ethernet z opakowania;
- Prowadź korytko kablowe Ethernet;
- Podłącz do portu Ethernet i dokręć mocno zgodnie z ruchem wskazówek zegara, aby zapewnić ochronę przed wodą;
- Podłącz wtryskiwacz PoE do komputera;
- Podłącz zasilacz do wtryskiwacza PoE;
- Pobierz narzędzie do konfiguracji WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Domyślny adres IP: 192.168.88.1, nazwa użytkownika: *admin* i nie ma hasła, w przypadku sparowanych modeli IP: 192.168.88.2/192.168.88.3 hasło należy znaleźć na naklejce;
- Po podłączeniu skonfiguruj urządzenie, aby miało aktywne połączenie z Internetem https://mt.lv/configuration-pl;
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- W przypadku ręcznej aktualizacji urządzenia, odwiedź stronę produktów na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), aby znaleźć swój produkt. Wymagane pakiety są dostępne w menu "Support&Downloads";
- Wgraj pobrane pakiety do menu "Files" w Winbox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- Połącz się ponownie i wybierz swój region w menu Wireless na karcie W60G, aby zastosować ustawienia przepisów krajowych;
- W przypadku pojedynczych modeli ustaw hasło routera w menu QuickSet po prawej stronie i powtórz je, będzie ono używane do zalogowania się następnym razem.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt jest przeznaczony do montażu na zewnątrz na słupie, ale może być również instalowany wewnątrz. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niewykorzystanie correc t i konfigurację sprzętu lub postępować zgodnie z procedurami, może doprowadzić do niebezpiecznych sytuacji dla ludzi i uszkodzić do syste m.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w takim przypadku użytkownik może być zobowiązany do podjęcia odpowiednich kroków!

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 53 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.10 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
Este guia rápido da série "nRAY" abrange os modelos: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [[https://mt.lv/um-pt](https://mt.lv/um-pt)](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [[https://mt.lv/help-pt](https://mt.lv/help-pt)](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-98.png)

**Primeiros passos:**

- Retire a tampa da porta Ethernet da embalagem;
- Guia Cabo Ethernet através da abertura;
- Conecte na porta Ethernet e aperte firmemente no sentido horário, para garantir a proteção da água;
- Conecte o injetor PoE ao computador;
- Conecte o adaptador de energia ao injetor PoE;
- Faça o download da ferramenta de configuração WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP padrão: 192.168.88.1, nome de usuário: *admin* e não há senha; para os modelos emparelhados IP: 192.168.88.2/192.168.88.3, localize a senha no adesivo;
- Uma vez conectado, configure o dispositivo, para que ele tenha uma conexão ativa com a Internet https://mt.lv/configuration-pt;
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para uma atualização manual do dispositivo, visite a página de produtos em [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) para encontrar seu produto. Os pacotes necessários estão acessíveis no menu "Support&Downloads";
- Faça o upload dos pacotes baixados no menu "Files" do Winbox e reinicie o dispositivo;
- Ao atualizar o software do RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- Conecte-se novamente e selecione sua região no menu Wireless, guia W60G, para aplicar as configurações de regulamentação do país;
- Para modelos individuais, configure a senha do roteador no menu QuickSet, à direita e repita, ela será usada para fazer o login na próxima vez.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e familiarize-se com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser montado ao ar livre em um poste, mas também pode ser instalado em ambientes fechados. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização da correc hardware t e configuração ou para seguir os procedimentos correctos pode resultar numa situação perigosa para as pessoas e para danificar o syste m.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- Este é um produto de classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio. Nesse caso, pode ser necessário que o usuário tome as medidas adequadas!

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 53 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.10 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
Acest ghid rapid seria „nRAY” acoperă modele: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [[https://mt.lv/um-ro](https://mt.lv/um-ro)](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [[https://mt.lv/help-ro](https://mt.lv/help-ro)](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-96.png)

**Primii pasi:**

- Scoateți capacul portului Ethernet din pachet;
- Ghid de deschidere prin cablu Ethernet;
- Introduceți în portul Ethernet și înșurubați strâns în sens orar, pentru a asigura protecția apei;
- Conectați injectorul PoE la computer;
- Conectați adaptorul de alimentare la injectorul PoE;
- Descărcați instrumentul de configurare WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP implicit: 192.168.88.1, nume utilizator: *admin* și nu există nicio parolă, pentru modelele împerecheate IP: 192.168.88.2/192.168.88.3, vă rugăm să găsiți parola pe autocolant;
- Odată conectat configurați dispozitivul, deci are o conexiune la Internet activă https://mt.lv/configuration-ro;
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru o actualizare manuală a dispozitivului, vizitați pagina de produse la [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) pentru a găsi produsul dvs. Pachetele necesare sunt accesibile în meniul "Support&Downloads";
- Încărcați pachetele descărcate în meniul "Files" din Winbox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- Conectați-vă din nou și selectați Regiunea în meniul Wireless, fila W60G, pentru a aplica setările de reglementare a țării;
- Pentru modele individuale, setați parola routerului în meniul QuickSet, în dreapta și repetați-l, va fi folosit d pentru a vă autentifica data viitoare.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie montat în aer liber pe un stâlp, dar poate fi instalat și în interior. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Acesta este un produs de clasa A. Într-un mediu intern, acest produs poate provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate!

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 53 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.10 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných používateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
Táto stručná príručka „nRAY“ pokrýva modely: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [[https://mt.lv/um-sk](https://mt.lv/um-sk)](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [[https://mt.lv/help-sk](https://mt.lv/help-sk)](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-98.png)

**Prvé kroky:**

- Z balenia odstráňte kryt ethernetového portu;
- Vodiaci kábel pre Ethernet kábel sa otvára;
- Zapojte do ethernetového portu a pevne priskrutkujte v smere hodinových ručičiek, aby ste zaistili ochranu vody;
- Pripojte injektor PoE k počítaču;
- Pripojte napájací adaptér k injektoru PoE;
- Stiahnite si konfiguračný nástroj WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Predvolená IP: 192.168.88.1, meno používateľa: *admin* a neexistuje žiadne heslo, pre spárované modely IP: 192.168.88.2/192.168.88.3, nájdete heslo na nálepke;
- Po pripojení nakonfigurujte zariadenie tak, aby malo aktívne internetové pripojenie https://mt.lv/configuration-sk;
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Pre manuálnu aktualizáciu zariadenia navštívte stránku produktov na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), aby ste našli váš produkt. Potrebné balíky sú dostupné v menu "Support&Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v Winbox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- Znovu sa pripojte a vyberte svoj región v ponuke Wireless pripojenie, karta W60G, aby ste použili nastavenia regulácie krajiny;
- V prípade jednotlivých modelov nastavte heslo smerovača v ponuke QuickSet napravo a opakujte ho. Pri ďalšom prihlásení sa použije písmeno d.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na montáž vonku na stožiar, ale môže byť nainštalovaný aj vo vnútri. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Zlyhanie použiť Korekcia t konfiguráciu hardvéru a alebo dodržať správny postup môže viesť k nebezpečným situáciám pre ľudí a poškodenia syst m.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Toto je produkt triedy A. V domácom prostredí môže tento produkt spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa požadované, aby prijal primerané opatrenia!

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované bližšie ako 53 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.10 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so odgovorni za upoštevanje lokalnih predpisov, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
Ta hitri vodnik serije "nRAY" zajema modele: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [[https://mt.lv/um-sl](https://mt.lv/um-sl)](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [[https://mt.lv/help-sl](https://mt.lv/help-sl)](https://mt.lv/help-sl)*
*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-98.png)

**Prvi koraki:**

- Vzemite pokrov vrat Ethernet iz paketa;
- Vhod skozi odprtino vodnika Ethernet;
- Priključite v vrata Ethernet in tesno privijte v smeri urinega kazalca, da zagotovite zaščito pred vodo;
- PoE priključite injektor v računalnik;
- Napajalnik priključite na PoE injektor;
- Prenesite orodje za konfiguracijo WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Privzeti IP: 192.168.88.1, uporabniško ime: *admin* in ni gesla, za seznanjene modele IP: 192.168.88.2/192.168.88.3, poiščite geslo na nalepki;
- Ko je povezava konfigurirana, tako da ima aktivno internetno povezavo https://mt.lv/configuration-sl;
- Kliknite na gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite stran izdelkov na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), da najdete svoj izdelek. Potrebni paketi so dostopni v meniju "Support&Downloads";
- Naložite prenesene pakete v meni "Files" v Winboxu in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico zagotovite optimalne zmogljivosti, stabilnost in varnostne posodobitve;
- Ponovno se povežite in izberite območje v meniju Wireless, zavihek W60G, da uporabite nastavitve za državno ureditev;
- Za enojne modele nastavite geslo usmerjevalnika v meniju QuickSet na desni in ga ponovite, naslednjič bo uporabljen d za prijavo.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti električnega tokokroga in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen za namestitev na prostem na drog, vendar ga je mogoče namestiti tudi v zaprtih prostorih. Pred začetkom namestitve natančno preberite navodila za montažo. Če ne uporabite correc t strojne opreme in konfiguracija ali sledite pravilni postopki lahko povzroči nevarne situacije za ljudi in škodo na Syste m.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje; v tem primeru se od uporabnika zahteva, da sprejme ustrezne ukrepe!

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 53 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.10 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [[https://mt.lv/um-sv](https://mt.lv/um-sv)](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [[https://mt.lv/help-sv](https://mt.lv/help-sv)](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfiguration, vänligen kontakta en konsult [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-98.png)

**Första stegen:**

- Ta Ethernet-portkåpan från paketet;
- Guide Ethernet-kabel genom öppning;
- Anslut Ethernet-porten och skruva medurs medurs för att säkerställa vattenskydd;
- Anslut PoE-injektorn till datorn;
- Anslut nätadaptern till PoE-injektorn;
- Ladda ner WinBox konfigurationsverktyg [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- Standard IP: 192.168.88.1, användarnamn: *admin* och det finns inget lösenord, för de parade modellerna, IP: 192.168.88.2/192.168.88.3 vänligen hitta lösenordet på klistermärket;
- När du är ansluten konfigurerar du enheten så att den har en aktiv internetanslutning https://mt.lv/configuration-sv;
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, besök produktsidan på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) för att hitta din produkt. De nödvändiga paketen finns tillgängliga under "Support&Downloads";
- Ladda upp nedladdade paket till Winbox "Files" -menyn och starta om enheten;
- Genom att uppdatera RouterOS-programvaran till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- Anslut igen och välj din region i den Wireless menyn, W60G-fliken, för att tillämpa landsregleringsinställningar;
- För enstaka modeller, ställ in ditt routerlösenord i QuickSet-menyn till höger och upprepa det, det kommer att användas d för att logga in nästa gång.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att monteras utomhus på en stolpe men kan också installeras inomhus. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa korrekta procedurer kan leda till en farlig situation för människor och skada på system.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- Detta är en klass A-produkt. I en hemmamiljö kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder!

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 53 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.10或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
此“ nRAY”系列快速指南涵盖以下型号：RBCube-60ad（Cube Lite60）。
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[[https://mt.lv/um-zh](https://mt.lv/um-zh)](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*有关产品的技术规格，手册和更多信息， 请访问[[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [[https://mt.lv/help-zh](https://mt.lv/help-zh)](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请寻求顾问 [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-99.png)

**第一步：**

- 从包装中取出以太网端口盖；
- 引导以太网电缆线槽打开；
- 插入以太网端口并顺时针拧紧，以确保防水。
- 将PoE注入器连接至计算机；
- 将电源适配器连接到PoE注入器；
- 下载WinBox配置工具[[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- 默认IP：192.168.88.1，用户名：*admin*，没有密码，对于配对的机型 IP: 192.168.88.2/192.168.88.3，请在贴纸上找到密码；
- 连接后，配置设备，使其具有活动的Internet连接https://mt.lv/configuration-zh
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 对于设备的手动更新，请访问[[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) 上的产品页面查找您的产品。所需的软件包可在"Support&Downloads"菜单下找到;
- 将下载的软件包上传到Winbox的"Files"菜单并重新启动设备;
- 通过将RouterOS软件更新到最新版本，您可以确保最佳性能，稳定性和安全更新;
- 再次连接并在“Wireless”菜单的“ W60G”选项卡中选择您的“地区”以应用国家/地区法规设置；
- 对于单个型号，请在右侧的QuickSet菜单中设置路由器密码，然后重复输入一次，下次将使用 d登录。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和配件，这些电源和配件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。安装程序负责确保设备的安装符合当地和国家的电气法规。请勿尝试拆卸，修理或修改设备。
- 该产品旨在安装在室外的杆子上，但也可以安装在室内。开始安装之前，请仔细阅读安装说明。若未使用correc 牛逼的硬件和配置，或者按照正确的程序可能会导致危险情况的人并伤害到SYSTE 米。
- 我们不能保证由于不正确使用本设备不会造成任何事故或损坏。请谨慎使用本产品，并自行承担风险！
- 如果设备发生故障，请断开电源。最快的方法是从电源插座上拔下电源适配器。
- 这是A类产品。在家庭环境中，此产品可能会造成无线电干扰，在这种情况下，可能要求用户采取适当的措施！

**射频辐射暴露：** 此 MikroTik 设备符合针对不受控制的环境规定的欧盟辐射暴露限制。此 MikroTik 设备的安装和操作距离您的身体、职业用户或公众不得超过 53 厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.10 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [[https://mt.lv/um-ru](https://mt.lv/um-ru)](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [[https://mt.lv/help-ru](https://mt.lv/help-ru)](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, обратитесь к консультанту [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-97.png)

**Первые шаги:**

- Снимите крышку Ethernet-порта;
- Протяните Ethernet-кабель через отверстие крышки;
- Подключите к порту Ethernet и плотно закрутите по часовой стрелке, чтобы обеспечить защиту от воды;
- Подключите PoE-инжектор к компьютеру;
- Подключите адаптер питания к PoE-инжектору;
- Загрузите инструмент настройки WinBox [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP-адрес по умолчанию: 192.168.88.1, имя пользователя: *admin,* пароль отсутствует, для парных моделей IP: 192.168.88.2/192.168.88.3, найдите пароль на наклейке;
- После подключения настройте устройство, чтобы у него было активное подключение к Интернету https://mt.lv/configuration-ru;
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства посетите страницу продукта на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), чтобы найти свой продукт. Необходимые пакеты доступны в меню "Support&Downloads";
- Загрузите скачанные пакеты в меню "Files" Winbox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- Подключитесь снова и выберите свой регион в меню «Wireless» на вкладке W60G, чтобы применить настройки страны;
- Для *nRAY 60G* моделей установите пароль маршрутизатора в меню QuickSet и повторите его, он будет использоваться для входа в следующий раз.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать как в помещении, так и на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
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

**Воздействие радиочастотного излучения.** Это устройство MikroTik должно быть установлено и эксплуатироваться не ближе 53 сантиметров от вашего тела, профессионального пользователя или широкой публики.

Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

| Частотный каналы | Мощность передатчика |
| --- | --- |
| 58.32 ГГц, 60.48 ГГц, 62.64 ГГц | ≤ 10 Вт |

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

![](./img/image2020-1-24_7-55-5.badge-101.png)

Во избежание загрязнения окружающей среды необходимо отделить устройство от бытовых отходов и утилизировать его безопасным способом, например в специально отведенных местах. Ознакомьтесь с процедурами надлежащей транспортировки оборудования к специальным местам утилизации в вашем регионе.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.10 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!

Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі пристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей короткий посібник серії "nRAY" охоплює моделі: nRAYG-60ad (nRAY 60G), nRAYG-60adpair (Wireless Wire nRAY).

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [[https://mt.lv/um-ua](https://mt.lv/um-ua)](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [[https://mt.lv/help-ua](https://mt.lv/help-ua)](https://mt.lv/help-ua)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_12-48-16.badge-40.png)

**Перші кроки:**

- Вийміть захисну кришку з Ethernet-порту з упаковки;
- Прокладіть Ethernet-кабель через отвір у кришці;
- Підключіть його до Ethernet-порту та закрутіть за годинниковою стрілкою, щоб забезпечити захист від води;
- Підключіть PoE-інжектор до комп'ютера;
- Підключіть адаптер живлення до PoE-інжектора;
- Завантажте інструмент конфігурації WinBox за посиланням [[[https://mt.lv/winbox](https://mt.lv/winbox)](https://mt.lv/winbox)](https://mt.lv/winbox);
- IP-адреса за замовчуванням: 192.168.88.1, ім'я користувача: admin, і відсутній пароль. Для парних моделей IP: 192.168.88.2/192.168.88.3, знайдіть пароль на наклейці;
- Після підключення налаштуйте пристрій для активного Інтернет-з'єднання https://mt.lv/configuration-ua;
- Натисніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products), щоб знайти свій продукт. Необхідні пакети доступні в меню "Support&Downloads";
- Завантажте завантажені пакети в меню "Files" Winbox та перезапустіть пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- Для моделей nRAY 60G налаштуйте пароль маршрутизатора в меню QuickSet та повторіть його, він буде використовуватися для входу наступного разу.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей продукт призначений для установки на відкритому повітрі на стовпі. Будь ласка, уважно прочитайте інструкцію з монтажу перед початком установки. Неправильне використання апаратного забезпечення та налаштувань або невідповідність правильним процедурам може створити ризик для безпеки осіб та призвести до пошкодження системи.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик!
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити — від’єднати адаптер електроживлення від розетки.
- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.
- Це продукт класу А. У побутових умовах цей продукт може спричинити радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити належних заходів!

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 53 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Unijas 2, Рига, Латвія, LV1039.

## Federal Communication Commission Interference Statement

FCC ID: TV7RAY60

![](./img/fcc_logo_ez.badge-88.jpg)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense.

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

IMPORTANT NOTE: This device is not to be operated on aircraft except for the conditions listed on FCC CFR §15.255 (b)

FCC Radiation Exposure Statement: This equipment complies with FCC radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 53cm between the radiator & your body.

 All cables used to connect peripherals must be shielded and grounded. Operation with cables connected to peripherals that are not shielded and grounded may result in interference to radio and television reception.

## Innovation, Science and Economic Development Canada

IC: 7442A-RAY60

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

IMPORTANT NOTE: This device is not to be operated on aircraft except for the conditions listed on ISED RSS-210 Annex J.1.

Cet appareil ne doit pas être utilisé sur un avion, sauf dans les conditions énumérées ISED RSS-210 Annex J.1.

IC Radiation Exposure Statement: This equipment complies with IC RSS-102 radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 53cm between the radiator & your body.

Cet équipement est conforme aux limites d'exposition aux rayonnements IC établies pour un environnement non contrôlé. Cet équipement doit être installé et utilisé avec un minimum de 53cm de distance entre la source de rayonnement et votre corps.

## UKCA marking

![](./img/ukca_black_fill.badge-97.gif)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение nRAYG-60ad, nRAYG-60adpair е в съответствие с Директива nRAYG-60ad, nRAYG-60adpair 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení nRAYG-60ad, nRAYG-60adpair je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen nRAYG-60ad, nRAYG-60adpair er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp nRAYG-60ad, nRAYG-60adpair der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός nRAYG-60ad, nRAYG-60adpair πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type nRAYG-60ad, nRAYG-60adpair is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico nRAYG-60ad, nRAYG-60adpair es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp nRAYG-60ad, nRAYG-60adpair vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi nRAYG-60ad, nRAYG-60adpair on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type nRAYG-60ad, nRAYG-60adpair est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa nRAYG-60ad, nRAYG-60adpair u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a nRAYG-60ad, nRAYG-60adpair típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio nRAYG-60ad, nRAYG-60adpair è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að nRAYG-60ad, nRAYG-60adpair er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas nRAYG-60ad, nRAYG-60adpair atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta nRAYG-60ad, nRAYG-60adpair atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju nRAYG-60ad, nRAYG-60adpair huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur nRAYG-60ad, nRAYG-60adpair conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret nRAYG-60ad, nRAYG-60adpair er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego nRAYG-60ad, nRAYG-60adpair jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio nRAYG-60ad, nRAYG-60adpair está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio nRAYG-60ad, nRAYG-60adpair este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu nRAYG-60ad, nRAYG-60adpair je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme nRAYG-60ad, nRAYG-60adpair skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning nRAYG-60ad, nRAYG-60adpair överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |

This device meets the Maximum TX power limit per ETSI regulations. The frequency and the maximum transmitted power in the EU are listed below: 57 - 66 GHz: 35.57 dBm. An Operational mode in the 60 GHz band: 58.32 GHz, 60.48 GHz, 62.64 GHz. This device is certified for outdoor use in Point to Multipoint applications. In the following countries this device cannot be used in Fixed Point-to-Point applications:

![](./img/tab-6.png)

## WiGig

| Operational channels / Maximum output power Betriebskanäle / maximale Ausgangsleistung Canaux opérationnels / puissance de sortie maximale Canali operativi / massima potenza di uscita Canales operacionales / potencia de salida máxima Операционные каналы / максимальная выходная мощность | 58.32 GHz / &lt;40 dBm |
| --- | --- |
| 60.48 GHz / &lt;40 dBm | |
| 62.64 GHz / &lt;40 dBm | |

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Current, A

PoE In Ethernet port (12 - 57 V DC)
24
0.38
IP55
-30°..+70°C

\#72835
