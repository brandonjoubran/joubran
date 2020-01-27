import requests

url = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=mMatchup&view=mMatchupScore'
espn_s2 = 'AECNDeJmu7pDlzUMCuuwNOz4Dy45P4h4hHOrc9FYds9z8GLJBK3VkXZFrJTG4I1XR%2BTcJwVGPFQETDuwaoc7PlsMnp%2FpO51lAAtVKTj1xruqsWnhKWcdYxqcwrIv%2BVzY1hvftMRj6uLE8Mqn1eGrJ7jN3QxsVk6HjBBqHH6QKuaWXtur7BGym0jGdeTgloKV1YE2tbw66jetHGx%2BooPCrJ1I8n2bNtLxQN8Jldv2n5ZXHa0o9qtqcIKUNWyKWIbPjju4STLTXo1PfoYjLEymjAXmRuHIS9EETwJnI6IlxalYjA%3D%3D'
swid = '{02E5A334-D73B-482C-B387-4C383B1130E6}'

url2 = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=mTeam'

r = requests.get(url,
		 cookies={"swid": swid,
			  "espn_s2": espn_s2})

r2 = requests.get(url2)

d = r.json()

d2 = r2.json()

print(len(d2['teams']))
    

for team in d['teams']:
    team_id = team['id']
    print(team_id)
    for t in d2['teams']:
        print(t['abbrev'])
        if t['id'] == team_id:
            print("" + str(t['abbrev']) + " (id: " +  str(team['id']) + ")")
            for player in team['roster']['entries']:
                player_name = player['playerPoolEntry']['player']['fullName']
                player_is = player['playerPoolEntry']['player']
                try:
                    print(player_name + " Goals: " + str(player_is['stats'][0]['stats']['13']) + " Assists: " + str(player_is['stats'][0]['stats']['14']))
                except:
                    try:
                        print(player_name + " GAA: " + str(player_is['stats'][0]['stats']['10']) + " SV %: " + str(player_is['stats'][0]['stats']['11']))
                    except:
                        try:
                            print(player_name + " NO STATS THIS SEASON! Last season: Goals: " + str(player_is['stats'][1]['stats']['13']) + " Assists: " + str(player_is['stats'][1]['stats']['14']))
                        except:
                            print(player_name)
                
                

'''print((d['teams'])[0]['roster']['entries'])'''

a = d['teams'][1]
b = a['id']
c = a['roster']['entries'][0]['playerPoolEntry']['player']['fullName']

        
'''for player in t:
    print(t['playerPoolEntry']['player']['fullName'])'''

