import subprocess as sp
import os
import click


class StClass():
    """Main class for stuff """
    p = os.path.dirname(os.path.realpath(__file__))
    bashscript = str(p)+'/samtools_view.sh'

    def runbams(self, bamfile, region, outputfile):
        """run samtools view"""
        sp.call(['{}'.format(self.bashscript),
                 '{}'.format(bamfile),
                 '{}'.format(region),
                 '{}'.format(outputfile)])


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
def main(inputfile, region, outputfile):
    sc = StClass()
    sc.runbams(inputfile, region, outputfile)


if __name__ == '__main__':
    main()
