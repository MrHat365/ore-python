"""
  @ Author:   Mr.Hat
  @ Date:     2024/4/4 19:14
  @ Description: 
  @ History:
"""
import subprocess

d = [
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
    "../ore --rpc 你自己的RPC地址 --keypair 私钥 --priority-fee 5000000 mine --threads 20",
]

while True:
    for item in d:
        try:
            subprocess.call(f"{item}", shell=True)
            # subprocess.Popen(d).wait()
        except:
            pass
