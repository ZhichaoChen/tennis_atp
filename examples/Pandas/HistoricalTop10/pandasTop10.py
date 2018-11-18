#!/usr/local/bin/python3
import pandas as pd
import glob
import datetime, sys

def parse(t):
    string_ = str(t)
    try:
        return datetime.date(int(string_[:4]), int(string_[4:6]), int(string_[6:]))
    except:
        print("Erro",string_)
        return datetime.date(1900,1,1)
    
def readAllFiles(dirname):
    allFiles = glob.glob(dirname + "/atp_rankings_" + "*.csv")
    ranks = pd.DataFrame()
    list_ = list()
    for filen in allFiles:
	    #print(filen)
        df = pd.read_csv(filen, 
                         index_col=None, 
                         header=None, 
                         parse_dates=[0], 
                         date_parser=None, #lambda t:parse(t),
                         low_memory=False)
        list_.append(df)
    ranks = pd.concat(list_)
    return ranks

def readPlayers(dirname):
    print ("Reading Players")
    return pd.read_csv(dirname+"/atp_players.csv",
                       index_col=None,
                       header=None,                       
                       parse_dates=[4])
                       
print(sys.argv[1])
ranks = readAllFiles(sys.argv[1])
ranks = ranks[(ranks[1]<10)]
#print ranks
players = readPlayers(sys.argv[1])
plRanks = ranks.merge(players,right_on=0,left_on=2)
print(ranks)
#plRanks["B"] = plRanks["0_x"] - plRanks[4]
#plRanks["B"] = plRanks["B"].astype(int) / (365*24*3600*1000000000.0)
#agg = plRanks[["0_x","B"]].groupby("0_x")

#agg.mean().to_csv("top100ages.csv")
