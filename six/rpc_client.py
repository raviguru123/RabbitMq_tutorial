import pika;
import sys;
import uuid

credentials=pika.PlainCredentials("guest","guest");
conn_param=pika.ConnectionParameters("localhost",credentials=credentials);
conn_broker=pika.BlockingConnection(conn_param);

channel=conn_broker.channel();

result=channel.queue_declare(exclusive=True);
queue_name=result.method.queue;

Response=False;

def callback(ch,method,properties,body):
    print("Response come from RPC server:",body);
    Response=True;

channel.basic_consume(callback,queue=queue_name);



def call(n):
    global Response;
    corr_id = str(uuid.uuid4())
    channel.basic_publish(exchange="",routing_key="rpc_queue"
    ,properties=pika.BasicProperties(
        reply_to=queue_name,
        correlation_id=corr_id
    ),
    body=str(n)
    );

    while(not Response):
        conn_broker.process_data_events();
    

call(sys.argv[1] or 5);