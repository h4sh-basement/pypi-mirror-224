import argparse
import logging
import json
import os


def build_parser():
    """Build and configure an ArgumentParser object"""
    parser = argparse.ArgumentParser(usage="%(prog)s [OPTION]... URL...")

    general = parser.add_argument_group("General Options")
    general.add_argument(
        "-c", "--config",
        dest="config", type=str,
        help="Path to config json file",
        default='config.json',
    )
    output = parser.add_argument_group("Output Options")
    output.add_argument(
        "-q", "--quiet",
        dest="loglevel", default=logging.INFO,
        action="store_const", const=logging.ERROR,
        help="Activate quiet mode",
    )
    output.add_argument(
        "-v", "--verbose",
        dest="loglevel",
        action="store_const", const=logging.DEBUG,
        help="Print various debugging information",
    )
    parser.add_argument(
        "urls", nargs="*",
        help=argparse.SUPPRESS,
    )

    return parser

config = {
    # Root for the gallery
    "gallery-root": None,
    # Regular expression to extract path of the file from URL
    "path-re": "^https://e[-x]hentai.org/g/([0-9]+)/[0-9a-z]+/*$",
    # if specified "gallery-root" and valid "path-re", get_gallery_dir_by_re will be used to get path

    # Args for running gallery-dl commandline program
    "gallery-dl-args": [],
    # Args for running gallery-dl commandline program for meta extraction
    "gallery-dl-meta-args": [],
}

def read_config(args, logger):
    if os.path.isfile(args.config):
        try:
            with open(args.config, encoding='utf8') as f:
                override = json.load(f)
                for k in config:
                    if k in override:
                        config[k] = override[k]
        except Exception as e:
            logger.warn("Cannot read config %s: %s" % (args.config, e))
    logger.info("Config: %s" % config)
    return config