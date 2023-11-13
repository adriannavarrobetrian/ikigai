
module "ecs" {
  source                    = "./ECS"
  vpc_id                    = var.vpc_id
  cluster_name              = var.cluster_name
  cluster_service_name      = var.cluster_service_name
  cluster_service_task_name = var.cluster_service_task_name
  vpc_id_subnet_list        = var.vpc_id_subnet_list
  execution_role_arn        = var.execution_role_arn
  image_id                  = var.image_id
}

