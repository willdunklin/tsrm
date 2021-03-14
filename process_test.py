import psutil

# https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
def checkIfProcessRunning(contains):
    # iterate over the all the running process
    for p in psutil.process_iter():
        try:
            if contains.lower() in p.name().lower():
                return p.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return -1

minecraft_pid = checkIfProcessRunning('java')
print('minecraft pid:', minecraft_pid)

def exists():
    return psutil.pid_exists(minecraft_pid)