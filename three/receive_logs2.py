import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);
channel=conn_broker.channel();

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue;

def callback(ch,method,property,body):
    print("message received:",body);
    
channel.queue_bind(exchange="logs",queue=queue_name);
channel.basic_consume(callback,queue=queue_name,no_ack=True);
channel.start_consuming();