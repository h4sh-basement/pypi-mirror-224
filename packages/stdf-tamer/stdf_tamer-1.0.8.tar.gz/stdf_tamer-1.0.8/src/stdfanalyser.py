"""List records in sbtdf file.

Usage:
  stdfanalyse <stdf_file_name_in>

Options:
  -h --help     Show this screen.
"""


import ams_rw_stdf
import bz2
import construct
import construct.lib
from docopt import docopt
import gzip
from rich.console import Console


_opener = {"bz2": bz2.open, "gz": gzip.open, "stdf": open}
construct.lib.setGlobalPrintFullStrings(True)

def main():
    console = Console()
    arguments = docopt(__doc__)
    si = arguments["<stdf_file_name_in>"]
    with _opener[si.split(".")[-1]](si, "rb") as f:
        parser = ams_rw_stdf.compileable_RECORD.compile()
        while True:
             b = ams_rw_stdf.get_record_bytes(f)
             c = parser.parse(b)
             console.print(str(c))
             if c.REC_TYP == 1 and c.REC_SUB == 20:
                 break


if __name__ == '__main__':
    main()
