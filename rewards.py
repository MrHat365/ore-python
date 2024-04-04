"""
  @ Author:   Mr.Hat
  @ Date:     2024/4/4 23:16
  @ Description: 查询是否mint成功，以及数量
  @ History:
"""
import subprocess

d = [
    "./ore --keypair 私钥 rewards",
    "./ore --keypair 私钥 rewards",
    "./ore --keypair 私钥 rewards",
    "./ore --keypair 私钥 rewards",
    "./ore --keypair 私钥 rewards",
    "./ore --keypair 私钥 rewards",
]

for item in d:
    try:
        subprocess.call(f"{item}", shell=True)
    except:
        pass
