"""
    To connect with an Ubuntu instance in GCP
    over ftp with paramiko Python package
"""
import paramiko

k = paramiko.RSAKey.from_private_key_file(r"C:\keys\gcp_privated.ppk")
transport = paramiko.Transport(("35.199.62.187", 22))
transport.connect(username = "qsandbox",pkey=k)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.listdir('/home/andres_gutierrez_arcia/andres')
pass

