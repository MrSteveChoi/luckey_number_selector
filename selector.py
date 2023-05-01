import random

def lucky_num_generator(n=int(input('insert count'))):
    final_list = []
    for _ in range(n):
        lucky_list = []
        while len(lucky_list) < 6:
            lucky_num = random.randint(1, 45)
            lucky_list.append(lucky_num)
            lucky_list = list(set(lucky_list))

        final_list.append(lucky_list)
    return print(final_list, end='\n')

if __name__ == '__main__':
    lucky_num_generator()
