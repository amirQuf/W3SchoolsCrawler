from bs4 import BeautifulSoup
import requests
import csv

limit = 0
el = []
data =[0,'','','']
header = ['id','url','doc', 'label']

urls = {
'html':'https://www.w3schools.com/html/',
'js':"https://www.w3schools.com/js/",
'python': "https://www.w3schools.com/python/" ,  
}

root_html = requests.get(urls['html'])    
soup_html = BeautifulSoup(root_html.content, "html.parser")
html_link_list = soup_html.select('#leftmenuinnerinner a')

# 0-33 html 
with open('w3.csv', 'w', encoding='UTF8') as fout:
    writer = csv.writer(fout)
    writer.writerow(header)
    print('<----html----->')
    for item in html_link_list:
        
        print (limit)
        data[0]= limit
        new_url = urls['html']+item['href']
        data[1]= new_url
        print(new_url)  
        new_url_=requests.get(new_url)
        soup_html_content = BeautifulSoup(new_url_.content, "html.parser")
        el.append(soup_html_content.find(
            id = 'main'))
        data[2]= el[limit].text.strip()
        data[3]='html'
        # print(data)
        writer.writerow(data)
        with open('{0}.txt'.format(limit) , 'w') as f :
            f.write(el[limit].text.strip())
            f.close()
        limit+=1
        if limit == 33:
            break
        writer.writerow(data)    


    print('<----js---->')
    root_js = requests.get("https://www.w3schools.com/js/default.asp")
    soup_js = BeautifulSoup(root_js.content, "html.parser")
    js_link_list = soup_js.select('#leftmenuinnerinner a')
    print (js_link_list)
    # 34-66 js 
    for item  in js_link_list:
        print (limit)
        data[0]= limit
        new_url = urls['js'] + item['href']
        data[1]= new_url
        print(new_url)
        new_url_js=requests.get(new_url)
        soup_js_content = BeautifulSoup(new_url_js.content, "html.parser")
        el_js= soup_js_content.find(
            id = 'main')
        data[2]= el_js.text.strip()
        data[3]='js'
        
        # print(data)
        with open('{0}.txt'.format(limit) , 'w') as f :
            f.write(data[2])
            f.close()
        limit+=1
        if limit == 66:
            break
        writer.writerow(data)


    # 67-99 python
    root_py = requests.get(urls['python'])
    soup_py = BeautifulSoup(root_py.content, "html.parser")
    py_link_list = soup_py.select('#leftmenuinnerinner a')
    print("<-- python -->")
    for item  in py_link_list:
        data[0]= limit
        print (limit)
        new_url = urls['python'] + item['href']
        data[1]= new_url
        print(new_url)
        new_url_py=requests.get(new_url)
        soup_py_content = BeautifulSoup(new_url_py.content, "html.parser")
        el_py= soup_py_content.find(
            id = 'main')
        data[2]= el_js.text.strip()
        data[3]='python'
        # print(data)
        with open('{0}.txt'.format(limit) , 'w') as f :
            f.write(el_py.text.strip())
            f.close()
        limit+=1
        if limit == 100:
            break
        writer.writerow(data)
    fout.close()
    print("<--done-->")