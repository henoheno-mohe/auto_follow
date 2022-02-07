import sys
sys.path.append('../')
#import config
import tweepy
import time


CK="TCR0L0CCEB1hbWsS4vS3QIJ3j"
CS="v8xTuXPfBFL08Ewz5Vu7TUswOsWGbn9MxmvOB5jsIhdoaw2QgE"
AT="1475721163594952706-L32d3fIGVjowIRuD7FfAsQ9r86u0xr"
AS="MvrgGFE5Y4hFCQ8ZXi64yzOv3xFWJMKvCTcvfp5clNIHq"
BT="AAAAAAAAAAAAAAAAAAAAABgCXgEAAAAA1SOlCtGKnVAZhRSUcKgumYYEO2o%3DbL6s4upYmaPe756MuCq6toxlqgwsvwcR41ZK92rNQoLgMChtNa"

# API KEY
#CK = config.CK
#CS = config.CS
#AT = config.AT
#AS = config.AS
#BT = config.BT

#tweepyの設定
client = tweepy.Client(BT, CK, CS, AT, AS)


# USER_NAME = "1394284521059586051"

#２）あるキーワードで検索したユーザを指定の件数フォローする

# 検索キーワード
keyword = "フォロー プレゼント is:verified -is:retweet"

# フォロー数
follow_cnt = 0

# 現在のフォローリストを作成
follow_list = client.get_users_following(id="1475721163594952706",max_results=100)
follow_lists = []

for follow in follow_list[0]:
    follow_lists.append(follow.id)



s_count = 15
results = client.search_recent_tweets(query=keyword, max_results=s_count, user_fields = "name", expansions=["author_id","referenced_tweets.id"],)

for result in results.data: 
    print(result.author_id)
    # print(result.referenced_tweets)


for result in results.data: 
    client.retweet(result.id)
    if result.author_id not in follow_lists:
        client.follow_user(result.author_id)
        print(result.author_id)
        time.sleep(90)
        
