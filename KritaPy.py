import zipfile
import argparse
from PIL import Image
import io
from os.path import isfile, splitext


def extractMergedImageFromKRA(kra):
    archive = zipfile.ZipFile(kra,'r')
    extract_image = archive.read('mergedimage.png')
    image = Image.open(io.BytesIO(extract_image))
    return image


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Basic operations for Krita .kra files")
    argparser.add_argument('input', help='File to import, must be KRA')
    argparser.add_argument('output', help='File to output to')
    argparser.add_argument('--mode',help='Mode of output image, eg, "RGBA". If not specified, mode will not be converted.')

    arguments = argparser.parse_args()

    def output_file(image):
        if arguments.mode:
            image = image.convert(arguments.mode)
        image.save(arguments.output)


    if isfile(arguments.input):
        if splitext(arguments.input)[1].lower() == '.kra':
            kra_merged = extractMergedImageFromKRA(arguments.input)
            output_file(kra_merged)