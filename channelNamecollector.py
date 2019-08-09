import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class channelHandling():
    def __init__(self):
        pass

    # Read text file from blog
    def readList(self):
        search = "channelList.txt"
        with open(search) as f:
            terms = f.read().splitlines()

        self.channelNames=[]
        self.channelLinks=[]
        for i,line in enumerate(terms):
            if(i%2==0):
                self.channelNames.append(line)
            else:
                self.channelLinks.append(line)

    def toAsci(self,st):
        nst=""
        for i in st:
            if(i.isalnum()):
                nst+=i
        if(len(nst)==0):
            nst = "BAD NAME"
        return nst

    # From random blog
    def getChannels(self):
        # Filename to write
        filename = "ChannelList.txt"

        # Open the file with writing permission
        myfile = open(filename, 'w')
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome("C:\\Python36\\selenium\\webdriver\\chrome\\chromedriver.exe",chrome_options=chrome_options)
        # driver = webdriver.PhantomJS("C:\\Python36\\selenium\\webdriver\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")

        driver.get("https://blog.feedspot.com/beauty_youtube_channels/")
        links=driver.find_elements_by_class_name('ext')
        titles=driver.find_elements_by_class_name('tlink')

        for i in range(len(links)):
            title=titles[i].get_attribute('text')
            link=links[i].get_attribute('href')
            myfile.write(title)
            myfile.write("\n")
            myfile.write(link)
            myfile.write('\n')

        print("Done")

        # Close the file
        myfile.close()
        driver.close()

    # Get links from channel video page
    def getVideoLinks(self,channels=-1,neededLinks=5,start=0):
        cwd=os.getcwd()+"/Data"
        os.chdir(cwd)
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome("C:\\Python36\\selenium\\webdriver\\chrome\\chromedriver.exe",chrome_options=chrome_options)

        if(channels==-1):
            channels = len(self.channelLinks)

        for i in range(start,channels):
            driver.get(self.channelLinks[i])
            folderName=self.toAsci(self.channelNames[i])
            try:
                os.chdir(folderName)
            except:
                os.makedirs('./'+folderName)
                os.chdir(folderName)

            filename = str(folderName)+".txt"
            fileWriter = open(filename,'w')

            videos = driver.find_elements_by_id('thumbnail')
            for j in range(neededLinks):
                videoLink = videos[j].get_attribute('href')
                if(videoLink==None):
                    continue
                print(videoLink)
                fileWriter.write(videoLink)
                fileWriter.write('\n')

            os.chdir(cwd)

            # fileWriter.close()

        driver.close()

if __name__=='__main__':
    # getChannels()
    ch = channelHandling()
    ch.readList()
    ch.getVideoLinks(4,7,3)
    pass
