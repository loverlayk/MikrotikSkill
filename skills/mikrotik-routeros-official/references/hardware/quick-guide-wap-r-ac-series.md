# Quick Guide - wAP R ac series

> Models: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit)

**Models: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit)**

![](./img/mt_logo_arrow_v2-02-106.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.2.3 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed.
:::

*This "wAP R ac" series Quick Guide covers models: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit),RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).*

*This is Wireless Network Device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [[https://mt.lv/um](https://mt.lv/um)](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, brochures, and more info about products at [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [[https://mt.lv/help](https://mt.lv/help)](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-121.png)

**First steps:**

- Open the cover and insert the SIM card. For the wAP R ac model, install your modem into miniPCIe slot;
- To install the modem, remove the screw located under the cover and split the case apart;
- Connect the device to the power source;
- Open network connections on your PC, search for MikroTik wireless network, and connect to it;
- Open the web browser, go to http://192.168.88.1 to start the configuration;
- User name: admin and there is no password by default (or, for some models, check user and wireless passwords on the sticker);
- Update the device by clicking the Check for updates on the right side and updating your RouterOS software to the latest version. Must have a valid SIM card inserted;
- To manually update the device, please go to https://mikrotik.com/download;
- Choose (ARM) packages for this device and download them to your PC;
- Upload downloaded packages to the (WebFig) (Files) menu and reboot the device;
- Updating your RouterOS software to the latest version will ensure the best performance, stability, and security updates;
- In the (QuickSet) menu set up the following: Choose your country, to apply country regulation settings;
- Set the *Installation* to indoors or outdoors, depending on the usage type;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- The socket-outlet shall be installed near the equipment and shall be easily accessible.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 45 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.2.3 или най-новата версия, за да се гарантира спазването на местните регулаторни разпоредби.
Крайните потребители са отговорни за спазването на местните разпоредби, включително работата в рамките на законни честотни канали, извеждане на продукция изисквания за захранване, окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е устройство за безжична мрежа. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [[https://mt.lv/um-bg](https://mt.lv/um-bg)](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, брошури и повече информация за продуктите на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [[https://mt.lv/help-bg](https://mt.lv/help-bg)](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-114.png)

**Първи стъпки:**

- Отворете капака и поставете SIM картата. За модела WAP R ac, инсталирайте вашия модем в слот miniPCIe;
- За да инсталирате модема, извадете винта, разположен под капака, и разделете кутията един от друг;
- Свържете устройството към източника на захранване;
- Отворете мрежовите връзки на вашия компютър, потърсете безжична мрежа MikroTik и се свържете към нея;
- Отворете уеб браузъра, отидете на http://192.168.88.1, за да стартирате конфигурацията;
- Потребителско име: admin и по подразбиране няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Актуализирайте устройството, като щракнете върху Check for updates от дясната страна и актуализирайте софтуера на RouterOS до най-новата версия. Трябва да е поставена валидна SIM карта;
- За да актуализирате устройството ръчно, моля, отидете на https://mikrotik.com/download;
- Изберете (ARM) пакети за това устройство и го изтеглете на вашия компютър;
- Качете изтеглените пакети в менюто (WebFig) (Fails) и рестартирайте устройството;
- Актуализирането на софтуера на RouterOS до най-новата версия ще гарантира най-добрата производителност, стабилност и актуализации за сигурност;
- В менюто (QuickSet) настройте следното: Изберете вашата страна, за да приложите настройките за регулиране на страната;
- Задайте инсталацията на *Outdoors* или на *Indoors*, в зависимост от вида на употреба;
- Настройте паролата за безжичната мрежа в лявото поле;
- Задайте паролата си на рутера в долното поле.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да бъде инсталиран на открито. Моля, прочетете внимателно инструкциите за монтаж преди да започнете инсталирането. Ако не използвате подходящия хардуер и конфигурация или не спазвате правилните процедури, това може да доведе до опасна ситуация за хората и да повреди системата на системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.
- Контактът трябва да бъде монтиран близо до оборудването и да бъде лесно достъпен.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация FCC, IC и Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 45 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Unijas iela 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.2.3 nebo na nejnovější verzi, aby bylo zajištěno dodržování předpisů místních úřadů.
Je odpovědností koncových uživatelů dodržovat místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupů požadavky na napájení, kabeláž a dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být profesionálně nainstalován.
Tato rychlá příručka „WAP R ac“ zahrnuje modely: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Toto je bezdrátové síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [[https://mt.lv/um-cs](https://mt.lv/um-cs)](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Technické specifikace, brožury a další informace o produktech na adrese [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [[https://mt.lv/help-cs](https://mt.lv/help-cs)](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-115.png)

**První kroky:**

- Otevřete kryt a vložte SIM kartu. U modelu WAP R ac nainstalujte modem do slotu miniPCIe;
- Chcete-li nainstalovat modem, odstraňte šroub umístěný pod krytem a rozdělte případ od sebe;
- Připojte zařízení ke zdroji napájení;
- Otevřete v počítači síťová připojení, vyhledejte bezdrátovou síť MikroTik a připojte se k ní;
- Spusťte webový prohlížeč, přejděte na adresu http://192.168.88.1 a spusťte konfiguraci;
- Uživatelské jméno: admin a ve výchozím nastavení není heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Aktualizujte zařízení kliknutím na Check for updates na pravé straně a aktualizujte software RouterOS na nejnovější verzi. Musí být vložena platná SIM karta;
- Chcete-li zařízení aktualizovat ručně, navštivte prosím https://mikrotik.com/download;
- Vyberte (ARM) balíčky pro toto zařízení a stáhněte si je do svého PC;
- Nahrajte stažené balíčky do nabídky (WebFig) (Files) a restartujte zařízení;
- Aktualizace softwaru RouterOS na nejnovější verzi zajistí nejlepší výkon, stabilitu a aktualizace zabezpečení;
- V nabídce (QuickSet) nastavte následující možnosti: Zvolte svou zemi, chcete-li použít nastavení regulace země;
- Nastavte instalaci na ''*Indoors*'' nebo ''*Outdoors*'' v závislosti na typu použití;
- Nastavte heslo bezdrátové sítě v levém poli;
- Ve spodním poli nastavte heslo routeru.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt lze instalovat venku. Před zahájením instalace si pozorně přečtěte montážní pokyny. Pokud nepoužijete odpovídající hardware a konfiguraci nebo nebudete dodržovat správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.
- Zásuvka musí být instalována v blízkosti zařízení a musí být snadno dostupná.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření FCC, IC a Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 45 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.2.3 eller den nyeste version for at sikre overholdelse af lokale myndigheders regler.
Det er slutbrugerens ansvar at følge lokale landes regler, herunder drift inden for lovlige frekvenskanaler, output strøm, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal være professionelt installeret.
:::

*Dette er trådløs netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [[https://mt.lv/um-da](https://mt.lv/um-da)](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, brochurer og mere info om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [[https://mt.lv/help-da](https://mt.lv/help-da)](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-115.png)

**Første trin:**

- Åbn dækslet, og indsæt SIM-kortet. For wAP R ac-modellen skal du installere dit modem i miniPCIe-slot;
- For at installere modemet skal du fjerne skruen, der er placeret under dækslet og dele kabinettet fra hinanden;
- Tilslut enheden til strømkilden;
- Åbn netværksforbindelser på din pc, søg efter MikroTik trådløse netværk og opret forbindelse til det;
- Åbn webbrowseren, gå til http://192.168.88.1 for at starte konfigurationen;
- Brugernavn: admin, og der er som standard ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløs adgangskoder på mærkaten);
- Opdater enheden ved at klikke på Check for updates til højre og opdatere din RouterOS-software til den nyeste version. Skal have et gyldigt SIM-kort indsat;
- For at manuelt opdatere enheden skal du gå til https://mikrotik.com/download;
- Vælg (ARM) -pakker til denne enhed, og download dem til din pc;
- Upload downloadede pakker til menuen (WebFig) (Files), og genstart enheden;
- Opdatering af din RouterOS-software til den nyeste version sikrer den bedste ydeevne, stabilitet og sikkerhedsopdateringer;
- Opsæt følgende i menuen (QuickSet): Vælg dit land for at anvende indstillinger for landegulering;
- Indstil installationen til *Indoors* eller *Outdoors*, afhængigt af brugstypen;
- Konfigurer din adgangskode til det trådløse netværk i det venstre felt;
- Konfigurer din routeradgangskode i det nederste felt.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt kan installeres udendørs. Læs monteringsvejledningen omhyggeligt, inden installationen påbegyndes. Undladelse af at bruge den korrekte hardware og konfiguration eller at følge de korrekte procedurer kan resultere i en farlig situation for mennesker og beskadigelse af syste m.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Stikkontakten skal installeres i nærheden af ​​udstyret og skal være let tilgængelig.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder FCC, IC og EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 45 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.2.3 oder die neueste Version aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten.
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle und der Ausgabe Anforderungen an Stromversorgung, Verkabelung und dynamische Frequenzauswahl (Dynamic Frequency Selection, DFS). Alle MikroTik Funkgeräte müssen professionell installiert.
:::

*Dies ist ein drahtloses Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [[https://mt.lv/um-de](https://mt.lv/um-de)](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [[https://mt.lv/help-de](https://mt.lv/help-de)](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-115.png)

**Erste Schritte:**

- Öffnen Sie die Abdeckung und legen Sie die SIM-Karte ein. Installieren Sie für das wAP R ac-Modell Ihr Modem im miniPCIe-Steckplatz;
- Entfernen Sie zum Installieren des Modems die Schraube unter der Abdeckung und teilen Sie das Gehäuse auseinander;
- Schließen Sie das Gerät an die Stromquelle an;
- Öffnen Sie Netzwerkverbindungen auf Ihrem PC, suchen Sie nach dem drahtlosen MikroTik-Netzwerk und stellen Sie eine Verbindung her;
- Öffnen Sie den Webbrowser und rufen Sie http://192.168.88.1 auf, um die Konfiguration zu starten;
- Benutzername: admin und standardmäßig gibt es kein Passwort (oder überprüfen Sie bei einigen Modellen die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Aktualisieren Sie das Gerät, indem Sie rechts auf Check for updates klicken und Ihre RouterOS-Software auf die neueste Version aktualisieren. Es muss eine gültige SIM-Karte eingelegt sein;
- Um das Gerät manuell zu aktualisieren, gehen Sie bitte zu https://mikrotik.com/download;
- Wählen Sie (ARM) -Pakete für dieses Gerät und laden Sie es auf Ihren PC herunter;
- Laden Sie heruntergeladene Pakete in das Menü (WebFig) (Files) hoch und starten Sie das Gerät neu;
- Durch das Aktualisieren Ihrer RouterOS-Software auf die neueste Version werden die besten Updates für Leistung, Stabilität und Sicherheit sichergestellt;
- Richten Sie im Menü (QuickSet) Folgendes ein: Wählen Sie Ihr Land aus, um die Länderregulierungseinstellungen anzuwenden;
- Stellen Sie die Installation je nach Nutzungsart auf „*Indoors*“ oder „*Outdoors*“ ein;
- Richten Sie im linken Feld Ihr WLAN-Passwort ein;
- Richten Sie Ihr Router-Passwort im unteren Feld ein.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt kann im Freien installiert werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie die richtige Hardware und Konfiguration nicht verwenden oder die richtigen Verfahren nicht befolgen, kann dies zu einer gefährlichen Situation für Personen und zu Schäden am System führen.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.
- Die Steckdose muss in der Nähe des Geräts installiert und leicht zugänglich sein.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den FCC-, IC- und EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 45 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.2.3 ή την τελευταία έκδοση για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς της τοπικής αυτοδιοίκησης.
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών, συμπεριλαμβανομένης της λειτουργίας εντός των νόμιμων καναλιών συχνότητας, της παραγωγής ισχύ, απαιτήσεις καλωδίωσης και απαιτήσεις δυναμικής επιλογής συχνότητας (DFS). Όλες οι ασύρματες συσκευές MikroTik πρέπει να είναι επαγγελματικά εγκατεστημένο.
Αυτός ο γρήγορος οδηγός της σειράς wAP R ac καλύπτει τα μοντέλα: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Αυτή είναι η ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [[https://mt.lv/um-el](https://mt.lv/um-el)](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [[https://mt.lv/help-el](https://mt.lv/help-el)](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-115.png)

**Πρώτα βήματα:**

- Ανοίξτε το κάλυμμα και τοποθετήστε την κάρτα SIM. Για το μοντέλο wap R ac, εγκαταστήστε το μόντεμ σας σε υποδοχή miniPCIe;
- Για να εγκαταστήσετε το μόντεμ, αφαιρέστε τη βίδα που βρίσκεται κάτω από το κάλυμμα και χωρίστε την θήκη;
- Συνδέστε τη συσκευή στην πηγή τροφοδοσίας;
- Ανοίξτε τις συνδέσεις δικτύου στον υπολογιστή σας, αναζητήστε ασύρματο δίκτυο MikroTik και συνδεθείτε με αυτό;
- Ανοίξτε το πρόγραμμα περιήγησης ιστού, μεταβείτε στη διεύθυνση http://192.168.88.1 για να ξεκινήσετε τη διαμόρφωση;
- Όνομα χρήστη: ''admin'' και δεν υπάρχει κωδικός πρόσβασης από προεπιλογή (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματης σύνδεσης στο αυτοκόλλητο);
- Ενημερώστε τη συσκευή κάνοντας κλικ στο κουμπί Check for updates στη δεξιά πλευρά και ενημερώνοντας το λογισμικό RouterOS στην πιο πρόσφατη έκδοση. Πρέπει να έχει τοποθετηθεί μια έγκυρη κάρτα SIM;
- Για μη αυτόματη ενημέρωση της συσκευής, μεταβείτε στη διεύθυνση https://mikrotik.com/download;
- Επιλέξτε (πακέτα) (ARM) για αυτήν τη συσκευή και κάντε λήψη στον υπολογιστή σας;
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού (WebFig) (Files) και επανεκκινήστε τη συσκευή;
- Η ενημέρωση του λογισμικού RouterOS στην πιο πρόσφατη έκδοση θα εξασφαλίσει τις καλύτερες επιδόσεις, σταθερότητα και ενημερώσεις ασφαλείας;
- Στο μενού (QuickSet) ρυθμίστε τα εξής: Επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις ρύθμισης χώρας;
- Ρυθμίστε την εγκατάσταση σε ''*Indoors*'' ή ''*Outdoors*'', ανάλογα με τον τύπο χρήσης;
- Ρυθμίστε τον κωδικό πρόσβασης ασύρματου δικτύου στο αριστερό πεδίο;
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή στο κάτω πεδίο.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν μπορεί να εγκατασταθεί σε εξωτερικούς χώρους. Παρακαλούμε διαβάστε προσεκτικά τις οδηγίες εγκατάστασης πριν ξεκινήσετε την εγκατάσταση. Η αδυναμία χρήσης του υλικού και των ρυθμίσεων διόρθωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και βλάβες στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.
- Η πρίζα πρέπει να είναι εγκατεστημένη κοντά στον εξοπλισμό και να είναι εύκολα προσβάσιμη.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας FCC, IC και Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 45 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Unijas iela 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.2.3 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales legales de frecuencia, salida alimentación, requisitos de cableado y requisitos de selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [[https://mt.lv/um-es](https://mt.lv/um-es)](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, folletos y más información sobre productos en [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [[https://mt.lv/help-es](https://mt.lv/help-es)](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-117.png)

**Primeros pasos:**

- Abra la tapa e inserte la tarjeta SIM. Para el modelo wAP R ac, instale su módem en la ranura miniPCIe;
- Para instalar el módem, retire el tornillo ubicado debajo de la cubierta y separe la carcasa;
- Conecte el dispositivo a la fuente de alimentación;
- Abra las conexiones de red en su PC, busque la red inalámbrica MikroTik y conéctese a ella;
- Abra el navegador web, vaya a http://192.168.88.1 para iniciar la configuración;
- Nombre de usuario: admin y no hay contraseña de forma predeterminada (o, en algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Actualice el dispositivo haciendo clic en (Verificar_actualizaciones) en el lado derecho y actualizando su software RouterOS a la última versión. Debe tener una tarjeta SIM válida insertada;
- Para actualizar manualmente el dispositivo, vaya a https://mikrotik.com/download;
- Elija los paquetes (ARM) para este dispositivo y descárguelo a su PC;
- Cargue los paquetes descargados en el menú (WebFig) (Files) y reinicie el dispositivo;
- Actualizar su software RouterOS a la última versión asegurará el mejor rendimiento, estabilidad y actualizaciones de seguridad;
- En el menú (QuickSet) configure lo siguiente: Elija su país, para aplicar la configuración de la regulación del país;
- Configure la Instalación en *Indoors* o *Outdoors*, según el tipo de uso;
- Configure su contraseña de red inalámbrica en el campo izquierdo;
- Configure la contraseña de su enrutador en el campo inferior.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto se puede instalar en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podrían producir situaciones peligrosas para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- La toma de corriente se instalará cerca del equipo y será de fácil acceso.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la FCC, IC y la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 45 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, protocolo 802.11b / g / n con antena PCB incorporada, ganancia máxima de 2.5 dBi.
Módulo inalámbrico integrado que funciona a 5 GHz, protocolo 802.11a / n / ac con antena PCB incorporada, ganancia máxima 2.5 dBi.

Rango de frecuencia (potencia de salida máxima): 2400-2483.5 MHz (30 dBm), 5725-5850 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.2.3 või uusimale versioonile.
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas toimimist seaduslikes sageduskanalites, väljund võimsus, kaabeldusnõuded ja dünaamilise sageduse valiku (DFS) nõuded. Kõik MikroTiku raadioseadmed peavad olema professionaalselt paigaldatud.
See "wAP R ac" -seeria lühijuhend hõlmab mudeleid: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*See on traadita võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [[https://mt.lv/um-et](https://mt.lv/um-et)](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [[https://mt.lv/help-et](https://mt.lv/help-et)](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-115.png)

**Esimesed sammud:**

- Avage kaas ja sisestage SIM-kaart. WAP R ac mudeli jaoks installige modem miniPCIe pesasse;
- Modemi paigaldamiseks eemaldage katte all olev kruvi ja jagage ümbris omavahel;
- Ühendage seade toiteallikaga;
- Avage oma arvuti võrguühendused, otsige MikroTik traadita võrku ja looge sellega ühendus;
- Konfiguratsiooni alustamiseks avage veebibrauser ja minge aadressile http://192.168.88.1
- Kasutajanimi: admin ja vaikimisi pole parooli (või mõne mudeli puhul kontrollige kleebiselt kasutaja ja traadita ühenduse paroole);
- Värskendage seadet, klõpsates paremal asuval nupul Check for updates ja värskendades tarkvara RouterOS uusimale versioonile. Peab olema sisestatud kehtiv SIM-kaart;
- Seadme käsitsi värskendamiseks minge https://mikrotik.com/download;
- Valige selle seadme (ARM) paketid ja laadige see oma arvutisse;
- Laadige allalaaditud paketid üles (WebFig) (Files) menüüsse ja taaskäivitage seade;
- RouterOS-i tarkvara värskendamine uusimale versioonile tagab parima jõudluse, stabiilsuse ja turbevärskendused;
- Seadistage (QuickSet) menüüs järgmine: Valige riik, et rakendada riigi regulatsioonisätteid;
- Määrake paigalduseks "*Indoors*" või "*Outdoors*", olenevalt kasutustüübist;
- Seadke traadita võrgu parool vasakpoolsesse välja;
- Seadistage ruuteri parool alumisel väljal.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- Seda toodet saab paigaldada välistingimustes. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhendit. Parandatud riistvara ja konfiguratsiooni kasutamata jätmine või õigete toimingute järgimata jätmine võib põhjustada inimestele ohtliku olukorra ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.
- Pistikupesa paigaldatakse seadme lähedusse ja see peab olema kergesti ligipääsetav.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab FCC, IC ja Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 45 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Unijas iela 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.2.3 -versioon tai uusimpaan versioon, jotta varmistetaan paikallisviranomaisten määräysten noudattaminen.
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtö teho, kaapelointivaatimukset ja dynaamisen taajuuden valinnan (DFS) vaatimukset. Kaikkien MikroTik-radiolaitteiden on oltava ammattimaisesti asennettu.
Tämä "wAP R ac" -sarjan pikaopas kattaa mallit: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [[https://mt.lv/um-fi](https://mt.lv/um-fi)](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [[https://mt.lv/help-fi](https://mt.lv/help-fi)](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-115.png)

**Ensiaskeleet:**

- Avaa kansi ja aseta SIM-kortti. Asenna modeemi miniPCIe-paikkaan wAP R ac -mallia varten;
- Asenna modeemi poistamalla kannen alla oleva ruuvi ja jaa kotelo erilleen;
- Kytke laite virtalähteeseen;
- Avaa verkkoyhteydet tietokoneellasi, etsi langaton MikroTik-verkko ja muodosta yhteys siihen;
- Avaa verkkoselain, siirry osoitteeseen http://192.168.88.1 aloittaaksesi määritykset;
- Käyttäjätunnus: admin ja salasanaa ei ole oletuksena (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Päivitä laite napsauttamalla Check for updates oikealla puolella ja päivittämällä RouterOS-ohjelmistosi uusimpaan versioon. Pitävä voimassa oleva SIM-kortti;
- Päivitä laite manuaalisesti siirtymällä osoitteeseen https://mikrotik.com/download
- Valitse (ARM) paketit tälle laitteelle ja lataa se tietokoneellesi;
- Lataa ladatut paketit (WebFig) (Files) -valikkoon ja käynnistä laite uudelleen;
- RouterOS-ohjelmiston päivittäminen uusimpaan versioon varmistaa parhaan suorituskyvyn, vakauden ja tietoturvapäivitykset;
- Määritä (QuickSet) -valikossa seuraava: Valitse maa, jos haluat käyttää maa-asetusasetuksia;
- Aseta asennus asetukseksi "*Indoors*" tai "Outdoors" käyttötyypistä riippuen;
- Aseta langattoman verkon salasana vasemmalle kentälle;
- Aseta reitittimen salasana alakenttään.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote voidaan asentaa ulkona. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikeiden laitteistojen ja kokoonpanojen käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa vaarallisen tilanteen ihmisille ja vaurioittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.
- Pistorasia on asennettava laitteen lähelle ja siihen on oltava helposti saatavilla.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on FCC: n, IC: n ja Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 45 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Unijas iela 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.2.3 ou la dernière version pour garantir la conformité aux réglementations des autorités locales.
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la sortie les exigences d'alimentation, de câblage et de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installé professionnellement.
:::

*Il s'agit d'un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [[https://mt.lv/um-fr](https://mt.lv/um-fr)](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, brochures et plus d'informations sur les produits sur [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [[https://mt.lv/help-fr](https://mt.lv/help-fr)](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-115.png)

**Premiers pas:**

- Ouvrez le couvercle et insérez la carte SIM. Pour le modèle wAP R ac, installez votre modem dans l'emplacement miniPCIe;
- Pour installer le modem, retirez la vis située sous le couvercle et séparez le boîtier;
- Connectez l'appareil à la source d'alimentation;
- Ouvrez les connexions réseau sur votre PC, recherchez le réseau sans fil MikroTik et connectez-vous à celui-ci;
- Ouvrez le navigateur Web, accédez à http://192.168.88.1 pour démarrer la configuration;
- Nom d'utilisateur: admin et il n'y a pas de mot de passe par défaut (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Mettez à jour l'appareil en cliquant sur Check for updates sur le côté droit et en mettant à jour votre logiciel RouterOS vers la dernière version. Doit avoir une carte SIM valide insérée;
- Pour mettre à jour manuellement l'appareil, rendez-vous sur https://mikrotik.com/download
- Choisissez les packages (ARM) pour cet appareil et téléchargez-les sur votre PC;
- Téléchargez les packages téléchargés dans le menu (WebFig) (Files) et redémarrez l'appareil;
- La mise à jour de votre logiciel RouterOS vers la dernière version garantira les meilleures mises à jour de performances, de stabilité et de sécurité;
- Dans le menu (QuickSet), configurez les éléments suivants: Choisissez votre pays pour appliquer les paramètres de réglementation du pays;
- Réglez l'installation sur *Indoors* ou *Outdoors*, selon le type d'utilisation;
- Configurez votre mot de passe de réseau sans fil dans le champ de gauche;
- Configurez le mot de passe de votre routeur dans le champ inférieur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit peut être installé à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration corrects ou de ne pas suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.
- La prise de courant doit être installée à proximité de l'équipement et doit être facilement accessible.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements FCC, IC et Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 45 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Unijas iela 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na RouterOS v7.2.3 ili najnoviju verziju kako bi se osigurala sukladnost s lokalnim propisima.
Odgovornost krajnjih korisnika je da slijede lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala zahtjevi za napajanje, kabliranje i zahtjevi za dinamički odabir frekvencije (DFS). Svi MikroTik radijski uređaji moraju biti profesionalno instaliran.
Ovaj "wAP R ac" serija Brzi vodič obuhvaća modele: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [[https://mt.lv/um-hr](https://mt.lv/um-hr)](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, brošure i više informacija o proizvodima na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [[https://mt.lv/help-hr](https://mt.lv/help-hr)](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-115.png)

**Prvi koraci:**

- Otvorite poklopac i umetnite SIM karticu. Za model WAP R ac, instalirajte svoj modem u utor miniPCIe;
- Da biste postavili modem, uklonite vijak koji se nalazi ispod poklopca i razdvojite kućište;
- Priključite uređaj na izvor napajanja;
- Otvorite mrežne veze na računalu, potražite MikroTik bežičnu mrežu i povežite se s njom;
- Otvorite web preglednik, idite na http://192.168.88.1 da biste pokrenuli konfiguraciju;
- Korisničko ime: admin i nema zaporke prema zadanim postavkama (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Ažurirajte uređaj klikom na Check for updates s desne strane i ažuriranjem softvera RouterOS na najnoviju verziju. Mora biti umetnuta valjana SIM kartica;
- Da biste ručno ažurirali uređaj, idite na https://mikrotik.com/download
- Odaberite (ARM) pakete za ovaj uređaj i preuzmite ga na svoje računalo;
- Učitajte preuzete pakete u izbornik (WebFig) (Files) i ponovno pokrenite uređaj;
- Ažuriranje softvera RouterOS na najnoviju verziju osigurat će najbolje performanse, stabilnost i sigurnosna ažuriranja;
- U izborniku (QuickSet) postavite sljedeće: Odaberite svoju zemlju da biste primijenili postavke regulacije zemlje;
- Postavite Instalaciju na *Indoors* ili *Outdoors*, ovisno o vrsti upotrebe;
- Postavljanje lozinke za bežičnu mrežu u lijevom polju;
- U donjem polju postavite lozinku za usmjerivač.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj se proizvod može instalirati na otvorenom. Prije početka instalacije pažljivo pročitajte upute za ugradnju. Ako ne koristite ispravni hardver i konfiguraciju ili ne slijedite ispravne postupke, može doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.
- Utičnica mora biti instalirana u blizini opreme i mora biti lako dostupna.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju FCC, IC i Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 45 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.2.3-ra vagy a legújabb verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést.
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon keresztüli működést is teljesítményre, kábelezésre és dinamikus frekvenciaválasztásra (DFS) vonatkozó követelmények. Az összes MikroTik rádiókészüléknek lennie kell szakszerűen telepítve.
Ez a "wAP R ac" sorozatú Gyors útmutató modellekre terjed ki: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Ez a vezeték nélküli hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [[https://mt.lv/um-hu](https://mt.lv/um-hu)](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki leírások, brosúrák és további információk a termékekről a [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) oldalon*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [[https://mt.lv/help-hu](https://mt.lv/help-hu)](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-114.png)

**Első lépések:**

- Nyissa fel a fedelet és helyezze be a SIM-kártyát. A wAP R ac modellhez telepítse a modemet a miniPCIe nyílásba;
- A modem beszereléséhez távolítsa el a fedél alatt található csavart, és ossza szét a házat;
- Csatlakoztassa a készüléket az áramforráshoz;
- Nyissa meg a számítógépes hálózati kapcsolatokat, keresse meg a MikroTik vezeték nélküli hálózatot, és csatlakozzon hozzá;
- Nyissa meg a webböngészőt, lépjen a http://192.168.88.1 webhelyre a konfiguráció elindításához;
- Felhasználónév: admin, és alapértelmezés szerint nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Frissítse az eszközt a jobb oldalon található Check for updates linkre kattintva, és frissítse a RouterOS szoftvert a legújabb verzióra. Érvényes SIM-kártyát kell behelyezni;
- Az eszköz manuális frissítéséhez kérjük, keresse fel a https://mikrotik.com/download oldalt
- Válasszon (ARM) csomagokat ehhez az eszközhöz, és töltse le a számítógépére;
- Töltse fel a letöltött csomagokat a (WebFig) (Files) menübe, és indítsa újra az eszközt;
- A RouterOS szoftver legfrissebb verziójára történő frissítése biztosítja a legjobb teljesítményt, stabilitást és biztonsági frissítéseket;
- A (QuickSet) menüben állítsa be a következőket: Válassza ki országát, hogy alkalmazza az országszabályozási beállításokat;
- Állítsa a telepítést "*Indoors*" vagy "*Outdoors*" értékre, a felhasználás típusától függően;
- Állítsa be a vezeték nélküli hálózat jelszavát a bal mezőben;
- Állítsa be az útválasztó jelszavát az alsó mezőben.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ez a termék kültéren is telepíthető. A telepítés megkezdése előtt olvassa el figyelmesen a szerelési útmutatót. A helyes hardver és konfiguráció használata vagy a helyes eljárások be nem tartása az emberek számára veszélyes helyzetet és a rendszer károsodását eredményezheti.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.
- Az aljzatot a berendezés közelében kell elhelyezni, és könnyen hozzáférhetőnek kell lennie.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az FCC, IC és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 45 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Unijas iela 2, Riga, Lettország, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.2.3 o alla versione più recente per garantire la conformità alle normative delle autorità locali.
È responsabilità dell'utente finale seguire le normative locali locali, incluso il funzionamento nei canali di frequenza legali, in uscita requisiti di alimentazione, cablaggio e selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installato professionalmente.
:::

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [[https://mt.lv/um-it](https://mt.lv/um-it)](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, brochure e maggiori informazioni sui prodotti su [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [[https://mt.lv/help-it](https://mt.lv/help-it)](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-115.png)

**Primi passi:**

- Aprire il coperchio e inserire la carta SIM. Per il modello wAP R ac, installare il modem nello slot miniPCIe;
- Per installare il modem, rimuovere la vite situata sotto il coperchio e dividere la custodia;
- Collegare il dispositivo alla fonte di alimentazione;
- Apri le connessioni di rete sul tuo PC, cerca la rete wireless MikroTik e connettiti ad essa;
- Aprire il browser Web, andare su http://192.168.88.1 per avviare la configurazione;
- Nome utente: admin e per impostazione predefinita non è presente alcuna password (o, per alcuni modelli, controllare l'utente e le password wireless sull'adesivo);
- Aggiorna il dispositivo facendo clic su Check for updates sul lato destro e aggiornando il software RouterOS alla versione più recente. Deve essere inserita una carta SIM valida;
- Per aggiornare manualmente il dispositivo, visitare https://mikrotik.com/download
- Scegli i pacchetti (ARM) per questo dispositivo e scaricalo sul tuo PC;
- Carica i pacchetti scaricati nel menu (WebFig) (Files) e riavvia il dispositivo;
- L'aggiornamento del software RouterOS all'ultima versione garantirà le migliori prestazioni, stabilità e aggiornamenti di sicurezza;
- Nel menu (QuickSet) impostare quanto segue: Scegliere il proprio paese per applicare le impostazioni relative alle normative nazionali;
- Impostare l'Installazione su ''*indoor*'' o ''*outdoor*'', a seconda del tipo di utilizzo;
- Imposta la password della tua rete wireless nel campo a sinistra;
- Imposta la password del router nel campo inferiore.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e acquisire familiarità con le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto può essere installato all'aperto. Leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il rispetto delle procedure corrette potrebbe comportare una situazione pericolosa per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.
- La presa deve essere installata vicino all'apparecchiatura e deve essere facilmente accessibile.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni FCC, IC e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 45 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Unijas iela 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.2.3 eða nýjustu útgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga.
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum, þar með talið rekstri innan löglegra tíðnisviða, framleiðsla afl, kaðall kröfur og Dynamic Frequency Val (DFS) kröfur. Öll MikroTik útvarpstæki verða að vera faglega sett upp.
Þessi „wAP R ac“ röð flýtileiðbeiningar ná yfir gerðir: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Þetta er þráðlaust net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [[https://mt.lv/um-is](https://mt.lv/um-is)](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tæknilýsingar, bæklingar og frekari upplýsingar um vörur á [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [[https://mt.lv/help-is](https://mt.lv/help-is)](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-115.png)

**Fyrstu skrefin:**

- Opnaðu hlífina og settu SIM kortið í. Fyrir wAP R AC líkanið skaltu setja mótaldið í miniPCIe raufina;
- Til að setja mótaldið upp, fjarlægðu skrúfuna sem er staðsett undir hlífinni og skiptu um borð í sundur;
- Tengdu tækið við aflgjafann;
- Opnaðu nettengingar á tölvunni þinni, leitaðu að þráðlausu MikroTik neti og tengdu það;
- Opnaðu vafrann, farðu á http://192.168.88.1 til að hefja stillingarnar;
- Notandanafn: admin og það er ekkert lykilorð sjálfgefið (eða, fyrir sumar gerðir, athugaðu notenda- og þráðlaus lykilorð á límmiðanum);
- Uppfærðu tækið með því að smella á Check for updates hægra megin og uppfæra RouterOS hugbúnaðinn í nýjustu útgáfuna. Verður að hafa gilt SIM-kort í;
- Til að uppfæra tækið handvirkt, vinsamlegast farðu https://mikrotik.com/download
- Veldu (ARM) pakka fyrir þetta tæki og halaðu því niður á tölvuna þína;
- Settu niður niðurhalaða pakka í (WebFig) (Files) valmyndina og endurræstu tækið;
- Að uppfæra RouterOS hugbúnaðinn þinn í nýjustu útgáfuna mun tryggja besta árangur, stöðugleika og öryggisuppfærslur;
- Í (QuickSet) valmyndinni settu upp eftirfarandi: Veldu land þitt, til að beita stillingum landsreglugerðar;
- Stilltu uppsetninguna á ''*Indoors*'' eða ''*Outdoors*'', allt eftir notkunartegundinni;
- Settu upp lykilorð þráðlausa netsins í vinstri reitnum;
- Settu upp lykilorð routersins í neðsta reitnum.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Hægt er að setja þessa vöru utandyra. Vinsamlegast lestu festingarleiðbeiningarnar vandlega áður en þú byrjar uppsetningu. Bilun í að nota leiðréttan vélbúnað og stillingar eða til að fylgja réttum aðferðum gæti valdið hættulegu ástandi fyrir fólk og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
- Innstungan skal vera nálægt búnaðinum og vera aðgengileg.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við FCC, IC og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 45 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Unijas iela 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.2.3 eller den nyeste versjonen for å sikre samsvar med lokale myndighetsbestemmelser.
Det er sluttbrukernes ansvar å følge lokale lands forskrifter, inkludert drift innen lovlige frekvenskanaler, output strøm, kabling og krav til dynamisk frekvensvalg (DFS). Alle MikroTik-radioenheter må være profesjonelt installert.
:::

*Dette er trådløs nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [[https://mt.lv/um-no](https://mt.lv/um-no)](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, brosjyrer og mer info om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [[https://mt.lv/help-no](https://mt.lv/help-no)](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-115.png)

**Første steg:**

- Åpne dekselet og sett inn SIM-kortet. For wAP R ac-modellen, installer modemet i miniPCIe-sporet;
- For å installere modemet, fjern skruen som er plassert under dekselet og del saken fra hverandre;
- Koble enheten til strømkilden;
- Åpne nettverkstilkoblinger på PCen din, søk etter det trådløse MikroTik-nettverket og koble til det;
- Åpne nettleseren, gå til http://192.168.88.1 for å starte konfigurasjonen;
- Brukernavn: admin og det er ikke noe passord som standard (eller, for noen modeller, sjekk bruker- og trådløst passord på klistremerket);
- Oppdater enheten ved å klikke på Check for updates på høyre side og oppdatere RouterOS-programvaren til den nyeste versjonen. Må ha et gyldig SIM-kort satt inn;
- For å oppdatere enheten manuelt, gå til https://mikrotik.com/download
- Velg (ARM) pakker for denne enheten og last dem ned til PC-en din;
- Last opp nedlastede pakker til (WebFig) (Files) -menyen, og start enheten på nytt;
- Oppdatering av RouterOS-programvaren til den nyeste versjonen vil sikre best ytelse, stabilitet og sikkerhetsoppdateringer;
- Konfigurer følgende i (QuickSet) -menyen: Velg ditt land for å bruke innstillinger for landsregulering;
- Sett installasjonen til *Indoors* eller *Outdoors*, avhengig av brukstype;
- Sett opp passordet for det trådløse nettverket i det venstre feltet;
- Sett opp rutepassordet ditt i nederste felt.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet kan installeres utendørs. Les monteringsanvisningene nøye før du begynner installasjonen. Unnlatelse av å bruke den rette maskinvaren og konfigurasjonen eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på syste m.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.
- Stikkontakten skal installeres i nærheten av utstyret og skal være lett tilgjengelig.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med FCC, IC og EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 45 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.2.3“ arba naujausią versiją, kad būtų užtikrinta atitiktis vietinės valdžios nuostatoms.
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi, įskaitant veikimą legaliais dažnių kanalais galios, kabelių ir dinaminio dažnio pasirinkimo (DFS) reikalavimai. Visi „MikroTik“ radijo prietaisai turi būti profesionaliai sumontuota.
Šis „wAP R ac“ serijos trumpasis vadovas apima modelius: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [[https://mt.lv/um-lt](https://mt.lv/um-lt)](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, brošiūros ir daugiau informacijos apie gaminius rasite [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [[https://mt.lv/help-lt](https://mt.lv/help-lt)](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-114.png)

**Pirmieji žingsniai:**

- Atidarykite dangtelį ir įdėkite SIM kortelę. Jei norite naudoti „wAP R ac“ modelį, modemą įdiekite į „miniPCIe“ lizdą;
- Norėdami įdiegti modemą, nuimkite varžtą, esantį po dangteliu, ir padalinkite korpusą;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Atidarykite tinklo jungtis savo kompiuteryje, suraskite „MikroTik“ belaidį tinklą ir prisijunkite prie jo;
- Atidarykite žiniatinklio naršyklę, eikite į http://192.168.88.1 ir pradėkite konfigūraciją;
- Vartotojo vardas: admin ir pagal numatytuosius nustatymus nėra slaptažodžio (arba kai kuriuose modeliuose patikrinkite naudotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Atnaujinkite įrenginį spustelėdami Check for updates dešinėje ir atnaujindami „RouterOS“ programinę įrangą į naujausią versiją. Turi būti įdėta galiojanti SIM kortelė;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į https://mikrotik.com/download
- Pasirinkite (ARM) šio įrenginio paketus ir atsisiųskite juos į savo kompiuterį;
- Įkelkite atsisiųstus paketus į (WebFig) (Fails) meniu ir paleiskite įrenginį iš naujo;
- Atnaujinę „RouterOS“ programinę įrangą į naujausią versiją, užtikrinsite geriausią našumą, stabilumą ir saugos atnaujinimus;
- Meniu („QuickSet“) nustatykite: Pasirinkite savo šalį, kad pritaikytumėte šalies reguliavimo parametrus;
- Nustatykite diegimą į „Indoors“ arba „Outdoors“, priklausomai nuo naudojimo tipo;
- Kairiajame lauke nustatykite belaidžio tinklo slaptažodį;
- Apatiniame lauke nustatykite maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šį gaminį galima montuoti lauke. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite pataisytos aparatūros ir konfigūracijos arba nesiimsite teisingų procedūrų, galite sukelti pavojingą situaciją žmonėms ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.
- Kištukinis lizdas turi būti įrengtas šalia įrangos ir turi būti lengvai pasiekiamas.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka FCC, IC ir Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 45 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Unijas iela 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.2.3 vai jaunāku versiju, lai nodrošinātu atbilstību vietējiem likuma normatīviem.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm ir jābūt profesionāli uzstādītām.
Šī "wAP R ac" sērijas instrukcija ietver sevī modeļus: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [[https://mt.lv/um-lv](https://mt.lv/um-lv)](https://mt.lv/um-lv), lai iegūtu pilnīgu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai ar papildus informāciju atrodama vietnē [[https://mt.lv/help-lv](https://mt.lv/help-lv)](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-115.png)

**Pirmie soļi:**

- Atveriet produkta vāciņu un ievietojiet SIM karti. WAP R ac modelim uzstādiet Jūsu modemu miniPCIe slotā;
- Lai uzstādītu modemu, atskrūvējiet skrūvi, kas atrodas zem vāciņa, un sadaliet korpusu divās daļās;
- Pievienojiet ierīci strāvas avotam;
- Datorā atveriet tīkla savienojumus, atrodiet MikroTik bezvadu tīklu un izveidojiet savienojumu ar to;
- Atveriet tīmekļa pārlūku, dodieties uz vietni http://192.168.88.1, lai sāktu konfigurēšanu;
- Lietotājvārds: admin, un pēc noklusējuma nav paroles (vai dažiem modeļiem pārbaudiet uzlīmes lietotāja un bezvadu paroles);
- Atjauniniet ierīci, labajā pusē noklikšķinot uz Check for updates un atjauninot programmatūru RouterOS uz jaunāko versiju. Jābūt ievietotai derīgai SIM kartei;
- Lai atjauninātu ierīci, kad SIM karte nav pieejama, lūdzu, dodieties uz https://mikrotik.com/download
- Izvēlieties (ARM) pakas, kuras paredzētas Jūsu ierīcei un lejupielādējiet to savā datorā;
- Augšupielādējiet lejupielādētās pakas izvēlnē (WebFig) (Files) un restartējiet ierīci;
- RouterOS programmatūras atjaunināšana uz jaunāko versiju nodrošinās vislabāko veiktspēju, stabilitāti un drošības atjauninājumus;
- Izvēlnē (QuickSet) iestatiet tālāk minētās lietas: Izvēlieties valsti, lai lietotu valsts normatīvajos aktos paredzētos iestatījumus;
- *Installation* sadaļā iestatiet *Indoors* vai *Outdoors*, atkarībā no lietošanas veida;
- Kreisajā laukā ievadiet bezvadu tīkla paroli;
- Apakšējā laukā ievadiet maršrutētāja paroli.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Uzstādītājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem normatīviem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šo izstrādājumu var uzstādīt ārpus telpām. Pirms instalēšanas, lūdzu, uzmanīgi izlasiet montāžas instrukcijas. Nepareizas aparatūras un nepareizas konfigurācijas lietošana var izraisīt bīstamu situāciju cilvēkiem un bojāt sistēmu.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.
- Kontaktligzdai jābūt uzstādītai netālu no iekārtas un tai jābūt viegli pieejamai.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst FCC, IC un Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jālieto ne tuvāk par 45 centimetriem no ķermeņa vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Unijas iela 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.2.3 jew l-aħħar verżjoni biex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali.
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż l-operazzjoni fil-kanali tal-frekwenza legali, tal-ħruġ qawwa, ħtiġiet ta 'kejbils, u Reklamar ta' Frekwenza Dinamika (DFS). L-apparati kollha tar-radju MikroTik għandhom ikunu installat professjonalment.
Din is-serje "wAP R ac" ta 'Gwida ta' malajr tkopri mudelli: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Dan huwa Apparat tan-Netwerk Wireless. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [[https://mt.lv/um-mt](https://mt.lv/um-mt)](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, fuljetti u aktar tagħrif dwar il-prodotti fuq [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [[https://mt.lv/help-mt](https://mt.lv/help-mt)](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-115.png)

**L-ewwel passi:**

- Iftaħ il-qoxra u daħħal il-SIM card. Għall-mudell wAP R ac, installa l-modem tiegħek fis-slot miniPCIe;
- Biex tinstalla l-modem, neħħi l-kamin li jinsab taħt il-qoxra u aqsam il-kaxxa minn xulxin;
- Qabbad it-tagħmir mas-sors tal-enerġija;
- Iftaħ konnessjonijiet għan-netwerk fuq il-PC tiegħek, fittex netwerk mingħajr fili MikroTik u qabbad miegħu;
- Iftaħ il-web browser, mur http://192.168.88.1 biex tibda l-konfigurazzjoni;
- Isem tal-utent: admin u m'hemm l-ebda password awtomatikament (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u wireless fuq l-istiker);
- Aġġorna l-apparat billi tikklikkja l- Check for updates fuq in-naħa tal-lemin u taġġorna s-softwer RouterOS għall-aħħar verżjoni. Irid ikollha karta SIM valida mdaħħla;
- Biex taġġorna manwalment it-tagħmir, jekk jogħġbok mur https://mikrotik.com/download
- Agħżel (ARM) pakketti għal dan l-apparat u niżżlu fil-PC tiegħek;
- Qiegħed il-pakketti mniżżla fil-menu (WebFig) (Fails) u rristartja l-apparat;
- L-aġġornament tas-softwer RouterOS tiegħek għall-aħħar verżjoni se jiżgura l-aħjar prestazzjoni, stabbiltà u aġġornamenti tas-sigurtà;
- Fil-menu (QuickSet) waqqaf dan li ġej: Agħżel il-pajjiż tiegħek, biex tapplika l-issettjar tar-regolamentazzjoni tal-pajjiż;
- Issettja l-Installazzjoni għal *Indoors* jew *Outdoors*, skond it-tip ta 'użu;
- Twaqqaf il-password tan-netwerk bla fili tiegħek fil-qasam tax-xellug;
- Twaqqaf il-password tar-router tiegħek fil-qasam tal-qiegħ.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott jista 'jiġi installat barra. Jekk jogħġbok aqra l-istruzzjonijiet tal-immuntar bir-reqqa qabel tibda l-installazzjoni. Jekk tonqos milli tuża l- hardware u l-konfigurazzjoni korretta jew issegwi l-proċeduri t-tajba tista ’tirriżulta f’sitwazzjoni perikoluża għan-nies u tagħmel ħsara lis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.
- Is-socket-outlet għandu jkun installat ħdejn it-tagħmir u għandu jkun faċilment aċċessibbli.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta 'FCC, IC u l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 45 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Unijas iela 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.2.3 of de nieuwste versie om te voldoen aan de voorschriften van de lokale autoriteiten.
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften, inclusief werking binnen wettelijke frequentiekanalen, te volgen vermogen, bekabelingseisen en Dynamic Frequency Selection (DFS) -vereisten. Alle MikroTik-radioapparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een draadloos netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [[https://mt.lv/um-nl](https://mt.lv/um-nl)](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, brochures en meer informatie over producten op [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [[https://mt.lv/help-nl](https://mt.lv/help-nl)](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-115.png)

**Eerste stappen:**

- Open het klepje en plaats de simkaart. Voor het wAP R ac-model installeert u uw modem in de miniPCIe-sleuf;
- Om de modem te installeren, verwijdert u de schroef onder het deksel en splitst u de behuizing uit elkaar;
- Sluit het apparaat aan op de stroombron;
- Open netwerkverbindingen op uw pc, zoek naar MikroTik draadloos netwerk en maak verbinding;
- Open de webbrowser, ga naar http://192.168.88.1 om de configuratie te starten;
- Gebruikersnaam: admin en er is standaard geen wachtwoord (of controleer bij sommige modellen de gebruikers- en draadloze wachtwoorden op de sticker);
- Werk het apparaat bij door aan de rechterkant op Check for updates te klikken en uw RouterOS-software bij te werken naar de nieuwste versie. Er moet een geldige simkaart zijn geplaatst;
- Ga naar https://mikrotik.com/download om het apparaat handmatig bij te werken;
- Kies (ARM) pakketten voor dit apparaat en download het naar uw pc;
- Upload gedownloade pakketten naar het menu (WebFig) (Files) en start het apparaat opnieuw op;
- Bijwerken van uw RouterOS-software naar de nieuwste versie zorgt voor de beste prestaties, stabiliteit en beveiligingsupdates;
- Stel in het menu (QuickSet) het volgende in: Kies uw land om de instellingen voor landregelgeving toe te passen;
- Postavite instalaciju na ''*Indoors*'' ili ''na *Outdoors*'', ovisno o vrsti upotrebe;
- Stel uw draadloze netwerkwachtwoord in het linker veld in;
- Stel uw routerwachtwoord in het onderste veld in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures voor het voorkomen van ongevallen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die door de fabrikant zijn goedgekeurd en die zich in de originele verpakking van dit product bevinden.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product kan buitenshuis worden geïnstalleerd. Lees de montage-instructies zorgvuldig voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stroomadapter uit het stopcontact te halen.
- Het stopcontact moet dichtbij de apparatuur worden geïnstalleerd en gemakkelijk toegankelijk zijn.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de FCC-, IC- en EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 45 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.2.3 lub najnowszej wersji, aby zapewnić zgodność z przepisami władz lokalnych.
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości wymagania dotyczące zasilania, okablowania i dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik muszą być profesjonalnie zainstalowany.
Niniejsza skrócona instrukcja „serii WAP R ac” obejmuje modele: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [[https://mt.lv/um-pl](https://mt.lv/um-pl)](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Dane techniczne, broszury i więcej informacji o produktach na stronie [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [[https://mt.lv/help-pl](https://mt.lv/help-pl)](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-115.png)

**Pierwsze kroki:**

- Otwórz pokrywę i włóż kartę SIM. W przypadku modelu wAP R ac zainstaluj modem w gnieździe miniPCIe;
- Aby zainstalować modem, wykręć śrubę znajdującą się pod pokrywą i rozdziel obudowę;
- Podłącz urządzenie do źródła zasilania;
- Otwórz połączenia sieciowe na komputerze, wyszukaj sieć bezprzewodową MikroTik i połącz się z nią;
- Otwórz przeglądarkę internetową, przejdź do strony http://192.168.88.1, aby rozpocząć konfigurację;
- Nazwa użytkownika: admin i domyślnie nie ma hasła (lub w przypadku niektórych modeli sprawdź hasła użytkownika i hasła bezprzewodowe na naklejce);
- Zaktualizuj urządzenie, klikając Check for updates po prawej stronie i aktualizując oprogramowanie RouterOS do najnowszej wersji. Musi być włożona ważna karta SIM;
- Aby ręcznie zaktualizować urządzenie, przejdź na stronę https://mikrotik.com/download
- Wybierz pakiety (ARM) dla tego urządzenia i pobierz je na swój komputer;
- Prześlij pobrane pakiety do menu (WebFig) (Files) i uruchom ponownie urządzenie;
- Aktualizacja oprogramowania RouterOS do najnowszej wersji zapewni najlepszą wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu (QuickSet) skonfiguruj: Wybierz swój kraj, aby zastosować ustawienia przepisów krajowych;
- Ustaw instalację na ''*Indoors*'' lub ''*Outdoors*'', w zależności od typu użytkowania;
- Ustaw hasło sieci bezprzewodowej w lewym polu;
- Ustaw hasło routera w dolnym polu.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt można zainstalować na zewnątrz. Proszę uważnie przeczytać instrukcję montażu przed rozpoczęciem instalacji. Niezastosowanie odpowiedniego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może spowodować zagrożenie dla ludzi i uszkodzenie systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.
- Gniazdko elektryczne powinno być zainstalowane w pobliżu urządzenia i powinno być łatwo dostępne.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie FCC, IC i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 45 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Unijas iela 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.2.3 ou a versão mais recente para garantir a conformidade com os regulamentos das autoridades locais.
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais de frequência legal, saída requisitos de alimentação, cabeamento e Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalado profissionalmente.
Este Guia Rápido da série "wAP R ac" abrange os modelos: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Este é o dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [[https://mt.lv/um-pt](https://mt.lv/um-pt)](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [[https://mt.lv/help-pt](https://mt.lv/help-pt)](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-115.png)

**Primeiros passos:**

- Abra a tampa e insira o cartão SIM. Para o modelo wAP R ac, instale o modem no slot miniPCIe;
- Para instalar o modem, remova o parafuso localizado sob a tampa e divida a caixa;
- Conecte o dispositivo à fonte de energia;
- Abra as conexões de rede no seu PC, procure a rede sem fio MikroTik e conecte-se a ela;
- Abra o navegador da web, vá para http://192.168.88.1 para iniciar a configuração;
- Nome de usuário: admin e não há senha por padrão (ou, para alguns modelos, verifique as senhas de usuário e de rede sem fio no adesivo);
- Atualize o dispositivo clicando em Check for updates no lado direito e atualizando o software RouterOS para a versão mais recente. Deve ter um cartão SIM válido inserido;
- Para atualizar manualmente o dispositivo, acesse https://mikrotik.com/download
- Escolha os pacotes (ARM) deste dispositivo e faça o download para o seu PC;
- Carregue os pacotes baixados no menu (WebFig) (Files) e reinicie o dispositivo;
- A atualização do software RouterOS para a versão mais recente garantirá as melhores atualizações de desempenho, estabilidade e segurança;
- No menu (QuickSet), configure o seguinte: Escolha seu país para aplicar as configurações de regulamentação do país;
- Configure a Instalação para ''*indoors*'' ou ''*outdoors*'', dependendo do tipo de uso;
- Configure sua senha de rede sem fio no campo esquerdo;
- Configure a senha do seu roteador no campo inferior.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto pode ser instalado ao ar livre. Leia atentamente as instruções de montagem antes de iniciar a instalação. A não utilização do hardware e configuração corretos ou do não cumprimento dos procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danificar o sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.
- A tomada deverá ser instalada próxima ao equipamento e deverá ser de fácil acesso.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da FCC, IC e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 45 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.2.3 sau cea mai recentă versiune pentru a asigura respectarea reglementărilor autorității locale.
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale cerințe de alimentare, cabluri și cerințe de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie să fie instalat profesional.
Acest ghid rapid seria „wAP R ac” acoperă modele: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Acesta este dispozitivul de rețea wireless. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [[https://mt.lv/um-ro](https://mt.lv/um-ro)](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, broșuri și mai multe informații despre produse la [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [[https://mt.lv/help-ro](https://mt.lv/help-ro)](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-112.png)

**Primii pasi:**

- Deschideți capacul și introduceți cartela SIM. Pentru modelul wAP R ac, instalați-vă modemul în slotul miniPCIe;
- Pentru a instala modemul, îndepărtați șurubul situat sub capac și despărțiți carcasa;
- Conectați dispozitivul la sursa de alimentare;
- Deschideți conexiunile de rețea pe computer, căutați rețeaua wireless MikroTik și conectați-vă la aceasta;
- Deschideți browserul web, accesați http://192.168.88.1 pentru a începe configurația;
- Nume de utilizator: admin și nu există o parolă în mod implicit (sau, pentru unele modele, verificați parolele de utilizator și wireless pe autocolant);
- Actualizați dispozitivul dând clic pe (Verificați_pentru data) din partea dreaptă și actualizați software-ul RouterOS la cea mai recentă versiune. Trebuie să fie introdusă o cartelă SIM valabilă;
- Pentru a actualiza manual dispozitivul, accesați https://mikrotik.com/download
- Alegeți pachetele (ARM) pentru acest dispozitiv și descărcați-l pe computer;
- Încărcați pachetele descărcate în meniul (WebFig) (Files) și reporniți dispozitivul;
- Actualizarea software-ului RouterOS la cea mai recentă versiune va asigura cele mai bune performanțe, stabilitate și actualizări de securitate;
- În meniul (QuickSet) configurați următoarele: Alegeți țara dvs. pentru a aplica setările de reglementare a țării;
- Defina a instalação para *Indoors* ou *Outdoors*, dependendo do tipo de uso;
- Configurați parola pentru rețeaua wireless în câmpul din stânga;
- Configurați parola routerului în câmpul de jos.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs poate fi instalat în aer liber. Citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Nefolosirea hardware-ului și configurației corecte sau respectarea procedurilor corecte poate duce la o situație periculoasă pentru oameni și deteriorarea sistemului m.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.
- Priza trebuie instalată în apropierea echipamentului și trebuie să fie ușor accesibilă.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații FCC, IC și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 45 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.2.3 alebo na najnovšiu verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov.
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny, vrátane prevádzky v rámci legálnych frekvenčných kanálov a výstupov požiadavky na energiu, kabeláž a dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť profesionálne nainštalovaný.
Táto stručná príručka „WAP R ac“ zahŕňa modely: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [[https://mt.lv/um-sk](https://mt.lv/um-sk)](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Technické špecifikácie, brožúry a ďalšie informácie o produktoch nájdete na adrese [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [[https://mt.lv/help-sk](https://mt.lv/help-sk)](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-115.png)

**Prvé kroky:**

- Otvorte kryt a vložte SIM kartu. V prípade modelu wAP R ac nainštalujte modem do slotu miniPCIe;
- Ak chcete nainštalovať modem, odstráňte skrutku umiestnenú pod krytom a oddeľte puzdro od seba;
- Pripojte zariadenie k zdroju napájania;
- Na počítači otvorte sieťové pripojenia, vyhľadajte bezdrôtovú sieť MikroTik a pripojte sa k nej;
- Otvorte webový prehľadávač, prejdite na stránku http://192.168.88.1 a spustite konfiguráciu;
- Používateľské meno: admin a v predvolenom nastavení nie je žiadne heslo (alebo pri niektorých modeloch skontrolujte používateľské a bezdrôtové heslá na nálepke);
- Aktualizujte zariadenie kliknutím na Check for updates na pravej strane a aktualizujte softvér RouterOS na najnovšiu verziu. Musíte mať vloženú platnú SIM kartu;
- Ak chcete zariadenie aktualizovať ručne, prejdite na stránku https://mikrotik.com/download
- Vyberte (ARM) balíky pre toto zariadenie a stiahnite ich do svojho PC;
- Nahrajte stiahnuté balíčky do ponuky (WebFig) (Files) a reštartujte zariadenie;
- Aktualizácia softvéru RouterOS na najnovšiu verziu zabezpečí najlepší výkon, stabilitu a aktualizácie zabezpečenia;
- V ponuke (QuickSet) nastavte nasledujúce možnosti: Vyberte svoju krajinu, ak chcete použiť nastavenia krajiny;
- Nastavte Inštaláciu na *Indoors* alebo *Outdoors* v závislosti od typu použitia;
- V ľavom poli nastavte heslo bezdrôtovej siete;
- V spodnom poli nastavte heslo smerovača.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je možné nainštalovať vonku. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nebudete používať správny hardvér a konfiguráciu alebo nebudete postupovať správne, môže to mať za následok nebezpečnú situáciu pre ľudí a poškodenie systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.
- Zásuvka musí byť inštalovaná v blízkosti zariadenia a musí byť ľahko dostupná.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu FCC, IC a Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 45 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.2.3 ali najnovejšo različico, da se zagotovi skladnost z lokalnimi predpisi.
Končni uporabniki so odgovorni za sledenje lokalnim predpisom, vključno z delovanjem v legalnih frekvenčnih kanalih, za doseganje rezultatov napajanje, zahteve za kabliranje in zahteve za dinamično izbiro frekvence (DFS). Vse radijske naprave MikroTik morajo biti strokovno nameščen.
Ta hitri vodnik serije "wAP R ac" zajema modele: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [[https://mt.lv/um-sl](https://mt.lv/um-sl)](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Tehnične specifikacije, brošure in več informacij o izdelkih na [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [[https://mt.lv/help-sl](https://mt.lv/help-sl)](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-115.png)

**Prvi koraki:**

- Odprite pokrov in vstavite kartico SIM. Za model WAP R ac namestite svoj modem v režo miniPCIe;
- Če želite namestiti modem, odstranite vijak, ki se nahaja pod pokrovom, in ločite ohišje;
- Napravo priključite na vir napajanja;
- V računalniku odprite omrežne povezave, poiščite brezžično omrežje MikroTik in se povežite z njim;
- Odprite spletni brskalnik, za začetek konfiguracije pojdite na http://192.168.88.1.
- Uporabniško ime: admin in privzeto ni gesla (ali pri nekaterih modelih preverite uporabniško in brezžično geslo na nalepki);
- Posodobite napravo tako, da na desni strani kliknete Check for updates in posodobite programsko opremo RouterOS na najnovejšo različico. Vstaviti mora veljavno kartico SIM;
- Če želite ročno posodobiti napravo, obiščite https://mikrotik.com/download
- Izberite (ARM) pakete za to napravo in jo naložite v svoj računalnik;
- Naložite pakete v meni (WebFig) (Files) in znova zaženite napravo;
- Posodobitev programske opreme RouterOS na najnovejšo različico bo zagotovila najboljše delovanje, stabilnost in varnostne posodobitve;
- V meniju (QuickSet) nastavite naslednje: Izberite državo in uporabite nastavitve države;
- Nastavite namestitev na ''*Indoors*'' ali ''*Outdoors*'', odvisno od vrste uporabe;
- V levem polju nastavite geslo za brezžično omrežje;
- V spodnjem polju nastavite geslo usmerjevalnika.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek lahko namestite na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Neuporaba ustrezne strojne opreme in konfiguracije ali upoštevanje pravilnih postopkov lahko povzroči nevarne razmere za ljudi in poškoduje sistem.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.
- Vtičnica mora biti nameščena v bližini opreme in mora biti lahko dostopna.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju FCC, IC in Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 45 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.2.3 eller den senaste versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser.
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, output kraft, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste vara professionellt installerat.
:::

*Det här är trådlöst nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [[https://mt.lv/um-sv](https://mt.lv/um-sv)](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, broschyrer och mer information om produkter på [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [[https://mt.lv/help-sv](https://mt.lv/help-sv)](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-115.png)

**Första stegen:**

- Öppna luckan och sätt i SIM-kortet. För wAP R ac-modellen installerar du ditt modem i miniPCIe-kortplatsen;
- För att installera modemet, ta bort skruven som sitter under locket och dela höljet isär;
- Anslut enheten till strömkällan;
- Öppna nätverksanslutningar på din dator, sök efter MikroTik trådlösa nätverk och anslut till det;
- Öppna webbläsaren, gå till http://192.168.88.1 för att starta konfigurationen;
- Användarnamn: admin och det finns inget lösenord som standard (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på dekalen);
- Uppdatera enheten genom att klicka på Check for updates till höger och uppdatera din RouterOS-programvara till den senaste versionen. Måste ha ett giltigt SIM-kort isatt;
- För att manuellt uppdatera enheten, gå till https://mikrotik.com/download
- Välj (ARM) paket för den här enheten och ladda ner det till din dator;
- Ladda upp nedladdade paket till (WebFig) (Files) -menyn och starta om enheten;
- Att uppdatera din RouterOS-programvara till den senaste versionen kommer att garantera bästa prestanda, stabilitet och säkerhetsuppdateringar;
- Ställ in följande i (QuickSet) -menyn: Välj ditt land, för att tillämpa landets regleringsinställningar;
- Ställ in installationen på *Indoors* eller *Outdoors*, beroende på användningstyp;
- Ställ in ditt lösenord för det trådlösa nätverket i det vänstra fältet;
- Ställ in ditt routerlösenord i det nedre fältet.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt kan installeras utomhus. Läs monteringsanvisningarna noggrant innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa de korrekta procedurerna kan leda till en farlig situation för människor och skada på systemet.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.
- Uttaget ska installeras nära utrustningen och ska vara lättillgängligt.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med FCC, IC och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 45 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.2.3或最新版本，以确保符合地方当局法规。
最终用户有责任遵守当地的法规，包括在合法频道内操作，输出 电源，布线要求和动态频率选择（DFS）要求。 所有MikroTik无线电设备必须 专业安装。
此“ wAP R ac”系列快速指南涵盖以下型号： RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*这是无线网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[[https://mt.lv/um-zh](https://mt.lv/um-zh)](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*有关产品的技术规格，手册和更多信息， 请访问[[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [[https://mt.lv/help-zh](https://mt.lv/help-zh)](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-116.png)

**第一步：**

- 打开盖子并插入SIM卡。对于 wAP R ac 型号，将调制解调器安装在 miniPCIe 插槽中；
- 要安装调制解调器，请拆下盖子下方的螺钉并拉开外壳；
- 将设备连接至电源；
- 打开电脑上的网络连接，找到MikroTik无线网络并连接；
- 打开网络浏览器并转到 http://192.168.88.1 开始设置；
- 用户名：admin，无默认密码（或者，对于某些型号，请检查贴纸上的用户密码和无线网络密码）；
- 单击右侧的检查更新并将 RouterOS 软件更新到最新版本来更新您的设备。必须安装有效的SIM卡；
- 要手动更新您的设备，请点击链接 https://mikrotik.com/download 选择该设备的（ARM）包并将其下载到您的PC；将下载的包加载到（WebFig）（失败）菜单中并重新启动设备；将RouterOS软件更新到最新版本将提供更好的性能、稳定性和安全性；在 (QuickSet) 菜单中，配置以下内容： 选择您所在的国家/地区以应用国家/地区法规设置；根据使用类型将安装设置为室内或室外；在左侧字段中设置您的无线网络密码；在底部字段中设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品可以安装在室外。 在开始安装之前，请仔细阅读安装说明。 不使用 正确的硬件和配置或遵循正确的步骤可能会导致人员受伤和系统损坏 。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。
- 插座应安装在设备附近且易于插拔的位置。

**射频辐射暴露：** 此MikroTik设备符合针对不受控制的环境所设定的FCC，IC和欧盟辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业用户或公众的距离不得超过45厘米。

制造商：Mikrotikls SIA，拉脱维亚Unijas iela 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.2.3 или до последней версии, чтобы обеспечить соответствие требованиям местных нормативов.
Конечные пользователи несут ответственность за соблюдение местных нормативов, в том числе за работу в пределах допустимых частотных каналов, вывод требования к питанию, кабелям и динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть профессионально установлены.
:::

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [[https://mt.lv/um-ru](https://mt.lv/um-ru)](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, брошюры и дополнительная информация о продуктах на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [[https://mt.lv/help-ru](https://mt.lv/help-ru)](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-114.png)

**Первые шаги:**

- Откройте крышку и вставьте SIM-карту. Для модели wAP R ac установите модем в слот miniPCIe;
- Чтобы установить модем, выверните винт, расположенный под крышкой, и раздвиньте корпус;
- Подключите устройство к источнику питания;
- Откройте сетевые подключения на вашем компьютере, найдите беспроводную сеть MikroTik и подключитесь к ней;
- Откройте веб-браузер, перейдите по адресу http://192.168.88.1, чтобы начать настройку;
- Имя пользователя: admin, пароль по умолчанию отсутствует (или, для некоторых моделей, проверьте пароль пользователя и пароль беспроводной сети на наклейке);
- Обновите устройство, щелкнув Check for updates справа и обновив программное обеспечение RouterOS до последней версии. Должна быть установлена ​​действующая SIM-карта;
- Чтобы обновить устройство вручную, перейдите по ссылке https://mikrotik.com/download;
- Выберите (ARM) пакеты для этого устройства и загрузите его на свой ПК;
- Загрузите загруженные пакеты в меню (WebFig) (Fails) и перезагрузите устройство;
- Обновление программного обеспечения RouterOS до последней версии обеспечит лучшую производительность, стабильность и безопасность;
- В меню (QuickSet) настройте следующее: Выберите свою страну, чтобы применить настройки нормативов страны;
- Установите установку в *Indoors* или *Outdoors*, в зависимости от типа использования;
- Установите пароль вашей беспроводной сети в левом поле;
- Установите пароль маршрутизатора в нижнем поле.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.
- Розетка должна быть установлена ​​рядом с оборудованием и должна быть легко доступна.
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
| 2400-2483.5 МГц, 5150-5350 МГц, 5650-5850 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

![](./img/image2020-1-24_7-55-5.badge-119.png)

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. **Cм. на упаковке.**

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.2.3 або останньої версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Усі радіопристрої MikroTik повинні бути професійно встановлені.
Цей короткий посібник серії "wAP R ac" охоплює моделі: RBwAPGR-5HacD2HnD (wAP R ac), RBwAPGR-5HacD2HnD&R11e-4G (wAP ac 4G kit), RBwAPGR-5HacD2HnD&R11e-LTE (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE-US (wAP ac LTE kit), RBwAPGR-5HacD2HnD&R11e-LTE6 (wAP ac LTE6 kit).
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [[https://mt.lv/um-ua](https://mt.lv/um-ua)](https://mt.lv/um-ua) для повної оновленої посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products)*
*Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [[https://mt.lv/help](https://mt.lv/help)](https://mt.lv/help)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [[https://mikrotik.com/consultants](https://mikrotik.com/consultants)](https://mikrotik.com/consultants)*

![](./img/ukraina.badge-11.png)

**Перші кроки:**

- Відкрийте кришку та вставте SIM-карту. Для моделі WAP R змінного струму встановіть свій модем у слот miniPCIe;
- Щоб встановити модем, вийміть гвинт, розташований під кришкою, і розділіть корпус;
- Підключіть пристрій до джерела живлення;
- Відкрийте мережеві з'єднання на своєму ПК, знайдіть бездротову мережу MikroTik та підключіться до неї;
- Відкрийте веб-браузер, перейдіть за посиланням http://192.168.88.1 для запуску конфігурації;
- Ім’я користувача: admin і пароль за замовчуванням відсутній (або, для деяких моделей, перевірте пароль користувача та пароль бездротового зв’язку на наклейці);
- Оновіть пристрій, натиснувши Check for updates праворуч та оновивши програмне забезпечення RouterOS до останньої версії. Повинна бути вставлена ​​дійсна SIM-карта;
- Щоб оновити пристрій вручну, перейдіть за посиланням https://mikrotik.com/download
- Виберіть (ARM) пакети для цього пристрою та завантажте його на свій ПК;
- Завантажте завантажені пакети до меню (WebFig) (Файли) та перезавантажте пристрій;
- Оновлення програмного забезпечення RouterOS до останньої версії забезпечить найкращі оновлення продуктивності, стабільності та безпеки;
- У меню (QuickSet) встановіть наступне: Виберіть свою країну, щоб застосувати настройки регулювання країни;
- Встановіть установку в *Indoors* або *Outdoors*, залежно від типу використання;
- Встановіть пароль своєї бездротової мережі в лівому полі;
- Встановіть свій пароль маршрутизатора в нижньому полі.

**Інформація про безпеку:**

- Перш ніж працювати над будь-яким обладнанням MikroTik, пам’ятайте про небезпеки, пов'язані з електричною схемою, та ознайомтеся зі стандартними методами запобігання аварій. Інсталятор повинен бути знайомий з мережевими структурами, термінами та поняттями.
- Використовуйте тільки джерело живлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей виріб можна встановити на відкритому повітрі. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Якщо не використовувати правильне обладнання та конфігурацію або дотримуватися правильних процедур, це може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати, що через неправильне використання пристрою не трапляються аварії та пошкодження. Будь ласка, використовуйте цей продукт обережно та працюйте на свій страх і ризик!
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки.
- Розетка має бути встановлена ​​поблизу обладнання та бути легко доступною.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення FCC, IC та Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 45 сантиметрів від вашого тіла, професіонала чи широкого загалу.
![](./img/ua.badge-37.jpg)

Виробник: Mikrotikls SIA, Unijas iela 2, Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм), 5150-5250 МГц (23 дБм), 5250-5350 МГц (20 дБм), 5470-5725 МГц (27 дБм).

Справжнім Mikrotikls SIA заявляє, що маршрутизатор відповідає основним вимогам та іншим відповідним положенням директиви 2014/53/EC, а також суттєвим вимогам Технічного регламенту радіообладнання, затвердженого постановою Кабінету Міністрів України від 24 травня 2017 року № 355.

Для експлуатації в Україні необхідно отримати дозвіл на експлуатацію у порядку, затвердженому рішенням НКРЗІ від 01.11.2012 № 559, зареєстрованому в Міністерстві юстиції України 03.01.2013 за № 57/22589.

## Federal Communication Commission Interference Statement

| Model | FCC ID | Contains FCC ID |
| --- | --- | --- |
| RBwAPGR-5HacD2HnD-US | TV7WAPGR5AC2D | None |
| RBwAPGR-5HacD2HnD-US&R11e-LTE-US | TV7WAPGR5AC2D | TV7R11ELTE |
| RBwAPGR-5HacD2HnD-US&R11e-4G | TV7WAPGR5AC2D | TV7R11E4G |
| RBwAPGR-5HacD2HnD-US&R11e-LTE6 | TV7WAPGR5AC2D | TV7R11ELTE6 |

![](./img/fcc_logo_ez.badge-104.jpg)
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
| RBwAPGR-5HacD2HnD-US | 7442A-WAPGR5AC2D | None |
| RBwAPGR-5HacD2HnD-US&R11e-LTE-US | 7442A-WAPGR5AC2D | 7442A-R11ELTE |
| RBwAPGR-5HacD2HnD-US&R11e-4G | 7442A-WAPGR5AC2D | 7442A-R11E4G |
| RBwAPGR-5HacD2HnD-US&R11e-LTE6 | 7442A-WAPGR5AC2D | 7442A-R11ELTE6 |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

The device for operation in the band 5150–5250 MHz is only for indoor use to reduce the potential for harmful interference to co-channel mobile satellite systems.

Les dispositifs fonctionnant dans la bande de 5 150 à 5 250 MHz sont réservés uniquement pour une utilisation à l'intérieur afin de réduire les risques de brouillage préjudiciable aux systèmes de satellites mobiles utilisant les mêmes canaux

## UKCA marking

![](./img/ukca_black_fill.badge-114.gif)

## CE Declaration of Conformity

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RouterBOARD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RouterBOARD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen RouterBOARD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp RouterBOARD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός RouterBOARD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type RouterBOARD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RouterBOARD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp RouterBOARD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RouterBOARD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type RouterBOARD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RouterBOARD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a RouterBOARD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio RouterBOARD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að RouterBOARD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas RouterBOARD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RouterBOARD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju RouterBOARD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur RouterBOARD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret RouterBOARD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RouterBOARD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RouterBOARD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RouterBOARD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RouterBOARD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme RouterBOARD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RouterBOARD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [[https://mikrotik.com/products](https://mikrotik.com/products)](https://mikrotik.com/products) |

## WLAN

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      2400-2483.5 MHz / 20 dBm
    
    5150-5250 MHz / 23 dBm
    5250-5350 MHz / 20 dBm
    5470-5725 MHz / 27 dBm
  

This MikroTik device meets Maximum WLAN and LTE transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

The WLAN function for this device is restricted to indoor use only when operating in the 5150 to 5350 MHz frequency range. / Die WLAN-Funktion dieses Geräts ist nur für die Verwendung in Innenräumen im Frequenzbereich 5150 bis 5350 MHz beschränkt. / La fonction WLAN de cet appareil est limitée à une utilisation en intérieur uniquement lorsqu'il fonctionne dans la gamme de fréquences 5150 à 5350 MHz. / La funzione WLAN per questo dispositivo è limitata all'uso interno solo quando si opera nella gamma di frequenza da 5150 a 5350 MHz. / La función WLAN para este dispositivo está restringida al uso en interiores solo cuando se opera en el rango de frecuencia de 5150 a 5350 MHz. / Функция WLAN для этого устройства ограничена использованием внутри помещения только при работе в диапазоне частот от 5150 до 5350 МГц.

![](./img/picto-24.png)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Варианты входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

DC Jack (10-57 V DC) PoE In Ethernet Port (18-57 V DC)
24 V / 0.8 A
IP20
-33°..+50°C

\#74053 #83890
