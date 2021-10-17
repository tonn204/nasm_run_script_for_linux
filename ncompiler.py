import os
import sys

def main():
    if len(sys.argv) <= 1:
        sys.stderr.write("Please specife file with source code\n")
        sys.stderr.flush()
    else:
        my_file = sys.argv[1]
        os.system(f"nasm -f elf {my_file}.asm")
        os.system(f"ld -m elf_i386 {my_file}.o -o {my_file}")
        os.system(f"./{my_file}")


if __name__ == "__main__":
    main()
