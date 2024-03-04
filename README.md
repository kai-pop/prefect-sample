gcloud compute ssh instance-1 --zone=us-west1-a --tunnel-through-iap --ssh-flag="-A -L 80:%INSTANCE%:80


prefect work-pool create --type cloud-run cloud-run-work-pool

prefect worker start --pool "cloud-run-work-pool" 

prefect init --recipe docker

prefect deploy --name weather-deployment

prefect worker start --pool "cloud-run-work-pool"y
