import platform
import sys

import pyinstaller.__main__

OS = platform.system()

if OS == 'Windows':
    pyinstaller.__main__.run([
        'twitchTransFN.py',
        '--clean',
        '--onefile',
        '--hidden-import=pywin32',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=twitchTransFN.exe'
    ])
elif OS == 'Darwin':
    pyinstaller.__main__.run([
        'twitchTransFN.py',
        '--clean',
        '--onefile',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=twitchTransFN.command'
    ])
elif OS == 'Linux':
    pyinstaller.__main__.run([
        'twitchTransFN.py',
        '--clean',
        '--onefile',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=twitchTransFN'
    ])
else:
    sys.exit(1)
