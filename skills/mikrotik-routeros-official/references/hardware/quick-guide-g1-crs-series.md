# Quick Guide G1 CRS series

> Models: CRS326-24G-2S+RM, CRS326-24G-2S+IN, CRS309-1G-8S+IN, CRS125-24G-1S-IN, CRS212-1G-10S-1S+IN, CRS305-1G-4S+IN

**Models: CRS326-24G-2S+RM, CRS326-24G-2S+IN, CRS309-1G-8S+IN, CRS125-24G-1S-IN, CRS212-1G-10S-1S+IN, CRS305-1G-4S+IN**

![](./img/mt_logo_arrow_v2-02-52.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to v7.10 or the latest software version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
:::

*This is a network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, Full EU Declaration of Conformity, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most relevant technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-59.png)

**First steps:**

- Connect with your computer to the device;
- Connect the device to a power source;
- Use WebFig in a web browser or the "WinBox" configuration tool [https://mt.lv/winbox](https://mt.lv/winbox); **multiple configuration methods are available to ensure accessibility**;
- Start configuration within the chosen tool, using the default IP address 192.168.88.1. If the IP address is unavailable, use Winbox and choose the "Neighbors" tab to find the device;
- Proceed to connect using the MAC address. The username is "admin", and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the WebFig or WinBox "Files" menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- Set up your router password.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product is intended to be installed indoors. Keep this product away from water, fire, humidity, or hot environments.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures.
Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до най-новата версия v7.10 на софтуера, за да се гарантира спазването на местните наредби!
Крайните потребители са отговорни за спазването на местните разпоредби. Всички устройства на MikroTik трябва да бъдат инсталирани професионално.
:::

*Това е мрежово устройство. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, пълна ЕС декларация за съответствие, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-57.png)

**Първи стъпки:**

- Свържете се с вашия компютър към устройството;
- Свържете устройството към източник на захранване;
- Използвайте WebFig в уеб браузър или конфигурационния инструмент "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **налични са множество методи за конфигуриране, за да се осигури достъпност**;
- Начнете конфигурацията с избран инструмент, използвайки стандартния IP адрес 192.168.88.1. Ако IP адресът не е достъпен, използвайте Winbox и изберете раздела "Neighbors", за да намерите устройството;
- Продължете да се свързвате чрез MAC адреса. Потребителското име е "admin", и няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- Кликнете на бутона "Check for updates" и актуализирайте RouterOS до последната версия;
- За ръчно обновяване на устройството посетете mikrotik.com, изберете модела си и намерете необходимите пакети в секцията "Downloads";
- Качете изтеглените пакети в менюто "Files" на WebFig или WinBox и рестартирайте устройството;
- Чрез актуализиране на софтуера на вашия RouterOS до последната версия, можете да гарантирате оптимална производителност, стабилност и актуализации за сигурност;
- Задайте парола за вашия рутер.

**Информация за безопасност:**

- Преди да работите с каквото и да е оборудване на MikroTik, бъдете наясно с опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и концепции.
- Използвайте само захранването и аксесоарите, одобрени от производителя и които могат да бъдат намерени в оригиналната опаковка на този продукт.
- Това оборудване трябва да бъде инсталирано от обучен и квалифициран персонал, съгласно тези инструкции за монтаж. Инсталаторът е отговорен да гарантира, че инсталирането на оборудването е в съответствие с местните и националните електрически кодекси. Не се опитвайте да разглобявате, поправяте или модифицирате устройството.
- Този продукт е предназначен за инсталиране на закрито. Пазете този продукт далеч от вода, огън, влажност или гореща среда.
- Не можем да гарантираме, че няма да възникнат инциденти или щети поради неправилна употреба на устройството. Моля, използвайте този продукт внимателно и работете на свой собствен риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най -бързият начин да направите това е като извадите щепсела от контакта.
- Това е продукт от клас А. В домашна среда този продукт може да причини радиосмущения, в този случай от потребителя може да се наложи да предприеме адекватни мерки.
Производител: Mikrotikls SIA, Unijas iela 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Aby bylo zajištěno dodržování předpisů místních úřadů, musí být toto zařízení upgradováno na nejnovější verzi softwaru v7.10!
Je odpovědností koncových uživatelů dodržovat místní předpisy. Všechna zařízení MikroTik musí být profesionálně nainstalována.
:::

*Toto je síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto rychlého průvodce.*
*Technické specifikace, úplné EU prohlášení o shodě, brožury a další informace o produktech na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-57.png)

**První kroky:**

- Připojte se k počítači k počítači;
- Připojte zařízení ke zdroji napájení;
- Použijte WebFig v webovém prohlížeči nebo konfigurační nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **je k dispozici více konfiguračních metod k zajištění přístupnosti;**
- Zahajte konfiguraci ve zvoleném nástroji s výchozí IP adresou 192.168.88.1. Pokud není IP adresa k dispozici, použijte Winbox a vyberte kartu "Neighbors", abyste zařízení našli;
- Pokračujte v připojení pomocí MAC adresy. Uživatelské jméno je "admin", a není žádné heslo (nebo, pro některé modely, zkontrolujte uživatelská a bezdrátová hesla na štítku);
- Klepněte na tlačítko "Check for updates" a aktualizujte RouterOS na nejnovější verzi;
- Pro manuální aktualizaci zařízení navštivte mikrotik.com, vyberte svůj model a najděte požadované balíčky v sekci "Downloads";
- Nahrajte stažené balíčky do menu "Files" ve WebFig nebo WinBox a restartujte zařízení;
- Aktualizací softwaru RouterOS na nejnovější verzi můžete zajistit optimální výkon, stabilitu a aktualizace zabezpečení;
- Nastavte heslo pro váš router.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro předcházení nehodám. Instalační technik by měl znát síťové struktury, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které lze nalézt v originálním balení tohoto produktu.
- Toto zařízení má být instalováno vyškoleným a kvalifikovaným personálem podle těchto instalačních pokynů. Instalační technik odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat nebo upravovat.
- Tento výrobek je určen k instalaci uvnitř. Chraňte tento produkt před vodou, ohněm, vlhkostí nebo horkým prostředím.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo škodám. Používejte prosím tento produkt opatrně a provozujte na vlastní nebezpečí!
- V případě poruchy zařízení jej odpojte od napájení. Nejrychlejším způsobem je vytáhnout zástrčku ze zásuvky.
- Toto je výrobek třídy A. V domácím prostředí může tento výrobek způsobovat rušení rádiových vln. V takovém případě může být uživatel povinen přijmout odpovídající opatření.
Výrobce: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til den nyeste softwareversion v7.10 for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landes regler. Alle MikroTik-enheder skal være professionelt installeret.
:::

*Dette er netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, fuld EU-overensstemmelseserklæring, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-57.png)

**Første trin:**

- Opret forbindelse med din computer til enheden;
- Tilslut enheden til en strømkilde;
- Brug WebFig i en webbrowser eller konfigurationsværktøjet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurationsmetoder er tilgængelige for at sikre tilgængelighed;**
- Start konfigurationen inden for det valgte værktøj ved hjælp af standard IP-adressen 192.168.88.1. Hvis IP-adressen ikke er tilgængelig, skal du bruge Winbox og vælge fanen "Neighbors" for at finde enheden;
- Fortsæt med at oprette forbindelse ved at bruge MAC-adressen. Brugernavnet er "admin", og der er ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløse adgangskoder på klistermærket);
- Klik på knappen "Check for updates" og opdater RouterOS til den nyeste version;
- For manuel opdatering af enheden, besøg mikrotik.com, vælg din model og find de nødvendige pakker i sektionen "Downloads";
- Upload downloadede pakker til WebFig eller WinBox "Files" menu og genstart enheden;
- Ved at opgradere din RouterOS-software til den nyeste version kan du sikre optimal ydeevne, stabilitet og sikkerhedsopdateringer;
- Indstil din routeradgangskode.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt er beregnet til at blive installeret indendørs. Hold dette produkt væk fra vand, ild, fugtighed eller varme omgivelser.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
- Dette er et klasse A-produkt. I et hjemligt miljø kan dette produkt forårsage radiointerferens, i hvilket tilfælde brugeren muligvis skal træffe passende foranstaltninger
Producent: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf die neueste Softwareversion v7.10 aktualisiert werden, um die Einhaltung der örtlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen. Alle MikroTik-Geräte müssen professionell installiert werden.
:::

*Dies ist das Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Daten, vollständige EU-Konformitätserklärung, Broschüren und weitere Informationen zu Produkten unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-57.png)

**Erste Schritte:**

