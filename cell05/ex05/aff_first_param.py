import sys

def main():
    num = len(sys.argv) - 1
    
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

if __name__ == "__main__":
    main()

