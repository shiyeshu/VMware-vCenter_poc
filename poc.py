import requests
def go(url):
        
        if 'http' not in url:
            url = 'http://'+url
            pass
        else: 
            url =url+ '/eam/vib?id=C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\vcdb.properties'
        geturl = requests.get(url)
        status=geturl.status_code
        if status == 200:
            print ("存在漏洞,请及时升级")
            pass
        else:
            print ("漏洞不存在")       
            pass
if __name__ == '__main__':
	t=input('请输入url\n')
	go(t)
