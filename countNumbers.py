
def main():
    x = 0
    num = 10
    for i in range(num):
        print(i + 1)
        # added in github again
        print(num - i)
        x = i  + x
        print("this is a mistake code that will be reverted latter")
    print("END!")
if __name__ == "__main__":
    main()

