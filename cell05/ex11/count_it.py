import sys

def main():
    if len(sys.argv) > 1:
        print(f"parameters: {len(sys.argv) - 1}")
        for param in sys.argv[1:]:
            print(f"{param} {len(param)}")
    else:
        print("none")

if __name__ == "__main__":
    main()

input()