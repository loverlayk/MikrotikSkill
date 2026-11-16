# CRS125-24G-1S-series

> The device can be accessed through the IP 192.168.88.1, the username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker). Please connect with your web browser to...

![](./img/api_crs125-24g-1s-in.webp) ![](./img/image2020-2-24_13-57-30.webp)

:::info[This article covers]

- **CRS125-24G-1S-IN**
- **CRS125-24G-1S-2HnD-IN**

:::

## First use

The device can be accessed through the IP 192.168.88.1, the username is admin and there is no password (or, for some models, check user and wireless passwords on the sticker). Please connect with your web browser to this IP address to configure it. See this page for connection and configuration guides: [RouterOS documentation](/docs/introduction)
The device comes preinstalled with RouterOS and is ready to use. The device is compatible with RouterOS v6 and newer.
For the wireless model CRS125-24G-1S-2HnD-IN, ports are switched, wireless interface and switch are bridged, and the bridge contains a DHCP server. Eth1 and SFP1 have DHCP client configured. After connected choose your country, to apply country regulation settings.

- Update the device by clicking the "Check for updates" button to v6.46 or the latest RouterOS software to ensure the best performance and stability. The device needs to have an active internet connection.
- To manually update the device, go to our download page https://mikrotik.com/download
- Choose your architecture (ARM) and download the latest packages from any channel to your PC.
- Open WinBox and upload packages in the Files menu.
- Reboot the device.
- Updating software will ensure the latest security fixes and regulations set by local law.
- Set up your password to secure the device.

## Powering

The device accepts direct-input power jack: 10-28 V (24 V0.8 A PSU included in the package).
The power consumption under maximum load can reach 20 W.

## Configuration

Once logged in, we recommend clicking the "Check for updates" button in the QuickSet menu, as updating your RouterOS software to the latest version ensures the best performance and stability. For wireless models, please make sure you have selected the country where the device will be used, to conform with local regulations.
RouterOS includes many configuration options in addition to what is described in this document. We suggest starting here to get yourself accustomed to the possibilities: https://mt.lv/help In case IP connection is not available, the WinBox tool (https://mt.lv/winbox) can be used to connect to the MAC address of the device from the LAN side (all access is blocked from the Internet port by default).
For recovery purposes, it is possible to boot the device from the network, see a section .

## Extension slots and ports

- Twenty four (24) 10/100/1000 (Gigabit) Ethernet ports (Auto MDI/X)
- CRS125 has one SFP cage, compatible with 1.25G SFP modules.
- CRS125-24G-1S-2HnD-IN has built-in 802.11b/g/n 2GHz wireless access point.

## Reset button

The routerBOOT reset button has the following functions. Press the button and apply the power, then:

- Release the button when green LED starts flashing, to reset RouterOS configuration to defaults.
- Release the button when the LED turns solid green to clear all configuration and defaults.
- Release the button after LED is no longer lit (~20 seconds) to cause a device to look for Netinstall servers (required for reinstalling RouterOS over the network).
Regardless of the above option used, the system will load the backup RouterBOOT loader if the button is pressed before power is applied to the device. Useful for RouterBOOT debugging and recovery.

## Operating system support

The device supports RouterOS software with the version number at or above what is indicated in the RouterOS menu /system resource. Other operating systems have not been tested.

## Safety Notice

![](../img/worddav8aafa0dcbb3328dd9f53f471f1e60640.badge.webp)

Electric shock hazard. This equipment is to be serviced by trained personnel only. This is a class A device, operating it near residential radio equipment could cause radio interference.

![](./img/image2020-2-24_13-58-18.webp)

CRS125-24G-1S-IN:

![](./img/image2020-2-24_13-59-37.webp)

![](../img/worddav5e0d6068efc4336c8967232b1a34b712.badge.webp)

 Federal Communication Commission Interference Statement
FCC ID:TV7CRS109-8G2HND
This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a residential installation.
This equipment generates, uses and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one of the following measures:

