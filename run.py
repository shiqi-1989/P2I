import subprocess

# shell = 'pyinstaller --add-data "config.ini:." --add-data "xiongmao.webp:." -F -w -n ' \
#         'AndroidTools main.py -y'
shell = 'pyinstaller --add-data "logo48.png:." --add-data "logo256.png:." -i logo48.png -n ' \
        'PDFTools -w -D main.py -y'
subprocess.run(shell)
