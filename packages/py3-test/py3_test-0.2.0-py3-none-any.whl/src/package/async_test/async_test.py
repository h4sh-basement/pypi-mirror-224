"""
@author: lijc210@163.com
@file: asyncio_test.py
@time: 2020/04/22
@desc: 功能描述。
"""
import asyncio
import time


# 定义异步函数
async def hello():
    print("Hello World:%s" % time.time())
    # 必须使用await，不能使用yield from；如果是使用yield from ，需要采用@asyncio.coroutine相对应
    await asyncio.sleep(1)
    print("Hello wow World:%s" % time.time())


def run():
    tasks = []
    for _i in range(5):
        tasks.append(hello())
    loop.run_until_complete(asyncio.wait(tasks))


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    run()
