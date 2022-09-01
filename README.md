# gcn-email

A hosted listener service to consume alerts from the GCN Kafka broker and send emails to users who subscribe through the new GCN site.

## Configuration

The following environment variables may be used to configure the service:

| Name                 | Value                                                                              |
| -------------------- | ---------------------------------------------------------------------------------- |
| `AWS_DEFAULT_REGION` | AWS region, e.g. `us-east-1`                                                       |
| `KAFKA_*`            | Kafka client configuration as understood by [Confluent Platform docker containers] |
| `EMAIL_SENDER`       | Address to be used as the sender for emails sent through SES                       |

## IAM Policy

The following is the minimum AWS IAM policy to grant the necessary permissions to this service. Replace `<region>` with the AWS region (e.g. `us-east-1`, `<account>` with the AWS account ID, and `<domain>` with the verified SES domain (e.g. `test.gcn.nasa.gov`.))

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ses:SendEmail",
                "ses:SendRawEmail"
            ],
            "Resource": "arn:aws:ses:<region>:<account>:identity/<domain>",
            "Effect": "Allow"
        },
        {
            "Action": [
                "ses:GetSendQuota"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "ssm:GetParameter"
            ],
            "Resource": "arn:aws:ssm:<region>:<account>:parameter/RemixGcnProduction/tables/email_notification_subscription",
            "Effect": "Allow"
        },
        {
            "Action": [
                "dynamodb:Query"
            ],
            "Resource": "arn:aws:dynamodb:<region>:<account>:table/RemixGcnProduction-EmailNotificationSubscriptionTable-*",
            "Effect": "Allow"
        }
    ]
}
```

[Confluent Platform docker containers]: https://docs.confluent.io/platform/current/installation/docker/config-reference.html
