"""Simulator run.

Usage:
  stdfrerunwithnewlimits --limit=<limit_file> --stdf-in=<stdf_file_name_in> --stdf-out=<stdf_file_name_out>

Options:
  -h --help     Show this screen.
"""


from docopt import docopt
import bz2
import gzip
import ams_rw_stdf_writer
import ams_rw_stdf
import construct.core
import rich.console

console = rich.console.Console()


_opener = {"bz2": bz2.open, "gz": gzip.open, "stdf": open}

_singleton_entries = {(0, 10): False,
                      (1, 10): False}

if __name__ == '__main__':
    main()

def main():
    arguments = docopt(__doc__)
    ams_rw_stdf_writer.load_limit_file(arguments["--limit"])
    so = arguments["--stdf-out"]
    si = arguments["--stdf-in"]
    with _opener[si.split(".")[-1]](si, "rb") as f, _opener[so.split(".")[-1]](so, "w+b") as out_f:
        while True:
            try:
                c = ams_rw_stdf.RECORD.parse_stream(f)
            except construct.core.StreamError:
                if "stream read less than specified amount, expected 2, found 0" not in str(e):
                    console.print(e)
                break

            if (c.REC_TYP, c.REC_SUB) in _singleton_entries.keys():
                if _singleton_entries[(c.REC_TYP, c.REC_SUB)] == False:
                    out_f.write(ams_rw_stdf.RECORD.build(c))
                _singleton_entries[(c.REC_TYP, c.REC_SUB)] = True
            elif c.REC_TYP == 5 and c.REC_SUB == 10:
                ams_rw_stdf_writer.start_sample((out_f, None))
            elif c.REC_TYP == 5 and c.REC_SUB == 20:
                PART_ID = (c.PL["PART_ID"])
                console.print("Finished part: {PART_ID}")
                ams_rw_stdf_writer._finish_sample((out_f, None), PART_ID)
            elif c.REC_TYP == 15 and c.REC_SUB == 10:
                try:
                    print("retest")
                    ams_rw_stdf_writer.test_value_between((out_f, None), c.PL.TEST_NUM, c.PL.TEST_TXT, c.PL.RESULT)
                except Exception as e:
                    console.print(e)
            else:
                out_f.write(ams_rw_stdf.RECORD.build(c))
