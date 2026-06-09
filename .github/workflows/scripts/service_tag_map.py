"""
Mapping of service identifiers to their corresponding Docker image environment variable names.

Keys:
    - "openedx": Open edX platform container
    - "mfe": Micro-frontend container
    - "aspects-superset": Superset-based reporting container

Values:
    Environment variable names used to specify Docker images for each service.
"""
service_tag_map = {
  "openedx": "DOCKER_IMAGE_OPENEDX",
  "mfe": "MFE_DOCKER_IMAGE",
  "aspects": "DOCKER_IMAGE_ASPECTS",
  "aspects-superset": "DOCKER_IMAGE_SUPERSET",
  "discovery": "DISCOVERY_DOCKER_IMAGE",
  "ecommerce": "ECOMMERCE_DOCKER_IMAGE",
  "ecommerce-worker": "ECOMMERCE_WORKER_DOCKER_IMAGE",
  "enterprise-catalog": "ENTERPRISE_CATALOG_DOCKER_IMAGE",
  "enterprise-catalog-worker": "ENTERPRISE_CATALOG_WORKER_DOCKER_IMAGE",
  "enterprise-access": "ENTERPRISE_ACCESS_DOCKER_IMAGE",
  "enterprise-access-worker": "ENTERPRISE_ACCESS_WORKER_DOCKER_IMAGE",
  "enterprise-subsidy": "ENTERPRISE_SUBSIDY_DOCKER_IMAGE",
  "license-manager": "LICENSE_MANAGER_DOCKER_IMAGE",
  "license-manager-worker": "LICENSE_MANAGER_WORKER_DOCKER_IMAGE",
  "license-manager-bulk-enrollment-worker": "LICENSE_MANAGER_BULK_ENROLLMENT_WORKER_DOCKER_IMAGE",
  "codejail": "CODEJAIL_DOCKER_IMAGE_V2",
  "codejail_apparmor": "CODEJAIL_APPARMOR_DOCKER_IMAGE",
}
