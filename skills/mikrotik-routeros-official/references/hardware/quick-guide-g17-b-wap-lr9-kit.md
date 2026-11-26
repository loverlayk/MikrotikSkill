# Quick Guide G17-b - wAP LR9 kit

> Models: RBwAPR-2nD&R11e-LR9 (wAP LR9 kit)

**Models: RBwAPR-2nD&R11e-LR9 (wAP LR9 kit)**

![](./img/mt_logo_arrow_v2-02-48.png)

## EN - English - Quick Guide

:::warning
This device needs to be upgraded to RouterOS v7.7 or the latest version to ensure compliance with local authority regulations!

It is the end users' responsibility to follow local country regulations, including operation within legal frequency channels, output power, cabling requirements, and Dynamic Frequency Selection (DFS) requirements. All MikroTik radio devices must be professionally installed
:::

*This is Wireless Network Device. You can find the product model name on the case label (ID).*
*Please visit the user manual page on [https://mt.lv/um](https://mt.lv/um) for the full up-to-date user manual. Or scan the QR code with your mobile phone.*
*Technical specifications, brochures, and more info about products at [https://mikrotik.com/products](https://mikrotik.com/products)*
*The most important technical specifications for this product can be found on the last page of this Quick Guide.*
*Configuration manual for software in your language with additional information can be found at [https://mt.lv/help](https://mt.lv/help)*
*MikroTik devices are for professional use. If you do not have qualifications please seek a consultant [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-1-31_12-4-32.badge-52.png)

**First steps:**

- Make sure your ISP is allowing hardware change and will issue an automatic IP address;
- Open the bottom lid;
- Connect an external antenna to the SMA connector;
- Connect the device to the power source;
- Connect your ISP cable to the Ethernet port;
- Navigate to the network connections section on your computer and locate the wireless network named *"MikroTik-..."*. Proceed to connect to it (check the wireless passwords on the sticker);
- Establish a connection using a mobile application. Alternatively, use WebFig in a web browser or the "WinBox" configuration tool at [https://mt.lv/WinBox](https://mt.lv/WinBox); **multiple configuration methods are available to ensure accessibility;**
- Download and open *Winbox*, and choose the *Neighbors* tab to find the device;
- The default IP address is 192.168.88.1. Click on the IP address. If the IP is not available, use *Winbox* and connect using the MAC address. The username is *"admin"* and there is no password (or, for some models, check user and wireless passwords on the sticker);
- Click the "Check for updates" button and update RouterOS to the latest version;
- For a manual update of the device, visit mikrotik.com, select your model, and locate the required packages in the "Downloads" section;
- Upload downloaded packages to the *WebFig or* *Winbox* *"Files"* menu and reboot the device;
- By upgrading your RouterOS software to the latest version, you can ensure optimal performance, stability, and security updates;
- In the *"QuickSet"* menu set up the following: Choose your country, to apply country regulation settings;
- Set up your wireless network password in the left field;
- Set up your router password in the bottom field;
- Find *LR Gateway ID* on the label within the product and register it in your Network Server.

**Safety Information:**

- Before you work on any MikroTik equipment, be aware of the hazards involved with electrical circuitry and be familiar with standard practices for preventing accidents. The installer should be familiar with network structures, terms, and concepts.
- Use only the power supply and accessories approved by the manufacturer, and which can be found in the original packaging of this product.
- This equipment is to be installed by trained and qualified personnel, as per these installation instructions. The installer is responsible for making sure, that the Installation of the equipment is compliant with local and national electrical codes. Do not attempt to disassemble, repair, or modify the device.
- This product can be installed outdoors. Please read the mounting instructions carefully before beginning installation. Failure to use the correct hardware and configuration or to follow the correct procedures could result in a hazardous situation to people and damage to the system.
- We cannot guarantee that no accidents or damage will occur due to the improper use of the device. Please use this product with care and operate at your own risk!
- In the case of device failure, please disconnect it from power. The fastest way to do so is by unplugging the power adapter from the power outlet.
- This is a Class A product. In a domestic environment, this product might cause radio interference in which case the user might be required to take adequate measures!

**Exposure to Radio Frequency Radiation:** This MikroTik equipment complies with the European Union radiation exposure limits set forth for an uncontrolled environment. This MikroTik device should be installed and operated no closer than 20 centimeters from your body, occupational user, or the general public.

Manufacturer: Mikrotikls SIA, Unijas iela 2, Riga, Latvia, LV1039.

## ES - Español. Guía rápida

:::warning
Este dispositivo debe actualizarse a RouterOS v7.7 o la última versión para garantizar el cumplimiento de las regulaciones de las autoridades locales.
Es responsabilidad del usuario final seguir las regulaciones locales del país, incluida la operación dentro de los canales legales de frecuencia, salida alimentación, requisitos de cableado y requisitos de selección de frecuencia dinámica (DFS). Todos los dispositivos de radio MikroTik deben ser instalado profesionalmente
:::

*Este es un dispositivo de red inalámbrica. Puede encontrar el nombre del modelo del producto en la etiqueta del caso (ID).*
*Visite la página del manual del usuario en [https://mt.lv/um-es](https://mt.lv/um-es) para obtener el manual del usuario actualizado. O escanee el código QR con su teléfono móvil.*
*Especificaciones técnicas, folletos y más información sobre productos en [https://mikrotik.com/products](https://mikrotik.com/products)*
*Las especificaciones técnicas más importantes de este producto se pueden encontrar en la última página de esta Guía rápida.*
*Puede encontrar el manual de configuración del software en su idioma con información adicional en [https://mt.lv/help-es](https://mt.lv/help-es)*
*Los dispositivos MikroTik son para uso profesional. Si no tiene calificaciones, busque un consultor [https://mikrotik.com/consultants](https://mikrotik.com/consultants)*

![](./img/image2020-2-4_17-27-25.badge-51.png)

**Primeros pasos:**

- Asegúrese de que su ISP permita cambios de hardware y emita una dirección IP automática;
- Abra la tapa inferior;
- Conecte una antena externa al conector SMA;
- Conecte el dispositivo a la fuente de alimentación;
- Conecte el cable de su ISP al puerto Ethernet;
- Navegue hasta la sección de conexiones de red en su computadora y ubique la red inalámbrica llamada *"MikroTik-..."*. Proceda a conectarse (verifique las contraseñas inalámbricas en la etiqueta);
- Establecer una conexión mediante una aplicación móvil. Alternativamente, puede utilizar WebFig en un navegador web o la herramienta de configuración "WinBox" en [https://mt.lv/WinBox](https://mt.lv/WinBox); **hay varios métodos de configuración disponibles para garantizar la accesibilidad;**
- Descargue y abra *Winbox*, y elija la pestaña *Neighbors* para encontrar el dispositivo;
- La dirección IP predeterminada es 192.168.88.1. Haga clic en la dirección IP. Si la IP no está disponible, use *Winbox* y conéctese usando la dirección MAC. El nombre de usuario es *"admin"* y no hay contraseña (o, para algunos modelos, verifique las contraseñas de usuario y de conexión inalámbrica en la etiqueta);
- Haga clic en el botón *"Check for updates"* y actualice RouterOS a la última versión;
- Para actualizar manualmente el dispositivo, visite mikrotik.com, seleccione su modelo y localice los paquetes requeridos en la sección "Downloads";
- Cargue los paquetes descargados en el menú *WebFig o Winbox"Files"* y reinicie el dispositivo;
- Al actualizar el software RouterOS a la última versión, puede garantizar un rendimiento óptimo, estabilidad y actualizaciones de seguridad;
- En el menú *"QuickSet"* configure lo siguiente: Elija su país para aplicar la configuración de regulación del país;
- Configure la contraseña de su red inalámbrica en el campo izquierdo;
- Configure la contraseña de su enrutador en el campo inferior;
- Busque *LR Gateway ID* en la etiqueta del producto y regístrelo en su servidor de red.

**Información de seguridad:**

- Antes de trabajar en cualquier equipo MikroTik, tenga en cuenta los riesgos relacionados con los circuitos eléctricos y familiarícese con las prácticas estándar para prevenir accidentes. El instalador debe estar familiarizado con las estructuras de red, los términos y los conceptos.
- Utilice solo la fuente de alimentación y los accesorios aprobados por el fabricante, y que se pueden encontrar en el embalaje original de este producto.
- Este equipo debe ser instalado por personal capacitado y calificado, según estas instrucciones de instalación. El instalador es responsable de asegurarse de que la instalación del equipo cumpla con los códigos eléctricos locales y nacionales. No intente desmontar, reparar o modificar el dispositivo.
- Este producto se puede instalar en exteriores. Lea atentamente las instrucciones de montaje antes de comenzar la instalación. Si no se utiliza el hardware y la configuración correctos o no se siguen los procedimientos correctos, se podrían producir situaciones peligrosas para las personas y daños en el sistema.
- No podemos garantizar que no ocurran accidentes o daños debido al uso incorrecto del dispositivo. ¡Utilice este producto con cuidado y opere bajo su propio riesgo!
- En caso de falla del dispositivo, desconéctelo de la alimentación. La forma más rápida de hacerlo es desconectando el adaptador de alimentación de la toma de corriente.
- Este es un producto de clase A. ¡En un entorno doméstico, este producto puede causar interferencias de radio, en cuyo caso el usuario deberá tomar las medidas adecuadas!

**Exposición a la radiación de radiofrecuencia:** este equipo MikroTik cumple con los límites de exposición a la radiación de la Unión Europea establecidos para un entorno no controlado. Este dispositivo MikroTik debe instalarse y operarse a no menos de 20 centímetros de su cuerpo, usuario profesional o público en general.

Fabricante: Mikrotikls SIA, Unijas iela 2 Riga, Letonia, LV1039.

**Información México:**

Módulo inalámbrico integrado que funciona a 2,4 GHz, protocolo 802.11b/g/n con antena PCB incorporada, ganancia máxima de 2 dBi.

Rango de frecuencia (potencia de salida máxima): 902-928 MHz (14 dBm), 2400-2483.5 MHz (30 dBm). Los canales de frecuencia disponibles pueden variar según el modelo y la certificación del producto.

Número de Certificado de Homologación (IFT): Ver la etiqueta del producto.

La operacion de este equipo esta sujeta a las siguientes dos condiciones:

- Es posible que este equipo o dispositivo no cause interferencia perjudicial y.
- Este equipo debe aceptar cualquier interferencia, incluyendo la que pueda causar su operacion no deseada.
Fabricante: Mikrotikls SIA, Unijas iela 2, Riga, LV-1039, Latvia.

País De Origen: Letonia; Lituania; China (Republica Popular); Estados Unidos De America; Mexico.

Por favor contacte a su distribuidor local para preguntas regionales específicas. La lista de importadores se puede encontrar en nuestra página de inicio – https://mikrotik.com/buy/latinamerica/mexico.

## Federal Communication Commission Interference Statement

| Model | FCC ID | Contains FCC ID |
| --- | --- | --- |
| RBwAPR-2nD&R11e-LR9 | TV7WAPR2ND | TV7LR9 |

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15 of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation
![](./img/fcc_logo_ez.badge-43.jpg)

This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. If this equipment does cause harmful interference to radio or television reception, which can be determined by turning the equipment off and on, the user is encouraged to try to correct the interference by one or more of the following measures:

FCC Caution: Any changes or modifications not expressly approved by the party responsible for compliance could void the user’s authority to operate this equipment.

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Note: This unit was tested with shielded cables on the peripheral devices. Shielded cables must be used with the unit to ensure compliance.

Antenna Installation WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in the USA (or where FCC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

APPROVED 824 - 960 MHz ANTENNA:

- 6.5 dBi Omnidirectional (Model: TOF-0809-7V-S1)
The same type of antenna and lower antenna gain than those listed above may also be used in accordance with the certification

## Innovation, Science, and Economic Development Canada

| Model | IC | Contains IC |
| --- | --- | --- |
| RBwAPR-2nD&R11e-LR9 | 7442A-WAPR2ND | 7442A-LR9 |

This device contains license-exempt transmitter(s)/receiver(s) that comply with Innovation, Science, and Economic Development Canada’s license-exempt RSS(s). Operation is subject to the following two conditions: (1) This device may not cause interference. (2) This device must accept any interference, including interference that may cause undesired operation of the device.

L’émetteur/récepteur exempt de licence contenu dans le présent appareil est conforme aux CNR d’Innovation, Sciences et Développement économique Canada applicables aux appareils radio exempts de licence. L’exploitation est autorisée aux deux conditions suivantes: 1) L’appareil ne doit pas produire de brouillage; 2) L’appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d’en compromettre le fonctionnement.

This Class A digital apparatus complies with Canadian ICES-003.

Cet appareil numérique de la classe [A] est conforme à la norme NMB-003 du Canada.

CAN ICES-003 (A) / NMB-003 (A)

Antenna Installation WARNING: It is the installer's responsibility to ensure that when using the authorized antennas in Canada (or where IC rules apply); only those antennas certified with the product are to be used. The installer should configure the output power level of antennas, according to country regulations and per antenna type. Professional installation is required for equipment with connectors to ensure compliance with health and safety issues.

APPROVED 824 - 960 MHz ANTENNA:

- 6.5 dBi Omnidirectional (Model: TOF-0809-7V-S1)
The same type of antenna and lower antenna gain than those listed above may also be used in accordance with the certification

(EN) Technical Specifications / (ES) Especificaciones técnicas:

(EN) Product Power Input Options(ES) Opciones de entrada de energía del producto
(EN) DC Adapter Output Specification(ES) Especificaciones de salida del adaptador de corriente continua
(EN) IP class of the enclosure(ES) Clase de IP del recinto
(EN) Operating Temperature(ES) Temperatura de funcionamiento

Voltage, V
Current, A

DC Jack (9-30 V DC) PoE In Ethernet Port (9-30 V DC) Automotive (9-30 V DC)
24
0.8
IP54
-33°..+60°C

\#79091
