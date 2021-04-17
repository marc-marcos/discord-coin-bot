# Bot coded by Marc Marcos Madruga for simp city server
# any other usage of this software can be reported to: marquitos#1583

from discord.ext import commands
import discord
import json
import random

bot = commands.Bot(command_prefix='$')

@bot.command()
async def cuenta(ctx):
    # autor: ctx.author
    
    f = open('data.json')
    data = json.load(f)
    f.close()

    if str(ctx.author) in data:
        await ctx.send(f'El balance actual de tu cuenta es de {data[str(ctx.author)]} pepe coins.')
    
    else:
        await ctx.send("No tienes ninguna cuenta actualmente, dejame crear una en un segundo, añado 50 pepe coins por defecto")

        data[str(ctx.author)] = 50
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

@bot.command()
async def transferir(ctx, user : str, amount : float):
    f = open('data.json')
    data = json.load(f)
    f.close()
    
    if data[str(ctx.author)] < amount:
        await ctx.send('Lo siento pero no puedo transferir más cantidad de la que tienes tu en la cuenta, ggs.')
    
    else:
        data[str(ctx.author)] = data[str(ctx.author)] - amount
        data[str(user)] = data[str(user)] + amount

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

@bot.command()
async def conseguir(ctx, guess):
    number = random.randint(1, 11)

    f = open('data.json')
    data = json.load(f)
    f.close()

    if data[str(ctx.author)] >= 1:
        if int(guess) == number:
            data[str(ctx.author)] = data[str(ctx.author)] + 10
            await ctx.send('Numero acertado, has conseguido 10 pepe coins.')

        else:
            await ctx.send('No has acertado el número, se te ha descontado 1 pepe coin, por joder.')
            await ctx.send(f'El número era el {number}')
            data[str(ctx.author)] = data[str(ctx.author)] - 1

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
        
    else:
        await ctx.send('No puedes conseguir dinero teniendo tan poco, es la gracia del capitalismo mi pana')

@bot.command()
async def apostar(ctx, cantidad : int, opcion : int):
    f = open('data.json')
    data = json.load(f)
    f.close()

    if not opcion:
        await ctx.send('Necesitas especificar a que numero deseas apostar')
        await ctx.send('Puedes apostar a 1 o a 2, entonces generaré un numero del 1 al 2 y ganarás o perderás dependiendo si has acertado.')
        await ctx.send('El índice de retorno es 1.5')   

    elif opcion >= 1 and opcion <= 2 and cantidad >= 10 and cantidad < data[str(ctx.author)]:
        bet = random.randint(1, 3)
        if bet == opcion:
            f = open('data.json')
            data = json.load(f)
            f.close()

            await ctx.send(f'Has acertado, te llevas {cantidad/2} por tu apuesta.')
            data[str(ctx.author)] = data[str(ctx.author)] + cantidad/2

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)
        
        else:
            f = open('data.json')
            data = json.load(f)
            f.close()

            await ctx.send(f'Has apostado al número incorrecto, más suerte la próxima.')

            data[str(ctx.author)] = data[str(ctx.author)] - cantidad

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file)

    elif cantidad > data[str(ctx.author)]:
        await ctx.send('No puedes apostar el dinero que no tienes, espabilao')

@bot.command()
async def total(ctx):
    f = open('data.json')
    data = json.load(f)
    f.close()

    total = 0

    for x in data:
        total += data[x]

    await ctx.send(f"La reserva nacional de Pepe Coins es de {total} Pepe Coins")

@bot.command()
async def clasificacion(ctx):
    f = open('data.json')
    data = json.load(f)
    f.close()

    sorted_dict = {}
    sorted_keys = sorted(data, key=data.get)  # [1, 3, 2]

    for w in sorted_keys:
        sorted_dict[w] = data[w]

    await ctx.send(f"1. {list(sorted_dict.keys())[-1]} \n2. {list(sorted_dict.keys())[-2]} \n3. {list(sorted_dict.keys())[-3]}")


bot.run('ODMxODg4NDQ0NDgwOTQ2MjQ2.YHbyfA.u_NMStXuKrKO39-GmIGanekayi8')