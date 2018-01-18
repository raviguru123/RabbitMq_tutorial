import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();

result=channel.queue_declare(exclusive=True);
queue_name=result.method.queue;

channel.exchange_declare(exchange="direct_logs",exchange_type="direct");

severity= sys.argv[1] if len(sys.argv)>1 else "info";
message=sys.argv[2]  if(len(sys.argv)>2) else "default message";

channel.basic_publish(exchange="direct_logs",routing_key=severity,body=message);
conn_broker.close();