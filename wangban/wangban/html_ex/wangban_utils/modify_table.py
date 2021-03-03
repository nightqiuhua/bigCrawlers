import __init__
from mysql_util import MySqlDBClass
from tasks_2 import all_tasks
from tasks_1 import all_2_tasks

mysql_conn = MySqlDBClass()

def modify_table(an_sub_url,old_list,sheet_name,spe_dict):
    try:
        sql_sen = "UPDATE {sheet_name} SET largeclass='{largeclass}', type='{type}',smallclass='{smallclass}' WHERE largeclass='{old_large}' and type='{old_type}'".format(
                  sheet_name =sheet_name,largeclass=spe_dict[an_sub_url][0],type=spe_dict[an_sub_url][1],
                  smallclass=spe_dict[an_sub_url][2],old_large=old_list[1],old_type=old_list[2],old_small=old_list[3])
        mysql_conn.update_table(sql_sen)
    except Exception as e:
        raise e



def get_task(ori_tasks):
    for task in ori_tasks:
        for an_major,an_major_value in task.items():
            for an_type,an_type_value in an_major_value.items():
                for an_sub,an_sub_url in an_type_value.items():
                    yield [an_sub_url,an_major,an_type,an_sub]

def special_dict(new_tasks):
    spe_dict = {}
    for task in new_tasks:
        for an_major,an_major_value in task.items():
            for an_type,an_type_value in an_major_value.items():
                for an_sub,an_sub_url in an_type_value.items():
                    spe_dict[an_sub_url] = [an_major,an_type,an_sub]
    return spe_dict

def main(new_tasks,old_tasks):
    info_dict = special_dict(new_tasks['tasks'])
    print(info_dict)
    for task_info in get_task(old_tasks['tasks']):
        modify_table(task_info[0],task_info,new_tasks['name'],info_dict)


if __name__ == '__main__':
    new_tasks = all_tasks['fuyang']
    old_tasks = all_2_tasks['fuyang']
    main(new_tasks,old_tasks)#