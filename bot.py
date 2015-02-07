from bs4 import BeautifulSoup
import requests

url = 'https://www.facebook.com/andrew.benson.4/posts/10203823674740568'
print requests.get(url).text.encode('utf-8')
parser = BeautifulSoup(requests.get(url).text) 
comment_nodes = parser.find_all('div', class_='UFICommentContent')
comments = []
for comment_node in comment_nodes:
  name_node = commend_node.children()[0]
  comment_content_node = commend_node.children()[2]
  print name_node
