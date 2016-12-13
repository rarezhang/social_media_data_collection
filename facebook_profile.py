######################################################################
## facebook_profile.py 
## Written by Wenli Zhang <catezhang@qq.com> for the MIS586 HW
## 
## usage: 
## 	1. APP_SECRET and APP_ID -> facebook credentials
##	2. file -> output paths
##	3. list_companies -> facebook pageID / pageName
## description:  
##    Output:
## 				1. file -> profile, raw json
##				 
#######################################################################

import urllib2
import json

 
def create_post_url(graph_url, APP_ID, APP_SECRET): 
    #create authenticated post URL
    post_args = "?key=value&access_token=" + APP_ID + "|" + APP_SECRET
    post_url = graph_url + post_args
 
    return post_url
    
def render_to_json(graph_url):
    #render graph url call to JSON
    web_response = urllib2.urlopen(graph_url)
    readable_page = web_response.read()
    json_data = json.loads(readable_page)
    
    return json_data
 
    
def main():
    #simple data pull App Secret and App ID
    APP_SECRET = "xxxxxxxxxxxxxxxxxxx"
    APP_ID = "xxxxxxxxxxxxxxxxxxxxx"
    
    #to find go to page's FB page, at the end of URL find username
    #e.g. http://facebook.com/walmart, walmart is the username
    list_companies = ['176104589110851','218675561564524']
    graph_url = "https://graph.facebook.com/"

    file = open("C:\\Users\\xxxxxxxxxxxxxxxx\\facebook_profile_large.txt", "w")
    for company in list_companies:
        #make graph api url with company username
        current_page = graph_url + company
                
        post_url = create_post_url(current_page, APP_ID, APP_SECRET)
                
        #open public page in facebook graph api
        json_fbpage = render_to_json(post_url )
##        print(json.dumps(json_fbpage, indent=4, sort_keys=True))
        file.write(json.dumps(json_fbpage, indent=4, sort_keys=True)+"\n")

    file.close()
    print("done!")


            

 
if __name__ == "__main__":
    main()   
