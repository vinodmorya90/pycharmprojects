import datetime
import boto3
import os

sns = boto3.client('sns')
iam = boto3.client('iam')

filePath = 'C:/Users/vinod\Documents/New folder/iam.txt'
# As file at filePath is deleted now, so we should check if file exists or not not before deleting them
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")

for user in iam.list_users()['Users']:
    a = "User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(user['UserName'], user['UserId'], user['Arn'],
                                                                    user['CreateDate'])
    key_created_date = datetime.date(user['CreateDate'].year, user['CreateDate'].month, user['CreateDate'].day)
    today_date = datetime.date.today()
    age_in_number_of_days = (today_date - key_created_date).days

    file = open(filePath, 'a')
    if age_in_number_of_days > 25:
        file.write(a)
        file.write("the total age of credentials in days is :" + str(age_in_number_of_days))
        file.write("\n========================================================================\n\n")
        file.close()


response = sns.publish(
    TopicArn='arn:aws:sns:ap-southeast-1:872599169723:mymail',
    Message='some credentials 90 days or more  older, please check the file having user details and its age at location'
            ' C:/Users/vinod\Documents/New folder/iam.txt',
)

print(response)














