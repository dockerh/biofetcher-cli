import argparse
import asyncio
from biofetcher.downloader import sync_download, async_download

def main():
    parser = argparse.ArgumentParser(description="Biofetcher CLI")
    parser.add_argument('--url', required=True)
    parser.add_argument('--output', default='output.txt')
    parser.add_argument('--mode', choices=['sync', 'async'], default='sync')
    args = parser.parse_args()

    if args.mode == 'sync':
        sync_download(args.url, args.output)
    else:
        asyncio.run(async_download(args.url, args.output))

if __name__ == "__main__":
    main()
