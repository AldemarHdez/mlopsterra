resource "aws_iam_role" "sagemaker_role" {
  name = "sagemaker_execution_role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "sagemaker_policy_attachment" {
  role       = aws_iam_role.sagemaker_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
}

resource "aws_sagemaker_model" "sagemaker_model" {
  name           = "iris-model"
  execution_role_arn = aws_iam_role.sagemaker_role.arn

  primary_container {
    image = "382416733822.dkr.ecr.us-west-2.amazonaws.com/tensorflow-inference:2.3.0-cpu"
    model_data_url = "s3://your-bucket/iris_model/model.tar.gz"
  }
}
