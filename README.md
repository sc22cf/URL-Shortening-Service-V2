# URL Shortener Service (Version 2)

---

## Overview
This is the second version of the URL shortener service, redesigned to enhance scalability and performance by integrating **Redis** for caching and **Cassandra** for persistent data storage. Additionally, **Docker Swarm** is utilized for clustering and orchestrating lab machines, ensuring efficient resource management and high availability.

---

## Key Features
1. **Redis Integration**:
   - Acts as a high-speed in-memory cache to store URL mappings.
   - Reduces database load by quickly serving frequently requested URLs.
   - Configured with a master-worker (replica) setup for redundancy and fault tolerance.

2. **Cassandra Integration**:
   - Provides distributed and fault-tolerant persistent storage for URL mappings.
   - Handles large-scale data with its linear scalability.
   - Ensures high write performance and strong consistency.

3. **Docker Swarm**:
   - Orchestrates the deployment of services across multiple lab machines.
   - Enables clustering for both Redis and Cassandra to distribute workload.
   - Provides fault tolerance and automated failover for seamless operations.
---

## Setup Instructions
Please read the report.pdf for explanation of the system architecture and design choices
