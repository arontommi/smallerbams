import subprocess as sp
import os
import click
import pandas as pd

class StClass():
    """Main class for stuff """

    def __init__(self):
        self.p = os.path.dirname(os.path.realpath(__file__))
        self.bashscript = str(self.p)+'/samtools_view.sh'

    def runbams(self, bamfile, region, outputfile):
        """run samtools view"""
        sp.call(['{}'.format(self.bashscript),
                 '{}'.format(bamfile),
                 '{}'.format(region),
                 '{}'.format(outputfile)])
    def runmultiple(self, csv):
        file = pd.read_csv(csv, header=None)
        for i, r in file.iterrows():
            self.runbams(r[0], r[1], r[2])


@click.command()
@click.option(
    '--region', '-r',
    help='give region to subset. Example : 6:30919168-30919391',
)
@click.option(
    '--inputfile', '-i',
    help='inputfile',
)
@click.option(
    '--outputfile', '-o',
    help='outputfile',
)
@click.option(
    '--csv', '-c',
    help='if multiple files need to be created use a simple csv, no header, with first column being input file,'
         ' second for region and third for outputfile '
)

def main(inputfile, region, outputfile, csv ):
    sc = StClass()
    if csv:
        sc.runmultiple(csv)
    else:
        sc.runbams(inputfile, region, outputfile)


if __name__ == '__main__':
    main()