- Stellen Sie mit Ihrem Computer eine Verbindung zum Gerät her;
- Schließen Sie das Gerät an eine Stromquelle an;
- Verwenden Sie WebFig in einem Webbrowser oder das Konfigurationstool "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **mehrere Konfigurationsmethoden stehen zur Verfügung, um die Barrierefreiheit sicherzustellen;**
- Starten Sie die Konfiguration im gewählten Tool mit der Standard-IP-Adresse 192.168.88.1. Wenn die IP-Adresse nicht verfügbar ist, verwenden Sie Winbox und wählen Sie die Registerkarte "Neighbors", um das Gerät zu finden;
- Fahren Sie fort, sich über die MAC-Adresse zu verbinden. Der Benutzername lautet "admin", und es gibt kein Passwort (oder, für einige Modelle, überprüfen Sie Benutzer- und drahtlose Passwörter auf dem Aufkleber);
- Klicken Sie auf die Schaltfläche "Check for updates" und aktualisieren Sie RouterOS auf die neueste Version;
- Für ein manuelles Update des Geräts besuchen Sie mikrotik.com, wählen Ihr Modell aus und finden die erforderlichen Pakete im Abschnitt "Downloads";
- Laden Sie die heruntergeladenen Pakete in das WebFig- oder WinBox-Menü "Files" hoch und starten Sie das Gerät neu;
- Durch Aktualisieren Ihrer RouterOS-Software auf die neueste Version können Sie optimale Leistung, Stabilität und Sicherheitsupdates gewährleisten;
- Legen Sie Ihr Router-Passwort fest.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, seien Sie sich der Gefahren im Zusammenhang mit elektrischen Schaltkreisen bewusst und machen Sie sich mit den Standardverfahren zur Unfallverhütung vertraut. Der Installateur sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur vom Hersteller zugelassene Netzteile und Zubehörteile, die sich in der Originalverpackung dieses Produkts befinden.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß dieser Installationsanleitung installiert werden. Der Installateur ist dafür verantwortlich sicherzustellen, dass die Installation des Geräts den lokalen und nationalen Elektrovorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt ist für die Installation in Innenräumen vorgesehen. Halten Sie dieses Produkt von Wasser, Feuer, Feuchtigkeit oder heißen Umgebungen fern.
- Wir können nicht garantieren, dass durch unsachgemäßen Gebrauch des Gerätes keine Unfälle oder Schäden entstehen. Bitte verwenden Sie dieses Produkt mit Sorgfalt und auf eigene Gefahr!
- Bei einem Geräteausfall trennen Sie es bitte vom Strom. Am schnellsten geht das, indem Sie den Netzstecker aus der Steckdose ziehen.
- Dies ist ein Produkt der Klasse A. In einer häuslichen Umgebung kann dieses Produkt Funkstörungen verursachen. In diesem Fall muss der Benutzer möglicherweise angemessene Maßnahmen ergreifen.
Hersteller: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στην πιο πρόσφατη έκδοση λογισμικού v7.10 για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών. Όλες οι συσκευές MikroTik πρέπει να εγκατασταθούν επαγγελματικά.
:::

*Αυτή είναι η συσκευή δικτύου*. *Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, φυλλάδια και περισσότερες πληροφορίες για τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-57.png)

**Πρώτα βήματα:**

- Συνδεθείτε με τον υπολογιστή σας στη συσκευή;
- Συνδέστε τη συσκευή σε πηγή ενέργειας;
- Χρησιμοποιήστε το WebFig σε ένα πρόγραμμα περιήγησης ή το εργαλείο ρύθμισης ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **διατίθενται πολλαπλές μέθοδοι ρύθμισης για να διασφαλιστεί η προσβασιμότητα;**
- Ξεκινήστε τη διαμόρφωση μέσα από το επιλεγμένο εργαλείο, χρησιμοποιώντας την προεπιλεγμένη διεύθυνση IP 192.168.88.1. Αν η διεύθυνση IP δεν είναι διαθέσιμη, χρησιμοποιήστε το Winbox και επιλέξτε την καρτέλα "Neighbors" για να βρείτε τη συσκευή;
- Συνεχίστε να συνδέεστε χρησιμοποιώντας τη διεύθυνση MAC. Το όνομα χρήστη είναι "admin", και δεν υπάρχει κωδικός (ή, για κάποια μοντέλα, ελέγξτε τους κωδικούς χρήστη και ασύρματους στο αυτοκόλλητο);
- Κάντε κλικ στο κουμπί "Check for updates" και ενημερώστε το RouterOS στην τελευταία έκδοση;
- Για χειροκίνητη ενημέρωση της συσκευής, επισκεφθείτε το mikrotik.com, επιλέξτε το μοντέλο σας και εντοπίστε τα απαιτούμενα πακέτα στην ενότητα "Downloads";
- Μεταφορτώστε τα κατεβασμένα πακέτα στο μενού "Files" του WebFig ή του WinBox και επανεκκινήστε τη συσκευή;
- Με την αναβάθμιση του λογισμικού RouterOS στην τελευταία έκδοση, μπορείτε να διασφαλίσετε βέλτιστη απόδοση, σταθερότητα και ενημερώσεις ασφαλείας;
- Ορίστε τον κωδικό πρόσβασης για τον router σας.

**Οδηγίες ασφαλείας:**

- Πριν εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, λάβετε υπόψη τους κινδύνους που συνδέονται με τα ηλεκτρικά κυκλώματα και εξοικειωθείτε με τις τυπικές πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιείτε μόνο το τροφοδοτικό και τα αξεσουάρ που έχουν εγκριθεί από τον κατασκευαστή και τα οποία βρίσκονται στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και εξειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για να βεβαιωθεί ότι η εγκατάσταση του εξοπλισμού συμμορφώνεται με τους τοπικούς και εθνικούς ηλεκτρικούς κωδικούς. Μην επιχειρήσετε να αποσυναρμολογήσετε, επισκευάσετε ή τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν προορίζεται για εγκατάσταση σε εσωτερικούς χώρους. Κρατήστε αυτό το προϊόν μακριά από νερό, φωτιά, υγρασία ή ζεστό περιβάλλον.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές λόγω ακατάλληλης χρήσης της συσκευής. Χρησιμοποιήστε αυτό το προϊόν με προσοχή και λειτουργήστε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από το ρεύμα. Ο γρηγορότερος τρόπος για να γίνει αυτό είναι να αποσυνδέσετε το φις από την πρίζα.
- Αυτό είναι ένα προϊόν κατηγορίας Α. Σε οικιακό περιβάλλον, αυτό το προϊόν ενδέχεται να προκαλέσει ραδιοφωνικές παρεμβολές, οπότε ενδέχεται να απαιτείται από τον χρήστη να λάβει τα κατάλληλα μέτρα.
Κατασκευαστής: Mikrotikls SIA, Unijas iela 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a la última versión de software v7.10 para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país. Todos los dispositivos MikroTik deben instalarse profesionalmente.
:::

*Este es un dispositivo de red. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, Declaración de conformidad de la UE completa, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-58.png)

**Primeros pasos:**

- Conéctese con su computadora al dispositivo;
- Conecte el dispositivo a una fuente de alimentación;
- Utilice WebFig en un navegador web o la herramienta de configuración "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Inicie la configuración dentro de la herramienta seleccionada, utilizando la dirección IP predeterminada 192.168.88.1. Si la dirección IP no está disponible, utilice Winbox y elija la pestaña "Neighbors" para encontrar el dispositivo;
- Proceda a conectarse utilizando la dirección MAC. El nombre de usuario es "admin", y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario e inalámbricas en la etiqueta);
- Haga clic en el botón "Check for updates" y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Sube los paquetes descargados al menú "Files" de WebFig o WinBox y reinicia el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento, estabilidad y actualizaciones de seguridad óptimos;
- Configure la contraseña de su enrutador.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los peligros relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras, los términos y los conceptos de la red.
- Utilice únicamente la fuente de alimentación y los accesorios aprobados por el fabricante y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, de acuerdo con estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto está diseñado para ser instalado en interiores. Mantenga este producto alejado del agua, el fuego, la humedad o los entornos calientes.
- No podemos garantizar que no ocurran accidentes o daños debido al uso inadecuado del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el enchufe de la toma de corriente.
- Este es un producto de Clase A. En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso es posible que el usuario deba tomar las medidas adecuadas.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

**Información México:**

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## ET - Eestlane. Kiirjuhend

:::warning
Kohalike omavalitsuste eeskirjade järgimise tagamiseks tuleb see seade värskendada uusimale tarkvaraversioonile v7.10!
Lõppkasutajate kohustus on järgida kohaliku riigi seadusi. Kõik MikroTik seadmed peavad olema professionaalselt installitud.
:::

*See on võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised andmed, täielik EL-i vastavusdeklaratsioon, brošüürid ja lisateave toodete kohta aadressil [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-57.png)

**Esimesed sammud:**

- Ühendage arvutiga seadmega;
- Ühendage seade toiteallikaga;
- Kasutage WebFigi veebi­brauseris või seadistus­tööriista "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **ligipääsetavuse tagamiseks on saadaval mitu seadistamismeetodit;**
- Alustage konfiguratsiooni valitud tööriista abil, kasutades vaikimisi IP-aadressi 192.168.88.1. Kui IP-aadress pole saadaval, kasutage Winboxi ja valige seade leidmiseks vahekaart "Neighbors";
- Jätkake ühendumist MAC-aadressi kasutades. Kasutajanimi on "admin" ja parooli pole (või mõne mudeli puhul kontrollige kasutaja ja traadita paroole kleebisel);
- Klõpsake nupul "Check for updates" ja ajakohastage RouterOS viimasele versioonile;
- Seadme käsitsi uuendamiseks külastage mikrotik.com, valige oma mudel ja leidke vajalikud paketid jaotises "Downloads";
- Lae allalaaditud paketid üles veebibrauseri WebFig või WinBox "Files" menüüsse ja taaskäivita seade;
- Värskendades oma RouterOS tarkvara viimasele versioonile, saate tagada optimaalse jõudluse, stabiilsuse ja turvavärskendused;
- Seadke oma ruuteri parool.

**Ohutusteave:**

- Enne mis tahes MikroTik seadmetega töötamist olge teadlik elektriskeemidega seotud ohtudest ja tutvuge õnnetuste vältimise tavapraktikaga. Paigaldaja peaks olema kursis võrgustruktuuride, terminite ja kontseptsioonidega.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Seda seadet peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevale paigaldusjuhendile. Paigaldaja vastutab selle eest, et seadme paigaldamine vastaks kohalikele ja riiklikele elektrikoodeksitele. Ärge proovige seadet lahti võtta, parandada ega muuta.
- See toode on ette nähtud paigaldamiseks siseruumidesse. Hoidke seda toodet eemal veest, tulest, niiskusest või kuumast keskkonnast.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Palun kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral ühendage see vooluvõrgust lahti. Kiireim viis selleks on toitepistik pistikupesast välja tõmmata.
- See on A -klassi toode. Koduses keskkonnas võib see toode põhjustada raadiohäireid, mille korral võib kasutaja nõuda piisavate meetmete võtmist.
Tootja: Mikrotikls SIA, Unijas iela 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä uusimpaan ohjelmistoversioon v7.10, jotta voidaan varmistaa paikallisten viranomaisten määräysten noudattaminen!
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja. Kaikki MikroTik-laitteet on asennettava ammattimaisesti.
:::

