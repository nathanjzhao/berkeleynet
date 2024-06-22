### From Image

import asyncio

from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig
import json

async def main():
    client = HumeStreamClient("o0pquuRGwVy9V5kRhngmcKHFl6T3ZaKL12ib7AVusT3JGgnw")
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file("/Users/timothygao/Documents/GitHub/berkeleynet/test_short.mov")
        print(result)
        json.dump(result, open("test_hume.json", "w"))

asyncio.run(main())


### From Speech

# import asyncio

# from hume import HumeStreamClient, StreamSocket
# from hume.models.config import ProsodyConfig

# async def main():
#     client = HumeStreamClient("o0pquuRGwVy9V5kRhngmcKHFl6T3ZaKL12ib7AVusT3JGgnw")
#     config = ProsodyConfig()
#     async with client.connect([config]) as socket:
#         result = await socket.send_file("/Users/timothygao/Documents/GitHub/berkeleynet/test_short.mov")
#         print(result)

# asyncio.run(main())