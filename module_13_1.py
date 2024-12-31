import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    for ball in range(5):
        delay = 5 - power
        if delay < 1:
            delay = 0.5
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял шар №{ball + 1} ')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())