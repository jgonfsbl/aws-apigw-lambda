# -*- coding: utf-8 -*-
""" Lambda Function for REST API """

from typing import TypeVar, Any

RespJSON = TypeVar('RespJSON', dict, str, None)
RespVar = TypeVar('RespVar', dict[str], dict[str, str], str, Any)


def run_get(uri, payload) -> str:
    """ get http verb """
    return uri


def run_post(uri, payload) -> str:
    """ post http verb """
    return payload


def run_put(uri, payload) -> str:
    """ put http verb """
    return payload


def respond(err, res=None) -> RespVar:
    """ Allow to respond to every lambda call """
    return {
        'statusCode': '400' if err else '200',
        'body': err.args[0] if err else res,
        'headers': {
            'Content-Type': 'application/json',
            'my_own_header': 'self_content',
        },
    }


def lambda_handler(event, context) -> RespJSON:
    """ Demonstrates a simple HTTP endpoint using API Gateway """

    operations = {
        'GET': run_get,
        'POST': run_post,
        'PUT': run_put
    }

    operation = event['httpMethod']

    if operation in operations:
        uri = event["requestContext"]["path"]
        payload = event["queryStringParameters"] if operation == 'GET' else event["body"]
        return respond(None, operations[operation](uri, payload))
    else:
        print(f'Error: {operation}')
        return respond(ValueError('Unsupported method "{}"'.format(operation)))


# -- ONLY VALID ON LOCAL DEVELOPMENT ------------------------------------------

def main() -> None:
    """ Main function """

    _my_event = {'resource': '/{proxy+}', 'path': '/proxy+', 'httpMethod': 'GET', 'headers': {'accept': '*/*', 'Host': 'ef6hjxjzv8.execute-api.us-east-1.amazonaws.com', 'User-Agent': 'curl/7.79.1', 'X-Amzn-Trace-Id': 'Root=1-630537b7-3e56090e5ccf1a7458ac2d41', 'X-Forwarded-For': '83.52.229.175', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https'}, 'multiValueHeaders': {'accept': ['*/*'], 'Host': ['ef6hjxjzv8.execute-api.us-east-1.amazonaws.com'], 'User-Agent': ['curl/7.79.1'], 'X-Amzn-Trace-Id': ['Root=1-630537b7-3e56090e5ccf1a7458ac2d41'], 'X-Forwarded-For': ['83.52.229.175'], 'X-Forwarded-Port': ['443'], 'X-Forwarded-Proto': ['https']}, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': {'proxy': 'proxy+'}, 'stageVariables': None, 'requestContext': {'resourceId': 'v5lp27', 'resourcePath': '/{proxy+}', 'httpMethod': 'PATCH', 'extendedRequestId': 'XVWkrEl2oAMF1Cg=', 'requestTime': '23/Aug/2022:20:25:27 +0000', 'path': '/v1/proxy+', 'accountId': '777973781667', 'protocol': 'HTTP/1.1', 'stage': 'v1', 'domainPrefix': 'ef6hjxjzv8', 'requestTimeEpoch': 1661286327334, 'requestId': '6b7abc4b-7694-4533-a0ae-33357d894b5d', 'identity': {'cognitoIdentityPoolId': None, 'accountId': None, 'cognitoIdentityId': None, 'caller': None, 'sourceIp': '83.52.229.175', 'principalOrgId': None, 'accessKey': None, 'cognitoAuthenticationType': None, 'cognitoAuthenticationProvider': None, 'userArn': None, 'userAgent': 'curl/7.79.1', 'user': None}, 'domainName': 'ef6hjxjzv8.execute-api.us-east-1.amazonaws.com', 'apiId': 'ef6hjxjzv8'}, 'body': None, 'isBase64Encoded': False}

#    _my_event = {"body":"eyJ0ZXN0IjoiYm9keSJ9","resource":"/{proxy+}","path":"/path/to/resource","httpMethod":"PUT","isBase64Encoded":True,"queryStringParameters":{"foo":"bar"},"multiValueQueryStringParameters":{"foo":["bar"]},"pathParameters":{"proxy":"/path/to/resource"},"stageVariables":{"baz":"qux"},"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"en-US,en;q=0.8","Cache-Control":"max-age=0","CloudFront-Forwarded-Proto":"https","CloudFront-Is-Desktop-Viewer":"true","CloudFront-Is-Mobile-Viewer":"false","CloudFront-Is-SmartTV-Viewer":"false","CloudFront-Is-Tablet-Viewer":"false","CloudFront-Viewer-Country":"US","Host":"1234567890.execute-api.us-east-1.amazonaws.com","Upgrade-Insecure-Requests":"1","User-Agent":"Custom User Agent String","Via":"1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)","X-Amz-Cf-Id":"cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==","X-Forwarded-For":"127.0.0.1, 127.0.0.2","X-Forwarded-Port":"443","X-Forwarded-Proto":"https"},"multiValueHeaders":{"Accept":["text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"],"Accept-Encoding":["gzip, deflate, sdch"],"Accept-Language":["en-US,en;q=0.8"],"Cache-Control":["max-age=0"],"CloudFront-Forwarded-Proto":["https"],"CloudFront-Is-Desktop-Viewer":["true"],"CloudFront-Is-Mobile-Viewer":["false"],"CloudFront-Is-SmartTV-Viewer":["false"],"CloudFront-Is-Tablet-Viewer":["false"],"CloudFront-Viewer-Country":["US"],"Host":["0123456789.execute-api.us-east-1.amazonaws.com"],"Upgrade-Insecure-Requests":["1"],"User-Agent":["Custom User Agent String"],"Via":["1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"],"X-Amz-Cf-Id":["cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="],"X-Forwarded-For":["127.0.0.1, 127.0.0.2"],"X-Forwarded-Port":["443"],"X-Forwarded-Proto":["https"]},"requestContext":{"accountId":"123456789012","resourceId":"123456","stage":"prod","requestId":"c6af9ac6-7b61-11e6-9a41-93e8deadbeef","requestTime":"09/Apr/2015:12:34:56 +0000","requestTimeEpoch":1428582896000,"identity":{"cognitoIdentityPoolId":"Null","accountId":"Null","cognitoIdentityId":"Null","caller":"Null","accessKey":"Null","sourceIp":"127.0.0.1","cognitoAuthenticationType":"Null","cognitoAuthenticationProvider":"Null","userArn":"Null","userAgent":"Custom User Agent String","user":"Null"},"path":"/prod/path/to/resource","resourcePath":"/{proxy+}","httpMethod":"POST","apiId":"1234567890","protocol":"HTTP/1.1"}}

    _my_context = {}
    res = lambda_handler(_my_event, _my_context)
    print(res)


if __name__ == '__main__':
    main()