*Tämä on verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, täydellinen EU-vaatimustenmukaisuusvakuutus, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-57.png)

**Ensiaskeleet:**

- Yhdistä tietokoneesi laitteeseen;
- Kytke laite virtalähteeseen;
- Käytä WebFi­giä web-selaimessa tai konfigurointityökalua "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **useita määritysmenetelmiä on saatavilla saavutettavuuden varmistamiseksi;**
- Aloita konfigurointi valitussa työkalussa käyttäen oletus-IP-osoitetta 192.168.88.1. Jos IP-osoite ei ole saatavilla, käytä Winboxia ja valitse "Neighbors"-välilehti laitteen löytämiseksi;
- Jatka yhteyden muodostamista MAC-osoitteen avulla. Käyttäjänimi on "admin", eikä salasanaa ole (tai joissakin malleissa tarkista käyttäjä- ja langattomat salasanat tarraan);
- Napsauta "Check for updates" -painiketta ja päivitä RouterOS uusimpaan versioon;
- Laitteen manuaalista päivitystä varten siirry osoitteeseen mikrotik.com, valitse mallisi ja etsi tarvittavat paketit osiossa "Downloads";
- Lataa ladatut paketit WebFigin tai WinBoxin "Files" -valikkoon ja käynnistä laite uudelleen;
- Päivittämällä RouterOS-ohjelmistosi uusimpaan versioon voit varmistaa optimaalisen suorituskyvyn, vakauden ja turvapäivitykset;
- Aseta reitittimen salasana.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik -laitteiden parissa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja tutustu tavanomaisiin käytäntöihin onnettomuuksien ehkäisemiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäisestä pakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilökunta näiden asennusohjeiden mukaisesti. Asentaja on vastuussa siitä, että laitteen asennus on paikallisten ja kansallisten sähkökoodien mukainen. Älä yritä purkaa, korjata tai muuttaa laitetta.
- Tämä tuote on tarkoitettu asennettavaksi sisätiloihin. Pidä tämä tuote poissa vedestä, tulesta, kosteudesta tai kuumasta ympäristöstä.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta varoen ja toimi omalla vastuullasi!
- Jos laite vioittuu, irrota se virtalähteestä. Nopein tapa tehdä se on irrottaa pistoke pistorasiasta.
- Tämä on luokan A tuote. Kotitalousympäristössä tämä tuote voi aiheuttaa radiohäiriöitä, jolloin käyttäjää voidaan joutua ryhtymään tarvittaviin toimenpiteisiin.
Valmistaja: Mikrotikls SIA, Unijas iela 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers la dernière version v7.10 du logiciel pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays. Tous les appareils MikroTik doivent être installés par des professionnels.
:::

*Ceci est un périphérique réseau. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, déclaration de conformité UE complète, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-57.png)

**Premiers pas:**

- Connectez-vous avec votre ordinateur à l'appareil;
- Connectez l'appareil à une source d'alimentation;
- Utilisez WebFig dans un navigateur web ou l’outil de configuration "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **plusieurs méthodes de configuration sont disponibles pour garantir l’accessibilité;**
- Démarrez la configuration dans l'outil choisi en utilisant l'adresse IP par défaut 192.168.88.1. Si l'adresse IP n'est pas disponible, utilisez Winbox et choisissez l'onglet "Neighbors" pour trouver le périphérique;
- Procédez à la connexion en utilisant l'adresse MAC. Le nom d'utilisateur est "admin", et il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Cliquez sur le bouton "Check for updates" et mettez à jour RouterOS vers la dernière version;
- Pour une mise à jour manuelle de l'appareil, rendez-vous sur mikrotik.com, sélectionnez votre modèle et localisez les paquets requis dans la section "Downloads";
- Téléchargez les packages téléchargés dans le menu "Files" de WebFig ou WinBox et redémarrez l'appareil;
- En mettant à jour votre logiciel RouterOS vers la dernière version, vous pouvez garantir des performances optimales, la stabilité et les mises à jour de sécurité;
- Configurez le mot de passe de votre routeur.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard pour prévenir les accidents. L'installateur doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement le bloc d'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit est destiné à être installé à l'intérieur. Gardez ce produit loin de l'eau, du feu, de l'humidité ou des environnements chauds.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec précaution et opérer à vos risques et périls!
- En cas de panne de l'appareil, veuillez le débrancher de l'alimentation. Le moyen le plus rapide de le faire est de débrancher la fiche d'alimentation de la prise de courant.
- Il s'agit d'un produit de classe A. Dans un environnement domestique, ce produit peut provoquer des interférences radio, auquel cas l'utilisateur peut être amené à prendre des mesures adéquates.
Fabricant: Mikrotikls SIA, Unijas iela 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj je uređaj potrebno nadograditi na najnoviju verziju softvera v7.10 kako bi se osigurala sukladnost s lokalnim propisima!
Odgovornost krajnjih korisnika je da slijede lokalne propise. Svi MikroTik uređaji moraju biti profesionalno instalirani.
:::

*Ovo je mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, puna EU izjava o sukladnosti, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-57.png)

**Prvi koraci:**

- Povežite se s računalom na uređaj;
- Priključite uređaj na izvor napajanja;
- Koristite WebFig u web-pregledniku ili konfiguracijski alat "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **dostupne su različite metode konfiguracije kako bi se osigurala pristupačnost;**
- Pokrenite konfiguraciju unutar odabranog alata, koristeći zadanu IP adresu 192.168.88.1. Ako IP adresa nije dostupna, koristite Winbox i odaberite karticu "Neighbors" da biste pronašli uređaj;
- Nastavite s povezivanjem putem MAC adrese. Korisničko ime je "admin", a nema lozinke (ili, za neke modele, provjerite korisničke i bežične lozinke na naljepnici);
- Kliknite na gumb "Check for updates" i ažurirajte RouterOS na najnoviju verziju;
- Za ručnu nadogradnju uređaja posjetite mikrotik.com, odaberite svoj model i pronađite potrebne pakete u odjeljku "Downloads";
- Prenesite preuzete pakete u WebFig ili WinBox "Files" izbornik i ponovno pokrenite uređaj;
- Ažuriranjem softvera RouterOS na najnoviju verziju možete osigurati optimalne performanse, stabilnost i sigurnosna ažuriranja;
- Postavite lozinku za vaš usmjerivač.

**Sigurnosne informacije:**

- Prije rada na bilo kojoj MikroTik opremi, budite svjesni opasnosti povezanih s električnim krugovima i upoznajte se sa standardnom praksom za sprječavanje nesreća. Instalacijski program trebao bi poznavati mrežne strukture, pojmove i koncepte.
- Koristite samo izvor napajanja i dodatnu opremu odobrene od proizvođača, koji se mogu pronaći u originalnom pakiranju ovog proizvoda.
- Ovu opremu mora instalirati obučeno i kvalificirano osoblje, u skladu s ovim uputama za ugradnju. Instalater je odgovoran za to da instalacija opreme bude u skladu s lokalnim i nacionalnim električnim kodovima. Ne pokušavajte rastaviti, popraviti ili preinačiti uređaj.
- Ovaj je proizvod namijenjen za ugradnju u zatvorene prostore. Držite ovaj proizvod dalje od vode, vatre, vlage ili vrućeg okruženja.
- Ne možemo jamčiti da neće doći do nesreća ili oštećenja zbog nepravilne uporabe uređaja. Pažljivo koristite ovaj proizvod i radite na vlastitu odgovornost!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanje utikača iz utičnice.
- Ovo je proizvod klase A. U kućnom okruženju ovaj proizvod može uzrokovati radio smetnje, u tom slučaju od korisnika se može zahtijevati da poduzme odgovarajuće mjere.
Proizvođač: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt a készüléket a legfrissebb szoftververzióra v7.10 kell frissíteni a helyi hatóságok előírásainak való megfelelés biztosítása érdekében!
A végfelhasználók felelőssége a helyi országos előírások betartása. Az összes MikroTik eszközt szakszerűen telepíteni kell.
:::

*Ez hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki adatok, teljes EU-megfelelőségi nyilatkozat, prospektusok és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products) oldalon*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-57.png)

**Első lépések:**

