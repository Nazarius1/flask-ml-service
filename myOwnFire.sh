#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "LSTAT":0.30,
   "RM":3,
   "PTRATIO":0.8,
   "INDUS":0.5
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
