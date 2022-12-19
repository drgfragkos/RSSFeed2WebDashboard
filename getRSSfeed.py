# This script requires the `requests` and `beautifulsoup4` libraries
# These can be installed using `pip`:
#
#   pip install requests beautifulsoup4
#
#   https://pypi.org/project/requests/
#   https://scrapfly.io/blog/web-scraping-with-python-beautifulsoup/
#   https://www.skytowner.com/explore/deleting_an_attribute_in_beautiful_soup


#Ubuntu
#sudo apt-get install libxml2-utils
#Cygwin
#apt-cyg install libxml2
#MacOS
#To install this on MacOS with Homebrew just do: brew install libxml2


# https://www.cisa.gov/uscert/ics/ICS-CERT-Feeds
# https://www.cisa.gov/uscert/ncas/current-activity.xml


####
# Import the `requests` and `beautifulsoup4` modules
import requests
from bs4 import BeautifulSoup
import html
# Import the datetime module
import datetime
import pytz
import re
import time

# Use the datetime.now() method to get the current date and time
#now = datetime.datetime.now()
#now = datetime.now(timezone.utc)
time_now_zone = datetime.datetime.now(pytz.timezone("Asia/Dubai"))
#print("Current Time in the UAE is : ", time_now_zone)
#print("Set Timezone : ", time_now_zone.tzinfo)                     # Prints the set timezone e.g. Asia/Dubai
# Use the strftime method to specify the format in which you want to display the date and time
#str_lastupdated = now.strftime("%A, %d-%b-%Y %H:%M:%S %Z")
str_lastupdated = time_now_zone.strftime("%A, %d-%b-%Y %H:%M:%S %Z")
#print("Last Updated: " + str_lastupdated)

# Define a function that accepts a URL to an XML RSS feed and returns the parsed content
def parse_rss_feed(url):
  # Use the `requests` library to fetch the contents of the URL
  response = requests.get(url)

  # special case where some characters such as < and > are written in the code as &lt; and &gt;. That need to be unescaped because BS4 cannot handle those. 
  #xml_string = html.unescape(response.text)

  # Parse the XML content using `beautifulsoup4`
  soup = BeautifulSoup(response.content, "xml")  
  #soup = BeautifulSoup(xml_string, "xml")  

  # Find all div tags with the specified class and remove them from the XML
  #classToIgnore = ["field field--name-body field--type-text-with-summary field--label-hidden field--item"]
  #classToIgnore = ["field"]
  #for div in soup.find_all('div', class_=lambda x: x in classToIgnore):
  #  div.decompose()
  # Print the updated XML
  #print(soup.prettify())
  # Return the parsed content
  return soup

# Define the URL of the RSS feed that we want to parse
url = "https://www.cisa.gov/uscert/ncas/current-activity.xml"

# Parse the RSS feed
rss_feed = parse_rss_feed(url)

with open("rssfeed-output.xml", "w") as f:
  f.write(rss_feed.decode())

#print(rss_feed.prettify())



#make HTML from XML #############################################
# create an empty HTML file
with open('rssfeed-output.html', 'w') as f:
#    f.write('<!DOCTYPE html>\n')
#    f.write('<html>\n')
#    f.write('<head>\n')
#    f.write('  <title>CISA Current Activity</title>\n')
#    f.write('  <style>\n')
#    f.write('    body {\n')
#    f.write('      font-family: Calibri;\n')
#    f.write('      font-size: 9pt;\n')
#    f.write('      background-color: rgb(22, 17, 17);\n')
#    f.write('      color: rgb(47, 199, 42);\n')
#    f.write('    }\n')
#    f.write('    a {\n')
#    f.write('      color: rgb(47, 199, 42);\n')
#    f.write('      font-weight: bold;\n')
#    f.write('    }\n')
#    f.write('    hr {\n')
#    f.write('      border-color: rgb(47, 199, 42);\n')
#    f.write('    }\n')
#    f.write('  </style>\n')        
#    f.write('</head>\n')
#    f.write('<body>\n')
#    f.write('\n')
#    f.write('<h1>CISA Current Activity</h1><br /><hr width="100%"/>\n')

    htmlstring = """
    <!DOCTYPE html>
    <html>
    <head>
      <title>CISA Current Activity</title>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css">
      <style>
        body {
          font-family: Calibri;
          font-size: 9pt;
          background-color: rgb(22, 17, 17);
          color: rgb(47, 199, 42);
        }
        a {
          color: rgb(47, 199, 42);
          font-weight: bold;
        }
        hr {
          border-color: rgb(47, 199, 42);
        }
      </style>        
    </head>
    <body>
    
    <table bgcolor="#2fc72a" width="100%" border="0">
      <tr>
        <td style="color: rgb(22, 17, 17); font-size: 30px;"  align="left"><b>CISA Current Activity</b></td>
        <td style="color: rgb(22, 17, 17); font-size: 10px;" align="center" width="270px">
            https://www.cisa.gov/uscert/ncas/current-activity &nbsp;&nbsp;<a href="https://www.cisa.gov/uscert/ncas/current-activity" style="color: rgb(22, 17, 17);"><i class="fa fa-external-link-alt" aria-hidden="true" style="color: rgb(22, 17, 17);" title="www"></i></a> &nbsp;&nbsp;<a href="https://www.cisa.gov/uscert/ncas/current-activity.xml" style="color: rgb(22, 17, 17);"><i class="fa fa-code" aria-hidden="true" style="color: rgb(22, 17, 17);" title="xml"></i></a>
            <br />""" + "Last Refreshed: " + str_lastupdated + """
        </td>
        <td style="color: rgb(22, 17, 17);" width="100px" align="center">&nbsp;SCSC&nbsp;</td>
      <tr>
    </table>
    <hr width="100%"/>
    """
    

