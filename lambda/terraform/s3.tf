resource "aws_s3_bucket" "marketplace" {
  bucket = "marketplace.${var.domain_name}"
}

resource "aws_s3_bucket_ownership_controls" "s3_bucket_ownership_controls" {
  bucket = aws_s3_bucket.marketplace.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_public_access_block" "s3_bucket_public_access_block" {
  bucket = aws_s3_bucket.marketplace.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "example" {
  depends_on = [
    aws_s3_bucket_ownership_controls.s3_bucket_ownership_controls,
    aws_s3_bucket_public_access_block.s3_bucket_public_access_block,
  ]

  bucket = aws_s3_bucket.marketplace.id
  acl    = "public-read"
}



resource "aws_s3_bucket_website_configuration" "website_configuration" {
  bucket = aws_s3_bucket.marketplace.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}




resource "aws_s3_bucket_policy" "policy" {
  bucket = aws_s3_bucket.marketplace.id
  policy = <<POLICY
{
  "Id": "1",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": [
        "${aws_s3_bucket.marketplace.arn}/*"
      ],
      "Principal": "*"
    }
  ]
}
POLICY

  depends_on = [
    aws_s3_bucket.marketplace
  ]
}