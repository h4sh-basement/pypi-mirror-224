import dataclasses
import json
from typing import List


def _dataclass_from_dict(klass_or_obj, d: dict):
    if isinstance(klass_or_obj, type): # klass
        ret = klass_or_obj()
    else:
        ret = klass_or_obj
    for k,v in d.items():
        if hasattr(ret, k):
            setattr(ret, k, v)
    return ret

'''
config = {
        "curonly": args.curonly,
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        "api": api,
        "failfast": args.failfast,
        "http_method": "POST",
        "index": index,
        "images": args.images,
        "logs": False,
        "xml": args.xml,
        "xmlrevisions": args.xmlrevisions,
        "namespaces": namespaces,
        "exnamespaces": exnamespaces,
        "path": args.path and os.path.normpath(args.path) or "",
        "cookies": args.cookies or "",
        "delay": args.delay,
        "retries": int(args.retries),
    }
'''
@dataclasses.dataclass
class Config:
    def asdict(self):
        return dataclasses.asdict(self)

    # General params
    delay: float = 0.0
    retries: int = 0
    path: str = ''
    logs: bool = False
    date: str = False

    # URL params
    index: str = ''
    api: str = ''

    # Download params
    xml: bool = False
    curonly: bool = False
    xmlapiexport: bool = False
    xmlrevisions: bool = False
    xmlrevisions_page: bool = False
    images: bool = False
    namespaces: List[int] = None
    exnamespaces: List[int] = None

    api_chunksize: int = 0  # arvlimit, ailimit, etc
    export: str = '' # Special:Export page name
    http_method: str = ''

    # Meta info params
    failfast: bool = False

    templates: bool = False

def new_config(configDict) -> Config:
    return _dataclass_from_dict(Config, configDict)

def load_config(config: Config=None, config_filename=""):
    """Load config file"""

    config_dict = dataclasses.asdict(config)

    if config.path:
        try:
            with open(f"{config.path}/{config_filename}", encoding="utf-8") as infile:
                config_dict.update(json.load(infile))
            return new_config(config_dict)
        except FileNotFoundError:
            pass

    raise RuntimeError("There is no config file. we can't resume.")

def save_config(config: Config, config_filename: str):
    """Save config file"""

    with open(f"{config.path}/{config_filename}", "w", encoding="utf-8") as outfile:
        json.dump(dataclasses.asdict(config), outfile, indent=4, sort_keys=True)