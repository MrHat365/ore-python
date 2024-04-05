<h1 align="center"> Ore挖矿 Windows懒人包 </h1>
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
## 👨‍💻‍使用说明
mining.bat是每个私钥一个bat文件，如果你有一个rpc，一个私钥，那么就一个bat文件，如果你有两个rpc，一个私钥就设置两个bat文件，如果你有两个rpc，两个私钥，那么就是四个bat文件。
  
  比如：你现在的rpc是 https://xxx.com, 和 https://yyy.com, 私钥是 xxx, yyy
  那么你就需要复制四个bat文件，我们命名为, x_y_1.bat, x_y_2.bat, x_y_3.bat, x_y_4.bat
  每个bat的内容为：

  ```shell
    @echo off
    for /l %%i in (1, 1, 100) do (
        ore --rpc 节点 --keypair 私钥 --priority-fee 5000000 mine --threads 50
    )
    pause
```
节点换成你的节点，私钥换成你的私钥，也就是每个bat文件对应一个节点，对应一个私钥，两个rpc，两个私钥也就是4个排列组合方式。


claim.bat的使用说明。
claim其实是用来收回你的token的，这里对rpc无要求，唯一的就是你的私钥需要按时收回token。
```shell
  @echo off
  for /l %%i in (1, 1, 100) do (
      ore --rpc 节点 --keypair 私钥 claim
  )
  pause
```
这里需要说明的是，和mining.bat不同的是，这里的rpc只需要可用就行了，不需要复制多个bat文件，一个就能解决，私钥是一个一行，如果你有四个私钥，那么代码应该长这样子。
```shell
  @echo off
  for /l %%i in (1, 1, 100) do (
      ore --rpc 节点 --keypair 私钥 claim
      ore --rpc 节点 --keypair 私钥 claim
      ore --rpc 节点 --keypair 私钥 claim
      ore --rpc 节点 --keypair 私钥 claim
  )
  pause
```
以此类推。

不同的是，mining.bat可能是很多个文件，因为你有很多rpc和私钥，通过排列组合的防止进行组合。但是claim只有一个bat文件。

---

### 🐹 更多其他脚本请关注首页
#### [Sollong脚本](https://github.com/MrHat365/sollong_daily_task.git)
#### [starrynift脚本](https://github.com/MrHat365/starrynift.git)

<p align="center">
  <a href="https://twitter.com/Crypto0xM"> <img width="120" height="38" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Ftwitter.com%2FCrypto0xM"/>
  </a>
</p>
