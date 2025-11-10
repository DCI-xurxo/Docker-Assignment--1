# AWS CloudFormation 3-Tier Architecture

## Project Overview
This project implements a simple 3-tier AWS architecture using CloudFormation with Infrastructure as Code (IaC) principles. The architecture includes:
- **Public Tier**: EC2 instance with internet access
- **Private Tier**: RDS MySQL database and S3 bucket
- **Network Layer**: VPC with public and private subnets

## Architecture Components

### Network Infrastructure
- **VPC**: Custom VPC with CIDR block `10.0.0.0/16`
- **Public Subnet**: `10.0.1.0/24` for EC2 instance
- **Private Subnets**: `10.0.2.0/24` and `10.0.3.0/24` for RDS and S3
- **Internet Gateway**: Provides internet access to public subnet
- **Route Tables**: Configured for public subnet internet routing

### Compute Resources
- **EC2 Instance**: 
  - Type: `t2.micro` (free tier eligible)
  - Location: Public subnet
  - Access: SSH (port 22) and HTTP (port 80)
  - Dynamic naming using environment type

### Database Resources
- **RDS MySQL Instance**:
  - Engine: MySQL 8.0.35
  - Instance class: `db.t3.micro`
  - Location: Private subnet
  - Access: Only from EC2 security group (port 3306)

### Storage Resources
- **S3 Bucket**:
  - Private access only
  - Name: `{StackName}-bucket-{AccountId}`
  - Fully encrypted with blocked public access

## Prerequisites

Before deploying this stack, ensure you have:

1. **AWS Account** with appropriate permissions
2. **AWS CLI** installed and configured
3. **EC2 Key Pair** created in your target region
4. **IAM Permissions** to create:
   - VPC and networking resources
   - EC2 instances
   - RDS databases
   - S3 buckets

## Deployment Instructions

### Step 1: Prepare Parameters

You'll need to provide the following parameters:
- `KeyName`: Name of your existing EC2 key pair
- `EnvironmentType`: Either `dev` or `prod` (default: `dev`)
- `DBName`: Database name (default: `myappdatabase`)
- `DBUser`: Database username (default: `admin`)
- `DBPassword`: Database password (minimum 8 characters)

### Step 2: Deploy via AWS Console

1. Log into the **AWS Console**
2. Navigate to **CloudFormation** service
3. Click **Create stack** → **With new resources**
4. Select **Upload a template file**
5. Upload the `template.yml` file
6. Click **Next**
7. Enter a **Stack name** (e.g., `my-3tier-stack`)
8. Fill in the parameters:
   - KeyName: Select your EC2 key pair
   - EnvironmentType: Choose `dev` or `prod`
   - DBName: Enter database name
   - DBUser: Enter database username
   - DBPassword: Enter secure password (8-41 characters, alphanumeric)
9. Click **Next** through the options
10. Review and click **Create stack**

### Step 3: Deploy via AWS CLI

```bash
aws cloudformation create-stack \
  --stack-name my-3tier-stack \
  --template-body file://template.yml \
  --parameters \
    ParameterKey=KeyName,ParameterValue=your-key-name \
    ParameterKey=EnvironmentType,ParameterValue=dev \
    ParameterKey=DBName,ParameterValue=myappdatabase \
    ParameterKey=DBUser,ParameterValue=admin \
    ParameterKey=DBPassword,ParameterValue=YourSecurePassword123 \
  --capabilities CAPABILITY_IAM
```

### Step 4: Monitor Deployment

Monitor the stack creation:
```bash
aws cloudformation describe-stacks --stack-name my-3tier-stack
```

Wait for status to change to `CREATE_COMPLETE` (typically 10-15 minutes due to RDS creation).

## Stack Update Task

To update the environment type from `dev` to `prod`:

### Via AWS Console:
1. Select your stack in CloudFormation
2. Click **Update**
3. Choose **Use current template**
4. Change `EnvironmentType` parameter to `prod`
5. Click **Next** through options
6. Review and click **Update stack**
7. Wait for `UPDATE_COMPLETE` status
8. Check **Outputs** tab to verify changes
9. Navigate to EC2 console to verify instance name changed to `MyInstance-prod`

