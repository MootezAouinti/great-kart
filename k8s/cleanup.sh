#!/bin/bash

echo "================================================"
echo "Cleaning up GreatKart Kubernetes Resources"
echo "================================================"

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${YELLOW}This will delete all GreatKart resources from Kubernetes${NC}"
read -p "Are you sure? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo -e "${GREEN}Cleanup cancelled${NC}"
    exit 0
fi

echo -e "\n${YELLOW}Deleting resources...${NC}"

kubectl delete -f 08-hpa.yaml 2>/dev/null
echo -e "${GREEN}✓ HPA deleted${NC}"

kubectl delete -f 07-ingress.yaml 2>/dev/null
echo -e "${GREEN}✓ Ingress deleted${NC}"

kubectl delete -f 06-service.yaml 2>/dev/null
echo -e "${GREEN}✓ Service deleted${NC}"

kubectl delete -f 05-deployment.yaml 2>/dev/null
echo -e "${GREEN}✓ Deployment deleted${NC}"

kubectl delete -f 04-pvc.yaml 2>/dev/null
echo -e "${GREEN}✓ PVCs deleted${NC}"

kubectl delete -f 03-secret.yaml 2>/dev/null
echo -e "${GREEN}✓ Secret deleted${NC}"

kubectl delete -f 02-configmap.yaml 2>/dev/null
echo -e "${GREEN}✓ ConfigMap deleted${NC}"

kubectl delete -f 01-namespace.yaml 2>/dev/null
echo -e "${GREEN}✓ Namespace deleted${NC}"

echo -e "\n${GREEN}================================================${NC}"
echo -e "${GREEN}Cleanup completed!${NC}"
echo -e "${GREEN}================================================${NC}"