 Data Collection: Lambda + S3 + CloudFront + EventBridge

Each month, Tennessee PD releases checkpoint info as PDFs. I set up an AWS Lambda function triggered by a monthly EventBridge cron job to grab these PDFs and toss them into an S3 bucket. The function also cleans up older PDFs, keeping the storage neat.

In my previous project ( https://www.rejectedvanityplates.com ) I got some feed back about directly hitting s3 buckets for relatively static data. So I set up a CF CDN in front of the bucket this time which the Lambda actually hits. The same is true of the site itself.

Hosting the Site: S3 + CloudFront + Route 53

The front end itself is a simple static website sitting in another S3 bucket, delivered via CloudFront CDN. For security, I implemented Origin Access Control, so only CloudFront can reach the bucket directly. Route 53 handles DNS.

WAF is set up to protect CloudFront from the usual suspects.

A Better Solution if I was Going to do this Again.

Honestly, parsing the PDFs into structured HTML with Lambda and directly updating the S3 bucket with static HTML monthly would’ve been even more performant. But hey, I mainly did this to practice data scraping with AWS, and it only took an evening to slap it all together.
Framework Check

The PDFs are only a few MB in size, but the architecture should be able to handle much bigger datasets. From the Well-Architected Framework, I tried to achieve.

    Operational Excellence: Automation via Lambda and EventBridge.

    Security: Using OAC and WAF.

    Reliability: Cloudfront for high avail.

    Performance Efficiency: Caching strategy.

    Cost Optimization: Reduced direct S3 access.