- Csatlakoztassa számítógépét a készülékhez;
- Csatlakoztassa a készüléket az áramforráshoz;
- Használja a WebFig-et webböngészőben vagy a "WinBox” konfigurációs eszközt [https://mt.lv/winbox](https://mt.lv/winbox); **számos konfigurációs módszer áll rendelkezésre az akadálymentesség biztosításához;**
- Indítsa el a konfigurációt az választott eszközön, az alapértelmezett 192.168.88.1 IP-cím használatával. Ha az IP-cím nem érhető el, használja a Winboxot, és válassza ki a "Neighbors" lapot az eszköz megtalálásához;
- Folytassa a kapcsolatot a MAC cím használatával. A felhasználónév "admin", és nincs jelszó (vagy néhány modell esetén ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Kattintson a "Check for updates" gombra, és frissítse a RouterOS-t a legújabb verzióra;
- Az eszköz kézi frissítéséhez látogasson el a mikrotik.com oldalra, válassza ki a modelljét, és találja meg a szükséges csomagokat a "Downloads" részben;
- Töltse fel a letöltött csomagokat a WebFig vagy WinBox "Files" menübe, majd indítsa újra az eszközt;
- Az RouterOS szoftver frissítésével a legújabb verzióra biztosíthatja az optimális teljesítményt, stabilitást és biztonsági frissítéseket;
- Állítsa be a router jelszavát.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozna, legyen tisztában az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismerje meg a balesetek megelőzésének szokásos gyakorlatát. A telepítőnek ismernie kell a hálózati struktúrákat, kifejezéseket és fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használja, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a berendezést képzett és szakképzett személyzet telepítse, a jelen szerelési utasítás szerint. A szerelő felelős azért, hogy megbizonyosodjon arról, hogy a berendezés telepítése megfelel a helyi és országos elektromos előírásoknak. Ne kísérelje meg szétszerelni, javítani vagy módosítani a készüléket.
- Ezt a terméket beltéri használatra tervezték. Tartsa távol a terméket víztől, tűztől, páratartalomtól vagy forró környezettől.
- Nem tudjuk garantálni, hogy a készülék nem rendeltetésszerű használata miatt baleset vagy sérülés nem következik be. Kérjük, óvatosan használja ezt a terméket, és saját felelősségére használja!
- A készülék meghibásodása esetén válassza le az áramellátást. Ennek leggyorsabb módja, ha kihúzza a hálózati csatlakozót a konnektorból.
- Ez egy A osztályú termék. Háztartási környezetben ez a termék rádióinterferenciát okozhat, ebben az esetben a felhasználónak meg kell tennie a megfelelő intézkedéseket.
Gyártó: Mikrotikls SIA, Unijas iela 2, Riga, Lettország, LV1039.

## ID - Bahasa Indonesia. Panduan cepat

:::warning
Perangkat ini perlu ditingkatkan ke v7.10 atau versi perangkat lunak terbaru untuk memastikan kepatuhan terhadap peraturan otoritas setempat!
Merupakan tanggung jawab pengguna akhir untuk mengikuti peraturan negara setempat. Semua perangkat MikroTik harus diinstal secara profesional.
:::

*Ini adalah Perangkat Jaringan. Anda dapat menemukan nama model produk pada label casing (ID).*
*Kunjungi halaman panduan pengguna di [https://mt.lv/um](https://mt.lv/um) untuk mendapatkan panduan pengguna terbaru dan lengkap. Atau pindai kode QR dengan ponsel Anda.*
*Spesifikasi teknis, Deklarasi Kesesuaian UE selengkapnya, brosur, dan info lebih lanjut tentang produk di [https://mikrotik.com/products](https://mikrotik.com/products)*
*Spesifikasi teknis paling relevan untuk produk ini dapat ditemukan di halaman terakhir Panduan Cepat ini.*
*Panduan konfigurasi untuk software dalam bahasa Anda dan informasi tambahan dapat ditemukan di [https://mt.lv/help](https://mt.lv/help)*
*Perangkat MikroTik ditujukan untuk penggunaan profesional. Jika Anda tidak memiliki kualifikasi silakan mencari konsultan [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/indonesian.badge-21.png)

**Langkah pertama:**

- Hubungkan komputer Anda ke perangkat;
- Hubungkan perangkat ke sumber listrik;
- Gunakan WebFig di peramban web atau alat konfigurasi "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **berbagai metode konfigurasi tersedia untuk memastikan aksesibilitas;**
- Mulai konfigurasi dalam alat yang dipilih, menggunakan alamat IP default 192.168.88.1. Jika alamat IP tidak tersedia, gunakan Winbox dan pilih tab "Neighbors" untuk menemukan perangkat;
- Lanjutkan untuk terhubung menggunakan alamat MAC. Nama penggunanya adalah "admin", dan tidak ada kata sandi (atau, untuk beberapa model, periksa kata sandi pengguna dan nirkabel pada stiker);
- Klik tombol "Check for updates" dan perbarui RouterOS ke versi terbaru;
- Untuk pembaruan manual perangkat, kunjungi mikrotik.com, pilih model Anda, dan temukan paket yang diperlukan di bagian "Downloads";
- Unggah paket yang diunduh ke menu "File" Winbox dan reboot perangkat;
- Dengan mengupgrade perangkat lunak RouterOS Anda ke versi terbaru, Anda dapat memastikan kinerja, stabilitas, dan pembaruan keamanan yang optimal;
- Siapkan kata sandi router Anda.

**Informasi keselamatan:**

- Sebelum Anda mengerjakan peralatan MikroTik apa pun, waspadai bahaya yang terkait dengan sirkuit listrik, dan pahami praktik standar untuk mencegah kecelakaan. Pemasang harus memahami struktur, istilah, dan konsep jaringan.
- Gunakan hanya catu daya dan aksesori yang disetujui oleh produsen, yang dapat ditemukan dalam kemasan asli produk ini.
- Peralatan ini harus dipasang oleh personel yang terlatih dan berkualifikasi, sesuai petunjuk pemasangan ini. Pemasang bertanggung jawab untuk memastikan bahwa Pemasangan peralatan mematuhi peraturan kelistrikan lokal dan nasional. Jangan mencoba membongkar, memperbaiki, atau memodifikasi perangkat.
- Produk ini dimaksudkan untuk dipasang di dalam ruangan. Jauhkan produk ini dari air, api, kelembapan, atau lingkungan panas.
- Kami tidak dapat menjamin bahwa tidak akan terjadi kecelakaan atau kerusakan akibat penggunaan perangkat yang tidak tepat. Harap gunakan produk ini dengan hati-hati dan pengoperasian dengan risiko Anda sendiri!
- Jika terjadi kegagalan perangkat, harap putuskan sambungannya dari listrik. Cara tercepat untuk melakukannya adalah dengan mencabut steker listrik dari stopkontak.
- Ini adalah produk Kelas A. Di lingkungan rumah tangga, produk ini dapat menyebabkan interferensi radio sehingga pengguna mungkin perlu mengambil tindakan yang memadai
Pabrikan: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato all'ultima versione del software v7.10 per garantire la conformità alle normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative locali locali. Tutti i dispositivi MikroTik devono essere installati in modo professionale.
:::

*Questo è il dispositivo di rete. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, dichiarazione di conformità UE completa, brochure e ulteriori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-57.png)

**Primi passi:**

- Connettiti con il tuo computer al dispositivo;
- Collegare il dispositivo a una fonte di alimentazione;
- Utilizzare WebFig in un browser web oppure lo strumento di configurazione "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **sono disponibili diversi metodi di configurazione per garantire l’accessibilità;**
- Inizia la configurazione all'interno dello strumento scelto, utilizzando l'indirizzo IP predefinito 192.168.88.1. Se l'indirizzo IP non è disponibile, utilizza Winbox e scegli la scheda "Neighbors" per trovare il dispositivo;
- Prosegui per connetterti utilizzando l'indirizzo MAC. Il nome utente è "admin", e non c'è alcuna password (o, per alcuni modelli, controlla le password dell'utente e wireless sull'etichetta);
- Fai clic sul pulsante "Check for updates" e aggiorna RouterOS all'ultima versione;
- Per aggiornare manualmente il dispositivo, visitare mikrotik.com, selezionare il modello e individuare i pacchetti necessari nella sezione "Downloads";
- Carica i pacchetti scaricati nel menu "Files" di WebFig o WinBox e riavvia il dispositivo;
- Aggiornando il software RouterOS alla versione più recente, puoi garantire prestazioni ottimali, stabilità e aggiornamenti di sicurezza;
- Imposta la password del tuo router.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, sii consapevole dei rischi legati ai circuiti elettrici e acquisisci familiarità con le pratiche standard per prevenire gli incidenti. L'installatore deve avere familiarità con le strutture, i termini e i concetti di rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme alle normative elettriche locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto è destinato all'installazione in interni. Tenere questo prodotto lontano da acqua, fuoco, umidità o ambienti caldi.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Si prega di utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più veloce per farlo è scollegare la spina di alimentazione dalla presa di corrente.
- Questo è un prodotto di classe A. In un ambiente domestico, questo prodotto potrebbe causare interferenze radio, nel qual caso l'utente potrebbe essere tenuto ad adottare misure adeguate.
Produttore: Mikrotikls SIA, Unijas iela 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Það þarf að uppfæra þetta tæki í nýjustu hugbúnaðarútgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga v7.10!
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum. Öll MikroTik tæki verða að vera sett upp á fagmennsku.
:::

*Þetta er net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tækniforskriftir, full ESB-samræmisyfirlýsing, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-57.png)

**Fyrstu skrefin:**

- Tengdu tölvuna þína við tækið;
- Tengdu tækið við aflgjafa;
- Notið WebFig í vefvafra eða uppsetningartól "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **margar stillingaraðferðir eru í boði til að tryggja aðgengi;**
- Byrjaðu uppsetningu innan valins tóls með sjálfgefinni IP-tölu 192.168.88.1. Ef IP-talan er ekki tiltæk, nottu Winbox og veldu "Neighbors" flipann til að finna tækið;
- Halda áfram að tengjast með því að nota MAC-tölu. Notendanafnið er "admin" og engin lykilorð (eða, í sumum gerðum, athugaðu notenda- og þráðlaus lykilorð á klisterinu);
- Smelltu á "Check for updates" hnappinn og uppfærðu RouterOS á nýjustu útgáfu;
- Til að uppfæra tækið handvirkt, farðu á mikrotik.com, veldu módelið þitt og finndu nauðsynlegu pakkana í kaflanum "Downloads";
- Hlaða niður pökkum á WebFig eða WinBox "Files" valmynd og endurræsa tækið;
- Með því að uppfæra hugbúnaðinn á RouterOS í nýjustu útgáfu getur þú tryggjað bestu mögulegu afköst, stöðugleika og öryggisuppfærslur;
- Stilla lykilorðið á routerinn þína.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði skaltu vera meðvitaður um hættuna sem fylgir rafrásum og þekkja staðlaða vinnubrögð við að koma í veg fyrir slys. Uppsetningarforritið ætti að þekkja netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og finnast í upprunalegum umbúðum þessarar vöru.
- Þessi búnaður á að setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðili ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundna og innlenda rafmagnsreglur. Ekki reyna að taka í sundur, gera við eða breyta tækinu.
- Þessari vöru er ætlað að setja upp innandyra. Hafðu þessa vöru fjarri vatni, eldi, raka eða heitu umhverfi.
- Við getum ekki ábyrgst að engin slys eða skemmdir verða vegna rangrar notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og farðu á eigin ábyrgð!
- Ef tækið bilar skaltu aftengja það frá rafmagni. Fljótlegasta leiðin til að gera það er með því að taka rafmagnstengið úr sambandi við rafmagnsinnstunguna.
- Þetta er vara í flokki A. Í heimalandi umhverfi gæti þessi vara valdið truflunum á útvarpi, en þá gæti þurft að gera notandann viðeigandi ráðstafanir.
Framleiðandi: Mikrotikls SIA, Unijas iela 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til den nyeste programvareversjonen v7.10 for å sikre samsvar med lokale myndighetsbestemmelser!
Det er sluttbrukernes ansvar å følge lokale lands forskrifter. Alle MikroTik-enheter må være profesjonelt installert.
:::

*Dette er nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, full EU-samsvarserklæring, brosjyrer og mer informasjon om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-57.png)

**Første steg:**

- Koble datamaskinen til enheten.
- Koble enheten til en strømkilde;
- Bruk WebFig i en nettleser eller konfigurasjonsverktøyet "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flere konfigurasjonsmetoder er tilgjengelige for å sikre tilgjengelighet;**
- Start konfigurasjonen innenfor det valgte verktøyet ved hjelp av standard IP-adresse 192.168.88.1. Hvis IP-adressen ikke er tilgjengelig, bruk Winbox og velg fanen "Neighbors" for å finne enheten;
- Fortsett å koble til ved å bruke MAC-adressen. Brukernavnet er "admin", og det er ingen passord (eller, for noen modeller, sjekk bruker- og trådløse passord på etiketten);
- Klikk på knappen "Check for updates" og oppdater RouterOS til den nyeste versjonen;
- For manuell oppdatering av enheten, gå til mikrotik.com, velg modellen din og finn de nødvendige pakkene i seksjonen "Downloads";
- Last opp nedlastede pakker til WebFig eller WinBox "Files"-menyen og start enheten på nytt;
- Ved å oppgradere RouterOS-programvaren til den nyeste versjonen kan du sikre optimal ytelse, stabilitet og sikkerhetsoppdateringer;
- Konfigurer router-passordet ditt.

**Sikkerhetsinformasjon:**

- Før du arbeider med noe MikroTik -utstyr, må du være oppmerksom på farene forbundet med elektriske kretser, og være kjent med standard praksis for å forhindre ulykker. Installatøren bør være kjent med nettverksstrukturer, begreper og begreper.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av opplært og kvalifisert personell i henhold til denne installasjonsinstruksjonene. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske forskrifter. Ikke forsøk å demontere, reparere eller endre enheten.
- Dette produktet er ment å installeres innendørs. Hold dette produktet borte fra vann, brann, fuktighet eller varme omgivelser.
- Vi kan ikke garantere at det ikke vil oppstå ulykker eller skader på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk på egen risiko!
- I tilfelle feil på enheten, må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke støpselet ut av stikkontakten.
- Dette er et klasse A -produkt. I et hjemmemiljø kan dette produktet forårsake radioforstyrrelser. I så fall kan det være nødvendig at brukeren tar nødvendige tiltak.
Produsent: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## LT - Lietuvių. Trumpas vadovas

:::warning
Šį įrenginį reikia atnaujinti į naujausią programinės įrangos versiją v7.10, kad būtų užtikrinta atitiktis vietos valdžios institucijų nuostatoms!
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi. Visi „MikroTik“ įrenginiai turi būti profesionaliai įdiegti.
:::

*Tai yra tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, visa ES atitikties deklaracija, brošiūros ir daugiau informacijos apie gaminius adresu [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-57.png)

**Pirmieji žingsniai:**

- Prijunkite savo kompiuterį prie įrenginio;
- Prijunkite įrenginį prie maitinimo šaltinio;
- Naudokite WebFig naršyklėje arba konfigūravimo įrankį "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **galimi keli konfigūravimo metodai prieinamumui užtikrinti;**
- Pradėkite konfigūraciją pasirinktame įrankyje, naudodami numatytąją IP adresą 192.168.88.1. Jei IP adresas nepasiekiamas, naudokite Winbox ir pasirinkite skirtuką "Neighbors", kad rastumėte įrenginį;
- Tęskite prisijungdami naudodami MAC adresą. Vartotojo vardas yra "admin", ir nėra slaptažodžio (arba, kai kuriems modeliams, patikrinkite vartotojo ir belaidžio slaptažodžius ant lipduko);
- Spustelėkite "Check for updates" mygtuką ir atnaujinkite RouterOS į naujausią versiją;
- Norėdami rankiniu būdu atnaujinti įrenginį, eikite į mikrotik.com, pasirinkite savo modelį ir raskite reikalingus paketus skiltyje "Downloads";
- Įkraukite atsisiųstus paketus į WebFig arba WinBox "Files" meniu ir paleiskite įrenginį iš naujo;
- Atnaujindami RouterOS programinę įrangą iki naujausios versijos, galite užtikrinti optimalų našumą, stabilumą ir saugumo atnaujinimus;
- Nustatykite savo maršrutizatoriaus slaptažodį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kokia „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine nelaimingų atsitikimų prevencijos praktika. Montuotojas turi būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintą maitinimo šaltinį ir priedus, kuriuos rasite originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokytas ir kvalifikuotas personalas pagal šias montavimo instrukcijas. Montuotojas yra atsakingas už tai, kad įrenginio montavimas atitiktų vietinius ir nacionalinius elektros kodeksus. Nemėginkite išardyti, taisyti ar keisti prietaiso.
- Šis gaminys skirtas montuoti patalpose. Laikykite šį gaminį atokiau nuo vandens, ugnies, drėgmės ar karštos aplinkos.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo neįvyks nelaimingų atsitikimų ar žalos. Prašome naudoti šį gaminį atsargiai ir veikti savo rizika!
- Įrenginio gedimo atveju atjunkite jį nuo maitinimo šaltinio. Greičiausias būdas tai padaryti yra ištraukti maitinimo kištuką iš elektros lizdo.
- Tai yra A klasės produktas. Buitinėje aplinkoje šis gaminys gali sukelti radijo trukdžius, todėl vartotojas gali imtis atitinkamų priemonių.
Gamintojas: Mikrotikls SIA, Unijas iela 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šīs ierīces programmatūras versiju ir jāatjaunina uz v7.10, vai jaunāko pieejamo, lai nodrošinātu atbilstību vietējās varas normatīviem!
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus. Visām MikroTik ierīcēm jābūt profesionāli uzstādītām.
:::

*Šī ir tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, pilna ES atbilstības deklarācija, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-57.png)

