import uvicorn


def main() -> None:
    uvicorn.run('app:app')


if __name__ == '__main__':
    main()
