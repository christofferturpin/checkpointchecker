import boto3
import urllib.request
import datetime

# AWS S3 Configuration
S3_BUCKET = "checkpointsthismonth"
s3_client = boto3.client("s3")

def lambda_handler(event, context):
    # Get current year and month
    now = datetime.datetime.utcnow()
    year = now.strftime("%Y")
    month = now.strftime("%B").upper()  # e.g., "MARCH"

    # Construct PDF URL
    pdf_url = f"https://www.tn.gov/content/dam/tn/safety/documents/thp-checkpoints/{year}/{month}.pdf"
    s3_pdf_key = f"checkpoints_{month}.pdf"

    try:
        # Download the PDF
        with urllib.request.urlopen(pdf_url) as response:
            pdf_data = response.read()

        # Upload PDF to S3
        s3_client.put_object(
            Bucket=S3_BUCKET, 
            Key=s3_pdf_key, 
            Body=pdf_data, 
            ContentType="application/pdf"
        )

        return {
            "statusCode": 200,
            "body": f"PDF successfully stored in S3: s3://{S3_BUCKET}/{s3_pdf_key}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Failed to fetch PDF: {str(e)}"
        }
