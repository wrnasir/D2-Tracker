from flask import Flask, render_template, request
from api import stats, api

app = Flask(__name__)
a = api()

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/stats', methods = ['GET', 'POST'])
def stats_page():
   print(request.args.get('user'))
   return render_template("stats.html")

@app.route('/profile')
def profile_page():
   return render_template("profile.html")

@app.route('/stats/', methods = ['GET', 'POST'])
def user_stats_page():
   accinfo = a.SearchByBungieName(request.args.get('name'), request.args.get('code'))
   
   username = accinfo['Response'][0]['bungieGlobalDisplayName'] + '#' + str(accinfo['Response'][0]['bungieGlobalDisplayNameCode'])
   membership_id = accinfo['Response'][0]['membershipId']
   membership_type = accinfo['Response'][0]['membershipType']

   statinfo = a.GetHistoricalStatsForAccount(membershipType=membership_type, destinyMembershipId=membership_id)
   
   q = stats(statinfo)

   return render_template('temp.html', username = username,
                                       kills = q.getKills(),
                                       deaths = q.getDeaths(),
                                       assists = q.getAssists(),
                                       revives = q.getRevives(),
                                       KD = q.getKD(),
                                       KDA = q.getKDA(),
                                       efficiency = q.getEfficiency(),
                                       opps_defeated = q.getOpponentsDefeated(),
                                       precisionkills = q.getPrecisionKills(),
                                       highestkills = q.getMostKills(),
                                       highestkillstreak = q.getHighestKillstreak(),
                                       timeplayed = q.getTimePlayed())

if __name__ == "__main__":
   app.run()