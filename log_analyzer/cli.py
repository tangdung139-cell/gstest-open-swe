import click

def parse_logs(logfile, output):
    from log_analyzer.parser import LogParser

    parser = LogParser()
    parser.parse_file(logfile)
    counts = parser.get_counts()

    with open(output, 'w') as csvfile:
        csvfile.write('Type,Count\n')
        for log_type, count in counts.items():
            csvfile.write(f'{log_type},{count}\n')

@click.command()
@click.argument('logfile', type=click.Path(exists=True))
@click.option('--output', default='report.csv', help='Output CSV file')
def main(logfile, output):
    """Simple CLI for analyzing logs."""
    parse_logs(logfile, output)
    click.echo(f'Analysis complete. Report saved to {output}')

if __name__ == '__main__':
    main()