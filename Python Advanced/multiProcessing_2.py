import time
import multiprocessing


square_numbers = []

def calc_square(numbers):
    global square_numbers
    for n in numbers:
        square_numbers.append(str(n*n))
        print('square ' + str(n*n))
    print("Outside Main, Inside Function : ", square_numbers)



if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    
    p1.start()

    p1.join()
    print("Inside Main : ", square_numbers)
    print("Done!")