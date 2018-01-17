import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();
channel.queue_declare(queue="hello");

def callback(ch,method,properties,body):
    print("Received message:",body);

channel.basic_consume(callback,queue="hello",no_ack=True);
channel.start_consuming();