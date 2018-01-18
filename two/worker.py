import pika;
import sys;
import time;


credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();
channel.queue_declare(queue="new_task");

def callback(ch,method,properties,body):
    print("Worker Received message:",body);
    time.sleep(body.count(b'.'));
    ch.basic_ack(delivery_tag=method.delivery_tag);

channel.basic_consume(callback,queue="new_task",no_ack=False);
channel.start_consuming();