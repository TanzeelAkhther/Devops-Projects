#!/bin/bash
# Filename: test.sh
# Purpose: Start Docker Compose, create users & orders, show outputs, API Gateway logs

# Step 1: Build and start Docker Compose services
echo "=== Starting Docker Compose ==="
docker compose down -v   # Stop and remove old containers & volumes
docker compose up -d --build

# Step 2: Wait for services to be ready
echo "=== Waiting 10 seconds for services to start ==="
sleep 10

# Step 3: Create users
echo "=== Creating Users ==="

USER1=$(curl -s -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Tanzeel","email":"tanzeel@example.com"}')
echo "User1 created: $USER1"

USER2=$(curl -s -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}')
echo "User2 created: $USER2"

# Step 4: Get user by ID
echo "=== Fetching Users ==="
curl -s http://localhost:5000/users/1 | jq .
curl -s http://localhost:5000/users/2 | jq .

# Step 5: Create multiple orders
echo "=== Creating Orders ==="

ORDER1=$(curl -s -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{"item":"Laptop","quantity":1}')
echo "Order1 created: $ORDER1"

ORDER2=$(curl -s -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{"item":"Mouse","quantity":3}')
echo "Order2 created: $ORDER2"

ORDER3=$(curl -s -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{"item":"Keyboard","quantity":2}')
echo "Order3 created: $ORDER3"

# Step 6: Fetch orders
echo "=== Fetching Orders ==="
curl -s http://localhost:5000/orders/1 | jq .
curl -s http://localhost:5000/orders/2 | jq .
curl -s http://localhost:5000/orders/3 | jq .

# Step 7: Show API Gateway logs
echo "=== API Gateway Logs ==="
docker logs api_gateway --tail 6