- Reorient or relocate the receiving antenna.
- Increase the separation between the equipment and receiver.
- Connect the equipment into an outlet on a circuit different from that to which the receiver is connected.
- Consult the dealer or an experienced radio/TV technician for help.
FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate this equipment.
This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation. This device and its antenna must not be co-located or operation in conjunction with any other antenna or transmitter.
IMPORTANT: Exposure to Radio Frequency Radiation.
This equipment complies with the FCC RF radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with a minimum distance of 20 cm between the radiator and any part of your body.

### CE Declaration of Conformity

Manufacturer: MikroTikls SIA, Brivibas gatve 214i Riga, Latvia, LV1039.

| *BG* | С настоящото Mikrotīkls SIA декларира, че този тип радиосъоръжение RouterBOARD е в съответствие с Директива 2014/53/ЕС. Цялостният текст на ЕС декларацията за съответствие може да се намери на следния интернет адрес: https://mikrotik.com/products |
| --- | --- |
| CS | Tímto Mikrotīkls SIA prohlašuje, že typ rádiového zařízení RouterBOARD je v souladu se směrnicí 2014/53/EU. Úplné znění EU prohlášení o shodě je k dispozici na této internetové adrese: https://mikrotik.com/products |
| DA | Hermed erklærer Mikrotīkls SIA , at radioudstyrstypen RouterBOARD er i overensstemmelse med direktiv 2014/53/EU. EU-overensstemmelseserklæringens fulde tekst kan findes på følgende internetadresse: https://mikrotik.com/products |
| DE | Hiermit erklärt Mikrotīkls SIA , dass der Funkanlagentyp RouterBOARD der Richtlinie 2014/53/EU entspricht. Der vollständige Text der EU-Konformitätserklärung ist unter der folgenden Internetadresse verfügbar: https://mikrotik.com/products |
| EL | Με την παρούσα ο/η Mikrotīkls SIA , δηλώνει ότι ο ραδιοεξοπλισμός RouterBOARD πληροί την οδηγία 2014/53/ΕΕ. Το πλήρες κείμενο της δήλωσης συμμόρφωσης ΕΕ διατίθεται στην ακόλουθη ιστοσελίδα στο διαδίκτυο: https://mikrotik.com/products |
| EN | Hereby, Mikrotīkls SIA declares that the radio equipment type RouterBOARD is in compliance with Directive 2014/53/EU. The full text of the EU declaration of conformity is available at the following internet address: https://mikrotik.com/products |
| ES | Por la presente, Mikrotīkls SIA declara que el tipo de equipo radioeléctrico RouterBOARD es conforme con la Directiva 2014/53/UE. El texto completo de la declaración UE de conformidad está disponible en la dirección Internet siguiente: https://mikrotik.com/products |
| ET | Käesolevaga deklareerib Mikrotīkls SIA , et käesolev raadioseadme tüüp RouterBOARD vastab direktiivi 2014/53/EL nõuetele. ELi vastavusdeklaratsiooni täielik tekst on kättesaadav järgmisel internetiaadressil: https://mikrotik.com/products |
| FI | Mikrotīkls SIA vakuuttaa, että radiolaitetyyppi RouterBOARD on direktiivin 2014/53/EU mukainen. EU-vaatimustenmukaisuusvakuutuksen täysimittainen teksti on saatavilla seuraavassa internetosoitteessa: https://mikrotik.com/products |
| FR | Le soussigné, Mikrotīkls SIA , déclare que l'équipement radioélectrique du type RouterBOARD est conforme à la directive 2014/53/UE. Le texte complet de la déclaration UE de conformité est disponible à l'adresse internet suivante: https://mikrotik.com/products |
| HR | Mikrotīkls SIA ovime izjavljuje da je radijska oprema tipa RouterBOARD u skladu s Direktivom 2014/53/EU. Cjeloviti tekst EU izjave o sukladnosti dostupan je na sljedećoj internetskoj adresi: https://mikrotik.com/products |
| HU | Mikrotīkls SIA igazolja, hogy a RouterBOARD típusú rádióberendezés megfelel a 2014/53/EU irányelvnek. Az EU-megfelelőségi nyilatkozat teljes szövege elérhető a következő internetes címen: https://mikrotik.com/products |
| IT | Il fabbricante, Mikrotīkls SIA , dichiara che il tipo di apparecchiatura radio RouterBOARD è conforme alla direttiva 2014/53/UE. Il testo completo della dichiarazione di conformità UE è disponibile al seguente indirizzo Internet: https://mikrotik.com/products |
| IS | Hér með lýsir Mikrotīkls SIA yfir því að RouterBOARD er í samræmi við grunnkröfur og aðrar kröfur, sem gerðar eru í tilskipun 2014/53/EU. Fullur texti ESB samræmisyfirlýsing er að finna á eftirfarandi netfangi: https://mikrotik.com/products |
| LT | Aš, Mikrotīkls SIA , patvirtinu, kad radijo įrenginių tipas RouterBOARD atitinka Direktyvą 2014/53/ES. Visas ES atitikties deklaracijos tekstas prieinamas šiuo interneto adresu: https://mikrotik.com/products |
| LV | Ar šo Mikrotīkls SIA deklarē, ka radioiekārta RouterBOARD atbilst Direktīvai 2014/53/ES. Pilns ES atbilstības deklarācijas teksts ir pieejams šādā interneta vietnē: https://mikrotik.com/products |
| MT | B'dan, Mikrotīkls SIA , niddikjara li dan it-tip ta' tagħmir tar-radju RouterBOARD huwa konformi mad-Direttiva 2014/53/UE. It-test kollu tad-dikjarazzjoni ta' konformità tal-UE huwa disponibbli f'dan l-indirizz tal-Internet li ġej: https://mikrotik.com/products |
| NL | Hierbij verklaar ik, Mikrotīkls SIA , dat het type radioapparatuur RouterBOARD conform is met Richtlijn 2014/53/EU. De volledige tekst van de EU-conformiteitsverklaring kan worden geraadpleegd op het volgende internetadres: https://mikrotik.com/products |
| NO | Mikrotīkls SIA erklærer herved at utstyret RouterBOARD er i samsvar med de grunnleggende krav og øvrige relevante krav i direktiv 2014/53/EU. Den fulle teksten til EU-samsvarserklæringen er tilgjengelig på følgende internettadresse: https://mikrotik.com/products |
| PL | Mikrotīkls SIA niniejszym oświadcza, że typ urządzenia radiowego RouterBOARD jest zgodny z dyrektywą 2014/53/UE. Pełny tekst deklaracji zgodności UE jest dostępny pod następującym adresem internetowym: https://mikrotik.com/products |
| PT | O(a) abaixo assinado(a) Mikrotīkls SIA declara que o presente tipo de equipamento de rádio RouterBOARD está em conformidade com a Diretiva 2014/53/UE. O texto integral da declaração de conformidade está disponível no seguinte endereço de Internet: https://mikrotik.com/products |
| RO | Prin prezenta, Mikrotīkls SIA declară că tipul de echipamente radio RouterBOARD este în conformitate cu Directiva 2014/53/UE. Textul integral al declarației UE de conformitate este disponibil la următoarea adresă internet: https://mikrotik.com/products |
| SK | Mikrotīkls SIA týmto vyhlasuje, že rádiové zariadenie typu RouterBOARD je v súlade so smernicou 2014/53/EÚ. Úplné EÚ vyhlásenie o zhode je k dispozícii na tejto internetovej adrese: https://mikrotik.com/products |
| SL | Mikrotīkls SIA potrjuje, da je tip radijske opreme RouterBOARD skladen z Direktivo 2014/53/EU. Celotno besedilo izjave EU o skladnosti je na voljo na naslednjem spletnem naslovu: https://mikrotik.com/products |
| SV | Härmed försäkrar Mikrotīkls SIA att denna typ av radioutrustning RouterBOARD överensstämmer med direktiv 2014/53/EU. Den fullständiga texten till EU-försäkran om överensstämmelse finns på följande webbadress: https://mikrotik.com/products |

