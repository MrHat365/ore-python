"""
  @ Author:   Mr.Hat
  @ Date:     2024/4/4 18:46
  @ Description: 
  @ History:
"""
import asyncio
import os
from loguru import logger
from keypair import Keypair


async def create_account(amount, file_name, save=True):
    """ 创建Solana钱包账户
    :param amount: 需要创建的钱包账户数量
    :param file_name: 需要存储的txt文件名称，名称包含".txt"
    :param save: 是否存储为文件类型，True为存储，False为不存储文件类型，这里是为了方便下方自动生成账户，自动邀请逻辑自行处理
    :return:
    """
    accounts = []
    for i in range(amount):
        new_account = Keypair()
        accounts.append(new_account)

    if save:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, "wallets", file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            for wallet_data in accounts:
                file.write(f"{wallet_data.public_key},{wallet_data.private_key}\n")

            file.close()
            logger.success(f"生成钱包成功, 数量为: {amount},  存放目录： {file_path}")
    else:
        return accounts


if __name__ == '__main__':
    asyncio.run(create_account(5, file_name="account.txt"))