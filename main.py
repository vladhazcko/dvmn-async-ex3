import asyncio
from asyncio import subprocess


def main():
    asyncio.run(archivate())


async def archivate():
    command = 'zip -r - test'

    process = await subprocess.create_subprocess_shell(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    with open('test.zip', 'wb') as zip_file:
        while True:

            archive_chunk = await process.stdout.read(100)
            zip_file.write(archive_chunk)
            if not archive_chunk:
                break


if __name__ == '__main__':
    main()
