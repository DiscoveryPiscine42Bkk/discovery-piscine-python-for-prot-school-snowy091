import sys

def main():
    if len(sys.argv) == 3:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])

            result = list(range(start, end))
            print(result)
        except ValueError:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()
input()