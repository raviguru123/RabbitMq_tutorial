import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);
channel=conn_broker.channel();

channel.exchange_declare(exchange="logs", exchange_type="fanout");
message=''.join(sys.argv[1:]) or "Default log message";

channel.basic_publish(exchange="logs",routing_key="", body=message);
print("message send:",message);

conn_broker.close();