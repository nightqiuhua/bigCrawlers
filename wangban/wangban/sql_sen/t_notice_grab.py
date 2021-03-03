# -*- coding: utf-8 -*-
sql_t_notice_grab_create_table = """CREATE TABLE IF NOT EXISTS T_NOTICE_GRAB (
            `ng_code` VARCHAR(255),
            `ng_title` VARCHAR(500),
            `ng_publish_time` VARCHAR(20),
            `ng_content` LONGTEXT,
            `ng_url` VARCHAR(500),
            `ng_area` VARCHAR(50),
            `ng_site` VARCHAR(255),
            `ng_type` VARCHAR(20),
            `create_time` VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1"""

sql_t_notice_grab_insert = """INSERT INTO t_notice_grab (`ng_code`, `ng_title`,`ng_publish_time`,
                       `ng_content`,`ng_url`,`ng_area`,`ng_site`,`ng_type`,`create_time`)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""


def main():
    return sql_t_notice_grab_create_table,sql_t_notice_grab_insert