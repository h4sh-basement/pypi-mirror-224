import os
import sys
from tempfile import TemporaryDirectory
import json
import random
import gallery_dl

META_FOLDER = 'metadata'

metadata_args = ["--write-metadata", "--postprocessor-option", f"directory={META_FOLDER}"]


def _download_gallery_metadata_and_extract_gallery_dir(url, gallery_dl_meta_args, logger):
    '''Download a metadata json file of the gallery'''
    with TemporaryDirectory() as dirname:
        filename = os.path.join(dirname, 'temp.txt')
        sys.argv = [
            "gallery_dl", "--no-download", "--range", "1",
            "--exec-after", "echo {} > %s" % filename,
            *metadata_args, *gallery_dl_meta_args, url
        ]
        logger.debug(f"Exec: {sys.argv}")
        returncode = gallery_dl.main()
        if returncode != 0 or not os.path.isfile(filename):
            raise ValueError("Cannot get gallery by gallery-dl")
        with open(filename, encoding='utf8') as fp:
            gallery_dir = os.path.join(fp.read().strip())
            # ↓↓↓↓↓↓↓↓ for stupid windows ↓↓↓↓↓↓↓↓
            if gallery_dir[0] == '"':
                gallery_dir = gallery_dir[1:]
            if gallery_dir[-1] == '"':
                gallery_dir = gallery_dir[0:-1]
            if gallery_dir[0:4] == '\\\\?\\':
                gallery_dir = gallery_dir[4:]
            # ↑↑↑↑↑↑↑↑ for stupid windows ↑↑↑↑↑↑↑↑
            gallery_dir = os.path.join(gallery_dir)
    return gallery_dir


def _get_gallery_metadata_filenames(gallery_dir):
    metafiles = []
    meta_folder = os.path.join(gallery_dir, META_FOLDER)
    os.makedirs(meta_folder, exist_ok=True)
    for file in os.listdir(meta_folder):
        if os.path.splitext(file)[1] == '.json':
            metafiles.append(file)
    return metafiles


def _get_gallery_metadata_files_path(gallery_dir):
    meta_folder = os.path.join(gallery_dir, META_FOLDER)
    return [os.path.join(meta_folder, file) for file in _get_gallery_metadata_filenames(gallery_dir)]


def _try_get_gallery_one_metadata_from_dir(gallery_dir, logger):
    '''Read a json file in the gallery metadata json files'''
    if gallery_dir is not None:
        metafiles = _get_gallery_metadata_files_path(gallery_dir)
        if len(metafiles) > 0:
            metafile = metafiles[random.randint(0, len(metafiles) - 1)]
            try:
                with open(metafile, encoding='utf8') as fp:
                    return json.load(fp)
            except Exception as e:
                logger.error(f"Cannot load exist json file {metafile}: {e}")


def get_gallery_one_metadata(url, gallery_dir, config, logger):
    '''Get a metadata of a gallery'''
    meta = _try_get_gallery_one_metadata_from_dir(gallery_dir, logger)
    if not meta:
        gallery_dir2 = _download_gallery_metadata_and_extract_gallery_dir(url, config["gallery-dl-meta-args"], logger)
        if gallery_dir is None:
            gallery_dir = gallery_dir2
        if os.path.abspath(gallery_dir) != os.path.abspath(gallery_dir2):
            raise ValueError(f"gallery_dir not match: {gallery_dir} != {gallery_dir2}")
    meta = _try_get_gallery_one_metadata_from_dir(gallery_dir, logger)
    if not meta:
        raise ValueError(f"Cannot get metadata: {url, gallery_dir}")
    return meta
