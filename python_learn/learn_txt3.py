import multiprocessing as mp
import threading, queue
import time
print({
    "并发与网络": {
        "I/O限制": "计算机的CPU速度非常快",
        "CPU限制": "在处理数字运算任务时, 如科学计算或图形计算",
    },
    "同步": "一件事接着一件事发生",
    "异步": "任务是互相独立的",
    "队列/FIFO(先进先出)": {
        "task_done()": "每一个get()调用到的任务,\
                        通过task_done()调用告诉队列该任务已处理完毕",
        "join()": "阻塞调用线程, 直到队列中的所有任务被处理掉",
        "put()": "将item放入队列中, timeout参数可设置超时",
        "get()": "从队列中移除并返回一个数据, timeout参数可设置超时",
        "empty()": "如果队列为空, 返回True, 反之为False",
        "full()": "判断队列是否为满, 满则返回True, 反之为False",
        "qsize()": "返回当前队列有多少成员",
        "maxsize()": "返回队列的最大长度",
    },
    "gevent": {
        "gethostbyname()": "同步函数",
        "spawn()": "为每个gevent.socket.gethostbynome(url)创建一个绿色线程",
    },
    "asyncio": "http://legacy.python.org/dev/peps/pep-3156/",
    "celery": "http://www.celeryproject.org/",
    "thoonk": "https://github.com/andyet/thoonk.py",
    "rq": "http://python-rq.org/",
    "Queues": "http://queues.io/",
        
            
    
})


class DishEs(object):
    def washer(self, dishes, output):
        for dish in dishes:
            print("Washing", dish, "dish")
            output.put(dish)

    def dryer(self, input):
        while True:
            dish = input.get()
            print("Drying", dish, "dish")
        input.tash_done()


class DishEs2(object):
    def do_this(self, what):
        self.whoami(what)

    def whoami(self, what):
        print("Thread %s says: %s"%(threading.current_thread(), what))


class DishEs3(object):
    def washer(self, dishes, dish_queue):
        for dish in dishes:
            print("Washing", dish)
            time.sleep(5)
            dish_queue.put(dish)

    def dryer(self, dish_queue):
        while True:
            dish = dish_queue.get()
            print("Drying", dish)
            time.sleep(10)
            print("task")
            dish_queue.task_done()
            print("done")


def gevent_test():
    import gevent
    from gevent import socket
    hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',\
             'www.antique-taxidermy.com']
    jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
    gevent.joinall(jobs, timeout=5)
    for job in jobs:
        print(job.value)



if __name__ == "__main__":
    gevent_test()
    """
    dish_queue = queue.Queue()
    d = DishEs3()
    for n in range(2):
        dryer_thread = threading.Thread(target=d.dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['salad', 'bread', 'entree', 'desert']
    d.washer(dishes, dish_queue)
    dish_queue.join()

    d = DishEs2()
    d.whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=d.do_this, args=("I'm, function %s"%n,))
        p.start()

    dish_queue = mp.JoinableQueue()
    d = DishEs()
    dryer_proc = mp.Process(target=d.dryer, args=(dish_queue,))
    dryer_proc.daemon = True
    dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert']
    d.washer(dishes, dish_queue)
    dish_queue.join()
    """





