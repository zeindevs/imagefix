import argparse
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog='tsconvert',
        description='Video converter .ts to .mp4',
        epilog='Thank for using %(prog)s :)',
        argument_default=argparse.SUPPRESS,
    )

    parser.add_argument('-i', '--input', help='Input file', required=True)

    args = parser.parse_args()

    source = Path(args.input)

    if source.is_file():
        if source.suffix != '.ts':
            print(f"The file {source.suffix} extension not valid, requires .ts")
            raise SystemExit(1)

        print('Convert: ', source)
        output = source.__str__().replace('.ts', '.mp4')
        subprocess.run(f'ffmpeg -i "{source}" -codec copy "{output}"')

        print('Complete')
        return

    if source.is_dir():
        videos = [x for x in source.glob('*.ts')]

        if len(videos) > 0:
            for idx, video in enumerate(videos):
                print(f'[{idx+1}/{len(videos)}] Convert: ', video)
                output = video.__str__().replace('.ts', '.mp4')
                subprocess.run(f'ffmpeg -i "{video}" -codec copy "{output}"')

            print('Complete')
            return

    print("The input file doesn't exist")
    raise SystemExit(1)