### Via AWS CLI:
```bash
aws cloudformation update-stack \
  --stack-name my-3tier-stack \
  --use-previous-template \
  --parameters \
    ParameterKey=KeyName,UsePreviousValue=true \
    ParameterKey=EnvironmentType,ParameterValue=prod \
    ParameterKey=DBName,UsePreviousValue=true \
    ParameterKey=DBUser,UsePreviousValue=true \
    ParameterKey=DBPassword,UsePreviousValue=true
```

## CloudFormation Outputs

After successful deployment, the stack provides these outputs:

| Output | Description | Usage |
|--------|-------------|-------|
| `VPCId` | VPC identifier | Reference for other resources |
| `EC2InstanceId` | EC2 instance ID | Connect via SSH or manage instance |
| `EC2PublicIP` | Public IP address | SSH access: `ssh -i key.pem ec2-user@<IP>` |
| `S3BucketName` | S3 bucket name | Store application data |
| `RDSEndpoint` | RDS database endpoint | Database connection string |

## Accessing Resources

### Connect to EC2 Instance:
```bash
ssh -i /path/to/your-key.pem ec2-user@<EC2PublicIP>
```

### Connect to RDS Database from EC2:
```bash
mysql -h <RDSEndpoint> -u admin -p
```

### Access S3 Bucket:
```bash
aws s3 ls s3://<S3BucketName>
```

## Security Considerations

✅ **Best Practices Implemented:**
- RDS database in private subnet (no public access)
- S3 bucket with public access blocked
- Security groups with minimal required access
- Passwords marked as `NoEcho` (not visible in console)

⚠️ **Production Recommendations:**
- Use AWS Secrets Manager for database credentials
- Implement VPC endpoints for S3 access
- Enable encryption at rest for RDS and S3
- Use AWS Systems Manager Session Manager instead of SSH
- Implement CloudWatch monitoring and alarms
- Add NAT Gateway for private subnet internet access (if needed)
- Use AWS Certificate Manager for HTTPS

## Troubleshooting

### Common Issues:

**Stack creation fails with "Key pair does not exist"**
- Verify the key pair exists in the correct region
- Ensure the key name is spelled correctly

**RDS creation timeout**
- RDS typically takes 10-15 minutes to create
- Wait for completion before troubleshooting

**Cannot connect to EC2 instance**
- Verify security group allows SSH from your IP
- Ensure you're using the correct key pair
- Check that instance has a public IP assigned

**S3 bucket name already exists**
- S3 bucket names must be globally unique
- CloudFormation adds account ID to make it unique
- If still fails, change the stack name

## Cost Estimation

Approximate monthly costs (us-east-1 region):
- EC2 t2.micro: ~$8.50/month (free tier: 750 hours/month)
- RDS db.t3.micro: ~$15/month (free tier: 750 hours/month)
- S3 Standard: $0.023/GB (free tier: 5GB)
- Data transfer: Variable based on usage

**Total estimated**: ~$24/month (without free tier)

## Cleanup

To delete all resources and avoid charges:

### Via AWS Console:
1. Navigate to CloudFormation
2. Select your stack
3. Click **Delete**
4. Confirm deletion

### Via AWS CLI:
```bash
aws cloudformation delete-stack --stack-name my-3tier-stack
```

**Note**: Empty the S3 bucket before deleting the stack if it contains data.

## Project Files

- `template.yml` - CloudFormation template
- `architecture_diagram.png` - Visual architecture diagram
- `README.md` - This documentation file

## Template Features

This template demonstrates the following CloudFormation features:

- **Parameters**: Input validation and constraints
- **Intrinsic Functions**:
  - `!Ref`: Reference parameters and resources
  - `!Sub`: String substitution for dynamic naming
  - `!GetAtt`: Retrieve resource attributes
  - `!Select` + `!GetAZs`: Dynamic availability zone selection
- **Outputs**: Export values for cross-stack references
- **Dependencies**: Proper resource creation order
- **Tags**: Resource organization and cost tracking

## Additional Resources

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)

## License

This project is provided as-is for educational purposes.

## Author

Created as part of AWS CloudFormation learning exercise.

---

**Last Updated**: November 2025
