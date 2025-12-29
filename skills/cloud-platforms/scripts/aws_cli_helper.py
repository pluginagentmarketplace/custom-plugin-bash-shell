#!/usr/bin/env python3
"""AWS CLI command generator."""

COMMANDS = {
    "list_ec2": "aws ec2 describe-instances --query 'Reservations[].Instances[].[InstanceId,State.Name]'",
    "list_s3": "aws s3 ls",
    "list_rds": "aws rds describe-db-instances --query 'DBInstances[].[DBInstanceIdentifier,DBInstanceStatus]'",
}

def get_command(action: str) -> str:
    return COMMANDS.get(action, "Command not found")

if __name__ == "__main__":
    import sys
    print(get_command(sys.argv[1] if len(sys.argv) > 1 else "list_ec2"))
