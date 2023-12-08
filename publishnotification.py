import boto3

# initialize the topic arn as blank
topic_arn = ""

# define a function that sends sns and takes in message and subject
def send_sns(message, subject):
    try:
        client = boto3.client("sns")
        result = client.publish(TopicArn = topic_arn, Message = message, Subject = subject)
        if result['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(result)
            print("Notification sent successfully!")
            return True
    except Exception as e:
        print("Error occurred while publish notificatins and error is :", e)
        return True
    
