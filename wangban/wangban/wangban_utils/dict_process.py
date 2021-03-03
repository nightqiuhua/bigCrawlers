def bfs(dict_value):
    queue = []
    queue.append(dict_value)
    while queue:
        node = queue.pop(0)
        #print(node)
        #paths = []
        #print(node)
        for key in node.keys():
            value = node[key]
            if not isinstance(value,dict):
                #print(value)
                paths = record_value_path(value,dict_value)
                yield value,paths
            if isinstance(value,dict):
                queue.append(value)

def record_value_path(key,dict_value,result_list=None):
    if not result_list:
        result_list=[]
    for ind,i in enumerate(gen_dict_extract(key,dict_value)):
        #print('i',i)
        result_list.extend(i)
    return result_list


def gen_dict_extract(check_key, var,curr_pos = None):
    if curr_pos == None:
        curr_pos = []
    if isinstance(var,dict):
        for k, v in var.items():
            if v == check_key:
                curr_pos.append(k)
                yield curr_pos[:]
            if isinstance(v, dict):
                curr_pos.append(k)
                for result in gen_dict_extract(check_key,v,curr_pos):
                    yield result
        if len(curr_pos)>0:
            curr_pos.pop()

def new_tasks(task_list):
    work_urls = []
    for task in task_list:
        for sub_url,value_list in bfs(task):
            sub_url_dict = {}
            sub_url_dict['an_major'] = value_list[0]
            sub_url_dict['an_type'] = value_list[1]
            sub_url_dict['an_sub'] = value_list[2]
            sub_url_dict['an_sub_url'] =sub_url
            work_urls.append(sub_url_dict)
    print(work_urls)


if __name__ == '__main__':
    
    data =     [{'建设工程':{
    '招标公告':{
    '施工':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001001/005001001001/MoreInfo.aspx?CategoryNum=005001001001',
    '设计':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001001/005001001002/MoreInfo.aspx?CategoryNum=005001001002',
    '监理':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001001/005001001003/MoreInfo.aspx?CategoryNum=005001001003',
    '其他':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001001/005001001004/MoreInfo.aspx?CategoryNum=005001001004',
    '补充通知':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001001/005001001005/MoreInfo.aspx?CategoryNum=005001001005',
    },
    '中标公示':{
    '施工':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001002/005001002001/MoreInfo.aspx?CategoryNum=005001002001',
    '设计':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001002/005001002002/MoreInfo.aspx?CategoryNum=005001002002',
    '监理':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001002/005001002003/MoreInfo.aspx?CategoryNum=005001002003',
    '其他':'http://www.cajyzx.org.cn:8080/chunanweb/jyxx/005001/005001002/005001002004/MoreInfo.aspx?CategoryNum=005001002004',
    },
    }}]
    new_tasks(data)