# import multiprocessing
#
#
# def spawn(num, num2):
#     print('Spawned {} {}'.format(num, num2))
#
# if __name__ == '__main__':
#     for i in range(55):
#         p = multiprocessing.Process(target=spawn, args=(i, i+1))
#         p.start()
#         # p.join()  # make processes in correct order

#  ________11_________

from multiprocessing import Pool


def job(num):
    return num * 2

if __name__ == '__main__':
    print('')
    p = Pool(processes=8)  # all processes are started
    data = p.map(job, range(22))
    data2 = p.map(job, [5])
    p.close()
    print(data)
    print(data2)
