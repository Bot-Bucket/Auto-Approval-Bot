# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "23926873"))
    API_HASH = getenv("API_HASH", "5e258639c6553fe80000c4c9b87742f2")
    BOT_TOKEN = getenv("BOT_TOKEN", "7019754440:AAGJBqcb0uNoUup_x-cMfAbGyLsZJnCmq-0")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1001938917728")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6012920664").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hociy26798:t6GqD7bHLJjuizQl@cluster0.wxourzg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
