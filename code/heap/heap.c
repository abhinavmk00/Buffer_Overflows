#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct User {
    char name[8];
    int is_admin;
};

struct User* global_user;

void set_username(char* input) {
    strcpy(global_user->name, input);
}

void print_user(struct User* user) {
    printf("User: %s\n", user->name);
    printf("Is admin: %d\n", user->is_admin);
}

int main() {
    global_user = (struct User*)malloc(sizeof(struct User));
    global_user->is_admin = 0;
    
    char input[100];
    printf("Enter username: ");
    scanf("%s", input);
    
    set_username(input);
    
    print_user(global_user);
    
    free(global_user);
    return 0;
}
