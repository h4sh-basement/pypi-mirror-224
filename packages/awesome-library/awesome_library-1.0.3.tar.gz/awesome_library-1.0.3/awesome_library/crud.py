import boto3
import pandas as pd


class DynamodbCrud:

    def __init__(
            self,
            endpoint_url: str,
            region_name: str,
            aws_access_key_id: str,
            aws_secret_access_key: str
    ) -> None:
        self.dynamodb = boto3.resource(
            "dynamodb",
            endpoint_url=endpoint_url,
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def create_entry(self, table_name: str, content: list[dict]) -> None:
        table = self.dynamodb.Table(table_name)
        content_without_key = [{key: value for key, value in issue.items() if key != "key"} for issue in content]

        with table.batch_writer() as batch:
            for index, issue in enumerate(content):
                item = {"Id": content[index]["key"], **content_without_key[index]}
                batch.put_item(
                    Item=item
                )
                print(f"Successfully inserted {item}")

    def read_data(self, table_name):
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)["Items"]

        df = pd.DataFrame(scan_response)

        return df

    def update_data(self, table_name, content):
        table = self.dynamodb.Table(table_name)
        for commit_id, commit_hash in content.items():
            table.update_item(
                Key={'Id': commit_id},
                UpdateExpression='SET commit_hash = :val',
                ExpressionAttributeValues={':val': commit_hash}
            )
        print("Successfully updated DB")

    def delete_entry(self):
        pass

    def convert_to_csv(self, table_name):
        table = self.dynamodb.Table(table_name)
        scan_response = table.scan(TableName=table_name)["Items"]

        df = pd.DataFrame(scan_response)
        csv_name = "data.csv"
        df.to_csv(csv_name)

        print(f"Created {csv_name}")
