
.open '{k[p1s3]}'
.databases
.mode csv
.import '{sv_01}' {sv_02}_{sv_03:02d}
.open '{k[zz1]}'
.databases
.header on
.tables
CREATE TABLE t_group
(  id           	INTEGER PRIMARY KEY AUTOINCREMENT
,  group_name		VARCHAR(255)
,  member_name		VARCHAR(255)
,  row_count		INTEGER
--
,  status		VARCHAR(255)
,  udc_int		INTEGER
,  udc_flt		FLOAT
--
,  udc_var		VARCHAR(255)
,  udc_txt		TEXT
);
SELECT 'Table t_group created in zz1 database' info;
CREATE TABLE s_group
(  id           	INTEGER PRIMARY KEY AUTOINCREMENT
,  group_name		VARCHAR(255)
,  member_name		VARCHAR(255)
,  row_count		INTEGER
--
,  status		VARCHAR(255)
,  udc_int		INTEGER
,  udc_flt		FLOAT
--
,  udc_var		VARCHAR(255)
,  udc_txt		TEXT
);
SELECT 'Table s_group created in zz1 database' info;
.tables
-- SELECT * FROM t_group WHERE group_name = 'p1s3_tables';
DELETE   FROM t_group WHERE group_name = 'p1s3_tables';
-- SELECT * FROM t_group WHERE group_name = 'p1s3_tables';
.open  '{k[p1s3]}'
attach '{k[zz1]}' as zz1;
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s3_tables' col_01, '{sv_02}_{sv_03:02}' col_02, col_03
  FROM ( SELECT count(1) col_03 FROM {sv_02}_{sv_03:02} );
.open '{k[zz1]}'
.head on
.mode columns
-- SELECT * FROM s_group WHERE group_name = 'p1s3_db';
DELETE FROM s_group WHERE group_name = 'p1s3_db';
-- SELECT * FROM s_group WHERE group_name = 'p1s3_db';
INSERT INTO s_group (group_name,member_name,row_count)
SELECT 'p1s3_db' col_01, 'all_tables' col_02, col_03
  FROM (SELECT sum(row_count)  col_03
          FROM t_group WHERE group_name = 'p1s3_tables');
SELECT group_name, member_name, row_count
  FROM t_group 
 WHERE group_name = 'p1s3_tables' ORDER BY id;
SELECT group_name, member_name, row_count
  FROM s_group 
 WHERE group_name = 'p1s3_db' ORDER BY id;
SELECT * FROM table_a;
.open  '{k[p1s4]}'
.databases
.header on
.tables
.width 3 20 12 7 10 5
.mode column
CREATE TABLE t_train
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , outage_duration  VARCHAR(255)
     , id               INTEGER
     , area_code        VARCHAR(255)
--                          
--                          
);
SELECT count(1) total_rows
FROM   t_train
;
pragma table_info('t_train');
CREATE TABLE t_test
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , outage_duration  VARCHAR(255)
     , id               INTEGER
     , area_code        VARCHAR(255)
--                          
);
SELECT count(1) total_rows
FROM   t_test
;
pragma table_info('t_test');
CREATE TABLE t_bband
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , id               INTEGER
     , broadband_type   VARCHAR(255)
--                          
);
SELECT count(1) total_rows
FROM   t_bband
;
pragma table_info('t_bband');
CREATE TABLE t_outage
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , id               INTEGER
     , outage_type      VARCHAR(255)
--                          
);
.tables
SELECT count(1) total_rows
FROM   t_outage
;
pragma table_info('t_outage');
CREATE TABLE t_report
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , id               INTEGER
     , log_report_type  VARCHAR(255)
     , volume           VARCHAR(255)
--                          
--                          
);
SELECT count(1) total_rows
FROM   t_report
;
pragma table_info('t_report');
CREATE TABLE t_server
(     r_id              INTEGER PRIMARY KEY AUTOINCREMENT
--                          
     , id               INTEGER
     , transit_server_type VARCHAR(255)
--                          
);
SELECT count(1) total_rows
FROM   t_server
;
pragma table_info('t_server');
.tables
.open  '{k[zz1]}'
attach '{k[p1s3]}' as p1s3;
attach '{k[p1s4]}' as p1s4;
.databases
INSERT INTO p1s4.t_train
(      outage_duration 
     , id              
     , area_code       
)
SELECT a.outage_duration 
     , a.id              
     , a.area_code       
  FROM p1s3.outage_dna_01 a
;
INSERT INTO p1s4.t_test
(      id              
     , area_code       
)
SELECT a.id              
     , a.area_code       
  FROM p1s3.outage_dnb_01 a
;
INSERT INTO p1s4.t_bband
(      id              
     , broadband_type  
)
SELECT a.id              
     , a.broadband_type  
  FROM p1s3.t_bband_01 a
;
INSERT INTO p1s4.t_outage
(      id              
     , outage_type     
)
SELECT a.id              
     , a.outage_type     
  FROM p1s3.t_outage_01 a
;
INSERT INTO p1s4.t_report
(      id              
     , log_report_type 
     , volume          
)
SELECT a.id              
     , a.log_report_type 
     , a.volume          
  FROM p1s3.t_report_01 a
;
INSERT INTO p1s4.t_server
(      id              
     , transit_server_type
)
SELECT a.id              
     , a.transit_server_type
  FROM p1s3.t_server_01 a
;
.open  '{k[p1s4]}'
attach '{k[zz1]}' as zz1;
DELETE FROM zz1.t_group WHERE group_name = 'p1s4_tables';
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_train' c2, c3
  FROM ( SELECT count(1) c3 FROM t_train );
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_test' c2, c3
  FROM ( SELECT count(1) c3 FROM t_test );
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_bband' c2, c3
  FROM ( SELECT count(1) c3 FROM t_bband );
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_outage' c2, c3
  FROM ( SELECT count(1) c3 FROM t_outage );
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_report' c2, c3
  FROM ( SELECT count(1) c3 FROM t_report );
INSERT INTO zz1.t_group (group_name,member_name,row_count)
SELECT 'p1s4_tables' c1, 't_server' c2, c3
  FROM ( SELECT count(1) c3 FROM t_server );
DELETE FROM zz1.s_group WHERE group_name = 'p1s4_db';
INSERT INTO zz1.s_group (group_name,member_name,row_count)
SELECT 'p1s4_db' c1, 'all_tables' c2, c3
  FROM (SELECT sum(row_count)  c3
          FROM zz1.t_group WHERE group_name = 'p1s4_tables');
.head on
.mode columns
SELECT group_name, member_name, row_count
  FROM zz1.t_group 
 WHERE group_name = 'p1s4_tables' ORDER BY id;
SELECT group_name, member_name, row_count
  FROM zz1.s_group 
 WHERE group_name = 'p1s4_db' ORDER BY id;