**Pirmie soļi:**

- Savienojiet ierīci ar datoru;
- Pievienojiet ierīci strāvas avotam;
- Izmantojiet WebFig tīmekļa pārlūkā vai konfigurācijas rīku "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **vairāki konfigurēšanas veidi ir pieejami piekļūstamības nodrošināšanai;**
- Sāciet konfigurēt izvēlētajā rīkā, izmantojot noklusēto IP adresi 192.168.88.1. Ja IP adrese nav pieejama, izmantojiet Winbox un izvēlieties cilni "Neighbors", lai atrastu ierīci;
- Turpiniet savienojumu, izmantojot MAC adresi. Lietotājvārds ir "admin", un nav paroles (vai dažiem modeļiem pārbaudiet lietotāja un bezvadu paroles uz uzlīmes);
- Noklikšķiniet uz pogas "Check for updates" un atjaunojiet RouterOS līdz jaunākajai versijai;
- Lai manuāli atjauninātu ierīci, apmeklējiet mikrotik.com, izvēlieties savu modeli un atrodiet nepieciešamās pakotnes sadaļā "Downloads";
- Augšupielādējiet lejupielādētās pakotnes uz WebFig vai WinBox "Files" izvēlni un pārstartējiet ierīci;
- Jauninot RouterOS programmatūru uz jaunāko versiju, jūs varat nodrošināt optimālu veiktspēju, stabilitāti un drošības atjauninājumus;
- Iestatiet sava maršrutētāja paroli.

**Drošības informācija:**

- Pirms strādājat ar jebkuru MikroTik aprīkojumu, apzinieties ar elektriskās ķēdes radīto apdraudējumu un iepazīstieties ar standarta praksi nelaimes gadījumu novēršanai. Instalētājam jāzina tīkla struktūras, termini un jēdzieni.
- Izmantojiet tikai ražotāja apstiprinātu barošanas avotu un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Šo aprīkojumu drīkst uzstādīt apmācīts un kvalificēts personāls saskaņā ar šīm uzstādīšanas instrukcijām. Uzstādītājs ir atbildīgs par to, lai iekārtas uzstādīšana atbilstu vietējiem un valsts elektriskajiem noteikumiem. Nemēģiniet izjaukt, labot vai pārveidot ierīci.
- Šis produkts ir paredzēts uzstādīšanai telpās. Sargājiet šo produktu no ūdens, uguns, mitruma vai karstas vides.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ nenotiks negadījumi vai bojājumi. Lūdzu, izmantojiet šo produktu piesardzīgi un darbojieties uz savu risku!
- Ierīces bojājuma gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir atvienot strāvas kontaktdakšu no kontaktligzdas.
- Šis ir A klases produkts. Sadzīves vidē šis produkts var izraisīt radio traucējumus, tādā gadījumā lietotājam var būt jāveic atbilstoši pasākumi.
Ražotājs: Mikrotikls SIA, Ūnijas iela 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għall-aħħar verżjoni tas-softwer v7.10 sabiex tiġi żgurata konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż. L-apparati kollha MikroTik għandhom ikunu installati professjonalment.
:::

*Dan huwa apparat tan-netwerk. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, Dikjarazzjoni Sħiħa ta' Konformità tal-UE, fuljetti, u aktar informazzjoni dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-57.png)

