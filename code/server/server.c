// Compile with: gcc -fno-stack-protector -z execstack -o vuln_server vuln_server.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 4444
#define BUFFER_SIZE 64

void handle_connection(int client_sock) {
    char buffer[BUFFER_SIZE];
    
    // Clear the buffer
    memset(buffer, 0, BUFFER_SIZE);
    
    // Vulnerable function - no bounds checking
    printf("Waiting for input...\n");
    read(client_sock, buffer, 256);  // Intentionally reads more than buffer size
    
    // Echo back input
    printf("Received: %s\n", buffer);
    write(client_sock, "Received your input!\n", 20);
}

int main() {
    int server_sock, client_sock;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    
    // Create socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        perror("Socket creation failed");
        exit(1);
    }
    
    // Configure socket
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);
    
    // Bind socket
    if (bind(server_sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(1);
    }
    
    // Listen for connections
    if (listen(server_sock, 5) < 0) {
        perror("Listen failed");
        exit(1);
    }
    
    printf("Server listening on port %d...\n", PORT);
    
    while(1) {
        // Accept connection
        client_sock = accept(server_sock, (struct sockaddr*)&client_addr, &client_len);
        if (client_sock < 0) {
            perror("Accept failed");
            continue;
        }
        
        printf("New connection accepted\n");
        handle_connection(client_sock);
        close(client_sock);
    }
    
    close(server_sock);
    return 0;
}
