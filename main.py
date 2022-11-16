import time
import art
def print_hi():
    count = 1000
    while count > 0:
        print(f"{count} - 7 = {count-7}")
        time.sleep(0.03)
        count -=7

    print("I'm a Ghoul!")
    print("  ")
    art.tprint("Dead inside.", font="#")


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
