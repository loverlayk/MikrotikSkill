# Quick Guide - KNOT LR8 kit

> It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements....

![](./img/mt_logo_arrow_v2-02-75.png)

![](./img/bluetooth_cm_black.badge.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.2.1 or the latest stable version, to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be installed according to instructions.
:::

This series Quick Guide covers models: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*This is a wireless network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Full technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*If you need help with configuration, please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*This Wireless product is featuring Bluetooth® technology.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**First steps:**

- Ensure your Internet Service Provider (ISP) allows hardware changes and automatically assigns an IP address;
- Please attach antennas to the device, before connecting to the power source;
- Connect the ISP cable to the Ethernet1 port;
- Connect the device to the power source;
- Connect to the device through any of the ports, excluding Ethernet1, or the wireless network "MikroTik-..." (ensure to check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility;**
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use WinBox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin" and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the "QuickSet" menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the FCC, IC, and European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.2.1 или най-новата стабилна версия, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни да спазват местните разпоредби, включително работа в рамките на законни честотни канали, изходна мощност, изисквания за окабеляване и изисквания за динамичен избор на честота (DFS). Всички радиоустройства MikroTik трябва да бъдат инсталирани съгласно инструкциите.
:::

Тази серия от кратки ръководства обхваща модели: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Това е безжично мрежово устройство. Името на модела на продукта можете да намерите на етикета на калъфа (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um](https://mt.lv/um) за пълното актуално ръководство за потребителя. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Пълни технически спецификации, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Ако имате нужда от помощ при конфигурирането, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Този безжичен продукт се отличава с технологията Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Първи стъпки:**

- Уверете се, че доставчикът на интернет услуги позволява промяна на хардуера и автоматично присвоява IP адрес;
- Моля, прикрепете антени към устройството, преди да го свържете към източника на захранване;
- Свържете кабела на доставчика към порт Ethernet1;
- Свържете устройството към източника на захранване;
- Свържете се с устройството чрез някой от портовете, с изключение на Ethernet1, или безжичната мрежа "MikroTik-..." (проверете паролите за безжична връзка на стикера);
- Установете връзка чрез мобилно приложение. Алтернативно, използвайте WebFig в уеб браузър или инструмента за конфигуриране "WinBox" на [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност;**
- Начнете конфигурацията с избран инструмент, използвайки стандартния IP адрес 192.168.88.1. Ако IP адресът не е достъпен, използвайте WinBox и изберете раздела "Neighbors", за да намерите устройството;
- Продължете да се свързвате чрез MAC адреса. Потребителското име е "admin", и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Натиснете бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- В менюто "QuickSet" настройте следното: Изберете вашата държава, за да приложите настройките за страната;
- Настройте паролата на вашата безжична мрежа в лявото поле;
- Настройте паролата на вашия рутер в долното поле.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт е предназначен за инсталиране на закрито. Дръжте този продукт далеч от вода, пожар, влажност или гореща среда.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е чрез изключване на захранващия адаптер от контакта.

**Излагане на радиочестотно излъчване:** Това оборудване MikroTik отговаря на ограниченията за радиация на радиационната радиация FCC, IC и Европейския съюз, определени за неконтролирана среда. Това устройство MikroTik трябва да бъде инсталирано и експлоатирано на не по-малко от 20 сантиметра от вашето тяло, професионален потребител или широката общественост.

Производител: Mikrotikls SIA, Brivibas gatve 214i Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na RouterOS v7.2.1 nebo na nejnovější stabilní verzi!
Je na koncových uživatelích, aby dodržovali místní předpisy, včetně provozu v rámci legálních frekvenčních kanálů, výstupního výkonu, požadavků na kabeláž a požadavků na dynamický výběr frekvence (DFS). Všechna rádiová zařízení MikroTik musí být nainstalována podle pokynů.
:::

Tato série Stručný průvodce zahrnuje modely: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Toto je zařízení bezdrátové sítě. Název modelu produktu najdete na štítku pouzdra (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um](https://mt.lv/um). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Kompletní technické specifikace, brožury a další informace o produktech na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Pokud potřebujete pomoc s konfigurací, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Tento bezdrátový produkt je vybaven technologií Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**První kroky:**

- Ujistěte se, že váš poskytovatel internetových služeb umožňuje změnu hardwaru a automaticky přiřazuje IP adresu;
- Před připojením ke zdroji napájení připojte k zařízení antény;
- Připojte kabel od poskytovatele k portu Ethernet1;
- Připojte zařízení k zdroji napájení;
- Připojte se k zařízení prostřednictvím kteréhokoli portu kromě Ethernet1 nebo bezdrátové sítě "MikroTik-..." (zkontrolujte hesla k bezdrátové síti na štítku);
- Vytvořte spojení pomocí mobilní aplikace. Alternativně můžete použít WebFig v webovém prohlížeči nebo nástroj pro konfiguraci "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Zahajte konfiguraci ve zvoleném nástroji s výchozí IP adresou 192.168.88.1. Pokud není IP adresa k dispozici, použijte WinBox a vyberte kartu "Neighbors", abyste zařízení našli;
- Pokračujte v připojení pomocí MAC adresy. Uživatelské jméno je "admin", a není žádné heslo (nebo, pro některé modely, zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Klikněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do nabídky "Files" na WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi zajistíte optimální výkon, stabilitu a aktualizace zabezpečení;
- V nabídce "QuickSet" proveďte následující nastavení: Vyberte svou zemi, abyste aplikovali nastavení pro regulaci země;
- Nastavte heslo k bezdrátové síti v levém poli;
- Nastavte heslo k vašemu routeru v dolním poli.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt je určen k instalaci uvnitř. Udržujte tento produkt mimo vodu, oheň, vlhkost nebo horké prostředí.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecího adaptéru ze zásuvky.

**Vystavení vysokofrekvenčnímu záření:** Toto zařízení MikroTik splňuje limity pro ozáření FCC, IC a Evropské unie stanovené pro nekontrolované prostředí. Toto zařízení MikroTik by mělo být instalováno a provozováno ne dále než 20 centimetrů od těla, profesionálního uživatele nebo široké veřejnosti.

Výrobce: Mikrotikls SIA, Brivibas gatve 214i Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.2.1 eller den seneste stabile version for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landets regler, herunder drift inden for lovlige frekvenskanaler, udgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik-radioenheder skal installeres i henhold til instruktionerne.
:::

Denne serie hurtigvejledninger dækker modeller: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Dette er en trådløs netværksenhed. Du kan finde produktmodelnavnet på sagsetiketten (ID).*
*Besøg brugervejledningssiden på [https://mt.lv/um](https://mt.lv/um) for den fulde opdaterede brugervejledning. Eller scan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Fuld tekniske specifikationer, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*Hvis du har brug for hjælp til konfiguration, skal du søge en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Dette trådløse produkt er udstyret med Bluetooth®-teknologi.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Første trin:**

- Sørg for, at din internetudbyder tillader ændringer i hardware og tildeler en IP-adresse automatisk;
- Tilslut venligst antenner til enheden, før du tilslutter til strømkilden;
- Tilslut ISP-kablet til Ethernet1-porten;
- Tilslut enheden til strømkilden;
- Forbind til enheden gennem en af portene, undtagen Ethernet1, eller det trådløse netværk "MikroTik-..." (sørg for at tjekke de trådløse adgangskoder på klistermærket);
- Opret forbindelse ved hjælp af en mobilapplikation. Alternativt kan du bruge WebFig i en webbrowser eller "WinBox" konfigurationsværktøjet på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Start konfigurationen inden for det valgte værktøj ved hjælp af standard IP-adressen 192.168.88.1. Hvis IP-adressen ikke er tilgængelig, skal du bruge WinBox og vælge fanen "Neighbors" for at finde enheden;
- Fortsæt med at oprette forbindelse ved at bruge MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload de downloadede pakker til WebFig eller WinBox "Files" menuen og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version sikrer du optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- I menuen "QuickSet" konfigurer følgende: Vælg dit land for at anvende landsreguleringsindstillinger;
- Indstil dit trådløse netværkspassword i det venstre felt;
- Indstil dit routerpassword i bundfeltet.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive installeret indendørs. Hold dette produkt væk fra vand, ild, fugtighed eller varme omgivelser.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-udstyr overholder FCC, IC og EU's strålingseksponeringsgrænser, der er fastsat for et ukontrolleret miljø. Denne MikroTik-enhed skal installeres og betjenes ikke nærmere 20 centimeter fra din krop, erhvervsbruger eller offentligheden.

Producent: Mikrotikls SIA, Brivibas gatve 214i Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.2.1 oder die neueste stabile Version aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften einzuhalten, einschließlich des Betriebs innerhalb der gesetzlichen Frequenzkanäle, der Ausgangsleistung, der Verkabelungsanforderungen und der Anforderungen für die dynamische Frequenzauswahl (DFS). Alle MikroTik-Funkgeräte müssen gemäß den Anweisungen installiert werden.
:::

Diese Kurzanleitungsserie behandelt Modelle: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Dies ist ein drahtloses Netzwerkgerät. Den Namen des Produktmodells finden Sie auf dem Etikett (ID).*
*Bitte besuchen Sie die Benutzerhandbuchseite unter [https://mt.lv/um](https://mt.lv/um), um das vollständige aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Vollständige technische Spezifikationen, Broschüren und weitere Informationen zu Produkten finden Sie unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*Wenn Sie Hilfe bei der Konfiguration benötigen, wenden Sie sich an einen Berater unter [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Dieses drahtlose Produkt verfügt über Bluetooth®-Technologie.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Erste Schritte:**

- Stellen Sie sicher, dass Ihr Internetdienstanbieter Hardwareänderungen zulässt und automatisch eine IP-Adresse vergibt;
- Bitte befestigen Sie die Antennen am Gerät, bevor Sie es an die Stromquelle anschließen;
- Schließen Sie das ISP-Kabel an den Ethernet1-Port an;
- Schließen Sie das Gerät an die Stromquelle an;
- Verbinden Sie sich mit dem Gerät über einen der Ports, außer Ethernet1, oder das drahtlose Netzwerk "MikroTik-..." (überprüfen Sie die drahtlosen Passwörter auf dem Aufkleber);
- Stellen Sie eine Verbindung mit einer mobilen Anwendung her. Alternativ können Sie WebFig in einem Webbrowser oder das "WinBox" Konfigurationswerkzeug unter [https://mt.lv/winbox](https://mt.lv/winbox) verwenden; **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Starten Sie die Konfiguration im gewählten Tool mit der Standard-IP-Adresse 192.168.88.1. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie WinBox und wählen Sie die Registerkarte "Neighbors", um das Gerät zu finden;
- Fahren Sie fort, sich über die MAC-Adresse zu verbinden. Der Benutzername lautet "admin", und es gibt kein Passwort (oder, für einige Modelle, überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch das Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie eine optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Konfigurieren Sie im Menü "QuickSet" folgendes: Wählen Sie Ihr Land aus, um länderspezifische Einstellungen anzuwenden;
- Legen Sie Ihr drahtloses Netzwerkkennwort im linken Feld fest;
- Legen Sie Ihr Routerkennwort im unteren Feld fest.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für den Innenbereich vorgesehen. Halten Sie dieses Produkt von Wasser, Feuer, Feuchtigkeit oder heißen Umgebungen fern.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, das Netzteil aus der Steckdose zu ziehen.

**Exposition gegenüber hochfrequenter Strahlung:** Dieses MikroTik-Gerät entspricht den FCC-, IC- und EU-Grenzwerten für die Strahlenexposition in unkontrollierten Umgebungen. Dieses MikroTik-Gerät sollte nicht näher als 20 Zentimeter von Ihrem Körper, berufsmäßigen Verwender oder der Öffentlichkeit entfernt installiert und betrieben werden.

Hersteller: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί σε RouterOS v7.2.1 ή την τελευταία σταθερή έκδοση, για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Αποτελεί ευθύνη των τελικών χρηστών να ακολουθούν τους κανονισμούς της τοπικής χώρας, συμπεριλαμβανομένης της λειτουργίας εντός νόμιμων καναλιών συχνότητας, ισχύος εξόδου, απαιτήσεων καλωδίωσης και απαιτήσεων δυναμικής επιλογής συχνότητας (DFS). Όλες οι ραδιοφωνικές συσκευές MikroTik πρέπει να εγκατασταθούν σύμφωνα με τις οδηγίες.
:::

Αυτός ο γρήγορος οδηγός σειράς καλύπτει μοντέλα: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Πρόκειται για μια ασύρματη συσκευή δικτύου. Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα περίπτωσης (ID).*
*Επισκεφθείτε τη σελίδα εγχειριδίων χρήστη στη διεύθυνση [https://mt.lv/um](https://mt.lv/um) για το πλήρες ενημερωμένο εγχειρίδιο χρήστη. Ή σαρώστε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Πλήρεις τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες σχετικά με προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Εάν χρειάζεστε βοήθεια σχετικά με τη διαμόρφωση, αναζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Αυτό το ασύρματο προϊόν διαθέτει τεχνολογία Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Πρώτα βήματα:**

- Βεβαιωθείτε ότι ο πάροχος υπηρεσιών internet επιτρέπει τις αλλαγές στον εξοπλισμό και αναθέτει αυτόματα μια διεύθυνση IP;
- Παρακαλούμε συνδέστε τις κεραίες στη συσκευή, πριν συνδεθείτε στην πηγή τροφοδοσίας;
- Συνδέστε το καλώδιο του παροχέα στη θύρα Ethernet1;
- Συνδέστε τη συσκευή στην πηγή ισχύος;
- Συνδεθείτε στη συσκευή μέσω οποιασδήποτε από τις θύρες, εξαιρουμένης της Ethernet1, ή του ασύρματου δικτύου "MikroTik-..." (βεβαιωθείτε ότι ελέγχετε τους κωδικούς πρόσβασης στο αυτοκόλλητο);
- Δημιουργήστε σύνδεση χρησιμοποιώντας μια κινητή εφαρμογή. Εναλλακτικά, μπορείτε να χρησιμοποιήσετε το WebFig σε έναν περιηγητή ή το εργαλείο διαμόρφωσης "WinBox" στη διεύθυνση [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ξεκινήστε τη διαμόρφωση μέσα από το επιλεγμένο εργαλείο, χρησιμοποιώντας την προεπιλεγμένη διεύθυνση IP 192.168.88.1. Αν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το WinBox και επιλέξτε την καρτέλα "Neighbors" για να βρείτε τη συσκευή;
- Συνεχίστε να συνδέεστε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός (ή, για κάποια μοντέλα, ελέγξτε τους κωδικούς χρήστη και ασύρματους στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην πιο πρόσφατη έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα ληφθέντα πακέτα στο μενού "Files" του WebFig ή WinBox και επανεκκινήστε τη συσκευή;
- Αναβαθμίζοντας το λογισμικό του RouterOS στην πιο πρόσφατη έκδοση, μπορείτε να εξασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Στο μενού "QuickSet" ρυθμίστε τα εξής: Επιλέξτε τη χώρα σας, για να εφαρμόσετε ρυθμίσεις κανονισμού για τη χώρα;
- Ρυθμίστε τον κωδικό πρόσβασης του ασύρματου δικτύου σας στο αριστερό πεδίο;
- Ρυθμίστε τον κωδικό πρόσβασης του δρομολογητή σας στο κάτω πεδίο.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Το προϊόν αυτό προορίζεται για εγκατάσταση σε εσωτερικό χώρο. Κρατήστε το προϊόν μακριά από νερό, φωτιά, υγρασία ή καυτό περιβάλλον.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το τροφοδοτικό από την πρίζα.

**Έκθεση σε ακτινοβολία ραδιοσυχνοτήτων:** Αυτός ο εξοπλισμός MikroTik συμμορφώνεται με τα όρια έκθεσης ακτινοβολίας FCC, IC και Ευρωπαϊκής Ένωσης που καθορίζονται για ανεξέλεγκτο περιβάλλον. Αυτή η συσκευή MikroTik πρέπει να εγκατασταθεί και να λειτουργήσει σε απόσταση μικρότερη από 20 εκατοστά από το σώμα σας, το επαγγελματικό χρήστη ή το ευρύ κοινό.

Κατασκευαστής: Mikrotikls SIA, Brivibas gatve 214i Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.2.1 o la última versión estable, para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales de frecuencia legales, la potencia de salida, los requisitos de cableado y los requisitos de Selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben instalarse de acuerdo con las instrucciones.
:::

Esta serie de guías rápidas cubre los modelos: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta de la caja (ID).*
*Visite la página del manual de usuario en [https://mt.lv/um](https://mt.lv/um) para obtener el manual de usuario completo y actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas completas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Si necesita ayuda con la configuración, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Este producto inalámbrico cuenta con tecnología Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Primeros pasos:**

- Asegúrese de que su proveedor de servicios de Internet permita cambios de hardware y asigne automáticamente una dirección IP;
- Conecte antenas al dispositivo antes de conectarlo a la fuente de alimentación;
- Conecte el cable del proveedor de servicios de Internet al puerto Ethernet1;
- Conecte el dispositivo a la fuente de alimentación;
- Conéctese al dispositivo a través de cualquiera de los puertos, excluyendo Ethernet1, o la red inalámbrica "MikroTik-..." (asegúrese de verificar las contraseñas inalámbricas en la etiqueta);
- Establecer una conexión mediante una aplicación móvil. Alternativamente, puede utilizar WebFig en un navegador web o la herramienta de configuración "WinBox" en [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Inicie la configuración dentro de la herramienta seleccionada, utilizando la dirección IP predeterminada 192.168.88.1. Si la dirección IP no está disponible, utilice WinBox y elija la pestaña "Neighbors" para encontrar el dispositivo;
- Proceda a conectarse utilizando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú "Files" de WebFig o WinBox y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- En el menú "QuickSet" configure lo siguiente: Elija su país para aplicar configuraciones de regulación del país;
- Configure la contraseña de su red inalámbrica en el campo izquierdo;
- Configure la contraseña de su router en el campo inferior.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para instalarse en interiores. Mantenga este producto alejado del agua, fuego, humedad o ambientes calientes.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la FCC, IC y la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Brivibas gatve 214i Riga, Letonia, LV1039.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, 802.11b/g/n con antena PIFA integrada, ganancia máxima de 1.5 dBi.

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
Kohaliku omavalitsuse eeskirjade järgimise tagamiseks tuleb see seade uuendada versioonile RouterOS v7.2.1 või uusimale stabiilsele versioonile!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi, sealhulgas seaduslikes sageduskanalites toimimist, väljundvõimsust, kaabeldusnõudeid ja dünaamilise sageduse valiku (DFS) nõudeid. Kõik MikroTiku raadioseadmed tuleb installida vastavalt juhistele.
:::

Selle seeria lühijuhend hõlmab mudeleid: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*See on traadita võrguseade. Toote mudeli nime leiate ümbrise sildilt (ID).*
*Täielikult ajakohastatud kasutusjuhendi leiate aadressilt [https://mt.lv/um](https://mt.lv/um). Või skannige QR-kood oma mobiiltelefoniga.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Täielikud tehnilised kirjeldused, brošüürid ja lisateave toodete kohta leiate aadressilt [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*Kui vajate seadistamisel abi, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Sellel traadita tootel on Bluetooth®-tehnoloogia.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Esimesed sammud:**

- Veenduge, et teie internetiteenuse pakkuja lubab riistvara muudatusi ja määrab automaatselt IP-aadressi;
- Enne toiteallikaga ühendamist ühendage seadmega antennid;
- Ühendage teenusepakkujalt saadud kaabel Ethernet1 pordiga;
- Ühendage seade toiteallikaga;
- Ühenduge seadmega läbi ühe võrgupordi, välja arvatud Ethernet1, või traadita võrguga "MikroTik-..." (veenduge, et kontrollite kleebisel olevaid traadita paroole);
- Looge ühendus mobiilirakenduse abil. Alternatiivselt saate kasutada WebFig'i veebibrauseris või "WinBox" konfiguratsioonitööriista aadressil [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Alustage konfiguratsiooni valitud tööriista abil, kasutades vaikimisi IP-aadressi 192.168.88.1. Kui IP-aadress pole saadaval, kasutage WinBoxi ja valige seade leidmiseks vahekaart "Neighbors";
- Jätkake ühendumist MAC-aadressi kasutades. Kasutajanimi on "admin" ja parooli pole (või mõne mudeli puhul kontrollige kasutaja ja traadita paroole kleebisel);
- Klõpsake nupul "Check for updates" ja värskendage RouterOS-i viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Laadige allalaaditud paketid üles WebFig või WinBox "Files" menüüsse ja taaskäivitage seade;
- Uuendades RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Menüüs "QuickSet" konfigureerige järgmist: Valige oma riik, et rakendada riigipõhiseid seadeid;
- Seadke traadita võrgu parool vasakusse välja;
- Seadke ruuteri parool alumisse välja.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- See toode on ette nähtud paigaldamiseks siseruumidesse. Hoidke seda toodet eemal veest, tulest, niiskusest ja kuumadest keskkondadest.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on toiteadapteri pistikupesast lahti ühendamine.

**Raadiosagedusliku kiirgusega kokkupuude:** see MikroTik seade vastab FCC, IC ja Euroopa Liidu kiirguskontrolli piirnormidele, mis on kehtestatud kontrollimatu keskkonna jaoks. Seda MikroTiku seadet tuleks paigaldada ja kasutada mitte kaugemal kui 20 sentimeetrit kehast, tööga seotud kasutajast või üldsusest.

Tootja: Mikrotikls SIA, Brivibas gatve 214i Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.2.1 tai uusin vakaa versio, jotta varmistetaan paikallisviranomaisten asetusten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maakohtaisia ​​määräyksiä, mukaan lukien toiminta laillisilla taajuuskanavilla, lähtöteho, kaapelointivaatimukset ja DFS (Dynamic Frequency Selection) vaatimukset. Kaikki MikroTik-radiolaitteet on asennettava ohjeiden mukaan.
:::

Tämän sarjan pikaopas kattaa mallit: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Tämä on langaton verkkolaite. Tuotemallin nimi löytyy kotelotarrasta (ID).*
*Vieraile osoitteessa [https://mt.lv/um](https://mt.lv/um) olevalla käyttöohjesivulla saadaksesi täydellisen ajantasaisen käyttöoppaan. Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Täydelliset tekniset tiedot, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*Jos tarvitset apua määrityksissä, ota yhteyttä konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Tämä langaton tuote sisältää Bluetooth®-tekniikan.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Ensiaskeleet:**

- Varmista, että Internet-palveluntarjoajasi sallii laitteiston muutokset ja antaa automaattisesti IP-osoitteen;
- Kiinnitä antennit laitteeseen ennen kuin liität sen virtalähteeseen;
- Kytke ISP-kaapeli Ethernet1-porttiin;
- Liitä laite virtalähteeseen;
- Yhdistä laite mihin tahansa porttiin, poislukien Ethernet1, tai langattomaan verkkoon "MikroTik-..." (varmista, että tarkistat langattomien salasanojen tarroja);
- Muodosta yhteys käyttämällä mobiilisovellusta. Vaihtoehtoisesti voit käyttää WebFigiä selaimessa tai "WinBox" konfiguraatiotyökalua osoitteessa [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Aloita konfigurointi valitussa työkalussa käyttäen oletus-IP-osoitetta 192.168.88.1. Jos IP-osoite ei ole saatavilla, käytä WinBoxia ja valitse "Neighbors"-välilehti laitteen löytämiseksi;
- Jatka yhteyden muodostamista MAC-osoitteen avulla. Käyttäjänimi on "admin", eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjä- ja langattomat salasanat tarraan);
- Klikkaa "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFig- tai WinBox-"Files"-valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmiston uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- "QuickSet"-valikossa aseta seuraavat: Valitse maasi, jotta voit soveltaa maasääntelyasetuksia;
- Aseta langattoman verkkosi salasana vasempaan kenttään;
- Aseta reitittimesi salasana alaosaan.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tämä tuote on tarkoitettu asennettavaksi sisätiloissa. Pidä tämä tuote poissa vedestä, tulesta, kosteudesta tai kuumasta ympäristöstä.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtalähde pistorasiasta.

**Radiotaajuussäteilyaltistus:** Tämä MikroTik-laite on FCC: n, IC: n ja Euroopan unionin säteilyaltistusrajojen mukainen, jotka on asetettu hallitsemattomalle ympäristölle. Tämä MikroTik-laite tulisi asentaa ja käyttää vain lähempänä kuin 20 senttimetriä kehosta, ammattilaisista käyttäjistä tai yleisöstä.

Valmistaja: Mikrotikls SIA, Brivibas gatve 214i Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.2.1 ou la dernière version stable, pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays, y compris le fonctionnement dans les canaux de fréquence légaux, la puissance de sortie, les exigences de câblage et les exigences de sélection dynamique de fréquence (DFS). Tous les appareils radio MikroTik doivent être installés conformément aux instructions.
:::

Cette série de guides rapides couvre les modèles : RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Ceci est un périphérique réseau sans fil. Vous pouvez trouver le nom du modèle de produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um](https://mt.lv/um) pour obtenir le manuel d'utilisation complet à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques complètes, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Si vous avez besoin d'aide pour la configuration, veuillez chercher un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ce produit sans fil est doté de la technologie Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Premiers pas:**

- Assurez-vous que votre fournisseur de services Internet autorise les modifications matérielles et attribue automatiquement une adresse IP;
- Veuillez fixer les antennes à l'appareil avant de vous connecter à la source d'alimentation;
- Connectez le câble de votre fournisseur de services Internet au port Ethernet1;
- Connectez l'appareil à la source d'alimentation;
- Connectez-vous à l'appareil via l'un des ports, à l'exclusion d'Ethernet1, ou du réseau sans fil "MikroTik-..." (assurez-vous de vérifier les mots de passe sans fil sur l'autocollant);
- Établir une connexion à l'aide d'une application mobile. Vous pouvez également utiliser WebFig dans un navigateur Web ou l'outil de configuration "WinBox" à l'adresse [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Démarrez la configuration dans l'outil choisi en utilisant l'adresse IP par défaut 192.168.88.1. Si l'adresse IP n'est pas disponible, utilisez WinBox et choisissez l'onglet "Neighbors" pour trouver le périphérique;
- Procédez à la connexion en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les paquets téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, une stabilité et des mises à jour de sécurité;
- Dans le menu "QuickSet", configurez ce qui suit: Choisissez votre pays pour appliquer les paramètres de régulation du pays;
- Configurez le mot de passe de votre réseau sans fil dans le champ de gauche;
- Configurez le mot de passe de votre routeur dans le champ inférieur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être installé à l'intérieur. Gardez ce produit loin de l'eau, du feu, de l'humidité ou des environnements chauds.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher l'adaptateur secteur de la prise de courant.

**Exposition aux rayonnements radiofréquences:** cet équipement MikroTik est conforme aux limites d'exposition aux rayonnements FCC, IC et Union européenne établies pour un environnement non contrôlé. Cet appareil MikroTik doit être installé et utilisé à au moins 20 centimètres de votre corps, de l'utilisateur professionnel ou du grand public.

Fabricant: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.2.1 ili najnoviju stabilnu verziju, kako bi se osigurala sukladnost s lokalnim propisima!
Krajnji su korisnici dužni slijediti lokalne propise, uključujući rad unutar legalnih frekvencijskih kanala, izlaznu snagu, zahtjeve za kabliranje i zahtjeve za dinamičkim odabirom frekvencije (DFS). Svi MikroTik radio uređaji moraju biti instalirani prema uputama.
:::

Ova serija kratkih vodiča pokriva modele: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Ovo je bežični mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Posjetite stranicu korisničkog priručnika na [https://mt.lv/um](https://mt.lv/um) za cjelovit i ažuriran korisnički priručnik. Ili skenirajte QR kôd mobitelom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Potpune tehničke specifikacije, brošure i više informacija o proizvodima potražite na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*Ako trebate pomoć oko konfiguracije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ovaj bežični proizvod sadrži Bluetooth® tehnologiju.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Prvi koraci:**

- Provjerite je li vaš pružatelj internetskih usluga dopušta promjene hardvera i automatski dodjeljuje IP adresu;
- Pričvrstite antene na uređaj prije spajanja na izvor napajanja;
- Povežite ISP kabel s Ethernet1 priključkom;
- Povežite uređaj s izvorom napajanja;
- Povežite se s uređajem putem bilo kojeg od priključaka, isključujući Ethernet1, ili bežične mreže "MikroTik-..." (obavezno provjerite bežične lozinke na naljepnici);
- Uspostavite vezu pomoću mobilne aplikacije. Opcionalno, koristite WebFig u web pregledniku ili alat za konfiguraciju "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Pokrenite konfiguraciju unutar odabranog alata, koristeći zadanu IP adresu 192.168.88.1. Ako IP adresa nije dostupna, koristite WinBox i odaberite karticu "Neighbors" da biste pronašli uređaj;
- Nastavite s povezivanjem putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Kliknite gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Učitajte preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem RouterOS softvera na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- U "QuickSet" izborniku postavite sljedeće: Odaberite svoju zemlju da biste primijenili postavke regulacije za tu zemlju;
- Postavite lozinku za svoju bežičnu mrežu u lijevo polje;
- Postavite lozinku za svoj usmjerivač u donje polje.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj je proizvod namijenjen ugradnji u zatvorenom prostoru. Ovaj proizvod držite podalje od vode, vatre, vlage ili vrućeg okruženja.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanjem mrežnog adaptera iz utičnice.

**Izloženost radiofrekvencijskom zračenju:** Ova oprema MikroTik udovoljava ograničenjima izloženosti zračenju FCC, IC i Europske unije utvrđenim za nekontrolirano okruženje. Ovaj MikroTik uređaj treba instalirati i upravljati ne više od 20 centimetara od vašeg tijela, profesionalnog korisnika ili šire javnosti.

Proizvođač: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt frissíteni kell a RouterOS v7.2.1-ra vagy a legújabb stabil verzióra, hogy biztosítsák a helyi hatóságok előírásainak való megfelelést!
A végfelhasználók felelőssége a helyi országos előírások betartása, ideértve a törvényes frekvenciacsatornákon történő működést, a kimeneti teljesítményt, a kábelezési követelményeket és a dinamikus frekvenciaválasztási (DFS) követelményeket. Az összes MikroTik rádiókészüléket az utasításoknak megfelelően kell telepíteni.
:::

Ez a sorozat Gyors útmutató a következő modellekre terjed ki: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Ez egy vezeték nélküli hálózati eszköz. A termékmodell nevét megtalálhatja a tok címkéjén (ID).*
*Kérjük, látogasson el a [https://mt.lv/um](https://mt.lv/um) felhasználói kézikönyv oldalára a teljes naprakész felhasználói kézikönyvért. Vagy beolvassa a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Teljes műszaki előírások, prospektusok és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products)*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*Ha segítségre van szüksége a konfiguráláshoz, kérjen tanácsadót: [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ez a vezeték nélküli termék Bluetooth® technológiát tartalmaz.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Első lépések:**

- Győződjön meg róla, hogy az internet szolgáltatója lehetővé teszi a hardverváltozásokat, és automatikusan hozzárendel egy IP-címet;
- Kérjük, csatlakoztassa az antennákat a készülékhez, mielőtt csatlakoztatná az áramforráshoz;
- Csatlakoztassa az ISP kábelt az Ethernet1 portra;
- Csatlakoztassa az eszközt az áramforráshoz;
- Csatlakozzon az eszközhöz bármelyik porton, kivéve az Ethernet1-et, vagy a "MikroTik-..." nevű vezeték nélküli hálózaton keresztül (győződjön meg róla, hogy ellenőrzi a matricán található vezeték nélküli jelszavakat);
- Kapcsolat létesítése mobilalkalmazás segítségével. Vagy használja a WebFig-et egy webböngészőben vagy a "WinBox" konfigurációs eszközt a [https://mt.lv/winbox](https://mt.lv/winbox) címen; **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Indítsa el a konfigurációt az választott eszközön, az alapértelmezett 192.168.88.1 IP-cím használatával. Ha az IP-cím nem érhető el, használja a WinBoxot, és válassza ki a "Neighbors" lapot az eszköz megtalálásához;
- Folytassa a kapcsolatot a MAC cím használatával. A felhasználónév "admin", és nincs jelszó (vagy néhány modell esetén ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- A RouterOS szoftver frissítésével a legújabb verzióra optimális teljesítményt, stabilitást és biztonsági frissítéseket biztosíthat;
- A "QuickSet" menüben állítsa be a következőket: Válassza ki az országát a szabályozási beállítások alkalmazásához;
- Állítsa be a vezeték nélküli hálózati jelszavát a bal oldali mezőben;
- Állítsa be a router jelszavát az alsó mezőben.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ezt a terméket beltéri használatra tervezték. Tartsa távol a terméket víztől, tűztől, páratartalomtól és forró környezettől.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati adaptert kihúzza a konnektorból.

**Rádiófrekvencia-sugárzás:** Ez a MikroTik berendezés megfelel az FCC, IC és az Európai Unió sugárterhelési határértékeinek, amelyeket egy ellenőrizetlen környezetre vonatkoznak. Ezt a MikroTik készüléket a testétől, a munkahelyi használótól vagy a lakosságtól legfeljebb 20 centiméter távolságra kell telepíteni és működtetni.

Gyártó: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettország, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.2.1 o all'ultima versione stabile, per garantire la conformità con le normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative nazionali locali, incluso il funzionamento nei canali di frequenza legali, la potenza di uscita, i requisiti di cablaggio e i requisiti di selezione della frequenza dinamica (DFS). Tutti i dispositivi radio MikroTik devono essere installati secondo le istruzioni.
:::

Questa serie di guide rapide copre i modelli: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Questo è un dispositivo di rete wireless. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale utente su [https://mt.lv/um](https://mt.lv/um) per il manuale utente completo e aggiornato. Oppure scansiona il codice QR con il tuo telefono cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche complete, brochure e ulteriori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*Se hai bisogno di aiuto con la configurazione, cerca un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Questo prodotto wireless è dotato della tecnologia Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Primi passi:**

- Assicurati che il tuo fornitore di servizi Internet permetta le modifiche hardware e assegni automaticamente un indirizzo IP;
- Collegare le antenne al dispositivo prima di collegarlo alla fonte di alimentazione;
- Collega il cavo del provider di servizi Internet alla porta Ethernet1;
- Collega il dispositivo all'adattatore di corrente incluso;
- Collegati al dispositivo attraverso uno dei porti Ethernet, escludendo Ethernet1, o alla rete wireless chiamata "MikroTik-..." (assicurati di controllare le password wireless sull'etichetta);
- Stabilire una connessione tramite un'applicazione mobile. In alternativa, utilizza WebFig in un browser web o lo strumento di configurazione "WinBox" all'indirizzo [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Inizia la configurazione all'interno dello strumento scelto, utilizzando l'indirizzo IP predefinito 192.168.88.1. Se l'indirizzo IP non è disponibile, utilizza WinBox e scegli la scheda "Neighbors" per trovare il dispositivo;
- Prosegui per connetterti utilizzando l'indirizzo MAC. Il nome utente è "admin," e non c'è alcuna password (o, per alcuni modelli, controlla le password dell'utente e wireless sull'etichetta);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Nel menu "QuickSet" imposta quanto segue: Scegli il tuo paese per applicare le impostazioni di regolamentazione nazionale;
- Imposta la password della tua rete wireless nel campo sinistro;
- Imposta la password del tuo router nel campo inferiore.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è destinato all'installazione all'interno. Tenere questo prodotto lontano da acqua, fuoco, umidità o ambienti caldi.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare l'alimentatore dalla presa di corrente.

**Esposizione alle radiazioni di radiofrequenza:** questa apparecchiatura MikroTik è conforme ai limiti di esposizione alle radiazioni FCC, IC e dell'Unione Europea stabiliti per un ambiente non controllato. Questo dispositivo MikroTik deve essere installato e utilizzato a una distanza non inferiore a 20 centimetri dal proprio corpo, utente professionale o pubblico.

Produttore: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í RouterOS v7.2.1 eða nýjustu stöðugu útgáfuna, til að tryggja að farið sé að reglugerðum sveitarfélaga!
Það er endanleg notandi að fylgja reglugerðum á hverjum stað, þar með talin notkun innan löglegra tíðnisviða, afköst, kaðallkröfur og DFS (Dynamic Frequency Selection) kröfur. Öll MikroTik útvarpstæki verða að vera sett upp samkvæmt leiðbeiningum.
:::

Þessi fljótlega leiðarvísasería nær yfir líkön: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Þetta er þráðlaust netkerfi. Þú getur fundið vörulíkanheitið á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um](https://mt.lv/um) til að fá alla uppfærðu notendahandbókina. Eða skannaðu QR kóðann með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Allar tækniforskriftir, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*Ef þú þarft hjálp við stillingar skaltu leita til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Þessi þráðlausa vara er með Bluetooth® tækni.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Fyrstu skrefin:**

- Ábyrgðu þig á að Internet-þjónustuveitandinn þinn leyfi breytingar á öruggu og úthluta sjálfkrafa IP-tölu;
- Vinsamlegast tengdu loftnet við tækið áður en þú tengir það við aflgjafa;
- Tengdu ISP snúruna við Ethernet1 portinn;
- Tengdu tækið við rafmagnsaflið;
- Tengdu þig við tækið í gegnum einhvern af netþáttum, nema Ethernet1, eða þráðlausa netið "MikroTik-..." (gangtu úr skugga um að athuga þráðlausa lykla á merki);
- Búið til tengingu með því að nota farsímaforrit. Eða notaðu WebFig í vafra eða stilliverkfærið "WinBox" á [https://mt.lv/winbox](https://mt.lv/winbox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Byrjaðu uppsetningu innan valins tóls með sjálfgefinni IP-tölu 192.168.88.1. Ef IP-talan er ekki tiltæk, nottu WinBox og veldu "Neighbors" flipann til að finna tækið;
- Halda áfram að tengjast með því að nota MAC-tölu. Notendanafnið er "admin" og engin lykilorð (eða, í sumum gerðum, athugaðu notenda- og þráðlaus lykilorð á klisterinu);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS í nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum í WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Með því að uppfæra RouterOS hugbúnaðinn á nýjustu útgáfu getur þú tryggt besta árangur, stöðugleika og öryggisuppfærslur;
- Í "QuickSet" valmyndinni stilltu eftirfarandi: Veldu landið þitt til að nota landsreglugerðarstillingar;
- Stilltu lykilorðið fyrir þitt þráðlausa net í vinstra reitnum;
- Stilltu lykilorðið fyrir routerinn þinn í neðra reitnum.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvituð um hættuna sem fylgir rafrásum og kynntu þér venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessari vöru er ætlað að setja upp innandyra. Geymið þessa vöru fjarri vatni, eldi, raka eða heitu umhverfi.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.

**Útsetning fyrir útvarpsbylgjugeislun:** Þessi MikroTik búnaður er í samræmi við FCC, IC og geislunarmörk Evrópusambandsins sem sett eru fyrir stjórnlaust umhverfi. Þetta MikroTik tæki ætti að vera sett upp og starfrækt ekki nær 20 sentímetrum frá líkama þínum, atvinnu notanda eða almenningi.

Framleiðandi: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.2.1 eller den siste stabile versjonen, for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukerens ansvar å følge lokale landsbestemmelser, inkludert drift innen lovlige frekvenskanaler, utgangseffekt, kablingskrav og DFS-krav (Dynamic Frequency Selection). Alle MikroTik radioenheter må installeres i henhold til instruksjonene.
:::

Denne hurtigveiledningsserien dekker modellene: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Dette er en trådløs nettverksenhet. Du finner produktmodellnavnet på saksetiketten (ID).*
*Vennligst besøk bruksanvisningssiden på [https://mt.lv/um](https://mt.lv/um) for den oppdaterte brukerhåndboken. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Fullstendige tekniske spesifikasjoner, brosjyrer og mer informasjon om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*Hvis du trenger hjelp med konfigurering, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Dette trådløse produktet har Bluetooth®-teknologi.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Første steg:**

- Sørg for at Internettleverandøren din tillater endringer i maskinvaren og automatisk tildeler en IP-adresse;
- Fest antenner til enheten før du kobler til strømkilden;
- Koble ISP-kabelen til Ethernet1-porten;
- Koble enheten til strømkilden;
- Koble til enheten gjennom en av portene, unntatt Ethernet1, eller det trådløse nettverket "MikroTik-..." (pass på å sjekke de trådløse passordene på etiketten);
- Opprett forbindelse ved hjelp av en mobilapplikasjon. Alternativt kan du bruke WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" på [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Start konfigurasjonen innenfor det valgte verktøyet ved hjelp av standard IP-adresse 192.168.88.1. Hvis IP-adressen ikke er tilgjengelig, bruk WinBox og velg fanen "Neighbors" for å finne enheten;
- Fortsett å koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på "Check for updates" -knappen og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig- eller WinBox-"Files" -menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen, kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- I "QuickSet" -menyen setter du opp følgende: Velg landet ditt for å bruke landsreguleringsinnstillinger;
- Sett opp passordet for det trådløse nettverket ditt i det venstre feltet;
- Sett opp passordet for ruteren din i det nedre feltet.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet er ment å installeres innendørs. Hold dette produktet borte fra vann, brann, fuktighet eller varme omgivelser.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke ut strømadapteren fra stikkontakten.

**Eksponering for radiofrekvensstråling:** Dette MikroTik-utstyret er i samsvar med FCC, IC og EUs strålingseksponeringsgrenser som er angitt for et ukontrollert miljø. Denne MikroTik-enheten skal installeres og betjenes ikke nærmere enn 20 centimeter fra kroppen din, yrkesbrukeren eller allmennheten.

Produsent: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į „RouterOS v7.2.1“ arba naujausią stabilią versiją, kad būtų užtikrinta, jog laikomasi vietos valdžios institucijų taisyklių!
Galutiniai vartotojai privalo laikytis vietos įstatymų, įskaitant veikimą teisėtais dažnio kanalais, išėjimo galią, kabelių reikalavimus ir dinaminio dažnio pasirinkimo (DFS) reikalavimus. Visi „MikroTik“ radijo įrenginiai turi būti įdiegti pagal instrukcijas.
:::

Šios serijos trumpasis vadovas apima modelius: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Tai yra belaidžio tinklo įrenginys. Produkto modelio pavadinimą rasite dėklo etiketėje (ID).*
*Prašome apsilankyti vartotojo vadovo puslapyje [https://mt.lv/um](https://mt.lv/um), kad gautumėte visą naujausią vartotojo vadovą. Arba nuskaitykite QR kodą mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Visas technines specifikacijas, brošiūras ir daugiau informacijos apie produktus rasite [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*Jei jums reikia pagalbos dėl konfigūracijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Šis belaidis produktas turi „Bluetooth®“ technologiją.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Pirmieji žingsniai:**

- Įsitikinkite, kad jūsų interneto paslaugų teikėjas leidžia atlikti aparatinės įrangos pakeitimus ir automatiškai priskiria IP adresą;
- Prieš jungdami prie maitinimo šaltinio, prie įrenginio pritvirtinkite antenas;
- Prijunkite ISP kabelį prie Ethernet1 prievado;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Prijunkite įrenginį per bet kurį iš prievadų, išskyrus Ethernet1, arba belaidžiu tinklu "MikroTik-..." (įsitikinkite, kad patikrinate belaidžių slaptažodžius ant lipduko);
- Sukurkite ryšį naudodami mobilųjį programėlę. Alternatyviai naudokite WebFig naršyklėje arba konfigūracijos įrankį "WinBox" adresu [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Pradėkite konfigūraciją pasirinktame įrankyje, naudodami numatytąją IP adresą 192.168.88.1. Jei IP adresas nepasiekiamas, naudokite WinBox ir pasirinkite skirtuką "Neighbors", kad rastumėte įrenginį;
- Tęskite prisijungdami naudodami MAC adresą. Vartotojo vardas yra "admin", ir nėra slaptažodžio (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Paspauskite mygtuką "Check for updates" ir atnaujinkite RouterOS iki naujausios versijos;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite prietaisą iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Meniu "QuickSet" nustatykite šiuos parametrus: Pasirinkite savo šalį, kad galėtumėte taikyti šalies reguliavimo nustatymus;
- Nustatykite belaidžio tinklo slaptažodį kairėje srityje;
- Nustatykite maršruto slaptažodį apačioje esančioje srityje.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas yra skirtas montuoti patalpose. Laikykite gaminį atokiau nuo vandens, ugnies, drėgmės ir karštos aplinkos.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo adapterį nuo maitinimo lizdo.

**Radijo dažnio spinduliuotės poveikis:** Ši „MikroTik“ įranga atitinka FCC, IC ir Europos Sąjungos radiacijos poveikio ribas, nustatytas nekontroliuojamai aplinkai. Šis „MikroTik“ prietaisas turėtų būti įmontuotas ir valdomas ne arčiau kaip 20 centimetrų atstumu nuo jūsų kūno, profesinio vartotojo ar plačiosios visuomenės.

Gamintojas: Mikrotikls SIA, Brivibas gatve 214i Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūra ir jāatjaunina uz RouterOS v7.2.1 vai jaunāku stabilo versiju, lai nodrošinātu atbilstību vietējās valsts likumdošanai.
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus, ieskaitot darbību likumīgos frekvences kanālos, jaudas izvadi, kabeļu prasības un dinamiskās frekvences izvēles (DFS) prasības. Visām MikroTik radio ierīcēm jābūt uzstādītām atbilstoši instrukcijām.
:::

Šīs sērijas īsā rokasgrāmata attiecas uz modeļiem: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Šī ir bezvadu tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu vietnē [https://mt.lv/um](https://mt.lv/um), lai iegūtu pilnībā atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Pilnas tehniskās specifikācijas, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*Ja, jums nepieciešama palīdzība ar ierīces konfigurēšanu, lūdzu, konsultējieties ar konsultantiem, kontaktinformācija atrodama vietnē [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Šis bezvadu produkts ir aprīkots ar Bluetooth® tehnoloģiju.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Pirmie soļi:**

- Pārliecinieties, vai jūsu interneta pakalpojumu sniedzējs ļauj veikt aparatūras izmaiņas un automātiski piešķir IP adresi;
- Lūdzu, savienojiet antenas ar ierīci pirms pieslēdzat strāvas avotu;
- Pieslēdziet ISP kabeli pie Ethernet1 portas;
- Pieslēdziet ierīci strāvas avotam;
- Pieslēdzieties ierīcei caur jebkuru no portiem, izņemot Ethernet1, vai bezvadu tīklam "MikroTik-..." (pārliecinieties, ka pārbaudāt bezvadu paroles uz uzlīmes);
- Izveidojiet savienojumu, izmantojot mobilās lietotnes. Kā alternatīvu varat izmantot WebFig pārlūkprogrammā vai konfigurācijas rīku "WinBox" vietnē [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Sāciet konfigurēt izvēlētajā rīkā, izmantojot noklusēto IP adresi 192.168.88.1. Ja IP adrese nav pieejama, izmantojiet WinBox un izvēlieties cilni "Neighbors", lai atrastu ierīci;
- Turpiniet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjauniniet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox sadaļu "Files" un pārstartējiet ierīci;
- Atjauninot savu RouterOS programmatūru līdz jaunākajai versijai, varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Sadaļā "QuickSet" iestatiet šādi: Izvēlieties savu valsti, lai piemērotu valsts regulējuma iestatījumus;
- Iestatiet savu bezvadu tīkla paroli kreisajā laukumā;
- Iestatiet savas maršruta paroli apakšējā laukumā.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Uzstādītājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Uzstādītāja pienākums ir pārliecināties, ka aprīkojuma uzstādīšana atbilst vietējiem un nacionālajiem elektrības noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šis produkts ir paredzēts uzstādīšanai telpās. Sargājiet šo izstrādājumu no ūdens, uguns, mitruma vai karstas vides.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas adapteri no kontaktligzdas.

**Radiofrekvences starojuma iedarbība:** Šī MikroTik iekārta atbilst FCC, IC un Eiropas Savienības radiācijas iedarbības ierobežojumiem, kas noteikti nekontrolētai videi. Šī MikroTik ierīce jāuzstāda un jādarbina ne tuvāk par 20 centimetriem no ķermeņa, profesionāla lietotāja vai plašas sabiedrības.

Ražotājs: Mikrotikls SIA, Brīvības gatve 214i Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.2.1 jew l-aħħar verżjoni stabbli, sabiex tkun assigurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż, inkluż it-tħaddim fil-kanali tal-frekwenza legali, l-enerġija tal-ħruġ, ir-rekwiżiti tal-kejbils u r-rekwiżiti tal-Għażla Dinamika tal-Frekwenza (DFS). L-apparati kollha tar-radju MikroTik għandhom jiġu installati skond l-istruzzjonijiet.
:::

Din is-serje ta' Gwidi Quick tkopri mudelli: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Dan huwa apparat tan-netwerk mingħajr fili. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna tal-manwal tal-utent fuq [https://mt.lv/um](https://mt.lv/um) għall-manwal tal-utent aġġornat sħiħ. Jew skannja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi sħaħ, fuljetti, u aktar tagħrif dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*Jekk għandek bżonn għajnuna bil-konfigurazzjoni, jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Dan il-prodott Wireless għandu teknoloġija Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**L-ewwel passi:**

- Ċertifika li l-fornitur ta 'servizz tal-internet tiegħek tippermetti bidliet fil-ħardwer u jintwera awtomatikament indirizz IP;
- Jekk jogħġbok waħħal antenni mal-apparat, qabel ma tikkonnettja mas-sors tal-enerġija;
- Ikkonnetta il-kaċċatur tal-fornitur tal-internet għall-port Ethernet1;
- Ikkonnetta l-apparat għall-sors tal-ħasil;
- Ikkonnetta mal-apparat permezz ta 'waħda mill-portijiet, bla Ethernet1, jew il-ħsieb bla wajers "MikroTik-..." (assigura li tikkontrolla l-passwords bla wajers fuq il-marcatur);
- Ewlenija bl-użu ta 'applikazzjoni mobbli. Bħala alternattiva, uża l-WebFig f'browser jew l-għodda ta' konfigurazzjoni "WinBox" fuq [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Ibda l-konfigurazzjoni fi ħdan l-għażla tal-għodda, bl-użu tal-indirizz IP predefinit 192.168.88.1. Jekk l-indirizz IP mhux disponibbli, uża l-WinBox u għażel it-tab "Neighbors" biex issib id-dispożitt;
- Żomm mill-quddiem biex tikkolet b'indirizz MAC. L-username huwa "admin," u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-kodiċijiet tal-utent u t-tal-wi-fi fuq l-isticker);
- Ikklikkja fuq il-buttuna "Check for updates" u agħġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Żid id-pakketti li dawn tniżżel fil-meni "Files" ta 'WebFig jew WinBox u rirreboot l-apparat;
- Billi taġġorna l-software RouterOS għall-aħħar verżjoni, tista 'tiżgura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Fl-menù "QuickSet" iwaqqaf l-iskont segwenti: Agħżel pajjiżek biex tapplika settings tar-regolazzjoni tal-pajjiż;
- Isetta il-password tal-netwerk tal-wi-fi tiegħek fis-suq;
- Isetta il-password tar-router tiegħek fis-suq.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jiġi installat fuq ġewwa. Żomm dan il-prodott 'il bogħod minn ilma, nar, umdità jew ambjenti sħan.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ l-adapter tal-enerġija mill-iżbokk tad-dawl.

**Esponiment għal Radjazzjoni ta 'Frekwenza tar-Radju:** Dan it-tagħmir MikroTik jikkonforma mal-limiti ta' esponiment ta 'FCC, IC u l-Unjoni Ewropea għar-radjazzjoni stabbiliti għal ambjent mhux kontrollat. Dan l-apparat MikroTik għandu jkun installat u jitħaddem mhux eqreb minn 20 ċentimetru minn ġismek, l-utent okkupazzjonali jew il-pubbliku ġenerali.

Manifattur: Mikrotikls SIA, Brivibas Gve 214i Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.2.1 of de nieuwste stabiele versie, om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften te volgen, waaronder de werking binnen de wettelijke frequentiekanalen, uitgangsvermogen, bekabelingsvereisten en vereisten voor dynamische frequentiekeuze (DFS). Alle MikroTik-radioapparaten moeten volgens de instructies worden geïnstalleerd.
:::

Deze serie snelgidsen behandelt modellen: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Dit is een draadloos netwerkapparaat. U kunt de modelnaam van het product vinden op het dooslabel (ID).*
*Bezoek de gebruikershandleiding op [https://mt.lv/um](https://mt.lv/um) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Volledige technische specificaties, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*Als u hulp nodig heeft bij de configuratie, zoek dan een consulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Dit draadloze product is voorzien van Bluetooth®-technologie.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Eerste stappen:**

- Zorg ervoor dat uw internetprovider hardwarewijzigingen toestaat en automatisch een IP-adres toewijst;
- Bevestig antennes op het apparaat voordat u het op de stroombron aansluit;
- Sluit de ISP-kabel aan op poort Ethernet1;
- Sluit het apparaat aan op de stroombron;
- Verbind met het apparaat via een van de poorten, met uitzondering van Ethernet1, of het draadloze netwerk "MikroTik-..." (controleer de draadloze wachtwoorden op het etiket);
- Maak verbinding met behulp van een mobiele applicatie. Als alternatief kunt u WebFig gebruiken in een webbrowser of het configuratiehulpmiddel "WinBox" op [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Start de configuratie binnen het gekozen gereedschap met het standaard IP-adres 192.168.88.1. Als het IP-adres niet beschikbaar is, gebruik WinBox en kies het tabblad "Neighbors" om het apparaat te vinden;
- Ga verder met verbinden met behulp van het MAC-adres. De gebruikersnaam is "admin" en er is geen wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- In het "QuickSet"-menu stelt u het volgende in: Kies uw land om landreguleringsinstellingen toe te passen;
- Stel uw draadloze netwerkwachtwoord in het linker veld in;
- Stel uw routerwachtwoord in het onderste veld in.

**Veiligheidsinformatie:**

- Voordat u aan een MikroTik-apparaat gaat werken, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die u kunt vinden in de originele verpakking van dit product.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om binnenshuis te worden geïnstalleerd. Houd dit product uit de buurt van water, vuur, vochtigheid of hete omgevingen.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom als het defect is. De snelste manier om dit te doen is door de stroomadapter uit het stopcontact te halen.

**Blootstelling aan radiofrequente straling:** deze MikroTik-apparatuur voldoet aan de FCC-, IC- en EU-limieten voor blootstelling aan straling die zijn vastgelegd voor een ongecontroleerde omgeving. Dit MikroTik-apparaat moet worden geïnstalleerd en bediend op niet meer dan 20 centimeter van uw lichaam, beroepsgebruiker of het grote publiek.

Fabrikant: Mikrotikls SIA, Brivibas gatve 214i Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do wersji RouterOS v7.2.1 lub najnowszej stabilnej wersji, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych, w tym działania w ramach legalnych kanałów częstotliwości, mocy wyjściowej, wymagań dotyczących okablowania i wymagań dynamicznego wyboru częstotliwości (DFS). Wszystkie urządzenia radiowe MikroTik należy zainstalować zgodnie z instrukcjami.
:::

Krótki przewodnik po tej serii obejmuje modele: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*To jest urządzenie sieci bezprzewodowej. Nazwę modelu produktu można znaleźć na etykiecie opakowania (ID).*
*Odwiedź stronę podręcznika użytkownika pod adresem [https://mt.lv/um](https://mt.lv/um), aby uzyskać pełną, aktualną instrukcję obsługi. Lub zeskanuj kod QR telefonem komórkowym.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Pełne specyfikacje techniczne, broszury i więcej informacji o produktach na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Jeśli potrzebujesz pomocy przy konfiguracji, skontaktuj się z konsultantem [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ten produkt bezprzewodowy obsługuje technologię Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Pierwsze kroki:**

- Upewnij się, że dostawca usług internetowych zezwala na zmiany sprzętu i automatycznie przypisuje adres IP;
- Proszę podłączyć anteny do urządzenia, przed podłączeniem do źródła zasilania;
- Podłącz kabel dostawcy usług internetowych do portu Ethernet1;
- Podłącz urządzenie do źródła zasilania;
- Połącz się z urządzeniem za pomocą jednego z portów, z wyłączeniem Ethernet1, lub z siecią bezprzewodową "MikroTik-..." (sprawdź hasła do sieci bezprzewodowej na naklejce);
- Utwórz połączenie za pomocą aplikacji mobilnej. Alternatywnie użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox" pod adresem [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Rozpocznij konfigurację w wybranym narzędziu, używając domyślnego adresu IP 192.168.88.1. Jeśli adres IP nie jest dostępny, użyj WinBoxa i wybierz zakładkę "Neighbors", aby odnaleźć urządzenie;
- Przejdź do połączenia za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła brak (lub, dla niektórych modeli, sprawdź hasła użytkownika i do sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Wgraj pobrane pakiety do menu "Files" w WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- W menu "QuickSet" skonfiguruj następujące: Wybierz swój kraj, aby zastosować ustawienia regulacji krajowej;
- Skonfiguruj hasło do swojej sieci bezprzewodowej w lewym polu;
- Skonfiguruj hasło do routera w dolnym polu.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt jest przeznaczony do instalacji w pomieszczeniach. Trzymaj ten produkt z dala od wody, ognia, wilgoci lub gorących środowisk.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem jest odłączenie zasilacza od gniazdka elektrycznego.

**Ekspozycja na promieniowanie o częstotliwości radiowej:** To urządzenie MikroTik jest zgodne z limitami ekspozycji na promieniowanie FCC, IC i Unii Europejskiej określonymi dla niekontrolowanego środowiska. To urządzenie MikroTik powinno być instalowane i obsługiwane nie bliżej niż 20 centymetrów od ciała, użytkownika zawodowego lub ogółu społeczeństwa.

Producent: Mikrotikls SIA, Brivibas gatve 214i Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.2.1 ou a versão estável mais recente, para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país, incluindo a operação dentro dos canais legais de frequência, potência de saída, requisitos de cabeamento e requisitos de Seleção Dinâmica de Frequência (DFS). Todos os dispositivos de rádio MikroTik devem ser instalados de acordo com as instruções.
:::

O Guia rápido desta série cobre os modelos: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Este é um dispositivo de rede sem fio. Você pode encontrar o nome do modelo do produto na etiqueta da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um](https://mt.lv/um) para obter o manual do usuário atualizado. Ou escaneie o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas completas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Se precisar de ajuda com a configuração, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Este produto sem fio possui tecnologia Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Primeiros passos:**

- Certifique-se de que o provedor de serviços de Internet permite alterações de hardware e atribui automaticamente um endereço IP;
- Conecte antenas ao dispositivo antes de conectá-lo à fonte de alimentação;
- Conecte o cabo do provedor de serviços de Internet à porta Ethernet1;
- Conecte o dispositivo à fonte de alimentação;
- Conecte-se ao dispositivo através de qualquer uma das portas, exceto Ethernet1, ou pela rede sem fio "MikroTik-..." (verifique as senhas da rede sem fio na etiqueta);
- Estabelecer uma conexão usando um aplicativo móvel. Alternativamente, use o WebFig em um navegador da web ou a ferramenta de configuração "WinBox" em [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Inicie a configuração dentro da ferramenta escolhida, usando o endereço IP padrão 192.168.88.1. Se o endereço IP não estiver disponível, use o WinBox e escolha a guia "Neighbors" para encontrar o dispositivo;
- Prossiga para se conectar usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique as senhas do usuário e sem fio no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Carregue os pacotes baixados no menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar seu software RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- No menu "QuickSet", configure o seguinte: Escolha o seu país para aplicar as configurações de regulamentação do país;
- Configure a senha da sua rede sem fio no campo esquerdo;
- Configure a senha do seu roteador no campo inferior.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser instalado em ambiente interno. Mantenha este produto longe de água, fogo, umidade ou ambientes quentes.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o adaptador de energia da tomada.

**Exposição à radiação de radiofrequência:** Este equipamento MikroTik está em conformidade com os limites de exposição à radiação da FCC, IC e União Europeia estabelecidos para um ambiente não controlado. Este dispositivo MikroTik deve ser instalado e operado a menos de 20 centímetros de seu corpo, usuário ocupacional ou público em geral.

Fabricante: Mikrotikls SIA, Brivibas gatve 214i Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la RouterOS v7.2.1 sau la cea mai recentă versiune stabilă, pentru a asigura respectarea reglementărilor autorității locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării, inclusiv operarea în cadrul canalelor de frecvență legale, puterea de ieșire, cerințele de cablare și cerințele de selecție a frecvenței dinamice (DFS). Toate dispozitivele radio MikroTik trebuie instalate conform instrucțiunilor.
:::

Această serie de ghiduri rapide acoperă modelele: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Acesta este un dispozitiv de rețea fără fir. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului de utilizare de pe [https://mt.lv/um](https://mt.lv/um) pentru manualul de utilizare complet actualizat. Sau scanați codul QR cu telefonul mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice complete, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dacă aveți nevoie de ajutor pentru configurare, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Acest produs wireless oferă tehnologie Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Primii pasi:**

- Asigurați-vă că furnizorul dvs. de servicii internet permite modificările de hardware și atribuie automat o adresă IP;
- Vă rugăm să atașați antenele la dispozitiv, înainte de a vă conecta la sursa de alimentare;
- Conectați cablul furnizorului de servicii internet la portul Ethernet1;
- Conectați dispozitivul la sursa de alimentare;
- Conectați-vă la dispozitiv printr-unul dintre porturi, cu excepția Ethernet1, sau prin rețeaua wireless "MikroTik-..." (verificați parolele wireless pe autocolant);
- Stabiliți o conexiune folosind o aplicație mobilă. Alternativ, utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox" la [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Începeți configurarea în instrumentul ales, utilizând adresa IP implicită 192.168.88.1. Dacă adresa IP nu este disponibilă, utilizați WinBox și alegeți fila "Neighbors" pentru a găsi dispozitivul;
- Continuați să vă conectați utilizând adresa MAC. Numele de utilizator este "admin", și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless de pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- În meniul "QuickSet" configurați următoarele: Alegeți țara pentru a aplica setările de reglementare ale țării;
- Configurați parola rețelei wireless în câmpul din stânga;
- Configurați parola routerului în câmpul de jos.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs este destinat să fie instalat în interior. Păstrați acest produs departe de apă, foc, umiditate sau medii calde.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta adaptorul de alimentare de la priza electrică.

**Expunerea la radiații de frecvență radio:** Acest echipament MikroTik respectă limitele de expunere la radiații FCC, IC și Uniunea Europeană stabilite pentru un mediu necontrolat. Acest dispozitiv MikroTik ar trebui instalat și funcționat la cel mult 20 centimetri de corpul dvs., de utilizatorul ocupațional sau de publicul larg.

Producător: Mikrotikls SIA, Brivibas gatve 214i Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na RouterOS v7.2.1 alebo na najnovšiu stabilnú verziu, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na konečných užívateľoch, aby dodržiavali miestne predpisy, vrátane prevádzky v rámci legálnych frekvenčných kanálov, výstupného výkonu, požiadaviek na kabeláž a požiadaviek na dynamický výber frekvencie (DFS). Všetky rádiové zariadenia MikroTik musia byť nainštalované podľa pokynov.
:::

Táto séria Stručný sprievodca sa týka modelov: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Toto je bezdrôtové sieťové zariadenie. Názov modelu produktu nájdete na štítku puzdra (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete na stránke používateľskej príručky na adrese [https://mt.lv/um](https://mt.lv/um). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Kompletné technické špecifikácie, brožúry a ďalšie informácie o produktoch na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Ak potrebujete pomoc s konfiguráciou, vyhľadajte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Tento bezdrôtový výrobok je vybavený technológiou Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Prvé kroky:**

- Uistite sa, že váš poskytovateľ internetových služieb umožňuje zmeny v hardvéri a automaticky prideliť IP adresu;
- Pred pripojením k zdroju napájania pripojte k zariadeniu antény;
- Pripojte kábel poskytovateľa internetových služieb k portu Ethernet1;
- Pripojte zariadenie k zdroju napájania;
- Pripojte sa k zariadeniu prostredníctvom ktorehokoľvek z portov s výnimkou Ethernet1 alebo bezdrôtovej siete "MikroTik-..." (skontrolujte heslá k bezdrôtovej sieti na štítku);
- Vytvorte pripojenie pomocou mobilnej aplikácie. Alternatívne použite WebFig v webovom prehliadači alebo nástroj na konfiguráciu "WinBox" na adrese [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Spustite konfiguráciu vo vybranom nástroji s predvolenou IP adresou 192.168.88.1. Ak adresa IP nie je k dispozícii, použite WinBox a vyberte kartu "Neighbors", aby ste zariadenie našli;
- Pokračujte v pripájaní pomocou MAC adresy. Užívateľské meno je "admin" a nie je žiadne heslo (alebo, pre niektoré modely, skontrolujte užívateľské a bezdrôtové heslá na štítku);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" v aplikácii WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a bezpečnostné aktualizácie;
- V menu "QuickSet" nastavte nasledujúce: Vyberte svoju krajinu, aby ste aplikovali nastavenia regulácie krajiny;
- Nastavte heslo k vašej bezdrôtovej sieti v ľavom poli;
- Nastavte heslo k vášmu routeru v dolnom poli.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento produkt je určený na inštaláciu vo vnútri. Chráňte tento výrobok pred vodou, ohňom, vlhkosťou alebo horúcim prostredím.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťového adaptéra zo sieťovej zásuvky.

**Vystavenie vysokofrekvenčnému žiareniu:** Toto zariadenie MikroTik spĺňa limity vystavenia žiareniu FCC, IC a Európskej únie stanovené pre nekontrolované prostredie. Toto zariadenie MikroTik by malo byť nainštalované a prevádzkované nie ďalej ako 20 centimetrov od vášho tela, profesionálneho používateľa alebo širokej verejnosti.

Výrobca: Mikrotikls SIA, Brivibas gatve 214i Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.2.1 ali najnovejšo stabilno različico, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so dolžni upoštevati lokalne predpise, vključno z delovanjem v zakonitih frekvenčnih kanalih, izhodno močjo, zahtevami za kabliranje in zahtevami dinamičnega izbiranja frekvenc (DFS). Vse radijske naprave MikroTik morajo biti nameščene v skladu z navodili.
:::

Ta serija hitrih navodil zajema modele: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*To je brezžična omrežna naprava. Ime modela izdelka najdete na nalepki ohišja (ID).*
*Obiščite stran z navodili za uporabo na [https://mt.lv/um](https://mt.lv/um), kjer najdete popoln in posodobljen uporabniški priročnik. Ali skenirajte kodo QR z mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Popolne tehnične specifikacije, brošure in več informacij o izdelkih najdete na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Če potrebujete pomoč pri konfiguraciji, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Ta brezžični izdelek ima tehnologijo Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Prvi koraki:**

- Prepričajte se, da vaš ponudnik internetnih storitev omogoča spremembe strojne opreme in samodejno dodeli IP naslov;
- Priključite antene na napravo, preden jo priključite na vir napajanja;
- Povežite kabel ponudnika internetnih storitev v vrata Ethernet1;
- Povežite napravo z napajalnikom;
- Povežite se z napravo prek katerega koli od vrat, razen Ethernet1, ali prek brezžičnega omrežja "MikroTik-..." (preverite gesla za brezžično omrežje na nalepki);
- Ustvarite povezavo z uporabo mobilne aplikacije. Kot alternativo uporabite WebFig v spletnem brskalniku ali orodje za konfiguracijo "WinBox" na [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Začnite konfiguracijo znotraj izbranega orodja, uporabite privzeti IP naslov 192.168.88.1. Če IP naslov ni na voljo, uporabite WinBox in izberite zavihek "Neighbors", da najdete napravo;
- Nadaljujte s povezovanjem z uporabo MAC naslova. Uporabniško ime je "admin," in gesla ni (ali, za nekatere modele, preverite gesla za uporabnika in brezžična gesla na nalepki);
- Kliknite gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" v aplikaciji WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico lahko zagotovite optimalno delovanje, stabilnost in posodobitve varnosti;
- V meniju "QuickSet" nastavite naslednje: Izberite svojo državo, da uporabite nastavitve regulacije države;
- Nastavite geslo za svoje brezžično omrežje v levem polju;
- Nastavite geslo za svoj usmerjevalnik v spodnjem polju.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek je namenjen namestitvi v zaprtih prostorih. Izdelek hranite ločeno od vode, ognja, vlage ali vročega okolja.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da napajalnik odklopite iz vtičnice.

**Izpostavljenost radiofrekvenčnim sevanjem:** Ta oprema MikroTik ustreza mejam izpostavljenosti sevanju FCC, IC in Evropske unije, določenim za nenadzorovano okolje. To napravo MikroTik je treba namestiti in uporabljati največ 20 centimetrov od vašega telesa, poklicnega uporabnika ali splošne javnosti.

Proizvajalec: Mikrotikls SIA, Brivibas gatve 214i Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Den här enheten måste uppgraderas till RouterOS v7.2.1 eller den senaste stabila versionen för att säkerställa överensstämmelse med lokala myndighetsbestämmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler, inklusive drift inom lagliga frekvenskanaler, utgångseffekt, kablingskrav och DFS-krav (Dynamic Frequency Selection). Alla MikroTik-radioenheter måste installeras enligt instruktionerna.
:::

Den här snabbguideserien täcker modellerna: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Detta är en trådlös nätverksenhet. Du hittar produktmodellnamnet på fodraletiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um](https://mt.lv/um) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Fullständiga tekniska specifikationer, broschyrer och mer info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*Om du behöver hjälp med konfigurationen, vänligen sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Denna trådlösa produkt har Bluetooth®-teknik.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Första stegen:**

- Se till att din internetleverantör tillåter hårdvaruändringar och tilldelar en IP-adress automatiskt;
- Vänligen anslut antenner till enheten innan du ansluter till strömkällan;
- Anslut ISP-kabeln till Ethernet1-porten;
- Anslut enheten till strömkällan;
- Anslut till enheten genom någon av portarna, förutom Ethernet1, eller det trådlösa nätverket "MikroTik-..." (se till att kontrollera de trådlösa lösenorden på klistermärket);
- Skapa en anslutning med hjälp av en mobilapplikation. Alternativt använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" på [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Påbörja konfigurationen inom det valda verktyget med standard IP-adress 192.168.88.1. Om IP-adressen inte är tillgänglig, använd WinBox och välj fliken "Neighbors" för att hitta enheten;
- Fortsätt att ansluta med hjälp av MAC-adressen. Användarnamnet är "admin" och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppgradera din RouterOS-programvara till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- I menyn "QuickSet" konfigurerar du följande: Välj ditt land för att tillämpa landsregleringsinställningar;
- Ställ in ditt trådlösa nätverkslösenord i det vänstra fältet;
- Ställ in ditt routerlösenord i det nedre fältet.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt är avsedd att installeras inomhus. Håll produkten borta från vatten, eld, luftfuktighet eller heta miljöer.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur nätadaptern från eluttaget.

**Exponering för radiofrekvensstrålning:** Denna MikroTik-utrustning överensstämmer med FCC, IC och Europeiska unionens strålningsexponeringsgränser som anges för en okontrollerad miljö. Denna MikroTik-enhet ska installeras och användas högst 20 centimeter från din kropp, yrkesanvändare eller allmänheten.

Tillverkare: Mikrotikls SIA, Brivibas gatve 214i Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到RouterOS v7.2.1或最新的稳定版本，以确保符合地方法规！
最终用户有责任遵守当地国家/地区的法规，包括在合法频道内运行，输出功率，电缆要求和动态频率选择（DFS）要求。必须按照说明安装所有MikroTik无线电设备。
:::

本系列快速指南涵盖以下型号：RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*这是一个无线网络设备。您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um](https://mt.lv/um) 上的用户手册页面， 以获取最新的用户手册。或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*完整的技术规格，手册以及有关产品的更多信息，请访问[https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*如果您需要配置方面的帮助，请寻求顾问 [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*此无线产品具有Bluetooth®技术。*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**第一步：**

- 确保您的互联网服务提供商允许硬件更改并将自动分配IP地址;
- *在连接电源之前，请先将天线连接到设备上；*
- 将ISP电缆连接到Ethernet1端口;
- 将设备连接到电源;
- 通过任何端口之一连接到设备，不包括Ethernet1，或连接到无线网络"MikroTik-..."（确保在贴纸上检查无线密码）;
- 使用移动应用程序建立连接。或者，使用WebFig在Web浏览器中或在[https://mt.lv/winbox](https://mt.lv/winbox) 上的"WinBox"配置工具; **提供多种配置方法以确保可访问性；**
- 在所选工具中使用默认IP地址192.168.88.1开始配置。如果IP地址不可用，请使用WinBox并选择“邻居”选项卡查找设备;
- 继续使用MAC地址进行连接。用户名为"admin"，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）;
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的"Files"菜单，并重新启动设备;
- 通过将RouterOS软件升级到最新版本，可以确保最佳性能、稳定性和安全更新;
- 在"QuickSet"菜单中设置以下内容: 选择您的国家以应用国家法规设置;
- 在左侧字段中设置您的无线网络密码;
- 在底部字段中设置您的路由器密码。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 该产品旨在安装在室内。 请将本产品远离水，火，潮湿或高温的环境。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源适配器。

**射频辐射暴露：** 此MikroTik设备符合针对不受控制的环境所设定的FCC，IC和欧盟辐射暴露限制。 此MikroTik设备的安装和操作距离您的身体，职业用户或公众的距离不得超过20厘米。

制造商：Mikrotikls SIA，拉脱维亚Brivibas gatve 214i Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство должно быть обновлено до RouterOS v7.2.1 или до последней стабильной версии, чтобы обеспечить соответствие местным нормативным требованиям!
Конечные пользователи несут ответственность за соблюдение местных нормативных требований, включая работу в рамках допустимых частотных каналов, выходную мощность, требования к кабельным системам и требования к динамическому выбору частоты (DFS). Все радиоустройства MikroTik должны быть установлены в соответствии с инструкциями.
:::

Эта серия кратких руководств охватывает модели: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Это беспроводное сетевое устройство. Вы можете найти название модели продукта на этикетке (ID) корпуса.*
*Пожалуйста, посетите страницу руководства пользователя по адресу [https://mt.lv/um](https://mt.lv/um), чтобы получить полное актуальное руководство пользователя. Или отсканируйте QR-код своим мобильным телефоном.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Полные технические характеристики, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Если вам нужна помощь с настройкой, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Этот беспроводной продукт поддерживает технологию Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Первые шаги:**

- Убедитесь, что ваш интернет-провайдер разрешает изменения в оборудовании и автоматически назначает IP-адрес;
- Пожалуйста, прикрепите антенны к устройству перед подключением к источнику питания;
- Подключите кабель провайдера к порту Ethernet1;
- Подключите устройство к источнику питания;
- Подключитесь к устройству через любой из портов, исключая Ethernet1, или беспроводную сеть "MikroTik-..." (обязательно проверьте пароли от беспроводной сети на наклейке);
- Установите соединение с помощью мобильного приложения. В качестве альтернативы используйте WebFig в веб-браузере или инструмент конфигурации "WinBox" доступный по адресу [https://mt.lv/winbox](https://mt.lv/winbox); **существует несколько методов настройки для обеспечения доступности;**
- Начните настройку в выбранном инструменте, используя стандартный IP-адрес 192.168.88.1. Если IP-адрес недоступен, используйте WinBox и выберите вкладку "Neighbors", чтобы найти устройство;
- Продолжайте подключение, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте пользовательские и беспроводные пароли на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" в WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- В меню "QuickSet" настройте следующее: выберите свою страну, чтобы применить настройки регулирования страны;
- Установите пароль для вашей беспроводной сети в левом поле;
- Установите пароль для вашего роутера в нижнем поле.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Этот продукт можно использовать как в помещении, так и на открытом воздухе. Перед началом установки внимательно прочтите инструкции по монтажу. Неспособность использовать правильное оборудование и конфигурацию или следовать правильным процедурам может привести к опасной ситуации для людей и повреждению системы.
- Мы не можем гарантировать, что в результате неправильного использования устройства не произойдет несчастных случаев или повреждений. Пожалуйста, используйте этот продукт с осторожностью и действуйте на свой страх и риск!
- В случае сбоя устройства отключите его от питания. Самый быстрый способ сделать это - вынуть вилку из розетки.

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

**Воздействие радиочастотного излучения.** *Это устройство MikroTik должно устанавливаться и эксплуатироваться не ближе 20 сантиметров от человека.*

| Частотный диапазон | Мощность передатчика |
| --- | --- |
| 2400-2483.5 МГц | ≤100 мВт |

Доступные частотные каналы могут различаться в зависимости от модели продукта и сертификации.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две
последующие означают номер недели.

![](./img/image2020-1-24_7-55-5.badge-82.png)

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. **Cм. на упаковке.**

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу. Информация об импортерах продукции MikroTik в Российскую Федерацию: https://mikrotik.com/buy/europe/russia

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS v7.2.1 або останньої стабільної версії, щоб забезпечити відповідність місцевим нормам влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил, включаючи функціонування в межах законних частотних каналів, вихідну потужність, вимоги до кабелів та вимоги щодо вибору динамічної частоти (DFS). Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

Цей короткий посібник охоплює моделі: RB924iR-2nD-BT5&BG77&R11e-LR8 (KNOT LR8 kit).

*Це пристрій бездротової мережі. Ви можете знайти назву моделі товару на етикетці футляра (ID).*
*Будь ласка, відвідайте сторінку керівництва користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) щоб отримати повне оновлене керівництво користувача. Або відскануйте QR-код за допомогою мобільного телефону.*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Повні технічні специфікації, брошури та додаткову інформацію про товари можна знайти на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [https://mt.lv/help-ua](https://mt.lv/help-ua)*
*Якщо вам потрібна допомога з налаштуванням, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*
*Цей бездротовий виріб оснащений технологією Bluetooth®.*

![](./img/image2020-1-31_12-4-32.badge-83.png)

**Перші кроки:**

- Переконайтеся, що ваш інтернет-провайдер дозволяє зміни в апаратурі та автоматично призначає IP-адресу;
- Будь ласка, приєднайте антени до пристрою перед підключенням до джерела живлення;
- Підключіть кабель провайдера до порту Ethernet1;
- Підключіть пристрій до джерела живлення;
- Підключіться до пристрою через будь-який з портів, за винятком Ethernet1, або бездротову мережу "MikroTik-..." (обов'язково перевірте паролі від бездротової мережі на наклейці);
- Встановіть з'єднання за допомогою мобільного додатка. Альтернативно, використовуйте WebFig у веб-браузері, або інструмент конфігурації "WinBox", доступний за адресою [https://mt.lv/winbox](https://mt.lv/winbox); **існує декілька методів налаштування для забезпечення доступності;**
- Розпочніть конфігурацію за допомогою обраного інструменту, використовуючи стандартну IP-адресу 192.168.88.1. Якщо IP-адреса недоступна, використовуйте WinBox і виберіть вкладку "Neighbors", щоб знайти пристрій;
- Продовжуйте підключення, використовуючи MAC-адресу. Ім'я користувача - "admin", і немає пароля (або, для деяких моделей, перевірте паролі користувача та бездротові паролі на наклейці);
- Клацніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" у WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- У меню "QuickSet" встановіть наступне: виберіть свою країну, щоб застосувати налаштування регулювання країни;
- Налаштуйте пароль для вашої бездротової мережі в лівому полі;
- Налаштуйте пароль для вашого маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати над будь-яким обладнанням MikroTik, пам’ятайте про небезпеки, пов'язані з електричною схемою, та ознайомтеся зі стандартними методами запобігання аварій. Інсталятор повинен бути знайомий з мережевими структурами, термінами та поняттями.
- Використовуйте тільки джерело живлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання повинно встановлюватися кваліфікованим та кваліфікованим персоналом відповідно до цих інструкцій з монтажу. Інсталятор несе відповідальність за те, щоб Установка обладнання відповідала місцевим та національним електричним кодам. Не намагайтеся розбирати, ремонтувати чи змінювати пристрій.
- Цей виріб призначений для встановлення в приміщенні. Тримайте цей продукт подалі від води, вогню, вологості або жаркого середовища.
- Ми не можемо гарантувати, що через неправильне використання пристрою не трапляються аварії та пошкодження. Будь ласка, використовуйте цей продукт обережно та працюйте на свій страх і ризик!
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши адаптер живлення від розетки.

**Вплив радіочастотного випромінювання:** Це обладнання MikroTik відповідає нормам радіаційного опромінення FCC, IC та Європейського Союзу, встановленим для неконтрольованого середовища. Цей пристрій MikroTik слід встановлювати та експлуатувати не ближче 20 сантиметрів від вашого тіла, професіонала чи широкого загалу.

Виробник: Mikrotikls SIA, Brivibas gatve 214i Рига, Латвія, LV1039.

Робоча частота (Максимальна вихідна потужність): 2400-2483.5 МГц (20 дБм)

## UKCA marking

![](./img/ukca_black_fill.badge-79.gif)

## CE Declaration of Conformity

| BG | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RB924iR-2nD-BT5&BG77&R11e-LR8 е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: [https://mikrotik.com/products](https://mikrotik.com/products) |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RB924iR-2nD-BT5&BG77&R11e-LR8 je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DA | Hermed erklærer Mikrotīkls SIA, at radioudstyrstypen RB924iR-2nD-BT5&BG77&R11e-LR8 er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| DE | Hiermit erklärt Mikrotīkls SIA, dass der Funkanlagentyp RB924iR-2nD-BT5&BG77&R11e-LR8 der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EL | Με την παρούσα ο/η Mikrotīkls SIA, δηλώνει ότι ο ραδιοεξοπλισμός RB924iR-2nD-BT5&BG77&R11e-LR8 πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: [https://mikrotik.com/products](https://mikrotik.com/products) |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type RB924iR-2nD-BT5&BG77&R11e-LR8 is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RB924iR-2nD-BT5&BG77&R11e-LR8 es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: [https://mikrotik.com/products](https://mikrotik.com/products) |
| ET | Käesolevaga deklareerib Mikrotīkls SIA, et käesolev raadioseadme tüüp RB924iR-2nD-BT5&BG77&R11e-LR8 vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RB924iR-2nD-BT5&BG77&R11e-LR8 on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: [https://mikrotik.com/products](https://mikrotik.com/products) |
| FR | Le soussigné, Mikrotīkls SIA, déclare que l'équipement radioélectrique du type RB924iR-2nD-BT5&BG77&R11e-LR8 est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RB924iR-2nD-BT5&BG77&R11e-LR8 u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| HU | Mikrotīkls SIA igazolja, hogy a RB924iR-2nD-BT5&BG77&R11e-LR8 típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IT | Il fabbricante, Mikrotīkls SIA, dichiara che il tipo di apparecchiatura radio RB924iR-2nD-BT5&BG77&R11e-LR8 è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| IS | Hér með lýsir Mikrotīkls SIA því yfir að RB924iR-2nD-BT5&BG77&R11e-LR8 er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsingar er að finna á eftirfarandi veffangi: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LT | Aš, Mikrotīkls SIA, patvirtinu, kad radijo įrenginių tipas RB924iR-2nD-BT5&BG77&R11e-LR8 atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RB924iR-2nD-BT5&BG77&R11e-LR8 atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: [https://mikrotik.com/products](https://mikrotik.com/products) |
| MT | B'dan, Mikrotīkls SIA, niddikjara li dan it-tip ta' tagħmir tar-radju RB924iR-2nD-BT5&BG77&R11e-LR8 huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NL | Hierbij verklaar ik, Mikrotīkls SIA, dat het type radioapparatuur RB924iR-2nD-BT5&BG77&R11e-LR8 conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: [https://mikrotik.com/products](https://mikrotik.com/products) |
| NO | Mikrotīkls SIA erklærer herved at utstyret RB924iR-2nD-BT5&BG77&R11e-LR8 er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RB924iR-2nD-BT5&BG77&R11e-LR8 jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: [https://mikrotik.com/products](https://mikrotik.com/products) |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RB924iR-2nD-BT5&BG77&R11e-LR8 está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RB924iR-2nD-BT5&BG77&R11e-LR8 este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RB924iR-2nD-BT5&BG77&R11e-LR8 je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme RB924iR-2nD-BT5&BG77&R11e-LR8 skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: [https://mikrotik.com/products](https://mikrotik.com/products) |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RB924iR-2nD-BT5&BG77&R11e-LR8 överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: [https://mikrotik.com/products](https://mikrotik.com/products) |

## WLAN/BlueTooth/LR/LTE

  
    
      
        Operating Frequency / Maximum output power
        Betriebsfrequenz / maximale Ausgangsleistung
        Fréquence de fonctionnement / puissance de sortie maximale
        Frequenza operativa / massima potenza di uscita
        Frecuencia de funcionamiento / potencia de salida máxima
        Рабочая частота / максимальная выходная мощность
      
      WLAN
      2400-2483.5 MHz / 20 dBm
    
    Bluetooth2400-2483.5 MHz / 10 dBm
    LR (SRD)863-870 MHz / 14 dBm
    LTE FDD Band 12100 MHz / 21 dBm
    LTE FDD Band 31800 MHz / 21 dBm
    LTE FDD Band 8900 MHz / 21 dBm
    LTE FDD Band 20800 MHz / 21 dBm
    LTE FDD Band 28700 MHz / 21 dBm
  

(EN) This MikroTik device meets Maximum WLAN and LTE transmit power limits per ETSI regulations. For more detailed information see Declaration of Conformity above / (DE) Dieses MikroTik-Gerät erfüllt die maximalen WLAN- und LTE-Sendeleistung Grenzwerte gemäß ETSI-Bestimmungen. Weitere Informationen finden Sie oben unter Konformitätserklärung / (FR) Cet appareil MikroTik respecte les limites maximales de puissance de transmission WLAN et LTE conformément aux réglementations ETSI. Pour plus d'informations, voir la déclaration de conformité ci-dessus / (IT) Questo dispositivo MikroTik è conforme ai limiti massimi di potenza di trasmissione WLAN e LTE in conformità con le normative ETSI. Per ulteriori informazioni, consultare la dichiarazione di conformità sopra / (ES) Este dispositivo MikroTik cumple con los límites máximos de potencia de transmisión WLAN y LTE de acuerdo con las regulaciones ETSI. Para obtener más información, consulte la declaración de conformidad anterior / (RU) Это устройство MikroTik соответствует максимальным пределам мощности передачи WLAN и LTE в соответствии с правилами ETSI. Для получения дополнительной информации см. Декларацию соответствия выше.

Bluetooth Qualified Product

This product has successfully completed Bluetooth Qualification Process. For more information on Bluetooth Qualified products please use the following link: https://launchstudio.bluetooth.com/Listings/Search

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Варианты входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Cuurent, A

DC Jack (12-57 V DC) PoE In Ethernet Port (18-57 V DC) MIcroUSB 5V Port (5 V DC)
24
1.2
IP20
±0°..+40°C

\#63206
