# def get_url(url):
#     #do someting 1
#     html = get_html(url) #此处暂停，切换到另一个函数去执行
#     # #parse html
#     urls = parse_url(html)
#
# def get_url(url):
#     #do someting 1
#     html = get_html(url) #此处暂停，切换到另一个函数去执行
#     # #parse html
#     urls = parse_url(html)

# 传统函数调用 过程 A->B->C
# 我们需要一个可以暂停的函数，并且可以在适当的时候恢复该函数的继续执行
# 出现了协程 -> 有多个入口的函数， 可以暂停的函数， 可以暂停的函数(可以向暂停的地方传入值)


# 回调之痛：
# 	可读性差
# 	共享状态管理困难
# 	异常处理困难

# C10M问题：如何利用8核心CPU，64G内存，在10gbps的网络上保持1000万并发连接

# 问题：
# 1.回调模式编码复杂度高
# 2.同步编程的并发性不高
# 3.多线程编程需要线程间同步，lock

# 解决方案：
# 1.采用同步的方式去编写异步的代码
# 2.使用单线程去切换任务
# 	线程是由操作系统切换的，单线程切换需要程序员自己去调度任务
# 	不再需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性更高


def gen_func():
    # 1. 可以产出值， 2. 可以接收值(调用方传递进来的值)
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"


# 1. throw, close，send


# 1. 生成器不只可以产出值，还可以接收值


if __name__ == "__main__":
    gen = gen_func()
    # 在调用send发送非none值之前，我们必须启动一次生成器， 方式有两种1. gen.send(None), 2. next(gen)
    url = gen.send(None)
    # gen.close()
    # download url
    html = "bobby"
    print(gen.send(html))  # send方法可以传递值进入生成器内部，同时还可以重启生成器执行到下一个yield位置
    print(gen.send(html))
    # 1.启动生成器方式有两种， next(), send

    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))
