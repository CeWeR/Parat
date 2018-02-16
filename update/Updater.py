#
# Copyright(c) 2017, micle(@micle_fm - www.micle.ir - mhd.ceh8@gmail)
# Parat project is under the GNU GENERAL PUBLIC LICENSE (GPL) license.
# see the COPYING file for the detailed licence terms
#

from os.path import abspath, join, dirname
from lib.ParatPrint import colorize, pprint

try:
    from ConfigParser import ConfigParser
    from urllib2 import urlopen
except ModuleNotFoundError:
    from configparser import ConfigParser
    from urllib.request import urlopen


__version__ = '1.1'

def check_update():

    root_path = abspath(join(dirname(__file__)))

    parser = ConfigParser()
    path_to_config = join(root_path, "..", "conf", "config.ini")

    with open(path_to_config, 'r') as config:
        parser.readfp(config)
    config.close()

    color_mode  = parser.get('cmd', 'colors').lower()
    colored     = True if color_mode == "on" else False

    try:

        updateurl = 'https://raw.githubusercontent.com/micle-fm/Parat/master/conf/parat.version'
        request = urlopen(updateurl)
        parat_version = request.read().rstrip('\n')
        request.close()

    except:

        path_to_version_file = join(root_path, "..", "conf", "parat.version")
        with open(path_to_version_file, 'r') as ver_file:
            parat_version = ver_file.read().rstrip('\n')
        ver_file.close()

    if parat_version != __version__:
        pprint(
            colorize(
                    " New version aviable on https://github.com/micle-fm/parat \n",
                    colored=colored,
                    status="WAR"
                ))
