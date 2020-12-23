# StarWarsAPI-test

<b>modules:</b> pytest, requests, collections, string</br>
<b>plugins:</b> pytest‐html

<b>start tests:</b> pytest ‐k tasks

<h4>task13:</h4> Bug with use of search parameter with wookie format. when we use wookie to get data it's expected that we will search data
using names on wookie, but it search names in English. I think the root of this is that data is stored in English and than
translated to wookie to represent to visitor. Search parameter work with data on db but not with data that will be represented.
