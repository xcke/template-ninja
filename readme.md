### Installation

Open a Windows PowerShell with admin privilage and install chocholatey (A windows package manager):

```ps
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

### Installation instructions for Windows:

#### Install required applications using chocholatey

```
choco install miniconda3
choco install git
```

#### Checkout the latest code to desired folder and install deps:

Activate the python env and install dependencies  
`conda activate`  
`git clone https://github.com/xcke/template-ninja.git`  
`pip install -r requirements.txt`

You can start the script for example: `python main.py my_template.xml database.csv`
