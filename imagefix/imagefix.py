import argparse
from pathlib import Path
from PIL import Image


def main():
    parser = argparse.ArgumentParser(
        prog='imagefix',
        description='Image fixer',
        epilog='Thank for using %(prog)s! :)',
        argument_default=argparse.SUPPRESS,
    )

    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-ext', '--extension', help='(jpg, png)', required=True)

    args = parser.parse_args()

    source_dir = Path(args.input)
    extension = args.extension

    if not source_dir.exists():
        print("The target directory doesn't exist")
        raise SystemExit(1)

    if extension not in ['jpg', 'png']:
        print("The file extension not supported")
        raise SystemExit(1)

    images = [x for x in source_dir.glob(f'*.{extension}')]

    if len(images) > 0:
        print(f'Found: {len(images)}\n')

        for idx, image in enumerate(images):
            img = Image.open(image)
            img.save(image)
            print(f"[{idx+1}/{len(images)}] Fix:", image)

        print("\nComplete")
        return

    print("No image found")
    raise SystemExit(1)
