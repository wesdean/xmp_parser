import sys
from os.path import abspath, basename
from pathlib import Path
from libxmp.utils import file_to_dict


def parse_xmp(filename: str) -> dict:
    return file_to_dict(filename)


def extract_created_date(xmp: dict) -> str:
    if 'http://ns.adobe.com/xap/1.0/' not in xmp:
        return ''

    for elem in (xmp['http://ns.adobe.com/xap/1.0/']):
        if elem[0] == 'xmp:CreateDate':
            return elem[1]


if __name__ == '__main__':
    print()
    for arg in sys.argv[1:]:
        filename = str(Path(arg).expanduser().resolve())
        xmp = parse_xmp(filename)
        created_date = extract_created_date(xmp)
        print('{filename}: {created_date}'.format(filename=basename(filename), created_date=created_date))
