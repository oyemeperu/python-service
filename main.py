
import core


def looped_greeting(greet: str, times: int = 10):
    for i in range(times):
        print(f"{i}: {greet}")


def main():
    looped_greeting("Hello World")


if __name__ == "__main__":
    main()
    core.meta_execution()