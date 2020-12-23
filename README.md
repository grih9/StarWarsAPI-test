# StarWarsAPI-test

<b>python modules:</b> pytest, requests, collections, string</br>
<b>pytest plugins:</b> pytest‐html

<b>command to start tests:</b> pytest ‐k tasks -v --html=report.html --self-contained-html

<h4>task13:</h4> Bug with use of search parameter with wookiee format. When we use wookiee to get data it's expected that we will search data
using names on wookiee, but it search names in English. I think the root of this is that data is stored in English and than
translated to wookiee to represent to visitor. Search parameter work with data on db but not with data that will be represented. <br>
Also it is impossible to get schema using wookiee format. It gave us only one string on wookiee format that can not be understood.
