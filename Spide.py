from selenium import webdriver
url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
driver = webdriver.Firefox()
fout = open('output.html', 'w', encoding='utf-8')
fout.write("<html>\n")
fout.write("<body>\n")
fout.write("<table border=‘5’>\n")
fout.write("<tr>\n")
fout.write("<th>歌单</th>\n")
fout.write("<th>播放数</th>\n")
fout.write("<th>URL</th>\n")
fout.write("</tr>\n")
while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    data = driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    for i in range(len(data)):
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split('万')[0]) > 500:
            msk = data[i].find_element_by_css_selector("a.msk")
            fout.write("<tr>\n")
            fout.write("<td>%s</td>\n" % msk.get_attribute('title'))
            fout.write("<td>%s</td>\n" % nb)
            fout.write("<td>%s</td>\n" % msk.get_attribute('href'))
            fout.write("</tr>\n")
    url = driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
fout.write("</table>\n")
fout.write("</body>\n")
fout.write("</html>\n")
fout.close()



