import re
from urllib import request

file_num = 0

protocol = 'http'
host = 'humor.oceanmate.co.kr'
uri = '/bbs/board.php'
params = '?bo_table=humor&wr_id='

for post_no in range(2100, 2200):
    post_url = "%s://%s%s%s%s" % (protocol, host, uri, params, post_no)
    html = request.urlopen(post_url).read()

    image_url_regex = "%s://%s/fun_img/[^\"\s>]+" % (protocol, host)
    image_urls = re.findall(image_url_regex, str(html))

    for image_url in image_urls:
        image_file = open('%s.jpg' % (file_num,), 'wb')
        image_file.write(request.urlopen(image_url).read())
        image_file.close()
        file_num += 1