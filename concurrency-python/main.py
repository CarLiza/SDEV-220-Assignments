import multiprocessing

def current_time(seconds):
    from datetime import datetime
    print('wait', seconds, 'seconds and the current time is:', datetime.utcnow())

if __name__ == '__main__':
    import random
    for i in range(3):
        s = random.randint(0,1)
        p = multiprocessing.Process(target=current_time, args = (s,))
        p.start()