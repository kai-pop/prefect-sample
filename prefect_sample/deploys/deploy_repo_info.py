from prefect import flow
from prefect_sample.repo_info import get_repo_info
from prefect.deployments.deployments import Deployment
if __name__ == "__main__":
    get_repo_info.deploy(
        name="",
        work_pool_name="",
        
    )
    Deployment.build_from_flow()
