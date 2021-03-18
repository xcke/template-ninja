1. Installation

Open a Windows PowerShell with admin privilage and install chocholatey (A windows package manager):

```ps
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

2. Install some programs:

˙˙˙
choco install miniconda3
choco install git
˙˙˙ 3. Checkout the latest code to desired folder and install deps:

Activate the python env
`conda activate`
`git clone https://github.com/xcke/xml-template.git`
`pip install -r requirements.txt`