**L-ewwel passi:**

- Qabbad mal-kompjuter tiegħek mal-apparat;
- Qabbad l-apparat ma 'sors ta' enerġija;
- Uża WebFig f’web browser jew l-għodda ta’ konfigurazzjoni “WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **metodi multipli ta’ konfigurazzjoni huma disponibbli biex tiġi żgurata l-aċċessibbiltà;**
- Ibda l-konfigurazzjoni fi ħdan l-għażla tal-għodda, bl-użu tal-indirizz IP predefinit 192.168.88.1. Jekk l-indirizz IP mhux disponibbli, uża l-Winbox u għażel it-tab "Neighbors" biex issib id-dispożitt;
- Żomm mill-quddiem biex tikkolet b'indirizz MAC. L-username huwa "admin", u m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-kodiċijiet tal-utent u t-tal-wi-fi fuq l-isticker);
- Ikklikkja fuq il-buttuna "Check for updates" u aġġorna l-RouterOS għall-aħħar verżjoni;
- Għal aġġornament manwali tal-apparat, żur mikrotik.com, agħżel il-mudell tiegħek u sib il-pakketti meħtieġa fis-sezzjoni "Downloads";
- Uploadja tal-pakketti miżjuda fil-menu "Files" ta' WebFig jew WinBox u rerew boot l-apparat;
- Billi taġġorna l-softwer tal-RouterOS għall-aħħar verżjoni, tista 'tissikura prestazzjoni, stabbiltà u aġġornamenti ta' sikurezza ottimali;
- Iffurmat il-password tar-router tiegħek.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi, u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi tan-netwerk, it-termini u l-kunċetti.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li jistgħu jinstabu fl-imballaġġ oriġinali ta 'dan il-prodott.
- Dan it-tagħmir għandu jiġi installat minn persunal imħarreġ u kwalifikat, skont dawn l-istruzzjonijiet tal-installazzjoni. L-installatur huwa responsabbli biex jiżgura li l-Installazzjoni tat-tagħmir tkun konformi mal-kodiċi elettriċi lokali u nazzjonali. Tippruvax iżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott huwa maħsub biex jiġi installat ġewwa. Żomm dan il-prodott 'il bogħod mill-ilma, nar, umdità, jew ambjenti sħan.
- Ma nistgħux niggarantixxu li ma jiġru l-ebda inċidenti jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u topera għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok skonnettjaha mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiskonnettja l-plagg tal-enerġija mill-iżbokk tal-elettriku.
- Dan huwa prodott tal-Klassi A. F'ambjent domestiku, dan il-prodott jista 'jikkawża interferenza tar-radju f'liema każ l-utent jista' jkun meħtieġ li jieħu miżuri adegwati.
Manifattur: Mikrotikls SIA, Unijas iela 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar de nieuwste softwareversie v7.10 om te voldoen aan de lokale regelgeving!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften. Alle MikroTik-apparaten moeten professioneel worden geïnstalleerd.
:::

*Dit is een netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties voor dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, volledige EU-conformiteitsverklaring, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-57.png)

**Eerste stappen:**

- Maak verbinding met uw computer naar het apparaat;
- Sluit het apparaat aan op een stroombron;
- Gebruik WebFig in een webbrowser of de configuratietool "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **er zijn meerdere configuratiemethoden beschikbaar om toegankelijkheid te waarborgen;**
- Start de configuratie binnen het gekozen gereedschap met het standaard IP-adres 192.168.88.1. Als het IP-adres niet beschikbaar is, gebruik Winbox en kies het tabblad "Neighbors" om het apparaat te vinden;
- Ga verder met verbinden met behulp van het MAC-adres. De gebruikersnaam is "admin" en er is geen wachtwoord (of, voor sommige modellen, controleer de gebruikers- en draadloze wachtwoorden op de sticker);
- Klik op de knop "Check for updates" en update RouterOS naar de nieuwste versie;
- Voor een handmatige update van het apparaat, ga naar mikrotik.com, selecteer uw model en vind de benodigde pakketten in de sectie "Downloads";
- Upload gedownloade pakketten naar het WebFig- of WinBox-"Files"-menu en herstart het apparaat;
- Door uw RouterOS-software bij te werken naar de nieuwste versie, kunt u optimale prestaties, stabiliteit en beveiligingsupdates garanderen;
- Stel uw routerwachtwoord in.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur gaat werken, moet u zich bewust zijn van de gevaren die verbonden zijn aan elektrische circuits en vertrouwd zijn met de standaardpraktijken om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die zijn goedgekeurd door de fabrikant en die zich in de originele verpakking van dit product bevinden.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur is ervoor verantwoordelijk dat de installatie van de apparatuur in overeenstemming is met de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product is bedoeld om binnenshuis te worden geïnstalleerd. Houd dit product uit de buurt van water, vuur, vochtigheid of hete omgevingen.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en gebruik het op eigen risico!
- In het geval van een apparaatstoring, koppel het dan los van de stroom. De snelste manier om dit te doen is door de stekker uit het stopcontact te halen.
- Dit is een klasse A-product. In een huiselijke omgeving kan dit product radiostoring veroorzaken, in welk geval de gebruiker mogelijk passende maatregelen moet nemen.
Fabrikant: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie musi zostać zaktualizowane do najnowszej wersji oprogramowania v7.10, aby zapewnić zgodność z lokalnymi przepisami!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych. Wszystkie urządzenia MikroTik muszą być profesjonalnie zainstalowane.
:::

*To jest urządzenie sieciowe. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Specyfikacje techniczne, pełna deklaracja zgodności UE, broszury i więcej informacji o produktach na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-57.png)

**Pierwsze kroki:**

- Połącz się z komputerem do urządzenia;
- Podłącz urządzenie do źródła zasilania;
- Użyj WebFig w przeglądarce internetowej lub narzędzia konfiguracyjnego "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **dostępnych jest wiele metod konfiguracji w celu zapewnienia dostępności;**
- Rozpocznij konfigurację w wybranym narzędziu, używając domyślnego adresu IP 192.168.88.1. Jeśli adres IP nie jest dostępny, użyj Winboxa i wybierz zakładkę "Neighbors", aby odnaleźć urządzenie;
- Przejdź do połączenia za pomocą adresu MAC. Nazwa użytkownika to "admin", a hasła brak (lub, dla niektórych modeli, sprawdź hasła użytkownika i do sieci bezprzewodowej na naklejce);
- Kliknij przycisk "Check for updates" i zaktualizuj RouterOS do najnowszej wersji;
- Aby ręcznie zaktualizować urządzenie, odwiedź mikrotik.com, wybierz swój model i znajdź wymagane pakiety w sekcji "Downloads";
- Prześlij pobrane paczki do menu "Files" WebFig lub WinBox i zrestartuj urządzenie;
- Aktualizując oprogramowanie RouterOS do najnowszej wersji, zapewnisz optymalną wydajność, stabilność i aktualizacje zabezpieczeń;
- Ustaw hasło dla swojego routera.

**Informacje dotyczące bezpieczeństwa:**

- Zanim zaczniesz pracować na jakimkolwiek sprzęcie MikroTik, bądź świadomy zagrożeń związanych z obwodami elektrycznymi i zapoznaj się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien znać struktury, terminy i koncepcje sieci.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta i znajdujących się w oryginalnym opakowaniu tego produktu.
- To urządzenie ma być instalowane przez przeszkolony i wykwalifikowany personel, zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie próbuj demontować, naprawiać ani modyfikować urządzenia.
- Ten produkt jest przeznaczony do instalacji w pomieszczeniach. Trzymaj ten produkt z dala od wody, ognia, wilgoci lub gorących środowisk.
- Nie możemy zagwarantować, że z powodu niewłaściwego użytkowania urządzenia nie nastąpią żadne wypadki lub uszkodzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia należy odłączyć je od zasilania. Najszybszym sposobem na to jest wyjęcie wtyczki z gniazdka.
- To jest produkt klasy A. W środowisku domowym ten produkt może powodować zakłócenia radiowe, w którym to przypadku użytkownik może być zobowiązany do podjęcia odpowiednich środków.
Producent: Mikrotikls SIA, Unijas iela 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para a versão mais recente do software v7.10 para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país. Todos os dispositivos MikroTik devem ser instalados profissionalmente.
:::

*Este é o dispositivo de rede. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, brochuras e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-57.png)

**Primeiros passos:**

- Conecte-se ao seu computador no dispositivo;
- Conecte o dispositivo a uma fonte de energia;
- Use o WebFig num navegador ou a ferramenta de configuração "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **estão disponíveis vários métodos de configuração para garantir a acessibilidade;**
- Inicie a configuração dentro da ferramenta escolhida, usando o endereço IP padrão 192.168.88.1. Se o endereço IP não estiver disponível, use o Winbox e escolha a guia "Neighbors" para encontrar o dispositivo;
- Prossiga para se conectar usando o endereço MAC. O nome de usuário é "admin", e não há senha (ou, para alguns modelos, verifique as senhas do usuário e sem fio no adesivo);
- Clique no botão "Check for updates" e atualize o RouterOS para a versão mais recente;
- Para atualizar manualmente o dispositivo, visite mikrotik.com, selecione o seu modelo e localize os pacotes necessários na seção "Downloads";
- Faça o upload dos pacotes baixados para o menu "Files" do WebFig ou WinBox e reinicie o dispositivo;
- Ao atualizar o software do RouterOS para a versão mais recente, você pode garantir desempenho, estabilidade e atualizações de segurança ideais;
- Configure a senha do seu roteador.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos perigos envolvidos com os circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com as estruturas, termos e conceitos de rede.
- Use apenas fonte de alimentação e acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto deve ser instalado em ambientes internos. Mantenha este produto longe de água, fogo, umidade ou ambientes quentes.
- Não podemos garantir que nenhum acidente ou dano ocorrerá devido ao uso impróprio do dispositivo. Use este produto com cuidado e opere por sua própria conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o plugue de alimentação da tomada.
- Este é um produto de Classe A. Em um ambiente doméstico, este produto pode causar interferência de rádio, caso em que o usuário pode ser obrigado a tomar as medidas adequadas.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie actualizat la cea mai recentă versiune software v7.10 pentru a asigura respectarea reglementărilor autorităților locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării. Toate dispozitivele MikroTik trebuie instalate profesional.
:::

