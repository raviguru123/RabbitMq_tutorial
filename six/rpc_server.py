import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();

channel.queue_declare(queue="rpc_queue");

def fib(num):
    if(num==0 or num==1):
        return num;
    return fib(num-1)+fib(num-1);

def callback(ch,method,property,body):
    print("Request for:",body);
    num=fib(int(body));


    ch.basic_publish(exchange="",
    routing_key=property.reply_to,
    properties=pika.BasicProperties(correlation_id=property.correlation_id),
    body=str(num));

    ch.basic_ack(delivery_tag=method.delivery_tag);
    


channel.basic_qos(prefetch_count=1);
channel.basic_consume(callback,queue="rpc_queue");
print("waiting for RPC call.....");
channel.start_consuming();
