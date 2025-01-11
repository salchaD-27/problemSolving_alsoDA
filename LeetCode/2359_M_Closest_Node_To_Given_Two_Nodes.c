#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int next(int* edges, int src) {
    return edges[src];
}

void calculateDistances(int* edges, int* dist, int startNode) {
    int currentNode = startNode;
    int distance = 0;
    while (currentNode != -1 && dist[currentNode] == INT_MAX) {
        dist[currentNode] = distance;
        currentNode = next(edges, currentNode);
        distance++;
    }
}

int closestMeetingNode(int* edges, int edgesSize, int node1, int node2) {
    int distFromNode1[edgesSize];
    int distFromNode2[edgesSize];
    for (int i = 0; i < edgesSize; i++) {
        distFromNode1[i] = distFromNode2[i] = INT_MAX;
    }
    calculateDistances(edges, distFromNode1, node1);
    calculateDistances(edges, distFromNode2, node2);
    
    int bestNode = -1;
    int minMaxDist = INT_MAX;
    for (int i = 0; i < edgesSize; i++) {
        if (distFromNode1[i] != INT_MAX && distFromNode2[i] != INT_MAX) {
            int maxDist = (distFromNode1[i] > distFromNode2[i]) ? distFromNode1[i] : distFromNode2[i];
            if (maxDist < minMaxDist) {
                minMaxDist = maxDist;
                bestNode = i;
            } else if (maxDist == minMaxDist && i < bestNode) {
                bestNode = i;
            }
        }
    }
    return bestNode;
}