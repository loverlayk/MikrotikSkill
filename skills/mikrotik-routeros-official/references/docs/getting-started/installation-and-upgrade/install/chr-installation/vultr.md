# CHR: Vultr Installation

> This page guides users through deploying MikroTik CHR on Vultr by first setting up a SystemRescue server, then writing the CHR image to disk using wget and dd commands, and finally connecting via SSH to configure the...

# CHR: Vultr Installation

Vultr has more than [two dozen data center locations](https://www.vultr.com/features/datacenter-locations/) where you can choose to deploy MikroTik CHR for the best [throughput and latency](https://nj-us-ping.vultr.com/).  
Follow these steps to install MikroTik CHR at Vultr.

## Step 1: Deploy a server in rescue mode

In this step, you'll deploy a new server at Vultr with SystemRescue, a bootable Linux ISO.

1. [Deploy](https://my.vultr.com/deploy/) a new [Cloud Compute](https://www.vultr.com/products/cloud-compute/) instance.
2. Choose the location with the best performance for your needs. You can use Vultr's [network-looking glass](https://nj-us-ping.vultr.com/) to test the throughput and latency of any location.
3. Select the **ISO Library** tab in the **Server Image** section.
4. Choose **SystemRescue x64**.
5. Choose a server size with [enough bandwidth allowance](https://www.vultr.com/resources/faq/?query=bandwidth#bandwidthcalculation) for your requirements.
6. Give the server a hostname, and a label, and then click **Deploy Now**.

When the server finishes deploying, proceed to the next step.

## Step 2: Write the CHR image to the disk

1. In your web browser, navigate to the [MikroTik download page](https://mikrotik.com/download).
2. Locate the latest Stable RAW CHR disk image. Vultr requires version **7.2.3 Stable** or later.
3. Right-click the floppy disk icon to copy the URL. Don't download the image now; you'll download it to the server in a later step.  
   ![](./img/vultr-01.webp)
4. Navigate to the server's information page in the [Vultr customer portal](https://my.vultr.com/).
5. Connect to the [web console](https://www.vultr.com/docs/vultr-web-console-faq/).  
   ![](./img/vultr-02.webp)
6. In the web console, download the CHR image to the server with "wget". If you copied the download URL to your clipboard, you can [send it to the server](https://www.vultr.com/docs/vultr-web-console-faq/) through the web console.

   Substitute your version for x.x.x in the examples that follow.

    ```bash
    # wget https://download.mikrotik.com/routeros/x.x.x/chr-x.x.x.img.zip
    ```

7. Unzip the downloaded file.

    ```bash
    # unzip chr-x.x.x.img.zip
    ```

8. Write the MikroTik CHR image to the server's disk with dd.

    ```bash
    # dd if=chr-x.x.x.img of=/dev/vda
    ```

- - **if** is the image that you unzipped in the previous step.
  - **of** is the server's disk:  `/dev/vda`.

This procedure takes a couple of minutes; proceed to the next step when complete.

## Step 3: Connect to MikroTik CHR

1. Navigate to the server's [settings page](https://my.vultr.com/).
2. Choose the **Custom ISO** menu, then click **Remove ISO**. The server will reboot.
3. Connect to the [web console](https://www.vultr.com/docs/vultr-web-console-faq/).
4. Log in as admin. There is no password set, so press <kbd>Enter</kbd> at the prompt.
5. View the software license, then choose a new, strong password.
6. Close the web console, then open a terminal on your local computer.
7. SSH as admin to the server's IP address.

   ```ros
   ssh admin@192.0.2.2
   ```

8. Enter the strong password you set in the prior step.

This completes the basic installation. Please [secure your MikroTik CHR router](../../../securing-your-router.md) and consult the [documentation](../../../first-time-configuration.md) to configure the server for production use. Visit the Vultr site for their [VPC](https://docs.vultr.com/products/network/vpc) and [firewall](https://docs.vultr.com/vultr-firewall) features.
