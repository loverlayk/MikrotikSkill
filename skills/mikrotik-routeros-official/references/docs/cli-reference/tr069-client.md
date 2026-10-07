# tr069-client

> RouterOS settings reference for /tr069-client.

-----------

## tr069-client 
**Package:** tr069-client
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (yes | no)">Enables or disables the CWMP protocol.</ArgTableRow>
<ArgTableRow arg="acs-url" typ="string">URL of the Auto Configuration Server (ACS). If the ACS is accessed using HTTPS, a Root CA must be imported in the client certificate store to verify the ACS server certificate.</ArgTableRow>
<ArgTableRow arg="username" typ="string">HTTP authentication username used by the CPE to authenticate with the ACS.</ArgTableRow>
<ArgTableRow arg="password" typ="string">HTTP authentication password used by the CPE to authenticate with the ACS.</ArgTableRow>
<ArgTableRow arg="periodic-inform-enabled" typ="bool">Enables or disables CPE periodic session initiation. The timer starts after every successful session. When a session is started by the periodic interval, the Inform RPC contains a "2 PERIODIC" event. Maps to `Device.ManagementServer.PeriodicInformEnable`.</ArgTableRow>
<ArgTableRow arg="periodic-inform-interval" typ="time">Timer interval of the periodic inform. Maps to `Device.ManagementServer.PeriodicInformInterval`.</ArgTableRow>
<ArgTableRow arg="connection-request-username" typ="string">Username used by the ACS to authenticate with the CPE for Connection Requests.</ArgTableRow>
<ArgTableRow arg="connection-request-password" typ="string">Password used by the ACS to authenticate with the CPE for Connection Requests.</ArgTableRow>
<ArgTableRow arg="connection-request-port" typ="num">Port on which the CPE listens for Connection Requests from the ACS.</ArgTableRow>
<ArgTableRow arg="provisioning-code" typ="string">Provisioning code for the device.</ArgTableRow>
<ArgTableRow arg="client-certificate" typ="enum (none)">Certificate from the certificate store that can be used by the ACS for extra authentication.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (yes | no)">Whether to check the ACS server certificate.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (disabled | initializing | error | waiting-url | running)">Informative status of the CWMP client. Disabled means the protocol is disabled, waiting-url means the protocol is enabled but the ACS URL is not configured, and running means CWMP is configured correctly and will communicate with the ACS on events.</ArgTableRow>
<ArgTableRow arg="last-session-error" typ="string">User-friendly error description indicating why the previous session did not finish successfully.</ArgTableRow>
<ArgTableRow arg="retry-count" typ="num">Consecutive unsuccessful session count. If greater than 0, last-session-error should indicate the error. Resets to 0 on a successful session, disabled protocol, or reboot.</ArgTableRow>
</ArgTable>
