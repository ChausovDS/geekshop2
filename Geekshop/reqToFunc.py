def main(request):
    print(request)
    return None


def call_main(func):
    request = 1
    func(request)


if __name__ == "__main__":
    call_main(main)
