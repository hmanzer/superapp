terraform {
  backend "gcs" {
    credentials = "~/terraform-gkecluster-superapp-keyfile.json"
    bucket      = "superapp-hm"
    prefix      = "terraform/state"
  }
}