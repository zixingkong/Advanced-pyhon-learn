# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_01
   Description :
   date：          2022/3/24
-------------------------------------------------
"""

# 运行协程的3种主要机制
#   1.asyncio.run()
#   2.等待一个协程
#   3.asyncio.create_task()用来并发运行作为asyncio任务的多个协程
import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    main()
    # asyncio.run(main())
