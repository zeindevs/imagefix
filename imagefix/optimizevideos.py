import argparse
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog='optimizevideos',
        description='Video optimization',
        epilog='Thank for using %(prog)s :)',
        argument_default=argparse.SUPPRESS,
    )

    parser.add_argument('-i', '--input', help='Input file', required=True)

    args = parser.parse_args()

    source = Path(args.input)

    if source.is_file():
        if source.suffix.lower() not in ['.mp4', '.mov', '.ts', '.mkv']:
            print(f"The file {source.suffix} extension not valid, requires 'mp4', 'mov', 'ts', 'mkv'")
            raise SystemExit(1)

        print('Optimize: ', source)
        out = source.__str__().replace(source.suffix.lower(), '-out.mp4')
        cmd = f'ffmpeg -hwaccel d3d11va -i "{source}" -preset slow -crf 22 -vcodec h264_amf -c:a copy "{out}"'
        subprocess.run(cmd)

        print('Complete')
        return
    else:
        videos = []

        for suffix in ['.mp4', '.mov', '.ts', '.mkv']:
            videos += source.glob(f'*{suffix}')

        if len(videos) > 0:
            for idx, video in enumerate(videos):
                print(f'[{idx+1}/{len(videos)}] Optimize: ', video)
                out = video.__str__().replace(video.suffix.lower(), '-out.mp4')
                cmd = f'ffmpeg -hwaccel d3d11va -i "{video}" -preset slow -crf 22 -vcodec h264_amf -c:a copy "{out}"'
                subprocess.run(cmd)

            print('Complete')
            return

        print("The input file doesn't exist")
        raise SystemExit(1)
