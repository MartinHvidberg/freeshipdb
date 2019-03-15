
import sys

def main(imo):
        print('Showing info for IMO: {}'.format(imo))

if __name__ == '__main__':

    if sys.argv and len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print('Please indicate IMO number')