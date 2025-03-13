import sys

def main():
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        found_z = False

        for char in input_string:
            if char == 'z':
                print('z')
                found_z = True

        if not found_z:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()
input()

