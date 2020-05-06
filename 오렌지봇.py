# 유저 아이디: message.author.name
# 채널 이름: message.channel
# 서버 아이디: message.author.display_name

import time
import discord
from discord.ext import commands
import datetime
import asyncio
import random
import sys
import urllib
from urllib.request import Request
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

token=("token")

client = discord.Client()

print ("----------------------------")
print ("")
print ("잠시만 기다려 주세요...")
print ("")
print ("----------------------------")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(client.user.id)
    print("ready")
    game = discord.Game("🍊 개발")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    # 봇 설명
    if message.content.startswith(".봇"):
        now = datetime.datetime.now()
        orangesendtime = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        embed = discord.Embed(title=str(client.user.name) + " 정보", description= """봇 이름: 오렌지 봇 🍊
        봇 ID: 680333364858978314
        봇 생일: 2020년 2월 20일
        오렌지 봇 홈페이지: https://jhcplace.wixsite.com/orangebot
        
        개발자: jhcpalce
        개발자 엔트리 마이페이지: https://playentry.org/jhcplece
        
        작성언어: python""", color=0x00ff00)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FVliqw%2FbtqCd1h9SOI%2FCzMfFsghAIdPfRkPzCKpak%2Fimg.png")
        embed.set_footer(text ="오렌지봇 | " + orangesendtime)
        await message.channel.send(embed=embed)
    
    # 안녕
    if message.content.startswith(".안녕"):
        await message.channel.send(embed=discord.Embed(description="안녕하세요! 오렌지봇이에요!", color=0x00ff00))

    if message.content.startswith(".메세지 삭제 안내"):
        await message.channel.send(embed=discord.Embed(description="서버 규칙에 따라 메세지가 삭제됨을 알려드립니다.(규칙 8)", color=0x00ff00))

    if message.content.startswith(".규칙"):
        await message.channel.send(embed=discord.Embed(description="서버 규칙이 수정되었습니다. 검토 바랍니다.", color=0x00ff00))

    # 안녕
    if message.content.startswith(".안내"):
        if message.author.id == 564250827959566359:
            choice = message.content.split(" ")
            choicenumber = choice[1]
            await message.channel.send(embed=discord.Embed(description="""(서버 안내)
            신규 회원 안내

            안녕하세요! {}님!
            Entry RPG 서버에 오신 것을 환영합니다!

            서버 규칙 채널에서 저희 서버의 규칙을 숙지해주세요.
            또한 작품 규칙 채널도 참고바랍니다.

            {}님, 어떤 역활을 하고 싶으신가요?
            디자인, 음향, 코딩, 스토리가 있습니다.""".format(choicenumber, choicenumber, choicenumber), color=0x00ff00))

    if message.content.startswith(".역활변경"):
        await message.channel.send(embed=discord.Embed(description="어떤 역활로 변경하고 싶으신가요?(역활변경 작업은 관리자가 온라인일 때만 처리됩니다.)", color=0x00ff00))

    if message.content.startswith(".처리완료"):
        if message.author.id == 564250827959566359:
            await message.channel.send(embed=discord.Embed(description="요청하신 '역활변경'이 정상적으로 처리되었습니다.", color=0x00ff00))

    # 도움말
    if message.content.startswith(".명령") or message.content.startswith(".도움"):
        print ("개발중")

    # 오픈소스
    if message.content.startswith(".오픈소스") or message.content.startswith(".오픈 소스"):
        embed = discord.Embed(title="오렌지 봇의 오픈소스가 궁굼한가요?", description= """여기, 오렌지봇의 오픈소스에요!
        https://jhcplace.wixsite.com/orangebot/opensource""", color=0x00ff00)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fr4qiU%2FbtqChGThDKZ%2FlJxXEs75PgNjRgdqKGZRsK%2Fimg.png")
        await message.channel.send(embed=embed)

    # 홈페이지
    if message.content.startswith(".홈페이지") or message.content.startswith(".홈피") or message.content.startswith(".사이트"):
        await message.channel.send(embed=discord.Embed(description="""오렌지봇 홈페이지:
        https://jhcplace.wixsite.com/orangebot""", color=0x00ff00))

    # 종료
    if message.content.startswith(".종료"):
        if message.author.id == 564250827959566359:
            await message.channel.send(embed=discord.Embed(description="오렌지봇을 종료합니다!", color=0xffa500))
            time.sleep(0.5)
            sys.exit()
        else:
            await message.channel.send(embed=discord.Embed(description="개발자나 관리자만 할 수 있는 기능이에요.", color=0xff0000))

    # 아니
    if message.content.startswith(".아니"):
        await message.channel.send(embed=discord.Embed(description="알겠어요!", color=0x00ff00))
        
    # 서버 정보
    if message.content.startswith(".서버"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name=message.guild.name + " 서버 정보", value="""

        ⚪ 서버 이름: {}
        🔖 서버 주인: {}
        
        🔑 서버 아이디: {}""".format(message.guild.name, message.guild.owner.name, message.guild.id), inline=True)
        await message.channel.send(embed=embed)

    # 싫어
    if message.content.startswith(".싫어"):
        await message.channel.send(embed=discord.Embed(description="알겠어요!", color=0x00ff00))

    # 뭐해
    if message.content.startswith(".뭐해"):
        await message.channel.send(embed=discord.Embed(description="저는 코딩 하고 있어요! 같이 해요!", color=0x00ff00))

    # 뭐할까
    if message.content.startswith(".뭐할") or message.content.startswith(".심심"):
        await message.channel.send(embed=discord.Embed(description="""음... 오렌지봇 홈페이지에 들어가 보세요!
        오렌지 봇 홈페이지: https://jhcplace.wixsite.com/orangebot""", color=0x00ff00))

    # 사랑해
    if message.content.startswith(".사랑해"):
        await message.channel.send(embed=discord.Embed(description="웩!   😒", color=0xffa500))

    # 사귀자
    if message.content.startswith(".사귀자") or message.content.startswith(".사귈래"):
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="진심인가요?", value="사양할게요!", inline=True)
        embed.set_image(url="https://media2.giphy.com/media/13dRJkj5wgKq9q/giphy.gif?cid=790b7611ee1093e19c0f04441bde10d69ed7a8c4a198aa47&rid=giphy.gif")
        await message.channel.send(embed=embed)

    # 뀨
    if message.content.startswith(".뀨"):
        await message.channel.send(embed=discord.Embed(description="제발 그런거 하지 마세요, 정말 구역질 나요!", color=0xffa500))

    # 미안해
    if message.content.startswith(".미안해"):
        await message.channel.send(embed=discord.Embed(description="미안해 하지 마세요! 전 괜찮아요, 로봇은 감정이 없거든요!", color=0x00ff00))

    # 잘가
    if message.content.startswith(".바이"):
        await message.channel.send(embed=discord.Embed(description="잘가요~ 다음에 다시 만나요! " + message.author.name + "!", color=0x00ff00))

    # 날씨 개그
    if message.content.startswith(".날씨 개그") or message.content.startswith(".날씨개그") or message.content.startswith(".날시 개그") or message.content.startswith(".날시개그"):
        embed = discord.Embed(title="현재 지역 날씨입니다.", description= """
        현재 온도: 100˚
        현재 상태: 내가 어떻게 알아
        현재 미세먼지 상태: 몰라
        비가 올 확률: 0% ~ 100%
        내일 날씨: 홍수가 일어납니다.
        
        오렌지 캐스터가 서울 한복판에 나와 있는데요,
        오렌지 캐스터, 그쪽 날씨는 어떤가요?""", color=0x00ff00)
        embed.set_image(url="https://i.ytimg.com/vi/7ly6SxwZNTY/hqdefault.jpg")
        await message.channel.send(embed=embed)

    # 랜덤 gif
    if message.content.startswith(".움짤") or message.content.startswith(".움잘"):
        randomgif = random.randrange(1,11)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="오렌지봇이 고른 움짤", value="여기, 움짤이에요! 풉!", inline=True)
        if randomgif == 1:
            embed.set_image(url="https://media0.giphy.com/media/rdma0nDFZMR32/giphy.gif?cid=790b7611f8ef36b5ce2d244fef0187f15cef47de367c448f&rid=giphy.gif")
        if randomgif == 2:
            embed.set_image(url="https://media3.giphy.com/media/3rgXBQIDHkFNniTNRu/giphy.gif?cid=790b7611f8ef36b5ce2d244fef0187f15cef47de367c448f&rid=giphy.gif")
        if randomgif == 3:
            embed.set_image(url="https://media3.giphy.com/media/3ohzAZ7dOGblBaOlHi/giphy.gif?cid=790b761100722c04c2b8b9e03f494eaeb5a262e1f15aac59&rid=giphy.gif")
        if randomgif == 4:
            embed.set_image(url="https://media2.giphy.com/media/lo5jV0hLNr7Gw/giphy.gif?cid=790b76112f234b59198e9190b54f7820414763e94b249a17&rid=giphy.gif")
        if randomgif == 5:
            embed.set_image(url="https://media1.giphy.com/media/SggILpMXO7Xt6/giphy.gif?cid=790b7611019546b130a87b8f67eedba8631bce5b63119017&rid=giphy.gif")
        if randomgif == 6:
            embed.set_image(url="https://media0.giphy.com/media/DbD6EnlEQmjTi/giphy.gif?cid=790b761151253b4ac5cf24f5ef499a9fbb28fe85aece2dd3&rid=giphy.gif")
        if randomgif == 7:
            embed.set_image(url="https://media2.giphy.com/media/KHJw9NRFDMom487qyo/giphy.gif?cid=790b7611743661149322a45c617ebf143443eac51a318ea3&rid=giphy.gif")
        if randomgif == 8:
            embed.set_image(url="https://media0.giphy.com/media/gj1kRead5SOE8/giphy.gif?cid=790b76115a9ed3c85ffdd7e6aa706ed8cd59aa07250934cb&rid=giphy.gif")
        if randomgif == 9:
            embed.set_image(url="https://media1.giphy.com/media/fjLUSoRRJfRxS/giphy.gif?cid=790b7611b9878407490ae90a36d01ea46baa54eabf8c9de8&rid=giphy.gif")
        if randomgif == 10:
            embed.set_image(url="https://media0.giphy.com/media/3kD7idHeAaZUc/giphy.gif?cid=790b761132e784708cc40a67c423ee5fc42cbc28cc3d31f5&rid=giphy.gif")
        await message.channel.send(embed=embed)

    # 경고
    if message.content.startswith(".경고"):
        if message.author.id == 564250827959566359:
            choice = message.content.split(" ")
            choicenumber = choice[1]
            await message.channel.send(embed=discord.Embed(description="""경고 메시지!
            {}님! {}님은 경고를 받으셨어요! +경고 1회!
            참고: 경고가 3번 쌓이면 퇴출 되실 수 있습니다.
            (경고사유: 최근 일주일 동안 활동하신 내용이 없습니다.)""".format(choicenumber, choicenumber), color=0xff0000))
            embed = discord.Embed(color=0xff0000)
            embed.set_image(url="https://cdn.pixabay.com/photo/2012/04/12/22/25/warning-sign-30915_960_720.png")
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=discord.Embed(description="관리자만 할 수 있는 기능이에요.", color=0xff0000))

    # 골라
    if message.content.startswith(".골라"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice) - 1)
        choiceresult = choice[choicenumber]
        await message.channel.send(embed=discord.Embed(description="🎰 과연 오렌지봇의 선택은? 두구두구~ 🎰", color=0x00ff00))
        await message.channel.send("||" + "            " + choiceresult + "!" + "            " + "||")

    if message.content.startswith('.주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: '+ ':one:', color=0x00ff00))
        if randomNum == 2:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':two:', color=0x00ff00))
        if randomNum ==3:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':three:', color=0x00ff00))
        if randomNum ==4:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':four:', color=0x00ff00))
        if randomNum ==5:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':five:', color=0x00ff00))
        if randomNum ==6:
            await message.channel.send(message.channel, embed=discord.Embed(description=':game_die: ' + ':six: ', color=0x00ff00))


    # 사용자 정보(이름, 서버닉네임, 가입일, 아이디를 보여줌)
    if message.content.startswith(".정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send("여기, 당신의 정보에요!", embed=embed)

    # offline/online 코드
    if message.content.startswith(".나가"):
        await message.channel.send(embed=discord.Embed(description="알겠어요... 당신이 원한다면요... 훌쩍!", color=0xffa500))
        time.sleep(2)
        await client.change_presence(status=discord.Status.offline)
        await message.channel.send(embed=discord.Embed(description="현재 오렌지 봇이 오프라인 상태입니다.", color=0xffa500))
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="현재 오렌지 봇이 오프라인 상태에요!", value="'.들어와'를 입력해 오렌지 봇을 온라인 상태로 만드세요!", inline=True)
    if message.content.startswith(".들어와"):
        await client.change_presence(status=discord.Status.online)
        time.sleep(2)
        await message.channel.send(embed=discord.Embed(description="반가워요! 절 부르셨나요?", color=0x6495ed))
    if message.content.startswith(".꺼져"):
        embed = discord.Embed(color=0xffa500)
        embed.add_field(name="헉! 어떻게 그렇게 심한 말을...", value="알았어요, 흥! 😡", inline=False)
        await message.channel.send(embed=embed)
        time.sleep(2)
        await client.change_presence(status=discord.Status.do_not_disturb)

client.run(token)

ⓒ 2020. jhcplace All Rights Reserved.
