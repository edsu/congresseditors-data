# congresseditors-data

This repository contains the archive for the [congresseditors] Twitter account
that tweets edits to Wikipedia articles about members of US congress. The
archive was downloaded directly from Twitter and can be updated on request (just
submit an issue ticket here on GitHub). The source code for the bot that listens
to Wikipedia for edits is also [available].

In addition to the archive this repository also includes `diffs.jsonl` which is
a snapshot of the revision information from Wikipedia's API. The included
`download.py` script will read the `tweets.csv` from the Twitter archive,
extract the diff URL from the tweet, and fetch the detailed revision metadata
using the [compare] API call. The tweet metadata is also added to the revision
which can be useful in cases where the revision has been deleted (rare, but it
happens). The result is written as line oriented JSON.  Here is an example of
what a revision looks like: 

```
{
  "fromid": 29699016,
  "fromrevid": 859421957,
  "fromns": 0,
  "fromtitle": "Thom Tillis",
  "fromsize": 32912,
  "fromuser": "Goodone121",
  "fromuserid": 5526749,
  "fromcomment": "Undid revision 859326304 by [[Special:Contributions/75.148.103.49|75.148.103.49]] ([[User talk:75.148.103.49|talk]])(uncited addition)",
  "fromparsedcomment": "Undid revision 859326304 by <a href=\"/wiki/Special:Contributions/75.148.103.49\" title=\"Special:Contributions/75.148.103.49\">75.148.103.49</a> (<a href=\"/wiki/User_talk:75.148.103.49\" title=\"User talk:75.148.103.49\">talk</a>)(uncited addition)",
  "toid": 29699016,
  "torevid": 859699623,
  "tons": 0,
  "totitle": "Thom Tillis",
  "tosize": 33970,
  "touser": "Btyner",
  "touserid": 185327,
  "tocomment": "/* Environment */ update, add citations",
  "toparsedcomment": "<a href=\"/wiki/Thom_Tillis#Environment\" title=\"Thom Tillis\">→</a>‎<span dir=\"auto\"><span class=\"autocomment\">Environment: </span> update, add citations</span>",
  "diffsize": 4793,
  "*": "<tr>\n  <td colspan=\"2\" class=\"diff-lineno\">Line 88:</td>\n  <td colspan=\"2\" class=\"diff-lineno\">Line 88:</td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>====Environment====</div></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>====Environment====</div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>In 2014, Tillis said that climate change is not a fact,&lt;ref&gt;{{cite web|publisher=The Charlotte Observer|date=April 22, 2014|last1=Morrill|first1=Jim|last2=Frank|first2=John|last3=Portillo|first3=Ely|title=Greg Brannon targets Thom Tillis in the first GOP Senate debate|url=https://www.charlotteobserver.com/news/politics-government/article9115142.html}}&lt;/ref&gt; and in 2015, voted against an amendment that said human activity is a contributor.&lt;ref&gt;{{cite web|date=January 22, 2015|publisher=Citizen Times|last=Barrett|first=Mark|title=Burr, Tillis say climate change is real — but|url=https://www.citizen-times.com/story/elections/2015/01/22/burr-tillis-climate-change-global-warming-not-a-hoax/22170965/}}&lt;/ref&gt;</div></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\"><a class=\"mw-diff-movedpara-left\" title=\"Paragraph was moved. Click to jump to new location.\" href=\"#movedpara_3_1_rhs\">&#x26AB;</a></td>\n  <td class=\"diff-deletedline\"><div><a name=\"movedpara_2_0_lhs\"></a>In 2017, Tillis was one of 22 senators to sign a letter&lt;ref&gt;{{cite web|last1=Inhofe|first1=James|title=Senator|url=https://www.inhofe.senate.gov/download/?id=E1E34574-5655-42AA-92E8-0D23DC8C33BA&amp;download=1|accessdate=7 June 2017}}&lt;/ref&gt; to President [[Donald Trump]] urging the President to have the United States withdraw from the [[Paris Agreement]]. According to the [[Center for Responsive Politics]], Tillis has received over $260,000 from oil, gas and coal interests since 2012.&lt;ref&gt;{{cite web|url=https://www.theguardian.com/us-news/2017/jun/01/republican-senators-paris-climate-deal-energy-donations|accessdate=June 1, 2017|publisher=The Guardian|date=June 1, 2017|title=The Republicans who urged Trump to pull out of Paris deal are big oil darlings}}&lt;/ref&gt;</div></td>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\"><a class=\"mw-diff-movedpara-right\" title=\"Paragraph was moved. Click to jump to old location.\" href=\"#movedpara_2_0_lhs\">&#x26AB;</a></td>\n  <td class=\"diff-addedline\"><div><a name=\"movedpara_3_1_rhs\"></a>In 2017, Tillis was one of 22 senators to sign a letter&lt;ref&gt;{{cite web|last1=Inhofe|first1=James|title=Senator|url=https://www.inhofe.senate.gov/download/?id=E1E34574-5655-42AA-92E8-0D23DC8C33BA&amp;download=1|accessdate=7 June 2017}}&lt;/ref&gt; to President [[Donald Trump]] urging the President to have the United States withdraw from the [[Paris Agreement]]. According to the [[Center for Responsive Politics]], Tillis has received over $260,000 from oil, gas and coal interests since 2012.&lt;ref&gt;{{cite web|url=https://www.theguardian.com/us-news/2017/jun/01/republican-senators-paris-climate-deal-energy-donations|accessdate=June 1, 2017|publisher=The Guardian|date=June 1, 2017|title=The Republicans who urged Trump to pull out of Paris deal are big oil darlings}}&lt;/ref&gt;<ins class=\"diffchange diffchange-inline\"> </ins></div></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"></td>\n</tr>\n<tr>\n  <td colspan=\"2\" class=\"diff-empty\">&#160;</td>\n  <td class=\"diff-marker\">+</td>\n  <td class=\"diff-addedline\"><div>As of 2018, Tillis now says that human activity is in fact a contributing factor to climate change. &lt;ref&gt;{{cite web|url=http://spectrumlocalnews.com/nc/charlotte/news/2018/08/07/exclusive-thom-tillis-speaks-on-climate-change|publisher=Spectrum News Charlotte|date=August 7, 2018|title=EXCLUSIVE: Thom Tillis speaks on climate change}}&lt;/ref&gt;</div></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"></td>\n</tr>\n<tr>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>====Gun law====</div></td>\n  <td class=\"diff-marker\">&#160;</td>\n  <td class=\"diff-context\"><div>====Gun law====</div></td>\n</tr>\n\n<!-- diff cache key enwiki:diff:wikidiff2:1.12:old-859421957:rev-859699623:1.7.3:25 -->\n",
  "tweet": {
    "tweet_id": "1041032304225865733",
    "in_reply_to_status_id": "",
    "in_reply_to_user_id": "",
    "timestamp": "2018-09-15 18:33:37 +0000",
    "source": "<a href=\"https://tools.wmflabs.org/anon/\" rel=\"nofollow\">anon-wikipedia</a>",
    "text": "Thom Tillis Wikipedia article edited by Btyner https://t.co/BjeAq768a3",
    "retweeted_status_id": "",
    "retweeted_status_user_id": "",
    "retweeted_status_timestamp": "",
    "expanded_urls": "https://en.wikipedia.org/w/index.php?diff=859699623&oldid=859421957"
  }
}
```

