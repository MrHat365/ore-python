@echo off
for /l %%i in (1, 1, 100) do (
    ore --rpc 节点 --keypair 私钥 --priority-fee 5000000 mine --threads 50
)
pause