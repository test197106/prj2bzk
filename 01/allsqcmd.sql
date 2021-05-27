
.open '{k[db0]}'
.databases
.mode csv
.import '{sv_01}' {sv_02}_{sv_03:02d}
.open '{k[zz1]}'
.header on
.tables
CREATE TABLE table_groups
(  id           	INTEGER PRIMARY KEY AUTOINCREMENT
,  group_name		VARCHAR(255)
,  table_name		VARCHAR(255)
,  row_count		INTEGER
--
,  status		VARCHAR(255)
,  udc_int		INTEGER
,  udc_flt		FLOAT
--
,  udc_var		VARCHAR(255)
,  udc_txt		TEXT
);
SELECT 'Table table_groups created in zz1 database' info;
SELECT * FROM table_groups WHERE group_name = 'db0_tables';
DELETE   FROM table_groups WHERE group_name = 'db0_tables';
SELECT * FROM table_groups WHERE group_name = 'db0_tables';
.open  '{k[db0]}'
attach '{k[zz1]}' as zz1;
INSERT INTO zz1.table_groups (group_name,table_name,row_count)
SELECT 'db0_tables' col_01, '{sv_02}_{sv_03:02}' col_02, col_03
  FROM ( SELECT count(1) col_03 FROM {sv_02}_{sv_03:02} );
.open '{k[zz1]}'
.head on
.mode columns
DELETE FROM table_groups WHERE group_name = 'db0_tables'
   AND table_name = 'all_tables';
INSERT INTO table_groups (group_name,table_name,row_count)
SELECT 'db0_tables' col_01, 'all_tables' col_02, col_03
  FROM (SELECT sum(row_count)  col_03
          FROM table_groups WHERE group_name = 'db0_tables');
SELECT group_name, table_name, row_count
  FROM table_groups 
 WHERE group_name = 'db0_tables' ORDER BY id;
