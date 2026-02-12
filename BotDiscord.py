from Ferramentas import discord, json, commands, random, Path, re, funcoes, load_dotenv 

load_dotenv()

TOKEN = os.getenv("TOKE_BOT")
CANAL_WESKER = os.getenv("CANAL_WESKER")

permissions = discord.Intents.all()
bot = commands.Bot("!", intents = permissions)

dadosBot_motiva = {"FraseMotiva":["Estou sem frases, mas saiba que você é incrível! 💪"]}

BASE_DIR = Path(__file__).resolve().parent

ARQUIVO_DADOS = BASE_DIR / "dados.json" 

#Carregamento de dados
dadosBot_motiva = {"frases": ["Estou sem frases, mas saiba que você é incrível! 💪"]}

try:
    with open(ARQUIVO_DADOS, encoding="utf8") as arquivo:
        dadosBot_motiva = json.load(arquivo)
#Tratamento de erros   
except FileNotFoundError:
    print(f"⚠️ ERRO CRÍTICO: O arquivo {ARQUIVO_DADOS} não foi encontrado. Usando frases de reserva.")
except json.JSONDecodeError:
    print("⚠️ ERRO CRÍTICO: O arquivo 'dados.json' está mal formatado. Usando frases de reserva.")

#Evento de inicialização
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizado {len(synced)} comandos de barra!")
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")
    print("Bot inicializado com sucesso!")

#Comando de motivação
@bot.command()
async def motiva(ctx:commands.Context):
    nome = ctx.author.mention
    list_frases = dadosBot_motiva["FraseMotiva"]
    dicionario_sorteado = random.choice(list_frases)
    frase_final = dicionario_sorteado["frases"]
    await ctx.send(f"{nome}{frase_final}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    #Verificação de palavras proibidas
    motivo = funcoes.verificar_palavroes(message)
    if motivo:
        conteudo_suspeito = message.content
        await message.delete()

    #Envio de mensagem de alerta
        await message.channel.send(f"⚠️ {message.author.mention}, a evidência foi destruída. "
            "Mantenha a discrição ou sofrerá as consequências.")
        canal_logs = bot.get_channel(CANAL_WESKER)

        #Envio de relatório
        if canal_logs:
            report = (f"🕵️ **Relatório de Campo - Alvo: {message.author}**\n"
                      f"**Local:** {message.channel.mention}\n"
                      f"**Evidência:** `{conteudo_suspeito}`")
            await canal_logs.send(report)

    await bot.process_commands(message)


#Comando de teste
@bot.command()
async def ola(ctx:commands.Context):
    nome = ctx.author.mention
    await ctx.send(f"Olá, tudo bem {nome} ?")



bot.run(TOKEN)