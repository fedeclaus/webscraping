# webscraping
Several webscraping projects

In glacio2.py i tried to make automatic (together with windows task scheduler) MODIS image download from NASA World View. Basic use of urllib.request and knowing some of url manipulation.

In glacio_polar, i tried the same. It is a bit more difficult. polarview.aq hasn´t an API, or a regular provision of Sentinel 1 radar images. I tried to filter what my mates at Argentina SHN Sea Ice division mostly use. In this script, I used BeautifulSoup4(BS4) and Selenium.

In scrap_metar, i am saving in a pythonanywhere.com account Marambio Base METARs that are not kept in a public archive, mostly for educational purpose. Next step, to keep analysis, satellite images and forecasts and organize METAR and SYNOP in a SQL DB.