*Acesta este dispozitivul de rețea. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Especificações técnicas, Declaração de conformidade completa da UE, folhetos e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-57.png)

**Primii pasi:**

- Conectați-vă cu computerul la dispozitiv;
- Conectați dispozitivul la o sursă de alimentare;
- Utilizați WebFig într-un browser web sau instrumentul de configurare "WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **sunt disponibile mai multe metode de configurare pentru a asigura accesibilitatea;**
- Începeți configurarea în instrumentul ales, utilizând adresa IP implicită 192.168.88.1. Dacă adresa IP nu este disponibilă, utilizați Winbox și alegeți fila "Neighbors" pentru a găsi dispozitivul;
- Continuați să vă conectați utilizând adresa MAC. Numele de utilizator este "admin", și nu există nicio parolă (sau, pentru unele modele, verificați parolele de utilizator și wireless de pe autocolant);
- Faceți clic pe butonul "Check for updates" și actualizați RouterOS la cea mai recentă versiune;
- Pentru actualizarea manuală a dispozitivului, accesați mikrotik.com, selectați modelul dvs. și găsiți pachetele necesare în secțiunea "Downloads";
- Încărcați pachetele descărcate în meniul "Files" al WebFig sau WinBox și reporniți dispozitivul;
- Prin actualizarea software-ului RouterOS la cea mai recentă versiune, puteți asigura performanțe, stabilitate și actualizări de securitate optime;
- Configurați parola routerului.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Instalatorul ar trebui să fie familiarizat cu structurile de rețea, termenii și conceptele.
- Utilizați numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament trebuie instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil pentru asigurarea faptului că instalarea echipamentului este conformă cu codurile electrice locale și naționale. Nu încercați să dezasamblați, să reparați sau să modificați dispozitivul.
- Acest produs este destinat instalării în interior. Păstrați acest produs departe de apă, foc, umiditate sau medii fierbinți.
- Nu putem garanta că nu vor apărea accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe propriul risc!
- În caz de defecțiune a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cea mai rapidă modalitate de a face acest lucru este deconectând ștecherul de la priză.
- Acesta este un produs de clasa A. Într-un mediu casnic, acest produs ar putea provoca interferențe radio, caz în care utilizatorul ar putea fi obligat să ia măsuri adecvate.
Producător: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie musí byť aktualizované na najnovšiu verziu softvéru v7.10, aby sa zabezpečilo dodržiavanie predpisov miestnych úradov!
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny. Všetky zariadenia MikroTik musia byť profesionálne nainštalované.
:::

*Toto je sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete nastránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej strane tohto stručného sprievodcu.*
*Specificații tehnice, Declarație de conformitate UE completă, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-57.png)

**Prvé kroky:**

- Spojte sa s počítačom so zariadením;
- Pripojte zariadenie k zdroju napájania;
- Použite WebFig v webovom prehliadači alebo konfiguračný nástroj "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na zabezpečenie prístupnosti sú k dispozícii viaceré metódy konfigurácie;**
- Spustite konfiguráciu vo vybranom nástroji s predvolenou IP adresou 192.168.88.1. Ak adresa IP nie je k dispozícii, použite Winbox a vyberte kartu "Neighbors", aby ste zariadenie našli;
- Pokračujte v pripájaní pomocou MAC adresy. Užívateľské meno je "admin" a nie je žiadne heslo (alebo, pre niektoré modely, skontrolujte užívateľské a bezdrôtové heslá na štítku);
- Kliknite na tlačidlo "Check for updates" a aktualizujte RouterOS na najnovšiu verziu;
- Na manuálnu aktualizáciu zariadenia navštívte mikrotik.com, vyberte svoj model a nájdite požadované balíčky v sekcii "Downloads";
- Nahrajte stiahnuté balíky do menu "Files" vo WebFig alebo WinBox a reštartujte zariadenie;
- Aktualizáciou softvéru RouterOS na najnovšiu verziu môžete zabezpečiť optimálny výkon, stabilitu a aktualizácie zabezpečenia;
- Nastavte heslo pre váš router.

**Bezpečnostné informácie:**

- Pred prácou na akomkoľvek zariadení MikroTik si uvedomte riziká spojené s elektrickým obvodom a oboznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, termínmi a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré sa nachádzajú v pôvodnom obale tohto produktu.
- Toto zariadenie má byť inštalované vyškoleným a kvalifikovaným personálom podľa týchto inštalačných pokynov. Inštalatér zodpovedá za to, že inštalácia zariadenia je v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je určený na inštaláciu v interiéri. Uchovávajte tento výrobok mimo vody, ohňa, vlhkosti alebo horúceho prostredia.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Používajte tento výrobok opatrne a pracujte na vlastné riziko!
- V prípade poruchy zariadenia ho odpojte od napájania. Najrýchlejší spôsob, ako to urobiť, je vytiahnuť sieťovú zástrčku zo zásuvky.
- Toto je výrobok triedy A. V domácom prostredí môže tento výrobok spôsobovať rádiové rušenie. V takom prípade môže byť od používateľa vyžadované prijatie primeraných opatrení.
Výrobca: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na najnovejšo različico programske opreme v7.10, da se zagotovi skladnost z lokalnimi predpisi!
Končni uporabniki so odgovorni za sledenje lokalnim predpisom. Vse naprave MikroTik morajo biti profesionalno nameščene.
:::

*To je omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani tega Hitrega vodnika.*
*Technické špecifikácie, úplné EÚ vyhlásenie o zhode, brožúry a ďalšie informácie o produktoch na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-57.png)

**Prvi koraki:**

- Povežite se z računalnikom v napravi;
- Napravo priključite na vir napajanja;
- Uporabite WebFig v spletni brskalniku ali konfiguracijsko orodje "WinBox“ [https://mt.lv/winbox](https://mt.lv/winbox); **na voljo je več metod konfiguracije za zagotovitev dostopnosti;**
- Začnite konfiguracijo znotraj izbranega orodja, uporabite privzeti IP naslov 192.168.88.1. Če IP naslov ni na voljo, uporabite Winbox in izberite zavihek "Neighbors", da najdete napravo;
- Nadaljujte s povezovanjem z uporabo MAC naslova. Uporabniško ime je "admin", in gesla ni (ali, za nekatere modele, preverite gesla za uporabnika in brezžična gesla na nalepki);
- Kliknite na gumb "Check for updates" in posodobite RouterOS na najnovejšo različico;
- Za ročno posodobitev naprave obiščite mikrotik.com, izberite svoj model in poiščite potrebne pakete v razdelku "Downloads";
- Naložite prenesene pakete v meni "Files" WebFig ali WinBox in znova zaženite napravo;
- Z nadgradnjo programske opreme RouterOS na najnovejšo različico zagotovite optimalne zmogljivosti, stabilnost in varnostne posodobitve;
- Nastavite geslo za svoj usmerjevalnik.

**Varnostne informacije:**

- Preden delate na kateri koli MikroTik opremi, se zavedajte nevarnosti, povezanih z električnimi vezji, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora poznati omrežne strukture, izraze in koncepte.
- Uporabljajte samo napajalnik in dodatno opremo, ki jih je odobril proizvajalec in jih najdete v originalni embalaži tega izdelka.
- To opremo mora namestiti usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstavljati, popravljati ali spreminjati.
- Ta izdelek je namenjen za vgradnjo v zaprtih prostorih. Izdelek hranite ločeno od vode, ognja, vlage ali vročih okolij.
- Ne moremo jamčiti, da zaradi nepravilne uporabe naprave ne bo prišlo do nesreč ali poškodb. Prosimo, da ta izdelek uporabljate previdno in delate na lastno odgovornost!
- V primeru okvare naprave odklopite napajanje. Najhitreje to storite tako, da izvlečete vtič iz vtičnice.
- To je izdelek razreda A. V domačem okolju lahko ta izdelek povzroči radijske motnje, v tem primeru bo uporabnik morda moral sprejeti ustrezne ukrepe.
Proizvajalec: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Denne enheten må oppgraderes til den nyeste programvareversjonen v7.10 for å sikre samsvar med lokale myndighetsbestemmelser!
Det är slutanvändarnas ansvar att följa lokala landsregler. Alla MikroTik-enheter måste vara professionellt installerade.
:::

*Det här är nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, fullständig EU-försäkran om överensstämmelse, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-57.png)

**Första stegen:**

