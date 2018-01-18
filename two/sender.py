import pika;
import sys;

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();
channel.queue_declare(queue="new_task");

message=''.join(sys.argv[1:]) or "Hello this is default message please enter message after command";

channel.basic_publish(exchange='', routing_key="new_task",body=message,properties=pika.BasicProperties(
    delivery_mode=2,
    )
    ,
    );




conn_broker.close();