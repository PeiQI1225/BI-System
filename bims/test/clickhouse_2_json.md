clickhouse-client -h 127.0.0.1 --database="dbup" --query="select * form db.test_table" --format CSVWithNames> test.json(带表头）

clickhouse（导入为csv格式）
clickhouse-client -h 127.0.0.1 --database="dbup" --query="insert into db.test_table FORMAT CSV" < test.csv （不带表头）
clickhouse-client -h 127.0.0.1 --database="dbup" --query="insert into db.test_table" --format CSVWithNames < test.csv(带表头）

clickhouse（导入为json格式）
clickhouse-client -h 127.0.0.1 --database="dbup" --query="insert into db.test_table" --format CSVWithNames < test.json(带表头）
