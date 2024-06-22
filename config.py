import os
from dotenv import load_dotenv
from nextcord import Embed

load_dotenv()

config = {
    "owners": [1037701642356805723,
    1129456838748942387],
    "embed-color": 0xff0053,
    "name": "Ash Blossom™",
    "guild_ids": [1093889894377590804, 1176882321304072292],
    "icon": "https://cdn.discordapp.com/attachments/1131256995450716293/1135128313812238377/Picsart_23-07-30_08-28-54-681.png",
    "tourna-icon": "https://cdn.discordapp.com/emojis/868507366658801734.png",
    "line": "https://cdn.discordapp.com/attachments/1180266906314346677/1181241158865797160/Picsart_23-12-04_14-27-09-677.png",
    
    "game-role":{
       "EDOPro": 1134960979743096832,
       "YGOOmega": 1134961080876142652,
       "DuelBook": 1134961494535180358,
       "Duelnexus": 1134961269099741245,
       "MasterDuel": 1134961743974645871,
       "DuelLinks": 1134961611803742289
    },
    
    "img": {
        "tournament": "https://cdn.discordapp.com/attachments/1180266906314346677/1248542764401168405/ash_blossom__joyous_spring__wallpaper__by_nhociory_dggi3rw-fullview.jpg",
        "bg": "https://cdn.discordapp.com/attachments/1180266906314346677/1248542764401168405/ash_blossom__joyous_spring__wallpaper__by_nhociory_dggi3rw-fullview.jpg",
        "done": "https://cdn.discordapp.com/emojis/1079031910010978315.png",
        "bg-welcome": "https://cdn.discordapp.com/attachments/1180266906314346677/1245767963492089856/ash_blossom__joyous_spring_extended_art_playmat_by_ptcl4_de5gcs1-fullview.jpg",
        "bg-duel": "https://cdn.discordapp.com/attachments/1180266906314346677/1247085016400527370/77b02254c2e559eb98419e8e31b74e41.jpg",
    },
    
    "emoji": {
        "manager": "<:manager:1242828171229921312>",
        "gems": "<:gem:1244963068539179122>",
        "points": "<:dp:1244966514168303684>",
        "star": "<a:XR_stars:1245011055252476057>",
        "duel": "<:duels:1244966260341473353>",
        "home": "<:home:1244656929301594196>",
        "join": "<:join:1242826815467421746>",
        "leave": "<:leave:1242826802259431455>",
        "list": "<:SY_Page:1196122570127314984>",
        "no": "<:Incorrect:1242934104660508806>",
        "yes": "<:Correct:1242933587695767713>",
        "loading": "<a:Loading_:1242932759710662699>",
        "round": "<:TagTournament:1243201034696786053>",
        "stats": "<:A_stats:1243530991448883240>",
         "log": "<:Logs:1243530370654408767>",
         "score": "<:score:1246896417734131782>",
         "vs": "<:vs:1244629382996299959>",
         "match-winner": "<:cup:1243709707378757732>",
         "cup": "<:cup:1243709707378757732>",
         "cup-winner": "<:CupWinner:1244565084169048074>",
         "win1": "<:Win1:1244564448518082600>",
         "win2": "<:Win2:1244564467904286764>",
         "win3": "<:Win3:1244564489395765340>",
         "time": "<a:time:1245381495909253231>",
         "gift": "<a:Giftsylv:1245459166659608587>",
         "verify": "<a:verify2:1245746751445532783>",
         "welcome": "<:Welcome:1245745683030478909>",
         "date": "<a:date:1247095480555540643>",
         "back": "<:page_left:1196122484567711755>",
         "ward": "<:page_right:1196122516360548605>",
         "link": "<:link:1247460369577021471>",
         "ticket": "<a:ticket:1247644590576767118>",
         "close": "<a:close:1247825175118872587>",
         "EDOPro": "<:EdoPro:1248606038744371200>",
	     "YGOOmega": "<:YGOOmega:1248606116297048064>",
	     "DuelBook": "<:DuelingBook:1248606611791155291>",
	     "Duelnexus": "<:DuelingNexus:1248606490273779764>",
	     "MasterDuel": "<:ZMasterDuel_icon:1248606224522412152>",
	     "DuelLinks": "<:duellinks:1248606399886524517>",
	     "latency": "<a:Latency:1248656235255824511>",
        
        "cmd": {
           "general": "<:commands:1244657920717885451>",
           "tournaments": "<:cup:1243709707378757732>",
           "admin": "<:admin:1245405666005483602>",
           "ygo": "<:ygo_card:1247298415642280068>"
        },
        
        "ranks": {
           "iron": "<:iron:1245078902838394960> Iron",
           "bronze": "<:bronze:1245076311144267826> Bronze",
           "silver": "<:silver:1245076407986683977> Silver",
           "gold": "<:gold:1245076604871246005> Gold",
           "platinum": "<:platinum:1245076707904589926> Platinum",
           "daimond": "<:diamond:1245076824443060285> Daimond",
           "master": "<:master:1245076931037368390> Master",
           "legend": "<:legend:1245077083739258891> Legend",
           "noob": "<:Noob:1245091241431928844> Noob..."
        },
        
        "number": {
            1: "<:number_1:1244623220338982952>",
            2: "<:number_2:1244623324177240126>",
            3: "<:number_3:1244623459816837161>",
            4: "<:number_4:1244623598195314730>",
            5: "<:number_5:1244623677056745482>",
            6: "<:number_6:1244623749735776341>",
            7: "<:number_7:1244623834485755984>",
            8: "<:number_8:1244623908389388439>",
            9: "<:number_9:1244623998982029463>",
            10: "<:number_10:1244624070751031368>",
            11: "<:number_11:1244624156050456646>",
            12: "<:number_12:1244624231161925703>",
            13: "<:number_13:1244624319343100004>",
            14: "<:number_14:1244624398443614229>",
            15: "<:number_15:1244624500021264425>",
            16: "<:number_16:1244624577754038332>",
            17: "<:number_17:1244624668951052359>",
            18: "<:number_18:1244624741382225991>",
            19: "<:number_19:1244624855631003651>",
            20: "<:number_20:1244624924971106384>",
            21: "<:number_21:1244624998065373268>",
            22: "<:number_22:1244625065031762015>",
            23: "<:number_23:1244625152222822491>",
            24: "<:number_24:1244625219734212608>",
            25: "<:number_25:1244625295785459742>",
            26: "<:number_26:1244625361707208798>",
            27: "<:number_27:1244625429864779837>",
            28: "<:number_28:1244625521531424849>",
            29: "<:number_29:1244625595946500166>",
            30: "<:number_30:1244625669699272775>"
        }
    },
}


loading = Embed(description=f"**{config['emoji']['loading']} Loading...**", color=config["embed-color"])