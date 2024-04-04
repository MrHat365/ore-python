<h1 align="center"> Ore挖矿 Python脚本版本 </h1>
<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.11-fadf6f"> </a>
  <a href="https://twitter.com/Crypto0xM"> <img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FCrypto0xM">
  </a>
</p>

---

### 打码平台
[Captcha.run](https://captcha.run/sso?inviter=766e7788-4ff4-47b6-b991-93ac43dbbfae)

[Yes Captcha!](https://yescaptcha.com/i/Sy4ti1)

[NoCaptcha.io](https://www.nocaptcha.io/register?c=W9SAq9)

[OKX注册地址](https://www.ouxyi.style/join/TOTHEMOON25)

---
## 👨‍💻‍说明
- 社区很多人对shell脚本使用都有一点问题
- 基础环境配置有难度
- 钱包管理莫名的各种问题

---
## 👨‍💻‍使用教程 [OKX注册地址](https://www.ouxyi.style/join/TOTHEMOON25)
```shell
# 一、Rust环境安装
如果是Mac和Linux用户非常简单，参考这篇文章，https://www.rust-lang.org/zh-CN/tools/install 一路下一步。
Windows用户其实也比较方便。https://juejin.cn/post/7219656530235670588 参考这篇文章。

# 二、克隆脚本，然后编译可用变量，这里建议自己编译，很简单，没那么复杂。
git clone https://github.com/Klinola/ore-cli.git
cd ore-cli
cargo build --release
cd target/release/

git clone https://github.com/MrHat365/ore-python.git
生成你需要的钱包私钥数量
在create_account.py文件中
asyncio.run(create_account(5, file_name="account.txt"))

对应的钱包地址会出现在wallets/account.txt中。格式为  [地址,私钥]

往需要执行的地址充值0.04个sol。
然后执行如下命令：
python start.py
```

```python
import subprocess

# RPC地址可以通过一下注册获取 https://www.alchemy.com/，申请solana的地址
# 私钥通过刚才生成的wallets/account.txt获取对应的私钥，粘贴进来。
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
            """
                subprocess.Popen说明：
                subprocess.call方法是，一行一行的执行，也就是，一个任务完成了再去完成下一个任务。
                Popen方法则不同，他会同时执行d列表中的所有任务，针对多现成模式来说，需要更高的电脑配置，以及性能要求。所以慎用。会卡！
                由于ore是每分钟只能mint一次，所以如果使用Popen方法需要携带等待时间。time.sleep(60)
            """
        except:
            pass
```

针对多个RPC的配置说明。
你可以复制多个start.py文件，通过不同的配置来实现。每个start.py文件都配置不同的rpc，使用方法都是`python start.py`

### 补充一点，很多人反应，while True 快捷键很难停掉
这里补充一下，可以使用 `ps -aux | grep python` 就可以看到
```shell
root     2411340  0.0  0.0  17808  9212 pts/14   S+   12:01   0:00 python3 strart.py
root     2411375  0.0  0.0  17808  9356 pts/16   S+   12:01   0:00 python3 strart1.py
root     2411447  0.0  0.0  17808  9316 pts/13   S+   12:02   0:00 python3 strart2.py
root     2411482  0.0  0.0  17808  9396 pts/12   S+   12:02   0:00 python3 strart3.py
root     2411519  0.0  0.0  17808  9308 pts/17   S+   12:02   0:00 python3 strart4.py
root     2411536  0.0  0.0  17808  9432 pts/15   S+   12:02   0:00 python3 strart5.py
```
类似于上方的终端命令，这里是需要使用`kill -9 2411340 2411375 2411447 2411482`回车即可。


### 🐹 更多其他脚本请关注首页
#### [Sollong脚本](https://github.com/MrHat365/sollong_daily_task.git)
#### [starrynift脚本](https://github.com/MrHat365/starrynift.git)

<p align="center">
  <a href="https://twitter.com/Crypto0xM"> <img width="120" height="38" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FCrypto0xM"/>
  </a>
</p>
