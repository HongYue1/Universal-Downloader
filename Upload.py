import os
import subprocess
import time


def Upload(path):
    if (os.path.exists(path)):

        command = [
            'curl', '--upload-file', path,
            'https://transfer.sh/' + os.path.basename(path)
        ]
        # Run the command
        print("The Link: ")
        subprocess.run(command)
    else:
        print("Path doesn't exist!")
        time.sleep(1.5)
