import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();

result=channel.queue_declare(exclusive=True);
queue_name=result.method.queue;

channel.exchange_declare(exchange="direct_logs", exchange_type="direct");

severities=sys.argv[1:];

if(severities):
    for severity in severities:
        channel.queue_bind(exchange="direct_logs",queue=queue_name,routing_key=severity);

def callback(ch,method,property,body):
    print(" [x] %r:%r" % (method.routing_key, body))
    # print("Message received:",method.routing_key,body);



channel.basic_consume(callback,queue=queue_name,no_ack=True);
channel.start_consuming();