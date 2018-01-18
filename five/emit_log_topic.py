import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);


channel=conn_broker.channel();
result=channel.queue_declare(exclusive=True);
queue_name=result.method.queue;

channel.exchange_declare(exchange="topic_logs",exchange_type="topic");

severity=sys.argv[1] if(len(sys.argv)>2) else "info";
Message=''.join(sys.argv[2:]) or "Default message";

channel.basic_publish(exchange="topic_logs",body=Message,routing_key=severity);

conn_broker.close();
