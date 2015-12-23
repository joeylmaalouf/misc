import re
import requests


class Match(object):
  def __init__(self, match_id):
    super(Match, self).__init__()
    self.match_id = match_id
    response = requests.get("http://www.datdota.com/match.php?q={0}".format(match_id))
    self.patch = re.findall("Patch:</b>(.+?)<br>", response.content)[0].strip()
    matches = re.findall("\"team.php\?q=(.+?)&team=(.+?)\"", response.content)
    if len(matches) > 0:
      self.competitive = True
      radiant = { "name": matches[0][1], "id": matches[0][0] }
      dire    = { "name": matches[1][1], "id": matches[1][0] }
      if re.findall("</a></td><td>(.*?)<", response.content)[1].strip().lower() == "radiant":
        self.winner, self.loser = radiant, dire
      else:
        self.winner, self.loser = dire, radiant
    else:
      self.competitive = False
      self.winner = { "name": "N/A", "id": "N/A" }
      self.loser  = { "name": "N/A", "id": "N/A" }

  def __str__(self):
    return "\n".join([
      "Match:       {0}".format(self.match_id),
      "Patch:       {0}".format(self.patch),
      "Competitive: {0}".format(self.competitive),
      "Winner:     {name} ({id})".format(**self.winner),
      "Loser:      {name} ({id})".format(**self.loser)
    ])

  def to_json(self):
    return {
      "id":          self.match_id,
      "patch":       self.patch,
      "competitive": self.competitive,
      "winner":      self.winner,
      "loser":       self.loser
    }


if __name__ == "__main__":
  for match in [1918457362, 1918614355, 1860830637]:
    m = Match(match)
    print(m)
    print(m.to_json())
    print("")
