import sys

def main():
    if len(sys.argv) > 1:
        for param in sys.argv[1:]:
            if not param.endswith("ism"):
                print(param + "ism")
    else:
        print("none")

if __name__ == "__main__":
    main()
input()