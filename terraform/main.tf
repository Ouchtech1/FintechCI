provider "aws" {
  region = var.aws_region
}

resource "aws_ecs_cluster" "cluster" {
  name = "fintech-cluster"
}

# Autres ressources AWS nécessaires, comme les définitions de tâches, les services ECS, les rôles IAM, etc.
