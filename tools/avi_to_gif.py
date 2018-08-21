import argparse
import imageio
import os, sys

GIF = "gif"
MP4 = "mp4"
AVI = "avi"

parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Specify the format to convert to.")
parser.add_argument("format", help="Specify the format to convert to. Options are: avi, gif, mp4")
arguments = parser.parse_args()

def convertVideo(inFile, targetFormat):

    outPath = os.path.splitext(inFile)[0] + '.' + targetFormat

    print 'Attempting to convert {} to {} format.'.format(inFile, targetFormat)

    reader = imageio.get_reader(inFile)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outPath, fps=fps)
    for i,im in enumerate(reader):
        print 'Writing frame {}'.format(i)
        writer.append_data(im)
    writer.close()
    print("Video successfully converted.")

convertVideo(arguments.filepath, arguments.format)