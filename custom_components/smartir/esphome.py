import os
import aiohttp

COMPONENT_ABS_DIR = os.path.dirname(os.path.abspath(__file__))


class Helper:
    @staticmethod
    async def downloader(url, file_path):
        """Download a file from url and save to file_path."""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()
                with open(file_path, "wb") as f:
                    f.write(content)
