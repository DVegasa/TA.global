import concurrent.futures

import fetching.camcatalog as cams
import fetching.file_manager as files

tag = "main"


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(files.grab_and_write)
        executor.submit(cams.powernet[0].start)


if __name__ == '__main__':
    main()
