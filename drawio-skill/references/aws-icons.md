# AWS 图标与服务名

## 1. 基本规则

- 优先使用 `mxgraph.aws4.*`
- 架构图中的 AWS 元素尽量使用官方图标，而不是普通矩形
- 分组容器优先用 `group`
- 单个服务节点优先用 `resourceIcon`
- 需要更像产品卡片时再考虑 `productIcon`

## 2. 常用样式模板

### 2.1 资源图标

```text
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;
```

### 2.2 产品图标

```text
shape=mxgraph.aws4.productIcon;prIcon=mxgraph.aws4.lambda;
```

### 2.3 分组容器

```text
shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc;
```

## 3. 常用图标清单

| 服务/容器 | 图标 | style key |
|-----------|------|-----------|
| AWS Cloud | mxgraph.aws4.group_aws_cloud_alt | group |
| Amazon VPC | mxgraph.aws4.group_vpc | group |
| Security Group | mxgraph.aws4.group_security_group | group |
| Auto Scaling Group | mxgraph.aws4.group_auto_scaling | group |
| Amazon EC2 | mxgraph.aws4.ec2 | resourceIcon |
| EC2 Instance | mxgraph.aws4.instance2 | resourceIcon |
| Elastic IP Address | mxgraph.aws4.elastic_ip_address | resourceIcon |
| Auto Scaling | mxgraph.aws4.auto_scaling2 | resourceIcon |
| AWS Lambda | mxgraph.aws4.lambda | resourceIcon |
| Lambda Function | mxgraph.aws4.lambda_function | resourceIcon |
| AWS App Runner | mxgraph.aws4.app_runner | resourceIcon |
| AWS Elastic Beanstalk | mxgraph.aws4.elastic_beanstalk | resourceIcon |
| Amazon ECS | mxgraph.aws4.ecs | resourceIcon |
| ECS Task | mxgraph.aws4.ecs_task | resourceIcon |
| Amazon EKS | mxgraph.aws4.eks | resourceIcon |
| AWS Fargate | mxgraph.aws4.fargate | resourceIcon |
| Amazon ECR | mxgraph.aws4.ecr | resourceIcon |
| Amazon S3 | mxgraph.aws4.s3 | resourceIcon |
| S3 Bucket | mxgraph.aws4.bucket | resourceIcon |
| S3 Object | mxgraph.aws4.object | resourceIcon |
| Amazon EFS | mxgraph.aws4.efs | resourceIcon |
| Amazon EBS | mxgraph.aws4.ebs | resourceIcon |
| Amazon FSx | mxgraph.aws4.fsx | resourceIcon |
| Amazon RDS | mxgraph.aws4.rds | resourceIcon |
| RDS DB Instance | mxgraph.aws4.db_instance | resourceIcon |
| Amazon Aurora | mxgraph.aws4.aurora | resourceIcon |
| Amazon DynamoDB | mxgraph.aws4.dynamodb | resourceIcon |
| Amazon ElastiCache | mxgraph.aws4.elasticache | resourceIcon |
| Amazon Redshift | mxgraph.aws4.redshift | resourceIcon |
| Generic Database | mxgraph.aws4.database | resourceIcon |
| Internet | mxgraph.aws4.internet | resourceIcon |
| Elastic Load Balancing | mxgraph.aws4.elastic_load_balancing | resourceIcon |
| Application Load Balancer | mxgraph.aws4.application_load_balancer | resourceIcon |
| Network Load Balancer | mxgraph.aws4.network_load_balancer | resourceIcon |
| Amazon API Gateway | mxgraph.aws4.api_gateway | resourceIcon |
| Amazon Route 53 | mxgraph.aws4.route_53 | resourceIcon |
| Amazon CloudFront | mxgraph.aws4.cloudfront | resourceIcon |
| Amazon VPC | mxgraph.aws4.vpc | resourceIcon |
| Internet Gateway | mxgraph.aws4.internet_gateway | resourceIcon |
| NAT Gateway | mxgraph.aws4.nat_gateway | resourceIcon |
| VPC Endpoint | mxgraph.aws4.endpoints | resourceIcon |
| AWS Transit Gateway | mxgraph.aws4.transit_gateway | resourceIcon |
| AWS IAM | mxgraph.aws4.identity_and_access_management | resourceIcon |
| Amazon Cognito | mxgraph.aws4.cognito | resourceIcon |
| AWS WAF | mxgraph.aws4.waf | resourceIcon |
| AWS KMS | mxgraph.aws4.key_management_service | resourceIcon |
| AWS Secrets Manager | mxgraph.aws4.secrets_manager | resourceIcon |
| AWS Certificate Manager | mxgraph.aws4.certificate_manager | resourceIcon |
| Amazon SQS | mxgraph.aws4.sqs | resourceIcon |
| SQS Queue | mxgraph.aws4.queue | resourceIcon |
| Amazon SNS | mxgraph.aws4.sns | resourceIcon |
| Amazon EventBridge | mxgraph.aws4.eventbridge | resourceIcon |
| AWS Step Functions | mxgraph.aws4.step_functions | resourceIcon |
| Amazon CloudWatch | mxgraph.aws4.cloudwatch | resourceIcon |
| AWS CloudTrail | mxgraph.aws4.cloudtrail | resourceIcon |
| AWS Config | mxgraph.aws4.config | resourceIcon |
| Amazon OpenSearch Service | mxgraph.aws4.opensearch | resourceIcon |
| Amazon Athena | mxgraph.aws4.athena | resourceIcon |
| AWS Glue | mxgraph.aws4.glue | resourceIcon |
| Amazon Kinesis | mxgraph.aws4.kinesis | resourceIcon |
| Amazon QuickSight | mxgraph.aws4.quicksight | resourceIcon |
| Users | mxgraph.aws4.users | resourceIcon |

## 4. 服务名写法

推荐写正式名称或广泛接受的简称：

- `Amazon ECS`
- `Amazon S3`
- `Amazon RDS`
- `AWS Lambda`
- `AWS IAM`

如果图里空间非常有限，可以在标题简化，但最好让图例或上下文里保持可辨识。

## 5. 搜索方式

用脚本按服务名或 icon key 搜索：

```bash
python scripts/find_aws_icon.py lambda
python scripts/find_aws_icon.py route_53
python scripts/find_aws_icon.py security
```
