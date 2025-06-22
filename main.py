# import packages
import asyncio
from airgradient import AirGradientClient

async def main() -> None:
    async with AirGradientClient('10.42.0.155') as client:
        measurements = await client.get_current_measures()
        print(measurements)

if __name__ == "__main__":
    asyncio.run(main())