######################################################################
## facebook_likedByThisPage.py
## Written by Wenli Zhang <catezhang@qq.com> for the MIS586 HW
## 
## usage: 
## 	1. APP_SECRET and APP_ID -> facebook credentials
##	2. file1, file2, file3 -> output paths
##	3. list_companies -> facebook pageID / pageName
## description:  
##    Output:
## 				1. file1 -> Liked by this page, raw json
##				2. file2 -> edges for gephi 
##				3. file3 -> input for facebook_profile.py          
#######################################################################

import urllib2
import json

 
def create_post_url(graph_url, APP_ID, APP_SECRET): 
    #create authenticated post URL
    post_args = "/likes?limit=2000&access_token=" + APP_ID + "|" + APP_SECRET
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
    APP_SECRET = "xxxxxxxxxxxxxxxxxxxx"
    APP_ID = "xxxxxxxxxxxxxxxxxx"
    
    #to find go to page's FB page, at the end of URL find username
    #e.g. http://facebook.com/walmart, walmart is the username
    list_companies = ["sustainableenergyforall","euroenergycentre"]
    graph_url = "https://graph.facebook.com/v2.1/"

    file1 = open("C:\\Users\\xxxxxxxxxxxxxxxxxxxx\\facebook_likedByThisPage.txt", "w")
    file2 = open("C:\\Users\\xxxxxxxxxxxxxxxxxxxx\facebook_friendlist.txt", "w")
    file3 = open("C:\\Users\\xxxxxxxxxxxxxxxxxxxx\facebook_profileList.txt", "w")
    for company in list_companies:
        #make graph api url with company username
        current_page = graph_url + company
       
        post_url = create_post_url(current_page, APP_ID, APP_SECRET)
        
        #open public page in facebook graph api
        json_fbpage = render_to_json(post_url)
        file1.write("company_name: "+company+":\n"+json.dumps(json_fbpage, indent=4, sort_keys=True)+"\n")

        friend_data=json_fbpage["data"]
        num = len(friend_data)
        i = 0
        while i < num:
            file2.write(company+","+friend_data[i]["id"]+"\n")
            file3.write("'"+friend_data[i]["id"]+"'"+",")
            i=i+1
			
    file1.close()
    file2.close()
    file3.close()
    print("done!")


if __name__ == "__main__":
    main()   
