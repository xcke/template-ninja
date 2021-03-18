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
```
conda activate
git clone https://github.com/xcke/template-ninja.git
cd template-ninja
pip install -r requirements.txt
```
Usage of the script: 

```
python main.py --help
usage: main.py [-h] [-D] [-n NAME] [-v] [--version] template input

positional arguments:
  template              Name of the template from the Templates dir
  input                 Input CSV file

optional arguments:
  -h, --help            show this help message and exit
  -D, --debug
  -n NAME, --name NAME
  -v, --verbose         Verbosity (-v, -vv, etc)
  --version             show program's version number and exit
(xml-templating) area-x51:xml-templating xcke$ 
```
