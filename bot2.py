import tweepy
import keys
import time
import random

auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.key, keys.secret)

api = tweepy.API(auth)

j = random.randint(3, 100)
js = str(j)

# text options up to 62
texts =  ['insert your text options here' ]

#insert up to 51  images
filenames = ['insert images here']

CryptoShill = 'Buy dog realated shit coin to make $5000 right now #DogeShit' + ' ' + js
#to upload multiple images

#uploads two images with rand text

def multipleimg():
     media_ids = []
     k23= random.randint(0, 50)
     
     k24= random.randint(0, 50)
     
     res = api.media_upload(filenames[k24])
     res1 = api.media_upload(filenames[k23])
     media_ids.append(res.media_id)
     media_ids.append(res1.media_id)
     api.update_status(status=texts[random.randint(0,61)], media_ids=media_ids)
     


#Upload single IMG + text

def singleimg(): 
     media_ids = []
     k2= random.randint(0, 50)
     ks2= str(k2)
     res = api.media_upload(filenames[k2])
     media_ids.append(res.media_id)
     api.update_status(status=texts[random.randint(0,61)] + '          ' + ks2, media_ids=media_ids)
     



# upload just text

def txtonly():
     k2= random.randint(0, 50)
     ks2= str(k2)
     api.update_status(status=texts[random.randint(0,61)] + '            ' + ks2)





#upload cryptoshill
def cryptshill():
     k2= random.randint(0, 50)
     ks2= str(k2)
     api.update_status(status=CryptoShill)
     for status in api.user_timeline(count = 1):
      print("The tweet id is:", status._json['id'])
      api.update_status(status = 'OMG btw do your own research to make sure you dont lose money ' +ks2, in_reply_to_status_id = status._json['id'] , auto_populate_reply_metadata=True)


     


def cryptocostream():
     k2= random.randint(0, 50)
     ks2= str(k2)
     api.update_status(status='OMG streaming with @ILikeToScamPeopleWithCrypto at 7pm eastern so come check it out at https://www.twitch.tv/scam' +' '+ ks2)

def nftmoney():
     media_ids = []
     k2= random.randint(0, 50)
     ks2= str(k2)
     res = api.media_upload(filenames[52])
     media_ids.append(res.media_id)
     api.update_status(status='Buy my NFT for 120k' + '           ' + ks2, media_ids=media_ids)
 

def main1():
     from time import sleep
     
     num_list = list(range(1, 100))
     Rnd = random.choice(num_list)
     

     if Rnd < 1:
               nftmoney()
               print('posted nft money')
     elif Rnd > 1 and Rnd < 2:
               print('posted crypto money')
               cryptshill()
     elif Rnd >2 and Rnd <5:
               txtonly()
               print('posted text only')
     elif Rnd >5 and Rnd <8:
               cryptocostream()
               print('posted costream')
     elif Rnd >8 and Rnd <13:
               multipleimg()
     else:
               singleimg()

                   

          


def main():
     from time import sleep
     while True:
          time.sleep(3600)
          num_list1 = list(range(1, 100))
          Rnd1 = random.choice(num_list1)
          if Rnd1 < 12:
               print('posted')
               main1()
               
               

main()