- Anslut med din dator till enheten;
- Anslut enheten till en strömkälla;
- Använd WebFig i en webbläsare eller konfigurationsverktyget "WinBox" [https://mt.lv/winbox](https://mt.lv/winbox); **flera konfigurationsmetoder är tillgängliga för att säkerställa tillgänglighet;**
- Påbörja konfigurationen inom det valda verktyget med standard IP-adress 192.168.88.1. Om IP-adressen inte är tillgänglig, använd Winbox och välj fliken "Neighbors" för att hitta enheten;
- Fortsätt att ansluta med hjälp av MAC-adressen. Användarnamnet är "admin" och det finns inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- Klicka på knappen "Check for updates" och uppdatera RouterOS till den senaste versionen;
- För manuell uppdatering av enheten, gå till mikrotik.com, välj din modell och hitta de nödvändiga paketen i avsnittet "Downloads";
- Ladda upp nedladdade paket till WebFig eller WinBox "Files" -menyn och starta om enheten;
- Genom att uppdatera RouterOS-programvaran till den senaste versionen kan du säkerställa optimal prestanda, stabilitet och säkerhetsuppdateringar;
- Konfigurera lösenordet för din router.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik -utrustning, var medveten om riskerna med elektriska kretsar och bekanta dig med standardmetoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen till denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt denna installationsanvisning. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska föreskrifter. Försök inte demontera, reparera eller modifiera enheten.
- Denna produkt är avsedd att installeras inomhus. Håll denna produkt borta från vatten, eld, fukt eller varma miljöer.
- Vi kan inte garantera att inga olyckor eller skador uppstår på grund av felaktig användning av enheten. Använd denna produkt med omsorg och kör på egen risk!
- Vid enhetsfel, koppla bort den från strömmen. Det snabbaste sättet att göra det är att dra ut kontakten ur vägguttaget.
- Detta är en klass A -produkt. I hemmet kan denna produkt orsaka radiostörningar, i vilket fall användaren kan behöva vidta lämpliga åtgärder.
Tillverkare: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
该设备需要升级到最新的软件版本 v7.10，以确保符合地方法规！
最终用户有责任遵守当地的法规。所有MikroTik设备都必须经过专业安装。
:::

*这是网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*技术规格、完整的欧盟符合性声明、手册以及有关产品的更多信息，请访问 [https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-57.png)

**第一步：**

- 将计算机连接到设备；
- 将设备连接到电源。
- 在网络浏览器中使用 WebFig 或使用“WinBox”配置工具 [https://mt.lv/winbox](https://mt.lv/winbox) **提供多种配置方法以确保可访问性；**
- 在所选工具中使用默认IP地址192.168.88.1开始配置。如果IP地址不可用，请使用Winbox并选择“邻居”选项卡查找设备;
- 继续使用MAC地址进行连接。用户名为"admin"，没有密码（或者，对于某些型号，请检查贴纸上的用户和无线密码）;
- 单击"Check for updates"按钮并将RouterOS更新到最新版本;
- 要手动更新设备，请访问 mikrotik.com，选择您的型号，并在"Downloads"部分找到所需的软件包；
- 将下载的软件包上传到WebFig或WinBox的“Files”菜单，并重新启动设备;
- 通过将RouterOS软件更新到最新版本，您可以确保最佳性能，稳定性和安全更新;
- 设置您的路由器密码。

**安全信息：**

- 在您使用任何 MikroTik 设备之前，请注意与电路相关的危险，并熟悉预防事故的标准做法。安装人员应熟悉网络结构、术语和概念。
- 只能使用制造商认可的电源和附件，这些附件可以在本产品的原始包装中找到。
- 该设备应由经过培训的合格人员按照这些安装说明进行安装。安装人员负责确保设备的安装符合当地和国家电气规范。请勿尝试拆卸、修理或改装设备。
- 本产品旨在安装在室内。使本产品远离水、火、湿气或高温环境。
- 我们不能保证不会因设备使用不当而发生事故或损坏。请谨慎使用本产品，操作风险自负！
- 如果设备出现故障，请断开电源。最快的方法是从电源插座上拔下电源插头。
- 这是A类产品。在家庭环境中，本产品可能会造成无线电干扰，在这种情况下，用户可能需要采取足够的措施
制造商：Mikrotikls SIA，拉脱维亚Unijas iela 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство необходимо обновить до последней версии программного обеспечения v7.10, чтобы обеспечить соответствие местных нормативов!
Конечные пользователи несут ответственность за соблюдение местных нормативов. Все устройства MikroTik должны быть профессионально установлены.
:::

*Это сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, Полная декларация о соответствии требованиям ЕС, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-56.png)

**Первые шаги:**

- Подключиться с помощью компьютера к устройству;
- Подключите устройство к источнику питания;
- Используйте WebFig в веб-браузере или инструмент настройки ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **доступно несколько методов настройки для обеспечения доступности;**
- Начните настройку в выбранном инструменте, используя стандартный IP-адрес 192.168.88.1. Если IP-адрес недоступен, используйте Winbox и выберите вкладку "Neighbors", чтобы найти устройство;
- Продолжайте подключение, используя MAC-адрес. Имя пользователя - "admin", и пароля нет (или, для некоторых моделей, проверьте пользовательские и беспроводные пароли на наклейке);
- Нажмите кнопку "Check for updates" и обновите RouterOS до последней версии;
- Для ручного обновления устройства зайдите на mikrotik.com, выберите свою модель и найдите необходимые пакеты в разделе "Downloads";
- Загрузите скачанные пакеты в меню "Files" WebFig или WinBox и перезагрузите устройство;
- Обновив программное обеспечение RouterOS до последней версии, вы можете обеспечить оптимальную производительность, стабильность и обновления безопасности;
- Настройте пароль для вашего роутера.

**Информация по технике безопасности:**

- Перед началом работы на любом оборудовании MikroTik ознакомьтесь с опасностями, связанными с электрическими цепями, и ознакомьтесь со стандартными методами предотвращения несчастных случаев. Установщик должен быть знаком с сетевыми структурами, терминами и концепциями.
- Используйте только те источники питания и аксессуары, которые утверждены производителем и находятся в оригинальной упаковке этого продукта.
- Это оборудование должно быть установлено обученным и квалифицированным персоналом согласно этим инструкциям по установке. Установщик несет ответственность за то, чтобы установка оборудования соответствовала местным и национальным электротехническим нормам и правилам. Не пытайтесь разбирать, ремонтировать или модифицировать устройство.
- Изделие предназначено для установки в помещении. Держите этот продукт вдали от воды, огня, влаги или жарких сред.
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
Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. **Cм. на упаковке.**

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

![](./img/image2020-1-24_7-55-5.badge-57.png)

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до останньої версії програмного забезпечення v7.10, щоб забезпечити відповідність місцевим нормам влади!

Кінцеві користувачі несуть відповідальність за дотримання місцевих правил. Всі радіопристрої MikroTik повинні бути встановлені відповідно до інструкцій.
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої версії посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Технічні характеристики, брошури та додаткова інформація про продукцію на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Посібник з налаштування програмного забезпечення вашою мовою з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image-2022-12-9_14-4-59.badge-13.png)

**Перші кроки:**

- Підключіться з комп'ютером до пристрою;
- Підключіть пристрій до адаптеру електроживлення;
- Використовуйте WebFig у веб-браузері або інструмент конфігурації ”WinBox” [https://mt.lv/winbox](https://mt.lv/winbox); **доступно декілька методів налаштування для забезпечення доступності;**
- Розпочніть конфігурацію в обраному інструменті, використовуючи стандартну IP-адресу 192.168.88.1. Якщо IP-адреса недоступна, використовуйте Winbox і виберіть вкладку "Neighbors", щоб знайти пристрій.
- Продовжуйте підключення, використовуючи MAC-адресу. Ім'я користувача - "admin", і немає пароля (або, для деяких моделей, перевірте паролі користувача та бездротові паролі на наклейці);
- Натисніть кнопку "Check for updates" і оновіть RouterOS до останньої версії;
- Щоб оновити пристрій вручну, відвідайте сторінку продуктів за адресою mikrotik.com, виберіть свою модель і знайдіть потрібні пакети в розділі "Downloads";
- Завантажте завантажені пакети в меню "Files" WebFig або WinBox та перезавантажте пристрій;
- Оновивши програмне забезпечення RouterOS до останньої версії, ви можете забезпечити оптимальну продуктивність, стабільність та оновлення безпеки;
- Встановіть свій пароль маршрутизатора.

**Інформація про безпеку:**

- Перш ніж працювати з будь-яким обладнанням MikroTik, усвідомте небезпеку, пов’язану з електричними схемами, і ознайомтеся зі стандартними методами запобігання нещасним випадкам. Особа, що виконує роботи зі встановлення устаткування мусить бути ознайомлена із правилами роботи з мережевими системами, термінами та концепціями.
- Використовуйте тільки адаптер електроживлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Це обладнання призначене для встановлення в приміщенні. Тримайте це обладнання подалі від води, вогню, вологи, або гарячого середовища.
- Ми не можемо гарантувати відсутність нещасних випадків або пошкоджень через неправильне використання пристрою. Використовуйте цей продукт обережно та на свій страх і ризик.
- У разі несправності пристрою відключіть його від електроживлення. Найшвидший спосіб це зробити — від’єднати адаптер електроживлення від розетки.
- Це продукт класу А. У побутових умовах цей виріб може викликати радіоперешкоди, і в цьому випадку від користувача може знадобитися вжити відповідних заходів.
Виробник: Mikrotikls SIA, Unijas iela 2, Рига, Латвія, LV1039.

![](./img/ua.badge-19.jpg)

## Federal Communication Commission Interference Statement

![](./img/fcc_logo_ez.badge-50.jpg)

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation.

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instruction manual, may cause harmful interference to radio communications. Operation of this equipment in a residential area is likely to cause harmful interference in which case the user will be required to correct the interference at his own expense

**FCC Caution:** Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

## Innovation, Science and Economic Development Canada

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

## UKCA marking

![](./img/ukca_black_fill.badge-55.gif)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Параметры входной мощности продукта
(EN) DC Adapter Output Specification, (V / A)(DE) Ausgangsspezifikationen des Gleichstromadapters, (V / A)(FR) Spécifications de sortie de l'adaptateur de courant continu, (V / A)(IT) Specifiche di uscita dell'adattatore di corrente continua, (V / A)(ES) Especificaciones de salida del adaptador de corriente continua, (V / A)(RU) Выходные характеристики адаптера постоянного тока, (В / А)
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

CRS125-24G-1S-IN, CRS305-1G-4S+IN DC Jack PoE In Ethernet Port CRS326-24G-2S+RM, CRS326-24G-2S+IN, CRS309-1G-8S+IN, CRS212-1G-10S+1S+IN DC Jack PoE In Ethernet Port
24 V / 0.8 A 24 V / 1.2 A
IP20 IP20
-40°..+60°C -40°..+60°C

\#77992 #77991
