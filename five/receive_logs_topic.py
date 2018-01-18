import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();

result=channel.queue_declare(exclusive=True);
queue_name=result.method.queue;

channel.exchange_declare(exchange="topic_logs",exchange_type="topic");

binding_keys=sys.argv[1:];

def callback(ch,method,property,body):
    print("Received message:",body);

for key in binding_keys:
    channel.queue_bind(exchange="topic_logs",queue=queue_name,routing_key=key);

channel.basic_consume(callback,queue=queue_name,no_ack=True);

channel.start_consuming();
