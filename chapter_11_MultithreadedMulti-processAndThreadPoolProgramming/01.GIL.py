# GIL：global interpreter lock (cpython)
#  python中一个线程对应于c语言中的一个线程
# GIL使得同一时刻只有一个线程在一个CPU上执行字节码，无法将多个线程映射到多个CPU上
# GIL会根据执行的字节码行数以及时间片释放，GIL在遇到IO操作的时候主动释放
import threading
# import dis
#
#
# def add(a):
# a = a + 1
# return a
#
#
# print(dis.dis(add))

total = 0


def add():
    global total
    for _ in range(1000000):
        total += 1


def desc():
    global total
    for _ in range(1000000):
        total -= 1


if __name__ == "__main__":
    thread1 = threading.Thread(target=add)
    thread2 = threading.Thread(target=desc)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print(total)
