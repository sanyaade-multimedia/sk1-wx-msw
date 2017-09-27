import sys

SCRIPT = "src\\sk1.py"

if len(sys.argv) == 1:
	sys.argv += ['py2exe', ]
elif len(sys.argv) == 2:
	sys.argv[1] = 'py2exe'
	SCRIPT = "src\\sk1_portable.py"
	
print SCRIPT

from distutils.core import setup
import py2exe

from glob import glob
data_files = [("Microsoft.VC90.CRT",
glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

INCLUDES = ['__future__', 'array', 'base64', 'binascii', 'cgi',
'codecs', 'collections', 'colorsys', 'copy', 'datetime',
'errno', 'importlib', 'inspect', 'itertools', 'io', 'fractions', 'functools',
'future_builtins', 'hashlib', 'logging', 'locale', 'math', 'marshal', 'md5',
'mmap', 'new', 'numbers', 'operator', 'os', 'pickle', 'cPickle', 'platform',
'pipes', 'pprint', 'random', 're', 'shutil', 'sets', 'shlex',
'stat', 'StringIO', 'cStringIO', 'shlex', 'socket', 'string', 'struct',
'subprocess', 'sys', 'tempfile', 'textwrap', 'time', 'traceback', 'types',
'unicodedata', 'urllib', 'urllib2', 'warnings', 'weakref', 'webbrowser',
'xml.dom', 'xml.sax', 'zipimport', 'zipfile', 'zlib', ]

setup(
	options={'py2exe': {'bundle_files': 3,
						'compressed': True,
						'includes':INCLUDES,
						}},
	windows=[{'script': SCRIPT,
# 	console=[{'script': SCRIPT,
			"icon_resources": [(1, "src\\sk1.ico")]
			}],
	data_files=data_files,
	zipfile=None,
	name="sK1",
	version="2.0RC2",
	description="Vector graphics editor",
	)
