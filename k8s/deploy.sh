#!/bin/bash

echo "================================================"
echo "Deploying GreatKart Django App to Kubernetes"
echo "================================================"

# Color codes for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to check if kubectl is installed
check_kubectl() {
    if ! command -v kubectl &> /dev/null; then
        echo -e "${RED}Error: kubectl is not installed${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ kubectl is installed${NC}"
}

# Function to check cluster connection
check_cluster() {
    if ! kubectl cluster-info &> /dev/null; then
        echo -e "${RED}Error: Cannot connect to Kubernetes cluster${NC}"
        exit 1
    fi
    echo -e "${GREEN}✓ Connected to Kubernetes cluster${NC}"
}

# Function to apply Kubernetes manifests
apply_manifests() {
    echo -e "\n${YELLOW}Applying Kubernetes manifests...${NC}"
    
    kubectl apply -f 01-namespace.yaml
    echo -e "${GREEN}✓ Namespace created${NC}"
    
    kubectl apply -f 02-configmap.yaml
    echo -e "${GREEN}✓ ConfigMap created${NC}"
    
    kubectl apply -f 03-secret.yaml
    echo -e "${GREEN}✓ Secret created${NC}"
    
    kubectl apply -f 04-pvc.yaml
    echo -e "${GREEN}✓ PersistentVolumeClaims created${NC}"
    
    kubectl apply -f 05-deployment.yaml
    echo -e "${GREEN}✓ Deployment created${NC}"
    
    kubectl apply -f 06-service.yaml
    echo -e "${GREEN}✓ Service created${NC}"
    
    kubectl apply -f 07-ingress.yaml
    echo -e "${GREEN}✓ Ingress created${NC}"
    
    kubectl apply -f 08-hpa.yaml
    echo -e "${GREEN}✓ HorizontalPodAutoscaler created${NC}"
}

# Function to wait for deployment
wait_for_deployment() {
    echo -e "\n${YELLOW}Waiting for deployment to be ready...${NC}"
    kubectl wait --for=condition=available --timeout=300s deployment/django-app -n greatkart
    echo -e "${GREEN}✓ Deployment is ready${NC}"
}

# Function to display status
show_status() {
    echo -e "\n${YELLOW}Deployment Status:${NC}"
    kubectl get all -n greatkart
    
    echo -e "\n${YELLOW}Persistent Volume Claims:${NC}"
    kubectl get pvc -n greatkart
    
    echo -e "\n${YELLOW}Service Details:${NC}"
    kubectl get svc django-service -n greatkart
}

# Main execution
main() {
    check_kubectl
    check_cluster
    apply_manifests
    wait_for_deployment
    show_status
    
    echo -e "\n${GREEN}================================================${NC}"
    echo -e "${GREEN}Deployment completed successfully!${NC}"
    echo -e "${GREEN}================================================${NC}"
    echo -e "\nAccess your application:"
    echo -e "  - Via LoadBalancer: ${YELLOW}kubectl get svc django-service -n greatkart${NC}"
    echo -e "  - Via Port Forward: ${YELLOW}kubectl port-forward -n greatkart svc/django-service 8000:80${NC}"
    echo -e "  - Via Ingress: ${YELLOW}http://greatkart.local${NC} (add to /etc/hosts)"
}

# Run main function
main