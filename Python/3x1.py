def main():
    num = int(input("Seed: "))

    while num != 1:
        print(num)
        if num % 2 == 0:
            num = num //2
        else:
            num = num * 3 + 1
    print(num)

if __name__ == "__main__":
    main()
