# -*- coding: utf-8 -*-
sql_jiangbei_create_table = """CREATE TABLE IF NOT EXISTS JIANGBEI (
            `sitename` VARCHAR(200),
            `region` VARCHAR(10),
            `county` VARCHAR(20),
            `type` VARCHAR(20),
            `largeclass` VARCHAR(150),
            `smallclass` VARCHAR(150),
            `title` TEXT,
            `pubdate` VARCHAR(20),
            `texttitle` TEXT,
            `text` MEDIUMTEXT,
            `link` VARCHAR(2500),
            `gettime` VARCHAR(100),
            `is_cl` INT(11) default 0,
            `number` INT(2)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1"""

sql_jiangbei_insert = """INSERT INTO JIANGBEI (`sitename`, `region`,`county`,
                       `type`,`largeclass`,`smallclass`,`title`,`pubdate`,`texttitle`,`text`,
                       `link`,`gettime`,`number`)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
