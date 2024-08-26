# Setting up a MySQL database on Windows

## Introduction

MySQL is an open-source relational database management system and it’s one of the most widely used databases for both personal and industry use.

 Installation for MySQL and other such databases is relatively straightforward; however, there are some system-specific dependencies and OS-specific differences. This reading is a guide to installing MySQL on a Windows device.

###  Step 1

The standard MySQL installation in Windows is done with the help of the MySQL Installer tool.

 First you need to download the MySQL Installer app from the official [MySQL website](https://dev.mysql.com/downloads/installer/).

 You will be presented with the following screen:

![The MySQL installers for different operating systems](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/yrlYj679SkSU7Co9TwU8Vg_92f9194348fa462cac0c9239a50a1ee1_Picture-1.png?expiry=1724630400000&hmac=aMGXftshATu5JNo-dVhAADh7DsRd2jdmtb9_KpNnL3w)

Select the larger installer and press the Download button. 

You can also choose the web-based installation if you are going to stay connected to the internet while installing MySQL on your local machine. 

Note: *The visual layout of the installer may appear slightly different according to the Windows version and MySQL installer at the time of installation. The general sequence of steps will however remain the same.*

### Step 2

Once downloaded, double-click on the MySQL installer file and follow the steps outlined below.

Note: During the installation, w*henever you’re unsure, select the default options in place.*

Select Full as the setup type.

![](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bqoDk3VZQv6aeaw-OOA13g_fb33e8679f4d4535b934e8e2a1b462e1_SQLsetUp1.png?expiry=1724630400000&hmac=BfjCd7j6ulUkziqiXACnWon9zFaRrSaEkDafbIuYToo)

All the required dependencies are selected for the installation. 

### Step 3

Proceed to the next step by clicking on the Next button. 

![Checking requirements before starting the installations](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/yg06MUbxTRib__S0h_dHOg_da9553c8b080486f9f2e9480686cf0e1_Picture-3.png?expiry=1724630400000&hmac=yN260HSDjMtoatjqcIdq2eYPImijb6VYhzN5ixxy3hY)

### Step 4

This step in the installation process lists all the products you may want to install with your MySQL database as below. Once you press the Execute button, the tools will be downloaded automatically. 

![List of items to be installed](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/X1htMpAASN2wpagqii0pXw_a76b57afe9f84081882d93752d7366e1_Picture-5.png?expiry=1724630400000&hmac=IltJvG-f7XVe1AryV4WAbu6my3f55VsAOnxcM8_wqTA)

In addition to the steps mentioned, specific connectors may be required to use MySQL with different tools such as VSCode and languages such as Python. For example, to use Python you would first need to install the package mysqlclient using pip.

Wait until all the downloads are complete and installed and you'll get a screen similar to this. 

![Downloading components was successful](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/SkXShJ5uRiC5P0uq8S-kfQ_867d3f1a3fb64c5e88946abe52ecd0e1_Picture-6.png?expiry=1724630400000&hmac=qg9ZIMrh7sMztOd4SJmXDcdD5eX8sWTJZCkE2duuJxo)

The list will depend on the tools available at the time of your installation. For a complete list of tools that you may require, you can refer to the official [MySQL website](https://dev.mysql.com/downloads/) which also provides an additional option to install tools individually.

Note: *For general use, the installation of MySQL Workbench and MySQL Server is important.*

### Step 5

The next screen provides a Product Configuration Overview of the installation. 

![Product configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/0-id_6uJTye3teemEKF_NA_baf721787d524adfa6852df465d4bee1_Picture-7.png?expiry=1724630400000&hmac=_YndqYOKl497e4mgjjIxe5EZo1b9KeiD7FFMjCiUr8s)

Pressing the Next button, will take you to the following screen:

![Network configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bkiiUjKUS9-CAzBbqD91Ww_90a0218efd264c809b21ba898c557de1_Picture-8.png?expiry=1724630400000&hmac=ar7zpeEbIxRvpZqOv147APix1usIyXcnaSHAkGUtUYY)

Keep the basic configuration and proceed with setting the password for the root user:

![Password configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/a9-xyE8hSJ6iUdPzFYLXlQ_04da77b0c26c4b44b866b36a8db037e1_Picture-9.png?expiry=1724630400000&hmac=N2rRUScRLV9gyL6375Zv-yXRmZbnF2w7CkpLyQ-Rk0c)

![Password settings](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/iB6qcKJ9RemlOidsX7Lt2g_43b4b18bac7b4d579355d4fb25522ce1_Picture-10.png?expiry=1724630400000&hmac=IX8CALh_zsOTJInCkfN7zy9vcCcuAdNiz4lB3IxibnI)

Note: *Make a note of the password you set and save it in a secure place to avoid having to reset it if you forget your password.*

If necessary, you can also add additional users on this page.

### Step 6

Proceed by pressing the Next button and add the MySQL Server Configuration which will be the first one downloaded. 

Proceed with all of the remaining steps by pressing the Next and Finish buttons.

![Configuring MySQL as a service for Windows](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/NpTeawZzTPes-MGfA9gG3g_f9160bc5444744548c0718b68b525ee1_Picture-11.png?expiry=1724630400000&hmac=SEGJf_ci6DVPskgf2JivCLz9jveefjuZjQf2Lm8jD44)

![Permission configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/a6SHQuKKQ6Cv5iU4BQIUvA_916a5412f0c244918ae80f7aff4812e1_Picture-12.png?expiry=1724630400000&hmac=QsIKHmdql7Guu_ctzyNRtECxy3omYpUWVjF2VC98_nc)

![Permission setup is complete](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/X82UZXqcTR2tmtkPWcbzcw_8e973b4842924380862493f9c76f2fe1_Picture-14.png?expiry=1724630400000&hmac=VxZ4cJy3V72LdsxyCIBV_J5j2NqVtP0Ey_-SDLbNOYk)

![Product configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Vk0MiAcyT7qU3vjNPawC6Q_0ad352baba4d40e9b393a73fd64162e1_Picture-15.png?expiry=1724630400000&hmac=DHwMDYomfB1ntstSoZyNAhp1NhTB_P-bnLNIYFUnq2Q)

![MySQL router configuration window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/BloKHe__RHK0spKbpMQpjg_e9653a2091464df3b987e1b752e477e1_Picture-16.png?expiry=1724630400000&hmac=15n5QSH_LMMrNpqa791oqT_aM8TXnm1SHMhSU1KTEes)

### Step 7

When you come to the screen below, add the root password you configured a few steps back during the installation. 

![MySQL connection check window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/Ah2d2ryUSnWEurzMJKp5UQ_430973b092754347a3262b46c7e8b9e1_picture-17.png?expiry=1724630400000&hmac=13nUC__fF9vg94byXR0bHK-YIa_CvJXI7Qt3As2guSU)

Proceed with all of the remaining steps by pressing the Next button and then Finish, keeping the default settings in place.

![MySQL connection check window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/dGhFRYEDSpieXOUcMFxrEQ_09686ab5e0c148d5b64e6370c483fbe1_Picture-18.png?expiry=1724630400000&hmac=Axn_iUieW5Dd9NHS66sD8SiGT8bQhQJ5nr1KOW_mS_8)

![Confirmation of the setup was complete and everything is ok.](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/h_O5hQBhRxiocvOiyRQAjw_18ec5d4a7d374315a37fef3c25665fe1_Picture-19.png?expiry=1724630400000&hmac=dsInZtVH8ZLIs5weRqwP2Uxf83D1rO_KK-GtHbxTtv4)

### Step 8

On the final page on the Installer, press the Finish button to complete the installation.

This will open two applications, MySQL Workbench and the command prompt logged into the MySQL shell, on your desktop as in the images below: 

![MySQL Workbench window](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/ghQJVpsvRFmOrfDt_HWVAQ_a56855c1b9f048a595fe356376c26be1_Picture-20.png?expiry=1724630400000&hmac=u6tAHnl3KpR2eN76_TgrM6F0QxYyHLVoZX5mRpdVGKY)

![Accessing MySQL from the command line](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/fLNMkqRAT_aHBifUgJtNKQ_58283312dac9471ab2681946cba8e7e1_Picture-21.png?expiry=1724630400000&hmac=vMvmfdzwFq-KahKH7rsXYalEURSkGBo3WovlDnC9j5o)

Note: *In case you encounter some problems during the installation, there are additional installation-specific details available on the* [*MySQL Windows installation page*](https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html)