#    htmlstring = '<!DOCTYPE html>\n'
#    htmlstring = htmlstring + '<html>\n'
#    htmlstring = htmlstring + '<head>\n'
#    htmlstring = htmlstring + '  <title>CISA Current Activity</title>\n'
#    htmlstring = htmlstring + '  <style>\n'
#    htmlstring = htmlstring + '    body {\n'
#    htmlstring = htmlstring + '      font-family: Calibri;\n'
#    htmlstring = htmlstring + '      font-size: 9pt;\n'
#    htmlstring = htmlstring + '      background-color: rgb(22, 17, 17);\n'
#    htmlstring = htmlstring + '      color: rgb(47, 199, 42);\n'
#    htmlstring = htmlstring + '    }\n'
#    htmlstring = htmlstring + '    a {\n'
#    htmlstring = htmlstring + '      color: rgb(47, 199, 42);\n'
#    htmlstring = htmlstring + '      font-weight: bold;\n'
#    htmlstring = htmlstring + '    }\n'
#    htmlstring = htmlstring + '    hr {\n'
#    htmlstring = htmlstring + '      border-color: rgb(47, 199, 42);\n'
#    htmlstring = htmlstring + '    }\n'
#    htmlstring = htmlstring + '  </style>\n'        
#    htmlstring = htmlstring + '</head>\n'
#    htmlstring = htmlstring + '<body>\n'
#    htmlstring = htmlstring + '\n'
#    htmlstring = htmlstring + '<h1>CISA Current Activity</h1><br /><hr width="100%"/>\n'
    f.write(htmlstring)

    
    
# Parse the XML file using BeautifulSoup
soup = BeautifulSoup(open("rssfeed-output.xml"), "xml")

# Open the output HTML file in write mode
with open("rssfeed-output.html", "a") as f:
  # Iterate over each item in the feed
  for item in soup.find_all("item"):
    # Extract the title, link, and description of the item
    title = item.title.text
    link = item.link.text
    description = item.description.text
    pub_date = item.find('pubDate')

    # Write the information to the output HTML file
    f.write("\n<h1>{}</h1>\n".format(title))                           ## The Title tag
    
    f.write("<a href='{}'>{}</a>\n".format(link, link))              ## The Link tag
    
    #f.write("<p>{}</p>\n".format(description))                      ## uses extra <p> tag for the Description tag, for more space if needed 
    f.write("{}\n".format(description))
    
    #f.write("<p>Publication date: " + pub_date.text + "</p>\n")     ## Alternative example to extract the Publication Date
    f.write("<p>Publication Date: {}</p>\n".format(pub_date))
    
    f.write('<hr width="100%"/>\n\n')                                    ## Add a line after each entry
    


# write the closing HTML tags
with open('rssfeed-output.html', 'a') as f:
    f.write('\n\n</body>\n')
    f.write('</html>\n')

            
            
#curl -L -s https://www.cisa.gov/uscert/ncas/current-activity.xml | grep -o '<link rel="alternate" type="application/rss+xml" href=".*" />' | sed 's/<link rel="alternate" type="application/rss+xml" href="\(.*\)" \/>/\1/' | xargs curl -L -s | xmllint --format -



#Sure, you can just select, find, or find_all the divs of interest in the usual way, and then call decompose() on those divs.
#For instance, if you want to remove all divs with class sidebar, you could do that with
## replace with `soup.findAll` if you are using BeautifulSoup3
#for div in soup.find_all("div", {'class':'sidebar'}): 
#    div.decompose()
#If you want to remove a div with a specific id, say main-content, you can do that with
#soup.find('div', id="main-content").decompose()


########################################################################################################################################
### Cheat way to add target="_blank" rel="noopener noreferrer" to all <a> tags in the .html file #######################################
###
# Read the input file
with open("rssfeed-output.html", "r") as f:
    text = f.read()

# Perform the substitution
text = re.sub(r"<a\s+", r'<a target="_blank" rel="noopener noreferrer" ', text)    # https://stackoverflow.com/questions/50709625/link-with-target-blank-and-rel-noopener-noreferrer-still-vulnerable

# Write the output to a file
time.sleep(1)
with open("rssfeed-output.html", "w") as f:
    f.write(text)

########################################################################################################################################
########################################################################################################################################