The `users.jsonl` file contains information for the users referenced in the
`diffs.jsonl`. It can be generated using the `users.py` program which fetches
the data from Wikipedia's [users] API call. Here is an example of what
information Wikipedia make available for a user:

```
{
  "editcount": 82479,
  "attachedlocal": {
    "CentralAuth": "",
    "local": ""
  },
  "name": "Barek",
  "rights": [
    "templateeditor",
    "changetags",
    "extendedconfirmed",
    "suppressredirect",
    "noratelimit",
    "deleterevision",
    "deletelogentry",
    "editcontentmodel",
    "block",
    "createaccount",
    "delete",
    "deletedhistory",
    "deletedtext",
    "undelete",
    "editinterface",
    "editsitejson",
    "edituserjson",
    "import",
    "move",
    "move-subpages",
    "move-rootuserpages",
    "move-categorypages",
    "patrol",
    "autopatrol",
    "protect",
    "editprotected",
    "rollback",
    "upload",
    "reupload",
    "reupload-shared",
    "unwatchedpages",
    "autoconfirmed",
    "editsemiprotected",
    "ipblock-exempt",
    "blockemail",
    "markbotedits",
    "apihighlimits",
    "browsearchive",
    "movefile",
    "unblockself",
    "mergehistory",
    "managechangetags",
    "deletechangetags",
    "autoreview",
    "stablesettings",
    "movestable",
    "review",
    "abusefilter-revert",
    "abusefilter-view-private",
    "jsonconfig-flush",
    "oathauth-enable",
    "tboverride",
    "titleblacklistlog",
    "transcode-reset",
    "transcode-status",
    "globalblock-whitelist",
    "nuke",
    "skipcaptcha",
    "override-antispoof",
    "abusefilter-log-detail",
    "massmessage",
    "read",
    "edit",
    "createtalk",
    "writeapi",
    "viewmywatchlist",
    "editmywatchlist",
    "viewmyprivateinfo",
    "editmyprivateinfo",
    "editmyoptions",
    "centralauth-merge",
    "abusefilter-view",
    "abusefilter-log",
    "vipsscaler-test",
    "collectionsaveasuserpage",
    "reupload-own",
    "createpage",
    "minoredit",
    "editmyusercss",
    "editmyuserjson",
    "editmyuserjs",
    "purge",
    "sendemail",
    "applychangetags",
    "spamblacklistlog",
    "mwoauthmanagemygrants",
    "collectionsaveascommunitypage"
  ],
  "groupmemberships": [
    {
      "group": "sysop",
      "expiry": "infinity"
    }
  ],
  "gender": "male",
  "implicitgroups": [
    "*",
    "user",
    "autoconfirmed"
  ],
  "userid": 1746167,
  "centralids": {
    "CentralAuth": 2872,
    "local": 1746167
  },
  "groups": [
    "sysop",
    "*",
    "user",
    "autoconfirmed"
  ],
  "registration": "2006-07-06T20:41:33Z",
  "emailable": ""
}
```

[available]: https://github.com/edsu/congresseditors
[congresseditors]: https://twitter.com/congresseditors
[compare]: https://en.wikipedia.org/w/api.php?action=help&modules=compare
[users]: https://en.wikipedia.org/w/api.php?action=help&modules=query%2Busers
