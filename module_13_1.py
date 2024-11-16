import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for _ in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {_}-й шар')
    print(f'Силач {name} закончил соревнования.')

async def start_competition():
    ## Первый вариант
    task_1 = asyncio.create_task(start_strongman('Ярослав', 3))
    task_2 = asyncio.create_task(start_strongman('Александр', 5))
    task_3 = asyncio.create_task(start_strongman('Дмитрий', 4))
    await task_1
    await task_2
    await task_3
    ## Второй вариант
    # await asyncio.gather(start_strongman('Ярослав', 3),
    #                      start_strongman('Александр', 5),
    #                      start_strongman('Дмитрий', 4))

asyncio.run(start_competition())
