output "region" {
  value       = var.region
  description = "GCloud Region"
}

output "project_id" {
  value       = var.project_id
  description = "GCloud Project ID"
}

output "kubernetes_cluster_name" {
  value       = module.gke.name
  description = "GKE Cluster Name"
}

output "kubernetes_cluster_host" {
  value       = module.gke.endpoint
  description = "GKE Cluster Host"
  sensitive = true
}