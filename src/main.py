import sys

from extractor.logger import Logger


logger = Logger.create(__name__)

def run(csv_file: str):
    logger.info(f"Run. CSV file: {csv_file}")



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("No arguments no work to do")
        sys.exit(1)

    file_ = sys.argv[1]

    import os
    if not os.path.exists(file_):
        file_ = os.path.join(os.getcwd(), file_)
        if not os.path.exists(file_):
            print(f'File not found: "{file_}".')
            sys.exit(1)

    run(file_)



