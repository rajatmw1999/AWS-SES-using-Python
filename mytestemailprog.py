#IN ORDER TO USE AWS SES, BOTH THE RECEIVER AND SENDER EMAIL HAS TO BE VERIFIED WITH AWS SES.TO AVOID THIS, SES HAS TO BE MOVED OUT OF ITS SANDBOX.

#TO USE THIS MODULE, CHANGE THE boto3.client() CONFIGURATION WITH THE REGION NAME, AWS ACCESS KEY ID AND ACCESS SECRET ACCESS KEY.

import boto3
    
def sendEmail():
    ses = boto3.client('ses', region_name = 'us-east-2', 
                        aws_access_key_id = '#', 
                        aws_secret_access_key = '#')

    print("starting")
    #Mail Body Extraction
    subject= 'Using AWS SES'
    body = 'THIS IS THE BEST CODE EVER WRITTEN'
    
    destEmail =["rajatis1999@gmail.com"] 
    sourceEmail = 'rajat.upadhyay@live.com'

    #Sending E-mail
    ses.send_email(
    Source =sourceEmail,
    Destination = {
            'ToAddresses' : destEmail
    },
    Message = {
            'Subject' :{
            'Data':subject,
            'Charset' :'UTF-8'
        },
        'Body' :{
                'Html' :{
                'Data' : body,
                'Charset':'UTF-8'
            }
        }
    }
    )
    emailDetails.sendEmail()
    print('Mail sent')
        

sendEmail()



           
            



