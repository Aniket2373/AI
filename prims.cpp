#include <iostream>
#include <climits>
using namespace std;

int minKey(int key[], bool mstSet[], int V) {
    int min = INT_MAX;
    int min_index;

    for (int i = 0; i < V; i++) {
        if (mstSet[i] == false && key[i] < min) {
            min = key[i];
            min_index = i;
        }
    }
    return min_index;
}

void printMST(int parent[], int graph[5][5], int V) {
    cout << "Edge \tWeight\n";
    int totalWeight = 0;
    for (int i = 1; i < V; i++) {
        cout << parent[i] << " - " << i << " \t" << graph[i][parent[i]] << "\n";
        totalWeight += graph[i][parent[i]];
    }
    cout << "Total Minimum Weight of MST: " << totalWeight << "\n";
}

void primMST(int graph[5][5], int V) {
    int parent[V];
    int key[V];
    bool mstSet[V];

    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    int startNode;
    cout << "Enter the starting node (0 to " << V - 1 << "): ";
    cin >> startNode;

    key[startNode] = 0;
    parent[startNode] = -1;

    for (int count = 0; count < V - 1; count++) {
        int u = minKey(key, mstSet, V);
        mstSet[u] = true;

        for (int i = 0; i < V; i++) {
            if (graph[u][i] && mstSet[i] == false && graph[u][i] < key[i]) {
                parent[i] = u;
                key[i] = graph[u][i];
            }
        }
    }

    printMST(parent, graph, V);
}

int main() {
    int V = 5;
    int graph[5][5] = {
        {0, 3, 0, 0, 0},
        {3, 0, 6, 10, 2},
        {0, 6, 0, 0, 1},
        {0, 10, 0, 0, 4},
        {0, 2, 1, 4, 0}
    };

    primMST(graph, V);

    return 0;
}




// int main()
// {
//     int V=5;
//     // cout << "Enter the number of vertices: ";
//     // cin >> V;

//     // int graph[15][15];

//     int graph[5][5]={{0,3,0,0,0},
//                      {3,0,6,10,2},
//                      {0,6,0,0,1}, 
//                      {0,10,0,0,4},
//                      {0,2,1,4,0}};

//     // cout << "Enter the adjacency matrix for the graph:\n";
//     // for (int i = 0; i < V; i++)
//     // {
//     //     for (int j = i + 1; j < V; j++)
//     //     {
//     //         cout << "Enter the Edge between " << i << "-" << j << ": ";
//     //         cin >> graph[i][j];
//     //         graph[j][i] = graph[i][j];
//     //     }
//     // }

//     primMST(graph, V);

//     return 0;
// }