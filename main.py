# import packages
import asyncio
from airgradient import AirGradientClient

async def main() -> None:
    async with AirGradientClient('192.168.1.234') as client:
        measurements = await client.get_current_measures()
        print(measurements)

if __name__ == "__main__":
    asyncio.run(main())