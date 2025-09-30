import paramiko

# SSH server details
hostname = 'ec2-52-91-13-88.compute-1.amazonaws.com'
username = 'ubuntu'
password = 'arduinio_py.pem' # Or use key_filename for key-based authentication

# Create an SSH client instance
ssh_client = paramiko.SSHClient()

# Automatically add the server's host key (not recommended for production without proper host key verification)
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the SSH server
    ssh_client.connect(hostname=hostname, username=username, key_filename=password)

    # Execute a command
    command = 'cd Arduino_rgb && ls -l && source .venv/bin/activate'
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Read the standard output
    output = stdout.read().decode('utf-8')
    print("Standard Output:")
    print(output)

    # Read the standard error
    error = stderr.read().decode('utf-8')
    if error:
        print("Standard Error:")
        print(error)

except paramiko.AuthenticationException:
    print("Authentication failed. Check your username and password or SSH keys.")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the SSH connection
    ssh_client.close()