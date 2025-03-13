import sys

def main():
    if len(sys.argv) > 2:
        reversed_params = sys.argv[1:][::-1]
        print(" ".join(reversed_params))
    else:
        print("none")

if __name__ == "__main__":
    main()
input()