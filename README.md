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

```

`wallets.txt`是需要填写转出目标地址列表，一行一个。

## 👨‍💻更新功能 [OKX注册地址](https://www.ouxyi.style/join/TOTHEMOON25)
更新交易所提现-划转功能。

- 更新交易所提现时候出现的异常处理
- 更新钱包多余资产转回交易所功能

参数说明：
```shell
交易所私钥配置参数：
API_KEY = ''  # 交易所api key
SECRET = ''  # 交易所 api secret
PASSPHRASE = ''  # okx交易所 passphrase

从交易所转出，公链配置参数
TOKEN = 'ZETA'  # token种类
NETWORK = 'ZetaChain'  # 公链名称

AMOUNT = 2  # 需要转出的zeta数量，okx当前默认为2个，也可以自定义

划转延时配置参数
MIN_DELAY = 20  # token提现最小延时时间
MAX_DELAY = 50  # token提现最大延时时间

多余资产转回交易所配置参数
RESERVED_AMOUNT = 0.1  # 钱包需要保留的token数量
EXCHANGE_ADDRESS = ""  # 需要转到交易所的充币地址

```
新增`data/temp_wallets.txt`文件，辅助交易所转账，可以将需要转回交易所的钱包私钥放置在对应的文件中，方便自动转回。

### 注意：okx提现需要添加地址白名单，这里只能手动添加。无法自动完成。添加玩白名单之后才可以进行脚本操作。



### 🐹 更多其他脚本请关注首页
#### [Sollong脚本](https://github.com/MrHat365/sollong_daily_task.git)
#### [starrynift脚本](https://github.com/MrHat365/starrynift.git)

<p align="center">
  <a href="https://twitter.com/Crypto0xM"> <img width="120" height="38" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FCrypto0xM"/>
  </a>
</p>
