import requests

class Fantasy:

    def __init__(self):
        self.url =  'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=mMatchup&view=mMatchupScore'
        self.espn_s2 = 'AECNDeJmu7pDlzUMCuuwNOz4Dy45P4h4hHOrc9FYds9z8GLJBK3VkXZFrJTG4I1XR%2BTcJwVGPFQETDuwaoc7PlsMnp%2FpO51lAAtVKTj1xruqsWnhKWcdYxqcwrIv%2BVzY1hvftMRj6uLE8Mqn1eGrJ7jN3QxsVk6HjBBqHH6QKuaWXtur7BGym0jGdeTgloKV1YE2tbw66jetHGx%2BooPCrJ1I8n2bNtLxQN8Jldv2n5ZXHa0o9qtqcIKUNWyKWIbPjju4STLTXo1PfoYjLEymjAXmRuHIS9EETwJnI6IlxalYjA%3D%3D'
        self.swid = '{02E5A334-D73B-482C-B387-4C383B1130E6}'
        self.url2 = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=mTeam'
    
    def find_team_id(self, abbrev):
        r2 = requests.get(self.url2)
        d2 = r2.json()
        for team in d2['teams']:
            if team['abbrev'] == abbrev:
                return team['id']
        return -1
            
    def print_team(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()

        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'
        
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '002020':
                            index = p
                            break 
                    try:
                        print(player_name + " Goals: " + str(player_is['stats'][index]['stats']['13']) + " Assists: " + str(player_is['stats'][index]['stats']['14']))
                    except:
                        try:
                            print(player_name + " GAA: " + str(player_is['stats'][index]['stats']['10']) + " SV %: " + str(player_is['stats'][index]['stats']['11']))
                        except:
                            try:
                                print(player_name + " NO STATS THIS SEASON! Last season: Goals: " + str(player_is['stats'][index]['stats']['13']) + " Assists: " + str(player_is['stats'][index]['stats']['14']))
                            except:
                                print(player_name)

    def sort_team_goals(self, abbrev):

        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()

        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        print("SORTING TEAM " + abbrev + " BY MOST GOALS")
        lst = []
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '022020':
                            index = p
                            break 
                    try:
                        lst.append((player_name, player_is['stats'][index]['stats']['13']))
                    except:
                        pass
        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        for tup in reverse_sorted_list:
           print(tup[0] + (30-len(tup[0]))*"." + str(tup[1]))

    def sort_team_assists(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()

        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        print("SORTING TEAM " + abbrev + " BY MOST ASSISTS")

        lst = []
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '022020':
                            index = p
                            break 
                    try:
                        lst.append((player_name, player_is['stats'][index]['stats']['14']))
                    except:
                        pass
        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        for tup in reverse_sorted_list:
           print(tup[0] + (30-len(tup[0]))*"." + str(tup[1]))

    def sort_team_pm(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()

        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        print("SORTING TEAM " + abbrev + " BY PLUS/MINUS")

        lst = []
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '022020':
                            index = p
                            break  
                    try:
                        lst.append((player_name, player_is['stats'][index]['stats']['15']))
                    except:
                        pass
        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        for tup in reverse_sorted_list:
           print(tup[0] + (30-len(tup[0]))*"." + str(tup[1]))

    def print_sort_team_weighted(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        score = 0
        index = 0
        fscore = 0
        dscore = 0
        gscore = 0
        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        print("SORTING TEAM " + abbrev + " BY WEIGHTING STATS (BEING MODIFIED)")

        lst = []
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '002020':
                            index = p
                            break                   
                    try:
                        if player_is['eligibleSlots'] == [4, 6, 7, 8]:
                            score = self.calculate_weighted_skater(player_is['stats'][index]['stats'], 'd')
                            dscore += score
                        else:
                            score = self.calculate_weighted_skater(player_is['stats'][index]['stats'], 'f')
                            fscore += score
                        lst.append((player_name, score))
                    except:
                        try:
                            score = self.calculate_weighted_goalie(player_is['stats'][index]['stats'])
                            if player_is['eligibleSlots'] == [5,7,8]:
                                gscore += score
                            lst.append((player_name, score))
                        except:
                            print("ERROR: Team " + abbrev + ' ' + player_name)
                    score = 0


        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        for tup in reverse_sorted_list:
           print(tup[0] + (30-len(tup[0]))*'.' + str(tup[1]))

        msg1 = "Points scored by forwards "
        msg2 = "Points scored by defense "
        msg3 = "Points scored by goalies "
        print(msg1 + (30 -len(msg1))*' ' + str(fscore))
        print(msg2 + (30 -len(msg2))*' '+ str(dscore))
        print(msg3 + (30 -len(msg3))*' ' + str(gscore))
        return reverse_sorted_list


    def sort_teams_weighted(self, abbrev1, abbrev2):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        score1 = 0
        score2 = 0
        fscore1 = 0
        dscore1 = 0
        gscore1 = 0
        fscore2 = 0
        dscore2 = 0
        gscore2 = 0
        abbrev_id1 = self.find_team_id(abbrev1)
        abbrev_id2 = self.find_team_id(abbrev2)

        if abbrev_id1 < 0:
            print('Abbreviation ' + abbrev1 + ' not found! Try again (abbreviation is case sensitive)')
            return 

        if abbrev_id2 < 0:
            print('Abbreviation ' + abbrev2 + ' not found! Try again (abbreviation is case sensitive)')
            return

        print("SORTING TEAMS " + abbrev1 + " AND " + abbrev2 + " BY WEIGHTING STATS (BEING MODIFIED)")

        lst1 = []
        lst2 = []
        for team in d['teams']:
            if team['id'] == abbrev_id1:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index1 = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '002020':
                            index1 = p
                            break                   
                    try:
                        
                        if player_is['eligibleSlots'] == [4, 6, 7, 8]:
                            score1 = self.calculate_weighted_skater(player_is['stats'][index1]['stats'], 'd')
                            dscore1 += score1
                        else:
                            score1 = self.calculate_weighted_skater(player_is['stats'][index1]['stats'], 'f')
                            fscore1 += score1
                        lst1.append((player_name, score1))
                    except:
                        try:
                            score1 = self.calculate_weighted_goalie(player_is['stats'][index1]['stats'])
                            if player_is['eligibleSlots'] == [5,7,8]:

                                gscore1 += score1
                            lst1.append((player_name, score1))
                        except:
                            print("ERROR: Team " + abbrev1 + ' ' + player_name)
                            return
                    score1 = 0

        for team in d['teams']:
            if team['id'] == abbrev_id2:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']

                    index2 = 0

                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '002020':
                            index2 = p
                            break
                    
                    try:
            
                        if player_is['eligibleSlots'] == [4, 6, 7, 8]:
                            score2 = self.calculate_weighted_skater(player_is['stats'][index2]['stats'], 'd')
                            dscore2 += score2
                        else:
                            score2 = self.calculate_weighted_skater(player_is['stats'][index2]['stats'], 'f')
                            fscore2 += score2
                        lst2.append((player_name, score2))
                    except:
                        try:
                            score2 = self.calculate_weighted_goalie(player_is['stats'][index2]['stats'])
                            if player_is['eligibleSlots'] == [5,7,8]:
                                gscore2 += score2 
                            lst2.append((player_name, score2))
                        except:
                            print("ERROR: Team " + abbrev2 + ' ' + player_name)
                    score2 = 0

        sorted_lst1 = sorted(lst1, key=lambda tup: tup[1])
        reversed_sorted_list1 = sorted_lst1[::-1]

        sorted_lst2 = sorted(lst2, key=lambda tup: tup[1])
        reversed_sorted_list2 = sorted_lst2[::-1]

        print("Team " + abbrev1 + (40-(len(abbrev1)) - len(abbrev2))*" " + "Team " + abbrev2)
        
        for tup in range(len(reversed_sorted_list1)):
            print(reversed_sorted_list1[tup][0] + " " + str(reversed_sorted_list1[tup][1]) + (40-(len(reversed_sorted_list1[tup][0]) +len(str(reversed_sorted_list1[tup][1]))))*" " + reversed_sorted_list2[tup][0] + " " + str(reversed_sorted_list2[tup][1]))

        msg1 = "Points scored by forwards "
        msg2 = "Points scored by defense "
        msg3 = "Points scored by goalies "
        print(msg1 + str(fscore1) + (40 - (len(msg1) + len(str(fscore1))) + 1)*' ' + msg1 + str(fscore2))
        print(msg2 + str(dscore1) + (40 - (len(msg2) + len(str(dscore1))) + 1)*' ' + msg2 + str(dscore2))
        print(msg3 + str(gscore1) + (40 - (len(msg3) + len(str(gscore1))) + 1)*' ' + msg3 + str(gscore2))


    def calculate_weighted_skater(self, player, pos):
        score = 0

        if pos == 'f':
            score += player['13'] #Goals
            score += player['14'] #Assists
            score += 0.5*player['15'] #P/M
            score += 0.5*player['29'] #SOG
            score += player['31'] #Hits
            score += 1.5*player['38'] #PPP
        else:
            score += 1.5*player['13'] #Goals
            score += 1.5*player['14'] #Assists
            score += 0.5*player['15'] #P/M
            score += 1.25*player['29'] #SOG
            score += 0.75*player['31'] #Hits
            score += 2*player['38'] #PPP

        time = player['27'] #TOI (in seconds)
        
        if time/60 >= 25:
            score += 4
        elif time/60 >= 20:
            score += 3
        elif time/60 >= 18:
            score += 2
        else:
            score -= 4
        
        return score

    def calculate_weighted_goalie(self, player):
        score = 0
        
        wins = player['1'] #Wins
        gp = player['8']/60 #Games played
        gaa = player['10'] #GAA
        svp = player['11'] #Save%

        if gp == 0:
            score += 0
        elif wins/gp == 1:
            score += 5
        elif wins/gp >= 0.8:
            score += 4.5
        elif wins/gp >= 0.6:
            score += 4
        elif wins/gp >= 0.5:
            score += 3
        elif wins/gp >= 0.4:
            score += 1
        else:
            score -= 3
        
        if gaa < 2:
            score += 4
        elif gaa <= 2.10:
            score += 3.5
        elif gaa <= 2.15:
            score += 3
        elif gaa < 2.20:
            score += 2.5
        elif gaa < 2.30:
            score += 2
        elif gaa < 2.50:
            score += 1.5
        else:
            score -= 2
          
        if svp >= 0.920:
            score += 4
        elif svp >= 0.915:
            score += 2
        elif svp >= 0.910:
            score += 1
        elif svp == 0:
            score += 0
        else:
            score -= 2

        return score

    def sort_team_weighted(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        score = 0
        index = 0
        fscore = 0
        dscore = 0
        gscore = 0
        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        #print("SORTING TEAM " + abbrev + " BY WEIGHTING STATS (BEING MODIFIED)")

        lst = []
        pos = ''
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '022020':
                            index = p
                            break                   
                    try:

                        if player_is['eligibleSlots'] == [4, 6, 7, 8]:
                            score = self.calculate_weighted_skater(player_is['stats'][index]['stats'], 'd')
                            pos = 'd'
                            dscore += score
                        else:
                            score = self.calculate_weighted_skater(player_is['stats'][index]['stats'], 'f')
                            pos = 'f'
                            fscore += score
                        lst.append((player_name, score, pos))
                    except:
                        try:
                            score = self.calculate_weighted_goalie(player_is['stats'][index]['stats'])
                            if player_is['eligibleSlots'] == [5,7,8]:
                                gscore += score
                            pos = 'g'
                            lst.append((player_name, score, pos))
                        except:
                            lst.append((player_name, score))
                    score = 0

        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        return reverse_sorted_list

    def recommend_fa(self, abbrev, position, amount):
        fa_url = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=kona_player_info'
        r = requests.get(fa_url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        options_n = 0
        options = []
        rem = []
        p_name = ''
        pos = ''
        score = 0
        fa_max= 500
        exceeded = -1
        valids = ['f', 'd', 'g']
        if position not in valids:
            print("Enter a valid position ('f', 'd', or 'g')")
            return

        abbrev_list = self.sort_team_weighted(abbrev)

        for player in d['players']:
            p_name = player['player']['fullName']
            if player['player']['eligibleSlots'] == [4, 6, 7, 8]:
                pos = 'd'
            elif 5 in player['player']['eligibleSlots']:
                pos = 'g'
            else:
                pos = 'f'
            lst = player['player']['stats']
            for index in lst:
                if index['id'] == '002020':
                    stats = index['stats']
                    if len(stats) < 5:
                        break
                    if pos == 'd':
                        try:
                            if stats['stats']['27'] < 1000:
                                break
                            score = self.calculate_weighted_skater(stats, 'd')
                        except:
                            pass
                    elif pos == 'f':
                        try:
                            if stats['27'] < 1000: #To make sure ice time is more than about 17mins
                                break
                            score = self.calculate_weighted_skater(stats, 'f')
                        except:
                            pass
                    else:
                        try:
                            score = self.calculate_weighted_goalie(stats)
                        except:
                            pass
                    
                    for p in abbrev_list[::-1]:
                        try:
                            if len(options) > fa_max:
                                print("Exceded " + str(fa_max) + " free agents")
                                exceeded = 1
                                break


                            elif p[2] == position and pos == position and len(options) <= fa_max:
                                options_n += 1
                                print("(" + str(options_n) + ") hmmm... " + str(len(options)))
                            
                                if score > p[1] and (player['status'] == "FREEAGENT" or player['status'] == "WAIVERS")  and p_name not in rem:
                                    rem += [p_name]
                                    options += [(p_name, score, p[0], p[1])]
                                    print("found one ... " + str(len(options)))
                        except:
                            pass
                    score = 0
            if exceeded > 0:
                break

        sorted_lst = sorted(options, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        if len(reverse_sorted_list) == 0:
            print("No recommendations!")
            return

        count = 0
        for tup in reverse_sorted_list:
            if count >= amount:
                 break
            print("Drop " + tup[2] + " (" + str(tup[3]) +  ") for " + tup[0] + " (" + str(tup[1]) + ")")
            count += 1
        return

    def find_fa(self, name):
        fa_url = 'http://fantasy.espn.com/apis/v3/games/fhl/seasons/2020/segments/0/leagues/216782?view=kona_player_info'
        r = requests.get(fa_url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        options_n = 0
        options = []
        rem = []
        p_name = ''
        pos = ''
        score = 0
        fa_max= 500
        exceeded = -1
        valids = ['f', 'd', 'g']

        for player in d['players']:
            p_name = player['player']['fullName']

            if p_name == name:
                if player['player']['eligibleSlots'] == [4, 6, 7, 8]:
                    pos = 'd'
                elif 5 in player['player']['eligibleSlots']:
                    pos = 'g'
                else:
                    pos = 'f'
                lst = player['player']['stats']
                for index in lst:
                    if index['id'] == '022020':
                        stats = index['stats']
                        if len(stats) < 5:
                            break
                        if pos == 'd':
                            try:
                                if stats['stats']['27'] < 1000:
                                    break
                                score = self.calculate_weighted_skater(stats, 'd')
                                print("Score for " + name + " is: " + str(score))
                                return
                            except:
                                pass
                        elif pos == 'f':
                            try:
                                if stats['27'] < 1000: #To make sure ice time is more than about 17mins
                                    break
                                score = self.calculate_weighted_skater(stats, 'f')
                                print("Score for " + name + " is: " + str(score))
                                return
                            except:
                                pass
                        else:
                            try:
                                score = self.calculate_weighted_goalie(stats)
                                print("Score for " + name + " is: " + str(score))
                                return
                            except:
                                pass
                        
        print("Player Not Found...")
        return

    def sort_team_pp60(self, abbrev):
        r = requests.get(self.url,
		 cookies={"swid": self.swid,
			  "espn_s2": self.espn_s2})
        d = r.json()
        abbrev_id = self.find_team_id(abbrev)

        if abbrev_id < 0:
            return 'Abbreviation not found! Try again'

        print("SORTING TEAM " + abbrev + " BY P/60")

        goals = 0
        assists = 0
        toi = 0

        lst = []
        for team in d['teams']:
            if team['id'] == abbrev_id:
                for player in team['roster']['entries']:
                    player_name = player['playerPoolEntry']['player']['fullName']
                    player_is = player['playerPoolEntry']['player']
                    index = 0
                    for p in range(len(player_is['stats'])):
                        if player_is['stats'][p]['id'] == '022020':
                            index = p
                            break  
                    try:
                        stats = player_is['stats'][index]['stats']
                        goals = stats['13']
                        assists = stats['14']
                        toi = stats['26']/60
                        pp60 = ((goals + assists)/toi)
                        lst.append((player_name, pp60*60))
                    except:
                        pass
        sorted_lst = sorted(lst, key=lambda tup: tup[1])
        reverse_sorted_list = sorted_lst[::-1]

        for tup in reverse_sorted_list:
           print(tup[0] + (30-len(tup[0]))*"." + str(tup[1]))
        
        