### MPE statement

This equipment complies with EU radiation exposure limits set forth for an uncontrolled environment. This equipment should be installed and operated with minimum distance of 20 cm between the radiator and your body, unless specifically stated otherwise in page 1 of this document. In RouterOS you must specify your country, to make sure local wireless regulations are observed.

### Frequency bands terms of use

| Frequency range (for applicable models) | Channels used | Maximum Output Power (EIRP) | Restriction |
| --- | --- | --- | --- |
| 2412-2472 MHz | 1 - 13 | 20 dBm | Without any restriction to use in all EU Member States |
| 5150-5250 MHz | 26 - 48 | 23 dBm | Restricted to indoor use only* |
| 5250-5350 MHz | 52 - 64 | 20 dBm | Restricted to indoor use only* |
| 5470-5725 MHz | 100 - 140 | 27 dBm | Without any restriction to use in all EU Member States |

** It is the customer's responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed!*

![](../img/eac.badge.webp)

***BG. Инструкция**: Свържете адаптера на захранване, за да включите устройството. Отворете 192.168.88.1 в уеб браузър, за да настроите продукта. Повече информация в* &#123;*&#125;&#123;+&#125;https://mt.lv/help-bg*
 ***CS. Návod k použití**: Připojte napájecí adaptér k zapnutí přístroje. Otevřete 192.168.88.1 ve webovém prohlížeči pro konfiguraci produktu. Více informací najdete v* &#123;*&#125;&#123;+&#125;https://mt.lv/help-cs*
 ***DA. Instruktionsbog**: Tilslut strømadapteren for at tænde for enheden. Åbn 192.168.88.1 i en webbrowser til at konfigurere produktet. Mere information i* &#123;*&#125;&#123;+&#125;https://mt.lv/help-da*
 ***DE. Bedienungsanleitung**: Verbinden Sie das Netzteil, um das Gerät einzuschalten. Öffnen Sie 192.168.88.1 in einem Web-Browser, um das Produkt zu konfigurieren. Weitere Informationen im* &#123;*&#125;&#123;+&#125;https://mt.lv/help-de*
 ***EL. εγχειρίδιο οδηγιών**: Συνδέστε τον προσαρμογέα τροφοδοσίας για να ενεργοποιήσετε τη μονάδα. Ανοίξτε 192.168.88.1 σε ένα πρόγραμμα περιήγησης στο Web για να διαμορφώσετε το προϊόν. Περισσότερες πληροφορίες στο* &#123;*&#125;&#123;+&#125;https://mt.lv/help-el*
 ***EN. Instruction manual**: Connect the power adapter to turn on the device. Open 192.168.88.1 in your web browser, to configure it. More information on* &#123;*&#125;&#123;+&#125;https://mt.lv/help*
 ***ES. Manual de instrucciones**: Conecte el adaptador de alimentación para encender la unidad. Abra 192.168.88.1 en un navegador web para configurar el producto. Más información en* &#123;*&#125;&#123;+&#125;https://mt.lv/help-es*
 ***ET. Kasutusjuhend**: Ühendage toiteadapter seadme sisselülitamiseks. Avatud 192.168.88.1 in veebilehitseja seadistada toodet. Rohkem teavet* &#123;*&#125;&#123;+&#125;https://mt.lv/help-et*
 ***FI. Käyttöohje**: Kytke virtalähde päälle laitteen. Avaa 192.168.88.1 in selaimen määrittää tuotteen. Lisää tietoa* &#123;*&#125;&#123;+&#125;https://mt.lv/help-fi*
 ***FR. Mode d'emploi**: Connectez l'adaptateur d'alimentation pour allumer l'appareil. Ouvrez 192.168.88.1 dans un navigateur Web pour configurer le produit. Plus d'informations dans* &#123;*&#125;&#123;+&#125;https://mt.lv/help-fr*
 ***HR. Uputa za uporabu**: Priključite napajanje i uključite uređaj. Za konfiguraciju uređaja u pregledniku otvorite 192.168.88.1. Više informacija je na* &#123;*&#125;&#123;+&#125;https://mt.lv/help-hr*
 ***HU. Használati utasítás**: Csatlakoztassa a hálózati adaptert a készülék bekapcsolásához. Megnyitása 192.168.88.1 egy webböngészőben beállítani a terméket. Több információ* &#123;*&#125;&#123;+&#125;https://mt.lv/help-hu*
 ***IT. Manuale di istruzioni**: Collegare l'adattatore di alimentazione per accendere l'unità. Aprire 192.168.88.1 in un browser Web per configurare il prodotto. Maggiori informazioni in* &#123;*&#125;&#123;+&#125;https://mt.lv/help-it*
 ***IS. Notkunarhandbók**: Tengdu straumbreytirinn til að kveikja á tækinu. Opnaðu 192.168.88.1 í vafranum þínum til að stilla það. Nánari upplýsingar á* &#123;*&#125;&#123;+&#125;https://mt.lv/help-is*
 ***NO. Instruksjonsmanual**: Koble strømadapteren for å slå på enheten. Åpne 192.168.88.1 i nettleseren din for å konfigurere den. Mer informasjon på* &#123;*&#125;&#123;+&#125;https://mt.lv/help-no*
 ***LT. Naudojimosi instrukcija**: Prijunkite maitinimo adapterį įjunkite įrenginį. Į interneto naršyklę 192.168.88.1 Atidarykite galite konfigūruoti gaminį. Daugiau informacijos rasite* &#123;*&#125;&#123;+&#125;https://mt.lv/help-lt*
 ***LV. Lietošanas instrukcija**: Pievienojiet Strāvas adapteri, lai ieslēgtu ierīci. Atvērt 192.168.88.1 ar interneta pārlūku, lai konfigurētu produktu. Plašāka informācija* &#123;*&#125;&#123;+&#125;https://mt.lv/help-lv*
 ***MT. Manwal tal-istruzzjoni**: Qabbad l-adapter tal-qawwa biex iddawwar it-tagħmir. Iftaħ 192.168.88.1 fil-web browser tiegħek, biex jiġi kkonfigurat. Aktar informazzjoni fuq* &#123;*&#125;&#123;+&#125;https://mt.lv/help-mt*
 ***NL. Handleiding**: Sluit voedingsadapter aan op het apparaat in te schakelen. Open 192.168.88.1 in een webbrowser om het product te configureren. Meer informatie in* &#123;*&#125;&#123;+&#125;https://mt.lv/help-nl*
 ***PL. Instrukcja obsługi**: Podłącz adapter zasilania, aby włączyć urządzenie. Otwórz 192.168.88.1 w przeglądarce internetowej, aby skonfigurować urządzenie. Więcej informacji w* &#123;*&#125;&#123;+&#125;https://mt.lv/help-pl*
 ***PT. Manual de instruções**: Conecte o adaptador de alimentação para ligar o aparelho. Abra 192.168.88.1 em um navegador da web para configurar o produto. Mais informações em* &#123;*&#125;&#123;+&#125;https://mt.lv/help-pt*
 ***RO. Instrucțiuni de utilizare**: Conectați adaptorul de alimentare pentru a porni aparatul. Deschide 192.168.88.1 într-un browser web pentru a configura produsul. Mai multe informații în* &#123;*&#125;&#123;+&#125;https://mt.lv/help-ro*
 ***SK. Navodila**: Priključite napajalnik za vklop naprave. Odprite 192.168.88.1 v spletnem brskalniku nastaviti izdelek. Več informacij v*
 &#123;*&#125;&#123;+&#125;https://mt.lv/help-sk*
 ***SL. Návod na použitie**: Pripojte napájací adaptér k zapnutiu prístroja. Otvorte 192.168.88.1 vo webovom prehliadači pre konfiguráciu produktu. Viac informácií nájdete v* &#123;*&#125;&#123;+&#125;https://mt.lv/help-sl*
 ***SV. Instruktionsmanual**: Anslut nätadaptern för att slå på enheten. Öppna 192.168.88.1 i en webbläsare för att konfigurera produkten. Mer information på* &#123;*&#125;&#123;+&#125;https://mt.lv/help-sv*
 ***NO. Bruksanvisningen**: Koble strømadapteren for å slå på enheten. Åpne 192.168.88.1 i en nettleser for å konfigurere produktet. Mer informasjon på* &#123;*&#125;&#123;+&#125;https://mt.lv/help-no*

- **RU. Руководство по эксплуатации**: подключите адаптер питания чтобы включить устройство. Откройте 192.168.88.1 в своем веб-браузере для конфигурации. Дополнительная информация* &#123;*&#125;&#123;+&#125;https://mt.lv/help-ru*
 ***CN. 说明书。*** *连接电源适配器以打开设备。 在Web浏览器中打开192.168.88.1进行配置。 有关*&#123;*&#125;&#123;+&#125;https://mt.lv/help-zh* *的更多信息*
