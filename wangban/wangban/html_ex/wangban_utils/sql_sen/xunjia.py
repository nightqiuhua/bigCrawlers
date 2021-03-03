# -*- coding: utf-8 -*-
sql_xunjia_create_table = """CREATE TABLE IF NOT EXISTS XUNJIA (
            `class_1` VARCHAR(200),
            `class_2` VARCHAR(200),
            `class_3` VARCHAR(200),
            `province` VARCHAR(20),
            `city` VARCHAR(20),
            `mt_name` VARCHAR(20),
            `link` VARCHAR(1000),
            `pubdate` VARCHAR(30),
            `mt_html` MEDIUMTEXT,
            `gettime` VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1"""

sql_xunjia_insert = """INSERT INTO XUNJIA (`class_1`, `class_2`,`class_3`,`province`,
                            `city`,`mt_name`,`link`,`mt_html`,
                            `pubdate`,`gettime`) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
#sql_xunjia_create_table = """CREATE TABLE IF NOT EXISTS ZAOJIATONG_XUNJIA (
#            `class_1` VARCHAR(200),
#            `class_2` VARCHAR(200),
#            `class_3` VARCHAR(200),
#            `province` VARCHAR(20),
#            `city` VARCHAR(20),
#            `mt_name` VARCHAR(20),
#            `link` VARCHAR(1000),
#            `pubdate` VARCHAR(30),
#            `mt_html` MEDIUMTEXT,
#            `gettime` VARCHAR(100)
#) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1"""
#
#sql_xunjia_insert = """INSERT INTO ZAOJIATONG_XUNJIA (`class_1`, `class_2`,`class_3`,`province`,
#                            `city`,`mt_name`,`link`,`mt_html`,
#                            `pubdate`,`gettime`) 
#        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""#