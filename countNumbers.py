
def main():
    x = 0
    num = 10
    for i in range(num):
        print(i + 1)
        print(i * i)
        # added in github
        print(i + 5)
        # added in github again
        print(num - i)
        x = i  + x
if __name__ == "__main__":
    main()

