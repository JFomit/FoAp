#!/usr/bin/python
import glob, os

def main() -> None:
    with open("result.md", "w") as result:
        for path in glob.glob("[0-9]*.md"):
            with open(path) as file:
                print(path)
                result.writelines(file.readlines())
                result.write("\n\n")

if __name__ == "__main__":
    main()