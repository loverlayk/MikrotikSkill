# Quick Guide - netFiber 9

> It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed. :::

![](./img/mt_logo_arrow_v2-02-88.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.12 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations. All MikroTik devices must be professionally installed.
:::

This Quick Guide covers the model: CRS310-1G-5S-4S+OUT.

*This is a network device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Technical specifications, Full EU Declaration of Conformity, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-100.png)

**First steps:**

- Connect with your computer to the device;
- Download the configuration tool [https://mt.lv/winbox](https://mt.lv/winbox);
- Open the *Neighbors* tab and connect to the device using MAC address;
- The user name: *admin*, by default there is no password (or, for some models, check user and wireless passwords on the sticker);
- To update the device to the latest software version download the latest RouterOS software from https://mikrotik.com/download;
- Choose ARM packages, and save them to your computer;
- Return to the WinBox and upload downloaded packages;
- Restart the device.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry, and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be used both indoors and outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation for people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power plug from the power outlet.
Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## BG - Български. Бързо ръководство

:::warning
Това устройство трябва да бъде надстроено до RouterOS v7.12 или най-новата версия на софтуера, за да се гарантира съответствие с разпоредбите на местните власти!
Крайните потребители са отговорни за спазването на местните разпоредби. Всички устройства на MikroTik трябва да бъдат професионално инсталиран.
:::

*Това е мрежово устройство. Можете да намерите името на модела на продукта на етикета на регистъра (ID).*
*Моля, посетете страницата с ръководството за потребителя на [https://mt.lv/um-bg](https://mt.lv/um-bg) за пълното актуализирано ръководство за употреба. Или сканирайте QR кода с мобилния си телефон.*
*Най-важните технически спецификации за този продукт могат да бъдат намерени на последната страница на това Кратко ръководство.*
*Технически спецификации, пълна ЕС декларация за съответствие, брошури и повече информация за продуктите на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Ръководство за конфигуриране на софтуер на вашия език с допълнителна информация можете да намерите на [https://mt.lv/help-bg](https://mt.lv/help-bg)*
*Устройствата MikroTik са за професионална употреба. Ако нямате квалификация, моля, потърсете консултант [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-15-57.badge-95.png)

**Първи стъпки:**

- Свържете се с вашия компютър към устройството;
- Изтеглете инструмента за конфигурация [https://mt.lv/winbox](https://mt.lv/winbox);
- Отворете раздела „ *Neighbors“* и се свържете с устройството, като използвате MAC адрес;
- Потребителското име: *admin*, по подразбиране няма парола (или, за някои модели, проверете потребителските и безжичните пароли на стикера);
- За да актуализирате устройството до най-новата версия на софтуера d, заредете най-новия софтуер на RouterOS от https://mikrotik.com/download;
- Изберете ARM пакети и ги запишете на вашия компютър;
- Върнете се в WinBox и качете изтеглени пакети;
- Рестартирайте устройството.

**Информация за безопасност:**

- Преди да работите с всяко оборудване на MikroTik, имайте предвид опасностите, свързани с електрическата верига, и се запознайте със стандартните практики за предотвратяване на злополуки. Инсталаторът трябва да е запознат с мрежовите структури, термини и понятия.
- Използвайте само захранването и аксесоарите, одобрени от производителя, и които можете да намерите в оригиналната опаковка на този продукт.
- Това оборудване трябва да се монтира от обучен и квалифициран персонал съгласно тези инструкции за монтаж. Инсталаторът отговаря за това, че инсталирането на оборудването е в съответствие с местните и националните електрически кодове. Не се опитвайте да разглобявате, ремонтирате или модифицирате устройството.
- Този продукт може да се използва както на закрито, така и на открито. Моля, прочетете внимателно инструкциите за монтаж, преди да започнете инсталацията. Неизползването на правилния хардуер и конфигурация или спазването на правилните процедури може да доведе до опасна ситуация за хората и повреда на системата.
- Не можем да гарантираме, че няма злополуки или повреди поради неправилна употреба на устройството. Моля, използвайте внимателно този продукт и работете на свой риск!
- В случай на повреда на устройството, моля, изключете го от захранването. Най-бързият начин да направите това е като извадите щепсела на захранването от контакта.
Производител: Mikrotikls SIA, Unijas iela 2, Рига, Латвия, LV1039.

## CS - Česko. Rychlý průvodce

:::warning
Toto zařízení musí být upgradováno na RouterOS v7.12 nebo nejnovější verzi softwaru, aby bylo zajištěno dodržování předpisů místních úřadů!
Je odpovědností koncových uživatelů dodržovat místní předpisy. Všechna zařízení MikroTik musí být profesionálně nainstalován.
Tento Stručný průvodce se týká modelu: CRS310-1G-5S-4S+OUT.
:::

*Toto je síťové zařízení. Název modelu produktu najdete na štítku případu (ID).*
*Úplnou aktuální uživatelskou příručku naleznete na stránce uživatelské příručky na adrese [https://mt.lv/um-cs](https://mt.lv/um-cs). Nebo naskenujte QR kód pomocí mobilního telefonu.*
*Nejdůležitější technické specifikace tohoto produktu najdete na poslední stránce tohoto Stručného průvodce.*
*Technické specifikace, úplné EU prohlášení o shodě, brožury a další informace o produktech na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurační příručku pro software ve vašem jazyce s dalšími informacemi naleznete na adrese [https://mt.lv/help-cs](https://mt.lv/help-cs)*
*Zařízení MikroTik jsou určena pro profesionální použití. Pokud nemáte kvalifikaci, vyhledejte konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-16-42.badge-95.png)

**První kroky:**

- Připojte se k počítači k počítači;
- Stáhněte si konfigurační nástroj [https://mt.lv/winbox](https://mt.lv/winbox);
- Otevřete kartu *Neighbors* a připojte se k zařízení pomocí adresy MAC;
- Uživatelské jméno: *admin*, ve výchozím nastavení není heslo (nebo u některých modelů zkontrolujte uživatelské a bezdrátové heslo na štítku);
- Chcete-li aktualizovat zařízení na nejnovější verzi softwaru, stáhněte si nejnovější software RouterOS z https://mikrotik.com/download;
- Vyberte si ARM balíčky a uložte je do svého počítače;
- Návrat do WinBoxu a nahrání stažených balíčků;
- Restartujte zařízení.

**Bezpečná informace:**

- Než začnete pracovat na jakémkoli zařízení MikroTik, uvědomte si rizika spojená s elektrickými obvody a seznamte se se standardními postupy pro prevenci nehod. Instalátor by měl být obeznámen se síťovými strukturami, termíny a koncepty.
- Používejte pouze napájecí zdroj a příslušenství schválené výrobcem, které najdete v originálním balení tohoto produktu.
- Toto zařízení musí instalovat vyškolený a kvalifikovaný personál podle těchto pokynů k instalaci. Instalátor odpovídá za to, že instalace zařízení je v souladu s místními a národními elektrickými předpisy. Nepokoušejte se zařízení rozebírat, opravovat ani upravovat.
- Tento produkt lze použít uvnitř i venku. Před zahájením instalace si prosím pečlivě přečtěte montážní pokyny. Pokud nebudete používat správný hardware a konfiguraci nebo nedodržíte správné postupy, může to mít za následek nebezpečnou situaci pro lidi a poškození systému.
- Nemůžeme zaručit, že v důsledku nesprávného používání zařízení nedojde k nehodám nebo poškození. Tento produkt používejte opatrně a používejte jej na vlastní nebezpečí!
- V případě poruchy zařízení jej prosím odpojte od napájení. Nejrychlejším způsobem je odpojení napájecí zástrčky ze zásuvky.
Výrobce: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## DA - Dansk. Hurtig guide

:::warning
Denne enhed skal opgraderes til RouterOS v7.12 eller den seneste softwareversion for at sikre overholdelse af lokale myndigheders regler!
Det er slutbrugerens ansvar at følge lokale landes regler. Alle MikroTik-enheder skal være professionelt installeret.
:::

*Dette er netværksenhed. Du kan finde produktmodelnavnet på sagetiketten (ID).*
*Besøg siden med brugermanualen på [https://mt.lv/um-da](https://mt.lv/um-da) for den fulde ajourførte brugermanual. Eller skan QR-koden med din mobiltelefon.*
*De vigtigste tekniske specifikationer for dette produkt findes på den sidste side i denne hurtigvejledning.*
*Tekniske specifikationer, fuld EU-overensstemmelseserklæring, brochurer og mere info om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationsvejledning til software på dit sprog med yderligere oplysninger kan findes på [https://mt.lv/help-da](https://mt.lv/help-da)*
*MikroTik-enheder er til professionel brug. Hvis du ikke har kvalifikationer, bedes du kontakte en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-13-55.badge-95.png)

**Første trin:**

- Opret forbindelse med din computer til enheden;
- Download konfigurationsværktøjet [https://mt.lv/winbox](https://mt.lv/winbox);
- Åbn fanen *Neighbors* og opret forbindelse til enheden ved hjælp af MAC-adresse;
- Brugernavnet: *admin*, som standard er der ingen adgangskode (eller, for nogle modeller, tjek bruger- og trådløs adgangskoder på mærkaten);
- Hvis du vil opdatere enheden til den nyeste softwareversion, skal du indlæse den nyeste RouterOS-software fra https://mikrotik.com/download;
- Vælg ARM-pakker, og gem dem på din computer;
- Vend tilbage til WinBox og upload downloadede pakker;
- Genstart enheden.

**Sikkerhedsoplysninger:**

- Inden du arbejder med MikroTik-udstyr, skal du være opmærksom på farerne i forbindelse med elektriske kredsløb og kende almindelig praksis til forebyggelse af ulykker. Installationsprogrammet skal være bekendt med netværksstrukturer, vilkår og koncepter.
- Brug kun strømforsyningen og det tilbehør, der er godkendt af producenten, og som findes i den originale emballage til dette produkt.
- Dette udstyr skal installeres af uddannet og kvalificeret personale i henhold til disse installationsinstruktioner. Installatøren er ansvarlig for at sikre, at installationen af ​​udstyret er i overensstemmelse med lokale og nationale elektriske koder. Forsøg ikke at adskille, reparere eller ændre enheden.
- Dette produkt kan bruges både indendørs og udendørs. Læs monteringsvejledningen grundigt inden installationen påbegyndes. Manglende brug af den korrekte hardware og konfiguration eller de korrekte procedurer kan resultere i en farlig situation for mennesker og skader på systemet.
- Vi kan ikke garantere, at der ikke vil ske ulykker eller skader på grund af forkert brug af enheden. Brug dette produkt med omhu og betjen det på egen risiko!
- I tilfælde af fejl på enheden skal du frakoble det fra strømmen. Den hurtigste måde at gøre det er ved at tage stikket ud af stikkontakten.
Producent: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## DE - Deutsche. Kurzanleitung

:::warning
Dieses Gerät muss auf RouterOS v7.12 oder die neueste Softwareversion aktualisiert werden, um die Einhaltung der örtlichen behördlichen Vorschriften zu gewährleisten!
Es liegt in der Verantwortung des Endbenutzers, die örtlichen Vorschriften zu befolgen. Alle MikroTik-Geräte müssen professionell installiert werden.
Diese Kurzanleitung behandelt das Modell: CRS310-1G-5S-4S+OUT.
:::

*Dies ist das Netzwerkgerät. Den Produktmodellnamen finden Sie auf dem Gehäuseaufkleber (ID).*
*Bitte besuchen Sie die Seite mit dem Benutzerhandbuch unter [https://mt.lv/um-de](https://mt.lv/um-de), um das vollständige und aktuelle Benutzerhandbuch zu erhalten. Oder scannen Sie den QR-Code mit Ihrem Handy.*
*Die wichtigsten technischen Daten für dieses Produkt finden Sie auf der letzten Seite dieser Kurzanleitung.*
*Technische Daten, vollständige EU-Konformitätserklärung, Broschüren und weitere Informationen zu Produkten unter [https://mikrotik.com/products](https://mikrotik.com/products)*
*Das Konfigurationshandbuch für Software in Ihrer Sprache mit zusätzlichen Informationen finden Sie unter [https://mt.lv/help-de](https://mt.lv/help-de)*
*MikroTik-Geräte sind für den professionellen Einsatz bestimmt. Wenn Sie keine Qualifikationen haben, suchen Sie bitte einen Berater [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-20-45.badge-95.png)

**Erste Schritte:**

- Stellen Sie mit Ihrem Computer eine Verbindung zum Gerät her;
- Laden Sie das Konfigurationstool [https://mt.lv/winbox](https://mt.lv/winbox) herunter;
- Öffnen Sie die Registerkarte *Neighbors* und stellen Sie über die MAC-Adresse eine Verbindung zum Gerät her;
- Der Benutzername: *admin*, standardmäßig gibt es kein Passwort (oder überprüfen Sie bei einigen Modellen die Benutzer- und WLAN-Passwörter auf dem Aufkleber);
- Um das Gerät auf die neueste Softwareversion zu aktualisieren, laden Sie die neueste RouterOS-Software von https://mikrotik.com/download herunter;
- Wählen Sie ARM-Pakete und speichern Sie sie auf Ihrem Computer;
- Kehren Sie zur WinBox zurück und laden Sie heruntergeladene Pakete hoch;
- Starten Sie das Gerät neu.

**Sicherheitsinformation:**

- Bevor Sie an MikroTik-Geräten arbeiten, sollten Sie sich der Gefahren bewusst sein, die mit elektrischen Schaltkreisen verbunden sind, und sich mit den Standardverfahren zur Verhinderung von Unfällen vertraut machen. Das Installationsprogramm sollte mit Netzwerkstrukturen, Begriffen und Konzepten vertraut sein.
- Verwenden Sie nur das vom Hersteller zugelassene Netzteil und Zubehör, das in der Originalverpackung dieses Produkts enthalten ist.
- Dieses Gerät muss von geschultem und qualifiziertem Personal gemäß diesen Installationsanweisungen installiert werden. Der Installateur ist dafür verantwortlich, dass die Installation des Geräts den örtlichen und nationalen elektrischen Vorschriften entspricht. Versuchen Sie nicht, das Gerät zu zerlegen, zu reparieren oder zu modifizieren.
- Dieses Produkt kann sowohl im Innen- als auch im Außenbereich verwendet werden. Bitte lesen Sie die Montageanleitung sorgfältig durch, bevor Sie mit der Installation beginnen. Wenn Sie die richtige Hardware und Konfiguration nicht verwenden oder die korrekten Verfahren nicht befolgen, kann dies zu einer Gefahrensituation für Personen und Schäden am System führen.
- Wir können nicht garantieren, dass durch unsachgemäße Verwendung des Geräts keine Unfälle oder Schäden auftreten. Bitte verwenden Sie dieses Produkt mit Vorsicht und arbeiten Sie auf eigenes Risiko!
- Trennen Sie das Gerät bei einem Stromausfall vom Stromnetz. Der schnellste Weg, dies zu tun, besteht darin, den Netzstecker aus der Steckdose zu ziehen.
Hersteller: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## EL - Ελληνικά. Γρήγορος οδηγός

:::warning
Αυτή η συσκευή πρέπει να αναβαθμιστεί στο RouterOS v7.12 ή στην πιο πρόσφατη έκδοση λογισμικού για να διασφαλιστεί η συμμόρφωση με τους κανονισμούς των τοπικών αρχών!
Είναι ευθύνη των τελικών χρηστών να ακολουθούν τους τοπικούς κανονισμούς των χωρών. Όλες οι συσκευές MikroTik πρέπει να εγκατασταθούν επαγγελματικά.
Αυτός ο γρήγορος οδηγός καλύπτει το μοντέλο: CRS310-1G-5S-4S+OUT.
:::

*Αυτή είναι η συσκευή δικτύου*. *Μπορείτε να βρείτε το όνομα του μοντέλου προϊόντος στην ετικέτα της θήκης (ID).*
*Επισκεφτείτε τη σελίδα του εγχειριδίου χρήστη στο [https://mt.lv/um-el](https://mt.lv/um-el) για το πλήρες ενημερωμένο εγχειρίδιο χρήσης. Ή να σαρώσετε τον κωδικό QR με το κινητό σας τηλέφωνο.*
*Οι πιο σημαντικές τεχνικές προδιαγραφές για αυτό το προϊόν βρίσκονται στην τελευταία σελίδα αυτού του γρήγορου οδηγού.*
*Τεχνικές προδιαγραφές, πλήρης δήλωση συμμόρφωσης ΕΕ, φυλλάδια και περισσότερες πληροφορίες σχετικά με τα προϊόντα στη διεύθυνση [https://mikrotik.com/products](https://mikrotik.com/products)*
*Το εγχειρίδιο διαμόρφωσης για λογισμικό στη γλώσσα σας με πρόσθετες πληροφορίες βρίσκεται στη διεύθυνση [https://mt.lv/help-el](https://mt.lv/help-el)*
*Οι συσκευές MikroTik προορίζονται για επαγγελματική χρήση. Εάν δεν έχετε τα προσόντα παρακαλώ ζητήστε έναν σύμβουλο [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-25-41.badge-95.png)

**Πρώτα βήματα:**

- Συνδεθείτε με τον υπολογιστή σας στη συσκευή;
- Κατεβάστε το εργαλείο διαμόρφωσης [https://mt.lv/winbox](https://mt.lv/winbox)
- Ανοίξτε την καρτέλα " *Neighbors*" και συνδεθείτε στη συσκευή χρησιμοποιώντας τη διεύθυνση MAC;
- Το όνομα χρήστη: *admin*, από προεπιλογή δεν υπάρχει κωδικός πρόσβασης (ή, για ορισμένα μοντέλα, ελέγξτε τους κωδικούς πρόσβασης χρήστη και ασύρματου δικτύου στο αυτοκόλλητο).
- Για να ενημερώσετε τη συσκευή με την πιο πρόσφατη έκδοση λογισμικού, φορτώστε το πιο πρόσφατο λογισμικό RouterOS από το https://mikrotik.com/download
- Επιλέξτε πακέτα ARM και αποθηκεύστε τα στον υπολογιστή σας;
- Επιστρέψτε στο WinBox και ανεβάστε τα ληφθέντα πακέτα;
- Επανεκκινήστε τη συσκευή.

**Οδηγίες ασφαλείας:**

- Πριν να εργαστείτε σε οποιοδήποτε εξοπλισμό MikroTik, να είστε ενήμεροι για τους κινδύνους που σχετίζονται με τα ηλεκτρικά κυκλώματα και να είστε εξοικειωμένοι με τις συνήθεις πρακτικές για την πρόληψη ατυχημάτων. Ο εγκαταστάτης πρέπει να είναι εξοικειωμένος με τις δομές, τους όρους και τις έννοιες του δικτύου.
- Χρησιμοποιήστε μόνο την τροφοδοσία ρεύματος και τα εξαρτήματα που έχει εγκριθεί από τον κατασκευαστή και τα οποία μπορείτε να βρείτε στην αρχική συσκευασία αυτού του προϊόντος.
- Αυτός ο εξοπλισμός πρέπει να εγκατασταθεί από εκπαιδευμένο και ειδικευμένο προσωπικό, σύμφωνα με αυτές τις οδηγίες εγκατάστασης. Ο εγκαταστάτης είναι υπεύθυνος για τη διασφάλιση της συμμόρφωσης της εγκατάστασης του εξοπλισμού με τους τοπικούς και εθνικούς ηλεκτρικούς κώδικες. Μην επιχειρήσετε να αποσυναρμολογήσετε, να επιδιορθώσετε ή να τροποποιήσετε τη συσκευή.
- Αυτό το προϊόν μπορεί να χρησιμοποιηθεί τόσο σε εσωτερικούς όσο και σε εξωτερικούς χώρους. Διαβάστε προσεκτικά τις οδηγίες τοποθέτησης πριν ξεκινήσετε την εγκατάσταση. Η μη χρήση του σωστού υλικού και της διαμόρφωσης ή η τήρηση των σωστών διαδικασιών μπορεί να οδηγήσει σε επικίνδυνη κατάσταση για τους ανθρώπους και ζημιά στο σύστημα.
- Δεν μπορούμε να εγγυηθούμε ότι δεν θα προκύψουν ατυχήματα ή ζημιές εξαιτίας της ακατάλληλης χρήσης της συσκευής. Χρησιμοποιείτε αυτό το προϊόν με προσοχή και λειτουργείτε με δική σας ευθύνη!
- Σε περίπτωση βλάβης της συσκευής, αποσυνδέστε την από την τροφοδοσία. Ο ταχύτερος τρόπος είναι να αποσυνδέσετε το φις από την πρίζα.
Κατασκευαστής: Mikrotikls SIA, Unijas iela 2, Ρίγα, Λετονία, LV1039.

## ES - Español. Guía rápida

:::warning
¡Este dispositivo debe actualizarse a RouterOS v7.12 o la última versión de software para garantizar el cumplimiento de las regulaciones de las autoridades locales!
Es responsabilidad del usuario final seguir las regulaciones locales del país. Todos los dispositivos de MikroTik deben ser instalado profesionalmente
Esta guía rápida cubre el modelo: CRS310-1G-5S-4S+OUT.
:::

*Este es un dispositivo de red. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Especificaciones técnicas, Declaración de conformidad de la UE completa, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-97.png)

**Primeros pasos:**

- Conéctese con su computadora al dispositivo;
- Descargue la herramienta de configuración [https://mt.lv/winbox](https://mt.lv/winbox);
- Abra la pestaña *Neighbors* y conéctese al dispositivo usando la dirección MAC;
- El nombre de usuario: *admin*, por defecto no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Para actualizar el dispositivo a la última versión del software, descargue el último software RouterOS desde https://mikrotik.com/download;
- Elija paquetes ARM y guárdelos en su computadora;
- Regrese a WinBox y cargue los paquetes descargados;
- Reinicia el dispositivo.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto se puede utilizar tanto en interiores como en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. No utilizar el hardware y la configuración correctos o no seguir los procedimientos correctos podría resultar en una situación peligrosa para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el enchufe de la toma de corriente.
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
See seade tuleb uuendada versioonile RouterOS v7.12 või uusimale tarkvaraversioonile, et tagada vastavus kohalike omavalitsuste eeskirjadele!
Lõppkasutajad vastutavad kohalike riigieeskirjade järgimise eest. Kõik MikroTik seadmed peavad olema professionaalselt paigaldatud.
See kiirjuhend hõlmab mudelit: CRS310-1G-5S-4S+OUT.
:::

*See on võrguseade. Toote mudeli nime leiate kohvri sildilt (ID).*
*Täieliku ja värske kasutusjuhendi saamiseks külastage kasutusjuhendit lehel [https://mt.lv/um-et](https://mt.lv/um-et). Või skannige oma mobiiltelefoniga QR-koodi.*
*Selle toote kõige olulisemad tehnilised andmed leiate selle kiirjuhendi viimaselt lehelt.*
*Tehnilised andmed, täielik EL-i vastavusdeklaratsioon, brošüürid ja lisateave toodete kohta aadressil [https://mikrotik.com/products](https://mikrotik.com/products)*
*Teie keeles oleva tarkvara konfiguratsioonijuhend koos lisateabega leiate aadressilt [https://mt.lv/help-et](https://mt.lv/help-et)*
*MikroTik seadmed on mõeldud professionaalseks kasutamiseks. Kui teil pole kvalifikatsiooni, pöörduge konsultandi poole [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-31-19.badge-95.png)

**Esimesed sammud:**

- Ühendage arvutiga seadmega;
- Laadige alla seadistusriist [https://mt.lv/winbox](https://mt.lv/winbox);
- Avage vahekaart *Neighbors* ja looge seadmega MAC-aadressi abil ühendus;
- Kasutajanimi: *admin*, vaikimisi parool puudub (või mõne mudeli puhul kontrollige kasutaja ja traadita ühenduse paroole kleebiselt);
- Seadme värskendamiseks uusimale tarkvaraversioonile laadige uusim tarkvara RouterOS alla aadressilt https://mikrotik.com/download;
- Valige ARM paketid ja salvestage need arvutisse;
- Naaske WinBoxi ja laadige alla laaditud paketid üles;
- Taaskäivitage seade.

**Ohutusteave:**

- Enne kui töötate mõne MikroTiku seadmega, tutvuge elektriskeemidega kaasnevate ohtudega ja tutvuge õnnetuste vältimise tavapraktikaga. Installer peaks tundma võrgustruktuure, termineid ja kontseptsioone.
- Kasutage ainult tootja poolt heaks kiidetud toiteallikat ja tarvikuid, mis on selle toote originaalpakendis.
- Need seadmed peavad paigaldama väljaõppinud ja kvalifitseeritud töötajad vastavalt käesolevatele paigaldusjuhistele. Paigaldaja vastutab selle eest, et seadmed paigaldataks vastavalt kohalikele ja riiklikele elektriseadustele. Ärge üritage seadet lahti võtta, remontida ega modifitseerida.
- Seda toodet saab kasutada nii toas kui ka väljas. Enne paigaldamise alustamist lugege hoolikalt paigaldusjuhiseid. Õige riistvara ja konfiguratsiooni kasutamata jätmine või õigete protseduuride järgimata jätmine võib põhjustada inimeste ohtlikku olukorda ja süsteemi kahjustada.
- Me ei saa garanteerida, et seadme ebaõige kasutamise tõttu ei juhtu õnnetusi ega kahjustusi. Kasutage seda toodet ettevaatlikult ja tegutsege omal vastutusel!
- Seadme rikke korral eraldage see vooluvõrgust. Kiireim viis selleks on pistiku pistikupesast lahti ühendamine.
Tootja: Mikrotikls SIA, Unijas iela 2, Riia, Läti, LV1039.

## FI - Suomalainen. Pikaopas

:::warning
Tämä laite on päivitettävä RouterOS v7.12:een tai uusimpaan ohjelmistoversioon paikallisten viranomaisten säädösten noudattamisen varmistamiseksi!
Loppukäyttäjien vastuulla on noudattaa paikallisia maalakeja. Kaikkien MikroTik-laitteiden on oltava ammattimaisesti asennettu.
Tämä pikaopas kattaa mallin: CRS310-1G-5S-4S+OUT.
:::

*Tämä on verkkolaite. Tuotemallin nimi löytyy kotelon etiketistä (ID).*
*Katso täydelliset ja ajantasaiset käyttöohjeet sivulta [https://mt.lv/um-fi](https://mt.lv/um-fi). Tai skannaa QR-koodi matkapuhelimellasi.*
*Tämän tuotteen tärkeimmät tekniset tiedot ovat tämän pikaoppaan viimeisellä sivulla.*
*Tekniset tiedot, täydellinen EU-vaatimustenmukaisuusvakuutus, esitteet ja lisätietoja tuotteista osoitteessa [https://mikrotik.com/products](https://mikrotik.com/products)*
*Kielelläsi olevien ohjelmistojen määritysoppaat, joissa on lisätietoja, ovat osoitteessa [https://mt.lv/help-fi](https://mt.lv/help-fi)*
*MikroTik-laitteet on tarkoitettu ammattikäyttöön. Jos sinulla ei ole pätevyyttä, ota yhteys konsulttiin [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-33-3.badge-95.png)

**Ensiaskeleet:**

- Yhdistä tietokoneesi laitteeseen;
- Lataa määritystyökalu [https://mt.lv/winbox](https://mt.lv/winbox);
- Avaa *Neighbors* välilehti ja muodosta yhteys laitteeseen MAC-osoitteen avulla;
- Käyttäjätunnus: *admin*, oletuksena ei ole salasanaa (tai joissakin malleissa tarkista käyttäjän ja langattoman verkon salasanat tarrasta);
- Laitteen päivittäminen uusimpaan ohjelmistoversioon d lataa uusin RouterOS-ohjelmisto osoitteesta https://mikrotik.com/download;
- Valitse ARM-paketit ja tallenna ne tietokoneellesi;
- Palaa WinBoxiin ja lataa ladatut paketit;
- Käynnistä laite uudelleen.

**Turvallisuustieto:**

- Ennen kuin työskentelet MikroTik-laitteiden kanssa, ole tietoinen sähköpiiriin liittyvistä vaaroista ja perehdy vakiintuneisiin käytäntöihin onnettomuuksien estämiseksi. Asentajan tulee tuntea verkkorakenteet, termit ja käsitteet.
- Käytä vain valmistajan hyväksymää virtalähdettä ja lisävarusteita, jotka löytyvät tämän tuotteen alkuperäispakkauksesta.
- Tämän laitteen saa asentaa koulutettu ja pätevä henkilöstö näiden asennusohjeiden mukaisesti. Asentajan on varmistettava, että laitteen asennus on paikallisten ja kansallisten sähkömääräysten mukainen. Älä yritä purkaa, korjata tai muokata laitetta.
- Tätä tuotetta voidaan käyttää sekä sisällä että ulkona. Lue asennusohjeet huolellisesti ennen asennuksen aloittamista. Oikean laitteiston ja kokoonpanon käyttämättä jättäminen tai oikeiden menettelytapojen noudattamatta jättäminen voi aiheuttaa ihmisille vaarallisen tilanteen ja vahingoittaa järjestelmää.
- Emme voi taata, että laitteen väärinkäytöstä ei aiheudu onnettomuuksia tai vaurioita. Käytä tätä tuotetta huolellisesti ja käytä omalla vastuulla!
- Irrota laite sähkövirrasta, jos laite vioittuu. Nopein tapa tehdä tämä on irrottaa virtajohto pistorasiasta.
Valmistaja: Mikrotikls SIA, Unijas iela 2, Riika, Latvia, LV1039.

## FR - Français. Guide rapide

:::warning
Cet appareil doit être mis à niveau vers RouterOS v7.12 ou la dernière version du logiciel pour garantir la conformité aux réglementations des autorités locales!
Il est de la responsabilité des utilisateurs finaux de suivre les réglementations locales du pays. Tous les appareils MikroTik doivent être installé professionnellement.
:::

*Ceci est un périphérique réseau. Vous pouvez trouver le nom du modèle du produit sur l'étiquette du boîtier (ID).*
*Veuillez visiter la page du manuel d'utilisation sur [https://mt.lv/um-fr](https://mt.lv/um-fr) pour le manuel d'utilisation complet et à jour. Ou scannez le code QR avec votre téléphone portable.*
*Les spécifications techniques les plus importantes de ce produit se trouvent sur la dernière page de ce guide rapide.*
*Spécifications techniques, déclaration de conformité UE complète, brochures et plus d'informations sur les produits sur [https://mikrotik.com/products](https://mikrotik.com/products)*
*Vous trouverez le manuel de configuration du logiciel dans votre langue avec des informations supplémentaires sur [https://mt.lv/help-fr](https://mt.lv/help-fr)*
*Les appareils MikroTik sont destinés à un usage professionnel. Si vous n'avez pas de qualifications, veuillez consulter un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-35-53.badge-95.png)

**Premiers pas:**

- Connectez-vous avec votre ordinateur à l'appareil;
- Téléchargez l'outil de configuration [https://mt.lv/winbox](https://mt.lv/winbox);
- Ouvrez l'onglet *Neighbors* et connectez-vous à l'appareil à l'aide de l'adresse MAC;
- Le nom d'utilisateur: *admin*, par défaut il n'y a pas de mot de passe (ou, pour certains modèles, vérifiez les mots de passe utilisateur et sans fil sur l'autocollant);
- Pour mettre à jour l'appareil vers la dernière version du logiciel, téléchargez le dernier logiciel RouterOS depuis https://mikrotik.com/download;
- Choisissez les packages ARM et enregistrez-les sur votre ordinateur;
- Revenez à la WinBox et téléchargez les packages téléchargés;
- Redémarrez l'appareil.

**Information sur la sécurité:**

- Avant de travailler sur un équipement MikroTik, soyez conscient des dangers liés aux circuits électriques et familiarisez-vous avec les pratiques standard de prévention des accidents. Le programme d'installation doit être familiarisé avec les structures, les termes et les concepts du réseau.
- Utilisez uniquement l'alimentation et les accessoires approuvés par le fabricant et qui se trouvent dans l'emballage d'origine de ce produit.
- Cet équipement doit être installé par du personnel formé et qualifié, conformément à ces instructions d'installation. L'installateur est responsable de s'assurer que l'installation de l'équipement est conforme aux codes électriques locaux et nationaux. N'essayez pas de démonter, réparer ou modifier l'appareil.
- Ce produit peut être utilisé aussi bien à l'intérieur qu'à l'extérieur. Veuillez lire attentivement les instructions de montage avant de commencer l'installation. Le fait de ne pas utiliser le matériel et la configuration corrects ou de suivre les procédures correctes peut entraîner une situation dangereuse pour les personnes et endommager le système.
- Nous ne pouvons garantir qu'aucun accident ou dommage ne se produira en raison d'une mauvaise utilisation de l'appareil. Veuillez utiliser ce produit avec soin et l'utiliser à vos propres risques!
- En cas de panne de l'appareil, veuillez le déconnecter de l'alimentation. La façon la plus rapide de le faire est de débrancher la fiche d'alimentation de la prise de courant.
Fabricant: Mikrotikls SIA, Unijas iela 2, Riga, Lettonie, LV1039.

## HR - Hrvatski. Brzi vodič

:::warning
Ovaj uređaj treba nadograditi na RouterOS v7.12 ili najnoviju verziju softvera kako bi se osigurala usklađenost s propisima lokalnih vlasti!
Odgovornost krajnjih korisnika je da slijede lokalne propise. Svi MikroTik uređaji moraju biti profesionalno instaliran.
Ovaj brzi vodič pokriva model: CRS310-1G-5S-4S+OUT.
:::

*Ovo je mrežni uređaj. Naziv modela proizvoda možete pronaći na naljepnici kućišta (ID).*
*Molimo posjetite stranicu s priručnikom na [https://mt.lv/um-hr](https://mt.lv/um-hr) za cjeloviti ažurirani korisnički priručnik. Ili skenirajte QR kod sa svojim mobilnim telefonom.*
*Najvažnije tehničke specifikacije za ovaj proizvod mogu se naći na posljednjoj stranici ovog Kratkog vodiča.*
*Tehničke specifikacije, puna EU izjava o sukladnosti, brošure i više informacija o proizvodima na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Priručnik o konfiguraciji softvera na vašem jeziku s dodatnim informacijama potražite na [https://mt.lv/help-hr](https://mt.lv/help-hr)*
*MikroTik uređaji su za profesionalnu upotrebu. Ako nemate kvalifikacije, potražite savjetnika [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-37-28.badge-95.png)

**Prvi koraci:**

- Povežite se s računalom na uređaj;
- Preuzmite alat za konfiguraciju [https://mt.lv/winbox](https://mt.lv/winbox);
- Otvorite karticu *Neighbors* i povežite se s uređajem pomoću MAC adrese;
- Korisničko ime: *admin*, prema zadanim postavkama nema lozinke (ili, za neke modele, provjerite korisničku i bežičnu lozinku na naljepnici);
- Za ažuriranje uređaja na najnoviju verziju softvera d vlastitim učitavanjem najnovijeg softvera RouterOS s https://mikrotik.com/download;
- Odaberite ARM pakete i spremite ih na svoje računalo;
- Vratite se na WinBox i prenesite preuzete pakete;
- Ponovo pokrenite uređaj.

**Sigurnosne informacije:**

- Prije nego što radite na bilo kojoj MikroTik opremi, budite svjesni opasnosti koje uključuju električni krug i upoznajte se sa standardnim postupcima za sprečavanje nezgoda. Instalacijski program trebao bi biti upoznat s mrežnim strukturama, pojmovima i konceptima.
- Koristite samo napajanje i pribor odobrene od proizvođača koji se mogu naći u originalnom pakiranju ovog proizvoda.
- Ovu opremu treba ugraditi obučeno i kvalificirano osoblje prema ovim uputama za ugradnju. Instalater je odgovoran za provjeru da je instalacija opreme u skladu s lokalnim i nacionalnim električnim propisima. Ne pokušavajte rastavljati, popravljati ili modificirati uređaj.
- Ovaj se proizvod može koristiti i u zatvorenom i na otvorenom. Molimo pažljivo pročitajte upute za montažu prije početka instalacije. Ako ne upotrijebite ispravan hardver i konfiguraciju ili ne slijedite ispravne postupke, moglo bi doći do opasne situacije za ljude i oštećenja sustava.
- Ne možemo jamčiti da neće doći do nezgoda ili oštećenja uslijed nepravilne uporabe uređaja. Molimo koristite ovaj proizvod s pažnjom i radite na vlastiti rizik!
- U slučaju kvara uređaja, isključite ga iz napajanja. Najbrži način za to je isključivanje utikača iz utičnice.
Proizvođač: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## HU - Magyar. Gyors útmutató

:::warning
Ezt az eszközt a RouterOS v7.12-re vagy a legújabb szoftververzióra kell frissíteni a helyi hatóságok előírásainak való megfelelés érdekében!
A végfelhasználók felelőssége a helyi országos előírások betartása. Az összes MikroTik készüléknek lennie kell szakszerűen telepítve.
Ez a gyors útmutató a következőre vonatkozik: CRS310-1G-5S-4S+OUT.
:::

*Ez hálózati eszköz. A terméktípus nevét a tok címkéjén (ID) találhatja meg.*
*Kérjük, keresse fel a használati útmutatót a [https://mt.lv/um-hu](https://mt.lv/um-hu) oldalon a teljes, legfrissebb használati útmutatóért. Vagy beolvashatja a QR-kódot mobiltelefonjával.*
*A termék legfontosabb műszaki specifikációi a Gyors útmutató utolsó oldalán találhatók.*
*Műszaki adatok, teljes EU-megfelelőségi nyilatkozat, prospektusok és további információk a termékekről a [https://mikrotik.com/products](https://mikrotik.com/products) oldalon*
*Az Ön nyelvén található szoftver konfigurációs kézikönyve és további információk a következő webhelyen találhatók: [https://mt.lv/help-hu](https://mt.lv/help-hu)*
*A MikroTik eszközök professzionális használatra készültek. Ha nem rendelkezik képesítéssel, kérjen tanácsadót [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-0-20.badge-95.png)

**Első lépések:**

- Csatlakoztassa számítógépét a készülékhez;
- Töltse le a konfigurációs eszközt: [https://mt.lv/winbox](https://mt.lv/winbox);
- Nyissa meg a *Neighbors* fület, és MAC-címmel csatlakozzon az eszközhöz;
- A felhasználónév: *admin*, alapértelmezés szerint nincs jelszó (vagy egyes modelleknél ellenőrizze a felhasználói és vezeték nélküli jelszavakat a matricán);
- Az eszköz frissítéséhez a legújabb szoftververzióra d töltse le a legújabb RouterOS szoftvert a https://mikrotik.com/download webhelyről;
- Válassza ki a ARM csomagokat, és mentse őket a számítógépére;
- Vissza a WinBox-hoz, és töltsön fel letöltött csomagokat;
- Indítsa újra az eszközt.

**Biztonsági információk:**

- Mielőtt bármilyen MikroTik berendezésen dolgozik, tisztában kell lennie az elektromos áramkörökkel kapcsolatos veszélyekkel, és ismernie kell a balesetek megelőzésére szolgáló szokásos gyakorlatokat. A telepítőnek ismeri a hálózati struktúrákat, a fogalmakat és a fogalmakat.
- Csak a gyártó által jóváhagyott tápegységet és tartozékokat használjon, amelyek a termék eredeti csomagolásában találhatók.
- Ezt a felszerelést képzett és képesített személyzetnek kell telepítenie, a jelen telepítési útmutató szerint. A telepítő felel annak biztosításáért, hogy a berendezés telepítése megfeleljen a helyi és az országos elektromos szabályoknak. Ne kísérelje meg szétszerelni, megjavítani vagy átalakítani a készüléket.
- Ez a termék beltéren és kültéren egyaránt használható. A telepítés megkezdése előtt figyelmesen olvassa el a szerelési útmutatót. Ha nem használja a megfelelő hardvert és konfigurációt, vagy nem tartja be a megfelelő eljárásokat, az veszélyes helyzetet okozhat az emberek számára, és károsíthatja a rendszert.
- Nem garantálhatjuk, hogy a készülék nem megfelelő használata miatt balesetek vagy károk nem következhetnek be. Kérjük, használja ezt a terméket körültekintően és működtesse a saját felelősségét!
- Eszköz meghibásodása esetén kérjük, húzza ki a tápkábelt. A leggyorsabb módszer erre az, ha a hálózati csatlakozót kihúzza a konnektorból.
Gyártó: Mikrotikls SIA, Unijas iela 2, Riga, Lettország, LV1039.

## IT - Italiano. Guida veloce

:::warning
Questo dispositivo deve essere aggiornato a RouterOS v7.12 o all'ultima versione del software per garantire la conformità con le normative delle autorità locali!
È responsabilità dell'utente finale seguire le normative locali locali. Tutti i dispositivi MikroTik devono essere installato professionalmente.
Questa guida rapida copre il modello: CRS310-1G-5S-4S+OUT.
:::

*Questo è il dispositivo di rete. È possibile trovare il nome del modello del prodotto sull'etichetta della custodia (ID).*
*Visitare la pagina del manuale dell'utente su [https://mt.lv/um-it](https://mt.lv/um-it) per il manuale utente completamente aggiornato. Oppure scansiona il codice QR con il tuo cellulare.*
*Le specifiche tecniche più importanti per questo prodotto si trovano nell'ultima pagina di questa Guida rapida.*
*Specifiche tecniche, dichiarazione di conformità UE completa, brochure e ulteriori informazioni sui prodotti su [https://mikrotik.com/products](https://mikrotik.com/products)*
*Il manuale di configurazione del software nella tua lingua con informazioni aggiuntive è disponibile all'indirizzo [https://mt.lv/help-it](https://mt.lv/help-it)*
*I dispositivi MikroTik sono per uso professionale. Se non si dispone di qualifiche, consultare un consulente [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-11-13.badge-95.png)

**Primi passi:**

- Connettiti con il tuo computer al dispositivo;
- Scarica lo strumento di configurazione [https://mt.lv/winbox](https://mt.lv/winbox);
- Apri la scheda *Neighbors* e connettiti al dispositivo utilizzando l'indirizzo MAC;
- Il nome utente: *admin*, per impostazione predefinita non esiste una password (oppure, per alcuni modelli, verificare utente e password wireless sull'adesivo);
- Per aggiornare il dispositivo all'ultima versione del software, scaricare l'ultimo software RouterOS da https://mikrotik.com/download;
- Scegli i pacchetti ARM e salvali sul tuo computer;
- Ritorna su WinBox e carica i pacchetti scaricati;
- Riavvia il dispositivo.

**Informazioni sulla sicurezza:**

- Prima di lavorare su qualsiasi apparecchiatura MikroTik, prestare attenzione ai pericoli connessi con i circuiti elettrici e conoscere le pratiche standard per la prevenzione degli incidenti. Il programma di installazione dovrebbe avere familiarità con le strutture, i termini e i concetti della rete.
- Utilizzare solo l'alimentatore e gli accessori approvati dal produttore e che si trovano nella confezione originale di questo prodotto.
- Questa apparecchiatura deve essere installata da personale addestrato e qualificato, secondo queste istruzioni di installazione. L'installatore è responsabile di assicurarsi che l'installazione dell'apparecchiatura sia conforme ai codici elettrici locali e nazionali. Non tentare di smontare, riparare o modificare il dispositivo.
- Questo prodotto può essere utilizzato sia all'interno che all'esterno. Si prega di leggere attentamente le istruzioni di montaggio prima di iniziare l'installazione. Il mancato utilizzo dell'hardware e della configurazione corretti o il mancato rispetto delle procedure corrette potrebbe comportare una situazione pericolosa per le persone e danni al sistema.
- Non possiamo garantire che non si verifichino incidenti o danni dovuti all'uso improprio del dispositivo. Utilizzare questo prodotto con cura e operare a proprio rischio!
- In caso di guasto del dispositivo, scollegarlo dall'alimentazione. Il modo più rapido per farlo è scollegare la spina di alimentazione dalla presa di corrente.
Produttore: Mikrotikls SIA, Unijas iela 2, Riga, Lettonia, LV1039.

## IS - Íslensku. Fljótur leiðarvísir

:::warning
Þetta tæki þarf að uppfæra í RouterOS v7.12 eða nýjustu hugbúnaðarútgáfuna til að tryggja samræmi við reglugerðir sveitarfélaga!
Það er ábyrgð notendanna að fylgja reglugerðum á staðnum. Öll MikroTik tæki verða að vera fagmannlega sett upp.
Þessi snögga leiðbeining nær yfir gerðina: CRS310-1G-5S-4S+OUT.
:::

*Þetta er net tæki. Þú getur fundið heiti vörulíkansins á merkimiðanum (ID).*
*Vinsamlegast farðu á notendahandbókarsíðuna á [https://mt.lv/um-is](https://mt.lv/um-is) fyrir allar uppfærðar notendahandbækur. Eða skannaðu QR kóða með farsímanum þínum.*
*Mikilvægustu tækniforskriftirnar fyrir þessa vöru er að finna á síðustu síðu þessarar hraðhandbókar.*
*Tækniforskriftir, full ESB-samræmisyfirlýsing, bæklingar og frekari upplýsingar um vörur á [https://mikrotik.com/products](https://mikrotik.com/products)*
*Stillingarhandbók fyrir hugbúnað á þínu tungumáli með viðbótarupplýsingum er að finna á [https://mt.lv/help-is](https://mt.lv/help-is)*
*MikroTik tæki eru til atvinnu notkunar. Ef þú ert ekki með hæfi vinsamlegast leitaðu til ráðgjafa [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-12-32.badge-95.png)

**Fyrstu skrefin:**

- Tengdu tölvuna þína við tækið;
- Sæktu stillitólið [https://mt.lv/winbox](https://mt.lv/winbox);
- Opnaðu *Neighbors* og tengdu við tækið með því að nota MAC-tölu;
- Notandanafnið: *admin*, sjálfgefið er ekkert lykilorð (eða, fyrir sumar gerðir, athugaðu notenda- og þráðlaus lykilorð á límmiðanum);
- Til að uppfæra tækið í nýjustu hugbúnaðarútgáfuna skal hlaða nýjasta RouterOS hugbúnaðinum frá https://mikrotik.com/download;
- Veldu ARM pakka og vistaðu þá á tölvunni þinni;
- Fara aftur í WinBox og hlaðið niður niðurhalaða pakka;
- Endurræstu tækið.

**Öryggisupplýsingar:**

- Áður en þú vinnur að einhverjum MikroTik búnaði, vertu meðvitaður um hættuna sem fylgir rafrásum og kynntu þér hefðbundnar venjur til að koma í veg fyrir slys. Uppsetningarforritið ætti að vera kunnugt um netkerfi, hugtök og hugtök.
- Notaðu aðeins aflgjafa og fylgihluti sem framleiðandi hefur samþykkt og er að finna í upprunalegum umbúðum þessarar vöru.
- Þessum búnaði skal setja upp af þjálfuðu og hæfu starfsfólki samkvæmt þessum uppsetningarleiðbeiningum. Uppsetningaraðilinn ber ábyrgð á því að uppsetning búnaðarins sé í samræmi við staðbundin og innlend rafmagnsnúmer. Ekki reyna að taka tækið í sundur, gera við eða breyta því.
- Þessa vöru er hægt að nota bæði inni og úti. Vinsamlegast lestu leiðbeiningar um uppsetningu vandlega áður en byrjað er að setja upp. Ef ekki er notaður réttur vélbúnaður og stillingar eða farið eftir réttum aðferðum gæti það valdið hættulegum aðstæðum fyrir fólk og skemmdum á kerfinu.
- Við getum ekki ábyrgst að engin slys eða skemmdir muni verða vegna óviðeigandi notkunar tækisins. Vinsamlegast notaðu þessa vöru með varúð og starfaðu á eigin ábyrgð!
- Ef bilun í tæki, vinsamlegast aftengdu það frá rafmagni. Skjótasta leiðin til þess er með því að taka rafmagnstengið úr sambandi.
Framleiðandi: Mikrotikls SIA, Unijas iela 2, Riga, Lettlandi, LV1039.

## NO - Norsk. Hurtiginnføring

:::warning
Denne enheten må oppgraderes til RouterOS v7.12 eller den nyeste programvareversjonen for å sikre samsvar med lokale myndigheters forskrifter!
Det er sluttbrukernes ansvar å følge lokale lands forskrifter. Alle MikroTik-enheter må være profesjonelt installert.
:::

*Dette er nettverksenhet. Du kan finne produktmodellnavnet på etiketten (ID).*
*Vennligst besøk bruksanvisningen på [https://mt.lv/um-no](https://mt.lv/um-no) for den fulle oppdaterte bruksanvisningen. Eller skann QR-koden med mobiltelefonen din.*
*De viktigste tekniske spesifikasjonene for dette produktet finner du på siste side i denne hurtigveiledningen.*
*Tekniske spesifikasjoner, full EU-samsvarserklæring, brosjyrer og mer informasjon om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurasjonshåndbok for programvare på ditt språk med tilleggsinformasjon finner du på [https://mt.lv/help-no](https://mt.lv/help-no)*
*MikroTik-enheter er til profesjonell bruk. Hvis du ikke har kvalifikasjoner, kan du søke en konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-13-45.badge-95.png)

**Første steg:**

- Koble datamaskinen til enheten.
- Last ned konfigurasjonsverktøyet [https://mt.lv/winbox](https://mt.lv/winbox);
- Åpne *Neighbors* fanen og koble til enheten ved hjelp av MAC-adresse;
- Brukernavnet: *admin*, som standard er det ikke noe passord (eller, for noen modeller, sjekk bruker- og trådløse passord på klistremerket);
- For å oppdatere enheten til den nyeste programvareversjonen d laste ned den nyeste RouterOS-programvaren fra https://mikrotik.com/download;
- Velg ARM-pakker, og lagre dem på datamaskinen din;
- Gå tilbake til WinBox og last opp nedlastede pakker;
- Start enheten på nytt.

**Sikkerhetsinformasjon:**

- Før du jobber med MikroTik-utstyr, må du være oppmerksom på farene som er forbundet med elektriske kretsløp, og kjenne til standard praksis for å forhindre ulykker. Installasjonsprogrammet skal være kjent med nettverksstrukturer, vilkår og konsepter.
- Bruk bare strømforsyningen og tilbehøret som er godkjent av produsenten, og som finnes i originalemballasjen til dette produktet.
- Dette utstyret skal installeres av trent og kvalifisert personell i henhold til denne installasjonsinstruksen. Installatøren er ansvarlig for at installasjonen av utstyret er i samsvar med lokale og nasjonale elektriske koder. Ikke prøv å demontere, reparere eller endre enheten.
- Dette produktet kan brukes både innendørs og utendørs. Les monteringsinstruksjonene nøye før du begynner å installere. Unnlatelse av å bruke riktig maskinvare og konfigurasjon eller å følge de riktige prosedyrene kan føre til en farlig situasjon for mennesker og skade på systemet.
- Vi kan ikke garantere at ingen ulykker eller skader vil oppstå på grunn av feil bruk av enheten. Bruk dette produktet med forsiktighet og bruk det på egen risiko!
- Ved feil på enheten må du koble den fra strømmen. Den raskeste måten å gjøre det på er ved å trekke støpselet ut av stikkontakten.
Produsent: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## LT - Lietuvis. Trumpas vadovas

:::warning
Šis įrenginys turi būti atnaujintas iki RouterOS v7.12 arba naujausios programinės įrangos versijos, kad būtų laikomasi vietos valdžios taisyklių!
Galutiniai vartotojai yra atsakingi už vietinių šalies įstatymų laikymąsi. Visi „MikroTik“ prietaisai turi būti profesionaliai sumontuota.
Šis trumpasis vadovas apima modelį: CRS310-1G-5S-4S+OUT.
:::

*Tai yra tinklo įrenginys. Produkto modelio pavadinimą galite rasti dėklo etiketėje (ID).*
*Norėdami gauti išsamesnį vartotojo vadovą, apsilankykite vartotojo vadovo puslapyje [https://mt.lv/um-lt](https://mt.lv/um-lt). Arba nuskaitykite QR kodą savo mobiliuoju telefonu.*
*Svarbiausias šio gaminio technines specifikacijas galite rasti paskutiniame šio greito vadovo puslapyje.*
*Techninės specifikacijos, visa ES atitikties deklaracija, brošiūros ir daugiau informacijos apie gaminius adresu [https://mikrotik.com/products](https://mikrotik.com/products)*
*Programinės įrangos jūsų kalba konfigūravimo vadovą su papildoma informacija galite rasti tinklalapyje [https://mt.lv/help-lt](https://mt.lv/help-lt)*
*„MikroTik“ prietaisai yra skirti profesionaliam naudojimui. Jei neturite kvalifikacijos, kreipkitės į konsultantą [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-15-30.badge-94.png)

**Pirmieji žingsniai:**

- Prijunkite savo kompiuterį prie įrenginio;
- Atsisiųskite konfigūravimo įrankį [https://mt.lv/winbox](https://mt.lv/winbox);
- Atidarykite skirtuką *Neighbors* ir prisijunkite prie įrenginio naudodami MAC adresą;
- Vartotojo vardas: *admin*, pagal nutylėjimą slaptažodžio nėra (arba, kai kuriuose modeliuose, patikrinkite vartotojo ir belaidžio ryšio slaptažodžius ant lipduko);
- Norėdami atnaujinti įrenginį į naujausią programinės įrangos versiją, atsisiųskite naujausią „RouterOS“ programinę įrangą iš https://mikrotik.com/download;
- Pasirinkite ARM paketus ir išsaugokite juos savo kompiuteryje;
- Grįžkite į „WinBox“ ir įkelkite atsisiųstus paketus;
- Iš naujo paleiskite įrenginį.

**Saugumo informacija:**

- Prieš pradėdami dirbti su bet kuria „MikroTik“ įranga, žinokite apie pavojus, susijusius su elektros grandinėmis, ir susipažinkite su standartine avarijų prevencijos praktika. Montuotojas turėtų būti susipažinęs su tinklo struktūromis, terminais ir sąvokomis.
- Naudokite tik gamintojo patvirtintus maitinimo šaltinius ir priedus, kuriuos galite rasti originalioje šio gaminio pakuotėje.
- Šią įrangą turi montuoti apmokyti ir kvalifikuoti darbuotojai, kaip numatyta šiose montavimo instrukcijose. Montuotojas yra atsakingas už tai, kad įranga būtų montuojama laikantis vietinių ir nacionalinių elektros taisyklių. Nemėginkite išardyti, taisyti ar modifikuoti įrenginio.
- Šis produktas gali būti naudojamas tiek viduje, tiek lauke. Prieš pradėdami diegimą, atidžiai perskaitykite montavimo instrukcijas. Jei nenaudosite tinkamos aparatūros ir konfigūracijos arba nesilaikysite teisingų procedūrų, žmonėms gali kilti pavojinga situacija ir sugadinti sistemą.
- Mes negalime garantuoti, kad dėl netinkamo prietaiso naudojimo nebus jokių avarijų ar žalos. Naudokite šį gaminį atsargiai ir dirbkite savo rizika!
- Sugedus įrenginiui, atjunkite jį nuo maitinimo. Greičiausias būdas tai padaryti yra atjungus maitinimo kištuką nuo maitinimo lizdo.
Gamintojas: Mikrotikls SIA, Unijas iela 2, Ryga, Latvija, LV1039.

## LV - Latviešu. Īsa rokasgrāmata

:::warning
Šī ierīce ir jāatjaunina uz RouterOS v7.12 vai uz jaunāko programmatūras versiju, lai nodrošinātu atbilstību vietējās varas normatīviem!
Gala lietotāju pienākums ir ievērot vietējos valsts normatīvus. Visām MikroTik ierīcēm jābūt profesionāli uzstādītām.
Šī īsā rokasgrāmata attiecas uz modeli: CRS310-1G-5S-4S+OUT.
:::

*Šī ir tīkla ierīce. Produkta modeļa nosaukumu varat atrast uz produkta iepakojuma (ID).*
*Lūdzu, apmeklējiet lietotāja rokasgrāmatas lapu [https://mt.lv/um-lv](https://mt.lv/um-lv), lai iegūtu pilnīgu un atjauninātu lietotāja rokasgrāmatu. Vai arī skenējiet QR kodu ar savu mobilo tālruni.*
*Vissvarīgākās šī produkta tehniskās specifikācijas ir atrodamas šīs ātrās rokasgrāmatas pēdējā lappusē.*
*Tehniskās specifikācijas, pilna ES atbilstības deklarācija, brošūras un vairāk informācijas par produktiem vietnē [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurācijas rokasgrāmata programmatūrai jūsu valodā ar papildu informāciju atrodama vietnē [https://mt.lv/help-lv](https://mt.lv/help-lv)*
*MikroTik ierīces ir paredzētas profesionālai lietošanai. Ja jums nav kvalifikācijas, lūdzu, meklējiet konsultanta palīdzību [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-18-11.badge-95.png)

**Pirmie soļi:**

- Savienojiet ierīci ar datoru;
- Lejupielādējiet konfigurācijas rīku [https://mt.lv/winbox](https://mt.lv/winbox);
- Atveriet to un cilnē *Neighbors* izveidojiet savienojumu ar ierīci, izmantojot MAC adresi;
- Lietotājvārds: *admin*, pēc noklusējuma nav paroles (vai atsevišķiem modeļiem pārbaudiet uz uzlīmes norādītās lietotāja un bezvadu paroles);
- Lai atjauninātu ierīci uz jaunāko programmatūras versiju, lejupielādējiet jaunāko RouterOS programmatūru no https://mikrotik.com/download;
- Izvēlieties ARM pakas un saglabājiet tās datorā;
- Atgriezieties WinBox un augšupielādējiet lejupielādētās paketes;
- Restartējiet ierīci.

**Drošības informācija:**

- Pirms sākat strādāt ar jebkuru MikroTik aprīkojumu, iepazīstieties ar briesmām, kas saistītas ar elektriskajām shēmām, un iepazīstieties ar standarta praksi negadījumu novēršanā. Instalētājam jāzina tīkla struktūras, termini un koncepcijas.
- Izmantojiet tikai ražotāja apstiprinātu barošanas kabeli un piederumus, kas atrodami šī produkta oriģinālajā iepakojumā.
- Saskaņā ar šīm uzstādīšanas instrukcijām šo aprīkojumu jāuzstāda apmācītam un kvalificētam personālam. Instalētāja pienākums ir pārliecināties, ka iekārtas uzstādīšana atbilst vietējiem un nacionālajiem elektriskajiem noteikumiem. Nemēģiniet ierīci izjaukt, labot vai pārveidot.
- Šo produktu var izmantot gan telpās, gan ārpus tām. Pirms uzstādīšanas, lūdzu, uzmanīgi izlasiet montāžas instrukciju. Pareizas aparatūras un konfigurācijas neizmantošana vai pareizu procedūru neievērošana var izraisīt cilvēkiem bīstamu situāciju un sistēmas bojājumus.
- Mēs nevaram garantēt, ka ierīces nepareizas lietošanas dēļ negadījumi vai bojājumi nenotiks. Lūdzu, izmantojiet šo produktu uzmanīgi un rīkojieties uz savu risku!
- Ierīces kļūmes gadījumā, lūdzu, atvienojiet to no strāvas. Ātrākais veids, kā to izdarīt, ir, atvienojot strāvas spraudni no kontaktligzdas.
Ražotājs: Mikrotikls SIA, Unijas iela 2, Rīga, Latvija, LV1039.

## MT - Malti. Gwida Quick

:::warning
Dan l-apparat jeħtieġ li jiġi aġġornat għal RouterOS v7.12 jew l-aħħar verżjoni tas-softwer biex tiġi żgurata l-konformità mar-regolamenti tal-awtorità lokali!
Hija r-responsabbiltà tal-utenti finali li jsegwu r-regolamenti lokali tal-pajjiż. L-apparati kollha MikroTik iridu jkunu installati professjonalment.
Din il-Gwida Quick tkopri l-mudell: CRS310-1G-5S-4S+OUT.
:::

*Dan huwa apparat tan-netwerk. Tista 'ssib l-isem tal-mudell tal-prodott fuq it-tikketta tal-każ (ID).*
*Jekk jogħġbok żur il-paġna manwal tal-utent fuq [https://mt.lv/um-mt](https://mt.lv/um-mt) għall-manwal aġġornat tal-utent. Jew skennja l-kodiċi QR bit-telefon ċellulari tiegħek.*
*L-iktar speċifikazzjonijiet tekniċi importanti għal dan il-prodott jistgħu jinstabu fl-aħħar paġna ta 'din il-Gwida ta' Ħeffa.*
*Speċifikazzjonijiet tekniċi, Dikjarazzjoni Sħiħa ta' Konformità tal-UE, fuljetti, u aktar informazzjoni dwar il-prodotti fuq [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manwal ta 'konfigurazzjoni għas-softwer fil-lingwa tiegħek b'informazzjoni addizzjonali jista' jinstab fuq [https://mt.lv/help-mt](https://mt.lv/help-mt)*
*L-apparat MikroTik huwa għal użu professjonali. Jekk m'għandekx kwalifiki jekk jogħġbok fittex konsulent [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-20-59.badge-95.png)

**L-ewwel passi:**

- Qabbad mal-kompjuter tiegħek mal-apparat;
- Niżżel l-għodda ta 'konfigurazzjoni [https://mt.lv/winbox](https://mt.lv/winbox);
- Iftaħ it-tab *Neighbors* u qabbad mat-tagħmir billi tuża l-indirizz MAC;
- L -isem tal-utent: *admin*, b'default m'hemm l-ebda password (jew, għal xi mudelli, iċċekkja l-passwords tal-utent u mingħajr fili fuq l-istiker);
- Biex taġġorna l-apparat għall-aħħar verżjoni tas-softwer li dloadload l-aħħar software RouterOS minn https://mikrotik.com/download;
- Agħżel il-pakketti ARM, u ssalvahom fuq il-kompjuter tiegħek;
- Irritorna lejn il-WinBox u ttella 'pakketti mniżżla;
- Irristartja l-apparat.

**Informazzjoni dwar is-Sikurezza:**

- Qabel ma taħdem fuq kwalunkwe tagħmir MikroTik, kun konxju tal-perikli involuti fiċ-ċirkwiti elettriċi u kun familjari mal-prattiki standard għall-prevenzjoni ta 'inċidenti. L-installatur għandu jkun familjari mal-istrutturi, termini u kunċetti tan-netwerk.
- Uża biss il-provvista tal-enerġija u l-aċċessorji approvati mill-manifattur, u li tista 'tinstab fl-imballaġġ oriġinali ta' dan il-prodott.
- Dan it-tagħmir għandu jkun installat minn persunal imħarreġ u kwalifikat, skond dawn l-istruzzjonijiet ta 'installazzjoni. L-installatur huwa responsabbli li jiżgura li l-Installazzjoni tat-tagħmir hija konformi mal-kodiċijiet elettriċi lokali u nazzjonali. Tippruvax tiżżarma, tissewwa jew timmodifika l-apparat.
- Dan il-prodott jista 'jintuża kemm ġewwa kif ukoll barra. Jekk jogħġbok aqra sew l-istruzzjonijiet tal-immuntar qabel tibda l-installazzjoni. Nuqqas li tuża l-hardware u l-konfigurazzjoni korretti jew li ssegwi l-proċeduri korretti jista 'jirriżulta f'sitwazzjoni perikoluża għan-nies u ħsara lis-sistema.
- Ma nistgħux niggarantixxu li ma jseħħ l-ebda inċident jew ħsara minħabba l-użu mhux xieraq tal-apparat. Jekk jogħġbok uża dan il-prodott b'attenzjoni u tħaddem għar-riskju tiegħek!
- Fil-każ ta 'ħsara fl-apparat, jekk jogħġbok aqla' mill-enerġija. L-iktar mod mgħaġġel biex tagħmel dan huwa billi tiftaħ il-plagg tal-qawwa mill-iżbokk tad-dawl.
Manifattur: Mikrotikls SIA, Unijas iela 2, Riga, il-Latvja, LV1039.

## NL - Nederlands. Snelgids

:::warning
Dit apparaat moet worden geüpgraded naar RouterOS v7.12 of de nieuwste softwareversie om te voldoen aan de voorschriften van de plaatselijke autoriteiten!
Het is de verantwoordelijkheid van de eindgebruiker om de lokale landelijke voorschriften. Alle MikroTik-apparatuur moet zijn professioneel geïnstalleerd.
:::

*Dit is een netwerkapparaat. U kunt de naam van het productmodel vinden op het etiket van de behuizing (ID).*
*Ga naar de gebruikerspagina op [https://mt.lv/um-nl](https://mt.lv/um-nl) voor de volledige bijgewerkte gebruikershandleiding. Of scan de QR-code met uw mobiele telefoon.*
*De belangrijkste technische specificaties van dit product vindt u op de laatste pagina van deze Quick Guide.*
*Technische specificaties, volledige EU-conformiteitsverklaring, brochures en meer informatie over producten op [https://mikrotik.com/products](https://mikrotik.com/products)*
*Configuratiehandleiding voor software in uw taal met aanvullende informatie is te vinden op [https://mt.lv/help-nl](https://mt.lv/help-nl)*
*MikroTik-apparaten zijn voor professioneel gebruik. Als u geen kwalificaties hebt, zoek dan een consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-22-25.badge-95.png)

**Eerste stappen:**

- Maak verbinding met uw computer naar het apparaat;
- Download de configuratietool [https://mt.lv/winbox](https://mt.lv/winbox);
- Open het tabblad *Neighbors* en maak verbinding met het apparaat via het MAC-adres;
- De gebruikersnaam: *admin*, standaard is er geen wachtwoord (of controleer bij sommige modellen de gebruikers- en draadloze wachtwoorden op de sticker);
- Om het apparaat bij te werken naar de nieuwste softwareversie, moet u de nieuwste RouterOS-software downloaden van https://mikrotik.com/download;
- Kies ARM-pakketten en sla ze op uw computer op;
- Keer terug naar de WinBox en upload gedownloade pakketten;
- Start het apparaat opnieuw op.

**Veiligheidsinformatie:**

- Voordat u aan MikroTik-apparatuur werkt, moet u zich bewust zijn van de gevaren van elektrische circuits en bekend zijn met standaardprocedures om ongevallen te voorkomen. Het installatieprogramma moet bekend zijn met netwerkstructuren, termen en concepten.
- Gebruik alleen de voeding en accessoires die door de fabrikant zijn goedgekeurd en die zich in de originele verpakking van dit product bevinden.
- Deze apparatuur moet worden geïnstalleerd door opgeleid en gekwalificeerd personeel, volgens deze installatie-instructies. De installateur moet ervoor zorgen dat de installatie van de apparatuur voldoet aan de lokale en nationale elektrische voorschriften. Probeer het apparaat niet uit elkaar te halen, te repareren of aan te passen.
- Dit product kan zowel binnen als buiten worden gebruikt. Lees de montage-instructies zorgvuldig door voordat u met de installatie begint. Het niet gebruiken van de juiste hardware en configuratie of het niet volgen van de juiste procedures kan leiden tot een gevaarlijke situatie voor mensen en schade aan het systeem.
- We kunnen niet garanderen dat er geen ongelukken of schade zullen optreden als gevolg van oneigenlijk gebruik van het apparaat. Gebruik dit product met zorg en werk op eigen risico!
- Koppel het apparaat los van de stroom in het geval van een apparaatstoring. De snelste manier om dit te doen, is door de stekker uit het stopcontact te halen.
Fabrikant: Mikrotikls SIA, Unijas iela 2, Riga, Letland, LV1039.

## PL - Polskie. Szybka porada

:::warning
To urządzenie wymaga aktualizacji do RouterOS v7.12 lub najnowszej wersji oprogramowania, aby zapewnić zgodność z przepisami władz lokalnych!
Użytkownicy końcowi są zobowiązani do przestrzegania lokalnych przepisów krajowych. Wszystkie urządzenia MikroTik muszą być profesjonalnie zainstalowany.
Niniejszy Krótki przewodnik obejmuje model: CRS310-1G-5S-4S+OUT.
:::

*To jest urządzenie sieciowe. Nazwę modelu produktu można znaleźć na etykiecie skrzynki (ID).*
*Odwiedź stronę instrukcji użytkownika na [https://mt.lv/um-pl](https://mt.lv/um-pl), aby uzyskać pełną aktualną instrukcję obsługi. Lub zeskanuj kod QR za pomocą telefonu komórkowego.*
*Najważniejsze dane techniczne tego produktu można znaleźć na ostatniej stronie tego skróconego przewodnika.*
*Specyfikacje techniczne, pełna deklaracja zgodności UE, broszury i więcej informacji o produktach na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Podręcznik konfiguracji oprogramowania w Twoim języku z dodatkowymi informacjami można znaleźć na stronie [https://mt.lv/help-pl](https://mt.lv/help-pl)*
*Urządzenia MikroTik są przeznaczone do użytku profesjonalnego. Jeśli nie masz kwalifikacji, poszukaj konsultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-39-6.badge-95.png)

**Pierwsze kroki:**

- Połącz się z komputerem do urządzenia;
- Pobierz narzędzie konfiguracyjne [https://mt.lv/winbox](https://mt.lv/winbox);
- Otwórz kartę *Neighbors* i połącz się z urządzeniem za pomocą adresu MAC;
- Nazwa użytkownika: *admin*, domyślnie nie ma hasła (lub, w przypadku niektórych modeli, sprawdzić hasła użytkownika i sieci bezprzewodowej na naklejce);
- Aby zaktualizować urządzenie do najnowszej wersji oprogramowania, pobierz najnowszą wersję oprogramowania RouterOS ze strony https://mikrotik.com/download;
- Wybierz pakiety ARM i zapisz je na swoim komputerze;
- Wróć do WinBox i prześlij pobrane pakiety;
- Uruchom ponownie urządzenie.

**Informacje dotyczące bezpieczeństwa:**

- Przed rozpoczęciem pracy z jakimkolwiek sprzętem MikroTik należy pamiętać o zagrożeniach związanych z obwodami elektrycznymi i zapoznać się ze standardowymi praktykami zapobiegania wypadkom. Instalator powinien zapoznać się ze strukturami sieci, terminami i koncepcjami.
- Używaj wyłącznie zasilacza i akcesoriów zatwierdzonych przez producenta, które znajdują się w oryginalnym opakowaniu tego produktu.
- To urządzenie powinno być zainstalowane przez przeszkolony i wykwalifikowany personel zgodnie z niniejszą instrukcją instalacji. Instalator jest odpowiedzialny za upewnienie się, że instalacja urządzenia jest zgodna z lokalnymi i krajowymi przepisami elektrycznymi. Nie należy podejmować prób demontażu, naprawy ani modyfikacji urządzenia.
- Ten produkt może być używany zarówno wewnątrz, jak i na zewnątrz. Przed rozpoczęciem instalacji prosimy o dokładne zapoznanie się z instrukcją montażu. Niezastosowanie prawidłowego sprzętu i konfiguracji lub nieprzestrzeganie prawidłowych procedur może skutkować niebezpieczną sytuacją dla ludzi i uszkodzeniem systemu.
- Nie możemy zagwarantować, że nie dojdzie do wypadków ani szkód spowodowanych niewłaściwym użytkowaniem urządzenia. Proszę używać tego produktu ostrożnie i działać na własne ryzyko!
- W przypadku awarii urządzenia odłącz je od zasilania. Najszybszym sposobem na to jest wyciągnięcie wtyczki z gniazdka.
Producent: Mikrotikls SIA, Unijas iela 2, Riga, Łotwa, LV1039.

## PT - Português. Guia rápido

:::warning
Este dispositivo precisa ser atualizado para o RouterOS v7.12 ou a versão de software mais recente para garantir a conformidade com os regulamentos das autoridades locais!
É responsabilidade do usuário final seguir as regulamentações locais do país. Todos os dispositivos de MikroTik devem ser instalado profissionalmente.
Este Guia Rápido cobre o modelo: CRS310-1G-5S-4S+OUT.
:::

*Este é o dispositivo de rede. Você pode encontrar o nome do modelo do produto no rótulo da caixa (ID).*
*Visite a página do manual do usuário em [https://mt.lv/um-pt](https://mt.lv/um-pt) para obter o manual do usuário completo e atualizado. Ou digitalize o código QR com seu telefone celular.*
*As especificações técnicas mais importantes para este produto podem ser encontradas na última página deste Guia Rápido.*
*Especificações técnicas, Declaração de conformidade completa da UE, folhetos e mais informações sobre produtos em [https://mikrotik.com/products](https://mikrotik.com/products)*
*O manual de configuração do software em seu idioma com informações adicionais pode ser encontrado em [https://mt.lv/help-pt](https://mt.lv/help-pt)*
*Os dispositivos MikroTik são para uso profissional. Se você não possui qualificações, procure um consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-40-42.badge-95.png)

**Primeiros passos:**

- Conecte-se ao seu computador no dispositivo;
- Faça o download da ferramenta de configuração [https://mt.lv/winbox](https://mt.lv/winbox);
- Abra a guia *Neighbors* e conecte-se ao dispositivo usando o endereço MAC;
- O nome de usuário: *admin*, por padrão, não há senha (ou, em alguns modelos, verifique as palavras-passe de utilizador e sem fios no autocolante);
- Para atualizar o dispositivo para a versão mais recente do software, faça o download do software RouterOS mais recente em https://mikrotik.com/download;
- Escolha pacotes ARM e salve-os no seu computador;
- Retorne ao WinBox e faça o upload dos pacotes baixados;
- Reinicie o dispositivo.

**Informação de Segurança:**

- Antes de trabalhar em qualquer equipamento MikroTik, esteja ciente dos riscos envolvidos nos circuitos elétricos e esteja familiarizado com as práticas padrão para prevenção de acidentes. O instalador deve estar familiarizado com estruturas, termos e conceitos de rede.
- Use apenas a fonte de alimentação e os acessórios aprovados pelo fabricante e que podem ser encontrados na embalagem original deste produto.
- Este equipamento deve ser instalado por pessoal treinado e qualificado, de acordo com estas instruções de instalação. O instalador é responsável por garantir que a instalação do equipamento esteja em conformidade com os códigos elétricos locais e nacionais. Não tente desmontar, reparar ou modificar o dispositivo.
- Este produto pode ser usado tanto em ambientes internos quanto externos. Leia as instruções de montagem cuidadosamente antes de iniciar a instalação. A falha em usar o hardware e a configuração corretos ou em seguir os procedimentos corretos pode resultar em uma situação perigosa para as pessoas e danos ao sistema.
- Não podemos garantir que nenhum acidente ou dano ocorra devido ao uso inadequado do dispositivo. Por favor, use este produto com cuidado e opere por sua conta e risco!
- No caso de falha do dispositivo, desconecte-o da energia. A maneira mais rápida de fazer isso é desconectando o plugue da tomada.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, Letônia, LV1039.

## RO - Română. Ghid rapid

:::warning
Acest dispozitiv trebuie să fie actualizat la RouterOS v7.12 sau la cea mai recentă versiune de software pentru a asigura conformitatea cu reglementările autorităților locale!
Este responsabilitatea utilizatorilor finali să urmeze reglementările locale ale țării. Toate dispozitivele MikroTik trebuie să fie instalat profesional.
Acest Ghid rapid acoperă modelul: CRS310-1G-5S-4S+OUT.
:::

*Acesta este dispozitivul de rețea. Puteți găsi numele modelului produsului pe eticheta carcasei (ID).*
*Vă rugăm să vizitați pagina manualului utilizatorului de pe [https://mt.lv/um-ro](https://mt.lv/um-ro) pentru manualul complet actualizat. Sau scanează codul QR cu telefonul tău mobil.*
*Cele mai importante specificații tehnice pentru acest produs pot fi găsite pe ultima pagină a acestui Ghid rapid.*
*Specificații tehnice, Declarație de conformitate UE completă, broșuri și mai multe informații despre produse la [https://mikrotik.com/products](https://mikrotik.com/products)*
*Manualul de configurare pentru software-ul în limba dvs. cu informații suplimentare poate fi găsit la [https://mt.lv/help-ro](https://mt.lv/help-ro)*
*Dispozitivele MikroTik sunt destinate utilizării profesionale. Dacă nu aveți calificări, vă rugăm să căutați un consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-42-33.badge-93.png)

**Primii pasi:**

- Conectați-vă cu computerul la dispozitiv;
- Descărcați instrumentul de configurare [https://mt.lv/winbox](https://mt.lv/winbox);
- Deschideți fila *Neighbors* și conectați-vă la dispozitiv folosind adresa MAC;
- Numele de utilizator: *admin*, implicit nu există parolă (sau, pentru unele modele, verificați parolele de utilizator și fără fir de pe autocolant);
- Pentru a actualiza dispozitivul la cea mai recentă versiune de software, descărcați cel mai recent software RouterOS de la https://mikrotik.com/download;
- Alegeți pachetele ARM și salvați-le pe computer;
- Reveniți la WinBox și încărcați pachetele descărcate;
- Reporniți dispozitivul.

**Informații de siguranță:**

- Înainte de a lucra la orice echipament MikroTik, fiți conștienți de pericolele implicate de circuitele electrice și cunoașteți practicile standard pentru prevenirea accidentelor. Programul de instalare ar trebui să fie familiarizat cu structurile, termenii și conceptele rețelei.
- Folosiți numai sursa de alimentare și accesoriile aprobate de producător și care pot fi găsite în ambalajul original al acestui produs.
- Acest echipament va fi instalat de personal instruit și calificat, conform acestor instrucțiuni de instalare. Instalatorul este responsabil să se asigure că Instalarea echipamentului respectă codurile electrice locale și naționale. Nu încercați să dezasamblați, reparați sau modificați dispozitivul.
- Acest produs poate fi utilizat atât în interior, cât și în exterior. Vă rugăm să citiți cu atenție instrucțiunile de montare înainte de a începe instalarea. Neutilizarea hardware-ului și a configurației corecte sau a respectării procedurilor corecte ar putea duce la o situație periculoasă pentru oameni și la deteriorarea sistemului.
- Nu putem garanta că nu se vor produce accidente sau daune din cauza utilizării necorespunzătoare a dispozitivului. Vă rugăm să utilizați acest produs cu grijă și să operați pe riscul dvs.!
- În cazul unei defecțiuni a dispozitivului, vă rugăm să îl deconectați de la alimentare. Cel mai rapid mod de a face acest lucru este prin a deconecta mufa de la priză.
Producător: Mikrotikls SIA, Unijas iela 2, Riga, Letonia, LV1039.

## SK - Slovenský. Stručný návod

:::warning
Toto zariadenie je potrebné aktualizovať na RouterOS v7.12 alebo najnovšiu verziu softvéru, aby sa zabezpečil súlad s predpismi miestnych úradov!
Je na koncových užívateľoch, aby dodržiavali miestne predpisy krajiny. Všetky zariadenia MikroTik musia byť profesionálne nainštalovaný.
Táto Stručná príručka sa týka modelu: CRS310-1G-5S-4S+OUT.
:::

*Toto je sieťové zariadenie. Názov modelu produktu nájdete na štítku prípadu (ID).*
*Úplnú aktualizovanú používateľskú príručku nájdete nastránke používateľskej príručky na adrese [https://mt.lv/um-sk](https://mt.lv/um-sk). Alebo naskenujte QR kód pomocou mobilného telefónu.*
*Najdôležitejšie technické špecifikácie tohto produktu nájdete na poslednej stránke tohto stručného sprievodcu.*
*Technické špecifikácie, úplné EÚ vyhlásenie o zhode, brožúry a ďalšie informácie o produktoch na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfiguračnú príručku pre softvér vo vašom jazyku s ďalšími informáciami nájdete na [https://mt.lv/help-sk](https://mt.lv/help-sk)*
*Zariadenia MikroTik sú určené pre profesionálne použitie. Ak nemáte kvalifikáciu, obráťte sa na konzultanta [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-44-55.badge-95.png)

**Prvé kroky:**

- Spojte sa s počítačom so zariadením;
- Stiahnite si konfiguračný nástroj [https://mt.lv/winbox](https://mt.lv/winbox);
- Otvorte kartu *Neighbors* a pripojte sa k zariadeniu pomocou adresy MAC;
- Používateľské meno: *admin*, v predvolenom nastavení nie je žiadne heslo (alebo v prípade niektorých modelov skontrolujte používateľské a bezdrôtové heslá na nálepke);
- Ak chcete aktualizovať zariadenie na najnovšiu verziu softvéru, stiahnite si najnovší softvér RouterOS z adresy https://mikrotik.com/download;
- Vyberte si balíčky ARM a uložte ich do svojho počítača;
- Vráťte sa do WinBoxu a nahrajte stiahnuté balíčky;
- Reštartujte zariadenie.

**Bezpečnostné informácie:**

- Predtým, ako začnete pracovať na akomkoľvek zariadení MikroTik, uvedomte si riziká spojené s elektrickými obvodmi a zoznámte sa so štandardnými postupmi prevencie nehôd. Inštalátor by mal byť oboznámený so sieťovými štruktúrami, pojmami a konceptmi.
- Používajte iba napájací zdroj a príslušenstvo schválené výrobcom, ktoré nájdete v pôvodnom obale tohto produktu.
- Toto zariadenie musí inštalovať školený a kvalifikovaný personál podľa týchto pokynov na inštaláciu. Inštalatér je zodpovedný za zabezpečenie toho, aby inštalácia zariadenia bola v súlade s miestnymi a národnými elektrickými predpismi. Nepokúšajte sa zariadenie rozoberať, opravovať alebo upravovať.
- Tento výrobok je možné používať v interiéroch aj exteriéroch. Pred začatím inštalácie si pozorne prečítajte montážne pokyny. Ak nepoužijete správny hardvér a konfiguráciu alebo nedodržíte správne postupy, môže to viesť k nebezpečnej situácii pre ľudí a poškodeniu systému.
- Nemôžeme zaručiť, že v dôsledku nesprávneho použitia zariadenia nedôjde k žiadnym nehodám alebo škodám. Tento výrobok používajte opatrne a pracujte na svoje vlastné riziko!
- V prípade poruchy zariadenia ho prosím odpojte od napájania. Najrýchlejším spôsobom je odpojenie sieťovej zástrčky zo zásuvky.
Výrobca: Mikrotikls SIA, Unijas iela 2, Riga, Lotyšsko, LV1039.

## SL - Slovenščina. Hitri vodnik

:::warning
To napravo je treba nadgraditi na RouterOS v7.12 ali najnovejšo različico programske opreme, da zagotovite skladnost s predpisi lokalnih oblasti!
Končni uporabniki so odgovorni za sledenje lokalnim predpisom. Vse naprave MikroTik morajo biti strokovno nameščen.
Ta hitri vodnik zajema model: CRS310-1G-5S-4S+OUT.
:::

*To je omrežna naprava. Ime modela izdelka najdete na nalepki (ID).*
*Za popoln posodobitev uporabniškega priročnika obiščite stran z navodili na strani [https://mt.lv/um-sl](https://mt.lv/um-sl). Ali pa skenirajte QR kodo s svojim mobilnim telefonom.*
*Najpomembnejše tehnične specifikacije za ta izdelek najdete na zadnji strani teh hitrih navodil.*
*Tehnične specifikacije, popolna izjava o skladnosti EU, brošure in več informacij o izdelkih na [https://mikrotik.com/products](https://mikrotik.com/products)*
*Navodila za konfiguracijo programske opreme v vašem jeziku z dodatnimi informacijami najdete na naslovu [https://mt.lv/help-sl](https://mt.lv/help-sl)*
*Naprave MikroTik so namenjene profesionalni uporabi. Če nimate kvalifikacij, poiščite svetovalca [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-46-47.badge-95.png)

**Prvi koraki:**

- Povežite se z računalnikom v napravi;
- Prenesite orodje za konfiguracijo [https://mt.lv/winbox](https://mt.lv/winbox);
- Odprite zavihek *Neighbors* in se z MAC naslovom povežite z napravo;
- Uporabniško ime: *admin*, privzeto ni gesla (pri nekaterih modelih preverite uporabniška in brezžična gesla na nalepki);
- Za posodobitev naprave na najnovejšo različico programske opreme d lastno naložite najnovejšo programsko opremo RouterOS s https://mikrotik.com/download;
- Izberite ARM pakete in jih shranite v računalnik;
- Vrnite se na WinBox in naložite naložene pakete;
- Znova zaženite napravo.

**Varnostne informacije:**

- Pred delom na kateri koli opremi MikroTik bodite pozorni na nevarnosti, povezane z električnim vezjem, in se seznanite s standardnimi praksami za preprečevanje nesreč. Namestitveni program mora biti seznanjen z omrežnimi strukturami, izrazi in koncepti.
- Uporabljajte samo napajalnik in dodatke, ki jih je odobril proizvajalec in ki jih najdete v originalni embalaži tega izdelka.
- To opremo mora vgraditi usposobljeno in usposobljeno osebje v skladu s temi navodili za namestitev. Monter je odgovoren za to, da je namestitev opreme skladna z lokalnimi in državnimi električnimi kodeksi. Naprave ne poskušajte razstaviti, popraviti ali spremeniti.
- Ta izdelek lahko uporabljate tako v zaprtih prostorih kot na prostem. Pred začetkom namestitve natančno preberite navodila za montažo. Če ne uporabite pravilne strojne opreme in konfiguracije ali ne upoštevate pravilnih postopkov, lahko pride do nevarnih razmer za ljudi in poškodbe sistema.
- Ne moremo zagotoviti, da se zaradi nepravilne uporabe naprave ne bo zgodilo nobena nesreča ali škoda. Uporabljajte ta izdelek previdno in delujte na lastno odgovornost!
- V primeru okvare naprave jo izklopite iz napajanja. Najhitreje to storite tako, da iztaknete napajalni kabel iz vtičnice.
Proizvajalec: Mikrotikls SIA, Unijas iela 2, Riga, Latvija, LV1039.

## SV - Svenska. Snabb guide

:::warning
Denna enhet måste uppgraderas till RouterOS v7.12 eller den senaste mjukvaruversionen för att säkerställa överensstämmelse med lokala myndigheters föreskrifter!
Det är slutanvändarnas ansvar att följa lokala landsregler. Alla MikroTik-enheter måste vara professionellt installerat.
:::

*Det här är nätverksenhet. Du hittar produktmodellnamnet på etiketten (ID).*
*Besök användarmanualsidan på [https://mt.lv/um-sv](https://mt.lv/um-sv) för en fullständig uppdaterad användarmanual. Eller skanna QR-koden med din mobiltelefon.*
*De viktigaste tekniska specifikationerna för denna produkt finns på den sista sidan i denna snabbguide.*
*Tekniska specifikationer, fullständig EU-försäkran om överensstämmelse, broschyrer och mer information om produkter på [https://mikrotik.com/products](https://mikrotik.com/products)*
*Konfigurationshandbok för programvara på ditt språk med ytterligare information kan hittas på [https://mt.lv/help-sv](https://mt.lv/help-sv)*
*MikroTik-enheter är för professionellt bruk. Om du inte har behörighet, sök en konsult [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-47-44.badge-95.png)

**Första stegen:**

- Anslut med din dator till enheten;
- Ladda ner konfigurationsverktyget [https://mt.lv/winbox](https://mt.lv/winbox);
- Öppna fliken *Neighbors* och anslut till enheten med MAC-adress;
- Användarnamnet: *admin*, som standard finns det inget lösenord (eller, för vissa modeller, kontrollera användar- och trådlösa lösenord på klistermärket);
- För att uppdatera enheten till den senaste programvaruversionen d ladda ner den senaste routerOS-programvaran från https://mikrotik.com/download;
- Välj ARM-paket och spara dem på din dator;
- Återgå till WinBox och ladda upp nedladdade paket;
- Starta om enheten.

**Säkerhetsinformation:**

- Innan du arbetar med någon MikroTik-utrustning ska du vara medveten om farorna med elektriska kretsar och känna till vanliga metoder för att förebygga olyckor. Installatören bör känna till nätverksstrukturer, termer och koncept.
- Använd endast den strömförsörjning och tillbehör som godkänts av tillverkaren och som finns i originalförpackningen för denna produkt.
- Denna utrustning ska installeras av utbildad och kvalificerad personal enligt dessa installationsinstruktioner. Installatören ansvarar för att installationen av utrustningen överensstämmer med lokala och nationella elektriska koder. Försök inte ta isär, reparera eller modifiera enheten.
- Denna produkt kan användas både inomhus och utomhus. Läs monteringsanvisningarna noga innan installationen påbörjas. Underlåtenhet att använda rätt maskinvara och konfiguration eller att följa rätt procedurer kan leda till en farlig situation för människor och skador på systemet.
- Vi kan inte garantera att inga olyckor eller skador kommer att inträffa på grund av felaktig användning av enheten. Använd denna produkt med försiktighet och använd den på egen risk!
- Vid fel på enheten, koppla bort den från strömmen. Det snabbaste sättet är att koppla ur stickkontakten från eluttaget.
Tillverkare: Mikrotikls SIA, Unijas iela 2, Riga, Lettland, LV1039.

## PRC - 中文. 快速指南

:::warning
本設備需升級至RouterOS v7.12或最新軟件版本，以確保符合當地權威法規！
最终用户有责任遵守当地国家法规。所有 MikroTik 设备都必须经过专业安装。
本快速指南介绍了以下型号：CRS310-1G-5S-4S+OUT。
:::

*这是网络设备。* *您可以在包装箱标签（ID）上找到产品型号名称。*
*请访问[https://mt.lv/um-zh](https://mt.lv/um-zh) 上的用户手册页面，以获取最新的用户手册。 或使用手机扫描QR码。*
*该产品最重要的技术规格可在本快速指南的最后一页找到。*
*技术规格、完整的欧盟符合性声明、手册以及有关产品的更多信息，请访问 [https://mikrotik.com/products](https://mikrotik.com/products)*
*可以在以下位置找到使用您的语言的软件配置手册以及更多信息 [https://mt.lv/help-zh](https://mt.lv/help-zh)*
*MikroTik设备是专业用途。 如果您没有资格，请寻求顾问[https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-49-44.badge-96.png)

**第一步：**

- 将计算机连接到设备；
- 下载配置工具[https://mt.lv/winbox](https://mt.lv/winbox) ；
- 打开“ *Neighbors”* 选项卡，然后使用MAC地址连接到设备；
- 用户名 *admin* ，默认情况下没有密码 (或者，对于某些型号，检查贴纸上的用户和无线密码）；
- 要将设备更新到最新的软件版本 ， 请从https://mikrotik.com/download 拥有最新的RouterOS软件；
- 选择ARM软件包，并将其保存到您的计算机中；
- 返回WinBox并上传下载的软件包；
- 重新启动设备。

**安全信息：**

- 在使用任何MikroTik设备之前，请注意电路所涉及的危险，并熟悉防止事故的标准做法。 安装程序应熟悉网络结构，术语和概念。
- 仅使用制造商认可的电源和附件，这些电源和附件可在该产品的原始包装中找到。
- 根据这些安装说明，应由经过培训的合格人员来安装本设备。 安装程序负责确保设备的安装符合当地和国家的电气法规。 请勿尝试拆卸，修理或改装设备。
- 本产品可在室内和室外使用。 请在开始安装前仔细阅读安装说明。 不使用正确的硬件和配置或不遵循正确的程序可能会导致人员危险和系统损坏。
- 由于设备使用不当，我们不能保证不会发生任何事故或损坏。 请谨慎使用本产品，风险自负！
- 如果设备发生故障，请断开电源。 最快的方法是从电源插座上拔下电源插头。
制造商：Mikrotikls SIA，拉脱维亚Unijas iela 2, Riga，LV1039。

## RU - Русский. Краткое пособие. Евразийский экономический союз информация

:::warning
Это устройство необходимо обновить до RouterOS v7.12 или последней версии программного обеспечения, чтобы обеспечить соответствие требованиям местных властей!
Конечные пользователи несут ответственность за соблюдение местных нормативов. Все устройства MikroTik должны быть профессионально установлены.
Это краткое руководство охватывает модель: CRS310-1G-5S-4S+OUT.
:::

*Это сетевое устройство. Вы можете найти название модели продукта на ярлыке кейса (ID).*
*Пожалуйста, посетите страницу руководства пользователя на [https://mt.lv/um-ru](https://mt.lv/um-ru), чтобы ознакомиться с полным актуальным руководством пользователя. Или отсканируйте QR-код с помощью мобильного телефона.*
*Наиболее важные технические характеристики этого продукта можно найти на последней странице этого Краткого руководства.*
*Технические характеристики, Полная декларация о соответствии требованиям ЕС, брошюры и дополнительная информация о продуктах на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Руководство по настройке программного обеспечения на вашем языке с дополнительной информацией можно найти по адресу [https://mt.lv/help-ru](https://mt.lv/help-ru)*
*Устройства MikroTik предназначены для профессионального использования. Если у вас нет квалификации, пожалуйста, обратитесь к консультанту [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-94.png)

**Первые шаги:**

- Подключиться с помощью компьютера к устройству;
- Загрузите инструмент настройки [https://mt.lv/winbox](https://mt.lv/winbox);
- Откройте вкладку « *Neighbors* » и подключитесь к устройству по MAC-адресу;
- Имя пользователя: *admin*, по умолчанию пароль отсутствует (или, для некоторых моделей, проверьте пароли пользователя и беспроводной связи на наклейке);
- Чтобы обновить устройство до последней версии программного обеспечения, загрузите последнюю версию программного обеспечения RouterOS с https://mikrotik.com/download;
- Выберите пакеты ARM и сохраните их на своем компьютере;
- Вернитесь в WinBox и загрузите загруженные пакеты;
- Перезагрузите устройство.

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
Производитель: Mikrotikls SIA, улица Унияс 2, Рига, Латвия, LV1039.

Информация о дате изготовления устройства указана в конце серийного номера на его наклейке через дробь. Первая цифра означает номер года (последняя цифра года), две последующие означают номер недели.

![](./img/image2020-1-24_7-55-5.badge-98.png)

Изготовитель: SIA Mikrotikls, Aizkraukles iela 23, Riga, LV-1006, Латвия, support@mikrotik.com. Сделано в Китае, Латвии или Литве. *Cм. на упаковке.*

Для получения подробных сведений о гарантийном обслуживании обратитесь к продавцу.

Продукты MikroTik, которые поставляются в Евразийский таможенный союз, оцениваются с учетом соответствующих требований и помечены знаком EAC, как показано ниже:

## UA - Українська. Короткий посібник

:::warning
Цей пристрій потрібно оновити до RouterOS версії 7.12 або останньої версії програмного забезпечення, щоб забезпечити відповідність вимогам місцевих органів влади!
Кінцеві користувачі несуть відповідальність за дотримання місцевих правил. Усі пристрої MikroTik повинні бути професійно встановлені.
Цей короткий посібник стосується моделі: CRS310-1G-5S-4S+OUT.
:::

*Це пристрій бездротової мережі. Ви можете знайти назву моделі продукту на етикетці корпусу (ID).*
*Будь ласка, відвідайте сторінку посібника користувача на [https://mt.lv/um-ua](https://mt.lv/um-ua) для повної оновленої посібника користувача. Або скануйте QR-код за допомогою мобільного телефону.*
*Найважливіші технічні характеристики цього виробу можна знайти на останній сторінці цього короткого посібника.*
*Технічні характеристики, повна декларація відповідності ЄС, брошури та додаткова інформація про продукти на [https://mikrotik.com/products](https://mikrotik.com/products)*
*Посібник з налаштування програмного забезпечення на вашій мові з додатковою інформацією можна знайти за посиланням [https://mt.lv/help](https://mt.lv/help)*
*Пристрої MikroTik призначені для професійного використання. Якщо у вас немає кваліфікації, зверніться до консультанта [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-5_9-51-14.badge-94.png)

**Перші кроки:**

- Підключіться з комп'ютером до пристрою;
- Завантажте інструмент налаштування [https://mt.lv/winbox](https://mt.lv/winbox);
- Відкрийте вкладку *Neighbors* та підключіться до пристрою за допомогою MAC-адреси;
- Ім'я користувача: *admin*, за замовчуванням немає пароля (або, для деяких моделей, перевірте паролі користувача та бездротового зв'язку на наклейці);
- Для оновлення пристрою до останньої версії програмного забезпечення d власне завантаження найновішого програмного забезпечення RouterOS з https://mikrotik.com/download;
- Виберіть пакети ARM та збережіть їх на своєму комп’ютері;
- Поверніться до WinBox та завантажте завантажені пакети;
- Перезавантажте пристрій.

**Інформація про безпеку:**

- Перш ніж працювати над будь-яким обладнанням MikroTik, пам’ятайте про небезпеки, пов'язані з електричною схемою, та ознайомтеся зі стандартними методами запобігання аварій. Інсталятор повинен бути знайомий з мережевими структурами, термінами та поняттями.
- Використовуйте тільки джерело живлення та аксесуари, затверджені виробником, і які можна знайти в оригінальній упаковці цього виробу.
- Це обладнання має встановлювати навчений та кваліфікований персонал відповідно до цих інструкцій зі встановлення. Особа, що виконує роботи зі встановлення устаткування несе відповідальність за те, щоб встановлення обладнання відповідало місцевим і національним електричним нормам. Не намагайтеся розібрати, відремонтувати чи модифікувати пристрій.
- Цей продукт можна використовувати як у приміщенні, так і на відкритому повітрі. Будь ласка, уважно прочитайте інструкції з монтажу перед початком установки. Невикористання належного обладнання та конфігурації або дотримання правильних процедур може призвести до небезпечної ситуації для людей та пошкодження системи.
- Ми не можемо гарантувати, що через неправильне використання пристрою не трапляються аварії та пошкодження. Будь ласка, використовуйте цей продукт обережно та працюйте на свій страх і ризик!
- У разі відмови пристрою, відключіть його від живлення. Найшвидший спосіб зробити це - від'єднавши шнур живлення від розетки.
Виробник: Mikrotikls SIA, Unijas iela 2, Рига, Латвія, LV1039.

## Federal Communication Commission Interference Statement

![](./img/fcc_logo_ez.badge-85.jpg)

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

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class B digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [B] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (B) / NMB-003 (B)

## UKCA marking

![](./img/ukca_black_fill.badge-94.gif)

(EN) Technical Specifications / (DE) Technische Spezifikationen / (FR) Spécifications techniques / (IT) Specifiche tecniche / (ES) Especificaciones técnicas / (RU) Технические характеристики:

(EN) Product Power Input Options(DE) Produkt Stromquellen Optionen(FR) Options d'entrée d'alimentation du produit(IT) Opzioni di ingresso alimentazione del prodotto(ES) Opciones de entrada de energía del producto(RU) Варианты входной мощности продукта
(EN) DC Adapter Output Specification(DE) Ausgangsspezifikationen des Gleichstromadapters(FR) Spécifications de sortie de l'adaptateur de courant continu(IT) Specifiche di uscita dell'adattatore di corrente continua(ES) Especificaciones de salida del adaptador de corriente continua(RU) Выходные характеристики адаптера постоянного тока
(EN) IP class of the enclosure(DE) IP-Klasse des Gehäuses(FR) Classe IP du boîtier(IT) Classe IP della custodia(ES) Clase de IP del recinto(RU) Класс защиты корпуса IP
(EN) Operating Temperature(DE) Betriebstemperatur(FR) température de fonctionnement(IT) temperatura di esercizio(ES) Temperatura de funcionamiento(RU) Рабочая Температура

Voltage, V
Current, A

DC Jack = 18-57 V DC PoE In = 18-57 V DC
48
0.95
IP66
-40°..+70°C

\#89837
